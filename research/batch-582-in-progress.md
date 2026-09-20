# Batch 582 — bounded research checkpoint, not a terminal review

Started 2026-09-20 UTC. PDF page 117, rows 21–30, covers ten distinct
indexed people: Ann J Dick, Doris R Dick, David H Dickason, Frederick G
Dickason, Samuel Dicken, Roger H Dickens, William B Dickens, Thelma W
Dickerman, Gelnn O Dickerson, and Harold E Dickerson. The original NARA page
was visually checked. Box 185 contains the first three rows; Box 186 contains
the remaining seven. All retain the indexed spelling and separate source
rows. None has a terminal research disposition yet.

The explicitly selected `batch-582` queue received ten bounded CIA Reading
Room searches (no discovery candidate) and ten Library of Congress searches
(four unreviewed newspaper-page discovery candidates, two each for Ann J
Dick and Harold E Dickerson). The LOC item URLs could not be opened by the
research browser. A direct HEAD request to one LOC resource page returned
HTTP 403 with a Cloudflare challenge on 2026-09-20; no challenge was bypassed.
The page contents, person identity, and employment relevance remain
unverified. A 1948 Harold E Dickerson hit cannot alone establish a pre-OSS
role. Do not publish these candidates as facts.

Three private official Army bulk-file identity candidates were accepted after
review of a nonshared protected identifier, name alignment, and the indexed
page: Roger H Dickens and Harold E Dickerson agree by full name; the Army
entry spells **Glenn O Dickerson** while the printed index visibly spells
**Gelnn O Dickerson**. Preserve `Gelnn` as the raw index reading and use
`Glenn` only as a documented variant. The decisions are importable from
`research/army_review_decisions_2026-09-20_batch582.csv`. These findings
establish wartime identity only. Army occupation codes do not name a civilian
employer or an immediate pre-OSS affiliation.

An initial generic `research --resume` call was found to follow global queue
priority, **not** the new assigned batch: it searched ten unrelated people
through each source. The CIA call did not produce new local attempt rows
because completed fingerprints already existed; the LOC call recorded ten
separate discovery attempts, with unreviewed candidates for Carl D Marshall
and Joseph F Willis. Those attempts remain in private SQLite but must not be
counted as Batch 582 review. Subsequent commands used `--batch batch-582`.

The global LOC search also exposed a scheduler bug: supplementary discovery
attempts could replace a previously reviewed terminal research status. It
temporarily changed Carl D Marshall, Constantine Papadopoulos, and Gus
Macriyanni from `requires_archival_review`, and Edson P Bradley from
`occupation_only_found`, to automatic discovery states. The four person and
queue statuses and next actions were restored from the exact-verified Batch
581 public projection via the importable
`research/review_decisions_2026-09-20_discovery_status_repair.csv`.
`oss_research/research.py` now increments attempt counters for supplemental
searches while allowing automatic status transitions **only** among
`not_started`, `in_progress`, and `candidate_found`; regression tests cover
ten reviewed-status categories. Unreviewed candidates remain available for
later assessment without erasing prior archival or employer conclusions.

Next: inspect accessible original or alternative archival context for the
four newspaper leads without bypassing access controls; run targeted
employment, obituary, institutional, and military/OSS disambiguation for
each person; review every candidate and rejection; then write an importable
evidence bundle with terminal outcomes only when the documented protocol is
met. The Box 185–186 personnel files remain archival fallback. No public
data build should treat this checkpoint as completed research.

Resume the bounded source checks with:

```bash
python3 -m oss_research assign-page-batch --batch-name batch-582 --page 117 --first-row 21 --last-row 30
python3 -m oss_research research --source cia --batch batch-582 --max-queries 10 --resume
python3 -m oss_research research --source loc --batch batch-582 --max-queries 10 --resume
python3 -m oss_research import-review-decisions research/army_review_decisions_2026-09-20_batch582.csv
python3 -m oss_research import-review-decisions research/review_decisions_2026-09-20_discovery_status_repair.csv
```

The completed search fingerprints and review decisions make these commands
safe to rerun against the same private database. Never interpret duplicate
search skips as a fresh source review.
