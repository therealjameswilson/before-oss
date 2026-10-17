# Batch 864 research progress

Date: 2026-10-17 America/New_York

## Scope and source validation

Batch 864 covers the 23 printed personnel rows on NARA index PDF page 422,
rows 1-23, from George Shaskan through Robert J Shaw. All 23 immutable source
rows remain preserved and linked to 23 separate active person entities. The
reviewed table preserves names, initials, printed ranks, private identifier
columns, Boxes 700-701 and archive locations 230/86/40/04 and 230/86/40/05.
Full service and officer numbers remain private. The next unresearched boundary
is PDF page 422, row 24, Jerome W Shay.

## Research outcomes

- The rare indexed name Cautley N Shaw, the truncated printed note `Squadro`,
  an official OSS award-board table naming `Sg Ldr Cautley Shaw (RAF)`, and an
  official London Gazette notice for Cautley Nasmyth Shaw align at high
  confidence. The Gazette documents his Royal Air Force Special Reserve
  commission and honorary Flying Officer rank effective November 15, 1931.
  This is published as a documented prewar military assignment, not a civilian
  employer, continuous-service claim or asserted immediate predecessor to
  OSS-related work.
- A 1946 official Army Military Government in Korea appointment order carries
  Lieutenant Colonel Lyman A Shaw's exact name, rank, Infantry branch and
  officer number. It confirms the indexed identity, but is explicitly used
  only as postwar identity evidence. It does not become a pre-OSS affiliation
  or employer claim.
- Official Army bulk data supplies high-confidence identity-only bridges for
  James F Shaughnessy, Nathan Shaul, Robert S Shaul, the second William H Shaul
  row, Ernest B Shaw, Gustavus W Shaw and Robert J Shaw. Robert S Shaull is
  preserved as the Army source variant; the internal `WIL IAM` spacing defect
  in the second William H Shaul source form is documented without altering the
  indexed name. Army-coded occupation and entry-grade fields remain private
  and do not become employers, OSS ranks or affiliations.
- The Army candidate tied to the first William H Shaul row names Kline William
  H and was rejected. The two same-name index rows carry distinct protected
  identifiers, remain separate, and share a visible possible-duplicate group
  for Box 700 comparison.
- George R Shaver produced mutually incompatible contemporary produce-firm,
  battery-service and military candidates; no candidate carried the indexed
  protected identifier or an OSS bridge. Talmage C Shaver produced at least
  two exact-name men born in 1907. Both remain visibly ambiguous rather than
  receiving a convenient biography.
- A Library of Congress correspondence-folder heading for Michael Q
  Shaughnessy, a genealogy chronology for Wanda Shaver in Calcutta and a
  Somerville municipal record for Earl B Shaw remain discovery leads only.
  None establishes the indexed identity or a pre-OSS employer.
- CIA Reading Room, exact-name OSS, employment, occupation, obituary,
  institutional, newspaper, directory and archival searches were saved for
  all 23 people. Plausible but unbridged namesakes were rejected. An interrupted
  Library of Congress adapter run was recorded as cancelled; no incomplete
  response was accepted as evidence. Authenticated NARA Catalog research
  remains disabled pending safe credential rotation.

The batch distribution is one `confirmed`, eight `high_confidence`, eight
`ambiguous` and six `unresolved` identities. Twenty-two records are
`requires_archival_review`; Cautley N Shaw is `completed` after the full online
protocol and still carries a high-priority file-review recommendation. Every
person has a saved non-planned research attempt and no Batch 864 record remains
`not_started` or `in_progress`. The evidence bundle contains five sources, one
organization, one affiliation, ten published claims, 23 person updates, 23
research attempts and 21 embedded claim-source links. Seven Army candidates
were individually accepted and one was rejected. SQLite's foreign-key check
returned no rows and its integrity check returned `ok`.

## Updated project coverage

- Index coverage: 23,978/23,978 linked source rows (100%).
- Active person entities: 23,937; stored entities: 23,941, including four
  unlinked superseded entities retained for auditability.
- Research-attempt coverage: 12,840 people (53.6408%).
- Verified-employer coverage: 423 people (1.7671%).
- Verified-affiliation coverage: 933 people (3.8977%).
- Archival-review coverage: 11,307 people (47.2365%).
- Not started: 11,092 people.
- Possible duplicate groups: 576.
- Conflicts: 447 people.
- Claim confidence totals: 1,612 confirmed, 4,071 high, 1,712 medium,
  202 low, 373 conflicting and two unresolved.
- Citations: 6,534; unique source documents: 3,523.
- Public projection: 23,937 people, 2,867 affiliations, 1,073 organizations,
  5,303 sources and 7,764 published or qualified claims.

Research-attempt and archival-review coverage each increased by 23 people.
Verified-affiliation coverage increased by one through Cautley N Shaw's RAF
Special Reserve assignment. Verified-employer coverage did not change.

## Validation

Local release validation passed. Python reports 145 tests and 81 parameterized
subtests passing. Astro checked 498 files with zero errors, warnings or hints
and built 25,054 static pages. The bounded Playwright release suite passed
84/84 checks across Batch 864, core routes, the oil-company category, analytics
and accessibility at desktop, phone and tablet viewports. The stratified
200-profile audit passed every check. All internal links across 25,054 HTML
files resolve; 51,417 unique external URLs were inventoried separately. The
public-identifier audit found zero unexpected boundary matches after checking
12,926 normalized identifiers and 120 formatted variants across 25,126 built
artifacts.

The public manifest covers 67 assets totaling 116,551,397 bytes with SHA-256
`5ec272cba9fa314f76488d9f26d9fb6d198aeb30b2f84ae7290b57567323557c`.
Two production builds produced the identical 25,126-file static-site hash
`e7c25a5eac4f692e280e2787186b7faee22acdf2438ec4ad40cf14e05e236a6b`.

## Publication status

The Batch 864 release candidate is locally verified but not yet published.
This section will be updated with the immutable content commit, GitHub Actions
runs and live manifest verification after deployment.

## Resume commands

```bash
.venv/bin/python -m oss_research --db research/research.sqlite import-review-decisions research/army_review_decisions_2026-10-17_batch864.csv
.venv/bin/python -m oss_research --db research/research.sqlite import-reviewed-evidence research/evidence-page422-shaskan-shaw-review_batch-864_2026-10-17.json
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
