# Batch 573 and oil-company category release report

Run: 2026-09-19 UTC

## Research and publication scope

Personnel-index PDF page 115 rows 23-32, Christian DeSorbier through Raymond
Deston, were visually checked and researched as a bounded cohort. Nine people
received terminal research dispositions; the tenth, Emile Despres, retained
his previously reviewed Federal Reserve Board claim. No new named pre-OSS
employer was established. Official Army evidence supports three occupation-
only findings, French archives support two officer identities without an
immediate-predecessor claim, and the 1941 Raymond Deston insurance lead remains
qualified and employer-free. The Desota/Desuta possible duplicate remains two
separate people and source rows. See the detailed
`research/batch-573-discovery-checkpoint.md` and versioned evidence bundle.

The public home page now displays a near-top oil-company category with the
seven people who have cited, published or visibly qualified employment claims
at nine historically named oil companies. It excludes a professional
affiliation to The Pure Oil Company that does not establish employment. Person
and organization links lead to the underlying evidence; the existing top
navigation and directory filter lead to the same seven-person set. This list
does not assert that each oil-company job was the immediate pre-OSS affiliation
or that seven is the total number of oil-industry workers in OSS.

## Exact coverage

| Measure | Count | Denominator | Coverage |
| --- | ---: | ---: | ---: |
| Index rows preserved and linked | 23,978 | 23,978 | 100.0000% |
| Active person entities | 23,940 | - | - |
| Research attempted | 5,495 | 23,940 | 22.9532% |
| Verified affiliation found | 596 | 23,940 | 2.4896% |
| Verified employer found | 260 | 23,940 | 1.0860% |
| Archival disposition assessed | 5,450 | 23,940 | 22.7652% |
| Not started | 18,445 | 23,940 | 77.0468% |

There are 256 possible-duplicate groups. The private database records 9,948
attempts, 4,856 citations, 2,220 unique source documents and 4,677 claims.
Claim-confidence totals are 1,307 confirmed, 1,707 high, 1,351 medium, 183 low
and 129 conflicting. The public projection contains 2,160 affiliations, 672
organizations, 3,665 sources and 4,491 claims. Research-status counts are in
`reports/research_coverage.md`; these counts do not represent completed
research for the entire index.

## Validation and release state

- All 95 Python tests, 522-page ingest validation and stratified 200-profile
  structural audit passed for the Batch 573 data.
- Astro reported zero errors, warnings or hints and built 24,620 static pages.
- The bounded browser release suite passed **81/81** checks: 21 newest-batch,
  27 core-route, six confidence-aware analysis and 27 accessibility checks at
  desktop, phone and tablet widths. The new home-page oil list is checked
  against the same seven-person directory filter, including exclusion of The
  Pure Oil Company nonemployee.
- All internal links across 24,620 HTML files resolve. The separate external
  URL inventory contains 50,084 unique links and is not a complete live check.
- The public-identifier audit scanned 24,692 artifacts against 12,926 private
  normalized identifiers and 120 formatted variants: no unexpected matches.
- The 70-file public-data tree totals 98,174,675 bytes at SHA-256
  `a9bb7b273d82e0f7db462f3517157cc970812cc284e198ffc997af0809c90e47`.
  The 24,692-file static build totals 290,603,447 bytes at SHA-256
  `51c3b4d459e878363f20eb8f44b16640fa340e8b0eb3eaecc6a040f6e86a3cb7`.
- Remote GitHub Pages publication and exact live-manifest verification remain
  pending until the release branch is pushed and merged.

## Resume

```bash
python3 -m oss_research import-reviewed-evidence research/evidence-page-one-hundred-and-fifteen-christian-desorbier-through-raymond-deston_batch-573_2026-09-19.json
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
NODE_OPTIONS=--max-old-space-size=8192 npm --prefix site run build
CI=1 npm --prefix site run test:release
npm --prefix site run check:links
python3 scripts/audit_public_identifiers.py --database research/research.sqlite --public-root site/dist
python3 scripts/verify_deployed_release.py --local-public-root site/public
```

Next research cohort: PDF page 115 rows 33-42, beginning with Frank J Desuta.
