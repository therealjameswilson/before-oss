# Batch 628: PDF pages 351-360 and completion of the McBride-McCann queue

Original NARA PDF pages **351-360** were rendered at 180 dpi. All **460**
printed rows were compared against the immutable SQLite extraction for row
order, indexed spelling, initials, rank, private-identifier column occupancy,
box, notes, and archival location. All ten pages match the current extraction.
Page 358 already had a complete correction review, so this replay adds nine
pages and **414** rows to the complete-page ledger. Visual review now covers
**295/522 pages** and **13,536/23,978 rows**: **13,504** reviewed rows match
the extraction, **32** retain reviewed corrections, and **10,442** remain for
complete visual comparison.

The complete page-303 `William H. McBride` through `Richard J. McCann` queue
contains **23** people. Its Library of Congress pass completed **23** live
exact-name searches and created **29** discovery candidates. Every candidate
was inspected through official item-level OCR and the bounded full-text
fallback. Candidates with differing initials or given names included James
Ross, James A., and James Clark McCain; Richard V. and Richard W. McCann;
William E. and William J. McBride; William X., William H., and William A.
McCall; and William J., William A., and William L. McCabe. Other hits were an
unresolved postwar Carlos R. McCalla Jr. notice, surname-only or radio-schedule
fragments, an exact-name Ward McCabe theater listing that could not resolve an
existing duplicate-identifier conflict, and an exact-name Nancy McCandlish
tennis result without a corroborating identifier or employment evidence. All
29 candidates were rejected. No employer claim was added and no raw Library
of Congress response was retained.

Four pre-existing official Army bulk candidates received manual review.
William H. McBride's full indexed name and nonshared protected identifier
agree, supporting a `high_confidence` identity crosswalk. Curtis B. McCammon's
first and last name and nonshared protected identifier agree, but the middle
initial conflicts, so the identity remains `conflicting` and the person moves
to `needs_identity_review`. The remaining two candidates concern the protected
identifier printed for both Ward McCabe and William W. McCabe on adjacent
index rows; both remain `conflicting` pending review of the original Box 497
jackets. Army grade and occupation codes were not treated as employers or
immediate pre-OSS affiliations.

The final queue state is **20** `in_progress`, **1**
`needs_identity_review`, and **2** `conflicting_sources`. All 23 people have a
saved Library of Congress attempt and every one of the 29 source candidates
has a review decision. This is research-attempt progress, not completion of
the minimum research protocol.

At this checkpoint, **23,978/23,978** printed rows link to **23,939** active
person entities. Research-attempt coverage is **7,557/23,939 (31.5677%)**;
confirmed/high verified-employer coverage is **280/23,939 (1.1696%)**;
confirmed/high verified-affiliation coverage is **628/23,939 (2.6233%)**;
archival-review disposition coverage is **6,298/23,939 (26.3085%)**. There are
**16,349** `not_started` people, **488** active possible-duplicate groups, and
**158** active people with conflicting identity or source status. The database
stores **12,615** attempts or plans and **4,900** claims: **1,311** confirmed,
**1,898** high, **1,374** medium, **185** low, and **132** conflicting. It
contains **5,045** source/citation records and **2,372** unique document keys.
The public projection remains **2,224** affiliations, **708** organizations,
**3,842** sources, and **4,711** claims. The oil-company category remains a
supported, incomplete evidence set of **seven** people across nine companies.
Full-index historical research is unfinished.

## Replay and continuation

After importing prior durable batches into private SQLite:

```sh
python3 -m oss_research import-page-reviews research/parser_visual_review_pages351-360_2026-09-21.json
python3 -m oss_research import-review-decisions research/loc_review_decisions_2026-09-21_batch628.csv
python3 -m oss_research import-review-decisions research/loc_review_decisions_2026-09-21_batch628b.csv
python3 -m oss_research import-review-decisions research/loc_review_decisions_2026-09-21_batch628c.csv
python3 -m oss_research import-review-decisions research/army_review_decisions_2026-09-21_batch628.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page303-mcbride-mccann-identity-review_batch-628_2026-09-21.json
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
```

Continue with the next assigned queue, then rebuild derived outputs:

```sh
python3 -m oss_research research --source loc --batch page-304-mccann-thomas-mccarthy-john-b623 --max-queries 10 --resume
python3 -m oss_research export-adapter-checkpoints
python3 -m oss_research export-derived
python3 -m oss_research build-public-data
python3 -m oss_research coverage-report
```

No API key, full service number, raw API response, or private reviewer note is
committed or included in the public site.
