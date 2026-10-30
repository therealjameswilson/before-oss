# Batch 965 release audit

Date: 2026-10-29 America/New_York

## Release contents

- NARA index page 473, rows 1-23: Edward M Trevaskis through Barry Trivers.
  Michael J Troisi at page 473 row 24 is the next cohort boundary.
- All 23 researched source rows remain separate people and every person in the
  cohort has a saved terminal research outcome.
- Six exact Army identity bridges publish only qualified dated occupation
  categories. Two identifier-agreeing but name-conflicting Army candidates are
  rejected and contribute no biographical fields.
- Original or authoritative records document Arthur Trevor-Wilson, Philip
  Trezise, Richard Trevett, Vincent Trifletti and Arthur Tritsch. Glenn
  Trewartha, Bonnell Tripcony, Vaso Trivanovitch and Barry Trivers remain
  visibly qualified where the public OSS identity bridge is incomplete.
- Seven unresolved identities retain archival-review outcomes rather than
  facts transferred from unbridged namesakes.
- No authenticated NARA Catalog API request was used. The evidence-defined
  oil-company category remains unchanged at 14 people linked to 15 historically
  named companies.

## Reproducible local release checks

- Evidence-bundle SHA-256:
  `351554002978c65a7fe167204188c6bdd396bbd21e61b43639d309e0194d0aee`.
- The durable import records 8 review decisions, 14 affiliations, 30 claims,
  23 person updates, 23 research attempts, 15 sources and 60 claim-source
  links; repeated imports are idempotent. SQLite integrity is ok and
  foreign-key violations are zero.
- PDF extraction validation: 23,978 rows across 522 pages; all checks pass.
- Stratified profile audit: 200/200 profiles pass every check.
- Python: 147 tests pass.
- Astro: 596 files checked with zero errors, warnings or hints; 25,226 static
  pages built.
- Batch browser suite: 27/27 checks pass on desktop, phone and tablet.
- Browser release suite: 96/96 checks pass across desktop, phone, tablet and
  accessibility coverage, including 30 axe scans with no serious or critical
  violations.
- Internal links: 25,226 HTML files checked; all links resolve. The checker
  separately inventories 52,005 unique external URLs for bounded live checks.
- Identifier audit: 12,926 normalized identifiers and 120 formatted variants
  checked across 25,298 public artifacts; 1,422 candidate substrings were
  inspected and there were zero unexpected boundary matches.
- Public manifest: 67 assets, 129,017,691 bytes, SHA-256
  `0dd517ac3f58c9bd915d23b8c846ee8e27ff3963744ef1ab9ef9601480542ad4`.
- Public tree: 70 files, 131,364,857 bytes, SHA-256
  `a7ac32c1618fca110e81d041eed3fb65953d792110caefafe59e4e54aab0a6c2`.
- Two consecutive output trees: 25,298 files and 416,224,328 bytes each, with
  identical SHA-256
  `0d6c2d8c38bb2ada81318b3505a31b5b474d6bd658fa949265731d9150329ada`.
- Production dependency audit: zero vulnerabilities. Development tooling is
  not shipped with the static site.

## Coverage prepared for publication

- Index: 23,978/23,978 source rows linked (100.0000%).
- Research attempted: 15,131/23,936 people (63.2144%).
- Verified affiliation: 1,085/23,936 people (4.5329%).
- Verified employer: 486/23,936 people (2.0304%).
- Archival disposition assessed: 13,607/23,936 people (56.8474%).
- Not started: 8,800 people; in progress: 1,883 people.
- Durable research attempts or plans: 29,349.
- Possible-duplicate groups: 663; conflicts: 519.
- Claim confidence: 1,699 confirmed; 5,029 high; 2,356 medium; 254 low;
  433 conflicting; 2 unresolved.
- Public projection: 23,936 profiles, 3,679 affiliations, 1,240 organizations,
  6,187 sources and 9,513 claims.
- Evidence ledger: 7,471 citations across 4,144 unique source documents.

## Replay disclosure

- Batch 965 evidence and review decisions replay idempotently.
- The older global replay limitation disclosed in Batch 959 remains: 473
  pre-Batch-959 person-level research-status changes are not yet represented
  in durable replay inputs. The integrity-checked current research database
  remains authoritative for the public projection.
- This release does not claim that the older global replay gap has been
  repaired.

## Publication verification

Pending immutable-commit deployment and unauthenticated live verification.
