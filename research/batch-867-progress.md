# Batch 867 research progress

Date: 2026-10-17 America/New_York

## Scope and source validation

Batch 867 covers the 23 printed personnel rows on NARA index PDF page 423,
rows 24-46, from John M Shepard through Harold S Sheridan. All 23 immutable
source rows remain preserved and link to 23 active person entities. The
reviewed table preserves original names, initials, printed ranks, the note
`From Vo`, private identifier columns, Box 703 and archive location
230/86/40/05. Full service and officer numbers remain private. The next
unresearched boundary is the first unassigned row after page 423, row 46.

## Research outcomes

- A Case Western Reserve University institutional biography identifies Jesse
  Hauk Shera and supplies a continuous employment sequence: Scripps Foundation
  for Research in Population Problems, 1928-40; Library of Congress, 1940-41;
  and OSS, 1941-44. The Library of Congress is modeled as Shera's strongly
  date-bounded immediate affiliation and last civilian government employer.
  Scripps remains a separate earlier documented prewar employer. No job title
  is inferred where the source supplies none.
- Exact names and nonshared protected identifiers support official Army
  identity bridges for Bernard T. P. Sherer, Cleatus E. Sheperd, Ervin L.
  Sherbrooke, John M. Shepard, Lee L. Sherdell, Robert L. Sherbert, Stanley J.
  Shepard, Thomas A. Sherard, William H. Sherertz and William S. Sheppard.
  Army entry-grade and occupation codes remain private and are not converted
  into employers, OSS ranks or predecessor assignments.
- The Army row attached to Louis W. Sherack's protected identifier names a
  different person. A 1943 contemporary newspaper documents a Private Louis
  Sherack formerly employed as a Minneapolis restaurant chef, but it neither
  connects him to OSS or Box 703 nor reconciles the rank difference with the
  indexed Captain. The conflict is published as a conflict; the chef lead is
  not published as Sherack's pre-OSS employment.
- A distinctive-name obituary for Charles A. Sheputa and a 1956 newspaper
  item naming Edith Sherbine are retained as low-confidence review leads only.
  Neither supplies the corroborating OSS, Box 703 or protected-identifier
  bridge required for a public factual claim.
- CIA-domain, NARA Catalog-domain, Library of Congress, exact-name OSS,
  employment, occupation, obituary, newspaper, institutional and archival
  searches were completed for the bounded cohort. The CIA adapter respected a
  robots restriction; the LoC adapter recorded two no-candidate results and a
  saved service error before source-wide probing stopped. Those access results
  were not treated as negative historical evidence. Authenticated NARA Catalog
  research remains disabled pending safe credential rotation.

The batch distribution is 12 `high_confidence`, two `ambiguous`, one
`conflicting` and eight `unresolved` identities. Jesse H Shera is
`verified_employer_found`, Louis W Sherack is `conflicting_sources`, and the
remaining 21 people are `requires_archival_review`. Every person has at least
one saved non-planned attempt; the cohort contains 28 total attempts because
bounded source-adapter checks supplement the 22 new manual attempts and
Whitney Shepardson already had a terminal preexisting review. No Batch 867
person remains `not_started` or `in_progress`.

The evidence bundle contains seven sources, two organizations, two
affiliations, 17 claims, 22 person updates, 22 manual research attempts and 33
embedded claim-source links. Ten Army candidates were accepted for identity
only and one was rejected. Reimporting both review files is idempotent.
SQLite's integrity check returned `ok`, and its foreign-key check returned no
rows.

## Updated project coverage

- Index coverage: 23,978/23,978 linked source rows (100%).
- Active person entities: 23,937; stored entities: 23,941, including four
  unlinked superseded entities retained for auditability.
- Research-attempt coverage: 12,907 people (53.9207%).
- Verified-employer coverage: 426 people (1.7797%).
- Verified-affiliation coverage: 938 people (3.9186%).
- Archival-review coverage: 11,374 people (47.5164%).
- Not started: 11,025 people.
- Possible duplicate groups: 579.
- Conflicts: 448 people.
- Claim confidence totals: 1,612 confirmed, 4,101 high, 1,712 medium,
  205 low, 374 conflicting and two unresolved.
- Citations: 6,554; unique source documents: 3,539.
- Public projection: 23,937 people, 2,873 affiliations, 1,076 organizations,
  5,320 sources and 7,795 published or qualified claims.

Relative to Batch 866, research-attempt and archival-review coverage each
increased by 22 people because Whitney Shepardson already had a prior terminal
review. Verified-employer and verified-affiliation coverage each increased by
one person. Fourteen new high-confidence public claims and one conflicting
claim document identity or pre-OSS pathways. Two low-confidence namesake leads
remain outside the public claim and source registers.

## Validation

Local release validation passed. Python reports 145 tests and 81 parameterized
subtests passing. The stratified 200-profile audit passed every check. Astro
checked 501 files with zero errors, warnings or hints and built 25,057 static
pages. The bounded Playwright release suite passed 87/87 checks across Batch
867, core routes, the oil-company category, analytics and accessibility at
desktop, phone and tablet viewports. All internal links across 25,057 HTML
files resolve; 51,431 unique external URLs were inventoried separately. The
public-identifier audit found zero unexpected boundary matches after checking
12,926 normalized identifiers and 120 formatted variants across 25,129 built
artifacts.

The public manifest covers 67 assets totaling 116,746,847 bytes with SHA-256
`4ab4f074fc6e8e850cc55a5818629916f97592d436e65908fdedf47dc4ced83f`.
Two production builds produced the identical 25,129-file static-site hash
`95dabb23c8b2b7d3a970d499da5fbc0010a618d5cc5762f4e07442102d522602`.

## Publication status

Batch 867 has passed local release gates but has not yet been published. The
current public site remains Batch 866 at
<https://therealjameswilson.github.io/before-oss/>.

## Resume commands

```bash
.venv/bin/python -m oss_research --db research/research.sqlite import-review-decisions research/army_review_decisions_2026-10-17_batch867.csv
.venv/bin/python -m oss_research --db research/research.sqlite import-reviewed-evidence research/evidence-page423-shepard-sheridan-review_batch-867_2026-10-17.json
.venv/bin/python -m oss_research --db research/research.sqlite export-adapter-checkpoints
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
