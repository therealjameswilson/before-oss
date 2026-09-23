# Batch 644: PDF pages 511-520 and McPadden-McVannel research

All **460** printed rows on original NARA PDF pages 511-520 were compared
against SQLite at 180 dpi. Pages 517-520 were already present in the
stratified-random complete-page ledger. Every row matches the current
extraction and requires no correction. Complete-page visual review now covers
**430/522 pages** and **19,746/23,978 rows**: **19,714** reviewed rows match
the extraction, **32** retain reviewed corrections, and **4,232** remain for
complete visual comparison.

The page-313 `John F. McPadden` through `Donald S. McVannel` queue contains 23
source rows representing **23** cautious person entities. All 23 received
staged project query plans and exact-name OSS/employment discovery review.
The Library of Congress adapter timed out after bounded retries on its first
request, and the CIA adapter correctly stopped at the collection's robots
policy. Those access outcomes are saved as errors rather than rewritten as
negative evidence. Targeted discovery searches produced no reliable employer
claim; search snippets and unrelated namesakes were not used as sources.

Six preexisting official Army or duplicate-boundary candidates received
review decisions. Exact normalized names and nonshared protected identifiers
support high-confidence identity crosswalks for Robert E. McPeek, James F.
McPoil, Robert C. McQueen, and Donald S. McVannel. The discrepant or date-bound
Army grade fields for McQueen and McVannel remain review context and are not
treated as contradictions or employer evidence.

Thomas E. McParland and Thomas E. McPharland remain two separate probable
entities. Their adjacent Box 512 rows share a protected identifier but differ
in indexed surname spelling and rank occupancy. Joann W. McQuiston and Joanne
W. Mcquiston likewise remain two separate probable entities: their adjacent
Box 513 rows have near-identical names, but no protected identifier resolves
whether the jackets belong to one person. Both pairs require examination of
both personnel files before any merge or employment inference.

The final 23-person queue state is **19** `in_progress` and four
`needs_identity_review`. All six stored candidates have review decisions:
four accepted and two probable. The bundle adds four high-confidence and four
qualified medium-confidence identity claims, with no employer or affiliation
claim. Full identifiers remain private. Army grades, entry dates, and
occupation codes remain identity context rather than employer evidence.

Rebuilt coverage remains **23,978/23,978** linked source rows and **23,939**
active person entities. Research-attempt coverage is **7,922/23,939
(33.0924%)**; confirmed/high verified-employer coverage is **280/23,939
(1.1696%)**; confirmed/high verified-affiliation coverage is **628/23,939
(2.6233%)**; archival-review disposition coverage is **6,380/23,939
(26.6511%)**. There are **16,012** `not_started` people, **490** active
possible-duplicate groups, and **170** active people with conflicting identity
or source status. The database stores **13,147** attempts or plans and
**5,000** claims: **1,311** confirmed, **1,973** high, **1,384** medium,
**187** low, and **145** conflicting. It contains **5,080** source/citation
records and **2,391** unique document keys. The public projection contains
**2,224** affiliations, **708** organizations, **3,873** sources, and **4,809**
claims. The oil-company category remains prominently available at the top of
the site and is a supported, incomplete evidence set of seven people across
nine historically named companies. Full-index historical research is
unfinished.

## Replay and continuation

After importing prior durable batches into private SQLite:

```sh
python3 -m oss_research import-page-reviews research/parser_visual_review_pages511-520_2026-09-22.json
python3 -m oss_research import-review-decisions research/identity_review_decisions_2026-09-22_batch644.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page313-mcpadden-mcvannel-review_batch-644_2026-09-22.json
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
```

Continue with the next bounded research and visual-audit batch, then rebuild:

```sh
python3 -m oss_research export-adapter-checkpoints
python3 -m oss_research export-derived
python3 -m oss_research build-public-data
python3 -m oss_research coverage-report
```

No API key, full service number, raw API response, copyrighted page image, or
private reviewer note is committed or included in the public site. No
authenticated NARA Catalog request was made.
