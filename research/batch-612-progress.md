# Batch 612: PDF pages 191–200 and bounded research

Original NARA PDF pages **191–200** were rendered at 180 dpi. All **460**
printed rows were compared against the immutable SQLite extraction for row
order, indexed spelling, initials, rank, private-identifier column occupancy,
box, notes, and archival location. All ten complete pages match the extraction;
there were no corrections. The replayed visual-review ledger is now **166/522
pages**; **356** pages remain for complete-page comparison.

Fifteen possible-duplicate or spelling-variant groups covering 31 people were
reviewed without merging any source row or person entity. They include
Hammond/Hammand, Hammet initial variants, duplicate Palmer Hansen, Hardin and
Harding variants, duplicate Edward Harding, Harjes, Harlow, John O/Otto Harris,
duplicate James Hart, Haselfeld/Haselfield, Haymaker, Hazalwood/Hazelwood,
Hazard/Hazzard, and Healey/Healy. Three Simon/Stephen Harrington records are
explicitly conflicting because two identical names carry different private
identifiers while one identifier also appears under a different first name.
The public profiles describe the collision without exposing those values. All
31 people remain separate pending direct file evidence.

The bounded, read-only Library of Congress first pass completed **46** searches
for the page-147 queue. It created or revisited **88** discovery candidates,
with **23** people having candidate-bearing attempts and **23** having no-result
attempts. There were no adapter errors, blocks, or duplicate skips. These
newspaper-page leads are not accepted identity matches, employer claims, or
completed multi-source protocols. No authenticated NARA Catalog request was
made.

[Knut Haugland](https://therealjameswilson.github.io/before-oss/people/8a1378f4-e6f0-530d-a153-2581acc176be/)
now has a high-confidence identity as Norwegian officer and radio specialist
Knut Magne Haugland. The reviewed Store norske leksikon biography and Kon-Tiki
Museum archive description support Høvding Radiofabrikk in Oslo as his last
documented civilian employer after 1940 demobilization and before his 1941
transition into clandestine Allied service. The evidence is strongly
date-bounded but does not say the factory was his immediate pre-OSS affiliation,
and neither reviewed account establishes a direct OSS assignment. The public
profile preserves that uncertainty and identifies Box 319 as the next action.
His personnel category is corrected to foreign or Allied military personnel;
he remains a commissioned officer and Allied or foreign person in the filters.

At this checkpoint, **23,978/23,978** printed rows link to **23,940** active
person entities. Research-attempt coverage is **6,963/23,940 (29.0852%)**;
confirmed/high verified-employer coverage is **274/23,940 (1.1445%)**;
confirmed/high verified-affiliation coverage is **622/23,940 (2.5982%)**;
archival-review disposition coverage is **5,896/23,940 (24.6282%)**. There are
**16,977** `not_started` people, **334** active possible-duplicate groups, and
**131** active people with conflicting identity or source status. The DB stores
**12,016** attempts or plans and **4,880** claims: **1,311** confirmed,
**1,879** high, **1,373** medium, **185** low, and **132** conflicting. It
contains **5,026** source/citation records and **2,353** unique document keys.
The public projection has **2,212** affiliations, **697** organizations,
**3,823** sources, and **4,691** claims. The top oil-company workers category
remains evidence-scoped to **seven** people. Full-index historical research is
unfinished.

Local QA passed **126** Python unit tests, the **200-profile structural** audit,
and **81/81** bounded desktop, phone, tablet, analysis, and accessibility checks,
including 12 focused checks for Haugland, the separate Haselfeld/Haselfield and
Harrington records, and the seven-person oil category. All internal links
resolved across **24,696** locally built HTML files. The public-number scan
covered **24,768** artifacts with zero unexpected matches. An unrelated
untracked duplicate Sources route adds 25 local-only pages and is excluded from
the clean release. The structural sample is **not** the required 200-profile
manual historical source audit. Clean-build determinism, CI, and public
deployment checks are reported separately.
An isolated tracked-only build produced **24,671** pages from **243** source
files. All internal links resolved; the public-identifier scan covered
**24,743** artifacts with zero unexpected matches; and two consecutive builds
had the same SHA-256 tree digest
`a524c8f6e3510181ef958df5d976438c92ae00f4d999b7adde271c49dae9dad5`.

## Replay and continuation

After importing the prior durable batches into private SQLite:

```sh
python3 -m oss_research import-page-reviews research/parser_visual_review_pages191-200_2026-09-21.json
python3 -m oss_research import-reviewed-evidence research/evidence-pages191-200-duplicate-review_batch-612_2026-09-21.json
python3 -m oss_research import-reviewed-evidence research/evidence-knut-haugland_batch-612_2026-09-21.json
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
python3 -m oss_research export-derived
python3 -m oss_research build-public-data
python3 -m oss_research coverage-report
```

The page-191 through page-200 queues are assigned durably in private SQLite.
Continue the bounded discovery queue with the next assigned page batch. No API
key, full service number, raw API response, or private reviewer note is
committed or included in the public site.
