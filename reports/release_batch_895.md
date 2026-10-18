# Batch 895 release audit

Date: 2026-10-18 America/New_York

## Release contents

- NARA index page 437, rows 24-46: Edwin N Snyder through John Soha.
- 23 terminal research outcomes and 23 manual research-attempt records.
- One reviewed Soffner/Sutton entity merge preserving both immutable index rows;
  the adjacent Heirich row and another Henry Sutton row remain separate.
- Six accepted official Army identity bridges and one materially conflicting
  candidate rejection; protected identifiers remain private.
- Jacques Snyder's immediate Army Air Corps language-training pathway and
  earlier Canadian armed-forces service remain distinct from civilian
  employment.
- Franciszek Sobecki's direct OSS record establishes identity and Polish Army
  status without inventing an immediate predecessor.
- Vincent Sofiano's RAF pathway is published with the unresolved attachment
  date stated explicitly.
- Heinrich Soffner/Henry Sutton's Army pathway is separated from qualified
  earlier union and refugee-organization affiliations.
- Four historical Army occupation categories remain qualified and are not
  converted into employers or workplaces.

## Reproducible local release checks

- SQLite integrity: ok; foreign-key violations: zero.
- Stratified profile audit: 200/200 profiles pass every check.
- Python: 146 tests and 84 parameterized subtests pass.
- Astro: 526 files checked with zero errors, warnings or hints; 25,092 static
  pages built.
- Browser release suite: 93/93 checks pass across desktop, phone and tablet,
  including 30 axe scans with no serious or critical violations.
- Internal links: 25,092 HTML files checked; all links resolve.
- Identifier audit: 12,926 normalized identifiers and 120 formatted variants
  checked across 25,164 artifacts; zero unexpected matches.
- Public manifest: 67 assets, 119,347,137 bytes, SHA-256
  `2379f1dd75b14c7ff7ef00b4d90d53c2b124c10a13bb4adaa25aa872a4c3defa`.
- Two consecutive public trees: 70 files, 121,694,290 bytes, SHA-256
  `3435afdfc2622f61a42e3223137fd152f92afbd14dd781f0e6c0f684b2b40871`.
- Two consecutive output trees: 25,164 files, 329,624,975 bytes, SHA-256
  `ab03b2b5dcb452bb91b61c32ffeb59d893f2aa7e67e9c8fa8b7069da0cb1d2dd`.
- Production dependency audit: zero vulnerabilities.

## Coverage at release candidate

- Index: 23,978/23,978 source rows linked (100.0000%).
- Research attempted: 13,542/23,936 people (56.5759%).
- Verified affiliation: 971/23,936 people (4.0567%).
- Verified employer: 436/23,936 people (1.8215%).
- Archival disposition assessed: 12,013/23,936 people (50.1880%).
- Not started: 10,389 people; in progress: 1,889 people.
- Public projection: 23,936 profiles, 3,005 affiliations, 1,111
  organizations, 5,511 sources and 8,197 claims.

## Publication verification

Not yet public. The clean GitHub Test workflow, Pages deployment and
unauthenticated deployed-release comparison remain release gates.
