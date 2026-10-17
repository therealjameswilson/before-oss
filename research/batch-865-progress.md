# Batch 865 research progress

Date: 2026-10-17 America/New_York

## Scope and source validation

Batch 865 covers the 23 printed personnel rows on NARA index PDF page 422,
rows 24-46, from Jerome W Shay through Nellie M Sheehy. All 23 immutable
source rows remain preserved. They link to 22 active person entities because
the two adjacent Charles W Shearer rows repeat the exact name, protected
identifier, Box 701 and archive location. The reviewed table preserves names,
initials, printed ranks, private identifier columns, Box 701 and archive
location 230/86/40/05. Full service and officer numbers remain private. The
next unresearched boundary is PDF page 423, row 1, R B Sheeks.

## Research outcomes

- A nonshared protected identifier links indexed John J Shea to official Army
  source form `SHEA JOHN`. The Army form omits the indexed middle initial, so
  that difference remains explicit. The identity bridge is accepted at high
  confidence, but Army-coded entry-grade and occupation fields remain private
  and are not converted into employer, OSS-rank or chronology claims.
- The two adjacent Charles W Shearer rows are linked to one high-confidence
  entity because their exact full name, protected identifier, box and location
  repeat. Both immutable source rows remain visible. This establishes a
  duplicate source-row relationship only; it supplies no employer.
- Two Clyde Shearer rows remain separate people in a visible duplicate group.
  Two Douglas G Shearer rows likewise remain separate. Name and adjacency alone
  do not justify a merge or transfer of namesake evidence.
- An official veterans memorial names an Army First Lieutenant William L Shea,
  which conflicts with the indexed Ensign. Without a protected-identifier or
  OSS bridge, that candidate was rejected rather than attached to the profile.
- An official 44th Infantry Division history names Major Thomas C Sheehan Jr as
  acting G-2 in April 1945. It lacks the indexed protected identifier and a
  direct OSS bridge, so it remains an archival comparison lead rather than a
  published identity or affiliation claim.
- Library of Congress discovery produced five candidates each for John J Shea
  and Michael J Shea. Their accessible metadata and OCR did not establish the
  exact indexed person, so all ten were individually rejected. The Morgan C
  Sheehan request timed out after bounded retries and no incomplete response
  was used as evidence.
- The direct CIA Reading Room adapter respected the site's robots policy and
  halted at the first disallowed request rather than bypassing the restriction.
  CIA-domain discovery searches, public NARA Catalog discovery searches,
  exact-name OSS searches, employment and occupation searches, and applicable
  obituary, directory, institutional, newspaper and archival searches were
  saved for the batch. Authenticated NARA Catalog research remains disabled
  pending safe credential rotation.
- No source met the identity and temporal thresholds for a pre-OSS employer or
  affiliation. Each profile states that no reliable pre-OSS employer has yet
  been identified in the accessible sources reviewed and directs researchers
  to Box 701.

The batch distribution is two `high_confidence`, 14 `ambiguous` and six
`unresolved` identities. All 22 people are `requires_archival_review`; every
person has a saved non-planned attempt, and no Batch 865 person remains
`not_started` or `in_progress`. The evidence bundle contains two sources, zero
organizations, zero affiliations, two published identity claims, 22 person
updates, 22 manual research attempts and three embedded claim-source links.
One Army candidate was accepted and ten LoC candidates were rejected.
SQLite's foreign-key check returned no rows and its integrity check returned
`ok`.

## Updated project coverage

- Index coverage: 23,978/23,978 linked source rows (100%).
- Active person entities: 23,937; stored entities: 23,941, including four
  unlinked superseded entities retained for auditability.
- Research-attempt coverage: 12,862 people (53.7327%).
- Verified-employer coverage: 423 people (1.7671%).
- Verified-affiliation coverage: 933 people (3.8977%).
- Archival-review coverage: 11,329 people (47.3284%).
- Not started: 11,070 people.
- Possible duplicate groups: 578.
- Conflicts: 447 people.
- Claim confidence totals: 1,612 confirmed, 4,073 high, 1,712 medium,
  202 low, 373 conflicting and two unresolved.
- Citations: 6,536; unique source documents: 3,524.
- Public projection: 23,937 people, 2,867 affiliations, 1,073 organizations,
  5,305 sources and 7,766 published or qualified claims.

Research-attempt and archival-review coverage each increased by 22 people.
Verified-employer and verified-affiliation coverage did not change. The two
new public claims document identity resolution, not employment.

## Validation

Local release validation passed. Python reports 145 tests and 81 parameterized
subtests passing. Astro checked 499 files with zero errors, warnings or hints
and built 25,054 static pages. The bounded Playwright release suite passed
87/87 checks across Batch 865, core routes, the oil-company category,
analytics and accessibility at desktop, phone and tablet viewports. The
stratified 200-profile audit passed every check. All internal links across
25,054 HTML files resolve; 51,417 unique external URLs were inventoried
separately. The public-identifier audit found zero unexpected boundary matches
after checking 12,926 normalized identifiers and 120 formatted variants across
25,126 built artifacts.

The public manifest covers 67 assets totaling 116,569,249 bytes with SHA-256
`494a3feef8147dd9f685cd4c68f79d7501623f18c37286be14c10e86c7545457`.
Two production builds produced the identical 25,126-file static-site hash
`4502fed8733dc44579c7300694e1e4c56e622a4e7393135ef5245a6cfae49e4b`.

## Publication status

Batch 865 is not yet published. All local gates pass; the current public site
remains the verified Batch 864 release until GitHub Actions and immutable
post-deployment verification pass.

## Resume commands

```bash
.venv/bin/python -m oss_research --db research/research.sqlite import-review-decisions research/army_review_decisions_2026-10-17_batch865.csv
.venv/bin/python -m oss_research --db research/research.sqlite import-review-decisions research/loc_review_decisions_2026-10-17_batch865.csv
.venv/bin/python -m oss_research --db research/research.sqlite import-reviewed-evidence research/evidence-page422-shay-sheehy-review_batch-865_2026-10-17.json
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
