# Batch 615: PDF pages 221–230 and bounded research

Original NARA PDF pages **221–230** were rendered at 180 dpi. All **460**
printed rows were compared against the immutable SQLite extraction for row
order, indexed spelling, initials, rank, private-identifier column occupancy,
box, notes, and archival location. All ten complete pages match the extraction;
there were no corrections. The replayed visual-review ledger rises to
**193/522 pages**; **329** pages remain for complete-page comparison.

Sixteen possible-duplicate or spelling-variant groups covering 34 people were
reviewed without merging a source row or person entity. Exact-name rows with
different private identifiers, rows with a private identifier present in only
one entry, common names with different initials, and one-letter spelling
variants all remain separate. Direct comparison of the indicated personnel
files remains the next action for every group. One previously supported Frank
V Huston identity remains high-confidence while the neighboring Frank U Huston
row is recorded only as a comparison lead.

The bounded, read-only Library of Congress first pass completed **46** searches
for the page-221 queue. It created or revisited **64** discovery candidates,
skipped one completed query fingerprint, and encountered no adapter errors or
blocks. Twenty-two people have candidate leads; 24 had no result from this
source-specific pass. These newspaper-page leads are not accepted identity
matches, employer claims, or completed multi-source protocols. No authenticated
NARA Catalog request was made.

[Alex Inkeles](https://therealjameswilson.github.io/before-oss/people/2a63f636-b442-5b0e-9b45-5c8c53d8b670/)
now has a high-confidence identity based on the distinctive exact indexed name,
official Cornell records, and a Harvard University Press history of the OSS
Research and Analysis Branch. Cornell's Board of Trustees minutes record his
paid appointment as an assistant in Sociology and Anthropology during 1941–42
and his resignation effective March 1, 1942. Barry Katz places Inkeles in the
U.S. Army Signal Corps at Shenango, Pennsylvania, immediately before OSS
recruitment. The public profile therefore distinguishes the Signal Corps as his
immediate pre-OSS military affiliation from Cornell as his last documented
civilian employer. No military rank is inferred; Box 363 remains necessary for
the exact Army and OSS chronology.

At this checkpoint, **23,978/23,978** printed rows link to **23,940** active
person entities. Research-attempt coverage is **7,101/23,940 (29.6617%)**;
confirmed/high verified-employer coverage is **277/23,940 (1.1571%)**;
confirmed/high verified-affiliation coverage is **625/23,940 (2.6107%)**;
archival-review disposition coverage is **6,028/23,940 (25.1796%)**. There are
**16,839** `not_started` people, **395** active possible-duplicate groups, and
**131** active people with conflicting identity or source status. The DB stores
**12,156** attempts or plans and **4,889** claims: **1,311** confirmed,
**1,888** high, **1,373** medium, **185** low, and **132** conflicting. It
contains **5,035** source/citation records and **2,362** unique document keys.
The public projection has **2,218** affiliations, **703** organizations,
**3,832** sources, and **4,700** claims. The top oil-company workers category
remains evidence-scoped to **seven** people across nine companies. Full-index
historical research is unfinished.

## Replay and continuation

After importing the prior durable batches into private SQLite:

```sh
python3 -m oss_research import-page-reviews research/parser_visual_review_pages221-230_2026-09-21.json
python3 -m oss_research import-reviewed-evidence research/evidence-pages221-230-duplicate-review_batch-615_2026-09-21.json
python3 -m oss_research import-reviewed-evidence research/evidence-alex-inkeles-cornell-signal-corps_batch-615_2026-09-21.json
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
python3 -m oss_research export-derived
python3 -m oss_research build-public-data
python3 -m oss_research coverage-report
```

The page-221 through page-230 queues are assigned durably in private SQLite.
Continue bounded discovery with the remaining assigned page batches. No API
key, full service number, raw API response, or private reviewer note is
committed or included in the public site.

## Local release validation

The isolated tracked-only Astro build reports zero errors, warnings, or hints
across **246** source files and produces **24,677** static HTML pages / **24,749**
total artifacts. The bounded Playwright release suite passes **81/81** checks
across desktop, phone, and tablet, including **30** accessibility checks with
no serious or critical axe violations. All **126** Python unit tests pass.
Every internal link resolves, and the deterministic 200-profile stratified
structural audit passes all seven checks; it is not the required independent
manual historical audit of 200 profiles. The private-identifier scanner compares
12,926 normalized identifiers and 120 formatted variants against every built
artifact with zero unexpected full-number boundary matches. The local manifest
verifier matches **67 assets / 97,806,543 bytes** at SHA-256
`ba1839fe7c086daa927371941ec2163ad8ec003bb11c9d720eaa82508b2c3aed`.
Two consecutive clean builds reproduce the **24,749-file** production-tree
digest `4c67df1037fe1f6f5c54d7eee8831e48f76392db5d3f86464bfa3786a47a5bcf`.
