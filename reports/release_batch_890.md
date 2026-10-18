# Batch 890 release audit

Date: 2026-10-18 America/New_York

## Release contents

- NARA index page 435, rows 1-23: Martha F Smith through the first Robert F
  Smith entry.
- 22 new terminal research outcomes; Nicol Smith's previously completed,
  verified-employer record remains unchanged.
- Five high-confidence Army identity bridges and five medium-confidence,
  qualified occupation or student findings.
- No new finding is mislabeled as an immediate affiliation, last civilian
  employer, named school or precise OSS-transfer sequence.
- The two exact Martin E Smith rows remain separate and visible in a possible-
  duplicate group; evidence for the protected-identifier row is not transferred
  to the row lacking that bridge.

## Reproducible release checks

- SQLite integrity: ok; foreign-key violations: zero.
- Stratified profile audit: 200/200 profiles pass every check.
- Python: 146 tests and 84 parameterized subtests pass.
- Astro: 521 files checked with zero errors, warnings or hints; 25,086 static
  pages built.
- Browser release suite: 96/96 checks pass across desktop, phone and tablet,
  including 30 axe scans with no serious or critical violations.
- Internal links: 25,086 HTML files checked; all links resolve.
- Identifier audit: 12,926 normalized identifiers and 120 formatted variants
  checked across 25,158 artifacts; zero unexpected matches.
- Public manifest: 67 assets, 118,713,154 bytes, SHA-256
  e3a3f2099497ab074fafe425d7250adaa105056dc4f1a94657f672d5ec80d5ba.
- Two consecutive public trees: 70 files, 121,060,305 bytes, SHA-256
  8762e7e5f51cf6fffd381c8cac8cfdfb0eccc0c0edd7ea037669f931e014123c.
- Two consecutive output trees: 25,158 files, 328,624,414 bytes, SHA-256
  d3e09a02a2f9ba061b073d19030a74583327c4b8ecdcbba2436b18c925bdced9.
- Production dependency audit: zero vulnerabilities.

## Coverage at release candidate

- Index: 23,978/23,978 source rows linked (100.0000%).
- Research attempted: 13,430/23,937 people (56.1056%).
- Verified affiliation: 964/23,937 people (4.0272%).
- Verified employer: 435/23,937 people (1.8173%).
- Archival disposition assessed: 11,898/23,937 people (49.7055%).
- Not started: 10,502 people; in progress: 1,892 people.
- Public projection: 23,937 profiles, 2,962 affiliations, 1,104
  organizations, 5,472 sources and 8,115 claims.

## Publication verification

Pending content commit, independent GitHub Test, Pages deployment and
unauthenticated live-release verification. The latest verified public release
remains Batch 889 until all four gates pass.
