# Batch 719: Olson-Omeara research

Batch 719 covers PDF page 350, rows 1-23, from **Curtis Olson** through
**Donn M Omeara**. A 300-dpi visual inspection confirmed all 23 printed rows,
representing 23 active person entities. The immutable extraction is unchanged.
Original spellings, ranks, box numbers, notes, and archival locations remain
recoverable. The first six rows are in Box 572; the remaining 17 rows are in
Box 573 at location 230/86/37/07.

Six people receive accepted identity matches from the official Army bulk
file: **Curtis Olson**, **John P Olson**, **Robert A Olson**, **Harry A
Olwell**, **John M Omalley**, and **Robert C Omalley**. Each match uses the
exact printed name plus a nonshared protected identifier. The identifiers
remain private, and no coded Army occupation was converted into an occupation
or employer claim.

**John E Olson** remains separate from source-derived **John E Olsen** on the
previous page. The same protected identifier is printed on both index rows,
while the Army bulk row uses Olsen. The two profiles remain linked in the
`serial-conflict:13175112` possible-duplicate group. Boxes 572 and 573 must be
compared before any merge or correction.

**Carla A Oman** remains conflicting. Her protected identifier reaches an
Army bulk row for **Carl A Oman**, but the given-name and sex-marker difference
cannot be silently corrected. **Donn M Omeara** also remains conflicting: his
printed identifier reaches an Army bulk row for **Albert L Monett**, an
incompatible name. No Army name, occupation, or other metadata is transferred
in either case; Box 573 review is required.

**Joseph H Omalley** is confirmed as the career Army officer **Joseph Henry
O'Malley** through the exact officer-number bridge, compatible colonel rank,
and name in the War Department's 1945 *Official Army Register*. The register
documents cadet status at the United States Military Academy from July 1929
through June 1933 and a career Army Cavalry path beginning as a second
lieutenant on June 13, 1933. West Point is modeled as student status, not
employment; the Army is modeled as a military assignment, not a civilian
employer. The register does not establish O'Malley's immediate pre-OSS
assignment, so Box 573 remains necessary and no immediate affiliation is
invented.

The CIA and Library of Congress adapters each made one bounded attempt and
failed closed. The web adapter recorded 23 deterministic planned queries
without making live requests. Manual staged review completed official,
exact-name OSS, employment, occupation, obituary, institutional, newspaper,
directory, military, punctuation-variant, spelling-variant, and archival
search families for every person. Discovery-only namesakes—including an
unbridged Ernest Olson obituary and an unrelated Robert O'Malley biography—
were rejected rather than converted into claims.

The cohort ends with 12 `requires_archival_review`, seven
`no_reliable_result_after_protocol`, three `conflicting_sources`, and one
`completed` outcome. Identity statuses are 13 `unresolved`, six
`high_confidence`, two `conflicting`, one `ambiguous`, and one `confirmed`.
The reviewed bundle imports three sources, two organizations, two
affiliations, 12 claims, 22 claim-source links, 23 person updates, and 23
consolidated research attempts. Six accepted and four conflicting
identity-review decisions are recorded.

Rebuilt coverage is **23,978/23,978** linked source rows and **23,939** active
person entities. Research-attempt coverage is **9,575/23,939 (39.9975%)**;
confirmed/high verified-employer coverage is **326/23,939 (1.3618%)**;
confirmed/high verified-affiliation coverage is **726/23,939 (3.0327%)**;
archival-review disposition coverage is **8,033/23,939 (33.5561%)**. There are
**14,359** `not_started` people, **523** possible-duplicate groups, and **304**
active conflicts. SQLite stores **17,406** attempts or plans and **6,149**
claims: 1,355 confirmed, 2,823 high, 1,508 medium, 198 low, 263 conflicting,
and two unresolved. It contains **5,602** citation records and **2,813** unique
source documents. The public projection contains **2,443** affiliations,
**846** organizations, **4,383** sources, and **5,942** claims. Full-index
historical research remains unfinished.

## Replay and continuation

After importing prior durable batches into private SQLite:

```sh
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
python3 -m oss_research assign-page-batch --batch-name batch-719 --page 350 --first-row 1 --last-row 23
python3 -m oss_research research --source cia --batch batch-719 --max-queries 23
python3 -m oss_research research --source loc --batch batch-719 --max-queries 23
python3 -m oss_research research --source web --batch batch-719 --resume --max-queries 23 --dry-run
python3 -m oss_research import-review-decisions research/identity_review_decisions_2026-10-04_batch719.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page350-olson-omeara-review_batch-719_2026-10-04.json
python3 -m oss_research export-adapter-checkpoints
python3 -m oss_research export-derived
python3 -m oss_research export-review-queue
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
```

Adapter checkpoints must be imported before final reviewed decisions and
evidence so temporary discovery states cannot supersede reviewed
dispositions. The next research boundary begins at PDF page 350, row 24.

No API key, full service or officer number, raw Catalog or LoC API response,
copyrighted page image, unrelated Army coded occupation, street address,
modern people-finder record, or private reviewer note is committed or
included in the public site. No authenticated NARA Catalog API request was
made for this batch.
