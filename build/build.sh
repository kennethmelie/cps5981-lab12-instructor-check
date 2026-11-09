#!/usr/bin/env bash
# Deterministic build: the same commit always produces the same bytes.
set -euo pipefail
VERSION="${1:-dev}"
export SOURCE_DATE_EPOCH="$(git log -1 --format=%ct)"
rm -rf dist && mkdir -p dist/stage/cougar-advising
cp -r app/. dist/stage/cougar-advising/
cp config/app.env dist/stage/cougar-advising/app.env
tar --sort=name --mtime="@${SOURCE_DATE_EPOCH}" --owner=0 --group=0 --numeric-owner \
    -C dist/stage -cf - cougar-advising | gzip -n -9 > "dist/cougar-advising.tar.gz"
rm -rf dist/stage
echo "built dist/cougar-advising.tar.gz for ${VERSION}"
