# Batch 604: index page 136 and cautious source review

The original NARA personnel-index PDF page 136 was rendered at 170 dpi and
rechecked against the saved extraction, row by row. All 46 printed personnel
rows match their immutable source records, including the Box 219-to-220
transition at Ruth Emswiler, the Box 220-to-221 transition at Ralph Eno,
the `ASN 0-1` and `ASN 020` notes, and the common archive location. Page 136
was already in the required visual sample, so the distinct review ledger
remains **107/522 pages**; **415** remain.

Two plausible variant pairs were flagged without merging either source rows
or people: Rudolphe J Emond / Rudolphe J Enond (separate boxes, only the
former with an identifier) and George W Engl / George W England (shared
box, only the former with an identifier). The printed spellings remain as
indexed. Their personnel files must be compared before any identity merge
or employer transfer.

The bounded Library of Congress pass makes one read-only first-pass query
for each of page 136's 46 indexed people. Saved newspaper-page candidates
are discovery leads, **not** accepted identity or employer evidence. A
query that returns no result is not a completed multi-source research
protocol. This batch makes no authenticated NARA Catalog request.

Three manual source reviews illustrate the confidence boundary:

- [Van Harvey English](https://therealjameswilson.github.io/before-oss/people/a1b5cb3b-8221-5bf4-ac6a-2cdf45dbab56/) is matched to the geographer/cartographer in [Dartmouth's November 1946 account](https://archive.dartmouthalumnimagazine.com/article/1946/11/1/with-the-faculty): the uncommon full name, Army captain rank, and explicit 1942–45 OSS service align with the index. [Dartmouth's October 1946 account](https://archive.dartmouthalumnimagazine.com/article/1946/10/1/faculty-appointments) corroborates the name and rank but disagrees with November about his Colorado State graduation year (1936 versus 1939). Neither article names a pre-OSS employer. The later Dartmouth appointment is not imported into his pre-OSS career.
- Indexed Robert K Enders has no rank or service identifier. The [Smithsonian authority entry for zoologist Robert Kendall Enders](https://siarchives.si.edu/collections/auth_per_fbr_eacp365) gives academic employers, but supplies no OSS link. That candidate remains rejected pending Box 220 review; its jobs are not assigned to the indexed person.
- Indexed John L Endacott is not [Paul Endacott, the Phillips Petroleum president named in the National Petroleum Council's 1955 report](https://www.npc.org/reports/1955-Petroleum_Imports.pdf). A shared surname and a postwar oil-company title do not establish John's identity or pre-OSS employer. His profile and the dedicated oil-company list exclude that false positive.

The top oil-company category remains a list of six people with cited,
person-specific pre-OSS employment evidence. It does not count oil-industry
mentions, relatives, namesakes, or speculative leads.

At the post-batch checkpoint, **23,978/23,978** index rows are linked to
**23,940** active people. **6,459** people have nonplanned research attempts
(26.9799%), **271** have confirmed/high published employer evidence
(1.1320%), **617** have confirmed/high published affiliation evidence
(2.5773%), and **5,764** have an assessed archival-review disposition
(24.0769%). **17,481** remain `not_started`. Two new possible-duplicate
groups bring that total to **279**. SQLite retains **11,502** attempts or
plans, **4,865** claims, **4,997** citations, and **2,326** unique source
documents. The public projection has **2,202** affiliations, **693**
organizations, **3,794** sources, and **4,676** claims. Full-index
historical research remains unfinished.

## Replay and continuation

After importing earlier batches into the private SQLite database:

```sh
python3 -m oss_research import-page-reviews research/parser_visual_review_page136_2026-09-21.json
python3 -m oss_research assign-page-batch --batch-name page-136-emerson-enos-b604 --page 136 --first-row 1 --last-row 46
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
python3 -m oss_research import-reviewed-evidence research/evidence-page136-duplicate-review_batch-604_2026-09-21.json
python3 -m oss_research import-reviewed-evidence research/evidence-page136-english-and-rejected-namesakes_batch-604_2026-09-21.json
python3 -m oss_research validate-ingest
python3 -m oss_research export-derived
python3 -m oss_research build-public-data
python3 -m oss_research coverage-report
```

The NARA API key is not used, copied into the repository, or included in
public assets. The local SQLite database remains private; its replayable
adapter checkpoint retains sanitized attempt metadata, not raw API payloads.
