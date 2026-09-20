# Batch 594 — PDF page 122, Donovan through Doucette

Reviewed 2026-09-20 UTC. The original [NARA OSS personnel index](https://www.archives.gov/files/iwg/declassified-records/rg-226-oss/personnel-database.pdf), PDF page 122, has 46 printed rows. The full-size rendered page was compared with all 46 extracted rows; all raw names, initials, suffixes, ranks, identifier-column positions, empty notes, Boxes 193–196, and location 230/86/30/02 match. The printed `Dopspn` spelling is retained rather than silently corrected. The matching-only page review is replayable from `research/parser_visual_review_page122_2026-09-20.json`.

The 46 rows remain 46 separate active person entities. The three James Donovan rows on this page (B, E, and R) remain separate. William J Donovan already had a cited employer finding before this batch; it was not reclassified or counted as new research.

One bounded [Library of Congress JSON API](https://www.loc.gov/apis/json-and-yaml/working-within-limits/) pass made 46 successful, rate-limited read-only searches, with zero blocked requests and zero errors. It saved 30 **unreviewed discovery candidates** concerning 10 people. None is an accepted identity, employer claim, or completed minimum-protocol outcome. The sanitized attempts and candidates are replayable from `research/adapter_attempt_checkpoints.json`.

The official [Army bulk file](https://catalog.archives.gov/id/1263923) already supplied 16 page-122 identity candidates. A review of nonshared protected-identifier agreement and the *full printed names*, not merely the adapter's initial-based alignment label, accepted 14 identity candidates, retained one probable spelling/suffix variant (Phillip G Dotzauer III versus Philip G Dotzauer TRD), and marked one name discrepancy conflicting (indexed John E Dooley versus bulk DO LEY JOHN E). These are **private identity decisions only**; Army occupation codes are not named employers, and none of the 16 was promoted to a public employer claim. The decisions are replayable from `research/army_review_decisions_2026-09-20_batch594.csv`.

Two source reviews require further work:

- Willy Dorchain, Box 194: the [June 1945 Justice Department FARA report](https://www.justice.gov/nsd-fara/page/file/991971/dl?inline=), original printed pp. 353–354/PDF pp. 356–357, records International Transport Workers Federation registration 212 from September 1943, but names Becu and Brier as officers, **not Dorchain**. The [June 1950 report](https://www.justice.gov/nsd-fara/page/file/991961/dl) names Willy Jules Polidore Dorchain under registration 212 in an index covering 1945–49. The organization's 1943 date cannot be imputed to Dorchain's personal employment, and his OSS entry date is still unknown. No pre-OSS federation employer is published.
- Alexis Doster Jr., Box 195: a genealogy search lead mentions experimental work at Colt, but the PDF timed out and was not inspected. Smithsonian and contemporary-news discovery excerpts describe a wartime Army experiment, not paid Colt employment or an OSS transition date. Search excerpts are not final sources. No Colt employer or immediate affiliation is published.

The Dorchain and Doster reviews are replayable from `research/evidence-page-122-donovan-doucette_batch-594_2026-09-20.json`. The bundle has two manual attempts and two person-status updates, **zero** public sources, claims, affiliations, or organizations. Both files retain high-priority Box review guidance. No authenticated NARA Catalog API call was made; no Catalog response body was stored.

At this checkpoint, page-122 statuses are 10 `candidate_found`, 33 `in_progress`, two `needs_identity_review`, and the one previously `verified_employer_found`. Thus 45 of 46 still need substantial source review; a LoC query is not a completed research protocol.

Project-wide index coverage is **23,978/23,978** linked source rows. Research-attempt coverage is **5,827/23,940** active people (24.3400%); verified-employer coverage is unchanged at **266/23,940** (1.1111%); verified-affiliation coverage is **607/23,940** (2.5355%); archival-review assessment is **5,701/23,940** (23.8137%). `not_started` is **18,113**. Private research attempts total **10,800**. Claim-confidence counts remain 1,308 confirmed, 1,843 high, 1,367 medium, 185 low, and 129 conflicting. The official Army bulk crosswalk still has thousands of unreviewed candidates; its `name_agrees` flag checks a first initial rather than exact full-name equality, so it must not be mass-promoted without a stricter predicate and QA.

Replay and resume:

```bash
python3 -m oss_research import-page-reviews research/parser_visual_review_page122_2026-09-20.json
python3 -m oss_research assign-page-batch --batch-name page-122-donovan-doucette-b594 --page 122 --first-row 1 --last-row 46
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
python3 -m oss_research import-review-decisions research/army_review_decisions_2026-09-20_batch594.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page-122-donovan-doucette_batch-594_2026-09-20.json
python3 -m oss_research research --source loc --batch page-122-donovan-doucette-b594 --max-queries 20 --resume
python3 -m oss_research export-adapter-checkpoints
python3 -m oss_research export-derived
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
```

Do not automate the CIA Reading Room route while its robots policy disallows it. The remaining page-122 people need official and institutional source checks, documented namesake rejections, and physical personnel-file review where online sources cannot settle identity or temporal order.

Local release validation: 121 Python tests passed; seven ingest gates passed;
the 200-profile stratified *structural* audit passed; the static build checked
224 source files with zero diagnostics and emitted 24,657 pages; all 78 bounded
browser tests passed, including 30 axe accessibility checks; all internal
links resolved; public-identifier redaction had zero unexpected matches; and
the local manifest matched 67 assets. These checks do not establish live
deployment or historical source-level audit completion.
