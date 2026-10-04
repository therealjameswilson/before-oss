# Batch 730: Pallen-Palmer research

Batch 730 covers PDF page 355, rows 24-46, from **Leonard M Pallen** through
**Quentin S Palmer**. A 300-dpi visual inspection confirmed all 23 printed
rows, representing 23 active person entities in Boxes 581-582 at locations
230/86/38/01 and 230/86/38/02. Embedded text was checked against the render,
and original spellings, grades, truncated notes, and protected identifiers
remain recoverable in the private database.

Eight people receive high-confidence identity links through exact indexed and
Army names plus nonshared protected identifiers: **Peter D Pallescki**,
**Augustine N Palluccio**, **Arthur E Palmer**, **Glenn E Palmer**, **Henry J
Palmer**, **Howard V Palmer**, **James W Palmer**, and **Quentin S Palmer**.
An OSS Operational Groups roster independently places T/5 Peter D. Pallescki
on the Choctaw mission. These sources establish wartime identity, not pre-OSS
employment, and no Army occupation code is converted into an occupation or
employer claim.

**Carter Palmer** remains conflicting. The indexed protected identifier
retrieves one Army bulk row naming Carter Palmer and another naming Howard R
Krampitz. Both official candidates remain visible, neither is accepted, and
no occupation or employer data are transferred pending Box 582 review.

Two institutional affiliations are published with medium confidence and
visible qualifications. A 1940 University of South Carolina campus newspaper
names Mitchell Palles in a student context. The distinctive name and chronology
support a probable link to **Mitchell D Palles**, but the paper omits the
middle initial and supplies no direct OSS identifier. University of South
Carolina is therefore modeled as documented prewar student status, not
employment and not the immediate pre-OSS affiliation.

A detailed obituary explicitly describes **Hazel Palmer** as recruited by the
OSS and serving in Italy, Austria, and Greece. A Johns Hopkins institutional
record independently dates her Radcliffe College A.B. to 1941. Because the
index supplies neither a middle initial nor a protected identifier for this
common name, the identity and Radcliffe student affiliation remain probable
and medium-confidence. Radcliffe is not labeled an employer. The Museum of
Fine Arts role is excluded from pre-OSS claims because institutional evidence
places it after the war.

The row printed as **\* Palmbaum** remains unresolved and critical for
archival review because the first name is absent and the note is truncated to
`no first n`. The other unresolved common-name and variant-spelling results
remain unpublished rather than being promoted for coverage.

The CIA and Library of Congress adapters failed closed in bounded attempts,
and the web adapter recorded deterministic query plans before manual staged
review. No authenticated NARA Catalog request was made because the local
project did not expose a key to this run.

The cohort ends with one `conflicting_sources`, three
`needs_identity_review`, and 19 `requires_archival_review` outcomes. Identity
statuses are eight `high_confidence`, two `probable`, one `conflicting`, and
12 `unresolved`. The reviewed bundle imports six sources, two organizations,
two affiliations, 13 claims, 27 claim-source links, 23 person updates, and 23
consolidated research attempts. Eight accepted and two conflicting identity
review decisions are recorded.

Rebuilt coverage is **23,978/23,978** linked source rows and **23,939** active
person entities. Research-attempt coverage is **9,826/23,939 (41.0460%)**;
confirmed/high verified-employer coverage is **332/23,939 (1.3869%)**;
confirmed/high verified-affiliation coverage is **741/23,939 (3.0954%)**;
archival-review disposition coverage is **8,284/23,939 (34.6046%)**. There
are **14,108** `not_started` people, **523** possible-duplicate groups, and
**323** active conflicts. SQLite stores **17,936** attempts or plans and
**6,298** claims: 1,373 confirmed, 2,913 high, 1,528 medium, 198 low, 284
conflicting, and two unresolved. It contains **5,679** citation records and
**2,868** unique source documents. The public projection contains **2,477**
affiliations, **860** organizations, **4,460** sources, and **6,091** claims.
Full-index historical research remains unfinished.

## Replay and continuation

After importing prior durable batches into private SQLite:

```sh
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
python3 -m oss_research assign-page-batch --batch-name batch-730 --page 355 --first-row 24 --last-row 46
python3 -m oss_research research --source cia --batch batch-730 --max-queries 23
python3 -m oss_research research --source loc --batch batch-730 --max-queries 23
python3 -m oss_research research --source web --batch batch-730 --resume --max-queries 23 --dry-run
python3 -m oss_research import-review-decisions research/identity_review_decisions_2026-10-04_batch730.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page355-pallen-palmer-review_batch-730_2026-10-04.json
python3 -m oss_research export-adapter-checkpoints
python3 -m oss_research export-derived
python3 -m oss_research export-review-queue
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
```

Adapter checkpoints must be imported before final reviewed decisions and
evidence so temporary discovery states cannot supersede reviewed dispositions.
The next research boundary is PDF page 356, rows 1-23, from Raye Palmer through
Giacomo Panza.

No API key, full service or officer number, raw Catalog or LoC API response,
copyrighted page image, street address, living-relative detail, modern
people-finder record, or private reviewer note is committed or included in the
public site. No authenticated NARA Catalog API request was made for this batch.
