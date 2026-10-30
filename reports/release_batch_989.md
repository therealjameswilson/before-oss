# Batch 989 release audit

Date: 2026-10-30 America/New_York

## Release contents

- NARA index page 485, rows 1-23: Alice Voiles through Herman W Von
  Meyerfeld. Page 485, row 24, Wilhelm-Viggo E.F. Von Moltke, is the next
  cohort boundary.
- All 23 source rows remain separate people and have saved terminal research
  outcomes: two occupation-only, eighteen archival-review, one documented-
  prewar-employer and two conflicting-source outcomes.
- Joseph C Vokoun Jr. and Mario H Volpe receive reviewed official Army
  occupation categories, never named employers. William J Volk and William
  Volpe retain identity bridges without unsupported occupation transfer.
- James Volosen's shared-identifier conflict and the truncated Wilhelm-Viggo
  E.F. Von Hoffmanst name conflict remain visible; no namesake employment is
  assigned.
- Nathalie Von Bretzel's documented National Park Junior College teaching is
  published as earlier employment, not as an immediate affiliation or last
  civilian employer.
- Maxim C Von Brevern and Gunther Von Fritsch receive qualified probable-
  identity context only. Unbridged namesakes create no public affiliations.
- No authenticated NARA Catalog API request was used.
- The oil-company category remains 14 people linked to 15 historically named
  companies.

## Reproducible local release checks

- Evidence-bundle SHA-256:
  `ca54ac159217b3fa0195d91ba89ef293cbbfada318949c0a9f1674ba09bc26ba`.
- Durable import: 9 sources, 3 organizations, 5 affiliations, 15 claims, 30
  claim-source links, 23 person updates and 23 research attempts; repeated
  imports replay to the same authoritative state.
- Review decisions: four accepted official Army identity candidates and two
  conflict-preservation decisions.
- Complete ingest audit and 200-profile stratified audit: every check passed.
- Python: 147 tests pass with the CI-equivalent `unittest discover` command.
- Targeted Batch browser matrix: 27/27 checks pass across desktop, phone and
  tablet.
- Clean-archive browser release suite: 96/96 current-batch, core-route,
  analysis and accessibility checks pass, including 30 axe scans with no
  serious or critical violations.
- Clean-archive Astro build: 620 files checked with zero diagnostics; 25,280
  canonical static pages built. Unrelated user-owned duplicate page files in
  the working checkout remain untouched and are not part of the release.
- Clean-archive internal links: 25,280 HTML files checked; all links resolve;
  52,186 unique external URLs were inventoried separately.
- Clean-archive identifier audit: 12,926 normalized identifiers and 120
  formatted variants checked across 25,352 artifacts; 1,462 candidate
  substrings and zero unexpected matches.
- Public manifest: 67 assets, 132,598,411 bytes, SHA-256
  `c198e65be6bd8c7adc023b52e56501eec95813c0dd3e3aa8753c904cec6a51c8`.
- Public tree: 70 files, 134,945,569 bytes, SHA-256
  `6a6e84c9f4eab7f844862d293e907cd77d63c5774e2f803690536df69562b123`.
- Determinism: two consecutive clean builds reproduced 25,352 files,
  422,166,684 bytes and tree SHA-256
  `400db4e65c75c4cb4eb9246296a758700782dd90bd27706e400a4b4fa2b3794c`.
- Production dependency audit: zero vulnerabilities.

## Coverage prepared for publication

- Index: 23,978/23,978 source rows linked (100.0000%).
- Research attempted: 15,679/23,936 people (65.5038%).
- Verified affiliation: 1,129/23,936 people (4.7167%).
- Verified employer: 510/23,936 people (2.1307%).
- Archival disposition assessed: 14,154/23,936 people (59.1327%).
- Not started: 8,252 people; in progress: 1,883 people.
- Claim confidence: 1,719 confirmed; 5,310 high; 2,558 medium; 255 low;
  438 conflicting; 2 unresolved.
- Public projection: 23,936 profiles, 3,926 affiliations, 1,292
  organizations, 6,451 sources and 10,021 published, qualified or conflict
  claims.
- Citations: 7,738 across 4,313 unique source documents.

## Publication verification

Batch 989 is public from audited release commit
`94b14df8e84a459e03d0c8f1786dc9fba6f7d00b`. GitHub Actions Test run
`41088622169` and Pages run `41088622180` both succeeded. The unauthenticated
deployed-release verifier matched all 67 manifested assets byte for byte across
132,598,411 bytes, verified eight core routes, all 44 source-register pages
and all 23 direct cohort profiles, and reproduced manifest SHA-256
`c198e65be6bd8c7adc023b52e56501eec95813c0dd3e3aa8753c904cec6a51c8`.
