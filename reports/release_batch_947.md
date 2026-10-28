# Batch 947 release audit

Date: 2026-10-28 America/New_York

## Release contents

- NARA index page 464, rows 1-23: Marcelen J. Tezak through Milton Theaman.
- 23 immutable source rows, 23 separate people and one saved terminal research
  outcome for every person in the cohort.
- Henry H. Thackthwaite's British SOE, Royal Army Service Corps and qualified
  translator-teacher history remains distinct from U.S. OSS employment.
- Charles Wheeler Thayer's State/Foreign Service path is a qualified government
  predecessor affiliation, not a civilian employer or explicit transfer claim.
- Milton Theaman's original OSS Assessment Staff roster establishes identity,
  second-lieutenant rank and Fairfax station but supplies no pre-OSS employer.
- The three duplicate clusters remain separate, and the unrelated Hucal record
  sharing William A. Thayer row 22's private identifier is explicitly rejected.
- Seven accepted Army occupation or student-status categories remain qualified
  and unnamed. Marcelen J. Tezak's code 999 is not interpreted.
- The evidence-defined oil-company category remains unchanged at 14 people
  linked to 15 historically named companies.

## Reproducible local release checks

- Evidence-bundle SHA-256:
  `a98d5e5b33cf80a4465b8a3f4976aa8a73c93effc2f09e2f8b4d0a80fbfb80ea`.
- An isolated replay from the pre-Batch-947 backup imports all nine review
  decisions and 23 research outcomes; a second import is idempotent. Its
  affiliation, claim, source, attempt and review-decision totals match the
  canonical SQLite database.
- SQLite integrity: ok; foreign-key violations: zero.
- PDF extraction validation: 23,978 rows across 522 pages; all checks pass.
- Stratified profile audit: 200/200 profiles pass every check.
- Python: 147 tests pass.
- Astro: 578 files checked with zero errors, warnings or hints; 25,193 static
  pages built.
- Batch browser suite: 27/27 checks pass on desktop, phone and tablet.
- Browser release suite: 96/96 checks pass across desktop, phone, tablet and
  accessibility coverage, including 30 axe scans with no serious or critical
  violations.
- Internal links: 25,193 HTML files checked; all links resolve. The checker
  separately inventories 51,895 unique external URLs without claiming they
  were all live-tested in this release pass.
- Identifier audit: 12,926 normalized identifiers and 120 formatted variants
  checked across 25,265 public artifacts; 1,416 candidate substrings were
  inspected and there were zero unexpected boundary matches.
- Public manifest: 67 assets, 126,481,197 bytes, SHA-256
  `b179d0acfd4d0524f189e12358cf752c65a52a6d03106b3f3e1046c41a008aaf`.
- Public tree: 70 files, 128,828,350 bytes, SHA-256
  `393738f06190e8091a0a3e4a0027b4390eb6613977abc6bd87a5883571ea9c19`.
- Two consecutive output trees: 25,265 files and 412,091,833 bytes each, with
  identical SHA-256
  `62c8ccfd89897616c00c072f213129387a756a064c865e4b783d86891842ac54`.
- Production dependency audit: zero vulnerabilities. Development tooling is
  not shipped with the static site.

## Coverage prepared for publication

- Index: 23,978/23,978 source rows linked (100.0000%).
- Research attempted: 14,722/23,936 people (61.5057%).
- Verified affiliation: 1,046/23,936 people (4.3700%).
- Verified employer: 470/23,936 people (1.9636%).
- Archival disposition assessed: 13,196/23,936 people (55.1303%).
- Not started: 9,209 people; in progress: 1,885 people.
- Durable research attempts or plans: 28,847.
- Possible-duplicate groups: 648; conflicts: 512.
- Claim confidence: 1,654 confirmed; 4,851 high; 2,214 medium; 252 low;
  428 conflicting; 2 unresolved.
- Public projection: 23,936 profiles, 3,490 affiliations, 1,208 organizations,
  6,009 sources and 9,143 claims.
- Evidence ledger: 7,288 citations across 4,031 unique source documents.

## Publication verification

Publication is pending the immutable content commit, GitHub Actions Test and
Pages runs, and the unauthenticated manifest-and-route verifier. This section
must be replaced with exact commit and run identifiers before Batch 947 is
reported as public.
