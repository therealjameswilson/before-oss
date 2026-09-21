# Batch 625: PDF pages 321-330 and Mayer research

Original NARA PDF pages **321-330** were rendered at 180 dpi. All **460**
printed rows were compared against the immutable SQLite extraction for row
order, indexed spelling, initials, rank, private-identifier column occupancy,
box, notes, and archival location. All ten pages match the current extraction.
Pages 326 and 330 already had complete visual review, so this replay adds eight
pages and **368** rows to the complete-page ledger. Visual review now covers
**271/522 pages** and **12,432/23,978 rows**: **12,400** reviewed rows match the
extraction, **32** retain reviewed corrections, and **11,546** remain for
complete visual comparison.

The audit preserves literal source anomalies rather than silently correcting
them. Examples include `Cpt`, `Y 1/c`, `G.E.`, `British ar`, `Eugeneis`,
`AOM3 C`, `LtCol`, `Andrew, II`, `Mitschke` with rank `AS`, `Mittendore`,
`Miyadira Kazyu`, `Mockler-Ferrt`, `P-D`, `Siguardo`, `Mogene`, `Monlvx`,
`Avary`, `Refer to`, `Margeret`, `CIV`, `file is ch`, `docume`, `C SP-P`,
`Moravansky`, `Raymound`, `Moreli`, `review th`, `T/J`, `Morguest`,
`Mauriyio`, lowercase `t-3`, `H. Jr.`, Czech and French notes, clipped text,
and visibly repeated or variant rows. Private identifiers are never included
in this note or public assets.

The next unsearched page-302 queue contained **10** people. Its Library of
Congress pass completed **10** live exact-name searches, creating **12**
discovery candidates with zero adapter errors or blocked requests. Every
candidate was inspected in official item-level OCR context. Eleven had no
matching exact-name context in the complete OCR. The remaining item was a
1906 classified advertisement for Hofmayer's Bureau rather than Rene A.
Mayer. All 12 candidates were rejected as context-free hits, postwar or
temporally remote material, or an unrelated OCR substring. No employer claim
was added and no raw Library of Congress response was retained.

One pre-existing official Army bulk candidate was accepted as an identity-only
crosswalk. Lawrence J. Mayer agrees with the index in full name and a
nonshared protected identifier, so the identity is now `high_confidence`.
The Army grade and occupation code were not translated into an employer,
occupation, or immediate affiliation. All ten people remain `in_progress`
with saved next actions; this is research-attempt progress, not completion of
the minimum research protocol.

At this checkpoint, **23,978/23,978** printed rows link to **23,939** active
person entities. Research-attempt coverage is **7,488/23,939 (31.2795%)**;
confirmed/high verified-employer coverage is **280/23,939 (1.1696%)**;
confirmed/high verified-affiliation coverage is **628/23,939 (2.6233%)**;
archival-review disposition coverage is **6,298/23,939 (26.3085%)**. There are
**16,415** `not_started` people, **488** active possible-duplicate groups, and
**157** active people with conflicting identity or source status. The database
stores **12,546** attempts or plans and **4,900** claims: **1,311** confirmed,
**1,898** high, **1,374** medium, **185** low, and **132** conflicting. It
contains **5,045** source/citation records and **2,372** unique document keys.
The public projection remains **2,224** affiliations, **708** organizations,
**3,842** sources, and **4,711** claims. The oil-company category remains a
supported, incomplete evidence set of **seven** people across nine companies.
Full-index historical research is unfinished.

## Replay and continuation

After importing prior durable batches into private SQLite:

```sh
python3 -m oss_research import-page-reviews research/parser_visual_review_pages321-330_2026-09-21.json
python3 -m oss_research import-review-decisions research/loc_review_decisions_2026-09-21_batch625.csv
python3 -m oss_research import-review-decisions research/army_review_decisions_2026-09-21_batch625.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page302-mayer-identity-review_batch-625_2026-09-21.json
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
```

Continue with the next unsearched queue, then rebuild derived outputs:

```sh
python3 -m oss_research research --source loc --batch page-302-mayes-mazzarini-b623 --max-queries 10 --resume
python3 -m oss_research export-adapter-checkpoints
python3 -m oss_research export-derived
python3 -m oss_research build-public-data
python3 -m oss_research coverage-report
```

No API key, full service number, raw API response, or private reviewer note is
committed or included in the public site.
