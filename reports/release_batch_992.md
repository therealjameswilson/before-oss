# Batch 992 release audit

Date: 2026-11-03 America/New_York

## Release contents

- NARA index page 486, rows 24-46: William Vyhnal through Claude V.
  Wadsworth. Page 486 ends at row 46; page 487, row 1, Albert H. Waffle, is
  the next cohort boundary.
- All 23 printed rows remain separate people and have saved terminal research
  outcomes: 2 `occupation_only_found` and 21 `requires_archival_review`.
- Official Army identity bridges for Charles S Wade and Frederick J Wadley
  III support only qualified historical occupation categories. Neither is
  converted into a named employer or agency.
- John E Wachsmuth's probable 1943 University of Minnesota ROTC match remains
  a qualified student and institutional affiliation, not employment or proof
  of commissioned status.
- Bertus Harry Wabeke's probable identity bridge from a 1954 institutional
  biography remains an identity lead only and creates no pre-OSS employer.
- Nineteen unresolved identities retain archival-review guidance and no
  invented affiliations.
- No authenticated NARA Catalog API request was used.

## Reproducible local release checks

- Audited content commit:
  `976a7e2e78255919a408ddc64b2159e864daf5a8`.
- Evidence-bundle SHA-256:
  `68df4a5428fe86ee1a833a57ca1d0128fad730d9ad0061f3268eb87d7cf1905d`.
- Durable import: 6 sources, 1 organization update, 3 affiliations, 7 claims,
  15 claim-source links, 23 person updates and 23 research attempts.
- Review decisions: two accepted official Army identity candidates.
- Complete ingest audit: every check passed for 23,978 rows and 522 pages.
- Python: 149 tests passed with the CI-equivalent `unittest discover`
  command.
- Targeted Batch browser matrix: 24/24 checks passed across desktop, phone and
  tablet.
- Clean-archive browser release suite: 93/93 current-batch, core-route,
  analysis and accessibility checks passed, including 30 axe scans with no
  serious violations.
- Clean-archive Astro build: 623 files checked with zero diagnostics; 25,291
  canonical static pages built.
- Clean-archive internal links: 25,291 HTML files checked; all links resolve;
  52,221 unique external URLs were inventoried separately.
- Clean-archive identifier audit: 12,926 normalized identifiers and 120
  formatted variants checked across 25,363 artifacts; 1,466 candidate
  substrings and zero unexpected matches.
- Public manifest: 67 canonical assets, 133,029,131 bytes, SHA-256
  `6218e159c9c99f82bf28942ac29485da6b9ca7fbbaf74019ff4e241c3b56ddff`.
- Public tree: 70 files, 135,376,302 bytes, SHA-256
  `6ad3796f44cd34e033e1bd0485b2cad16f6e798b469b614dfbfb0259a3b91269`.
- Determinism: two consecutive clean builds reproduced 25,363 files,
  422,891,379 bytes and tree SHA-256
  `8f75fce90aa962d0df0e55d9b6c98a3fd3a2049cb798cee5b92ea9e7618d612f`.
- Production dependency audit: zero vulnerabilities.
- Release hardening: canonical migration discovery ignores noncanonical
  duplicate migration filenames, while public manifest generation enumerates
  only expected canonical assets. Both safeguards have regression tests.

## Coverage prepared for publication

- Index: 23,978/23,978 source rows linked (100.0000%).
- Research attempted: 15,748/23,936 people (65.7921%).
- Verified affiliation: 1,138/23,936 people (4.7543%).
- Verified employer: 516/23,936 people (2.1557%).
- Archival disposition assessed: 14,223/23,936 people (59.4210%).
- Not started: 8,183 people; in progress: 1,883 people.
- Possible-duplicate groups: 679; conflicts: 531.
- Claim confidence: 1,728 confirmed; 5,337 high; 2,575 medium; 255 low;
  439 conflicting; and 2 unresolved.
- Public projection: 23,936 profiles, 3,954 affiliations, 1,303
  organizations, 6,488 sources and 10,075 published, qualified or conflict
  claims.
- Citations: 7,775 across 4,340 unique source documents.

## Publication verification

- Immutable published release commit:
  `976a7e2e78255919a408ddc64b2159e864daf5a8`.
- GitHub Actions Test run `41641804166` completed successfully.
- GitHub Pages run `41641803447` completed successfully; its deploy job
  completed at `2026-11-03T13:11:33Z`.
- On 2026-11-03, the unauthenticated deployed-release verifier checked the
  live GitHub Pages site against that exact commit and the Batch 992 evidence
  bundle. It verified all 67 public assets (133,029,131 bytes; manifest
  SHA-256
  `6218e159c9c99f82bf28942ac29485da6b9ca7fbbaf74019ff4e241c3b56ddff`),
  all eight core routes, all 44 source-register pages and all 23 direct Batch
  992 profile routes.
- Independent unauthenticated HTTP checks returned status 200 for the home
  page, the oil-company category, and the Bertus Harry Wabeke, John E
  Wachsmuth, Charles S Wade and Frederick J Wadley III profile pages.

Public release URL: <https://therealjameswilson.github.io/before-oss/>.
