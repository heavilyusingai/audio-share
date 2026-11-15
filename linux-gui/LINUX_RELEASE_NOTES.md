Linux desktop prerelease for Audio Share 0.3.4.

Includes distro-native GTK3 GUI + PipeWire server archives for **Arch Linux/CachyOS, Debian 12, Ubuntu 24.04, Fedora and openSUSE Tumbleweed** (x86_64). Choose the archive built for your distribution family; extract it and read `SETUP.md`, run `python3 gui/audio-share-gui`, or run `sudo sh gui/install.sh` to install the bundled server and desktop entry. On other distributions, build from source using `docs/linux.md`.

The server now distinguishes audio capture readiness from opening the network listener and exits on capture failure. GUI sink discovery is nonblocking, and the UI differentiates starting, listening, capture-ready, stopped and error states. Native builds, frontend tests, GTK state tests under a virtual display, archive integrity and staged installation have passed in CI containers for these distro families.

**Scope and caution:** This is a Linux-only prerelease; no new Android APK or Windows executable. Distro-linked binaries are not universal and other releases/derivatives may differ. Real phone audio streaming and diverse desktop/PipeWire hardware still need on-device tests. The current protocol has no authentication or encryption: use a trusted local network and do not expose its port to the Internet.
