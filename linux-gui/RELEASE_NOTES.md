Arch Linux / CachyOS desktop prerelease for Audio Share 0.3.4.

Includes a GTK3 GUI and a native `as-cmd` PipeWire server for x86_64 Arch-based systems. Select a LAN address, port and audio sink, then start the server and connect from the Android Audio Share app. The package includes an optional desktop launcher installer; see its `README.txt` after extracting.

Also fixes LAN address selection, bind-port validation, compatibility with current Arch Protobuf and Asio packages, and a crash when PipeWire is unavailable.

**Scope:** This prerelease contains only the Arch/CachyOS desktop server package; it does not include a new Android APK or Windows build. It requires Arch system libraries and a running PipeWire session. CI verifies compilation, frontend tests, GUI launch under Xvfb, and the no-PipeWire error path; audio streaming to a phone has not been hardware-tested here.
