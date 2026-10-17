# Batch 862 research progress

Date: 2026-10-17 America/New_York

## Scope and source validation

Batch 862 covers the 23 printed personnel rows on NARA index PDF page 421,
rows 1-23, from Eugene Shaffer through John A Shannon. All 23 immutable source
rows remain preserved and linked to 23 separate active person entities. The
reviewed table preserves names, initials, printed ranks, private identifier
columns, Boxes 698-699 and archive location 230/86/40/04. Full service
identifiers remain private. The next unresearched boundary is PDF page 421,
row 24.

## Research outcomes

- An official National Park Service history identifies John M. Shaheen as the
  OSS officer who served on the McGregor Mission and describes him as a former
  publicity director for the Republican Party in Illinois. The political work
  is published as a documented-prewar professional affiliation because the
  source does not establish the legal employer or compensation. It is not
  marked immediate. Shaheen's postwar oil career was deliberately excluded.
- An official OSS Mission to France award document exactly matches Lawrence B.
  Shallcross's name, rank and leading-zero-normalized protected identifier. It
  confirms his identity but supplies no pre-OSS employer or transition
  chronology.
- A 1948 United Nations roster supplies the probable identity variant
  `Muddassir Ali Shamsee`. Because it is postwar, it remains identity context
  only and does not become pre-OSS employment.
- A specialized historical account supports a probable match for Jack T.
  "Black Jack" Shannon and a visibly qualified medium-confidence U.S. Army
  lieutenant-to-OSS recruitment pathway in early 1944. It does not establish
  a civilian employer, and Box 699 remains necessary for primary confirmation.
- Official Army bulk data supplies identity-only bridges for Theodore F.
  Shaffer, John J. Shanahan, Robert J. Shane, Julius L. Shanker and John A.
  Shannon. The official source's `Shanhan` spelling is preserved as evidence,
  not silently corrected. Army-coded occupation and entry fields were not
  published as employers, OSS ranks or affiliations.
- Julius A. Shanker remains a separate unresolved person entity from the
  adjacent, independently identified Julius L. Shanker row. Incompatible or
  insufficient namesake results for the remaining people were rejected rather
  than converted into claims. Authenticated NARA Catalog research remains
  disabled pending safe credential rotation.

The batch distribution is two `confirmed`, five `high_confidence`, two
`probable` and 14 `unresolved` identities. All 23 records are
`requires_archival_review`. Every person has a saved non-planned research
attempt and no Batch 862 record remains `not_started`. The evidence bundle
contains six sources, two organizations, two affiliations, 11 published or
qualified claims, 23 person updates, 23 research attempts and 20 embedded
claim-source links. Five Army candidates were individually reviewed and
accepted. SQLite's foreign-key check returned no rows and its integrity check
returned `ok`.

## Updated project coverage

- Index coverage: 23,978/23,978 linked source rows (100%).
- Active person entities: 23,937; stored entities: 23,941, including four
  unlinked superseded entities retained for auditability.
- Research-attempt coverage: 12,795 people (53.4528%).
- Verified-employer coverage: 422 people (1.7630%).
- Verified-affiliation coverage: 930 people (3.8852%).
- Archival-review coverage: 11,262 people (47.0485%).
- Not started: 11,137 people.
- Possible duplicate groups: 572.
- Conflicts: 447 people.
- Claim confidence totals: 1,610 confirmed, 4,053 high, 1,712 medium,
  202 low, 373 conflicting and two unresolved.
- Citations: 6,522; unique source documents: 3,514.
- Public projection: 23,937 people, 2,863 affiliations, 1,070 organizations,
  5,291 sources and 7,744 published or qualified claims.

Research-attempt and archival-review coverage each increased by all 23 people.
Verified-affiliation coverage increased by John M. Shaheen. Verified-employer
coverage did not change because the political role is not supported as a named
employment relationship and no other Batch 862 source establishes an employer
at the publication threshold.

## Validation

Local release validation passed. Python reports 145 tests and 81 parameterized
subtests passing. Astro checked 496 files with zero errors, warnings or hints
and built 25,051 static pages. The bounded Playwright release suite passed
87/87 checks across Batch 862, core routes, the oil-company category, analytics
and accessibility at desktop, phone and tablet viewports. The stratified
200-profile audit passed every check. All internal links across 25,051 HTML
files resolve; 51,407 unique external URLs were inventoried separately. The
public-identifier audit found zero unexpected boundary matches after checking
12,926 normalized identifiers and 120 formatted variants across 25,123 built
artifacts.

The public manifest covers 67 assets totaling 116,402,851 bytes with SHA-256
`2198dfb8729d7f05ebb21ae38da809d413512dec95bcd39e5df8691bb657eaf9`.
Two production builds produced the identical 25,123-file tree hash
`ecb5d33b2b899e3ae90107eaf590c01a84344f7060abd7f97809c9d5fed0b3ee`.

## Publication status

Local release gates are complete. Publication and unauthenticated live
verification are pending.

## Resume commands

```bash
.venv/bin/python -m oss_research --db research/research.sqlite import-review-decisions research/army_review_decisions_2026-10-17_batch862.csv
.venv/bin/python -m oss_research --db research/research.sqlite import-reviewed-evidence research/evidence-page421-shaffer-shannon-review_batch-862_2026-10-17.json
.venv/bin/python -m oss_research --db research/research.sqlite export-derived
.venv/bin/python -m oss_research --db research/research.sqlite export-review-queue
.venv/bin/python -m oss_research --db research/research.sqlite build-public-data
.venv/bin/python -m oss_research --db research/research.sqlite coverage-report
.venv/bin/python -m oss_research --db research/research.sqlite audit-profiles --sample-size 200
.venv/bin/python -m pytest -q
npm --prefix site run build
npm --prefix site run test:release
npm --prefix site run check:links
.venv/bin/python scripts/verify_deployed_release.py --local-public-root site/public
.venv/bin/python scripts/audit_public_identifiers.py --database research/research.sqlite --public-root site/dist
.venv/bin/python scripts/hash_tree.py site/public site/dist
```
