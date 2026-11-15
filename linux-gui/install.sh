#!/bin/sh
# Install the frontend (not the as-cmd server). PREFIX defaults to /usr/local.
set -eu
prefix=${PREFIX:-/usr/local}
destdir=${DESTDIR:-}
source_dir=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
install -Dm755 "$source_dir/audio-share-gui" "$destdir$prefix/share/audio-share-gui/audio-share-gui"
install -Dm644 "$source_dir/backend.py" "$destdir$prefix/share/audio-share-gui/backend.py"
install -Dm644 "$source_dir/io.github.mkckr0.AudioShare.desktop" "$destdir$prefix/share/applications/io.github.mkckr0.AudioShare.desktop"
mkdir -p "$destdir$prefix/bin"
printf '#!/bin/sh\nexec python3 "%s/share/audio-share-gui/audio-share-gui" "$@"\n' "$prefix" > "$destdir$prefix/bin/audio-share-gui"
chmod 755 "$destdir$prefix/bin/audio-share-gui"
