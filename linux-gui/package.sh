#!/bin/sh
# Bundle the native Arch build and GTK frontend. Run from any working directory.
set -eu
here=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
root=$(dirname "$here")
server=${1:-"$root/server-core/out/install/linux-system-Release/bin/as-cmd"}
out=${2:-"$root/server-core/out/install/linux-system-Release"}
version=$(cat "$root/VERSION")
name="audio-share-${version}-arch-linux-gui"
test -x "$server" || { echo "Missing executable server: $server" >&2; exit 1; }
mkdir -p "$out"
out=$(cd "$out" && pwd)
stage=$(mktemp -d)
trap 'rm -rf "$stage"' EXIT HUP INT TERM
mkdir -p "$stage/$name/bin" "$stage/$name/gui"
install -m755 "$server" "$stage/$name/bin/as-cmd"
install -m755 "$here/audio-share-gui" "$here/install.sh" "$stage/$name/gui/"
install -m644 "$here/backend.py" "$here/io.github.mkckr0.AudioShare.desktop" "$stage/$name/gui/"
install -m644 "$root/LICENSE" "$stage/$name/LICENSE"
cat > "$stage/$name/README.txt" <<'EOF'
Audio Share for Arch Linux / CachyOS (x86_64)

Requires PipeWire, WirePlumber, Python, PyGObject/GTK3 and iproute2.
Install dependencies: sudo pacman -S --needed pipewire wireplumber python python-gobject gtk3 iproute2

Run from the unpacked directory: python3 gui/audio-share-gui
To install both the GUI desktop launcher and bundled server:
    sudo sh gui/install.sh
Then launch Audio Share from the application menu or run audio-share-gui.
Use the Android Audio Share app on the same network. If you use a firewall,
allow TCP and UDP for the selected port (default 65530).

This is an Arch/CachyOS package built against Arch system libraries, not a
universal Linux binary. The installer does not modify PipeWire or firewall
configuration. See the project README for troubleshooting and source code.
EOF
tar -C "$stage" -czf "$out/$name.tar.gz" "$name"
(cd "$out" && sha256sum "$name.tar.gz" > "$name.tar.gz.sha256")
echo "$out/$name.tar.gz"
