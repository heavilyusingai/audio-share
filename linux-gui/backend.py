"""Validation and subprocess management for the Linux desktop frontend."""

import ipaddress
import json
import os
from pathlib import Path
import re
import shutil
import signal
import subprocess
import threading

DEFAULT_PORT = 65530
ENDPOINT_RE = re.compile(r"^\s*([* ])\s+id:\s*(\S+)\s+name:\s*(.+)$")


def find_server():
    """Prefer an explicit binary, then a neighboring unpacked/build binary, then PATH."""
    explicit = os.environ.get("AUDIO_SHARE_SERVER")
    if explicit:
        path = Path(explicit).expanduser()
        if not path.is_file() or not os.access(path, os.X_OK):
            raise FileNotFoundError(f"AUDIO_SHARE_SERVER is not executable: {path}")
        return str(path.resolve())
    root = Path(__file__).resolve().parent.parent
    for path in (root / "as-cmd", root / "bin/as-cmd",
                 root / "server-core/out/install/linux-Release/bin/as-cmd",
                 root / "server-core/out/install/linux-system-Release/bin/as-cmd"):
        if path.is_file() and os.access(path, os.X_OK):
            return str(path)
    result = shutil.which("as-cmd")
    if not result:
        raise FileNotFoundError("as-cmd not found. Install/build the server or set AUDIO_SHARE_SERVER to its path.")
    return result


def local_address():
    """Choose a LAN address on an active interface, without relying on an Internet route."""
    try:
        output = subprocess.run(["ip", "-j", "-4", "address", "show", "up"],
                                capture_output=True, text=True, timeout=3, check=True)
        addresses = [info["local"] for iface in json.loads(output.stdout)
                     if iface.get("link_type") != "loopback"
                     for info in iface.get("addr_info", []) if info.get("family") == "inet"]
        return next((a for a in addresses if ipaddress.ip_address(a).is_private),
                    addresses[0] if addresses else "")
    except (OSError, subprocess.SubprocessError, ValueError, KeyError, TypeError):
        return ""


def parse_endpoints(output):
    """Return (id, display name, is_default) tuples from as-cmd -l output."""
    endpoints = []
    for line in output.splitlines():
        match = ENDPOINT_RE.match(line)
        if match:
            endpoints.append((match[2], match[3], match[1] == "*"))
    return endpoints


def list_endpoints(binary):
    result = subprocess.run([binary, "--list-endpoint"], capture_output=True,
                            text=True, timeout=8)
    if result.returncode:
        raise RuntimeError(result.stderr.strip() or "Could not list PipeWire sinks")
    return parse_endpoints(result.stdout)


def server_args(binary, host, port, endpoint):
    try:
        address = ipaddress.IPv4Address(host.strip())
    except ipaddress.AddressValueError as exc:
        raise ValueError("Host must be a valid IPv4 address on this computer") from exc
    if address.is_unspecified or address.is_multicast or address.is_loopback:
        raise ValueError("Choose a reachable LAN IPv4 address, not a loopback or wildcard address")
    try:
        number = int(port)
    except (TypeError, ValueError) as exc:
        raise ValueError("Port must be an integer from 1 to 65535") from exc
    if str(number) != str(port).strip() or not 1 <= number <= 65535:
        raise ValueError("Port must be an integer from 1 to 65535")
    return [binary, f"--bind={address}:{number}", f"--endpoint={endpoint or 'default'}"]


def classify_server_line(line):
    """Do not confuse a bound socket with an operational audio capture stream."""
    if "audio capture ready" in line:
        return "ready"
    if "PipeWire capture failed" in line:
        return "capture_error"
    if "server started" in line:
        return "listening"
    if "[error]" in line or "No PipeWire audio sinks" in line or "Selected PipeWire sink is unavailable" in line:
        return "error"
    return "log"


class Server:
    """Own one as-cmd process; callbacks are called from the reader thread."""

    def __init__(self, on_line, on_exit):
        self.on_line = on_line
        self.on_exit = on_exit
        self.process = None
        self._lock = threading.Lock()

    def start(self, args):
        with self._lock:
            if self.process is not None:
                raise RuntimeError("Server is already running")
            self.process = subprocess.Popen(args, stdout=subprocess.PIPE,
                                            stderr=subprocess.STDOUT, text=True,
                                            bufsize=1, start_new_session=True)
            process = self.process
        threading.Thread(target=self._read, args=(process,), daemon=True).start()

    def _read(self, process):
        try:
            for line in process.stdout:
                self.on_line(line.rstrip("\n"))
        finally:
            process.stdout.close()
            code = process.wait()
            with self._lock:
                if self.process is process:
                    self.process = None
            self.on_exit(code)

    def stop(self):
        with self._lock:
            process = self.process
        if process is None or process.poll() is not None:
            return
        # The CLI has no shutdown command. Stop its process group so a launcher
        # cannot leave an orphan behind; wait outside the GTK event loop.
        def terminate():
            try:
                os.killpg(process.pid, signal.SIGTERM)
                process.wait(timeout=3)
            except subprocess.TimeoutExpired:
                os.killpg(process.pid, signal.SIGKILL)
            except ProcessLookupError:
                pass
        threading.Thread(target=terminate, daemon=True).start()
