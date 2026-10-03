# Batch 692 release - Myers-Nader research

Research and local release date: 2026-10-02 America/New_York.

## Historical work

Batch 692 covers PDF page 336, rows 23-45, from Jack M Myers through Thomas G
Nader. Fresh page inspection confirmed all 23 printed rows, preserved the
literal note `retained` for Marinus D Myrland, and treated Thomas G Nader's
all-numeric rank-column value as a displaced identifier that is masked rather
than represented as a rank.

Gunnar G Mykland is a high-confidence identity match across two authoritative
government sources. A National Park Service note identifies him as executive
officer of OSS Detachment 202 and cites his November 1, 1944 report. The
October 1939 federal *Monthly Catalog* names Gunnar Mykland as assistant
director of the Housing Authority of Austin. That job is published only as
documented prewar employment: the reviewed evidence does not establish that it
was his immediate pre-OSS affiliation or last civilian employer before wartime
service.

Marinus D Myrland is a high-confidence match to the Operation Rype member whose
rare name and protected identifier appear in a scholarly history, with OSS
service independently recorded in a NARA-based Operational Groups roster. The
history calls him a former ship's engineer. The site publishes that as an
occupation, without inventing a vessel, shipping company, or immediate
chronology.

James H Mysberch is a high-confidence match to James H Mysbergh. Official Army
bulk data agrees on the protected identifier and name components across the
one-letter spelling difference; a declassified 1945 OSS Detachment 101 report
independently prints James H Mysbergh. Both spellings remain searchable.

Official Army bulk data also supports high-confidence identity matches for
Thomas L Myers, Walter R Myers, William L Myers, Richard Myrick, and Joseph E
Nadeau. Four incompatible shared-identifier cases remain visible as conflicts,
and Kenneth Mygatt remains ambiguous rather than receiving a tempting but
unproved travel-company affiliation. The featured oil-company category remains
**nine people across 11 historically named companies**.

## Reproducible coverage

| Measure | Count |
| --- | ---: |
| Printed index rows preserved and linked | 23,978 / 23,978 |
| Visually audited extraction | 23,978 / 23,978 rows; 522 / 522 pages |
| Active person entities | 23,939 |
| People with nonplanned research attempts | 8,961 (37.4326%) |
| People with confirmed/high employer evidence | 313 (1.3075%) |
| People with confirmed/high affiliation evidence | 693 (2.8949%) |
| Archival-review dispositions assessed | 7,418 (30.9871%) |
| Not started | 14,973 |
| Possible duplicate groups | 518 |
| Conflicts | 258 |
| Attempts or plans | 16,165 |
| Claims by confidence | confirmed 1,340; high 2,566; medium 1,458; low 196; conflicting 231 |
| Citation records / unique source documents | 5,424 / 2,668 |

Research statuses are: `blocked_by_source_access` 1; `candidate_found` 333;
`completed` 157; `conflicting_sources` 215;
`documented_prewar_employer_found` 150; `in_progress` 1,904;
`needs_identity_review` 442; `needs_temporal_review` 23;
`no_reliable_result_after_protocol` 646; `not_started` 14,973;
`occupation_only_found` 1,036; `requires_archival_review` 3,783; and
`verified_employer_found` 276.

The public projection contains **2,365** published affiliations, **792**
organizations, **4,207** public sources, and **5,588** published claims.
Full-index historical research remains unfinished.

## Local verification

The exact rebuilt tree passed these release gates:

- Python unit suite: **139 / 139 passed**.
- Ingest validation: **23,978 / 23,978 rows**, **522 / 522 pages**, SQLite
  quick check `ok`, no foreign-key errors, and all parser-warning rows visually
  resolved.
- Stratified profile audit: **200 profiles**, with every identity, queue,
  commissioned-category, duplicate-review, source-row, and public-projection
  invariant passing.
- Astro diagnostics: **326 files**, **0 errors, 0 warnings, 0 hints**.
- Production build: **24,768 pages**.
- Browser release suite: **90 / 90 passed** across desktop, phone, and tablet
  (21 Batch 692, 33 core, six analytics, and 30 accessibility checks).
- Link check: **24,768 HTML files** checked; every internal link resolved and
  50,520 unique external URLs inventoried for the separate live check.
- Public manifest: **67 assets / 102,952,273 bytes** verified; manifest SHA-256
  `a8bd64bd4b1c7cb47062a7feca6d6ea31fa10a089215f4c24342dd5ef1eb756f`.
- Private-identifier audit: **24,840 artifacts** scanned with **0 unexpected
  boundary matches**.
- Production dependency audit: **0 vulnerabilities**. Astro and Sharp are
  build-only development dependencies because the deployed GitHub Pages
  artifact is static and has no Node runtime.
- Build-tool audit: two high-severity findings remain in Astro's build-only
  `http-cache-semantics` dependency; the advisory currently lists no patched
  release. The affected shared authenticated-cache behavior is not present in
  the static deployment. The suggested forced downgrade to Astro 2.10.9 was
  not applied. See <https://github.com/advisories/GHSA-ch52-4w7c-c8xp>.
- Determinism: two consecutive build trees matched at **24,840 files /
  302,975,457 bytes**, SHA-256
  `d499040c9024550fd1c77786fcaf26cf678b5c2865cc90ac242ba0e2f236bb23`.

## Publication status

Publication to GitHub Pages and post-deployment byte verification are pending.

## Resume

```sh
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
python3 -m oss_research import-review-decisions research/identity_review_decisions_2026-10-02_batch692.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page336-myers-nader-review_batch-692_2026-10-02.json
python3 -m oss_research export-adapter-checkpoints
python3 -m oss_research export-derived
python3 -m oss_research export-review-queue
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
```

No API key, raw API response, full service number, copyrighted page image,
unrelated Army coded occupation, street address, or private reviewer note is
committed or published. No authenticated NARA Catalog API request was made for
this batch.
