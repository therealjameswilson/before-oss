# Batch 1004 release audit

Date: 2026-11-03 America/New_York

## Release contents

- NARA index page 494, rows 1-46: Jeanette Weber through Charles F.
  Weible. All 46 printed rows remain separately recoverable and link to 45
  cautious person entities because rows 11 and 12 are separately preserved
  entries for John D. Webster with the same protected identifier.
- Every cohort person has a saved research attempt and a terminal review
  outcome: 34 `requires_archival_review`, 8 `occupation_only_found`, 1
  `verified_employer_found`, 1 `completed` and 1 `conflicting_sources`.
- Identity disposition is 10 confirmed, 1 high-confidence, 1 conflicting and
  33 unresolved people.
- Nine official Army bulk-record bridges were accepted after exact-name,
  protected-identifier and conflict review. Eight profiles preserve only the
  qualified historical occupation category recorded at Army entry. No named
  employer, institution or workplace was inferred from a coded occupation.
- A Library of Congress finding aid and the reviewed Army bridge confirm
  Joseph Wechsberg, preserve the Army spelling `Wachsberg` as a variant and
  identify self-employed freelance journalism as his last documented civilian
  work before Army service. His 1943 New Yorker contributor status is kept as
  a professional affiliation, not silently converted into employment.
- An official OSS European Theater roster independently corroborates Kenneth
  H. Weberg's identity and rank; his Army occupation code remains only a
  qualified general-office-clerk category.
- An institutional publication reproducing an official 1942 War Department
  letter supports a high-confidence Clarence N. Weems Jr. identity and the
  Military Intelligence Service Far East Branch as a qualified probable
  immediate pre-OSS government assignment. The exact transfer order and last
  civilian employer remain unresolved. An uncorroborated oil-company lead was
  withheld, and he was not added to the oil-company category.
- Roland E. Wechsberg on page 494 and Roland E. Weschler on page 498 share a
  protected identifier but remain separate entities with an explicit conflict
  pending personnel-file review.
- All 46 page-494 source rows and the page-498 conflict row were checked
  against layout-preserving text and original-detail renders. Relevant Army
  occupation-code pages and the Kenneth Weberg roster page were also
  inspected.
- No authenticated NARA Catalog API request was used.

## Reproducible release checks

- Audited content commit:
  `89d99a0d4cf2972abd093f54c77d9a0bc90c6fde`.
- Evidence-bundle SHA-256:
  `a93d300bf87e8c17108ba1f82d2c46402a9057e898b57018074d6ba68a5504f5`.
- Army-review-decision SHA-256:
  `fb102947b1d3a75d96bc9f5671ea195656891c08c9a644a00ae2783a5670c0fb`.
- Re-running the bundle generator reproduced the same evidence hash.
- Durable import: 8 sources, 3 organization inputs, 12 affiliations, 24
  claims, 56 claim-source links, 45 person updates and 45 research attempts.
- Batch claim confidence: 10 confirmed, 3 high, 10 medium and 1 conflicting.
  Publication disposition is 13 published, 10 qualified and 1 conflict
  claim.
- Review decisions: nine accepted official Army candidates and one retained
  conflict.
- Python: 154 tests passed locally and in the independent GitHub Actions run.
- Checked-in public manifest: 67 canonical assets, 134,804,462 bytes,
  SHA-256
  `9e401aa1e03541bb1cad8b81f072ce0d22a543569bb62a07f736be226b3eafc9`.
- Clean GitHub Actions Astro check: zero errors, zero warnings and zero hints.
- Clean static build: 25,310 pages.
- Bounded browser release suite: 99/99 checks passed across desktop, phone and
  tablet: 30 latest-batch checks, 33 core-route and interaction checks, 6
  analysis checks, and 30 accessibility scans with no serious axe
  violations.
- Internal links: 25,310 HTML files checked; all links resolve. The checker
  inventoried 52,276 unique external URLs separately.
- Clean-checkout public identifier audit: 25,382 artifacts checked against
  12,926 normalized private identifiers and 120 formatted variants. It found
  zero aggregate false positives, zero manifest-size false positives and zero
  unexpected boundary matches.
- Production dependency audit: zero vulnerabilities.

## Coverage published

- Index: 23,978/23,978 source rows linked (100.0000%).
- Research attempted: 16,115/23,936 people (67.3254%).
- Verified affiliation: 1,152/23,936 people (4.8128%).
- Verified employer: 523/23,936 people (2.1850%).
- Archival disposition assessed: 14,590/23,936 people (60.9542%).
- Not started: 7,816 people; in progress: 1,883 people.
- Research outcomes include 1,748 `occupation_only_found`, 8,875
  `requires_archival_review`, 440 `verified_employer_found`, 285
  `documented_prewar_employer_found` and 460 `conflicting_sources` people.
- Possible-duplicate groups: 679; conflicts: 540.
- Claim confidence: 1,809 confirmed; 5,382 high; 2,679 medium; 258 low;
  448 conflicting; and 2 unresolved.
- Public projection: 23,936 profiles, 4,073 affiliations, 1,322
  organizations, 6,574 sources and 10,314 published, qualified or conflict
  claims.
- Citations: 7,864 across 4,391 unique source documents.

## Publication verification

- Immutable published release commit:
  `89d99a0d4cf2972abd093f54c77d9a0bc90c6fde`.
- GitHub Actions Test run `41734939763` completed successfully on
  2026-11-03.
- GitHub Pages run `41734939490` completed successfully on 2026-11-03.
- On 2026-11-03, the unauthenticated deployed-release verifier checked the
  live GitHub Pages site against that exact commit and evidence bundle. It
  verified all 67 public assets (134,804,462 bytes; manifest SHA-256
  `9e401aa1e03541bb1cad8b81f072ce0d22a543569bb62a07f736be226b3eafc9`),
  all eight core routes, all 44 source-register pages and all 45 direct Batch
  1004 profile routes.

Public release URL: <https://therealjameswilson.github.io/before-oss/>.
