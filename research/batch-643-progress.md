# Batch 643: PDF pages 501-510 and McNamara-McNutt research

All **460** printed rows on original NARA PDF pages 501-510 were compared
against SQLite at 180 dpi. Page 506 was already in the deterministic-random
visual-review ledger. Every row matches the current extraction and requires no
correction. Complete-page visual review now covers **424/522 pages** and
**19,470/23,978 rows**: **19,438** reviewed rows match the extraction, **32**
retain reviewed corrections, and **4,508** remain for complete visual
comparison.

The page-313 `James J. McNamara` through `Mack McNutt` queue contains 23
source rows representing **23** cautious person entities. A live Library of
Congress attempt is saved for every person. The pass created 17 newspaper
candidates across seven people; every item context was inspected and rejected
because it identifies a different name or initial, is postwar, or supplies no
OSS, rank, protected-identifier, or Box 511-512 bridge. No namesake occupation
was transferred. In particular, a casualty report's truck-driver occupation
belongs to William C. McNeil, not indexed William D. McNeil.

Thirteen preexisting official Army or duplicate-boundary candidates received
review decisions. Exact normalized names and nonshared protected identifiers
support high-confidence identity crosswalks for Thomas J. McNamara, William D.
McNeely, Edward F. McNeil, Volney G. McNeill, Harry P. McNickle, John J.
McNulty, Joseph G. McNulty, and Joseph S. McNulty. The official `Jr.` suffix
for Joseph S. McNulty is preserved as a variant without changing the indexed
display name. The discrepant or malformed Army grade for Harry P. McNickle is
retained as review context, not treated as a contradiction in the unique-name
and unique-identifier crosswalk.

One protected-identifier conflict remains visible. The identifier printed for
Coy I. McNeil points to an official Army entry rendered `MC VIEL/COY`. The
surname and middle-initial evidence conflict, so Coy remains `conflicting`,
requires critical Box 512 review, and receives no identity or employment
inference from that entry.

James E. McNearnry and James E. McNerney remain two separate probable entities.
Their adjacent Box 512 rows share a protected identifier but differ in indexed
surname and rank; the official Army entry favors `MC NERNEY JAMES E`. Both
source rows, both entities, and the possible-duplicate group remain visible
pending review of both jackets. Full identifiers are excluded from public
output. Army grade, entry date, and occupation codes are identity context, not
employer evidence.

The final 23-person queue state is **20** `in_progress`, two
`needs_identity_review`, and one `conflicting_sources`. All **30** candidates
in the cohort have review decisions: eight accepted, four probable, one
conflicting, and 17 rejected. None remains unreviewed. This is
research-attempt progress, not completion of the minimum research protocol. No
new employer or affiliation claim was made.

Rebuilt coverage remains **23,978/23,978** linked source rows and **23,939**
active person entities. Research-attempt coverage is **7,899/23,939
(32.9964%)**; confirmed/high verified-employer coverage is **280/23,939
(1.1696%)**; confirmed/high verified-affiliation coverage is **628/23,939
(2.6233%)**; archival-review disposition coverage is **6,357/23,939
(26.5550%)**. There are **16,035** `not_started` people, **489** active
possible-duplicate groups, and **170** active people with conflicting identity
or source status. The database stores **13,099** attempts or plans and
**4,992** claims: **1,311** confirmed, **1,969** high, **1,380** medium,
**187** low, and **145** conflicting. It contains **5,078** source/citation
records and **2,390** unique document keys. The public projection contains
**2,224** affiliations, **708** organizations, **3,871** sources, and **4,801**
claims. The oil-company category remains prominently available at the top of
the site and is a supported, incomplete evidence set of seven people across
nine historically named companies. Full-index historical research is
unfinished.

## Replay and continuation

After importing prior durable batches into private SQLite:

```sh
python3 -m oss_research import-page-reviews research/parser_visual_review_pages501-510_2026-09-22.json
python3 -m oss_research import-review-decisions research/loc_review_decisions_2026-09-22_batch643.csv
python3 -m oss_research import-review-decisions research/identity_review_decisions_2026-09-22_batch643.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page313-mcnamara-mcnutt-review_batch-643_2026-09-22.json
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
