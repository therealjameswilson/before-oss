#!/usr/bin/env bash
set -euo pipefail

project_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
destination="$project_dir/data/source/personnel-database.pdf"
expected_sha="7268492342ab131d3b6d2697cfa4f6856cbdcd16e0ed3877e8d6a0478f58c02b"
source_url="https://www.archives.gov/files/iwg/declassified-records/rg-226-oss/personnel-database.pdf"

mkdir -p "$(dirname "$destination")"
curl --fail --location --proto '=https' --tlsv1.2 \
  --output "$destination" "$source_url"
actual_sha="$(shasum -a 256 "$destination" | awk '{print $1}')"
if [[ "$actual_sha" != "$expected_sha" ]]; then
  echo "Source checksum mismatch: expected $expected_sha, got $actual_sha" >&2
  exit 1
fi
echo "Verified $destination ($actual_sha)"
