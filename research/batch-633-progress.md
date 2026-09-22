# Batch 633: PDF pages 401-410 and McCormick-McCracken research

All **460** printed rows on original NARA PDF pages 401-410 were compared
against SQLite at 180 dpi. Page 402 retains its earlier authoritative
`reviewed_matches` decision from the deterministic random-page audit. The
other nine pages match the current extraction and require no correction. This
adds nine pages and **414** rows to the complete-page ledger. Visual review now
covers **337/522 pages** and **15,468/23,978 rows**: **15,436** reviewed rows
match the extraction, **32** retain reviewed corrections, and **8,510** remain
for complete visual comparison.

The complete page-306 `Howard P. McCormick` through `Charles McCracken Jr.`
queue contains **23** people. Its Library of Congress pass saved one live
result for every person and created **44** discovery candidates across ten
people. Every official item context was inspected. Thirty-nine candidates were
rejected because they concerned conflicting initials, unrelated OCR or lists,
postwar material, famous namesakes, or common names without an indexed-person
bridge. Five independent contexts consistently identify Major General Frank
R. McCoy. Exact full-name and exceptional-rank agreement support a probable,
medium-confidence identity finding, but not a confirmed OSS relationship or a
pre-OSS employer. The profile therefore remains `needs_identity_review` and
directs researchers to Box 501.

Four official Army bulk candidates were reviewed. Howard P. McCormick, John
F. McCormick, and Charles McCracken Jr. received high-confidence identity
crosswalks from exact normalized names and nonshared protected identifiers.
Fixed-width `MC CORMICK` and `MC CRACKEN` spacing is treated as formatting,
not a public name variant. The protected identifier printed for indexed
Corporal William J. McCoy instead resolves to a wholly different Army name and
grade. That Army identity was not assigned to McCoy; his profile is explicitly
`conflicting_sources` pending Box 501 review. Army grade and occupation codes
were not converted into employers or predecessor affiliations. The adjacent
Virgina McCoud and Virgina C. McCould rows remain separate ambiguous entities
in duplicate group `p306-virgina-mccoud-mccould-b623` pending comparison of
Boxes 500 and 499.

The final 23-person queue state is **19** `in_progress`, three
`needs_identity_review`, and one `conflicting_sources`. All 48 candidates have
review decisions; none remains unreviewed. This is research-attempt progress,
not completion of the minimum research protocol. No new employer or
affiliation claim was made.

Rebuilt coverage remains **23,978/23,978** linked source rows and **23,939**
active person entities. Research-attempt coverage is **7,675/23,939
(32.0607%)**; confirmed/high verified-employer coverage is **280/23,939
(1.1696%)**; confirmed/high verified-affiliation coverage is **628/23,939
(2.6233%)**; archival-review disposition coverage is **6,300/23,939
(26.3169%)**. There are **16,250** `not_started` people, **488** active
possible-duplicate groups, and **160** active people with conflicting identity
or source status. The database stores **12,750** attempts or plans and **4,922**
claims: **1,311** confirmed, **1,915** high, **1,375** medium, **187** low,
and **134** conflicting. It contains **5,058** source/citation records and
**2,381** unique document keys. The public projection contains **2,224**
affiliations, **708** organizations, **3,851** sources, and **4,731** claims.
The oil-company category remains a supported, incomplete evidence set of seven
people across nine companies. Full-index historical research is unfinished.

## Local release verification

The isolated tracked-only release candidate passed all local gates: **132/132**
Python tests; all seven checks in the 200-profile stratified structural audit;
Astro diagnostics across **264** source files with zero errors, warnings, or
hints; a **24,681**-page static build; and the complete bounded **84/84**
desktop, phone, tablet, analysis, and accessibility suite. Every internal link
resolved across 24,681 HTML files. The identifier audit found zero unexpected
full-number boundary matches across **24,753** artifacts. All **67** public
manifest assets verified, totaling **98,230,826** bytes at manifest SHA-256
`f1041c176097ee821e71a6b3904f96ba4eeb19e6512cd0731460cf26810f2a13`.
Two consecutive clean builds reproduced output-tree SHA-256
`3305acea947a144e5e7b86ced0ad1440d9e2cb9dc037f932d57f4030fad65e0c`.
These local checks do not by themselves establish CI or public deployment.

## Replay and continuation

After importing prior durable batches into private SQLite:

```sh
python3 -m oss_research import-page-reviews research/parser_visual_review_pages401-410_2026-09-22.json
python3 -m oss_research import-review-decisions research/loc_review_decisions_2026-09-22_batch633.csv
python3 -m oss_research import-review-decisions research/identity_review_decisions_2026-09-22_batch633.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page306-mccormick-mccracken-review_batch-633_2026-09-22.json
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
```

Continue with the next bounded research and visual-audit batch, then rebuild:

```sh
python3 -m oss_research export-adapter-checkpoints
python3 -m oss_research export-derived
python3 -m oss_research build-public-data
python3 -m oss_research coverage-report
```

No API key, full service number, raw API response, copyrighted page image, or
private reviewer note is committed or included in the public site. No
authenticated NARA Catalog request was made.
