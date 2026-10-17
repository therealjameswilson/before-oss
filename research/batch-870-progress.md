# Batch 870 research progress

Date: 2026-10-17 America/New_York

## Scope and source validation

Batch 870 covers the 23 printed personnel rows on NARA index PDF page 425,
rows 1-23, from Naotada Shimomura through Clifton B Shoemaker. All 23 immutable
source rows remain preserved and link to 23 active person entities. The table
was checked against both layout-preserving extraction and a rendered page
image. Printed names, initials, ranks, identifier columns, Boxes 705-706 and
archive location 230/86/40/05 remain recoverable. Full service and officer
numbers remain private. The next unresearched boundary is page 425, row 24.

## Research outcomes

- A direct official NARA OSS award roster confirms Major Ezra Shine as chief
  of Schools & Training at OSS Main from October 1944 through May 1945. This
  establishes identity and an OSS assignment, not a pre-OSS employer.
- Official NARA OSS evidence and an OSS Society obituary support a
  high-confidence identification of Maurice Shire. The one-digit discrepancy
  between protected identifiers is preserved rather than silently corrected.
  A postwar business founded in 1965 is excluded from pre-OSS employment.
- Official Bureau of Labor Statistics and Ford Presidential Library sources
  support a probable identification of Julius Shiskin. They document Rutgers
  teaching in 1934-1938, National Bureau of Economic Research work in
  1938-1942, and War Production Board work in 1942-1945. The affiliations are
  published with medium confidence and qualified chronology; none is labeled
  immediate pre-OSS.
- A detailed Washington Post obituary supports a high-confidence
  identification of Clayton L Shirey and sequences Penn State attendance,
  Army entry and OSS assignment. Penn State is modeled as student status, not
  employment.
- An OSS Operational Groups roster supports Harry Shiomos at high confidence.
  Exact names and nonshared protected identifiers support Kenneth O Shirley
  and William E Shockley through official Army crosswalks. These identity
  bridges do not create employer or OSS-rank claims.
- John L Shimondle's incompatible middle initial and Jack E Shine's surname
  mismatch against Army candidates remain explicit conflicts. Neither
  candidate was forced onto the indexed person.
- Direct underlying files for James Shiozaki and Saikichi Shirasawa leads were
  inaccessible or lacked a defensible OSS bridge. Those leads remain withheld
  from public employment claims pending archival review.
- Authenticated NARA Catalog research remains disabled pending safe credential
  rotation. No exposed credential was used, logged or written to project data.

The cohort distribution is one `confirmed`, five `high_confidence`, two
`probable`, two `conflicting` and 13 `unresolved` identities. One person is
`documented_prewar_employer_found`, one is `occupation_only_found`, two are
`conflicting_sources`, and 19 are `requires_archival_review`. Every person has
at least one saved non-planned attempt. No Batch 870 person remains
`not_started` or `in_progress`.

The evidence bundle contains eight sources, four organizations, four
affiliations, 13 claims, 23 person updates, 23 research attempts and 24
claim-source links. Three Army candidates were accepted and two retained as
conflicting. Reimporting the review files is idempotent. SQLite's integrity
check returned `ok`, and its foreign-key check returned no rows.

## Updated project coverage

- Index coverage: 23,978/23,978 linked source rows (100%).
- Active person entities: 23,937; stored entities: 23,941, including four
  unlinked superseded entities retained for auditability.
- Research-attempt coverage: 12,975 people (54.2048%).
- Verified-employer coverage: 428 people (1.7880%).
- Verified-affiliation coverage: 941 people (3.9312%).
- Archival-review coverage: 11,442 people (47.8005%).
- Not started: 10,957 people.
- Possible duplicate groups: 579.
- Conflicts: 450 people.
- Claim confidence totals: 1,614 confirmed, 4,127 high, 1,725 medium,
  206 low, 376 conflicting and two unresolved.
- Citations: 6,577; unique source documents: 3,556.
- Public projection: 23,937 people, 2,886 affiliations, 1,083 organizations,
  5,342 sources and 7,838 published or qualified claims.

Relative to Batch 869, research-attempt and archival-review coverage each
increased by 23 people. Verified-affiliation coverage increased by one;
verified-employer coverage did not change. Four affiliations, one organization,
eight public sources and 13 published or qualified claims entered the public
projection. Two additional people are explicitly classified as conflicts.

## Validation

Local release validation passed. Python reports 145 tests and 81 parameterized
subtests passing. The stratified 200-profile audit passed every check. Astro
checked 504 files with zero errors, warnings or hints and built 25,064 static
pages. The bounded Playwright release suite passed 90/90 checks across Batch
870, core routes, the oil-company category, analytics and accessibility at
desktop, phone and tablet viewports. All internal links across 25,064 HTML
files resolve; 51,449 unique external URLs were inventoried separately. The
public-identifier audit found zero unexpected boundary matches after checking
12,926 normalized identifiers and 120 formatted variants across 25,136 built
artifacts.

The public manifest covers 67 assets totaling 117,019,452 bytes with SHA-256
`e4ab5fb64dcf850280e6e1c1cb1966a33938b0613799a9fa57b89763211e703f`.
Two production builds produced the identical 25,136-file static-site hash
`ee2c376bf290be403d25c86e16b3a08603132a6daa8c2ff8f7d670b4456d418a`.

## Publication status

Batch 870 has passed all local release gates and is awaiting publication to the
existing GitHub Pages site. The immutable content commit, GitHub Actions runs
and post-deployment verification will be recorded here after deployment.

## Resume commands

```bash
.venv/bin/python -m oss_research --db research/research.sqlite import-review-decisions research/army_review_decisions_2026-10-17_batch870.csv
.venv/bin/python -m oss_research --db research/research.sqlite import-reviewed-evidence research/evidence-page425-shimomura-shoemaker-review_batch-870_2026-10-17.json
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
.venv/bin/python scripts/hash_tree.py site/dist
```
