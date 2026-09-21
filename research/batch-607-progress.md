# Batch 607: PDF pages 141–150 and bounded research

Original NARA PDF pages **141–150** were rendered at 180 dpi. All **460**
printed rows were compared against the immutable SQLite extraction for row
order, indexed spelling, initials, rank, private-identifier column occupancy,
box, notes, and archival location. There were no extraction corrections. The
distinct visual-review ledger is now **121/522 pages**; **401** pages remain
for individual visual comparison. The 92 selected QA pages and all parser-
warning rows have completed their required visual review. These checks do
not mean that every page of the PDF has passed manual comparison.

The original index suggests eight new possible-duplicate or spelling-variant
groups: Roger Faucher, Robert W Feeney, Leon Feldman, Harry Finney, John
Fistere, Brooks K Fleming/Flemming, John E Fleming/Flemming, and Andre
Fleuridas. These are marked ambiguous and remain separate person entities
pending file-level comparison. Page 148 has two identical Harry Flater
source rows already linked to one high-confidence person through the shared
indexed name and private identifier. Page 146's James Fischer and page 149's
James A Fogarty pairs have distinct private identifiers and remain separate.
The public site masks those identifiers.

The printed `Cmdr` rank exposed a classification gap. The exact abbreviation
now classifies as commissioned naval officer, and the monotonic
`refresh-classifications` command upgraded **8** formerly indeterminate
source rows and **7** single-row person entities. It did not alter raw rank
cells, already known categories, or a previously reviewed person category.
`--dry-run` and a focused idempotence test protect future replays.

The bounded, read-only Library of Congress first pass completed **36/36**
page-139, **46/46** page-140, and **46/46** page-141 searches: **128** live
queries with no errors. It saved **13**, **6**, and **35** unreviewed
newspaper-page candidates respectively (**54** total). These are discovery
leads, not accepted identity matches or employer claims, and a single LoC
search is not a completed multi-source research protocol. No authenticated
NARA Catalog request was made.

[Linn M Farish](https://therealjameswilson.github.io/before-oss/people/c9356a0e-8474-5f03-a634-0bff4555e069/)
of page 141 has one new qualified **medium-confidence earlier professional
affiliation** with Amiranian Oil Company. A [1937 State Department diplomatic
despatch](https://history.state.gov/historicaldocuments/frus1937v02/d592)
explicitly calls him its representative; a [CIA-published review](https://www.cia.gov/resources/csi/static/Intel-Officers-Bookshelf-54.4.pdf)
corroborates the distinctive OSS Major identity. Neither source establishes
that he was salaried by the company, that it was his final civilian employer,
or that it immediately preceded OSS service. His profile therefore leaves
those questions unresolved and prioritizes Box 228 review. The public
oil-company **workers** category remains **seven** cited employees and
excludes this representation-only lead.

At this checkpoint, **23,978/23,978** printed rows link to **23,940** active
person entities. Research-attempt coverage is **6,684/23,940 (27.9198%)**;
confirmed/high verified-employer coverage is **271/23,940 (1.1320%)**;
confirmed/high verified-affiliation coverage is **617/23,940 (2.5773%)**;
archival-review disposition coverage is **5,786/23,940 (24.1688%)**. There
are **17,256** `not_started` people, **289** possible-duplicate groups, and
**128** active people with conflicting identity or source status. The DB
stores **11,733** attempts or plans and **4,868** claims: **1,311** confirmed,
**1,868** high, **1,372** medium, **185** low, and **132** conflicting. It
contains **5,009** source/citation records and **2,337** unique document
keys. The public projection has **2,205** affiliations, **695** organizations,
**3,806** sources, and **4,679** claims. Full-index historical research is
unfinished.

Local QA passed: **126** Python unit tests; the **78/78** bounded desktop,
phone, and tablet release checks, including **30** axe accessibility checks;
the **200-profile structural** audit; the **24,694-page** internal-link
check; the public-number redaction scan; and the static Astro build. The
structural sample is **not** the required 200-profile manual historical
source audit. The link checker inventoried **50,228** external URLs but did
not request every target. Clean CI and public deployment require separate
verification.

## Replay and continuation

After importing the prior durable batches into private SQLite:

```sh
python3 -m oss_research import-page-reviews research/parser_visual_review_pages141-145_2026-09-21.json
python3 -m oss_research import-page-reviews research/parser_visual_review_pages146-150_2026-09-21.json
python3 -m oss_research import-reviewed-evidence research/evidence-pages142-143-duplicate-review_batch-607_2026-09-21.json
python3 -m oss_research import-reviewed-evidence research/evidence-pages146-149-duplicate-review_batch-607_2026-09-21.json
python3 -m oss_research import-reviewed-evidence research/evidence-linn-farish-amiranian_batch-607_2026-09-21.json
python3 -m oss_research refresh-classifications --dry-run
python3 -m oss_research refresh-classifications
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
python3 -m oss_research export-derived
python3 -m oss_research build-public-data
python3 -m oss_research coverage-report
```

The ten PDF-page batches are assigned durably in the private research queue;
the exported adapter checkpoint carries the three completed LoC batches.
Continue with the assigned page-142 queue using
`python3 -m oss_research research --source loc --batch page-142-faucher-feldman-b607 --max-queries 46 --resume`.
No API key, full service number, raw API response, or private reviewer note is
committed or included in the public site.
