# Batch 635: PDF pages 421-430 and McDonald-McDowell research

All **460** printed rows on original NARA PDF pages 421-430 were compared
against SQLite at 180 dpi. Every page matches the current extraction and
requires no correction. Page 424 had already been reviewed in the deterministic
random sample, so this batch adds nine pages and 414 rows to the complete-page
ledger. Visual review now covers **356/522 pages** and **16,342/23,978 rows**:
**16,310** reviewed rows match the extraction, **32** retain reviewed
corrections, and **7,636** remain for complete visual comparison.

The complete page-307 `Mary B. McDonald` through `Michael V. McDowell` queue
contains **23** people. Its Library of Congress pass saved at least one live
result for every person and created **28** discovery candidates across ten
people. Every official item context was inspected. All 28 candidates were
rejected because they concerned conflicting initials, unrelated or contextless
names, postwar material, or common names without an indexed-person bridge.

Six official Army bulk candidates were reviewed. Michael V. McDowell, Paul J.
McDougall, Thomas F. McDonnell, and William P. McDonough received
high-confidence identity crosswalks from nonshared protected identifiers and
exact or carefully qualified name agreement. Fixed-width surname spacing is
treated as formatting, while the sourced `MC DONELL` one-letter variant for
Thomas remains visible. Differences between Army-entry and index grades remain
chronology questions for the personnel file; neither Army grades nor occupation
codes were converted into employers or predecessor affiliations.

The protected identifiers printed for indexed Privates Raymond W. McDonald and
Roy W. McDonald resolve to conflicting Army names. Those Army identities were
not assigned to either person, and a same-name institutional employment lead
for Roy remains unassigned because it has no indexed-person bridge. Both
profiles are explicitly `conflicting_sources` pending Box 503 review, and the
other Army names and full identifiers are withheld from public output.

The two adjacent Robert L. McDougal rows remain separate ambiguous entities in
duplicate group `p307-robert-l-mcdougal-two-rows-b623`. One printed row has a
T/5 grade but no protected identifier; the other has an identifier but no
grade. The evidence does not establish that they are one person, so both
immutable source rows and both cautious person entities remain distinct pending
comparison of the Box 503 files.

The final 23-person queue state is **19** `in_progress`, two
`needs_identity_review`, and two `conflicting_sources`. All **34** candidates
have review decisions; none remains unreviewed. This is research-attempt
progress, not completion of the minimum research protocol. No new employer or
affiliation claim was made.

Rebuilt coverage remains **23,978/23,978** linked source rows and **23,939**
active person entities. Research-attempt coverage is **7,721/23,939
(32.2528%)**; confirmed/high verified-employer coverage is **280/23,939
(1.1696%)**; confirmed/high verified-affiliation coverage is **628/23,939
(2.6233%)**; archival-review disposition coverage is **6,300/23,939
(26.3169%)**. There are **16,208** `not_started` people, **488** active
possible-duplicate groups, and **163** active people with conflicting identity
or source status. The database stores **12,823** attempts or plans and
**4,934** claims: **1,311** confirmed, **1,924** high, **1,375** medium,
**187** low, and **137** conflicting. It contains **5,062** source/citation
records and **2,383** unique document keys. The public projection contains
**2,224** affiliations, **708** organizations, **3,855** sources, and
**4,743** claims. The oil-company category remains a supported, incomplete
evidence set of seven people across nine companies. Full-index historical
research is unfinished.

## Replay and continuation

After importing prior durable batches into private SQLite:

```sh
python3 -m oss_research import-page-reviews research/parser_visual_review_pages421-430_2026-09-22.json
python3 -m oss_research import-review-decisions research/loc_review_decisions_2026-09-22_batch635.csv
python3 -m oss_research import-review-decisions research/identity_review_decisions_2026-09-22_batch635.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page307-mcdonald-mcdowell-review_batch-635_2026-09-22.json
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
