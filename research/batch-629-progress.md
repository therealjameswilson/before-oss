# Batch 629: PDF pages 361-370 and completion of the McCann-McCarthy queue

Original NARA PDF pages **361-370** were rendered at 180 dpi. All **460**
printed rows were compared against the immutable SQLite extraction for row
order, indexed spelling, initials, rank, private-identifier column occupancy,
box, notes, and archival location. All ten pages match the current extraction.
This adds ten pages and **460** rows to the complete-page ledger. Visual review
now covers **305/522 pages** and **13,996/23,978 rows**: **13,964** reviewed
rows match the extraction, **32** retain reviewed corrections, and **9,982**
remain for complete visual comparison.

The complete page-304 `Thomas A. McCann` through `John A. McCarthy` queue
contains **23** people. Its Library of Congress pass completed **23** live
exact-name searches and created **36** discovery candidates. Every candidate
was inspected through official item-level OCR context and rejected. The
rejections preserve the specific reason: conflicting given names or initials,
postwar namesakes, surname-only or OCR-adjacent fragments, or a common exact
name without a corroborating identifier and pre-OSS employment evidence. No
employer claim was added and no raw Library of Congress response was retained.

Official Army bulk candidates were reviewed separately. Seven people - Donald
K. McCarthy, Elder McCarter, Emmett J. McCarthy, Francis P. McCarthy, Harry L.
McCarthy, John A. McCarthy, and the staff-sergeant John F. McCarthy row - now
have `high_confidence` identity crosswalks because the indexed full or
normalized name agrees with a nonshared protected identifier. The adjacent
second John F. McCarthy row remains a separate ambiguous person because the
index prints a different identifier.

The index prints Jack L. McCarary on page 304 and Jack L. McCrary on page 306
with the same protected identifier, middle initial, and Box 501. The Army
fixed-width name supports the McCrary spelling. Both profiles and both source
rows remain separate, however, and the pair is recorded only as a probable
duplicate pending examination of the original Box 501 jackets. Army grade and
occupation codes were not treated as employers or immediate pre-OSS
affiliations.

The final queue state is **19** `in_progress` and **4**
`needs_identity_review`. Its identity state is **7** `high_confidence`, **4**
`ambiguous`, and **12** `unresolved`. All 23 people have a saved Library of
Congress attempt and every one of the 36 source candidates has a review
decision. This is research-attempt progress, not completion of the minimum
research protocol.

At this checkpoint, **23,978/23,978** printed rows link to **23,939** active
person entities. Research-attempt coverage is **7,580/23,939 (31.6638%)**;
confirmed/high verified-employer coverage is **280/23,939 (1.1696%)**;
confirmed/high verified-affiliation coverage is **628/23,939 (2.6233%)**;
archival-review disposition coverage is **6,298/23,939 (26.3085%)**. There are
**16,331** `not_started` people, **488** active possible-duplicate groups, and
**158** active people with conflicting identity or source status. The database
stores **12,638** attempts or plans and **4,900** claims: **1,311** confirmed,
**1,898** high, **1,374** medium, **185** low, and **132** conflicting. It
contains **5,045** source/citation records and **2,372** unique document keys.
The public projection remains **2,224** affiliations, **708** organizations,
**3,842** sources, and **4,711** claims. The oil-company category remains a
supported, incomplete evidence set of **seven** people across nine companies.
Full-index historical research is unfinished.

## Replay and continuation

After importing prior durable batches into private SQLite:

```sh
python3 -m oss_research import-page-reviews research/parser_visual_review_pages361-370_2026-09-22.json
python3 -m oss_research import-review-decisions research/loc_review_decisions_2026-09-22_batch629.csv
python3 -m oss_research import-review-decisions research/loc_review_decisions_2026-09-22_batch629b.csv
python3 -m oss_research import-review-decisions research/loc_review_decisions_2026-09-22_batch629c.csv
python3 -m oss_research import-review-decisions research/army_review_decisions_2026-09-22_batch629.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page304-mccann-mccarthy-identity-review_batch-629_2026-09-22.json
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
```

Continue with the second assigned page-304 queue, then rebuild derived outputs:

```sh
python3 -m oss_research research --source loc --batch page-304-mccarthy-joseph-mcclelian-b623 --max-queries 10 --resume
python3 -m oss_research export-adapter-checkpoints
python3 -m oss_research export-derived
python3 -m oss_research build-public-data
python3 -m oss_research coverage-report
```

No API key, full service number, raw API response, or private reviewer note is
committed or included in the public site.
