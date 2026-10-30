# Batch 990 release audit

Date: 2026-10-30 America/New_York

## Release contents

- NARA index page 485, rows 24-46: Wilhelm-Viggo E.F. Von Moltke through
  George C Vournas. Page 486, row 1, Jacques Voyer, is the next cohort
  boundary.
- All 23 source rows remain separate people and have saved terminal research
  outcomes.
- Four people gain verified-employer outcomes: Nicholas A Vonneuman, Francis
  S Vonstade, Robert J Voskuil and George C Vournas. Their immediate military
  or government pathways remain separately typed from civilian employment.
- Four official Army categories publish only qualified occupations, never
  named employers. James A Voorhees and Raymond G Vosper retain identity
  bridges without unsafe occupation transfer.
- Bert D Voot/Bert D Vogt and Walter Von Schuschn/Walter Schuschnigg remain
  separate visible conflict or possible-duplicate pairs.
- No authenticated NARA Catalog API request was used.
- The oil-company category remains 14 people linked to 15 historically named
  companies.

## Reproducible local release checks

- Evidence-bundle SHA-256:
  `c94a1165c099203a532fd87f30752efe18d150e7acff5491fbbcd570aa99bfe4`.
- Durable import: 19 sources, 10 organizations, 17 affiliations, 32 claims,
  70 claim-source links, 25 person updates and 23 research attempts; repeated
  imports reproduce the same authoritative evidence counts.
- Review decisions: seven accepted official Army identity candidates and one
  conflict-preservation decision.
- Complete ingest audit and 200-profile stratified audit: every check passed.
- Python: 147 tests passed with the CI-equivalent `unittest discover`
  command.
- Targeted Batch browser matrix: 30/30 checks passed across desktop, phone
  and tablet.
- Clean-archive browser release suite: 99/99 current-batch, core-route,
  analysis and accessibility checks passed, including 30 axe scans with no
  serious or critical violations.
- Clean-archive Astro build: 621 files checked with zero diagnostics; 25,290
  canonical static pages built. Unrelated user-owned duplicate page files in
  the working checkout remain untouched and are not part of the release.
- Clean-archive internal links: 25,290 HTML files checked; all links resolve;
  52,211 unique external URLs were inventoried separately.
- Clean-archive identifier audit: 12,926 normalized identifiers and 120
  formatted variants checked across 25,362 artifacts; 1,470 candidate
  substrings and zero unexpected matches.
- Public manifest: 67 assets, 132,835,276 bytes, SHA-256
  `772ceea7fb76f85d985840e91b2495d8609a9569228872b5de68abc8fb26ea56`.
- Public tree: 70 files, 135,182,431 bytes, SHA-256
  `2b0a9d657bed395d26ddac615a51244ddb54555d4bdd5ef85b0e0f85315504b9`.
- Determinism: two consecutive clean builds reproduced 25,362 files,
  422,575,960 bytes and tree SHA-256
  `a589f230670128630e29fb40fb27eeae5ec688f58cac16070c84763dff2803b8`.
- Production dependency audit: zero vulnerabilities.

## Coverage prepared for publication

- Index: 23,978/23,978 source rows linked (100.0000%).
- Research attempted: 15,702/23,936 people (65.5999%).
- Verified affiliation: 1,135/23,936 people (4.7418%).
- Verified employer: 514/23,936 people (2.1474%).
- Archival disposition assessed: 14,177/23,936 people (59.2288%).
- Not started: 8,229 people; in progress: 1,883 people.
- Claim confidence: 1,723 confirmed; 5,328 high; 2,567 medium; 255 low;
  439 conflicting; and 2 unresolved.
- Public projection: 23,936 profiles, 3,943 affiliations, 1,302
  organizations, 6,470 sources and 10,053 published, qualified or conflict
  claims.
- Citations: 7,757 across 4,328 unique source documents.

## Publication verification

Publication is pending the audited release commit, successful GitHub Actions
Test and Pages runs, and unauthenticated deployed-release verification.
