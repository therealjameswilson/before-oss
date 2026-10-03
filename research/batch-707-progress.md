# Batch 707: Noel-Norberg research

Batch 707 covers PDF page 343, row 46, and page 344, rows 1-22, from
**Joseph L Noel** through **Charles R Norberg**. Fresh 300-dpi visual inspection
confirmed all 23 printed rows, representing 23 active person entities. The
immutable extraction is unchanged. The visual source reads Paul F Nolan's
identifier as 1175263; an NARA web extraction that transposes two digits is not
used to overwrite the PDF record.

Six people are high-confidence identity matches through exact indexed names and
nonshared protected identifiers in official Army evidence: **Joe P Nogay**,
**Joseph Noia**, **Loren A Nolan**, **Richard G Nolan**, **Thomas A Nolan**, and
**Orestes M Nomico**. An OSS Operational Groups roster independently documents
T/5 Joseph Noia on the Chicago II and Ginny I rosters. These are identity and
wartime-service decisions only; Army coded occupations are not converted into
employer claims.

The rankless, identifier-free **Isamu Noguchi** row remains only a probable
match to the New York sculptor. Institutional evidence documents that man's
prewar self-employment as an artist and sculptor, but it also distinguishes
Noguchi from artists documented as working for the OSS. The public profile
therefore states the identity and occupation conditionally and does not claim
that the famous sculptor served in OSS. **Louis A Nonni** is likewise only a
probable match to the man in the Ritchie Boys roster because that source does
not supply the index rank or identifier.

The rankless **Charles R Norberg** row is a probable match to attorney Charles
Robert Norberg. A Washington Post obituary dates his Philadelphia law practice
before Army Air Forces service, and a biographical directory names his
1939-1942 employer as **Hepburn and Norris**. The site publishes this last
civilian employer only as a visibly qualified, medium-confidence claim. It is
excluded from default verified-employer analytics.

Two protected-identifier leads remain conflicts rather than silent
corrections: **Oscar D Nohowel** versus an official Army spelling of Nohowell,
and **John N Norback** versus an Army record reading Morback. The CIA and
Library of Congress adapters failed closed without producing a usable result.
Exact-name OSS, employment, occupation, institutional, newspaper, obituary,
military, and archival searches were nevertheless reviewed for all 23 people.

The cohort ends with 19 `no_reliable_result_after_protocol`, two
`conflicting_sources`, one `occupation_only_found`, and one
`documented_prewar_employer_found` outcome. Identity statuses are six
`high_confidence`, three `probable`, two `conflicting`, and 12 `unresolved`.
The reviewed bundle imports eight sources, two organizations, two affiliations,
13 claims, 29 claim-source links, 23 person updates, and 23 consolidated
research attempts. Claim decisions comprise six high-confidence, five visibly
qualified medium-confidence, and two conflicting claims. Eight review decisions
are recorded and imported.

Rebuilt coverage is **23,978/23,978** linked source rows and **23,939** active
person entities. Research-attempt coverage is **9,300/23,939 (38.8487%)**;
confirmed/high verified-employer coverage is **320/23,939 (1.3367%)**;
confirmed/high verified-affiliation coverage is **711/23,939 (2.9700%)**;
archival-review disposition coverage is **7,758/23,939 (32.4074%)**. There are
**14,634** `not_started` people, **523** possible-duplicate groups, and **278**
active conflicts. SQLite stores **16,821** attempts or plans and **6,005**
claims: 1,352 confirmed, 2,717 high, 1,486 medium, 196 low, 252 conflicting,
and two unresolved. It contains **5,532** citation records and **2,757** unique
source documents. The public projection contains **2,412** affiliations,
**824** organizations, **4,315** sources, and **5,800** claims. Full-index
historical research remains unfinished.

## Replay and continuation

After importing prior durable batches into private SQLite:

```sh
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
python3 -m oss_research assign-page-batch --batch-name batch-707a --page 343 --first-row 46 --last-row 46
python3 -m oss_research assign-page-batch --batch-name batch-707b --page 344 --first-row 1 --last-row 22
python3 -m oss_research research --source cia --batch batch-707a --max-queries 1
python3 -m oss_research research --source cia --batch batch-707b --max-queries 22
python3 -m oss_research research --source loc --batch batch-707a --max-queries 1
python3 -m oss_research research --source loc --batch batch-707b --max-queries 22
python3 -m oss_research research --source web --batch batch-707a --resume --max-queries 1
python3 -m oss_research research --source web --batch batch-707b --resume --max-queries 22
python3 -m oss_research import-review-decisions research/identity_review_decisions_2026-10-03_batch707.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page343-344-noel-norberg-review_batch-707_2026-10-03.json
python3 -m oss_research export-adapter-checkpoints
python3 -m oss_research export-derived
python3 -m oss_research export-review-queue
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
```

Adapter checkpoints must be imported before final reviewed decisions and
evidence so temporary discovery states cannot supersede reviewed dispositions.
The next research boundary begins at PDF page 344, row 23 (**Willard P
Norberg**).

No API key, full service number, raw Catalog or LoC API response, copyrighted
page image, unrelated Army coded occupation, street address, or private
reviewer note is committed or included in the public site. No authenticated
NARA Catalog API request was made for this batch.
