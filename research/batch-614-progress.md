# Batch 614: PDF pages 211–220 and bounded research

Original NARA PDF pages **211–220** were rendered at 180 dpi. All **460**
printed rows were compared against the immutable SQLite extraction for row
order, indexed spelling, initials, rank, private-identifier column occupancy,
box, notes, and archival location. All ten complete pages match the extraction;
there were no corrections. Because pages 215 and 220 already had complete-page
visual decisions, the replayed ledger rises by eight to **183/522 pages**;
**339** pages remain for complete-page comparison.

Twenty-six possible-duplicate or spelling-variant groups covering 52 people
were reviewed without merging a source row or person entity. Twenty-five are
newly grouped. The preexisting Albert J Hoffarth/Hoffman group received a safe
descriptive slug in place of one derived from a private identifier. Same-
identifier, different-identifier, present/absent-identifier, and no-identifier
pairs all remain separate. Direct comparison of the indicated personnel files
remains the next action for every group.

The bounded, read-only Library of Congress first pass completed **46** searches
for the page-149 queue. It created or revisited **34** discovery candidates,
skipped two completed query fingerprints, and encountered no adapter errors or
blocks. These newspaper-page leads are not accepted identity matches, employer
claims, or completed multi-source protocols. No authenticated NARA Catalog
request was made.

[William V. Holohan](https://therealjameswilson.github.io/before-oss/people/d9962ab3-e93e-5613-9f03-7021a0f31b28/)
now has a high-confidence identity based on the exact indexed name and Major
rank plus independent official NARA and Defense Department records of his OSS
service in Italy. A 1951 Defense Department memorandum preserved by the CIA
Reading Room identifies Holohan as a former Securities and Exchange Commission
attorney; the SEC's own 1945 annual report independently lists him among
Commission employees in the armed services. The SEC is therefore published as
his last documented civilian employer before wartime service, not as the
immediate pre-OSS affiliation. Box 344 remains necessary to document the Army
Reserve activation, active-duty sequence, and exact OSS assignment chronology.

At this checkpoint, **23,978/23,978** printed rows link to **23,940** active
person entities. Research-attempt coverage is **7,055/23,940 (29.4695%)**;
confirmed/high verified-employer coverage is **276/23,940 (1.1529%)**;
confirmed/high verified-affiliation coverage is **624/23,940 (2.6065%)**;
archival-review disposition coverage is **5,994/23,940 (25.0376%)**. There are
**16,885** `not_started` people, **379** active possible-duplicate groups, and
**131** active people with conflicting identity or source status. The DB stores
**12,109** attempts or plans and **4,886** claims: **1,311** confirmed,
**1,885** high, **1,373** medium, **185** low, and **132** conflicting. It
contains **5,032** source/citation records and **2,359** unique document keys.
The public projection has **2,216** affiliations, **701** organizations,
**3,829** sources, and **4,697** claims. The top oil-company workers category
remains evidence-scoped to **seven** people across nine companies. Full-index
historical research is unfinished.

## Replay and continuation

After importing the prior durable batches into private SQLite:

```sh
python3 -m oss_research import-page-reviews research/parser_visual_review_pages211-220_2026-09-21.json
python3 -m oss_research import-reviewed-evidence research/evidence-pages211-220-duplicate-review_batch-614_2026-09-21.json
python3 -m oss_research import-reviewed-evidence research/evidence-william-v-holohan_batch-614_2026-09-21.json
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
python3 -m oss_research export-derived
python3 -m oss_research build-public-data
python3 -m oss_research coverage-report
```

The page-211 through page-220 queues are assigned durably in private SQLite.
Continue the bounded discovery queue with the next assigned page batch. No API
key, full service number, raw API response, or private reviewer note is
committed or included in the public site.

## Local release validation

The tracked-only Astro build reports zero errors, warnings, or hints across
245 source files and produces 24,675 static HTML pages / 24,747 total
artifacts. The bounded Playwright release suite passes 81/81 checks across
desktop, phone, and tablet, including 30 accessibility checks with no serious
or critical axe violations. All internal links resolve. The private-identifier
audit reports zero unexpected full-number boundary matches. The local manifest
verifier matches 67 assets / 97,743,773 bytes at SHA-256
`d1c0101f509748d9332b38394947d631eb37621aadbab4b8374d5b1f3948816d`.
Two consecutive clean builds reproduce the 24,747-file production-tree digest
`c8aa4e20b30dd4aed81238f5506b6be6ece97a65f2ff5f7d5309d0873932bd43`.
