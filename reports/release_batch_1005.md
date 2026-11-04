# Batch 1005 release audit

Date: 2026-11-03 America/New_York

## Release contents

- NARA index page 495, rows 1-46: Ray J. Weichbrodt through Harold
  Weisberg. All 46 printed rows remain separately recoverable and link to 46
  cautious person entities.
- Every cohort person has a saved research attempt and a terminal review
  outcome: 27 `requires_archival_review`, 15 `occupation_only_found`, 2
  `verified_employer_found`, 1 `completed` and 1 `conflicting_sources`.
- Identity disposition is 15 confirmed, 5 high-confidence, 1 conflicting and
  25 unresolved people.
- Nineteen official Army bulk-record candidates received explicit review:
  18 were accepted and one remains conflicting. Fifteen accepted records
  support only qualified historical occupation or student categories. No
  named employer, institution or workplace was inferred from those codes.
- Richard Weil Jr. is confirmed as president of L. Bamberger & Company
  immediately before his March 1943 OSS commission. His earlier R. H. Macy &
  Company work is modeled separately rather than conflated with the immediate
  employer.
- Harold Weisberg is confirmed through an official OSS form and the reviewed
  Army bridge. His immediate pre-OSS affiliation is the U.S. Army; freelance
  writing is his last documented civilian work, with Click magazine and the
  U.S. Senate Civil Liberties Committee modeled separately. Army occupation
  code 940 remains withheld rather than decoded or published.
- Guido G. Weigend's University of Chicago relationship is published as
  student status, not employment.
- The two George Weiner rows remain separate and share a visible possible-
  duplicate group. The protected identifier on the second row resolves to a
  materially different Army name, so the record remains conflicting and no
  Army occupation is transferred.
- Robert P. Weimann and George B. Weisback have high-confidence Army identity
  bridges, but the reviewed Army-entry records postdate the relevant OSS
  period. Those records are not presented as pre-OSS occupations.
- Exact-name duplicate groups for Morris Weil, Daniel J. Weiner and George
  Weiner remain visible and were never silently merged.
- All 46 page-495 source rows were checked against layout-preserving text and
  an original-detail page render. Relevant official Army code-list pages, the
  Harold Weisberg OSS form and the Summit Herald page carrying the Richard
  Weil account were also visually inspected.
- No authenticated NARA Catalog API request was used.

## Reproducible release checks

- Audited content commit:
  `42827f1a7b5231671a4f25684b2336d930df66ca`.
- Evidence-bundle SHA-256:
  `ffb9ad5775323c5a49acbb26b58b9291d49580397a0dac6b9208beffe4164e50`.
- Army-review-decision SHA-256:
  `05091c978e4a78c6cf88da476997c512a481d34291e41cf26531d2d47cbc291c`.
- Re-running the bundle generator reproduced the same evidence hash.
- Durable import: 8 sources, 7 organization inputs, 22 affiliations, 44
  claims, 97 claim-source links, 46 person updates and 46 research attempts.
- Batch claim confidence: 17 confirmed, 11 high, 15 medium and 1 conflicting.
  Publication disposition is 28 published, 15 qualified and 1 conflict
  claim.
- Python: 154 tests passed locally and in the independent GitHub Actions run.
- SQLite foreign-key and quick checks passed.
- The deterministic 200-profile stratified audit passed all seven invariants.
- Checked-in public manifest: 67 canonical assets, 135,100,184 bytes,
  SHA-256
  `842c6b9fd11ccf352aaf5f6ff5efcb711179cb56ebe3d8784e4cb9d197d14ecd`.
- Clean GitHub Actions Astro check: zero errors, zero warnings and zero hints.
- Clean static build: 25,314 pages.
- Bounded browser release suite: 99/99 checks passed across desktop, phone and
  tablet: 30 latest-batch checks, 33 core-route and interaction checks, 6
  analysis checks, and 30 accessibility scans with no serious axe
  violations.
- Internal links: 25,314 HTML files checked; all links resolve. The checker
  inventoried 52,284 unique external URLs separately.
- Clean-checkout public identifier audit: 25,386 artifacts checked against
  12,926 normalized private identifiers and 120 formatted variants. It found
  zero aggregate false positives, zero manifest-size false positives and zero
  unexpected boundary matches.
- Production dependency audit: zero vulnerabilities.

## Coverage published

- Index: 23,978/23,978 source rows linked (100.0000%).
- Research attempted: 16,161/23,936 people (67.5175%).
- Verified affiliation: 1,155/23,936 people (4.8254%).
- Verified employer: 525/23,936 people (2.1933%).
- Archival disposition assessed: 14,636/23,936 people (61.1464%).
- Not started: 7,770 people; in progress: 1,883 people.
- Research outcomes include 1,763 `occupation_only_found`, 8,902
  `requires_archival_review`, 442 `verified_employer_found`, 285
  `documented_prewar_employer_found` and 461 `conflicting_sources` people.
- Possible-duplicate groups: 682; conflicts: 541.
- Claim confidence: 1,826 confirmed; 5,393 high; 2,694 medium; 258 low;
  449 conflicting; and 2 unresolved.
- Public projection: 23,936 profiles, 4,095 affiliations, 1,326
  organizations, 6,582 sources and 10,358 published, qualified or conflict
  claims.
- Citations: 7,872 across 4,396 unique source documents.

## Publication verification

- Immutable published release commit:
  `42827f1a7b5231671a4f25684b2336d930df66ca`.
- GitHub Actions Test run
  [41746848593](https://github.com/therealjameswilson/before-oss/actions/runs/41746848593)
  completed successfully on 2026-11-03.
- GitHub Pages run
  [41746848443](https://github.com/therealjameswilson/before-oss/actions/runs/41746848443)
  completed successfully on 2026-11-03.
- On 2026-11-03, the unauthenticated deployed-release verifier checked the
  live GitHub Pages site against that exact commit and evidence bundle. It
  verified all 67 public assets (135,100,184 bytes; manifest SHA-256
  `842c6b9fd11ccf352aaf5f6ff5efcb711179cb56ebe3d8784e4cb9d197d14ecd`),
  all eight core routes, all 44 source-register pages and all 46 direct Batch
  1005 profile routes.

Public release URL: <https://therealjameswilson.github.io/before-oss/>.
