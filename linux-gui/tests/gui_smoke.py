"""Exercise GTK session states with a fake server under xvfb-run (CI only)."""

import os
from pathlib import Path
import runpy
import tempfile
import time
import sys

import gi
gi.require_version("Gtk", "3.0")
from gi.repository import GLib, Gtk

root = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(root))
with tempfile.TemporaryDirectory() as directory:
    binary = Path(directory) / "as-cmd"
    binary.write_text("""#!/bin/sh
if [ "$1" = "--list-endpoint" ]; then
  printf 'endpoint list:\\n\\t* id: 1 name: Test sink\\ntotal: 1\\n'
else
  echo '[info] server started'
  sleep 0.4
  echo '[info] audio capture ready'
  sleep 30
fi
""")
    binary.chmod(0o755)
    os.environ["AUDIO_SHARE_SERVER"] = str(binary)
    Window = runpy.run_path(str(root / "audio-share-gui"), run_name="gui_smoke")["Window"]
    window = Window()
    window.show_all()
    phase = [0]
    deadline = time.monotonic() + 6
    result = ["timed out"]

    def check():
        status = window.status.get_text()
        if time.monotonic() > deadline:
            result[0] = "Timed out in phase %s: %s" % (phase[0], status)
            window.server.stop()
            Gtk.main_quit()
            return False
        if phase[0] == 0 and status == "Ready to start":
            window.on_toggle(None)
            phase[0] = 1
        elif phase[0] == 1 and "waiting for audio capture" in status:
            phase[0] = 2  # listening is not yet capture ready
        elif phase[0] == 2 and status.startswith("Capture ready"):
            window.on_toggle(None)
            phase[0] = 3
        elif phase[0] == 3 and status == "Server stopped":
            result[0] = "ok"
            Gtk.main_quit()
            return False
        return True

    GLib.timeout_add(50, check)
    Gtk.main()
    assert result[0] == "ok", result[0]
