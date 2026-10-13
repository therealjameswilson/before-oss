# Batch 784 release record

Date: 2026-10-13 America/New_York

## Scope

Batch 784 covers PDF page 382, rows 1-24, John E Quintrell through John M
Radaszewski. All 24 printed rows remain preserved and linked to 23 person
entities. The two John M Radaszewski rows share the same protected identifier
but point to Boxes 629 and 630, so they remain distinct source records linked to
one cautious person entity. Every person received a saved, terminal research
outcome. The next indexed boundary is page 382, row 25, Edwin R Raddatz.

## Research outcome

- Twenty-one people have the terminal status "requires_archival_review";
  Akeley P Quirk and Gregory L Rabassa have "occupation_only_found".
- Eleven official Army candidate rows representing ten people were accepted as
  high-confidence identity evidence. Army occupation codes were not converted
  into employer or affiliation claims.
- A State Bar of California record and a citation to Akeley P Quirk's
  first-person USNR memoir support a high-confidence identity and prewar
  attorney status. No employer or law firm was inferred.
- An official U.S. Copyright Office/Library of Congress profile identifies
  Gregory L Rabassa as a Dartmouth student who enlisted in the Army in 1942 and
  served as an OSS cryptographer. Dartmouth remains student status, and the
  Army is modeled separately as his immediate military pathway.
- An official U.S. Army Special Operations history documents Melbourne L
  Rackett with OSS Detachment 101 in Burma in early 1944. It confirms wartime
  identity and OSS context but not a pre-OSS employer.
- The clipped notes "Extract fr" and "No first n" remain exactly as printed and
  were not expanded or interpreted.
- No new verified civilian employer was added. Unresolved profiles direct
  researchers to the indexed personnel files rather than implying that no
  prior employment existed.
- NARA Catalog work was dry-run only: 23 first-pass and 17 serial-focused
  searches were planned with zero authenticated requests. The CIA Reading Room
  adapter failed closed after its permitted retry. The Library of Congress
  adapter completed a bounded retry with two searches, one source-access error,
  three people attempted, and no adapter candidates. These source-access
  limitations were not treated as negative historical evidence.

## Exact coverage at export

- Index: 23,978/23,978 linked rows (100%).
- Active person entities: 23,939.
- Research attempted: 11,032/23,939 (46.0838%).
- Verified employer: 358/23,939 (1.4955%).
- Verified affiliation: 803/23,939 (3.3544%).
- Archival review assessed: 9,491/23,939 (39.6466%).
- Not started: 12,902.
- Possible duplicate groups: 547.
- Conflicts: 373.
- Claims: 1,411 confirmed; 3,417 high; 1,604 medium; 202 low; 323
  conflicting; two unresolved.
- Citations: 5,997 records representing 3,102 unique source documents.
- Public data: 2,599 published affiliations, 929 organizations, 4,772 public
  sources, and 6,751 published claims.

## Local release gates

- Python: 141 tests passed, including 81 parameterized subtests.
- Ingest: all 23,978 rows, 522 pages, 32 parser-warning rows, selected visual-QA
  pages, SQLite integrity, and foreign keys passed.
- Astro: 418 source files checked with zero errors, warnings, or hints; 24,908
  HTML pages built.
- Browser: 87/87 desktop, phone, tablet, analysis, and accessibility checks
  passed: 18 Batch 784 checks, 33 core-site checks, six analysis checks, and 30
  axe checks.
- Links: all 24,908 generated HTML files passed internal-link checks; 50,964
  unique external URLs were inventoried.
- Redaction: zero unexpected private-identifier boundary matches across 24,980
  artifacts.
- Dependencies: the production audit found zero vulnerabilities.
- Manifest: 67 assets, 109,811,736 bytes, SHA-256
  "126dee0dc3c781cd9869be531dc7850260f866532688780d00e1fc7f6bc49d9e".
- Determinism: two consecutive builds produced public-tree SHA-256
  "dc804defe02898d279f79cbae2124ab34e550b6aff540dc195d05368628f3631"
  across 70 files and 112,158,881 bytes, and production-tree SHA-256
  "45c197cc1d4cac8a7dbb22f975276eb92395d9bc3bc66602454671ab1d5ac671"
  across 24,980 files and 314,236,569 bytes.

## Publication

- Release commit:
  "bc6fb0ea2da0e5e07d2e33088282451865b4dbf4".
- The [Deploy GitHub Pages workflow](https://github.com/therealjameswilson/before-oss/actions/runs/38449330150)
  completed successfully.
- The [Test workflow](https://github.com/therealjameswilson/before-oss/actions/runs/38449329874)
  completed successfully.
- Immutable live verification against the release commit confirmed all 67
  manifest assets and 109,811,736 bytes, all eight core routes, all 32 source
  register pages, and all 23 directly affected profile routes. The deployed
  manifest SHA-256 is
  "126dee0dc3c781cd9869be531dc7850260f866532688780d00e1fc7f6bc49d9e".
- Live site: <https://therealjameswilson.github.io/before-oss/>.

Both workflows emitted maintenance notices that selected GitHub actions still
target Node.js 20 and that "ubuntu-latest" is scheduled to migrate to Ubuntu 26.
GitHub ran the affected actions on Node.js 24; neither notice failed or altered
this release.

The full project remains unfinished. Batch 784 is published, but 12,902 active
person entities remain "not_started"; work resumes at page 382, row 25, Edwin R
Raddatz.
