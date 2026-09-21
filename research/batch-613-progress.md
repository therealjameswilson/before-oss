# Batch 613: PDF pages 201–210 and bounded research

Original NARA PDF pages **201–210** were rendered at 180 dpi. All **460**
printed rows were compared against the immutable SQLite extraction for row
order, indexed spelling, initials, rank, private-identifier column occupancy,
box, notes, and archival location. All ten complete pages match the extraction;
there were no corrections. Because page 207 already had a complete-page visual
decision, the replayed ledger rises by nine to **175/522 pages**; **347** pages
remain for complete-page comparison.

Twenty-two possible-duplicate or spelling-variant groups covering 44 people
were reviewed without merging a source row or person entity. Twenty are newly
grouped; two preexisting groups received safe descriptive slugs and explicit
evidence in place of values derived from private identifiers. Same-identifier
pairs remain separate, different-identifier pairs remain separate, and common
names or omitted initials do not transfer biographical facts. Direct comparison
of the indicated personnel files remains the next action for every group.

The bounded, read-only Library of Congress first pass completed **45** searches
for the page-148 queue. It created or revisited **21** discovery candidates for
eight people; 37 people had no-result attempts. There were no adapter errors,
blocks, or duplicate skips. These newspaper-page leads are not accepted
identity matches, employer claims, or completed multi-source protocols. No
authenticated NARA Catalog request was made.

[Charles J. Hitch](https://therealjameswilson.github.io/before-oss/people/077388e6-27b2-502b-b1c1-8509e3bcbb03/)
now has a high-confidence identity based on the exact indexed name and officer
context plus an authoritative University of California Academic Senate
memorial. The profile separates three relationships: the U.S. Army was the
explicit immediate affiliation before his 1943 OSS assignment; the U.S. War
Production Board was an intervening government assignment; and Oxford
University, where he was a don and Fellow of Queen's College, was the last
documented civilian employer before those wartime assignments. Box 337 remains
necessary to document the precise OSS assignment, commission chronology, and
the index's `also AS` note.

At this checkpoint, **23,978/23,978** printed rows link to **23,940** active
person entities. Research-attempt coverage is **7,009/23,940 (29.2774%)**;
confirmed/high verified-employer coverage is **275/23,940 (1.1487%)**;
confirmed/high verified-affiliation coverage is **623/23,940 (2.6023%)**;
archival-review disposition coverage is **5,941/23,940 (24.8162%)**. There are
**16,931** `not_started` people, **354** active possible-duplicate groups, and
**131** active people with conflicting identity or source status. The DB stores
**12,062** attempts or plans and **4,884** claims: **1,311** confirmed,
**1,883** high, **1,373** medium, **185** low, and **132** conflicting. It
contains **5,028** source/citation records and **2,355** unique document keys.
The public projection has **2,215** affiliations, **700** organizations,
**3,825** sources, and **4,695** claims. The top oil-company workers category
remains evidence-scoped to **seven** people. Full-index historical research is
unfinished.

Local QA passed **126** Python unit tests, the **200-profile structural** audit,
and **81/81** bounded desktop, phone, tablet, analysis, and accessibility checks,
including 12 focused checks for Hitch, the separate Hoshide/Hoshicle and
Hipp/Pipp records, and the seven-person oil category. All internal links
resolved across **24,699** locally built HTML files. The public-number scan
covered **24,771** artifacts with zero unexpected matches. An unrelated
untracked duplicate Sources route adds 25 local-only pages and is excluded from
the clean release. The structural sample is **not** the required 200-profile
manual historical source audit. Clean-build determinism, CI, and public
deployment checks are reported separately.
An isolated tracked-only build produced **24,674** pages from **244** source
files. All internal links resolved; the public-identifier scan covered
**24,746** artifacts with zero unexpected matches; and two consecutive builds
had the same SHA-256 tree digest
`4307133fca8068d114207cd7f80da367f6021c38defbb056e72e7a6b68fc3981`.

## Replay and continuation

After importing the prior durable batches into private SQLite:

```sh
python3 -m oss_research import-page-reviews research/parser_visual_review_pages201-210_2026-09-21.json
python3 -m oss_research import-reviewed-evidence research/evidence-pages201-210-duplicate-review_batch-613_2026-09-21.json
python3 -m oss_research import-reviewed-evidence research/evidence-charles-j-hitch_batch-613_2026-09-21.json
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
python3 -m oss_research export-derived
python3 -m oss_research build-public-data
python3 -m oss_research coverage-report
```

The page-201 through page-210 queues are assigned durably in private SQLite.
Continue the bounded discovery queue with the next assigned page batch. No API
key, full service number, raw API response, or private reviewer note is
committed or included in the public site.
