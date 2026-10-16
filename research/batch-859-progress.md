# Batch 859 research progress

Date: 2026-10-16 America/New_York

## Scope and source validation

Batch 859 covers the 23 printed personnel rows on NARA index PDF page 419,
rows 24-46, from William W Selvig through Anthony Serao. All 23 immutable
source rows remain preserved and linked to 23 separate active person entities.
The reviewed table preserves names, initials, printed ranks, private identifier
columns, Boxes 695-696 and archive location 230/86/40/04. Full service
identifiers remain private. The unfamiliar printed abbreviation `CAMDR` for
John W Senter remains verbatim and was not forced into a military category.
The next unresearched boundary is PDF page 420, row 1, Walter Sereda.

## Research outcomes

- A Smithsonian Archives of American Art finding aid provides the strongest
  identity bridge for Peter Howard Selz and documents Columbia University
  attendance in 1937-1938. Columbia is published as a student affiliation,
  never as an employer or an immediate predecessor to OSS.
- A 1944 OSS board report directly identifies Mario V. Semolich and records
  his last civilian work as a cook at the Palmer House in Chicago. The Palmer
  House is published as his strongly date-bounded last civilian employer
  before Army and OSS service, not as an immediate pre-OSS affiliation.
- A separate 1944 OSS board report directly identifies Amos E. Sentman and
  states that he served in the Regular Army from November 1917 until assignment
  to OSS in September 1942. The Regular Army is therefore published as his
  explicit immediate military affiliation; no civilian employer is inferred.
- The official Congressional Record supports a high-confidence identity for
  Amato A. Semenza through his uncommon name and documented service with the
  32d Signal Center Team and Psychological Warfare Branch in North Africa and
  Italy. That wartime context does not establish a pre-OSS employer or
  immediate predecessor, so the profile remains assigned for archival review.
- An OSS Operational Groups roster and an official Army identity bridge place
  Hercules J. Sembrakis in Greek Operational Group II and support enlisted Army
  classification. A secondary Greek Army lead was not strong enough to publish
  as a pre-OSS affiliation.
- Official Army data provides identity-only bridges for Alfonso A Senatore,
  Antonino J Seminara, August V Sepetauc, Frank J Senft (spelled `Senfft` in the
  Army record), Frederick A Senger, Hercules J Sembrakis, Lester L Seng, Mario
  V Semolich and Royal F Sengstacken Jr. Army-coded occupation and entry fields
  were not published as employers, OSS ranks or pre-OSS affiliations.
- CIA and Library of Congress automated discovery failed at their first
  bounded requests because of source-access errors. Those failures are saved
  as access limitations, not negative evidence. Authenticated NARA Catalog
  research remains disabled pending safe credential rotation.

The batch distribution is two `confirmed`, ten `high_confidence` and eleven
`unresolved` identities. One record is `completed`, one is
`verified_employer_found`, and 21 are `requires_archival_review`. All 23
records have a saved non-planned research attempt and no Batch 859 record
remains `not_started`. The evidence bundle contains six sources, three
organizations, three affiliations, 15 published claims, 23 person updates, 23
research attempts and 29 claim-source links. Nine Army candidates were
individually reviewed and accepted. SQLite's foreign-key check returned no rows
and its integrity check returned `ok`.

## Updated project coverage

- Index coverage: 23,978/23,978 linked source rows (100%).
- Active person entities: 23,937; stored entities: 23,941, including four
  unlinked superseded entities retained for auditability.
- Research-attempt coverage: 12,726 people (53.1646%).
- Verified-employer coverage: 419 people (1.7504%).
- Verified-affiliation coverage: 924 people (3.8601%).
- Archival-review coverage: 11,193 people (46.7602%).
- Not started: 11,206 people.
- Possible duplicate groups: 572.
- Conflicts: 447 people.
- Claim confidence totals: 1,608 confirmed, 4,016 high, 1,704 medium,
  202 low, 373 conflicting and two unresolved.
- Citations: 6,496; unique source documents: 3,494.
- Public projection: 23,937 people, 2,851 affiliations, 1,063 organizations,
  5,265 sources and 7,697 published claims.

Research-attempt and archival-review coverage each increased by all 23 people.
Verified-affiliation coverage increased by Peter Selz, Mario Semolich and Amos
Sentman. Verified-employer coverage increased by Mario Semolich.

## Validation

Local release validation passed. Python reports 145 tests and 81 parameterized
subtests passing. Astro checked 493 files with zero errors, warnings or hints
and built 25,044 static pages. The bounded Playwright release suite passed
90/90 checks across Batch 859, core routes, the oil-company category, analytics
and accessibility at desktop, phone and tablet viewports. The stratified
200-profile audit passed every check. All internal links across 25,044 HTML
files resolve; 51,385 unique external URLs were inventoried separately. The
public-identifier audit found zero unexpected boundary matches after checking
12,926 normalized identifiers and 120 formatted variants across 25,116 built
artifacts.

The public manifest covers 67 assets totaling 116,101,952 bytes with SHA-256
`04090186539b9ddc96c78f482a547b9d78dedd79742acfde07100678281441ed`.
Two production builds produced the identical 25,116-file tree hash
`61170f147ee41a5947391a11e180b02a6534122ab9d313d667f7f06fc69c7607`.

## Publication status

Publication is pending the content commit, GitHub Actions checks and immutable
live-release verification. The overall every-person research goal remains
active.

## Resume commands

```bash
.venv/bin/python -m oss_research --db research/research.sqlite import-review-decisions research/army_review_decisions_2026-10-16_batch859.csv
.venv/bin/python -m oss_research --db research/research.sqlite import-reviewed-evidence research/evidence-page419-selvig-serao-review_batch-859_2026-10-16.json
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
.venv/bin/python -m oss_research --db research/research.sqlite assign-page-batch --batch-name batch-860 --page 420 --first-row 1 --last-row 23
```
