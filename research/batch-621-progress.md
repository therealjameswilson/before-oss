# Batch 621: PDF pages 281-290 and variant review

Original NARA PDF pages **281-290** were rendered at 180 dpi. All **460**
printed rows were compared against the immutable SQLite extraction for row
order, indexed spelling, initials, rank, private-identifier column occupancy,
box, notes, and archival location. All ten complete pages match the current
extraction. Page 281 had already been audited as a parser-warning page, so this
replay adds nine pages and **414** rows to the complete-page ledger. Visual
review now covers **242/522 pages** and **11,098/23,978 rows**: **11,070**
reviewed rows match the extraction, **28** retain reviewed corrections, and
**12,880** remain for complete visual comparison.

The review preserves literal index anomalies rather than silently repairing
them. Page 281 row 22, Marion Loftis, retains its prior reviewed correction:
the digits are visibly printed in the rank column and the private-identifier
column is blank. Other preserved forms include `Loehr, ndrew`; repeated Max
Loeb and Vincent Lossowski rows; Longenecker / Longnecker and Loofbourrow /
Loofburrow spellings; scientific-notation-looking text for Robert Luther;
Macaulay / Macauley; `MacHado`; three Robert B MacLeod rows across two boxes
and archive locations; clipped index notes; and military, naval, civilian,
foreign, and warrant grades exactly as printed.

Twenty-one bounded queues were assigned for **459** previously unowned people.
Gus Macriyanni at page 289 row 27 retains the earlier `pilot-v1` assignment and
`requires_archival_review` status, so Batch 621 deliberately does not overwrite
that queue ownership.

The two page-281 Library of Congress passes completed **46** live searches,
producing **13** newspaper candidates across eight people with zero adapter
errors. Context review rejected all 13 as composer references, early or postwar
namesakes, a burglary notice, a place-name or real-estate usage, conflicting
middle initials, adjacent OCR names, or an item whose malformed official OCR
left metadata too weak to identify the indexed person. Four people whose only
candidate was rejected returned to `in_progress`; four remain
`candidate_found` because separate Army bulk or duplicate-person candidates
still require review. No employer claim was added, no raw LoC response was
retained, and no authenticated NARA request was made.

Twelve possible-duplicate, spelling-variant, or private-identifier conflict
groups covering **27 people** were reviewed without an unsupported merge. The
groups include three materially different names sharing one private identifier
on page 281; Longenecker / Longnecker; Loofbourrow / Loofburrow; two Vincent
Lossowski rows; Luciani / Luciano with the `?Lucky?` note; two Helen Ludwig
rows; two Richard Lyman rows; Macaulay / Macauley; two Clark MacGregor rows;
two Malcolm S MacKenzie rows; the cross-page Mackay / McCay identifier match;
and three Robert B MacLeod rows. Three people carry `conflicting` identity
status with critical archival priority; the other 24 are `ambiguous` with high
priority. Page 304 row 36 was visually checked only to corroborate the
Mackay/McCay pair; page 304 is not counted as a complete-page audit.

At this checkpoint, **23,978/23,978** printed rows link to **23,939** active
person entities. Research-attempt coverage is **7,376/23,939 (30.8116%)**;
confirmed/high verified-employer coverage is **280/23,939 (1.1696%)**;
confirmed/high verified-affiliation coverage is **628/23,939 (2.6233%)**;
archival-review disposition coverage is **6,237/23,939 (26.0537%)**. There are
**16,563** `not_started` people, **476** active possible-duplicate groups, and
**146** active people with conflicting identity or source status. The database
stores **12,434** attempts or plans and **4,900** claims: **1,311** confirmed,
**1,898** high, **1,374** medium, **185** low, and **132** conflicting. It
contains **5,045** source/citation records and **2,372** unique document keys.
The public projection remains **2,224** affiliations, **708** organizations,
**3,842** sources, and **4,711** claims. The oil-company category remains a
supported, incomplete evidence set of **seven** people across nine companies.
Full-index historical research is unfinished.

## Local release validation

Release validation will be recorded in `reports/release_batch_621.md` after the
tracked-only candidate passes the complete test, build, accessibility, link,
redaction, and deterministic-build suite.

## Replay and continuation

After importing the prior durable batches into private SQLite:

```sh
python3 -m oss_research import-page-reviews research/parser_visual_review_pages281-290_2026-09-21.json
python3 -m oss_research import-review-decisions research/loc_review_decisions_2026-09-21_batch621.csv
python3 -m oss_research import-reviewed-evidence research/evidence-pages281-290-duplicate-review_batch-621_2026-09-21.json
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
```

Recreate the exact 21 page queues idempotently with these commands:

```sh
python3 -m oss_research assign-page-batch --batch-name page-281-lockwood-logan-b621 --page 281 --first-row 1 --last-row 23
python3 -m oss_research assign-page-batch --batch-name page-281-logan-loney-b621 --page 281 --first-row 24 --last-row 46
python3 -m oss_research assign-page-batch --batch-name page-282-long-longley-b621 --page 282 --first-row 1 --last-row 23
python3 -m oss_research assign-page-batch --batch-name page-282-longnecker-lopresti-b621 --page 282 --first-row 24 --last-row 46
python3 -m oss_research assign-page-batch --batch-name page-283-lopresto-losinski-b621 --page 283 --first-row 1 --last-row 23
python3 -m oss_research assign-page-batch --batch-name page-283-losquadro-lovelock-b621 --page 283 --first-row 24 --last-row 46
python3 -m oss_research assign-page-batch --batch-name page-284-lovenbein-lowndes-b621 --page 284 --first-row 1 --last-row 23
python3 -m oss_research assign-page-batch --batch-name page-284-lowndes-luce-b621 --page 284 --first-row 24 --last-row 46
python3 -m oss_research assign-page-batch --batch-name page-285-luciani-lukacs-b621 --page 285 --first-row 1 --last-row 23
python3 -m oss_research assign-page-batch --batch-name page-285-luke-lunning-b621 --page 285 --first-row 24 --last-row 46
python3 -m oss_research assign-page-batch --batch-name page-286-luntz-lydon-b621 --page 286 --first-row 1 --last-row 23
python3 -m oss_research assign-page-batch --batch-name page-286-lydon-lynch-b621 --page 286 --first-row 24 --last-row 46
python3 -m oss_research assign-page-batch --batch-name page-287-lynch-lytzen-b621 --page 287 --first-row 1 --last-row 23
python3 -m oss_research assign-page-batch --batch-name page-287-mabie-macdonald-b621 --page 287 --first-row 24 --last-row 46
python3 -m oss_research assign-page-batch --batch-name page-288-macdonald-mack-b621 --page 288 --first-row 1 --last-row 23
python3 -m oss_research assign-page-batch --batch-name page-288-mack-maclennan-b621 --page 288 --first-row 24 --last-row 46
python3 -m oss_research assign-page-batch --batch-name page-289-macleod-macpherson-b621 --page 289 --first-row 1 --last-row 23
python3 -m oss_research assign-page-batch --batch-name page-289-macpherson-macridis-b621 --page 289 --first-row 24 --last-row 26
python3 -m oss_research assign-page-batch --batch-name page-289-mactavish-maehle-b621 --page 289 --first-row 28 --last-row 46
python3 -m oss_research assign-page-batch --batch-name page-290-maertens-magyar-b621 --page 290 --first-row 1 --last-row 23
python3 -m oss_research assign-page-batch --batch-name page-290-mahala-maisonpierre-b621 --page 290 --first-row 24 --last-row 46
```

The page-281 LoC passes and decisions are already checkpointed. Continue with
the first unsearched queue, then rebuild all derived outputs:

```sh
python3 -m oss_research research --source loc --batch page-282-long-longley-b621 --max-queries 23 --resume
python3 -m oss_research export-adapter-checkpoints
python3 -m oss_research export-derived
python3 -m oss_research build-public-data
python3 -m oss_research coverage-report
```

No API key, full service number, raw API response, or private reviewer note is
committed or included in the public site.
