# Batch 616: PDF pages 231–240 and bounded research

Original NARA PDF pages **231–240** were rendered at 180 dpi. All **460**
printed rows were compared against the immutable SQLite extraction for row
order, indexed spelling, initials, rank, private-identifier column occupancy,
box, notes, and archival location. All ten complete pages match the extraction;
there were no corrections. The replayed visual-review ledger rises to
**203/522 pages**; **319** pages remain for complete-page comparison.

Sixteen possible-duplicate or spelling-variant groups covering 32 people were
reviewed without merging a source row or person entity. Exact-name rows with
different private identifiers, rows with a private identifier present in only
one entry, familiar-name variants, and one-letter spelling variants all remain
separate. Direct comparison of the indicated personnel files remains the next
action for every group. A separate Robert H Johnson pair on page 234 was
already linked to one entity by the existing identity build because the two
preserved source rows share the same exact name, box, and private identifier;
Batch 616 did not perform a new merge.

The bounded, read-only Library of Congress first pass completed **45** searches
for the two page-231 queues. It created or revisited **22** discovery
candidates, skipped two completed query fingerprints, and encountered no
adapter errors or blocks. These newspaper-page leads are not accepted identity
matches, employer claims, or completed multi-source protocols. No authenticated
NARA Catalog request was made.

[Garson Kanin](https://therealjameswilson.github.io/before-oss/people/03835a06-93bb-5db7-846a-aec5e47b58df/)
now has a high-confidence identity based on the distinctive exact indexed name,
the Library of Congress finding aid for his papers, the AFI Catalog, and the
Garson Kanin Estate chronology. The public profile distinguishes the U.S. Army
Signal Corps film unit as his immediate documented pre-OSS military assignment
from RKO Radio Pictures as his last documented civilian employer. The RKO claim
is high-confidence; the immediate Signal Corps claim is visibly qualified at
medium confidence pending review of Box 389 for the exact transfer and
commissioning chronology.

At this checkpoint, **23,978/23,978** printed rows link to **23,940** active
person entities. Research-attempt coverage is **7,147/23,940 (29.8538%)**;
confirmed/high verified-employer coverage is **278/23,940 (1.1612%)**;
confirmed/high verified-affiliation coverage is **626/23,940 (2.6149%)**;
archival-review disposition coverage is **6,061/23,940 (25.3175%)**. There are
**16,793** `not_started` people, **411** active possible-duplicate groups, and
**131** active people with conflicting identity or source status. The DB stores
**12,202** attempts or plans and **4,892** claims: **1,311** confirmed,
**1,890** high, **1,374** medium, **185** low, and **132** conflicting. It
contains **5,039** source/citation records and **2,366** unique document keys.
The public projection has **2,220** affiliations, **705** organizations,
**3,836** sources, and **4,703** claims. The top oil-company workers category
remains evidence-scoped to **seven** people across nine companies. Full-index
historical research is unfinished.

## Replay and continuation

After importing the prior durable batches into private SQLite:

```sh
python3 -m oss_research import-page-reviews research/parser_visual_review_pages231-240_2026-09-21.json
python3 -m oss_research import-reviewed-evidence research/evidence-pages231-240-duplicate-review_batch-616_2026-09-21.json
python3 -m oss_research import-reviewed-evidence research/evidence-garson-kanin-rko-signal-corps_batch-616_2026-09-21.json
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
python3 -m oss_research export-derived
python3 -m oss_research build-public-data
python3 -m oss_research coverage-report
```

The page-231 through page-240 queues are assigned durably in private SQLite.
Continue bounded discovery with the remaining assigned page batches. No API
key, full service number, raw API response, or private reviewer note is
committed or included in the public site.

## Local release validation

The isolated tracked-only Astro build reports zero errors, warnings, or hints
across **247** source files and produces **24,679** static HTML pages / **24,751**
total artifacts. The bounded Playwright release suite passes **81/81** checks
across desktop, phone, and tablet, including **30** accessibility checks with
no serious or critical axe violations. All **126** Python unit tests pass.
Every internal link resolves, and the deterministic 200-profile stratified
structural audit passes all seven checks; it is not the required independent
manual historical audit of 200 profiles. The private-identifier scanner
compares 12,926 normalized identifiers and 120 formatted variants against every
built artifact with zero unexpected full-number boundary matches. The local
manifest verifier matches **67 assets / 97,869,420 bytes** at SHA-256
`a616541f0e3670a8076eaccb978b50d2fb859e7c508708ddeec6da1452ce449c`.
Two consecutive clean builds reproduce the **24,751-file** production-tree
digest `60d4916b9aa1ac1155d5f34bf77bfc3914f51631915ac8855f2c44b03aef177f`.
