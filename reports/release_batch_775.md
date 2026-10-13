# Batch 775 release record

Date: 2026-10-13 America/New_York

## Scope

Batch 775 covers PDF page 377, rows 24-46, Isma L Price through Charles E
Prieve. All 23 printed rows remain preserved and linked to 23 distinct person
entities. Twenty-two people received new terminal manual research attempts;
Edgar A Prichard already had a terminal reviewed outcome and published evidence
from an earlier cross-index batch. The next indexed boundary is page 378, row
1, Vangjel Prifti.

## Research outcome

- The batch records 20 `requires_archival_review` outcomes, one
  `conflicting_sources` outcome, one `occupation_only_found` outcome, and one
  `verified_employer_found` outcome.
- Nancy M Prichard has a high-confidence identity match and a high-confidence
  immediate pre-OSS employment claim. Smithsonian Institution Archives states
  that Nancy McCandlish Prichard worked for three years as Special Assistant to
  the Meteorologist at the Smithsonian Astrophysical Observatory before joining
  OSS. A Washington Post obituary independently corroborates Smithsonian
  employment, civilian OSS status, and Cairo service.
- Edgar A Prichard's existing published pathway remains unchanged: immediate
  pre-OSS service as an Army company clerk and an earlier Oklahoma journalism
  occupation, with no newspaper employer inferred.
- Ten Army identity candidates were accepted and one candidate was retained as
  conflicting. Robert R Price and Wayne E Price retain `Jr` as an official
  source variant. Indexed Ellwood Pride retains the Army-source spelling
  `Elwood` as a variant. No coded Army occupation was converted into an
  employer.
- Raford C Price remains a visible conflict because the Army record associated
  with the protected identifier carries a materially different name.
- NARA Catalog work was dry-run only: 22 new planned searches, one duplicate,
  and zero authenticated requests. CIA and LoC adapters failed closed on their
  first eligible requests. Access errors were not treated as negative
  historical evidence.
- The page-batch command now supports explicit, validated reassignment from a
  named prior batch. This was used only to move Ursula E Price from the stranded
  `pilot-v1` assignment into Batch 775; two focused tests cover the safeguard.

## Exact coverage at export

- Index: 23,978/23,978 linked rows (100%).
- Active person entities: 23,939.
- Research attempted: 10,825/23,939 (45.2191%).
- Verified employer: 354/23,939 (1.4788%).
- Verified affiliation: 793/23,939 (3.3126%).
- Archival review assessed: 9,284/23,939 (38.7819%).
- Not started: 13,109.
- Possible duplicate groups: 540.
- Conflicts: 368.
- Claims: 1,408 confirmed; 3,332 high; 1,586 medium; 202 low; 321
  conflicting; two unresolved.
- Citations: 5,941 records representing 3,059 unique source documents.

## Local release gates

- Python: 141 tests passed.
- Profile audit: all seven checks passed for the deterministic 200-profile
  sample.
- Astro: 409 source files checked with zero errors, warnings, or hints; 24,894
  HTML pages built.
- Browser: 84/84 desktop, phone, tablet, analysis, and accessibility checks
  passed, including 30 axe checks and all 15 Batch 775 checks.
- Extraction: 522/522 pages and 23,978/23,978 rows validated; all 32 parser
  warnings have completed visual review.
- Links: all 24,894 generated HTML files passed internal-link checks; 50,918
  unique external URLs were inventoried.
- Redaction: zero unexpected full service-number matches across 24,966
  artifacts.
- Dependencies: the production audit found zero vulnerabilities.
- Manifest: 67 assets, 109,184,287 bytes, SHA-256
  `8f588272d89935954b05f9ff74e95eb5cab53664af00288b191667fcfcfc5440`.
- Determinism: two consecutive builds produced public-tree SHA-256
  `131dd141dd352a612334cb7619aafc2f67123036ec36333450840071a333f23b`
  across 70 files and 111,531,438 bytes, and production-tree SHA-256
  `a48a67b062a1fe4ee4fd3ec6d500e10caaca0334046f12455eb5717dd9d311fd`
  across 24,966 files and 313,205,405 bytes.

## Publication

Publication details are recorded after the immutable release commit passes the
GitHub test and Pages deployment workflows and the unauthenticated live site is
verified against that commit.
