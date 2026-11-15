# Linux desktop setup (x86_64)

Audio Share's GTK3 frontend launches the PipeWire `as-cmd` server. It needs a graphical session for the GUI, a running **user** PipeWire session and at least one audio sink; the Android app must be on a reachable network. Do not run the GUI/server with sudo. The CLI remains usable headlessly. The table below is tested by CI in representative **container** environments (native compilation, dependencies, GTK launch with a fake server), not a guarantee for every derivative, desktop environment, or sound device.

| Family tested in CI | GUI/runtime dependencies | Native build dependencies (in addition to runtime) |
|---|---|---|
| Arch Linux / CachyOS | `sudo pacman -S --needed pipewire wireplumber python python-gobject gtk3 iproute2` | `sudo pacman -S --needed git base-devel cmake pkgconf protobuf asio spdlog cxxopts` |
| Debian 12 | `sudo apt install pipewire wireplumber python3 python3-gi gir1.2-gtk-3.0 iproute2` | `sudo apt install git build-essential cmake pkg-config libpipewire-0.3-dev libprotobuf-dev protobuf-compiler libasio-dev libspdlog-dev libcxxopts-dev` |
| Ubuntu 24.04 | `sudo apt install pipewire wireplumber python3 python3-gi gir1.2-gtk-3.0 iproute2` | `sudo apt install git build-essential cmake pkg-config libpipewire-0.3-dev libprotobuf-dev protobuf-compiler libasio-dev libspdlog-dev libcxxopts-dev` |
| Fedora | `sudo dnf install pipewire wireplumber python3 python3-gobject gtk3 iproute` | `sudo dnf install git gcc-c++ make cmake pkgconf-pkg-config pipewire-devel protobuf-devel protobuf-compiler asio-devel spdlog-devel cxxopts-devel` |
| openSUSE Tumbleweed | `sudo zypper install pipewire wireplumber python3 python3-gobject-Gdk typelib-1_0-Gtk-3_0 iproute2` | `sudo zypper install git gcc-c++ make cmake pkg-config pipewire-devel protobuf-devel asio-devel spdlog-devel cxxopts-devel` |

Check distro/package names if using a different release. Debian 12's packaged Asio is too old for the coroutine API used here: CMake fetches a **pinned Asio 1.30.2 source tree from GitHub** during configure when the installed headers are older than 1.28. A network connection is therefore needed for that build unless you provide a recent header tree with `-DASIO_INCLUDE_DIR=/path/to/include`. This source fetch is **build-time only**; the installed GUI/server do not contact GitHub to play audio. Ubuntu/Fedora/openSUSE/Arch can build with their tested system packages.

## Build and run from source

From the repository root, after installing the appropriate build dependencies above:

```sh
cmake -S server-core --preset linux-system-Release
cmake --build server-core/out/build/linux-system-Release --target install/strip -j2
python3 linux-gui/audio-share-gui
```

The build preset installs into `server-core/out/install/linux-system-Release/bin/as-cmd`, which the GUI detects automatically in a source checkout. To install globally:

```sh
sudo install -Dm755 server-core/out/install/linux-system-Release/bin/as-cmd /usr/local/bin/as-cmd
sudo sh linux-gui/install.sh
```

Use `audio-share-gui` from a terminal or the **Audio Share** desktop entry. If the server is somewhere else, set `AUDIO_SHARE_SERVER=/absolute/path/to/as-cmd` before launching the GUI; desktop launchers do not inherit temporary shell variables. Or extract a matching distro archive and run `python3 gui/audio-share-gui` in the extracted directory. In an archive, `sudo sh gui/install.sh` installs both its bundled server and GUI. The archive's native binary links against its build distribution's system libraries; do **not** assume a Fedora/Arch binary works on Debian or vice versa. Build from source on other Linux families.

## Connectivity and troubleshooting

1. On a desktop, check `systemctl --user status pipewire wireplumber` and `as-cmd --list-endpoint`. A sink must be present. On minimal systems, install/configure the distro's PipeWire session and output sink first.
2. Select the PC's **LAN IPv4** address reachable from the phone and the sink to capture. A TCP listener is not proof that capture is ready; wait for **Capture ready** in the GUI.
3. Use the same IP/port on Android. If a firewall is enabled, allow **TCP and UDP** on that port (default 65530). The GUI does not change firewall rules or start services as root.
4. If audio is silent despite a connection, check the selected sink, whether the PC application is playing to it, and phone media volume. Check the technical output for a capture error.

The current wire protocol does **not** implement encrypted or authenticated transport. Use a trusted local network; do not forward its port to the Internet. Hardware playback, suspend/resume, and every derivative distribution still need on-device testing. Source tests: `python3 -m unittest discover -s linux-gui/tests -v`; GTK state smoke (with Xvfb): `xvfb-run -a python3 linux-gui/tests/gui_smoke.py`.
