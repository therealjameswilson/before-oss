#!/usr/bin/env bash
set -euo pipefail

project_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$project_dir"

python3 -m oss_research provenance
python3 -m oss_research ingest --pdf data/source/personnel-database.pdf
python3 -m oss_research import-page-reviews \
  research/parser_visual_review_decisions.json
python3 -m oss_research validate-ingest --pdf data/source/personnel-database.pdf
python3 -m oss_research build-identities
python3 -m oss_research create-pilot --size 75 --batch-name pilot-v1
python3 -m oss_research import-adapter-checkpoints \
  research/adapter_attempt_checkpoints.json
for review_decisions in research/*_review_decisions_*.csv; do
  if [[ -f "$review_decisions" ]]; then
    python3 -m oss_research import-review-decisions "$review_decisions"
  fi
done
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
    # Finder-style duplicate copies are not reviewed evidence bundles. Keeping
    # them out of deterministic rebuilds prevents an unrelated local copy from
    # influencing the durable database merely because it matches the glob.
    if [[ "$filename" == *" 2.json" ]]; then
      continue
    fi
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
before_oss_npm_cache="${BEFORE_OSS_NPM_CACHE:-${TMPDIR:-/tmp}/before-oss-npm-cache}"
mkdir -p "$before_oss_npm_cache"
npm ci --cache "$before_oss_npm_cache"
npm run build
