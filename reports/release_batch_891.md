# Batch 891 release audit

Date: 2026-10-18 America/New_York

## Release contents

- NARA index page 435, rows 24-46: Robert W Smith through Sunday B Smith.
- 23 terminal research outcomes; two people already had earlier automated
  attempts, so project research-attempt coverage increases by 21.
- Nine high-confidence Army identity bridges and nine medium-confidence,
  qualified occupation or student-status findings.
- No new finding is mislabeled as an immediate affiliation, last civilian
  employer, named school or precise OSS-transfer sequence.
- The same-name Robert A, Robert B and Robert F source rows remain separate and
  visible in three possible-duplicate groups; evidence is not transferred
  among rows.

## Reproducible release checks

- SQLite integrity: ok; foreign-key violations: zero.
- Stratified profile audit: 200/200 profiles pass every check.
- Python: 146 tests and 84 parameterized subtests pass.
- Astro: 522 files checked with zero errors, warnings or hints; 25,086 static
  pages built.
- Browser release suite: 87/87 checks pass across desktop, phone and tablet,
  including 30 axe scans with no serious or critical violations.
- Internal links: 25,086 HTML files checked; all links resolve.
- Identifier audit: 12,926 normalized identifiers and 120 formatted variants
  checked across 25,158 artifacts; zero unexpected matches.
- Public manifest: 67 assets, 118,829,260 bytes, SHA-256
  b4658c94bf23fea477abcf61b6543b31936013adcefd31013fbb886466cf1460.
- Two consecutive public trees: 70 files, 121,176,404 bytes, SHA-256
  20f3f5a0e2589416a5237c2b644f36fc1be2e43eeabcc8480fc8695deeb127de.
- Two consecutive output trees: 25,158 files, 328,808,293 bytes, SHA-256
  8c057b57ef2852340201c627bdf328eb2405b6e997c0afffc0917dd0a728a04e.
- Production dependency audit: zero vulnerabilities.

## Coverage at release candidate

- Index: 23,978/23,978 source rows linked (100.0000%).
- Research attempted: 13,451/23,937 people (56.1933%).
- Verified affiliation: 964/23,937 people (4.0272%).
- Verified employer: 435/23,937 people (1.8173%).
- Archival disposition assessed: 11,921/23,937 people (49.8016%).
- Not started: 10,481 people; in progress: 1,890 people.
- Public projection: 23,937 profiles, 2,971 affiliations, 1,104
  organizations, 5,476 sources and 8,133 claims.

## Publication verification

Publication is pending. Local validation establishes a release candidate but
does not establish a public deployment.
