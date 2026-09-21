# Batch 624: PDF pages 311-320 and May/Mayer research

Original NARA PDF pages **311-320** were rendered at 180 dpi. All **460**
printed rows were compared against the immutable SQLite extraction for row
order, indexed spelling, initials, rank, private-identifier column occupancy,
box, notes, and archival location. All ten pages match the current extraction.
Page 312 already retained a reviewed correction and page 314 already had a
complete deterministic-random review, so this replay adds eight pages and
**368** rows to the complete-page ledger. Visual review now covers **263/522
pages** and **12,064/23,978 rows**: **12,032** reviewed rows match the
extraction, **32** retain reviewed corrections, and **11,914** remain for
complete visual comparison.

The audit preserves literal source anomalies rather than silently correcting
them. Examples include `PVT (Au`, `Sep-39`, `023034/84`, `RA 3994620`,
`RA1404787`, `A700336`, `A402911`, Virgina, Lawerence, Jospeh,
Meeksdelbert?, Melnikoff II, McNearnry / McNerney, McParland / McPharland,
Meader / Meador, Menanga / Menengas, Mersereau / Meserau, Meuller, Meysereav,
Micheals, clipped notes, values visibly displaced between columns, and visibly
repeated or variant rows. Private identifiers are never included in this note
or public assets.

The first unsearched page-302 queue contained **11** people. Its Library of
Congress pass completed **11** live exact-name searches, creating **24**
discovery candidates with zero adapter errors or blocked requests. Every
candidate was inspected in official item-level OCR context. Two initially
failed contexts were retried directly: one was a 1940 opinion letter by an
otherwise unidentified Charles Mayer and the other an 1898 Brooklyn piano
advertisement. All 24 candidates were rejected as context-free hits, distinct
namesakes, unrelated family or entertainment material, postwar items, or
temporally remote occurrences without corroborating identifiers. No employer
claim was added and no raw Library of Congress response was retained.

Two pre-existing official Army bulk candidates were accepted as identity-only
crosswalks. Charles A Mayer and Emil Mayer each agree with the index in full
name and a nonshared protected identifier, so both identities are now
`high_confidence`. Army grades and occupation codes were not translated into
an employer, occupation, or immediate affiliation. All 11 people remain
`in_progress` with a saved next action; this is research-attempt progress, not
completion of the minimum research protocol.

At this checkpoint, **23,978/23,978** printed rows link to **23,939** active
person entities. Research-attempt coverage is **7,478/23,939 (31.2377%)**;
confirmed/high verified-employer coverage is **280/23,939 (1.1696%)**;
confirmed/high verified-affiliation coverage is **628/23,939 (2.6233%)**;
archival-review disposition coverage is **6,298/23,939 (26.3085%)**. There are
**16,425** `not_started` people, **488** active possible-duplicate groups, and
**157** active people with conflicting identity or source status. The database
stores **12,536** attempts or plans and **4,900** claims: **1,311** confirmed,
**1,898** high, **1,374** medium, **185** low, and **132** conflicting. It
contains **5,045** source/citation records and **2,372** unique document keys.
The public projection remains **2,224** affiliations, **708** organizations,
**3,842** sources, and **4,711** claims. The oil-company category remains a
supported, incomplete evidence set of **seven** people across nine companies.
Full-index historical research is unfinished.

## Replay and continuation

After importing prior durable batches into private SQLite:

```sh
python3 -m oss_research import-page-reviews research/parser_visual_review_pages311-320_2026-09-21.json
python3 -m oss_research import-review-decisions research/loc_review_decisions_2026-09-21_batch624.csv
python3 -m oss_research import-review-decisions research/army_review_decisions_2026-09-21_batch624.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page302-may-mayer-identity-review_batch-624_2026-09-21.json
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
```

Continue with the next unsearched queue, then rebuild derived outputs:

```sh
python3 -m oss_research research --source loc --batch page-302-mayer-gerald-mayersaks-b623 --max-queries 10 --resume
python3 -m oss_research export-adapter-checkpoints
python3 -m oss_research export-derived
python3 -m oss_research build-public-data
python3 -m oss_research coverage-report
```

No API key, full service number, raw API response, or private reviewer note is
committed or included in the public site.
