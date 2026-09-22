# Batch 627: PDF pages 341-350 and completion of the Mazzone-McBride queue

Original NARA PDF pages **341-350** were rendered at 180 dpi. All **460**
printed rows were compared against the immutable SQLite extraction for row
order, indexed spelling, initials, rank, private-identifier column occupancy,
box, notes, and archival location. All ten pages match the current extraction.
Pages 345 and 349 already had complete visual review, so this replay adds eight
pages and **368** rows to the complete-page ledger. Visual review now covers
**286/522 pages** and **13,122/23,978 rows**: **13,090** reviewed rows match
the extraction, **32** retain reviewed corrections, and **10,856** remain for
complete visual comparison.

The audit preserves literal anomalies rather than silently correcting them.
Examples include `Ilhan`, `Nichnowiitz`, the distinct `Nickolodoulos` and
`Nicolopoulos` spellings, `Capt-`, `Nikrodananda`, `Nimomiya`, `Yincenzo`,
`Nohowel`, `Noia`, `Nolino`, `Norborg`, `Noris`, `Brunnon`, `Norsic`,
`Notides`, `Nuttal`, `Nygaro`, `Obucina`, `Oconor`, `Odunne`, a lowercase
middle initial, `Oesh`, `Oexner`, `Oflaherty`, `Lairo`, `Ogrean`, `Ohanlon`,
`Ohshita`, `Oistad`, `Ojesdal`, `Ojibway`, `Okeeffee`, `Oldashi`, `Oliveria`,
`Olos`, `OnaHary`, `Onativia`, `Ondreas`, and the distinct `Oneal`, `Oneil`,
and `Oneill` spellings. Clipped notes, rank variants, nonnumeric prefixed
identifiers, duplicated names and identifiers, isolated box anomalies, and
mixed archive locations also remain literal. Private identifiers are not
included in this note or public assets.

The complete page-303 `Mazzone` through `John J. McBride` queue contains
**23** people. Its Library of Congress pass completed **23** live exact-name
searches and created **7** discovery candidates. Every candidate was inspected
through official item-level OCR and the bounded full-text fallback. The
candidates concerned George A. McAdams rather than George F.; George Warren
and George W. McBride rather than George J.; and John P., John S., or John E.
McBride rather than John J. The initials conflict and no independent
identifier supports a match. All seven candidates were rejected. No employer
claim was added and no raw Library of Congress response was retained.

No pre-existing Army bulk candidate was available for this queue. All 23
people remain `in_progress` with saved next actions; this is research-attempt
progress, not completion of the minimum research protocol.

At this checkpoint, **23,978/23,978** printed rows link to **23,939** active
person entities. Research-attempt coverage is **7,534/23,939 (31.4717%)**;
confirmed/high verified-employer coverage is **280/23,939 (1.1696%)**;
confirmed/high verified-affiliation coverage is **628/23,939 (2.6233%)**;
archival-review disposition coverage is **6,298/23,939 (26.3085%)**. There are
**16,370** `not_started` people, **488** active possible-duplicate groups, and
**157** active people with conflicting identity or source status. The database
stores **12,592** attempts or plans and **4,900** claims: **1,311** confirmed,
**1,898** high, **1,374** medium, **185** low, and **132** conflicting. It
contains **5,045** source/citation records and **2,372** unique document keys.
The public projection remains **2,224** affiliations, **708** organizations,
**3,842** sources, and **4,711** claims. The oil-company category remains a
supported, incomplete evidence set of **seven** people across nine companies.
Full-index historical research is unfinished.

## Replay and continuation

After importing prior durable batches into private SQLite:

```sh
python3 -m oss_research import-page-reviews research/parser_visual_review_pages341-350_2026-09-21.json
python3 -m oss_research import-review-decisions research/loc_review_decisions_2026-09-21_batch627.csv
python3 -m oss_research import-review-decisions research/loc_review_decisions_2026-09-21_batch627b.csv
python3 -m oss_research import-review-decisions research/loc_review_decisions_2026-09-21_batch627c.csv
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
```

Continue with the next unsearched queue, then rebuild derived outputs:

```sh
python3 -m oss_research research --source loc --batch page-303-mcbride-william-mccann-richard-b623 --max-queries 10 --resume
python3 -m oss_research export-adapter-checkpoints
python3 -m oss_research export-derived
python3 -m oss_research build-public-data
python3 -m oss_research coverage-report
```

No API key, full service number, raw API response, or private reviewer note is
committed or included in the public site.
