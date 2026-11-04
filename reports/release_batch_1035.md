# Batch 1035 release audit

Date: 2026-11-04 America/New_York

## Release contents

- NARA index page 290, rows 1-46: Nelle E. Maertens through Robert J.
  Maisonpierre. All 46 rows remain separately recoverable as 46 cautious
  person entities.
- Forty-five people received new saved research outcomes; John Magruder's
  previously confirmed, completed profile was preserved without replacement.
  The full cohort contains 30 `requires_archival_review`, 15
  `occupation_only_found`, and one `completed` outcome.
- Sixteen protected-identifier Army candidates received explicit review: 15
  exact-name candidates were accepted and the damaged-name Clyde M. Maffin
  candidate was rejected. No fields were transferred from the rejected
  candidate.
- The accepted Army-entry records support broad, date-bounded occupation or
  student categories only; no coded occupation was converted into a named
  employer, institution, workplace, or immediate pre-OSS affiliation.
- A direct wartime OSS Detachment 101 promotions report confirms Capt. John D.
  Maharg's identity and unit context but supplies no pre-OSS employer.
- Orrin R. Magill Jr.'s student status is supported by the protected Army
  link. A direct OSS report names Orrin F. Magill Jr.; the middle-initial
  disagreement remains explicit and requires personnel-file review.
- An American Council of Learned Societies finding aid contains a William
  Louis Magistretti file dated 1937-41, but the file title does not state the
  relationship and therefore was not treated as employment evidence.
- Shirley K. Mains's indexed “Aka Ray” note is preserved as a search variant
  rather than silently resolving her identity.
- The cohort identity assessment is 16 confirmed, one high-confidence, and 29
  unresolved people, including John Magruder's preserved confirmed profile.
- No authenticated NARA Catalog API request was used.

## Evidence and import

- Reviewed evidence bundle: five sources, no new organizations, 15
  affiliations, 16 claims, 62 claim-source links, 45 person updates, and 45
  research attempts.
- Sixteen Army identity-review decisions were imported. Decision and evidence
  imports were tested against a disposable database before the durable
  update.
- A pre-import SQLite backup is retained at
  `/private/tmp/before-oss-pre-b1035-20261104.sqlite` for local recovery.
- Post-import SQLite integrity and foreign-key checks passed with zero
  violations.
- Evidence-bundle SHA-256:
  `16ca0da3d197b7848cd53a3512f46a0e76c6de291523da4e9d73cb9532f50dae`.

## Coverage prepared for publication

- Index: 23,978/23,978 source rows linked (100.0000%).
- Research attempted: 17,492/23,935 people (73.0813%).
- Verified affiliation: 1,223/23,935 people (5.1097%).
- Verified employer: 558/23,935 people (2.3313%).
- Archival disposition assessed: 15,967/23,935 people (66.7098%).
- Not started: 6,438 people; in progress: 1,878 people.
- Research outcomes include 2,091 `occupation_only_found`, 9,790
  `requires_archival_review`, 470 `verified_employer_found`, 298
  `documented_prewar_employer_found`, 622 `needs_identity_review`, 50
  `needs_temporal_review`, and 487 `conflicting_sources` people.
- Claim confidence: 2,018 confirmed; 5,598 high; 3,082 medium; 261 low; 473
  conflicting; and two unresolved.
- Public projection: 23,935 profiles, 4,583 affiliations, 1,401
  organizations, 6,876 sources, and 11,167 published, qualified, or conflict
  claims.
- Citations: 8,169 across 4,596 unique source documents.
- Possible duplicate groups: 699. Total conflict flags: 567.

## Local publication verification

- Python: 267 pytest cases and 87 subtests passed.
- Clean Astro check: 666 files with zero errors, warnings, or hints.
- Clean static build: 25,390 pages and 25,462 total output artifacts.
- Bounded browser release suite: 87/87 checks passed across desktop, phone,
  and tablet: 18 Batch 1035 checks, 33 core-route and interaction checks, six
  analysis checks, and 30 accessibility scans with no serious axe violations.
- Internal links: 25,390 HTML files checked; all links resolve. The checker
  inventoried 52,513 unique external URLs separately.
- Checked-in public manifest: 67 canonical assets, 141,595,026 bytes,
  SHA-256
  `26b57fc0138e34fe5aa1edc74e885fecc869b870f2025dd49614a3f778a706bf`.
- Public-identifier audit: 25,462 output artifacts checked against 12,926
  normalized private identifiers and 120 formatted variants. It inspected
  1,584 candidate substrings and found zero aggregate, manifest-size, or
  unexpected boundary matches.
- Two consecutive local builds reproduced 25,462 artifacts totaling
  437,149,556 bytes at output-tree SHA-256
  `8e58830b435055a19471fc5d5af8b93285bb48d6111daa6e6c8e7e7835ad2ede`.
- The complete 522-page ingest audit and deterministic 200-profile stratified
  audit passed all defined gates.

## Deployment status

- Publication commit:
  [`0d75256c86bfa59b027c558dd6cc0d92841f654e`](https://github.com/therealjameswilson/before-oss/commit/0d75256c86bfa59b027c558dd6cc0d92841f654e).
- GitHub Actions Test run
  [41932816595](https://github.com/therealjameswilson/before-oss/actions/runs/41932816595)
  passed, including Python tests, the public-manifest check, the clean static
  build, the bounded browser suite, and a rebuilt private-identifier audit.
- GitHub Pages run
  [41932816842](https://github.com/therealjameswilson/before-oss/actions/runs/41932816842)
  built and deployed successfully.
- The unauthenticated deployed-release verifier matched all 67 manifested
  assets and 141,595,026 bytes at SHA-256
  `26b57fc0138e34fe5aa1edc74e885fecc869b870f2025dd49614a3f778a706bf`,
  then checked eight core routes, all 46 source-register pages, and all 45
  newly reviewed direct profile URLs against the immutable content commit.
  John Magruder's preserved 46th cohort profile was checked separately at its
  direct public URL and returned HTTP 200 with the expected confirmed,
  completed outcome.
- The deployed stats endpoint exactly reports the Batch 1035 totals recorded
  above.
- Public base URL:
  <https://therealjameswilson.github.io/before-oss/>.
