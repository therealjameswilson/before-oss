# Batch 603: index page 135 and E-section research

The original NARA personnel-index PDF page 135 was rendered at 170 dpi and
compared row-by-row with the saved extraction. All 46 printed rows match their
immutable source records, including the Box 217-to-218 and archive-location
change at William W Ellis, the Box 219 change at Albert P Emanuel, the
Yeoman/USNR note on the second Richard D Ellmann row, and the printed
`ASN 200` note on Robert N Elwell. The distinct page-review ledger is now
**107/522 pages**; **415** remain. Two possible-duplicate groups—Richard D
Ellmann twice and Ted/Theodore Ellis—were marked for physical-file comparison.
Neither source rows nor person entities were merged.

The page-133 and page-134 research queues received **45** and **46** bounded,
read-only Library of Congress searches respectively. All **46** page-135
people have a saved live source attempt; **64** page-135 queries were made
because 18 already-covered people received a second name-variant query before
the `--resume` repair. These are discovery attempts, not completed
multi-source research protocols. Newspaper-page results remain unreviewed
candidates until their text, identity, and time context are inspected. A
temporary DNS failure stopped the first page-134 attempt, but a controlled
retry completed it; no 429 rate-limit bypass or NARA Catalog request was made.
During page 135, a LoC read timeout interrupted a saved batch. Checkpoint
inspection revealed that the previously parsed `--resume` flag had not
prevented second-name-variant searches for already-covered people. The
scheduler now skips saved live source attempts when `--resume` is supplied,
while excluding dry-run plans; an 18-person dry-run verified the remaining
first-pass cohort before network requests resumed. Further variant searches
remain available by omitting `--resume` or targeting one person.

Three source reviews add differentiated pre-OSS context:

- [Sergei Elisseeff](https://therealjameswilson.github.io/before-oss/people/8829fd35-280c-54c2-8348-ca57b8befb3d/) is strongly identified with Serge Elisséeff through the rare indexed name, Dr. title, and the [Harvard-Yenching Institute's Sergei/Serge crosswalk](https://www.harvard-yenching.org/news/new-book-published-former-hyi-director-serge-elisseeff/). [Harvard's 1930s chronology](https://ealc.fas.harvard.edu/1930-1940) supports a 1934 professorship and separate Institute directorship; [two](https://www.thecrimson.com/article/1934/1/26/serge-elisseeff-chosen-to-be-harvard/) [contemporary notices](https://www.thecrimson.com/article/1934/2/15/elisseeff-appointed-to-head-yenching-institute/) document his preceding École pratique des hautes études role. The roles are not called jobs he left directly for OSS. Box 216 and the consultant timeline remain to be examined. A guarded display-name decision removes the printed `Dr.` honorific from the normalized name while preserving the raw index row.
- [Lorenz E. A. Eitner](https://therealjameswilson.github.io/before-oss/people/31a9a6d6-7414-5e2c-887d-214d6e723ea7/) is matched at high confidence to [Princeton's graduate memorial](https://paw.princeton.edu/memorial/lorenz-e-eitner-52/), which states he withdrew in 1943 to join the Army and OSS. Princeton is recorded as student status, **not** employment; an Army assignment may have intervened before OSS.
- The indexed *Yeoman/USNR* [Richard D. Ellmann row](https://therealjameswilson.github.io/before-oss/people/572c9c93-f927-5f68-8344-4a76fe5ff959/) is linked at high confidence to [Nicolas Barker's British Academy memoir](https://www.thebritishacademy.ac.uk/sites/default/files/08%20Ellmann%201808.pdf). Its explicit chronology places a Harvard instructorship in 1942–43 before Navy service, then a transfer **from the Navy back to OSS**. Harvard is therefore recorded as the last named civilian employer before Navy service, while the Navy is the immediate affiliation for the later OSS transfer. Ellmann's initial 1942 COI work and the unranked same-name Box 218 row are kept separate from those two claims; the latter row is not merged or assigned Harvard employment without personnel-file review.

A re-review of [Yale's John Fee Embree chronology](https://macmillan.yale.edu/southeast-asia/john-fee-embree), [Fred Eggan's 1951 memorial](https://cseas.yale.edu/sites/default/files/files/Embree_obit_Eggan.pdf), and [Densho's account](https://encyclopedia.densho.org/John_F._Embree/) preserves the 1941 University of Toronto position but lowers its *immediate* temporal basis from strongly date-bounded to probable. The reviewed sources do not give his Toronto exit date or exact COI/OSS start. The public claim is qualified; his earlier University of Hawaii employment stays documented.

The top oil-company category continues to include only the six previously
cited employees; none of these academic affiliations changes that list.

At the post-batch checkpoint: 23,978/23,978 index rows are linked; 23,940
active person entities include 6,413 with nonplanned research attempts,
271 with confirmed/high published employer evidence, 617 with confirmed/high
published affiliation evidence, and 5,757 with an assessed archival-review
disposition. There are 17,527 `not_started` people. The new LoC candidates
have not been accepted as historical claims.

## Replay and continuation

After importing earlier batches into the private SQLite database:

```sh
python3 -m oss_research import-page-reviews research/parser_visual_review_page135_2026-09-20.json
python3 -m oss_research assign-page-batch --batch-name page-135-ellis-emerine-b603 --page 135 --first-row 1 --last-row 46
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
python3 -m oss_research import-reviewed-evidence research/evidence-page135-duplicate-review_batch-603_2026-09-20.json
python3 -m oss_research import-reviewed-evidence research/evidence-sergei-elisseeff-harvard_batch-603_2026-09-20.json
python3 -m oss_research import-reviewed-evidence research/evidence-lorenz-eitner-princeton_batch-603_2026-09-20.json
python3 -m oss_research import-reviewed-evidence research/evidence-embree-toronto-chronology-correction_batch-603_2026-09-20.json
python3 -m oss_research import-reviewed-evidence research/evidence-richard-ellmann-harvard-navy_batch-603_2026-09-20.json
python3 -m oss_research import-review-decisions research/identity_display_corrections_batch-603_2026-09-20.csv
python3 -m oss_research validate-ingest
python3 -m oss_research export-derived
python3 -m oss_research build-public-data
python3 -m oss_research coverage-report
```

The NARA Catalog API key is not present in the local environment. It was not
used, copied into the repository, or exposed to the public site. The local
SQLite database remains private; its versioned adapter checkpoint retains
sanitized attempt metadata, not raw Library of Congress API responses.
