# Batch 991 release audit

Date: 2026-10-30 America/New_York

## Release contents

- NARA index page 486, rows 1-23: Jacques Voyer through Ladislav Hugh
  Vydra. Page 486, row 24, William Vyhnal, is the next cohort boundary.
- All 23 source rows remain separate people and have saved terminal research
  outcomes.
- Wayne S Vucinich and George M Vujnovich gain verified-employer outcomes.
  Their student, military and government pathways remain separately typed
  from civilian employment.
- Jacques Voyer's BCRA pathway publishes only with visible temporal
  qualification; his earlier Free French service remains separate.
- Two official Army categories publish only qualified occupations, never
  named employers. George Vuletic's undefined code 993 remains uninterpreted.
- Both Alexander S Vuchinich rows remain separate and ambiguous. Daniel
  Vujnovich and Daniel Vujovick also remain separate inside a visible
  possible-duplicate group.
- No authenticated NARA Catalog API request was used.
- The oil-company category remains 14 people linked to 15 historically named
  companies.

## Reproducible local release checks

- Audited content commit:
  `7f7822bd9cf7cdabc7b34a3e252e52f96c670749`.
- Evidence-bundle SHA-256:
  `22d94c81ae445faec3bbd7d579e8f49483382cd5e623f7fc3f426134b04b23ff`.
- Durable import: 12 sources, 6 organizations, 8 affiliations, 15 claims,
  37 claim-source links, 23 person updates and 23 research attempts.
- Review decisions: three accepted official Army identity candidates.
- Complete ingest audit and 200-profile stratified audit: every check passed.
- Python: 147 tests passed with the CI-equivalent `unittest discover`
  command.
- Targeted Batch browser matrix: 30/30 checks passed across desktop, phone
  and tablet.
- Clean-archive browser release suite: 99/99 current-batch, core-route,
  analysis and accessibility checks passed, including 30 axe scans with no
  serious or critical violations.
- Clean-archive Astro build: 622 files checked with zero diagnostics; 25,291
  canonical static pages built. Unrelated user-owned duplicate page files in
  the working checkout remain untouched and are not part of the release.
- Clean-archive internal links: 25,291 HTML files checked; all links resolve;
  52,219 unique external URLs were inventoried separately.
- Clean-archive identifier audit: 12,926 normalized identifiers and 120
  formatted variants checked across 25,363 artifacts; 1,466 candidate
  substrings and zero unexpected matches.
- Public manifest: 67 assets, 132,965,437 bytes, SHA-256
  `0a917647f633360fca8a780a8e109308b6219622472f3c02bbe6e233edb8ad53`.
- Public tree: 70 files, 135,312,593 bytes, SHA-256
  `6ef5b1879c05dd5c7efb36de8c837c6d5b215930698ac13d2df497301eb10bb4`.
- Determinism: two consecutive clean builds reproduced 25,363 files,
  422,788,354 bytes and tree SHA-256
  `68d01ea3fa3494b068859e8248f58096d7e1aba2d635b6685f9bff773fa3c4f3`.
- Production dependency audit: zero vulnerabilities.

## Coverage prepared for publication

- Index: 23,978/23,978 source rows linked (100.0000%).
- Research attempted: 15,725/23,936 people (65.6960%).
- Verified affiliation: 1,138/23,936 people (4.7543%).
- Verified employer: 516/23,936 people (2.1557%).
- Archival disposition assessed: 14,200/23,936 people (59.3249%).
- Not started: 8,206 people; in progress: 1,883 people.
- Claim confidence: 1,726 confirmed; 5,337 high; 2,570 medium; 255 low;
  439 conflicting; and 2 unresolved.
- Public projection: 23,936 profiles, 3,951 affiliations, 1,303
  organizations, 6,482 sources and 10,068 published, qualified or conflict
  claims.
- Citations: 7,769 across 4,337 unique source documents.

## Publication verification

Publication is pending the GitHub Actions Test and Pages workflows. This
section will identify the immutable release commit and unauthenticated live
verification only after both workflows succeed.
