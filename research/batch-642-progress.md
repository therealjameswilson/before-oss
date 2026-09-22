# Batch 642: PDF pages 491-500 and McLaughlin-McMahon research

All **460** printed rows on original NARA PDF pages 491-500 were compared
against SQLite at 180 dpi. None of these pages was already in the
complete-page ledger. Every row matches the current extraction and requires
no correction. Visual review now covers **415/522 pages** and
**19,056/23,978 rows**: **19,024** reviewed rows match the extraction, **32**
retain reviewed corrections, and **4,922** remain for complete visual
comparison.

The page-312 `Arthur B. McLaughlin` through `Robert F. McMahon` queue contains
23 source rows representing **22** cautious person entities. The two John J.
McLaughlin rows remain separately preserved but link to one high-confidence
entity because the exact name, protected identifier, box, and archival
location all agree. A live Library of Congress attempt is saved for every
person. The pass created 22 newspaper candidates across six people; every item
context was inspected and rejected because it identifies a different name or
initial, is postwar, or supplies no OSS, rank, protected-identifier, or Box 510
bridge. In particular, exact-name Harvard Law professor references were not
assigned to indexed James A. McLaughlin because a common name alone does not
establish identity.

Six preexisting official Army candidates received review decisions. Exact
normalized names and nonshared protected identifiers support high-confidence
identity crosswalks for James A. McLaughlin, Ellis R. McLuckie, James A.
McLuskey, and Robert F. McMahon. The official `Jr.` suffix for Robert F.
McMahon is preserved as a variant without changing the indexed display name.
The Francis B. McLeod candidate remains probable because its name field carries
unexplained trailing `TRD` text. It requires Box 510 review before evidence is
assigned beyond the qualified identity claim.

One protected-identifier conflict remains visible. The identifier printed for
Gene J. McLaughlin points to an official Army entry for Jean J. McLaughlin.
The first names conflict, so Gene remains `conflicting`, requires critical Box
510 review, and receives no identity or employment inference from that entry.
Full identifiers are excluded from public output. Army grade, entry date, and
occupation codes are identity context, not employer evidence.

The final 22-person queue state is **19** `in_progress`, one
`verified_employer_found`, one `needs_identity_review`, and one
`conflicting_sources`. Donal McLaughlin already had a verified-employer outcome
before this batch. All **28** candidates in the cohort have review decisions:
four accepted, one probable, one conflicting, and 22 rejected. None remains
unreviewed. This is research-attempt progress, not completion of the minimum
research protocol. No new employer or affiliation claim was made.

Rebuilt coverage remains **23,978/23,978** linked source rows and **23,939**
active person entities. Research-attempt coverage is **7,876/23,939
(32.9003%)**; confirmed/high verified-employer coverage is **280/23,939
(1.1696%)**; confirmed/high verified-affiliation coverage is **628/23,939
(2.6233%)**; archival-review disposition coverage is **6,346/23,939
(26.5090%)**. There are **16,058** `not_started` people, **489** active
possible-duplicate groups, and **169** active people with conflicting identity
or source status. The database stores **13,062** attempts or plans and
**4,981** claims: **1,311** confirmed, **1,961** high, **1,378** medium,
**187** low, and **144** conflicting. It contains **5,076** source/citation
records and **2,389** unique document keys. The public projection contains
**2,224** affiliations, **708** organizations, **3,869** sources, and **4,790**
claims. The oil-company category remains a supported, incomplete evidence set
of seven people across nine companies. Full-index historical research is
unfinished.

## Replay and continuation

After importing prior durable batches into private SQLite:

```sh
python3 -m oss_research import-page-reviews research/parser_visual_review_pages491-500_2026-09-22.json
python3 -m oss_research import-review-decisions research/loc_review_decisions_2026-09-22_batch642.csv
python3 -m oss_research import-review-decisions research/identity_review_decisions_2026-09-22_batch642.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page312-mclaughlin-mcmahon-review_batch-642_2026-09-22.json
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
