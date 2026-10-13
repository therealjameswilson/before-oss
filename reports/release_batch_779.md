# Batch 779 release record

Date: 2026-10-13 America/New_York

## Scope

Batch 779 covers PDF page 379, rows 24-46, Alvin G Psinas through Michael C
Puleo. All 23 printed rows remain preserved and linked to 23 distinct person
entities. Every person received a saved, terminal research outcome. The next
indexed boundary is page 380, row 1.

## Research outcome

- The batch records 22 `requires_archival_review` outcomes and one
  `occupation_only_found` outcome.
- Udom Puhpadhana has a high-confidence identity match and a documented 1942
  Miami University student affiliation. Student status is not employment and
  is not labeled the immediate pre-OSS affiliation.
- National Park Service history provides a high-confidence match for George N.
  Psoinos as a Greek-American radio operator on the OSS Peking mission. No
  pre-OSS employer is inferred.
- Ten official Army identity candidates were accepted. Coded Army occupations
  were retained only as identity evidence and were never converted into
  employers.
- Two identity candidates were rejected. One mapped George J Pugliese to a
  wholly different official Army name. The other mapped Peter N Pugliese to
  Peter F Pugliese even though the index preserves separate Peter N and Peter F
  rows.
- A 1958 Signal Oil directory entry for a Leo F Ptacek was rejected as postwar
  and unbridged to the index row. It does not appear in the public oil-company
  category or as an affiliation.
- NARA Catalog work was dry-run only: 23 searches planned and zero authenticated
  requests made. CIA access failed closed; Library of Congress completed three
  no-result checks before a later request stalled. Source-access limitations
  were not treated as negative historical evidence.

## Exact coverage at export

- Index: 23,978/23,978 linked rows (100%).
- Active person entities: 23,939.
- Research attempted: 10,917/23,939 (45.6034%).
- Verified employer: 356/23,939 (1.4871%).
- Verified affiliation: 799/23,939 (3.3376%).
- Archival review assessed: 9,376/23,939 (39.1662%).
- Not started: 13,017.
- Possible duplicate groups: 542.
- Conflicts: 369.
- Claims: 1,410 confirmed; 3,382 high; 1,590 medium; 202 low; 322
  conflicting; two unresolved.
- Citations: 5,966 records representing 3,078 unique source documents.
- Public data: 2,591 published affiliations, 923 organizations, 4,741 public
  sources, and 6,700 published claims.
- Research statuses: one `blocked_by_source_access`; 333 `candidate_found`; 198
  `completed`; 313 `conflicting_sources`; 182
  `documented_prewar_employer_found`; 1,901 `in_progress`; 535
  `needs_identity_review`; 25 `needs_temporal_review`; 1,156
  `no_reliable_result_after_protocol`; 13,017 `not_started`; 1,058
  `occupation_only_found`; 4,916 `requires_archival_review`; and 304
  `verified_employer_found`.

## Local release gates

- Python: 141 tests passed, including 81 parameterized subtests.
- Astro: 413 source files checked with zero errors, warnings, or hints; 24,902
  HTML pages built.
- Browser: 87/87 desktop, phone, tablet, analysis, and accessibility checks
  passed: 18 Batch 779 checks, 33 core-site checks, six analysis checks, and 30
  axe checks.
- Links: all 24,902 generated HTML files passed internal-link checks; 50,941
  unique external URLs were inventoried.
- Redaction: zero unexpected private-identifier boundary matches across 24,974
  artifacts.
- Dependencies: the production audit found zero vulnerabilities.
- Manifest: 67 assets, 109,490,313 bytes, SHA-256
  `a0e952861af55a4967e27cf5389284e47024ee427ba67d5acad5bde6d67c9cfc`.
- Determinism: two consecutive builds produced public-tree SHA-256
  `cedef3bc048ed08ff5583e786e58585c363782152c792da9641659cf5da926f8`
  across 70 files and 111,837,457 bytes, and production-tree SHA-256
  `c3b95f91cf0d64f44412d1edebb9d08f9496763580fa7af3da8f1b4ba144b65f`
  across 24,974 files and 313,718,011 bytes.

## Publication

- Release commit:
  `4ccec3ed8002cd5f05cf558a48570125896c434f`.
- The [Deploy GitHub Pages workflow](https://github.com/therealjameswilson/before-oss/actions/runs/38424730707)
  completed successfully.
- The [Test workflow](https://github.com/therealjameswilson/before-oss/actions/runs/38424730635)
  completed successfully.
- Immutable live verification against the release commit confirmed all 67
  manifest assets and 109,490,313 bytes, all eight core routes, all 32 source
  register pages, and all 23 directly affected profile routes. The deployed
  manifest SHA-256 is
  `a0e952861af55a4967e27cf5389284e47024ee427ba67d5acad5bde6d67c9cfc`.
- Live site: <https://therealjameswilson.github.io/before-oss/>.

Both workflows emitted maintenance notices that selected GitHub actions still
target Node.js 20 and that `ubuntu-latest` is scheduled to migrate to Ubuntu 26.
GitHub ran the affected actions on Node.js 24; neither notice failed or altered
this release.

The full project remains unfinished. Batch 779 is published, but 13,017 active
person entities remain `not_started`; work resumes at page 380, row 1.
