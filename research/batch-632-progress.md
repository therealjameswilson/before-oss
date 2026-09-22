# Batch 632: PDF pages 391-400 and McConaughy-McCormick research

Original NARA PDF pages **391-400** were rendered at 180 dpi. All **460**
printed rows were compared against the immutable SQLite extraction for row
order, indexed spelling, initials, rank, private-identifier column occupancy,
box, notes, and archival location. Pages 396, 397, and 398 retain their earlier
authoritative corrected decisions for the Alfred Roch, David Rodnick, and
Charlene Roland column shifts. The other seven pages match the current
extraction. This adds seven pages and **322** rows to the complete-page ledger.
Visual review now covers **328/522 pages** and **15,054/23,978 rows**:
**15,022** reviewed rows match the extraction, **32** retain reviewed
corrections, and **8,924** remain for complete visual comparison.

The complete page-305 `James L. Dr. McConaughy` through `Charles H.
McCormick` queue contains **23** people. Its Library of Congress pass saved one
live result for every person and created **11** discovery candidates across
George R. McCone, John W. McConnell, William M. McCormack, and Charles H.
McCormick. All 11 official item contexts were inspected and rejected. They
were different-initial namesakes, an OCR collision between McCone County and
George Conkin, a vessel rather than a person, an exact common-name casualty
listing without a second identifier, or an unrelated postwar item. No
newspaper identity, occupation, affiliation, or employer claim was retained,
and no raw Library of Congress response was stored.

Four official Army bulk candidates were accepted as high-confidence identity
crosswalks. John N. McConnaughe appears as John N. McConnaughey in the Army
file; Robert J. McConnachie's Army name omits the middle initial; Wallack H.
McCord appears as Hallack H. McCord; and William M. McCormack agrees after
normalization of fixed-width `MC CORMACK` spacing. Each match combines a
nonshared protected identifier with strong name agreement. The source
differences are visible and qualified, the indexed display names remain
unchanged, and Army grade and occupation codes were not converted into
employers or immediate affiliations.

The three Alice M. McCool rows remain three separate ambiguous people in the
existing `p305-alice-m-mccool-three-rows-b623` duplicate group. The first row
prints civilian grade CAF-6, while the next two print no grade; none carries a
protected identifier that would justify a merge.

The final 23-person queue state is **20** `in_progress` and three
`needs_identity_review`. It contains four `high_confidence`, three `ambiguous`,
and 16 unresolved identities. All 23 people have a saved Library of Congress
attempt; all 11 newspaper candidates and all four newly reviewed Army
candidates have explicit decisions. This is research-attempt progress, not
completion of the minimum research protocol.

At this checkpoint, **23,978/23,978** printed rows link to **23,939** active
person entities. Research-attempt coverage is **7,652/23,939 (31.9646%)**;
confirmed/high verified-employer coverage is **280/23,939 (1.1696%)**;
confirmed/high verified-affiliation coverage is **628/23,939 (2.6233%)**;
archival-review disposition coverage is **6,300/23,939 (26.3169%)**. There are
**16,271** `not_started` people, **488** active possible-duplicate groups, and
**159** active people with conflicting identity or source status. The database
stores **12,722** attempts or plans and **4,917** claims: **1,311** confirmed,
**1,912** high, **1,374** medium, **187** low, and **133** conflicting. It
contains **5,054** source/citation records and **2,378** unique document keys.
The public projection contains **2,224** affiliations, **708** organizations,
**3,847** sources, and **4,726** claims. The oil-company category remains a
supported, incomplete evidence set of **seven** people across nine companies.
Full-index historical research is unfinished.

## Replay and continuation

After importing prior durable batches into private SQLite:

```sh
python3 -m oss_research import-page-reviews research/parser_visual_review_pages391-400_2026-09-22.json
python3 -m oss_research import-review-decisions research/loc_review_decisions_2026-09-22_batch632.csv
python3 -m oss_research import-review-decisions research/identity_review_decisions_2026-09-22_batch632.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page305-mcconaughy-mccormick-review_batch-632_2026-09-22.json
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
```

Continue with the next bounded research and visual-audit batch, then rebuild:

```sh
python3 -m oss_research export-adapter-checkpoints
python3 -m oss_research export-derived
python3 -m oss_research build-public-data
python3 -m oss_research coverage-report
```

No API key, full service number, raw API response, or private reviewer note is
committed or included in the public site. No authenticated NARA Catalog request
was made.
