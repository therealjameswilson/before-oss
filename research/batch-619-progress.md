# Batch 619: PDF pages 261–270 and variant review

Original NARA PDF pages **261–270** were rendered at 180 dpi. All **460**
printed rows were compared against the immutable SQLite extraction for row
order, indexed spelling, initials, rank, private-identifier column occupancy,
box, notes, and archival location. All ten complete pages match the extraction;
there were no corrections. Five of these pages were already part of the
required middle-page or parser-warning audit, so this replay advances the
complete-page ledger by five pages and 230 rows. The visual-review ledger now
covers **224/522 pages** and **10,270/23,978 rows**: **10,240** reviewed rows
match the extraction, **30** retain earlier reviewed corrections, and **13,708**
remain for complete visual comparison.

The review preserves literal index anomalies rather than silently repairing
them. These include two Mary Kuschke rows, several words printed in the
middle-initial column, two Reynold W Larson rows in Boxes 433 and 434, Charles
Lascelles's printed `!st Lt`, and displaced or truncated rank and note text.
Julius Leblanc's `PFC` is visibly printed in the middle-initial column; the
parser warning is therefore resolved as a faithful transcription, not a field
correction.

Fifteen possible-duplicate, spelling-variant, or private-identifier conflict
groups covering **45 active people** were reviewed. The two Reynold W Larson
rows already link to one high-confidence entity because their name, rank, and
private identifier match; both immutable rows and both box references remain
visible. Seven same-identifier comparisons remain unresolved: Kuznecoff /
Volosen, Lallas / Lalonoe, Lecalvez / Legalvez, Kute Braho / Braho Kute, Lawton
/ Lax, Lalli / Lalotte, and Langhead / Laughead. Substantially different-name
collisions are marked conflicting and critical; plausible spelling or name-
order variants are marked ambiguous and high-priority. Ten same-name groups
and five additional spelling-variant groups remain separate pending physical-
file comparison. No private identifier is published or placed in a group
label.

The bounded, read-only Library of Congress discovery pass completed **46**
searches for the two page-261 queues, producing two discovery candidates and
no adapter errors. John D. Kurtz was rejected because the contemporary item
identified John J. Kurtz without an OSS or employment bridge. Benjamin Kushner
was rejected because the item provided no middle name, OSS identifier,
employer, or relevant chronology. Both people returned to `in_progress`; these
searches do not constitute the completed multi-source protocol. An initial
sandboxed request stopped on local DNS before making a request, and the
authorized retry completed. No authenticated NARA Catalog request was made.

At this checkpoint, **23,978/23,978** printed rows link to **23,939** active
person entities. Research-attempt coverage is **7,285/23,939 (30.4315%)**;
confirmed/high verified-employer coverage is **280/23,939 (1.1696%)**;
confirmed/high verified-affiliation coverage is **628/23,939 (2.6233%)**;
archival-review disposition coverage is **6,162/23,939 (25.7404%)**. There are
**16,654** `not_started` people, **450** active possible-duplicate groups, and
**141** active people with conflicting identity or source status. The database
stores **12,342** attempts or plans and **4,900** claims: **1,311** confirmed,
**1,898** high, **1,374** medium, **185** low, and **132** conflicting. It
contains **5,045** source/citation records and **2,372** unique document keys.
The public projection has **2,224** affiliations, **708** organizations,
**3,842** sources, and **4,711** claims. The oil-company category remains a
supported, incomplete evidence set of **seven** people across nine companies.
Full-index historical research is unfinished.

## Local release validation

The clean tracked-only release candidate passed 126 Python unit tests, a
200-profile deterministic structural audit, and 81 bounded Playwright tests
(including 30 accessibility cases with no serious or critical axe findings).
Astro reported zero errors, warnings, or hints and emitted 24,681 HTML pages
among 24,753 total artifacts. All internal links resolved. The public-
identifier audit found no unexpected matches, aggregate false positives, or
manifest-size false positives. Two clean production builds produced the same
24,753-file tree SHA-256:
`1f836e027bda9dc6144bf421d2fb75be0f3cf109b98a44e0551dd52e61735d58`.
The 67-asset release manifest covers 98,003,514 bytes and has SHA-256
`4ef376c64439bef98ce651dffc2c4810d26ca4aa1356cb65d3433ce3e3cd7ec3`.

## Replay and continuation

After importing the prior durable batches into private SQLite:

```sh
python3 -m oss_research import-page-reviews research/parser_visual_review_pages261-270_2026-09-21.json
python3 -m oss_research import-review-decisions research/loc_review_decisions_2026-09-21_batch619.csv
python3 -m oss_research import-reviewed-evidence research/evidence-pages261-270-duplicate-review_batch-619_2026-09-21.json
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
```

Recreate the exact 20 page queues idempotently with these commands:

```sh
python3 -m oss_research assign-page-batch --batch-name page-261-kunkel-kuschke-b619 --page 261 --first-row 1 --last-row 23
python3 -m oss_research assign-page-batch --batch-name page-261-kuschke-kwilosz-b619 --page 261 --first-row 24 --last-row 46
python3 -m oss_research assign-page-batch --batch-name page-262-kwock-lachance-b619 --page 262 --first-row 1 --last-row 23
python3 -m oss_research assign-page-batch --batch-name page-262-lachaussee-lafitte-b619 --page 262 --first-row 24 --last-row 46
python3 -m oss_research assign-page-batch --batch-name page-263-laflamme-lailes-b619 --page 263 --first-row 1 --last-row 23
python3 -m oss_research assign-page-batch --batch-name page-263-lain-lamarre-b619 --page 263 --first-row 24 --last-row 46
python3 -m oss_research assign-page-batch --batch-name page-264-lamas-lamonica-b619 --page 264 --first-row 1 --last-row 23
python3 -m oss_research assign-page-batch --batch-name page-264-lamonica-landsberg-b619 --page 264 --first-row 24 --last-row 46
python3 -m oss_research assign-page-batch --batch-name page-265-landwirth-langan-b619 --page 265 --first-row 1 --last-row 23
python3 -m oss_research assign-page-batch --batch-name page-265-langballe-lanning-b619 --page 265 --first-row 24 --last-row 46
python3 -m oss_research assign-page-batch --batch-name page-266-lanteigne-laroche-b619 --page 266 --first-row 1 --last-row 23
python3 -m oss_research assign-page-batch --batch-name page-266-larosa-larson-b619 --page 266 --first-row 24 --last-row 46
python3 -m oss_research assign-page-batch --batch-name page-267-larson-lassawski-b619 --page 267 --first-row 1 --last-row 23
python3 -m oss_research assign-page-batch --batch-name page-267-lassucq-laughead-b619 --page 267 --first-row 24 --last-row 46
python3 -m oss_research assign-page-batch --batch-name page-268-laughlin-law-b619 --page 268 --first-row 1 --last-row 23
python3 -m oss_research assign-page-batch --batch-name page-268-lawler-lawson-b619 --page 268 --first-row 24 --last-row 46
python3 -m oss_research assign-page-batch --batch-name page-269-lawton-leach-b619 --page 269 --first-row 1 --last-row 23
python3 -m oss_research assign-page-batch --batch-name page-269-leacock-lebo-b619 --page 269 --first-row 24 --last-row 46
python3 -m oss_research assign-page-batch --batch-name page-270-lebourgeois-lee-b619 --page 270 --first-row 1 --last-row 23
python3 -m oss_research assign-page-batch --batch-name page-270-lee-lee-b619 --page 270 --first-row 24 --last-row 46
```

The page-261 Library of Congress passes are already checkpointed. Continue
with the first unsearched queue, then rebuild all derived outputs:

```sh
python3 -m oss_research research --source loc --batch page-262-kwock-lachance-b619 --max-queries 23 --resume
python3 -m oss_research export-adapter-checkpoints
python3 -m oss_research export-derived
python3 -m oss_research build-public-data
python3 -m oss_research coverage-report
```

No API key, full service number, raw API response, or private reviewer note is
committed or included in the public site.
