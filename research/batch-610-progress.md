# Batch 610: PDF pages 171–180 and bounded research

Original NARA PDF pages **171–180** were rendered at 180 dpi. All **460**
printed rows were compared against the immutable SQLite extraction for row
order, indexed spelling, initials, rank, private-identifier column occupancy,
box, notes, and archival location. All ten pages add matching-only decisions;
there were no extraction corrections. The distinct visual-review ledger is now
**147/522 pages**; **375** pages remain for individual comparison.

Eight new possible-duplicate or spelling-variant groups are marked ambiguous
without merging any source row or person entity. They cover the repeated Edward
J Glavin, William H Glazier, Kermit Gordon, and Robert H Green names; Gavin
W/G Gonzalez; Katherine/Kathryn Gorman; and the Charles S and Francis X
Green/Greene spelling pairs. The Glazier and Gordon pairs have different
private identifiers. Every private value remains masked publicly, and all eight
groups await personnel-file comparison.

The bounded, read-only Library of Congress first pass completed **46** searches
for the page-145 queue. It created or revisited **32** unreviewed newspaper-page
candidates across **12** people; the other **34** searches had no result. These
are discovery leads, not accepted identity matches, employer claims, or
completed multi-source protocols. No authenticated NARA Catalog request was
made.

[Nelson Glueck](https://therealjameswilson.github.io/before-oss/people/61e39cb1-9c3d-5f1e-badb-712e2694b4f7/)
now has two high-confidence documented earlier affiliations. A Hebrew Union
College institutional article dates his HUC faculty appointment to 1928, gives
three periods as director of the American School of Oriental Research in
Jerusalem, and separately records his OSS mapping and logistics work. NARA's
Entry 210 inventory independently identifies wartime records by and relating to
Glueck. Neither source establishes a formal recruitment date or whether either
institutional relationship was the immediate predecessor, so both remain in the
earlier-affiliations section and Box 277 review is the next action.

At this checkpoint, **23,978/23,978** printed rows link to **23,940** active
person entities. Research-attempt coverage is **6,870/23,940 (28.6967%)**;
confirmed/high verified-employer coverage is **272/23,940 (1.1362%)**;
confirmed/high verified-affiliation coverage is **620/23,940 (2.5898%)**;
archival-review disposition coverage is **5,845/23,940 (24.4152%)**. There are
**17,070** `not_started` people, **314** possible-duplicate groups, and **128**
active people with conflicting identity or source status. The DB stores
**11,922** attempts or plans and **4,875** claims: **1,311** confirmed,
**1,874** high, **1,373** medium, **185** low, and **132** conflicting. It
contains **5,021** source/citation records and **2,348** unique document keys.
The public projection has **2,210** affiliations, **697** organizations,
**3,818** sources, and **4,686** claims. Full-index historical research is
unfinished.

Local QA passed: **126** Python unit tests; **81/81** bounded desktop, phone,
and tablet release checks; the **200-profile structural** audit; the
**24,696-page** internal-link check; the public-number redaction scan across
**24,768** artifacts; and the static Astro build with zero errors, warnings, or
hints across **242** source files. The structural sample is **not** the required
200-profile manual historical source audit. An unrelated untracked duplicate
Sources route adds 25 local-only pages and is excluded from the clean release.
Clean CI and public deployment require separate verification.

## Replay and continuation

After importing the prior durable batches into private SQLite:

```sh
python3 -m oss_research import-page-reviews research/parser_visual_review_pages171-180_2026-09-21.json
python3 -m oss_research import-reviewed-evidence research/evidence-pages171-180-duplicate-review_batch-610_2026-09-21.json
python3 -m oss_research import-reviewed-evidence research/evidence-nelson-glueck_batch-610_2026-09-21.json
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
python3 -m oss_research export-derived
python3 -m oss_research build-public-data
python3 -m oss_research coverage-report
```

The page-171 through page-180 queues are assigned durably in private SQLite;
the pilot member on page 176 retains the original assignment. Continue the
bounded discovery queue with `python3 -m oss_research research --source loc
--batch page-146-fine-fischl-b607 --max-queries 46 --resume`. No API key, full
service number, raw API response, or private reviewer note is committed or
included in the public site.
