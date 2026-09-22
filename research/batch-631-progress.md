# Batch 631: PDF pages 381-390 and McClellan-McCollum research

Original NARA PDF pages **381-390** were rendered at 180 dpi. All **460**
printed rows were compared against the immutable SQLite extraction for row
order, indexed spelling, initials, rank, private-identifier column occupancy,
box, notes, and archival location. Pages 381, 387, and 389 retain their earlier
authoritative decisions, including three corrected column-shift rows on pages
387 and 389. The other seven pages match the current extraction. This adds
seven pages and **322** rows to the complete-page ledger. Visual review now
covers **321/522 pages** and **14,732/23,978 rows**: **14,700** reviewed rows
match the extraction, **32** retain reviewed corrections, and **9,246** remain
for complete visual comparison.

The complete page-305 `Margaret J. McClellan` through `Oscar D. McCollum`
queue contains **23** people. Its Library of Congress pass completed **23**
live exact-name searches and created **four** discovery candidates. All four
official item contexts were inspected and rejected. Three John P. McClelland
candidates had conflicting middle initials or unrelated OCR context. The
Russell S. McClure candidate was a postwar article in which Russell and
McClure were separate people. No newspaper identity, occupation, affiliation,
or employer claim was retained, and no raw Library of Congress response was
stored.

Seven official Army bulk candidates were accepted at high confidence. Douglas
T. McClure, Floyd F. McClintock, Harold C. McCollom, Jack M. McClintock, James
I. McCollum, John J. McCole, and Oscar D. McCollum each have normalized
full-name agreement and a nonshared protected-identifier match. The Army
entries add `Jr.` for Harold C. McCollom and Oscar D. McCollum; those forms are
retained as sourced name variants without changing the names printed in the
index. Army grades and occupation codes remain identity context only and were
not converted into employers, immediate affiliations, or civilian roles.

The two adjacent Ruth K. McClenon rows remain separate ambiguous people in the
existing `p305-ruth-k-mcclenon-repeat-b623` duplicate group. The records repeat
the name, civilian grade, and box but supply no protected identifier. Elmer L.
McCollum also remains separate from the page-304 McCcollum spelling variant;
their rank conflict still requires Box 499 review.

The final 23-person queue state is **20** `in_progress` and three
`needs_identity_review`. It contains seven `high_confidence`, three
`ambiguous`, and 13 unresolved identities. All 23 people have a saved Library
of Congress attempt; all four newspaper candidates and all seven newly
reviewed Army candidates have explicit decisions. This is research-attempt
progress, not completion of the minimum research protocol.

At this checkpoint, **23,978/23,978** printed rows link to **23,939** active
person entities. Research-attempt coverage is **7,629/23,939 (31.8685%)**;
confirmed/high verified-employer coverage is **280/23,939 (1.1696%)**;
confirmed/high verified-affiliation coverage is **628/23,939 (2.6233%)**;
archival-review disposition coverage is **6,300/23,939 (26.3169%)**. There are
**16,291** `not_started` people, **488** active possible-duplicate groups, and
**159** active people with conflicting identity or source status. The database
stores **12,695** attempts or plans and **4,913** claims: **1,311** confirmed,
**1,908** high, **1,374** medium, **187** low, and **133** conflicting. It
contains **5,052** source/citation records and **2,377** unique document keys.
The public projection contains **2,224** affiliations, **708** organizations,
**3,845** sources, and **4,722** claims. The oil-company category remains a
supported, incomplete evidence set of **seven** people across nine companies.
Full-index historical research is unfinished.

## Replay and continuation

After importing prior durable batches into private SQLite:

```sh
python3 -m oss_research import-page-reviews research/parser_visual_review_pages381-390_2026-09-22.json
python3 -m oss_research import-review-decisions research/loc_review_decisions_2026-09-22_batch631.csv
python3 -m oss_research import-review-decisions research/identity_review_decisions_2026-09-22_batch631.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page305-mcclellan-mccollum-review_batch-631_2026-09-22.json
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
