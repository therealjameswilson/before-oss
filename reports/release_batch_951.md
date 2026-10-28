# Batch 951 release audit

Date: 2026-10-28 America/New_York

## Release contents

- NARA index page 466, rows 1-23: Austin H Thompson through James L
  Thompson. Janet F Thompson on row 24 is the next cohort boundary.
- 23 immutable source rows, 23 separate people and one saved terminal research
  outcome for every person in the cohort.
- Six Army identities have accepted private identifier bridges. Five dated
  occupation categories and one student category remain qualified and unnamed;
  none is treated as a named employer or immediate OSS predecessor.
- Frances K Thompson remains a visible identity conflict because the protected
  identifier points to Frank K Thompson in the Army file. No Army field was
  transferred across the name disagreement.
- Architect Benjamin C Thompson remains a low-confidence, withheld candidate
  because the contemporary source does not bridge the common name to the Box
  774 file.
- Fifteen people retain explicit Box 774 archival-review outcomes after the
  staged online protocol. No authenticated NARA Catalog API request was used.
- The evidence-defined oil-company category remains unchanged at 14 people
  linked to 15 historically named companies.

## Reproducible local release checks

- Evidence-bundle SHA-256:
  `0bbeba178c0aadfe49ba1d1e80e00ad5a019ae111c0015bd4ed6ab2f154f72f6`.
- An isolated replay imports all seven review decisions, six affiliations, 14
  claims, no organizations, 23 person updates, 23 research attempts, five
  sources and 33 claim-source links; a second import is idempotent. SQLite
  integrity is ok and foreign-key violations are zero.
- PDF extraction validation: 23,978 rows across 522 pages; all checks pass.
- Stratified profile audit: 200/200 profiles pass every check.
- Python: 147 tests pass.
- Astro: 582 files checked with zero errors, warnings or hints; 25,194 static
  pages built.
- Batch browser suite: 21/21 checks pass on desktop, phone and tablet.
- Browser release suite: 90/90 checks pass across desktop, phone, tablet and
  accessibility coverage, including 30 axe scans with no serious or critical
  violations.
- Internal links: 25,194 HTML files checked; all links resolve. The checker
  separately inventories 51,900 unique external URLs without claiming they
  were all live-tested in this release pass.
- Identifier audit: 12,926 normalized identifiers and 120 formatted variants
  checked across 25,266 public artifacts; 1,418 candidate substrings were
  inspected and there were zero unexpected boundary matches.
- Public manifest: 67 assets, 126,877,985 bytes, SHA-256
  `280d81d1923459cb2e2117d8a857cb37dc83c30eb85a3b0562de033819e1837d`.
- Public tree: 70 files, 129,225,141 bytes, SHA-256
  `0558262596bdbe0f20e18897066e831de050d5cc7a0ee75d351b81946cd6e19e`.
- Two consecutive output trees: 25,266 files and 412,728,585 bytes each, with
  identical SHA-256
  `17d7c65f57a45bf6af61f546966f9bfe5787799fb880f5282d5fe6851339ed06`.
- Production dependency audit: zero vulnerabilities. Development tooling is
  not shipped with the static site.

## Coverage published

- Index: 23,978/23,978 source rows linked (100.0000%).
- Research attempted: 14,813/23,936 people (61.8859%).
- Verified affiliation: 1,050/23,936 people (4.3867%).
- Verified employer: 471/23,936 people (1.9677%).
- Archival disposition assessed: 13,288/23,936 people (55.5147%).
- Not started: 9,118 people; in progress: 1,884 people.
- Durable research attempts or plans: 28,939.
- Possible-duplicate groups: 648; conflicts: 513.
- Claim confidence: 1,662 confirmed; 4,881 high; 2,235 medium; 253 low;
  429 conflicting; 2 unresolved.
- Public projection: 23,936 profiles, 3,520 affiliations, 1,209 organizations,
  6,032 sources and 9,203 claims.
- Evidence ledger: 7,312 citations across 4,040 unique source documents.

## Publication verification

- Immutable content commit:
  [`edb489e8d94adffbefb627b2fadf6c56c5ec984c`](https://github.com/therealjameswilson/before-oss/commit/edb489e8d94adffbefb627b2fadf6c56c5ec984c).
- GitHub Test run
  [40686642320](https://github.com/therealjameswilson/before-oss/actions/runs/40686642320)
  passed, including the Python tests, checked-in public-manifest check, bounded
  browser release suite and public-identifier redaction audit.
- GitHub Pages run
  [40686642571](https://github.com/therealjameswilson/before-oss/actions/runs/40686642571)
  passed and deployed the immutable content commit.
- The unauthenticated deployed-release verifier compared 67 public assets
  totaling 126,877,985 bytes to that commit's manifest; the deployed manifest
  SHA-256 was
  `280d81d1923459cb2e2117d8a857cb37dc83c30eb85a3b0562de033819e1837d`.
- Eight core routes, 41 source-register pages and all 23 direct Batch 951
  profile routes returned successfully from
  <https://therealjameswilson.github.io/before-oss/>.
- GitHub emitted advisory runner notices about the Node.js 20 action runtime
  transition and the planned `ubuntu-latest` migration; neither notice caused
  a test or deployment failure.
