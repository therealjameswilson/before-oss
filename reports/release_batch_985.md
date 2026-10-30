# Batch 985 release audit

Date: 2026-10-30 America/New_York

## Release contents

- NARA index page 483, rows 1-23: George Vetlesen through Peter P Viezbicke
  Jr. Page 483, row 24, Joseph P Viggiani, is the next cohort boundary.
- All 23 source rows remain separate people and have saved terminal research
  outcomes: two completed outcomes, one verified-employer outcome, one
  documented-prewar-employer outcome, six occupation-only outcomes, one
  conflict and 12 archival-review outcomes.
- Peter Viertel's Warner Bros. employment remains distinct from his immediate
  United States Marine Corps pathway into OSS. Alexander O Vietor's Cox &
  Stevens and Yale roles remain documented prewar work rather than immediate
  or last civilian employment.
- Four official Army categories remain qualified occupations rather than
  named employers. Thomas F Vietor Jr.'s Princeton affiliation remains student
  status, and Francis J Vicovari's ambulance work remains volunteer service.
- Edward C Viegel's protected-identifier collision with separately printed
  Edward C Veigel remains an identity conflict. Unbridged namesakes, snippets,
  relatives, genealogy and postwar-only leads create no public employers.
- No authenticated NARA Catalog API request was used.
- The oil-company category remains 14 people linked to 15 historically named
  companies.

## Reproducible local release checks

- Evidence-bundle SHA-256:
  `ea5f349d2139bb7309534a9a387bb1e58e14b5495bf96560f8b5cba4e19a1a3e`.
- Durable import: 14 sources, 6 organization inputs, 12 affiliations, 22
  claims, 48 claim-source links, 23 person updates and 23 research attempts;
  repeated imports replay to the same authoritative state.
- Review decisions: three accepted and one conflicting official Army identity
  candidate.
- Complete ingest audit and 200-profile stratified audit: every check passed.
- Python: 147 tests pass.
- Astro: 616 files checked with zero diagnostics; 25,272 static pages built
  from a clean worktree.
- Batch browser matrix: 27/27 checks pass across desktop, phone and tablet.
- Browser release suite: 96/96 checks pass, including 30 axe scans with no
  serious or critical violations.
- Internal links: 25,272 HTML files checked; all links resolve.
- Identifier audit: 12,926 normalized identifiers and 120 formatted variants
  checked across 25,344 clean output artifacts; 1,441 candidate substrings and
  zero unexpected matches.
- Public manifest: 67 assets, 132,055,053 bytes, SHA-256
  `9211cf135ed73a1edb263db621ba6228bb12c5d26c8254a0f615175d0c2610d4`.
- Public tree: 70 files, 134,402,210 bytes, SHA-256
  `6f5e5deb10e87b10ddca1c0e107b32a66e6749ab8b0ee30cb4c018f3793fc967`.
- Determinism: two consecutive clean builds reproduced 25,344 files,
  421,256,782 bytes and tree SHA-256
  `145dc7f3bf4df1d93fb4ca358275245de442908391fcbc777c98711eb20bbc4e`.
- Production dependency audit: zero vulnerabilities.

## Coverage prepared for publication

- Index: 23,978/23,978 source rows linked (100.0000%).
- Research attempted: 15,587/23,936 people (65.1195%).
- Verified affiliation: 1,124/23,936 people (4.6959%).
- Verified employer: 505/23,936 people (2.1098%).
- Archival disposition assessed: 14,063/23,936 people (58.7525%).
- Not started: 8,344 people; in progress: 1,883 people.
- Claim confidence: 1,718 confirmed; 5,267 high; 2,524 medium; 255 low;
  436 conflicting; 2 unresolved.
- Public projection: 23,936 profiles, 3,889 affiliations, 1,285 organizations,
  6,419 sources and 9,941 published, qualified or conflict claims.
- Citations: 7,706 across 4,294 unique source documents.

## Publication verification

Local release checks pass. Public commit, GitHub Actions run identifiers and
the unauthenticated manifest/profile verification will be recorded after the
content commit deploys successfully.
