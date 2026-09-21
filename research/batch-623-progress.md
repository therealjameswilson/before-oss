# Batch 623: PDF pages 301-310 and identity review

Original NARA PDF pages **301-310** were rendered at 180 dpi. All **460**
printed rows were compared against the immutable SQLite extraction for row
order, indexed spelling, initials, rank, private-identifier column occupancy,
box, notes, and archival location. All ten complete pages match the current
extraction. Pages 301-303 and 307 had already received deterministic-random
complete-page review, and page 308 had already passed correction review, so
this replay adds five pages and **230** rows to the complete-page ledger.
Visual review now covers **255/522 pages** and **11,696/23,978 rows**:
**11,664** reviewed rows match the extraction, **32** retain reviewed
corrections, and **12,282** remain for complete visual comparison.

The audit preserves literal anomalies rather than silently correcting them.
Examples include scientific-notation-looking identifier text; unusual and
mixed-case grades; clipped notes; Virgina, Benard, Ivna and Ivan, McCoud and
McCould, McCcollum, McDanile, Lawerence, Hoeph, McGrnahan, and McIninch;
numbers visibly displaced between columns; and repeated or variant rows for
Mauro, Mayer, May, McCarthy, McClenon, McCool, McDougal, McFadden, McGinnis,
McGowan, and others.

Twenty-two bounded queues were assigned for **454** previously unowned people.
The ten pages contain **457** active person entities: page 301 has 45 because
two Joseph P Mauro rows already link to one high-confidence person, and page
308 has 44 because the duplicate Robert D McFadden and Stuart P McFadden pairs
already link to one person each. The two Frederick Mayer entities on page 302
and Donald C McKay on page 310 retain their earlier research ownership and
statuses; Batch 623 deliberately does not overwrite those checkpoints.

The two page-301 Library of Congress passes completed **45** live searches,
producing **48** candidates with zero adapter errors. Every candidate was
inspected in official item-level OCR context. Three failed context lookups
were retried directly: two official item URLs remained 404, and the third
yielded no exact-name OCR context. All 48 candidates were rejected as
surname-only OCR hits, inaccessible pages, distinct namesakes, minimally
identified occurrences, postwar material, or text without a usable exact-name
context. Fourteen affected people remain `in_progress` or move to an identity
review status described below. No employer claim was added and no raw LoC
response was retained.

Eighteen pre-existing official Army bulk candidates for these queues were
also reviewed. Sixteen candidates were accepted as identity-only crosswalks
because full indexed names and nonshared protected identifiers agree. One
Charles Maxwell candidate remains `probable` because the bulk surname is
printed `MAXWELC` and adds a middle initial. One Erwin Mauss candidate is
`conflicting` because the same protected identifier points to the materially
different Army bulk name Stephen Z Krzyzaniak. No Army occupation code was
translated into an employer or immediate affiliation.

Eighteen new same-name, spelling-variant, or protected-identifier groups
covering **38 people** were reviewed without an unsupported merge. They cover:
the two Georges May rows; McAragle / McGaragle; Ward and William McCabe;
McCarary / McCrary; McCargar / McCaroar; two John F McCarthy rows; the
three-row McCaughy / McGaughy cluster; McCausland / McClausland; McCcollum /
McCollum; two Ruth K McClenon rows; three Alice M McCool rows; McCoud /
McCould; Ivna McCrary / Ivan McCray; two Joseph F McCrindle rows; Dervey /
Hervey McDonald; two Robert L McDougal rows; two David K McGinnis rows; and
two John E McGowan rows. The existing Frederick Mayer and Robert Mackay /
McCay reviews remain authoritative, as do the three already-linked exact
duplicate clusters. Public group labels remain non-identifying.

At this checkpoint, **23,978/23,978** printed rows link to **23,939** active
person entities. Research-attempt coverage is **7,467/23,939 (31.1918%)**;
confirmed/high verified-employer coverage is **280/23,939 (1.1696%)**;
confirmed/high verified-affiliation coverage is **628/23,939 (2.6233%)**;
archival-review disposition coverage is **6,298/23,939 (26.3085%)**. There are
**16,436** `not_started` people, **488** active possible-duplicate groups, and
**157** active people with conflicting identity or source status. The database
stores **12,525** attempts or plans and **4,900** claims: **1,311** confirmed,
**1,898** high, **1,374** medium, **185** low, and **132** conflicting. It
contains **5,045** source/citation records and **2,372** unique document keys.
The public projection remains **2,224** affiliations, **708** organizations,
**3,842** sources, and **4,711** claims. The oil-company category remains a
supported, incomplete evidence set of **seven** people across nine companies.
Full-index historical research is unfinished.

## Replay and continuation

After importing the prior durable batches into private SQLite:

```sh
python3 -m oss_research import-page-reviews research/parser_visual_review_pages301-310_2026-09-21.json
python3 -m oss_research import-review-decisions research/loc_review_decisions_2026-09-21_batch623.csv
python3 -m oss_research import-review-decisions research/army_review_decisions_2026-09-21_batch623.csv
python3 -m oss_research import-reviewed-evidence research/evidence-pages301-310-identity-review_batch-623_2026-09-21.json
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
```

Recreate the exact 22 page queues idempotently with these commands:

```sh
python3 -m oss_research assign-page-batch --batch-name page-301-matuszowicz-mautner-b623 --page 301 --first-row 1 --last-row 23
python3 -m oss_research assign-page-batch --batch-name page-301-maves-may-lewis-b623 --page 301 --first-row 24 --last-row 46
python3 -m oss_research assign-page-batch --batch-name page-302-may-philip-mayer-ferdinand-b623 --page 302 --first-row 1 --last-row 11
python3 -m oss_research assign-page-batch --batch-name page-302-mayer-gerald-mayersaks-b623 --page 302 --first-row 14 --last-row 23
python3 -m oss_research assign-page-batch --batch-name page-302-mayes-mazzarini-b623 --page 302 --first-row 24 --last-row 46
python3 -m oss_research assign-page-batch --batch-name page-303-mazzone-mcbride-john-b623 --page 303 --first-row 1 --last-row 23
python3 -m oss_research assign-page-batch --batch-name page-303-mcbride-william-mccann-richard-b623 --page 303 --first-row 24 --last-row 46
python3 -m oss_research assign-page-batch --batch-name page-304-mccann-thomas-mccarthy-john-b623 --page 304 --first-row 1 --last-row 23
python3 -m oss_research assign-page-batch --batch-name page-304-mccarthy-joseph-mcclelian-b623 --page 304 --first-row 24 --last-row 46
python3 -m oss_research assign-page-batch --batch-name page-305-mcclellan-mccollum-oscar-b623 --page 305 --first-row 1 --last-row 23
python3 -m oss_research assign-page-batch --batch-name page-305-mcconaughy-mccormick-charles-b623 --page 305 --first-row 24 --last-row 46
python3 -m oss_research assign-page-batch --batch-name page-306-mccormick-mccracken-b623 --page 306 --first-row 1 --last-row 23
python3 -m oss_research assign-page-batch --batch-name page-306-mccrary-mccutcheon-b623 --page 306 --first-row 24 --last-row 46
python3 -m oss_research assign-page-batch --batch-name page-307-mcdaniel-mcdonald-kenneth-b623 --page 307 --first-row 1 --last-row 23
python3 -m oss_research assign-page-batch --batch-name page-307-mcdonald-mcdowell-b623 --page 307 --first-row 24 --last-row 46
python3 -m oss_research assign-page-batch --batch-name page-308-mcdowell-mcfadden-thomas-b623 --page 308 --first-row 1 --last-row 23
python3 -m oss_research assign-page-batch --batch-name page-308-mcfaddin-mcghee-b623 --page 308 --first-row 24 --last-row 46
python3 -m oss_research assign-page-batch --batch-name page-309-mcgill-mcgovern-b623 --page 309 --first-row 1 --last-row 23
python3 -m oss_research assign-page-batch --batch-name page-309-mcgowan-mcguire-b623 --page 309 --first-row 24 --last-row 46
python3 -m oss_research assign-page-batch --batch-name page-310-mcguire-mcintosh-henry-b623 --page 310 --first-row 1 --last-row 23
python3 -m oss_research assign-page-batch --batch-name page-310-mcintosh-jean-mckay-ann-b623 --page 310 --first-row 24 --last-row 32
python3 -m oss_research assign-page-batch --batch-name page-310-mckay-grace-mckee-b623 --page 310 --first-row 34 --last-row 46
```

The page-301 LoC passes and source decisions are already checkpointed. Continue
with the first unsearched queue, then rebuild all derived outputs:

```sh
python3 -m oss_research research --source loc --batch page-302-may-philip-mayer-ferdinand-b623 --max-queries 11 --resume
python3 -m oss_research export-adapter-checkpoints
python3 -m oss_research export-derived
python3 -m oss_research build-public-data
python3 -m oss_research coverage-report
```

No API key, full service number, raw API response, or private reviewer note is
committed or included in the public site.
