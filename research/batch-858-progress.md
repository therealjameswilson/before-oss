# Batch 858 research progress

Date: 2026-10-16 America/New_York

## Scope and source validation

Batch 858 covers the 23 printed personnel rows on NARA index PDF page 419,
rows 1-23, from Albert B Seitz through Helen M Selvig. All 23 immutable source
rows remain preserved and linked to 23 separate active person entities. The
reviewed table preserves names, initials, printed ranks, private identifier
columns, Box 695 and archive location 230/86/40/04. Full service identifiers
remain private.

George C Selvig and Conrad G Selvig remain separate because the current
evidence does not establish that their differently ordered names represent one
person. Harvey T Selee remains separate from a Harvy T Solee index record after
a protected-identifier collision was rejected as proof of identity. Both
review issues use opaque public duplicate labels. The next unresearched
boundary is PDF page 419, row 24, William W Selvig.

## Research outcomes

- Marguerite Osborne Seitzer's Washington Post obituary supports her State
  Department work earlier in World War II followed by OSS cryptographic work
  in the Mediterranean. The State Department is published as a qualified
  probable-immediate government assignment, not as a civilian employer.
- Official National Park Service history identifies Joseph P. Seliquini as an
  OSS Italian Operational Group radio operator. Together with the protected
  Army identity bridge, it supports a high-confidence identity and enlisted
  Army classification, but it does not identify a pre-OSS employer or
  predecessor assignment.
- The official Marine Corps history *Herringbone Cloak--GI Dagger* aligns the
  uncommon George C. Selvig name, captain rank and OSS Yugoslavia context. It
  establishes OSS identity rather than a pre-OSS affiliation. The possible
  George/Conrad name-order duplication remains visible and unresolved.
- Minnesota Historical Society and University of Minnesota records support
  Helen Marion Selvig's identity and prewar university attendance. The
  University of Minnesota is published as a student affiliation, never as an
  employer.
- Official Army data provides identity-only bridges for Donald C Sellman,
  George J Seleno, George R Selby, Harold S Seligmann, Harry G Sells, Joseph M
  Self Jr., Joseph P Seliquini and Lyle E Selix. Army-coded occupation and
  entry fields were not published as employers or OSS ranks.
- A New York Public Library collection description supplied a plausible
  journalism lead for Herbert Seligmann, but no source bridged that namesake to
  the index person. The lead remains rejected for publication and the profile
  remains unresolved.
- CIA and Library of Congress automated discovery failed at their first
  bounded requests because of source-access errors. Those failures are saved
  as access limitations, not negative evidence. Authenticated NARA Catalog
  research remains disabled pending safe credential rotation.

The batch distribution is 11 `high_confidence`, ten `unresolved`, one
`ambiguous` and one `conflicting` identity. One record is `completed`, one is
`conflicting_sources`, and 21 are `requires_archival_review`. All 23 records
have a saved non-planned research attempt and no Batch 858 record remains
`not_started`. The evidence bundle contains eight sources, two reused
organizations, two affiliations, 13 published claims, 23 person updates, 23
research attempts and 27 claim-source links. SQLite's foreign-key check
returned no rows and its integrity check returned `ok`.

## Updated project coverage

- Index coverage: 23,978/23,978 linked source rows (100%).
- Active person entities: 23,937; stored entities: 23,941, including four
  unlinked superseded entities retained for auditability.
- Research-attempt coverage: 12,703 people (53.0685%).
- Verified-employer coverage: 418 people (1.7463%).
- Verified-affiliation coverage: 921 people (3.8476%).
- Archival-review coverage: 11,170 people (46.6642%).
- Not started: 11,229 people.
- Possible duplicate groups: 572.
- Conflicts: 447 people.
- Claim confidence totals: 1,604 confirmed, 4,005 high, 1,704 medium,
  202 low, 373 conflicting and two unresolved.
- Citations: 6,490; unique source documents: 3,491.
- Public projection: 23,937 people, 2,848 affiliations, 1,062 organizations,
  5,259 sources and 7,682 published claims.

Research-attempt and archival-review coverage each increased by all 23 people.
Verified-affiliation coverage increased by Helen Selvig's documented student
affiliation. Verified-employer coverage did not change.

## Validation

Local release validation passed. Python reports 145 tests passing. Astro
checked 492 files with zero errors, warnings or hints and built 25,043 static
pages. The bounded Playwright release suite passed 90/90 checks across Batch
858, core routes, the oil-company category, analytics and accessibility at
desktop, phone and tablet viewports. The stratified 200-profile audit passed
every check. All internal links across 25,043 HTML files resolve; 51,382 unique
external URLs were inventoried separately. The public-identifier audit found
zero unexpected boundary matches after checking 12,926 normalized identifiers
and 120 formatted variants across 25,115 built artifacts.

The public manifest covers 67 assets totaling 116,012,998 bytes with SHA-256
`0d3f90dc101ef769f19745e1e9182cda3c5cd0edfa9b75365d97a22a2b031309`.
Two production builds produced the identical 25,115-file tree hash
`179aaba5410208d7f179693e410a7773af01b3dfa06ad22987fc26ea19776a6c`.

## Publication status

Published from content commit
`4037fe2e4d211c17b0b738dbcd7f8cf093a9f8b4`. GitHub Pages run
`38953214685` and Test run `38953214654` completed successfully. The
unauthenticated immutable verifier checked all 67 manifested assets
(116,012,998 bytes), eight core routes, 36 source-register pages and all 23
direct profile routes referenced by the evidence bundle at
`https://therealjameswilson.github.io/before-oss/`. The live manifest SHA-256
is `0d3f90dc101ef769f19745e1e9182cda3c5cd0edfa9b75365d97a22a2b031309`,
matching the reviewed release. Live statistics report 12,703
research-attempted people, 418 verified-employer profiles, 921
verified-affiliation profiles and 11,170 people with archival-review
assessment. The overall every-person research goal remains active.

## Resume commands

```bash
.venv/bin/python -m oss_research --db research/research.sqlite import-review-decisions research/army_review_decisions_2026-10-16_batch858.csv
.venv/bin/python -m oss_research --db research/research.sqlite import-reviewed-evidence research/evidence-page419-seitz-selvig-review_batch-858_2026-10-16.json
.venv/bin/python -m oss_research --db research/research.sqlite export-derived
.venv/bin/python -m oss_research --db research/research.sqlite export-review-queue
.venv/bin/python -m oss_research --db research/research.sqlite build-public-data
.venv/bin/python -m oss_research --db research/research.sqlite coverage-report
.venv/bin/python -m oss_research --db research/research.sqlite audit-profiles --sample-size 200
.venv/bin/python -m unittest discover -s tests -v
npm --prefix site run build
npm --prefix site run test:release
npm --prefix site run check:links
.venv/bin/python scripts/verify_deployed_release.py --local-public-root site/public
.venv/bin/python scripts/audit_public_identifiers.py --database research/research.sqlite --public-root site/dist
.venv/bin/python scripts/hash_tree.py site/public site/dist
.venv/bin/python -m oss_research --db research/research.sqlite assign-page-batch --batch-name batch-859 --page 419 --first-row 24 --last-row 46
```
