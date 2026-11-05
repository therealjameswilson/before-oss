# Batch 1037 release audit

Date: 2026-11-04 America/New_York

## Release contents

- NARA index page 292, rows 1-46: Robert Maloof through Gottfried T. Mann.
  All 46 rows remain separately recoverable as 46 cautious person entities,
  and all now have saved terminal research outcomes.
- The cohort contains 23 `requires_archival_review`, 15
  `occupation_only_found`, four `needs_identity_review`, two
  `verified_employer_found`, one `needs_temporal_review`, and one `completed`
  outcome.
- Twenty-one protected-identifier Army candidates received explicit review:
  18 exact-name, nonshared candidates were accepted and three were rejected.
  No fields were transferred from either shared-identifier Marcus Manaloe
  candidate or the different-name Morton C. Menaugh candidate.
- Sixteen accepted Army-entry records support broad, date-bounded occupation
  or student categories only. Codes 993 and 999 remain uninterpreted, and no
  coded occupation was converted into a named employer, institution,
  workplace, or immediate pre-OSS affiliation.
- A Bancroft Library finding aid supports the University of Minnesota as
  David G. Mandelbaum's immediate affiliation and last civilian employer: it
  states that he went to OSS while on leave from the university.
- Deutsche Biographie and OCLC authority records identify indexed Gottfried
  T. Mann as Golo Mann, born Angelus Gottfried Thomas Mann. His 1942-43 Olivet
  College history lectureship is the best-supported last civilian employment
  before U.S. Army/OSS service beginning in 1943.
- Erika Mann's 1942 Office of War Information work remains a qualified earlier
  government assignment, not an immediate or last-civilian-employer claim.
  NARA's 1943 OSS letter description supports identity and wartime context.
- National Park Service history supports Major Cyrus E. Manierre Jr.'s OSS
  Team Dodge identity but not an earlier employer or immediately preceding
  military assignment.
- The malformed numeric value printed in Nicholas M. Mancini's rank column
  was visually confirmed and preserved without silent correction.
- No authenticated NARA Catalog API request was used.

## Evidence and import

- Reviewed evidence bundle: ten sources, three organizations, 19
  affiliations, 25 claims, 85 claim-source links, 46 person updates, and 46
  research attempts.
- Twenty-one Army identity-review decisions were imported. Decision and
  evidence imports were tested against a disposable database before the
  durable update.
- A pre-import SQLite backup is retained at
  `/private/tmp/before-oss-pre-b1037-20261104.sqlite` for local recovery.
- Post-import SQLite integrity and foreign-key checks passed with zero
  violations; every new public claim has citation links.
- Evidence-bundle SHA-256:
  `e02b97c7751a96b23f3868289370216de06b27d84842cee8ac9e42b984ed3749`.

## Coverage prepared for publication

- Index: 23,978/23,978 source rows linked (100.0000%).
- Research attempted: 17,538/23,935 people (73.2734%).
- Verified affiliation: 1,226/23,935 people (5.1222%).
- Verified employer: 560/23,935 people (2.3397%).
- Archival disposition assessed: 16,057/23,935 people (67.0859%).
- Not started: 6,392 people; in progress: 1,832 people.
- Research outcomes include 2,121 `occupation_only_found`, 9,836
  `requires_archival_review`, 472 `verified_employer_found`, 298
  `documented_prewar_employer_found`, 633 `needs_identity_review`, 51
  `needs_temporal_review`, and 487 `conflicting_sources` people.
- Claim confidence: 2,022 confirmed; 5,608 high; 3,115 medium; 261 low; 473
  conflicting; and two unresolved.
- Public projection: 23,935 profiles, 4,619 affiliations, 1,402
  organizations, 6,894 sources, and 11,214 published, qualified, or conflict
  claims.
- Citations: 8,187 across 4,605 unique source documents.
- Possible duplicate groups: 703. Total conflict flags: 569.

## Local publication verification

- Python: 283 pytest cases and 87 subtests passed.
- Clean Astro check: 668 files with zero errors, warnings, or hints.
- Clean static build: 25,391 pages and 25,463 total output artifacts.
- Bounded browser release suite: 87/87 checks passed across desktop, phone,
  and tablet: 18 Batch 1037 checks, 33 core-route and interaction checks, six
  analysis checks, and 30 accessibility scans with no serious axe violations.
- Internal links: 25,391 HTML files checked; all links resolve. The checker
  inventoried 52,520 unique external URLs separately.
- Checked-in public manifest: 67 canonical assets, 141,989,514 bytes,
  SHA-256
  `6f0e223474cbb95c493f8d17bc983a62de856b4e78cbfdc28a890e46e6838dc5`.
- Public-identifier audit: 25,463 output artifacts checked against 12,926
  normalized private identifiers and 120 formatted variants. It inspected
  1,586 candidate substrings and found zero aggregate, manifest-size, or
  unexpected boundary matches.
- Two consecutive local builds reproduced 25,463 artifacts totaling
  437,795,241 bytes at output-tree SHA-256
  `ee794f6ab3c799f50740962502ef8a37fda0fc55cd71b99927c8622e1892144b`.
- The complete 522-page ingest audit and deterministic 200-profile stratified
  audit passed all defined gates.

## Deployment status

- Publication commit: pending.
- GitHub Actions Test run: pending.
- GitHub Pages run: pending.
- Deployed immutable-release verification: pending.
- Public base URL:
  <https://therealjameswilson.github.io/before-oss/>.
