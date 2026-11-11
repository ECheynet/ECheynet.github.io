#!/usr/bin/env bash
set -euo pipefail
: "${IMAGEMAGICK_APP_RUN:?ImageMagick has not been installed}"

case "${0##*/}" in
  convert|magick) exec "$IMAGEMAGICK_APP_RUN" "$@" ;;
  identify|mogrify|montage|compare|composite) exec "$IMAGEMAGICK_APP_RUN" "${0##*/}" "$@" ;;
  *) echo "Unsupported ImageMagick command: ${0##*/}" >&2; exit 2 ;;
esac
