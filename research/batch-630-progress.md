# Batch 630: PDF pages 371-380 and McCarthy-McClelian research

Original NARA PDF pages **371-380** were rendered at 180 dpi. All **460**
printed rows were compared against the immutable SQLite extraction for row
order, indexed spelling, initials, rank, private-identifier column occupancy,
box, notes, and archival location. Page 372 already had an authoritative
complete-page decision; the other nine pages match the current extraction.
This adds nine pages and **414** rows to the complete-page ledger. Visual
review now covers **314/522 pages** and **14,410/23,978 rows**: **14,378**
reviewed rows match the extraction, **32** retain reviewed corrections, and
**9,568** remain for complete visual comparison.

The complete page-304 `Joseph P. McCarthy` through `Grant S. McClelian` queue
contains **23** people. Its Library of Congress pass completed **23** live
exact-name searches and created **20** discovery candidates. All 20 official
item contexts were inspected. Nineteen candidates were rejected for name,
initial, chronology, geography, or identity-evidence conflicts. A February
1945 newspaper item supplied a probable John W. McClain identity and occupation
lead, but it names no employer and lacks a protected identifier, OSS assignment,
or second independent identity bridge. The related low-confidence identity and
occupation claims and affiliation remain private and are excluded from the
public profile, sources, downloads, and analytics.

Official Army bulk candidates were reviewed separately. Richard D. McCarthy,
Lester K. McClaflin, and William H. McClare now have `high_confidence`
identity crosswalks because the indexed full or normalized name agrees with a
nonshared protected identifier. Army grade and occupation codes were not
treated as employers or immediate pre-OSS affiliations. Rex H. McCauley's
printed identifier points to an Army row naming Lawrence R. Chambers; the
conflict is published as an identity warning and no Army occupation or employer
is attached to McCauley.

Three probable-duplicate clusters remain separate: Edward A. McCaughy and the
two Edward McGaughy rows; Elmer L. McCcollum and Elmer L. McCollum; and Robert
McCay and Robert Mackay. Each cluster preserves the original spellings, ranks,
boxes, and identifier conflicts for archival review. Paul W. McCausland and
Paul W. McClausland also remain separate ambiguous entities rather than being
forced into a duplicate decision.

The final 23-person queue state is **16** `in_progress` and **7**
`needs_identity_review`. It contains three `high_confidence`, one `probable`,
five `ambiguous`, one `conflicting`, and 13 unresolved identities. All 23
people have a saved Library of Congress attempt and all 20 source candidates
have review decisions. This is research-attempt progress, not completion of
the minimum research protocol.

At this checkpoint, **23,978/23,978** printed rows link to **23,939** active
person entities. Research-attempt coverage is **7,607/23,939 (31.7766%)**;
confirmed/high verified-employer coverage is **280/23,939 (1.1696%)**;
confirmed/high verified-affiliation coverage is **628/23,939 (2.6233%)**;
archival-review disposition coverage is **6,300/23,939 (26.3169%)**. There are
**16,311** `not_started` people, **488** active possible-duplicate groups, and
**159** active people with conflicting identity or source status. The database
stores **12,665** attempts or plans and **4,906** claims: **1,311** confirmed,
**1,901** high, **1,374** medium, **187** low, and **133** conflicting. It
contains **5,050** source/citation records and **2,377** unique document keys.
The public projection contains **2,224** affiliations, **708** organizations,
**3,843** sources, and **4,715** claims. The oil-company category remains a
supported, incomplete evidence set of **seven** people across nine companies.
Full-index historical research is unfinished.

## Replay and continuation

After importing prior durable batches into private SQLite:

```sh
python3 -m oss_research import-page-reviews research/parser_visual_review_pages371-380_2026-09-22.json
python3 -m oss_research import-review-decisions research/loc_review_decisions_2026-09-22_batch630.csv
python3 -m oss_research import-review-decisions research/identity_review_decisions_2026-09-22_batch630.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page304-mccarthy-mcclelian-review_batch-630_2026-09-22.json
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
