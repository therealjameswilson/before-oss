# Batch 898 release audit

Date: 2026-10-25 America/New_York

## Release contents

- NARA index page 439, rows 1-23: Gene Sorisi through Jacques Soustelle.
- 23 terminal research outcomes and 23 manual research-attempt records.
- Five accepted official Army identity bridges; three historical occupation
  findings remain qualified and identify no employer or workplace.
- The Sorota and Soskice variant rows remain separate. Alexander J Soto's
  protected-identifier conflict with William J Smith remains visible without
  transferring disputed evidence.
- Rolf Sørlie's engineer occupation, Stephen S. Sorota's probable Phillips
  Academy work, Victor Andrew Soskice's student chronology, Frédéric Souard's
  military record and Jacques Soustelle's three prewar institutional roles are
  published with identity, temporal and relationship distinctions intact.
- The next boundary, M J Soustelle on page 439 row 24, was visually confirmed.

## Reproducible local release checks

- SQLite integrity: ok; foreign-key violations: zero.
- PDF extraction validation: 23,978 rows across 522 pages; all checks pass.
- Stratified profile audit: 200/200 profiles pass every check.
- Python: 146 tests and 84 parameterized subtests pass.
- Astro: 529 files checked with zero errors, warnings or hints; 25,106 static
  pages built.
- Browser release suite: 93/93 checks pass across desktop, phone and tablet,
  including 30 axe scans with no serious or critical violations.
- Internal links: 25,106 HTML files checked; all links resolve.
- Identifier audit: 12,926 normalized identifiers and 120 formatted variants
  checked across 25,178 artifacts; zero unexpected matches.
- Public manifest: 67 assets, 119,850,846 bytes, SHA-256
  `f45190c6ca142c14876c461b2925da616318e2c1280a267b1373382e7e544f66`.
- Two consecutive public trees: 70 files, 122,198,001 bytes, SHA-256
  `a8ba7e8bb7d3a6970b75336c65a015a5bf3027d0a4c6c7b6e365546ac4aa6412`.
- Two consecutive output trees: 25,178 files, 330,453,050 bytes, SHA-256
  `f3a8d609eeaf9aeca20ec27c8a73b972761d3ebe2528aae3f5851d30ef88ab31`.
- Production dependency audit: zero vulnerabilities.

## Coverage at release candidate

- Index: 23,978/23,978 source rows linked (100.0000%).
- Research attempted: 13,611/23,936 people (56.8641%).
- Verified affiliation: 978/23,936 people (4.0859%).
- Verified employer: 439/23,936 people (1.8341%).
- Archival disposition assessed: 12,082/23,936 people (50.4763%).
- Not started: 10,320 people; in progress: 1,889 people.
- Public projection: 23,936 profiles, 3,043 affiliations, 1,125
  organizations, 5,546 sources and 8,267 claims.

## Publication verification

The release candidate is locally validated. Content commit, GitHub Actions
status, deployed-manifest comparison and unauthenticated public-route checks
will be added after publication. The currently public Batch 897 release remains
available at <https://therealjameswilson.github.io/before-oss/>.
