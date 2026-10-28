# Batch 933 release audit

Date: 2026-10-27 America/New_York

## Release contents

- NARA index page 457, rows 1-23: Fred G. Swafford through Victor H.
  Swearingen.
- 23 immutable source rows, 23 separate people and 23 saved terminal research
  attempts.
- Four accepted official Army candidates and one rejected conflicting
  candidate; no full protected identifier appears in tracked evidence, review
  decisions or public data.
- Lawrence E. Swank is a high-confidence identity with a documented West Point
  student affiliation and an explicit Army Corps of Engineers pathway into
  OSS. Paul A. Swank is a separate high-confidence identity with a documented
  United States Army and Camp Claiborne pathway before OSS volunteering.
- Four Army categories remain occupation or student-status only and
  employer-free. Thomas J. Swartz's damaged grade value `PV0` is not
  interpreted.
- Anthony I. Swarowsky's conflicting Army candidate is rejected. Harvey R.
  Swarts and Fred S. Watson Jr. remain separate despite a shared protected
  identifier; their duplicate group is opaque in tracked and public data.
- Fifteen unresolved people retain explicit Box 760 archival-review guidance.
- The evidence-defined oil-company category remains unchanged at 14 people
  linked to 15 historically named companies.

## Reproducible local release checks

- SQLite integrity: ok; foreign-key violations: zero.
- PDF extraction validation: 23,978 rows across 522 pages; all checks pass.
- Stratified profile audit: 200/200 profiles pass every check.
- Python: 147 tests pass.
- Astro: 564 files checked with zero errors, warnings or hints; 25,167 static
  pages built.
- Batch browser suite: 27/27 checks pass on desktop, phone and tablet.
- Browser release suite: 96/96 checks pass across desktop, phone, tablet and
  accessibility coverage, including 30 axe scans with no serious or critical
  violations.
- Internal links: 25,167 HTML files checked; all links resolve. The checker
  separately inventories 51,785 unique external URLs without claiming they
  were all live-tested in this release pass.
- Identifier audit: 12,926 normalized identifiers and 120 formatted variants
  checked across 25,239 production artifacts; 1,414 candidate substrings were
  inspected and there were zero unexpected boundary matches.
- Public manifest: 67 assets, 124,398,240 bytes, SHA-256
  `23baf53b2371dd3fcf39efe65182cace1f10bc711274e086394b08198ae007c2`.
- Public tree: 70 files, 126,745,377 bytes, SHA-256
  `c9ad25b96d35900f07c764e9e71518cc7443869f85f3f37227e5be26ca6106c7`.
- Two consecutive output trees: 25,239 files and 408,750,651 bytes each, with
  identical SHA-256
  `6fd27bbae456666c3a76442a9b2608c11f85fd75b19281b8f99b59db2533914b`.
- Production dependency audit: zero vulnerabilities. Development tooling is
  not shipped with the static site.

## Coverage prepared for publication

- Index: 23,978/23,978 source rows linked (100.0000%).
- Research attempted: 14,405/23,936 people (60.1813%).
- Verified affiliation: 1,021/23,936 people (4.2655%).
- Verified employer: 460/23,936 people (1.9218%).
- Archival disposition assessed: 12,878/23,936 people (53.8018%).
- Not started: 9,526 people; in progress: 1,886 people.
- Durable research attempts or plans: 28,526.
- Possible-duplicate groups: 631; conflicts: 497.
- Claim confidence: 1,650 confirmed; 4,710 high; 2,096 medium; 252 low;
  419 conflicting; 2 unresolved.
- Public projection: 23,936 profiles, 3,349 affiliations, 1,183 organizations,
  5,851 sources and 8,871 claims.
- Evidence ledger: 7,130 citations across 3,919 unique source documents.

## Publication verification

Pending. Local preparation is not publication. Record the immutable content
commit, successful GitHub Actions Test and Pages runs, and unauthenticated live
manifest and direct-profile verification here before calling Batch 933 public.
