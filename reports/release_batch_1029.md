# Batch 1029 release audit

Date: 2026-11-04 America/New_York

## Release contents

- NARA index page 519, rows 1-46: Francis S. Yuhashi through Joseph S.
  Zbeig. All 46 printed rows remain separately recoverable as 46 cautious
  person entities. The page 520 boundary was also visually checked.
- Every cohort person has a saved terminal outcome: 19
  `requires_archival_review`, 19 `occupation_only_found`, four
  `needs_temporal_review`, two `needs_identity_review`, and two
  `conflicting_sources`.
- Twenty-two protected-identifier Army candidates received explicit review:
  18 accepted, two rejected, and two retained as conflicting. Shared,
  damaged, post-OSS, and undefined records were not converted into
  occupations or employers.
- Sylvia B. Zagoria's documented 1943 Brooklyn College transition is modeled
  as student status, not employment. Her earlier unnamed summer-camp dance
  instruction remains a separate, qualified occupation-only affiliation.
- David D. Zagier's publisher biography supports journalism as his
  best-supported last civilian occupation before OSS recruitment, but does
  not name an employer; none is invented.
- Wilhelm Zagorski/Zagórski's last documented civilian occupation as a
  railway worker is separated from his later coerced German Army assignment.
- Edward B. Zarembo is the cohort's only newly documented commissioned
  officer. His West Point cadet status and Quartermaster Corps military
  assignment remain separate and neither is labeled civilian employment.
- Daniel A. Zaret's Lincoln Brigade service is modeled as a volunteer
  affiliation. Dim V. Zaikowsky's film-technician directory entry remains
  temporally qualified. Archie C. Zarkadas's 1939 National Guard service is
  a documented prewar military affiliation, not an employer.
- Frank V. Zabatta's likely duplicate relationship and Asa Zatz's damaged
  Army-name link remain explicit conflicts; neither produces an affiliation
  claim.
- No authenticated NARA Catalog API request was used.

## Evidence and import

- Reviewed evidence bundle: 17 sources, seven organizations, 26
  affiliations, 42 claims, 99 claim-source links, 46 person updates, and 46
  research attempts.
- Twenty-two Army identity-review decisions were imported. The decision and
  evidence imports were tested twice against a disposable database before
  the durable database update; repeated import was idempotent.
- Post-import SQLite integrity and foreign-key checks passed with zero
  violations.
- Evidence-bundle SHA-256:
  `58612b3e91d0911e2145f52e37ba1d8c4ab29e27950bdaf022c8eb47c2aa07c9`.

## Coverage prepared for publication

- Index: 23,978/23,978 source rows linked (100.0000%).
- Research attempted: 17,254/23,935 people (72.0869%).
- Verified affiliation: 1,211/23,935 people (5.0595%).
- Verified employer: 553/23,935 people (2.3104%).
- Archival disposition assessed: 15,735/23,935 people (65.7405%).
- Not started: 6,676 people; in progress: 1,879 people.
- Research outcomes include 2,009 `occupation_only_found`, 9,659
  `requires_archival_review`, 466 `verified_employer_found`, 297
  `documented_prewar_employer_found`, 610 `needs_identity_review`, 47
  `needs_temporal_review`, and 483 `conflicting_sources` people.
- Claim confidence: 2,016 confirmed; 5,571 high; 2,997 medium; 261 low; 467
  conflicting; and two unresolved.
- Public projection: 23,935 profiles, 4,480 affiliations, 1,391
  organizations, 6,815 sources, and 11,047 published, qualified, or conflict
  claims.
- Citations: 8,108 across 4,558 unique source documents.
- Possible duplicate groups: 699. Total conflict flags: 563.

## Local publication verification

- Python: all 214 tests and 87 subtests passed. Batch 1029's eight focused
  evidence tests and complete schema validation are included.
- Clean Astro check: 660 files with zero errors, warnings, or hints.
- Clean static build: 25,380 pages.
- Bounded browser release suite: 93/93 checks passed across desktop, phone,
  and tablet: 24 Batch 1029 checks, 33 core-route and interaction checks, six
  analysis checks, and 30 accessibility scans with no serious axe
  violations.
- Internal links: 25,380 HTML files checked; all links resolve. The checker
  inventoried 52,476 unique external URLs separately.
- Checked-in public manifest: 67 canonical assets, 140,489,074 bytes,
  SHA-256
  `78ab323328ea2fc5e7d5082e10e1bae80b341f4dc24747143dd5ceea43fb4e43`.
- Public-identifier audit: 25,452 public artifacts checked against 12,926
  normalized private identifiers and 120 formatted variants. It inspected
  1,585 candidate substrings and found zero aggregate, manifest-size, or
  unexpected boundary matches.
- Two consecutive local builds reproduced 25,452 artifacts totaling
  435,318,831 bytes at output-tree SHA-256
  `2321dd2f072e4706aa2ec705c8d05c39a05c85a0df2684696b4b34272f2cd025`.

## Deployment status

- Publication commit:
  `606f7d6074553d483d73e01fdbced7c238e28d0e`.
- GitHub Actions Test run
  [41894266937](https://github.com/therealjameswilson/before-oss/actions/runs/41894266937)
  passed, including the complete Python suite, checked-in manifest check,
  bounded browser release suite, and public-identifier audit.
- GitHub Pages run
  [41894266883](https://github.com/therealjameswilson/before-oss/actions/runs/41894266883)
  built and deployed successfully.
- The read-only immutable-commit verifier matched all 67 canonical public
  assets (140,489,074 bytes) to manifest SHA-256
  `78ab323328ea2fc5e7d5082e10e1bae80b341f4dc24747143dd5ceea43fb4e43`.
  It also verified eight core routes, all 46 source-register pages, and all 46
  direct Batch 1029 profile routes.
- Public base URL:
  <https://therealjameswilson.github.io/before-oss/>.
