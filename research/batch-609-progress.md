# Batch 609: PDF pages 161–170 and bounded research

Original NARA PDF pages **161–170** were rendered at 180 dpi. All **460**
printed rows were compared against the immutable SQLite extraction for row
order, indexed spelling, initials, rank, private-identifier column occupancy,
box, notes, and archival location. Pages 162 and 170 already had durable
visual-review decisions and retain them; pages 161 and 163–169 add eight
matching-only decisions. There were no new extraction corrections. The
distinct visual-review ledger is now **137/522 pages**; **385** pages remain
for individual comparison.

Nine new possible-duplicate or spelling-variant groups are marked ambiguous
without merging any source rows or person entities. They cover the repeated
Peter G Gavreledes, Joseph A Gengerelli, George Gerbner, and Walker F Givan
names; Eldred D/E Gegenheimer; Gercke/Gerke; Gibbeney/Gibboney;
Gibbon/Gibbons; and Geise/Giese. The George Gerbner, Walker F Givan, and
Geise/Giese pairs each have two different private identifiers, while several
other pairs have an identifier on only one row. Every private value remains
masked publicly and each pair awaits personnel-file comparison.

The bounded, read-only Library of Congress first pass completed **46** searches
for the page-144 queue and created or revisited **14** unreviewed
newspaper-page candidates across five people. The remaining 41 searches had
no result. These are discovery leads, not accepted identity matches, employer
claims, or completed multi-source protocols. No authenticated NARA Catalog
request was made.

[Alexander Gerschenkron](https://therealjameswilson.github.io/before-oss/people/36062bdb-bd0c-5653-8b7e-6b0915258619/)
now has a high-confidence **documented earlier government affiliation**. A
1948 Congressional Record personnel statement dates his Board of Governors of
the Federal Reserve System service to February 29, 1944, and Harvard's archival
finding aid independently identifies his role as European economic analyst.
Neither source establishes his exact OSS entry date or whether the Board
appointment continued, paused, or ended. The public profile therefore keeps
the Board assignment out of the immediate-affiliation and last-civilian-
employer fields; Box 269 review is the next action.

At this checkpoint, **23,978/23,978** printed rows link to **23,940** active
person entities. Research-attempt coverage is **6,823/23,940 (28.5004%)**;
confirmed/high verified-employer coverage is **271/23,940 (1.1320%)**;
confirmed/high verified-affiliation coverage is **619/23,940 (2.5856%)**;
archival-review disposition coverage is **5,828/23,940 (24.3442%)**. There are
**17,117** `not_started` people, **306** possible-duplicate groups, and
**128** active people with conflicting identity or source status. The DB
stores **11,875** attempts or plans and **4,872** claims: **1,311** confirmed,
**1,871** high, **1,373** medium, **185** low, and **132** conflicting. It
contains **5,018** source/citation records and **2,345** unique document keys.
The public projection has **2,208** affiliations, **695** organizations,
**3,815** sources, and **4,683** claims. Full-index historical research is
unfinished.

Local QA passed: **126** Python unit tests; the bounded desktop, phone, and
tablet release checks; the **200-profile structural** audit; the internal-link
check; the public-number redaction scan; and the static Astro build. The
structural sample is **not** the required 200-profile manual historical source
audit. Clean CI and public deployment require separate verification.

## Replay and continuation

After importing the prior durable batches into private SQLite:

```sh
python3 -m oss_research import-page-reviews research/parser_visual_review_pages161_163-169_2026-09-21.json
python3 -m oss_research import-reviewed-evidence research/evidence-pages164-170-duplicate-review_batch-609_2026-09-21.json
python3 -m oss_research import-reviewed-evidence research/evidence-page166-alexander-gerschenkron-pathway_batch-609_2026-09-21.json
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
python3 -m oss_research export-derived
python3 -m oss_research build-public-data
python3 -m oss_research coverage-report
```

The page-161 through page-170 queues are assigned durably in private SQLite;
the two pilot members on pages 168 and 170 retain their original assignment.
Continue with `python3 -m oss_research research --source loc --batch
page-145-feurig-fine-b607 --max-queries 46 --resume`. No API key, full
service number, raw API response, or private reviewer note is committed or
included in the public site.
