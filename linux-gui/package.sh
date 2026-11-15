#!/bin/sh
# Bundle a distribution-native build and GTK frontend. Run from any directory.
set -eu
here=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
root=$(dirname "$here")
server=${1:-"$root/server-core/out/install/linux-system-Release/bin/as-cmd"}
out=${2:-"$root/server-core/out/install/linux-system-Release"}
version=$(cat "$root/VERSION")
distro=${3:-arch-linux}
case "$distro" in
    ''|*[!a-z0-9-]*) echo "Invalid distro slug: $distro" >&2; exit 1 ;;
esac
name="audio-share-${version}-${distro}-gui"
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
install -m644 "$root/docs/linux.md" "$stage/$name/SETUP.md"
cat > "$stage/$name/README.txt" <<EOF
Audio Share for $distro (x86_64)

Install the matching distro runtime packages listed in SETUP.md.
Run from this extracted directory: python3 gui/audio-share-gui
To install both the GUI desktop entry and bundled server:
    sudo sh gui/install.sh
Then run audio-share-gui or launch Audio Share from the application menu.

This binary is built against $distro system libraries, not universal Linux.
Do not expose the unauthenticated/unencrypted stream outside a trusted LAN.
The installer does not change PipeWire or firewall configuration.
EOF
tar -C "$stage" -czf "$out/$name.tar.gz" "$name"
(cd "$out" && sha256sum "$name.tar.gz" > "$name.tar.gz.sha256")
echo "$out/$name.tar.gz"
