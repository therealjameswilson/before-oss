# Batch 652: pages 75-84 extraction audit and Merrick-Meslin research

All **470** printed rows on original NARA PDF pages 75-84 were compared with
the immutable extraction at 180 dpi. Page 77 was already in the visual-review
set; the other nine pages and **414** rows received their first complete visual
comparison in this batch. Every row matches. Complete-page visual review now
covers **500/522 pages** and **22,966/23,978 rows**: **22,934** reviewed rows
match the extraction, **32** retain reviewed corrections, and **1,012** remain
unaudited. Every PDF page remains represented, every parser warning is
resolved, and SQLite integrity and foreign-key checks pass.

The page-317 `Ray D. Merrick` through `Jerome Meslin` queue contains **22
source rows and 22 cautious person entities**. Each person received saved NARA,
CIA Reading Room, Library of Congress, and targeted-web source work plus a
reviewed research outcome. NARA, CIA, and web adapters were dry-run plans; the
LoC adapter ran 22 bounded live queries. It produced **seven** candidates. All
seven were rejected after page-context review because they concerned different
people, a club or place named Merrick or Merrill, or a postwar OCR false
positive. No authenticated NARA Catalog request was made and no API key was
stored or logged.

The principal findings preserve identity and chronology limits:

- **Frank C. Mesle** is identified with high confidence as Frank Carl Mesle
  Jr. A contemporary University of Iowa commencement list corroborates the
  uncommon name, Sherrill hometown, and 1937 Bachelor of Arts degree. A later
  family obituary supplies the explicit OSS bridge and says that he worked as
  a professional Scout in Camden from graduation until entering military
  service in 1941. Because it does not name a local council, the site publishes
  the Boy Scouts of America normalization only as a qualified, medium-confidence
  last civilian employer. It separately models the Corps of Engineers as the
  best-supported military predecessor to OSS training, also qualified because
  the exact transfer sequence is not stated. The University of Iowa is
  correctly recorded as student status, never as an employer.
- **Ray D. Merrick, Morehouse N. Merrifield, John Merrin, Malcolm Merritt, Saul
  Meschenberg, John J. Meshna, and Jerome Meslin** have high-confidence official
  Army identity bridges from exact or compatible names and nonshared protected
  identifiers. Army codes are not treated as employers.
- **Lawrencee N. Merritt** remains conflicting because the protected identifier
  points to official Army Noel L. Merritt.
- **Charles P. Mersereau** and **Charles P. Meserau** remain separate and
  conflicting. Their protected identifier is also printed for C. P. Meysereav;
  the Army spelling agrees with Mersereau, but no records are merged without
  direct file evidence.
- **William L. Merritts** remains conflicting because the same protected
  identifier appears with Marritts, Meritts, and Merritts source spellings.
- The index's literal **F Nevill Merritt** first- and middle-name fields remain
  recoverable. Searches in both name orders produced no reliable bridge, so the
  source cells were not silently reordered.

The cohort ends with **17** `in_progress`, four `conflicting_sources`, and one
`documented_prewar_employer_found` status. Identity statuses are eight
`high_confidence`, ten `unresolved`, and four `conflicting`. The reviewed
evidence bundle adds **15** claims: nine high, two medium, and four conflicting.

Rebuilt coverage is **23,978/23,978** linked source rows and **23,939** active
person entities. Research-attempt coverage is **8,097/23,939 (33.8235%)**;
confirmed/high verified-employer coverage is **288/23,939 (1.2031%)**;
confirmed/high verified-affiliation coverage is **643/23,939 (2.6860%)**;
archival-review disposition coverage is **6,553/23,939 (27.3737%)**. There are
**15,837** `not_started` people, **492** possible-duplicate groups, and **189**
active conflicts. SQLite stores **13,895** attempts or plans and **5,135**
claims: 1,311 confirmed, 2,065 high, 1,406 medium, 189 low, and 164 conflicting.
It contains **5,145** citation records and **2,445** unique source documents.
The public projection contains **2,263** affiliations, **740** organizations,
**3,935** sources, and **4,942** claims.

The oil-company category remains prominently available at the top of the
personnel directory and on its dedicated page. It remains an evidence-scoped
set of **seven people across nine historically named companies**. None of the
Batch 652 findings is an oil-company employment claim. Full-index historical
research is unfinished.

## Replay and continuation

After importing prior durable batches into private SQLite:

```sh
python3 -m oss_research import-page-reviews research/parser_visual_review_pages75-84_2026-09-23.json
python3 -m oss_research import-review-decisions research/identity_review_decisions_2026-09-23_batch652.csv
python3 -m oss_research import-review-decisions research/loc_review_decisions_2026-09-23_batch652.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page317-merrick-meslin-review_batch-652_2026-09-23.json
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
```

Continue with the next bounded research and extraction-audit batch, then run:

```sh
python3 -m oss_research export-adapter-checkpoints
python3 -m oss_research export-derived
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
```

No API key, full service number, raw Catalog API response, copyrighted page
image, or private reviewer note is committed or included in the public site.
