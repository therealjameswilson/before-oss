# Batch 626: PDF pages 331-340 and completion of the Mayes-Mazzarini queue

Original NARA PDF pages **331-340** were rendered at 180 dpi. All **460**
printed rows were compared against the immutable SQLite extraction for row
order, indexed spelling, initials, rank, private-identifier column occupancy,
box, notes, and archival location. All ten pages match the current extraction.
Pages 336, 337, and 339 already had correction-complete visual review, so this
replay adds seven pages and **322** rows to the complete-page ledger. Visual
review now covers **278/522 pages** and **12,754/23,978 rows**: **12,722**
reviewed rows match the extraction, **32** retain reviewed corrections, and
**11,224** remain for complete visual comparison.

The audit preserves literal anomalies rather than silently correcting them.
Examples include `Chalen`, `McClora`, `Arnando`, `Mourqet`, `Mouinhan`,
`Moussean`, `Moyingan`, `Mrgudic`, `Mroziz`, `Mueke`, `Mukanos`, `Mulloly`,
`Corlyn`, `Avary`, `Murayame`, `Muredon`, `Annel`, `Lirving`, `Muurphy`,
`Derrecalde`, `Muzukauskas`, `Mysberch`, `Nadelhoffer`, `Chaste`, `Kashumi`,
`Napombejara A`, `Naranong Chok`, `Nasht`, `Natirbov`, `Naughan`, `Navellou`,
`Nazzarro`, `Neague`, `Neasse`, `Nefopulas`, `Neimczylc`, `Lenoore`, `Ingolv`,
`Nelson M A`, `Nelson. III`, `Nemekofsky`, `Lubitsa`, and `Nespodzany`;
rank-like values printed in middle-initial cells; a numeric value displaced
into a rank cell; clipped notes; damaged identifiers containing question-mark
characters; repeat names; and mixed archive locations. Private identifiers
are never included in this note or public assets.

The complete page-302 `Mayes` through `Mazzarini` queue contains **23** people.
Its Library of Congress pass completed **23** live exact-name searches and
created **11** discovery candidates. Every candidate was inspected through
official item-level OCR and the bounded full-text fallback. Nine candidates
supplied no usable exact-name context, three postwar hits supplied no usable
context, one context concerned newborn William James Mayhew rather than
indexed Major William A. Mayhew, and one probate notice named Thomas G. Mays
rather than indexed Thomas J. Mays. These categories overlap because the three
postwar hits are among the context-free candidates. All 11 candidates were
rejected. No employer claim was added and no raw Library of Congress response
was retained.

Five pre-existing official Army bulk candidates were accepted as identity-only
crosswalks. John T. Mayher, Alex Mazel, Dana G. Mazerolle, Chester John Mazur,
and Gesualdo J. Mazza agree with the index in name and a nonshared protected
identifier, so their identities are now `high_confidence`. Army grades and
bulk occupation codes were not translated into employers, occupations, or
immediate affiliations. All 23 people remain `in_progress` with saved next
actions; this is research-attempt progress, not completion of the minimum
research protocol.

An exhausted LoC read timeout exposed a batch-control defect: the adapter
correctly retried and audited the request, but the scheduler propagated the
exception as a traceback. The scheduler now saves only the exception class in
an `error` research attempt, keeps the person resumable, stops the bounded run
without probing every remaining person, and never treats the failure as a
negative search result. The original request subsequently succeeded through
the ordinary `--resume` path. Focused scheduler and LoC tests cover the new
behavior.

At this checkpoint, **23,978/23,978** printed rows link to **23,939** active
person entities. Research-attempt coverage is **7,511/23,939 (31.3756%)**;
confirmed/high verified-employer coverage is **280/23,939 (1.1696%)**;
confirmed/high verified-affiliation coverage is **628/23,939 (2.6233%)**;
archival-review disposition coverage is **6,298/23,939 (26.3085%)**. There are
**16,392** `not_started` people, **488** active possible-duplicate groups, and
**157** active people with conflicting identity or source status. The database
stores **12,569** attempts or plans and **4,900** claims: **1,311** confirmed,
**1,898** high, **1,374** medium, **185** low, and **132** conflicting. It
contains **5,045** source/citation records and **2,372** unique document keys.
The public projection remains **2,224** affiliations, **708** organizations,
**3,842** sources, and **4,711** claims. The oil-company category remains a
supported, incomplete evidence set of **seven** people across nine companies.
Full-index historical research is unfinished.

## Replay and continuation

After importing prior durable batches into private SQLite:

```sh
python3 -m oss_research import-page-reviews research/parser_visual_review_pages331-340_2026-09-21.json
python3 -m oss_research import-review-decisions research/loc_review_decisions_2026-09-21_batch626.csv
python3 -m oss_research import-review-decisions research/army_review_decisions_2026-09-21_batch626.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page302-mayes-mayo-identity-review_batch-626_2026-09-21.json
python3 -m oss_research import-review-decisions research/loc_review_decisions_2026-09-21_batch626b.csv
python3 -m oss_research import-review-decisions research/loc_review_decisions_2026-09-21_batch626c.csv
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
```

Continue with the next unsearched queue, then rebuild derived outputs:

```sh
python3 -m oss_research research --source loc --batch page-303-mazzone-mcbride-john-b623 --max-queries 10 --resume
python3 -m oss_research export-adapter-checkpoints
python3 -m oss_research export-derived
python3 -m oss_research build-public-data
python3 -m oss_research coverage-report
```

No API key, full service number, raw API response, or private reviewer note is
committed or included in the public site.
