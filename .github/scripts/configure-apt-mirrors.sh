#!/usr/bin/env bash
# Configure the ephemeral GitHub runner, without changing package trust or suites.
# Optional file arguments allow offline tests against temporary fixtures.
set -euo pipefail

if (( $# == 0 )); then
  set -- /etc/apt/apt-mirrors.txt /etc/apt/sources.list /etc/apt/sources.list.d/ubuntu.sources
fi

for config_file in "$@"; do
  if [[ -f "$config_file" ]]; then
    # GitHub's mirror list prefers Azure even when sources use mirror+file:.
    # Keep its official Ubuntu fallbacks and all Signed-By settings intact.
    sed -i -E 's|https?://azure\.archive\.ubuntu\.com/|https://archive.ubuntu.com/|g' "$config_file"
  fi
done
