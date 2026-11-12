# Batch 1059 release audit

Research and release preparation date: 2026-11-11 America/New_York.

## Release contents

- NARA index page 314, rows 1-46: Francis C. McVarish through D.
  Meedsellen. The official 522-page PDF matched the frozen provenance
  manifest, and page 314 was rendered and visually checked. All 46 printed
  rows remain separately recoverable through 46 cautious active person
  entities.
- Every person in the cohort has a saved terminal outcome: 23
  `requires_archival_review`, ten `occupation_only_found`, seven
  `needs_identity_review`, three `verified_employer_found`, two `completed`,
  and one `conflicting_sources`.
- Eleven accepted, nonshared, wartime-dated Army identity links support broad
  qualified occupational categories: author/editor/reporter; sailor or
  deckhand outside the U.S. Navy; packing/filling/labeling/marking/bottling;
  civil engineer; guide; manager or official; stock clerk; mining engineer;
  retail manager; chauffeur or driver; and sales clerk. None identifies a
  named employer or proves an Army-to-OSS chronology. The relevant official
  Army code-list pages 170-174 were visually checked before the categories
  were published.
- Edwin E. Meader retains his stronger, high-confidence Kalamazoo Vegetable
  Parchment Company last-employer and Army-pathway findings. His Army-entry
  category is a separate qualified occupation and is not tied to the company.
  Julia C. McWilliams retains her confirmed personnel-file chronology, and
  Robert H. McWilliams retains his ONI and Denver District Attorney findings.
  A 1945 Army entry for Robert H. McWilliams was not promoted as a pre-OSS
  occupation because its chronology does not support that use.
- Donn P. Medalie's documented Foreign Service affiliation and Thomas O.
  Medlicott's explicit Coast Guard-to-OSS pathway are preserved as government
  or military assignments, not civilian employers. David C. Meck's probable
  identity and qualified law-school and Federal Security Agency affiliations
  remain visible pending a direct personnel-file bridge.
- Two duplicate boundaries remain unresolved: the adjacent identical Mary P.
  Meade rows and the adjacent Lorraine M. Meader/Meador spelling variants. All
  four people remain separate pending personnel-file evidence.
- R. McVickerst and Aneo Mediler retain conflicting identity links and remain
  in identity review. Two incompatible Army records share Joseph B.
  Medagliant's printed identifier; neither was selected. No occupation or
  biography crossed any conflict boundary.
- Exact-name official, institutional, obituary, archival, employment, and OSS
  searches were recorded as applicable. Search snippets, people-finder pages,
  genealogy, and chronologically irrelevant namesakes were not used as final
  evidence. No authenticated NARA Catalog API request was made.

## Evidence and import

- Reviewed evidence bundle: four sources, no new organizations, 11 qualified
  affiliations, 11 occupation claims, 46 person updates, and 46 research
  attempts. Existing reviewed identity, employer, pathway, duplicate, and
  conflict claims were not duplicated.
- The evidence import was tested twice against a disposable database and was
  idempotent: both imports reported the same 11 affiliations, 11 claims, 44
  claim-source links, four sources, 46 person updates, and 46 attempts.
- Evidence-bundle SHA-256:
  `fdf4d6deb60b89d2f984b056ea79b248e6c2185adecb9693c7a1222cd6271c30`.
- After import, export, coverage, and profile-audit runs, the release database
  has SHA-256
  `c503b3871ee37c41c4fe5b4ab4b3084cb85e684185754606fac8e3bda5d57256`.
- SQLite integrity is `ok`, foreign-key violations are zero, all 46 page-314
  people have terminal outcomes, and every new public affiliation has one
  inspectable claim with four linked source assessments.

## Coverage prepared for publication

- Index: 23,978/23,978 source rows linked (100.0000%).
- Research attempted: 17,989/23,935 active people (75.1577%). The count is
  unchanged because the cohort already had saved nonplanned attempts.
- Verified affiliation: 1,261/23,935 people (5.2684%).
- Verified employer: 578/23,935 people (2.4149%).
- Archival disposition assessed: 16,871/23,935 people (70.4867%). The count is
  unchanged because all page-314 profiles already had an assessed archival
  priority.
- Not started: 5,946 people; in progress: 1,354 people.
- Research outcomes include 2,362 `occupation_only_found`, 10,453
  `requires_archival_review`, 489 `verified_employer_found`, 309
  `documented_prewar_employer_found`, 649 `needs_identity_review`, 53
  `needs_temporal_review`, 501 `conflicting_sources`, and 330 `completed`
  people.
- Claim confidence: 2,050 confirmed; 5,731 high; 3,378 medium; 263 low; 480
  conflicting; and two unresolved.
- Public projection: 23,935 profiles, 4,935 affiliations, 1,440 organizations,
  7,079 sources, and 11,635 published, qualified, or conflict claims.
- Citations: 8,374 across 4,714 unique source documents.
- Possible duplicate groups: 712. Total conflict flags: 584.
- Private derived data contain 4,962 affiliations, 1,454 organizations,
  33,225 research attempts, 20,441 unresolved rows, and 23,488 NARA pull-list
  rows.

## Local publication verification

- Twelve focused Batch 1058 and Batch 1059 Python tests passed before the
  canonical import; all six Batch 1059 tests passed again against the imported
  canonical database. The complete Python suite is reserved for the clean
  GitHub runner because the local virtual environment contains macOS iCloud
  placeholders that can stall broad test discovery.
- Astro and TypeScript validation reported zero errors, warnings, or hints in
  a fully materialized temporary checkout built from the repository's local
  Git objects and overlaid with the Batch 1059 data.
- Static build: 25,431 pages. The public-asset copy contains 70 files totaling
  147,960,957 bytes.
- Bounded browser release suite: 87/87 checks passed across desktop, phone, and
  tablet: 18 Batch 1059 checks, 33 core-route and interaction checks, six
  analysis checks, and 30 accessibility scans with no serious or critical axe
  violations.
- Internal links: 25,431 HTML files checked; all links resolve. The checker
  inventoried 52,631 unique external URLs separately.
- Checked-in public manifest: SHA-256
  `1541adf54da885ba1f8231dd79b273aad2332f8c1b1fcf48b204a9626f9a56db`.
  The same manifest was copied into the production tree.
- Public-identifier audit: 25,503 output artifacts checked against 12,926
  normalized private identifiers and 120 formatted variants. It inspected
  1,590 candidate substrings and found zero aggregate, manifest-size, or
  unexpected boundary matches.
- The deterministic 200-profile stratified audit passed all seven defined
  gates.

## Deployment status

- Local research, data, and publication gates have passed. Clean GitHub Test
  and Pages workflow results and independent deployed verification will be
  appended after publication.

Public base URL: <https://therealjameswilson.github.io/before-oss/>.

Full-index historical research remains unfinished.
