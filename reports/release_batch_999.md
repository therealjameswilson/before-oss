# Batch 999 release audit

Date: 2026-11-03 America/New_York

## Release contents

- NARA index page 490, rows 1-23: Robert E. Walters through John H.
  Warburton. Page 490, row 24, Betty Lou Ward, is the next cohort boundary.
- All 23 printed rows remain separately recoverable and have saved terminal
  research outcomes: 16 `requires_archival_review`, 5
  `occupation_only_found`, 1 `conflicting_sources` and 1
  `documented_prewar_employer_found`.
- Identity disposition is 7 confirmed, 2 high-confidence, 1 probable, 1
  conflicting and 12 unresolved people.
- Seven official Army bulk-record bridges were accepted. Alan T. Walther,
  Daniel W. Walton, Rafael Wand, Newton R. Wantland and John H. Warburton have
  qualified historical occupation categories; Wilson W. Waltz and Kenneth
  Wanamaker have identity evidence only. No named employer or immediate
  Army-to-OSS sequence was inferred from those records.
- The shared protected-identifier candidate for Joseph A. Walukinas conflicts
  with a materially different indexed name. The identifier remains private,
  the evidence was not transferred, and the conflict is visible publicly.
- A scholarly source and two University of Chicago finding aids support
  high-confidence, date-bounded employment for Douglas Waples at the
  University of Chicago. It is published as documented prewar employment, not
  as an immediate predecessor or last civilian employer.
- An official Army order of battle supports a qualified, probable pre-OSS
  military assignment for Harry F. Wanvig as commander of the 309th Field
  Artillery Regiment through October 1940. The intervening chronology remains
  unresolved and requires the Box 815 file.
- Scholarly evidence supports Robert E. Wampler's identity and OSS Special
  Operations assignment in Kunming, but no reliable pre-OSS employer was
  established. His profile does not invent one.
- The transparent rank normalizer now recognizes the fully spelled printed
  rank `Major`. The monotonic refresh corrected 43 source rows representing 41
  people, including Wampler, without changing the original printed fields.
- The CIA adapter stopped at the current robots restriction and was not
  bypassed. The first Library of Congress request timed out and was not
  misreported as a negative result. Accessible official, institutional,
  scholarly and staged web evidence was reviewed and rejection reasons were
  retained for unsupported common-name candidates.
- No authenticated NARA Catalog API request was used.

## Reproducible local release checks

- Audited content commit:
  `a11aa2cafc5cf5eeaf61466f756cabad0b18175e`.
- Evidence-bundle SHA-256:
  `ec656af0afa3c934f9ed6c09cd7fdad653d95719fea291fb3acf9f0daba054ff`.
- Re-running the bundle generator reproduced the same evidence hash.
- Durable import: 9 sources, 2 organizations, 7 affiliations, 18 claims, 42
  claim-source links, 23 person updates and 23 research attempts.
- Batch claim confidence: 7 confirmed, 3 high, 7 medium and 1 conflicting.
  Publication disposition is 10 published, 7 qualified and 1 conflict claim.
- Review decisions: seven accepted and two conflicting official Army
  candidates.
- Stratified profile audit: every check passed for 200 profiles.
- Python: 151 tests passed with the CI-equivalent `unittest discover`
  command.
- Targeted Batch browser matrix: 30/30 checks passed across desktop, phone and
  tablet.
- Current-worktree browser release suite: 99/99 current-batch, core-route,
  analysis and accessibility checks passed, including 30 axe scans with no
  serious violations.
- Clean-worktree browser release suite: 98 checks passed and one tablet axe
  check encountered a browser timeout; that exact check passed immediately in
  isolation. The independent GitHub Actions clean run subsequently passed the
  entire bounded suite.
- Clean-worktree Astro build: 630 files checked with zero diagnostics; 25,302
  canonical static pages built.
- Clean-worktree internal links: 25,302 HTML files checked; all links resolve;
  52,249 unique external URLs were inventoried separately.
- Public identifier audit: the local and independent CI checks found zero
  aggregate, manifest-size or unexpected boundary matches in the public
  projection.
- Public manifest: 67 canonical assets, 133,812,408 bytes, SHA-256
  `58f850dbf694e2286fdd535272d3af938b3818f08287839e5447efb79027880f`.
- Public tree: 70 files, 136,159,565 bytes, SHA-256
  `f127922de03da022e97963010bfed7c6e97087201b228182df8c132f8a5c3949`.
- Determinism: two consecutive clean builds reproduced 25,374 files,
  424,185,696 bytes and tree SHA-256
  `5129141a731827d6dcb070dfa4fa399fdf6acac98e7811f9f66927291bc8d50d`.
- Production dependency audit: zero vulnerabilities.
- GitHub noted non-blocking future runner-maintenance warnings for Node 20-
  based action internals and the `ubuntu-latest` image migration. No test,
  build, privacy-audit or deployment step failed.

## Coverage published

- Index: 23,978/23,978 source rows linked (100.0000%).
- Research attempted: 15,909/23,936 people (66.4647%).
- Verified affiliation: 1,146/23,936 people (4.7878%).
- Verified employer: 519/23,936 people (2.1683%).
- Archival disposition assessed: 14,384/23,936 people (60.0936%).
- Not started: 8,022 people; in progress: 1,883 people.
- Research outcomes include 1,704 `occupation_only_found` and 8,725
  `requires_archival_review` people.
- Possible-duplicate groups: 679; conflicts: 536.
- Claim confidence: 1,762 confirmed; 5,360 high; 2,622 medium; 255 low;
  444 conflicting; and 2 unresolved.
- Public projection: 23,936 profiles, 4,008 affiliations, 1,314
  organizations, 6,533 sources and 10,184 published, qualified or conflict
  claims.
- Citations: 7,820 across 4,363 unique source documents.

## Publication verification

- Immutable published release commit:
  `a11aa2cafc5cf5eeaf61466f756cabad0b18175e`.
- GitHub Actions Test run `41684339739` completed successfully at
  `2026-11-03T17:31:14Z`.
- GitHub Pages run `41684339666` completed successfully at
  `2026-11-03T17:28:54Z`.
- On 2026-11-03, the unauthenticated deployed-release verifier checked the
  live GitHub Pages site against that exact commit and the Batch 999 evidence
  bundle. It verified all 67 public assets (133,812,408 bytes; manifest
  SHA-256
  `58f850dbf694e2286fdd535272d3af938b3818f08287839e5447efb79027880f`),
  all eight core routes, all 44 source-register pages and all 23 direct Batch
  999 profile routes.

Public release URL: <https://therealjameswilson.github.io/before-oss/>.
