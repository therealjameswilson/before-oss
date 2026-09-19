# Batch 574 release report

Run: 2026-09-19 UTC

## Research and publication scope

The source PDF's page 115 rows 33-42, Frank J Desuta through Richard B
Deufson, were visually checked and researched as a ten-person bounded cohort.
All ten now have saved terminal outcomes. The Library of Congress and National
Park Service support Wallace R. Deuel's Chicago Daily News career through
1941, followed by 1941 entry into the Coordinator of Information and later
OSS service. NARA dates COI's conversion into OSS to June 1942, so COI is
modeled as his immediate pre-OSS government assignment; Chicago Daily News is
his last documented civilian employer. His earlier American University in
Beirut teaching is a separate documented role. Nine other people remain
unresolved or ambiguous and are directed to archival review. Four Library of
Congress OCR candidates were
reviewed, none used as final employer evidence. See the detailed
`research/batch-574-discovery-checkpoint.md` and versioned evidence bundle.

The previously published home-page oil-company category remains a
confidence-labeled seven-person listing; Batch 574 does not add an oil-company
employee. The category continues to distinguish documented employment from
professional affiliation and does not claim to represent the full OSS index.

## Exact coverage

| Measure | Count | Denominator | Coverage |
| --- | ---: | ---: | ---: |
| Index rows preserved and linked | 23,978 | 23,978 | 100.0000% |
| Active person entities | 23,940 | - | - |
| Research attempted | 5,505 | 23,940 | 22.9950% |
| Verified affiliation found | 597 | 23,940 | 2.4937% |
| Verified employer found | 261 | 23,940 | 1.0902% |
| Archival disposition assessed | 5,460 | 23,940 | 22.8070% |
| Not started | 18,435 | 23,940 | 77.0050% |

There are 256 possible-duplicate groups. The private database records 9,978
attempts, 4,861 citations, 2,221 unique source documents and 4,691 claims.
Claim-confidence totals are 1,307 confirmed, 1,721 high, 1,351 medium, 183
low and 129 conflicting. The public projection contains 2,163 affiliations,
673 organizations, 3,670 sources and 4,504 claims. Research-status counts are
in `reports/research_coverage.md`; an issued automated query alone is not
treated as completed research for the full index.

## Validation and release state

- All 95 Python tests, 522-page ingest validation and stratified 200-profile
  structural audit passed.
- Astro reported zero errors, warnings or hints and built 24,621 static pages.
- The bounded browser release suite passed **75/75** checks: 15 newest-batch,
  27 core-route, six confidence-aware analysis and 27 accessibility checks at
  desktop, phone and tablet widths. The oil-company category remains covered.
- All internal links across 24,621 HTML files resolve. The separate external
  URL inventory contains 50,086 unique links and is not a complete live check.
- The public-identifier audit scanned 24,693 artifacts against 12,926 private
  normalized identifiers and 120 formatted variants: no unexpected matches.
- The 70-file public-data tree totals 98,251,871 bytes at SHA-256
  `96c72e04be2b282bab91f7375bbf4a61a1a9396beed6d7b0a09e09637778a6a1`.
  The 24,693-file static build totals 290,724,441 bytes at SHA-256
  `2044d8485474384b75acd9d2ef2fd7f14def3dfc4295ac294a76e665b2ab6427`.
- The local manifest guard verifies all 67 assets (95,904,747 bytes) at
  SHA-256 `fcf00162246f7e65dbb70071b05dc76e14fb573ad9cb9d0636d00fdbb20c74fc`.

This remains a **local release candidate** until the exact committed revision
passes CI, GitHub Pages deployment and unauthenticated live verification. The
existing public release is Batch 573.

## Resume

```bash
python3 -m oss_research import-reviewed-evidence research/evidence-page-one-hundred-and-fifteen-frank-j-desuta-through-richard-b-deufson_batch-574_2026-09-19.json
python3 -m oss_research import-review-decisions research/loc_review_decisions_2026-09-19_batch574.csv
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
npm --prefix site ci
npm --prefix site run build
npm --prefix site run test:release
npm --prefix site run check:links
python3 scripts/audit_public_identifiers.py --database research/research.sqlite --public-root site/dist
python3 scripts/verify_deployed_release.py --local-public-root site/public
```

Next research cohort: PDF page 115 rows 43-46, then page 116 rows 1-6.
