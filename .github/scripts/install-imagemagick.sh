#!/usr/bin/env bash
# Install the maintainer's portable Linux binary, not an unverified third-party action.
set -euo pipefail
: "${RUNNER_TEMP:?Run inside GitHub Actions or supply an explicit temporary directory}"
: "${GITHUB_PATH:?GitHub Actions path file is required}"
: "${GITHUB_ENV:?GitHub Actions environment file is required}"

version="7.1.2-35"
sha256="f111044ed06b68cfb478df724c5a32d35145afa21073242f888d234a2f8cc002"
script_dir="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
install_dir="$RUNNER_TEMP/imagemagick-$version"
appimage="$install_dir/ImageMagick.AppImage"
mkdir -p "$install_dir/bin"

if [[ ! -f "$appimage" ]]; then
  curl --fail --location --retry 2 --connect-timeout 15 --max-time 120 \
    "https://github.com/ImageMagick/ImageMagick/releases/download/$version/ImageMagick-$version-gcc-x86_64.AppImage" \
    --output "$appimage"
fi
printf '%s  %s\n' "$sha256" "$appimage" | sha256sum --check -
chmod u+x "$appimage"

# Extraction avoids FUSE, privileged mounts and any additional Ubuntu packages.
(cd "$install_dir" && "$appimage" --appimage-extract >/dev/null)
install -m 644 "$script_dir/imagemagick-policy.xml" "$install_dir/squashfs-root/usr/etc/ImageMagick-7/policy.xml"
export IMAGEMAGICK_APP_RUN="$install_dir/squashfs-root/AppRun"
for tool in magick convert identify mogrify montage compare composite; do
  install -m 755 "$script_dir/imagemagick-cli.sh" "$install_dir/bin/$tool"
done
printf '%s\n' "$install_dir/bin" >> "$GITHUB_PATH"
printf 'IMAGEMAGICK_APP_RUN=%s\n' "$IMAGEMAGICK_APP_RUN" >> "$GITHUB_ENV"

# Exercise the same PNG-to-WebP conversion used by jekyll-imagemagick.
"$install_dir/bin/convert" -version
"$install_dir/bin/convert" -size 2x2 xc:white "$install_dir/smoke.png"
"$install_dir/bin/convert" "$install_dir/smoke.png" -resize 1x1 "$install_dir/smoke.webp"
[[ "$("$install_dir/bin/identify" -format '%wx%h' "$install_dir/smoke.webp")" == "1x1" ]]
