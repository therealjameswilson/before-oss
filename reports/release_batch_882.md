# Batch 882 release audit

Date: 2026-10-17 America/New_York

## Release contents

- NARA index page 431, rows 1-23: Arthur A Skiathitis through Clarence W
  Skupic.
- 23 saved terminal research outcomes: three confirmed, eleven high-
  confidence, two probable, six unresolved and one conflicting identity.
- Nine new public affiliations, eleven new public sources and 26 new public
  claims.
- High-confidence immediate pathways for Einar Skinnarland's Mårvatn dam work
  and Frank J Skokoski's 541st Parachute Infantry Regiment assignment, without
  relabeling a work site or military unit as a civilian employer.
- Medium, visibly qualified employment histories for Sibilla Skidelsky, Folke
  K Skoog and George P Skouras.
- Ten accepted and two conflicting Army review decisions, with protected
  identifiers excluded from public assets.
- Explicit preservation of the Hakon A Skjolsvik/H Skgolsvik shared-identifier
  conflict without merging the two index people.

## Reproducible release checks

- SQLite integrity: ok; foreign-key violations: zero.
- Stratified profile audit: 200/200 profiles pass every check.
- Python: 145 tests and 81 parameterized subtests pass.
- Astro: 513 files checked with zero errors, warnings or hints; 25,080 static
  pages built.
- Browser release suite: 90/90 checks pass across desktop, phone and tablet,
  including 30 axe scans with no serious or critical violations.
- Internal links: 25,080 HTML files checked; all links resolve.
- Identifier audit: 12,926 normalized identifiers and 120 formatted variants
  checked across 25,152 artifacts; zero unexpected matches.
- Public manifest: 67 assets, 118,015,204 bytes, SHA-256
  529349e4558c79ceb3479fa736bdcb115b887f035a0f7309beb8197815ea48aa.
- Two consecutive output trees: 25,152 files, 327,508,136 bytes, SHA-256
  002271f5d4bb2786de88cd3da19b32ad65a6aca3e9b96f3e1e8015c348ab57eb.
- Dependency audit: zero vulnerabilities.

## Coverage at release candidate

- Index: 23,978/23,978 source rows linked (100.0000%).
- Research attempted: 13,248/23,937 people (55.3453%).
- Verified affiliation: 961/23,937 people (4.0147%).
- Verified employer: 433/23,937 people (1.8089%).
- Archival disposition assessed: 11,715/23,937 people (48.9410%).
- Not started: 10,684 people; in progress: 1,893 people.
- Public projection: 23,937 profiles, 2,919 affiliations, 1,098
  organizations, 5,424 sources and 8,008 claims.

## Publication verification

- Content commit:
  19af3ca713d1bb90122270c12b364cc8d6fd106e.
- Clean Linux Test workflow: passed in run 39091880913:
  https://github.com/therealjameswilson/before-oss/actions/runs/39091880913
- GitHub Pages build and deploy: passed in run 39091880875:
  https://github.com/therealjameswilson/before-oss/actions/runs/39091880875
- Unauthenticated verification: all 67 manifest assets, eight core routes, 37
  source-register pages and all 23 direct Batch 882 profiles matched the
  immutable content commit at
  https://therealjameswilson.github.io/before-oss/.

GitHub emitted non-failing maintenance annotations that its Node 20-based
actions are currently being forced onto Node 24 and that ubuntu-latest is
scheduled to migrate to Ubuntu 26. Neither annotation changed the successful
release result.
