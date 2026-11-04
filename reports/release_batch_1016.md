# Batch 1016 release audit

Date: 2026-11-04 America/New_York

## Release contents

- NARA index page 506, rows 1-46: Lansing Williams through Lawrence J.
  Willinger. All 46 printed rows remain separately recoverable as 46 cautious
  person entities.
- Every cohort person has a saved explicit outcome: 38
  `requires_archival_review`, six `occupation_only_found`, one
  `needs_identity_review` and one `conflicting_sources`.
- Identity disposition is six confirmed, three high-confidence, one probable,
  one conflicting and 35 unresolved cohort people.
- Eight protected-identifier Army bridges received explicit acceptance
  review. Six safely documented historical occupation or student categories
  remain visibly qualified and are not converted into named employers,
  schools, workplaces or exact OSS-transfer dates.
- Milton D. Williams's Army entry postdates OSS dissolution, while Peter W.
  Williams's code 478 is not defined in the inspected official table; both
  bridges confirm identity only. One identifier maps to two incompatible
  Norman Williams Army rows, so no Army data are transferred pending Box 840
  review.
- Two Ball State institutional records support a probable Jayo Williamson
  identity, his 1935 *Easterner* assistant-copy-editor role and Class of 1939
  status. The result is published as a qualified student affiliation, never
  as employment.
- Two direct CIA OSS records and two *Foreign Service Journal* records support
  a high-confidence David Williamson identity. His 1942 Foreign Service
  resignation is published as the best-supported probable immediate
  government affiliation before his documented OSS European and Mediterranean
  operations leadership. It is not labeled a private civilian employer or an
  explicit transition.
- A bounded CIA adapter check encountered `CiaRobotsUnavailable`, and a
  Library of Congress check encountered `URLError`. Both failures remain
  auditable and are not treated as negative results. Accessible official and
  institutional alternatives were reviewed. No authenticated NARA Catalog API
  request was used.

## Reproducible release checks

- Evidence-bundle SHA-256:
  `a450ce4ae4abea921b1e253e53faf7ab4bcc774a781b88e4f7ee1745ca0866e7`.
- Army review-decision SHA-256:
  `4e958f607dfb28415dfaf217abeb74695c82cb879f75244450ee68e1b0e73438`.
- Durable import: ten sources, two organization inputs, eight affiliations,
  19 claims, 46 person updates, 46 manual research attempts and 60
  claim-source links. A second evidence import reproduced identical database
  counts.
- Batch claim confidence: six confirmed, four high, eight medium and one
  conflicting. Publication disposition is ten published, eight visibly
  qualified and one conflict claim.
- Python: all 154 tests passed.
- SQLite foreign-key, integrity and complete 522-page ingest checks passed.
- The deterministic 200-profile stratified audit passed all seven invariants.
- Checked-in public manifest: 67 canonical assets, 137,493,997 bytes,
  SHA-256
  `b1e79cdbdd41cf8e8adc6f2389dfcfd29855805471b9ef9b21b63c3012864be1`.
- Clean Astro check: 647 files with zero errors, warnings or hints.
- Clean static build: 25,339 pages.
- Bounded browser release suite: 96/96 checks passed across desktop, phone and
  tablet: 27 Batch 1016 checks, 33 core-route and interaction checks, six
  analysis checks and 30 accessibility scans with no serious axe violations.
- Internal links: 25,339 HTML files checked; all links resolve. The checker
  inventoried 52,361 unique external URLs separately.
- Public-identifier audit: 25,411 artifacts checked against 12,926 normalized
  private identifiers and 120 formatted variants. It inspected 1,552
  candidate substrings and found zero aggregate, manifest-size or unexpected
  boundary matches.
- Two consecutive local builds reproduced 25,411 artifacts and 430,294,346
  bytes at output-tree SHA-256
  `e142b2c1bbd7cd1d150f36ae95a48dd18d8a1aa3c48a0ee47f151aa5af974360`.
- The production dependency audit found zero vulnerabilities.

## Coverage prepared for publication

- Index: 23,978/23,978 source rows linked (100.0000%).
- Research attempted: 16,661/23,935 people (69.6094%).
- Verified affiliation: 1,176/23,935 people (4.9133%).
- Verified employer: 538/23,935 people (2.2478%).
- Archival disposition assessed: 15,140/23,935 people (63.2546%).
- Not started: 7,269 people; in progress: 1,880 people.
- Research outcomes include 1,867 `occupation_only_found`, 9,264
  `requires_archival_review`, 451 `verified_employer_found`, 291
  `documented_prewar_employer_found`, 602 `needs_identity_review` and 471
  `conflicting_sources` people.
- Possible-duplicate groups: 691; conflicts: 551.
- Claim confidence: 1,915 confirmed; 5,459 high; 2,821 medium; 261 low; 459
  conflicting; and two unresolved.
- Public projection: 23,935 profiles, 4,260 affiliations, 1,351 organizations,
  6,687 sources and 10,650 published, qualified or conflict claims.
- Citations: 7,979 across 4,464 unique source documents.

## Publication verification

Content commit `a818516f9611f8140ce81626a5ea0b5d943c9958` passed the full
[Test workflow](https://github.com/therealjameswilson/before-oss/actions/runs/41804388078)
and the
[GitHub Pages workflow](https://github.com/therealjameswilson/before-oss/actions/runs/41804388024).
The unauthenticated deployed-release verifier matched all 67 canonical assets
and 137,493,997 bytes to the committed manifest at SHA-256
`b1e79cdbdd41cf8e8adc6f2389dfcfd29855805471b9ef9b21b63c3012864be1`.
It also returned successful main content for all eight core routes, all 45
source-register pages and all 46 Batch 1016 direct profile URLs.

Public release URL: <https://therealjameswilson.github.io/before-oss/>.
