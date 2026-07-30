#!/usr/bin/env bash
set -euo pipefail

project_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$project_dir"

python3 -m oss_research provenance
python3 -m oss_research ingest --pdf data/source/personnel-database.pdf
python3 -m oss_research validate-ingest --pdf data/source/personnel-database.pdf
python3 -m oss_research build-identities
python3 -m oss_research create-pilot --size 75 --batch-name pilot-v1
# File prefixes evolved during the project, so lexical glob order is not
# chronological. Import by the explicit batch number to ensure later review
# decisions deterministically supersede earlier ones on every rebuild.
while IFS=$'\t' read -r _ evidence_bundle; do
  python3 -m oss_research import-reviewed-evidence "$evidence_bundle"
done < <(
  for evidence_bundle in research/evidence_*.json research/evidence-*.json; do
    if [[ ! -f "$evidence_bundle" ]]; then
      continue
    fi
    filename="${evidence_bundle##*/}"
    batch_number=0
    if [[ "$filename" =~ batch[-_]?0*([0-9]+) ]]; then
      batch_number="${BASH_REMATCH[1]}"
    fi
    printf '%04d\t%s\n' "$batch_number" "$evidence_bundle"
  done | sort -t $'\t' -k1,1n -k2,2
)
python3 -m oss_research export-derived
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data

cd site
npm ci
npm run build
