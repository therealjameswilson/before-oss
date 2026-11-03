# Batch 1003 release audit

Date: 2026-11-03 America/New_York

## Release contents

- NARA index page 493, rows 1-46: Arthur W. Watterson through Jacob H.
  Weber. All 46 printed rows remain separately recoverable, including the
  unusual printed `Weaver and C *` row.
- Every cohort person has a saved research attempt and a terminal review
  outcome: 34 `requires_archival_review`, 10 `occupation_only_found` and 2
  `verified_employer_found`.
- Identity disposition is 11 confirmed, 2 high-confidence, 3 probable and 30
  unresolved people.
- Eleven official Army bulk-record bridges were accepted after exact-name and
  protected-identifier review. Ten profiles preserve only the qualified
  historical occupation or student category recorded at Army entry. Charlton
  A. Weaver's Army record postdates OSS service, so it supports identity only
  and no occupation was transferred. No named employer or workplace was
  inferred from a coded occupation.
- A scholarly institutional obituary supports a high-confidence Robert
  Wauchope identity and identifies Tulane University as both his immediate
  pre-OSS affiliation and last civilian employer.
- An American Foreign Service Association memorial supports a high-confidence
  Meredith Weatherby identity and identifies the Foreign Service and United
  States Department of State as his last civilian government affiliation
  before Army service. It is not presented as his immediate pre-OSS
  affiliation or as a civilian-employer aggregate.
- An official CIA OSS order and the reviewed Army bridge confirm Frank R.
  Weber. Three low-confidence namesake candidates remain private review leads
  and were not published as facts.
- All 46 source rows were checked against layout-preserving text and an
  original-detail render. Relevant Army occupation-code pages were also
  inspected.
- No authenticated NARA Catalog API request was used.

## Reproducible release checks

- Audited content commit:
  `f49f96bc132fc3ec9931664f26119229aa1918ce`.
- Evidence-bundle SHA-256:
  `d1a73853ae4f1a33a6987106f65fbfafaa927b550949a70dbd3c32db12d36896`.
- Re-running the bundle generator reproduced the same evidence hash.
- Durable import: 10 sources, 2 organization inputs, 12 affiliations, 29
  claims, 63 claim-source links, 46 person updates and 46 research attempts.
- Batch claim confidence: 11 confirmed, 5 high, 10 medium and 3 low.
  Publication disposition is 16 published, 10 qualified and 3 withheld
  claims.
- Review decisions: eleven accepted official Army candidates.
- Python: 154 tests passed locally and in the independent GitHub Actions run.
- Checked-in public manifest: 67 canonical assets, 134,600,891 bytes,
  SHA-256
  `315be40619c9ef8ae4dd05b4747d4ab78068f01a2534c2bdf0cda35fc284d5a4`.
- Clean GitHub Actions Astro check: zero errors, zero warnings and zero hints.
- Clean static build: 25,310 pages.
- Bounded browser release suite: 99/99 checks passed across desktop, phone and
  tablet: 30 latest-batch checks, 33 core-route and interaction checks, 6
  analysis checks, and 30 accessibility scans with no serious axe
  violations.
- Internal links: 25,310 HTML files checked; all links resolve. The checker
  inventoried 52,273 unique external URLs separately.
- Clean-checkout public identifier audit: 25,382 artifacts checked against
  12,926 normalized private identifiers and 120 formatted variants. It found
  zero aggregate false positives, zero manifest-size false positives and zero
  unexpected boundary matches.
- Production dependency audit: zero vulnerabilities.

## Coverage published

- Index: 23,978/23,978 source rows linked (100.0000%).
- Research attempted: 16,070/23,936 people (67.1374%).
- Verified affiliation: 1,151/23,936 people (4.8087%).
- Verified employer: 522/23,936 people (2.1808%).
- Archival disposition assessed: 14,545/23,936 people (60.7662%).
- Not started: 7,861 people; in progress: 1,883 people.
- Research outcomes include 1,740 `occupation_only_found`, 8,841
  `requires_archival_review`, 439 `verified_employer_found`, 285
  `documented_prewar_employer_found` and 459 `conflicting_sources` people.
- Possible-duplicate groups: 679; conflicts: 539.
- Claim confidence: 1,799 confirmed; 5,379 high; 2,669 medium; 258 low;
  447 conflicting; and 2 unresolved.
- Public projection: 23,936 profiles, 4,061 affiliations, 1,322
  organizations, 6,566 sources and 10,290 published, qualified or conflict
  claims.
- Citations: 7,856 across 4,387 unique source documents.

## Publication verification

- Immutable published release commit:
  `f49f96bc132fc3ec9931664f26119229aa1918ce`.
- GitHub Actions Test run `41720030185` completed successfully on
  2026-11-03.
- GitHub Pages run `41720030064` completed successfully on 2026-11-03.
- On 2026-11-03, the unauthenticated deployed-release verifier checked the
  live GitHub Pages site against that exact commit and evidence bundle. It
  verified all 67 public assets (134,600,891 bytes; manifest SHA-256
  `315be40619c9ef8ae4dd05b4747d4ab78068f01a2534c2bdf0cda35fc284d5a4`),
  all eight core routes, all 44 source-register pages and all 46 direct Batch
  1003 profile routes.

Public release URL: <https://therealjameswilson.github.io/before-oss/>.
