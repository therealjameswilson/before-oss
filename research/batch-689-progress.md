# Batch 689: Murphy-Murray research

Batch 689 covers PDF page 335, rows 1-23, from `Daniel E Murphy` through
`Harry A Murray`. Fresh visual inspection confirmed all 23 printed rows. The
audit preserves Ione M Murphy's literal truncated note `also AS` and Albert E
Murray's literal truncated note `Refer to`; neither note is silently expanded.
Every source row remains linked to its own person entity, and the original
index spelling remains recoverable.

Official Army bulk data supports high-confidence identities for **Joseph
Murphy** (with the documented variant Joseph E Murphy), **Rex R Murphy**,
**Thomas R Murphy**, **Warren G Murphy**, **Emmett L Murray**, and **Harry A
Murray** through name and nonshared protected-identifier agreement. Those
matches establish identity only. Army coded occupations are not converted into
named employers or immediate pre-OSS affiliations.

**Albert E Murray** retains an explicit identity conflict. One Army bulk record
agrees on the exact name and protected identifier; a second malformed bulk
record carries the same identifier with an unrelated-looking name string and
invalid-looking coded fields. Both records remain visible in the review trail,
and the printed `Refer to` note remains incomplete. No record is silently
discarded, corrected, or promoted to employer evidence.

**James R Murphy** is a high-confidence match to James Russell Murphy. The
exact middle-initial name and indexed CAF-15 grade align with an official
counterintelligence history that names James R. Murphy as OSS X-2 chief and a
Washington Post obituary that describes his COI and OSS leadership. The
obituary explicitly says that after earning his law degree in 1931 he spent
the next ten years in private practice in Washington, then joined Donovan's
COI in spring 1941. The project therefore publishes **Self-employed legal
practice** as both his immediate pre-COI/OSS affiliation and his last civilian
employer before wartime service. The law firm named at his death is postwar and
is not projected backward.

Targeted research rejected several superficially attractive leads: modern
Daniel E Murphy professional results, same-name James H Murphy military and
grave records, an unbridged Second Lieutenant Joseph Murphy finding-aid lead,
Warren G Murphy burial leads, Emmett L Murray cemetery and directory results,
and psychologist Henry "Harry" Murray. Each lacked the identifiers and
chronology needed to support the indexed person or a pre-OSS employer.

The cohort ends with 21 `no_reliable_result_after_protocol`, one
`conflicting_sources`, and one `verified_employer_found` outcome. Identity
statuses are seven `high_confidence`, one `conflicting`, and 15 `unresolved`.
No negative online result is represented as proof that prior employment did
not exist; unresolved questions route to the indexed Boxes 546-547 personnel
jackets and relevant original service records.

The evidence bundle imports four sources, one normalized organization, one
affiliation, 31 claims, 41 claim-source links, 23 person updates, and 23
consolidated research attempts. Eight reviewed candidate decisions are
preserved separately: six accepted identity matches and two conflict decisions
for Albert E Murray's competing Army records.

Rebuilt coverage is **23,978/23,978** linked source rows and **23,939** active
person entities. Research-attempt coverage is **8,896/23,939 (37.1611%)**;
confirmed/high verified-employer coverage is **311/23,939 (1.2991%)**;
confirmed/high verified-affiliation coverage is **688/23,939 (2.8740%)**;
archival-review disposition coverage is **7,353/23,939 (30.7156%)**. There are
**15,038** `not_started` people, **518** possible-duplicate groups, and **253**
active conflicts. SQLite stores **16,054** attempts or plans and **5,697**
claims: 1,336 confirmed, 2,483 high, 1,456 medium, 196 low, and 226
conflicting. It contains **5,405** citation records and **2,653** unique source
documents. The public projection contains **2,359** affiliations, **790**
organizations, **4,188** sources, and **5,494** claims. The featured oil-
company category remains **nine people across 11 historically named
companies**. Full-index historical research remains unfinished.

## Replay and continuation

After importing prior durable batches into private SQLite:

```sh
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
python3 -m oss_research import-review-decisions research/identity_review_decisions_2026-10-02_batch689.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page335-murphy-murray-review_batch-689_2026-10-02.json
python3 -m oss_research export-adapter-checkpoints
python3 -m oss_research export-derived
python3 -m oss_research export-review-queue
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
```

Adapter checkpoints must be imported before final reviewed decisions and
evidence so temporary discovery states cannot supersede reviewed dispositions.

No API key, full service number, raw Catalog API response, copyrighted page
image, unrelated Army coded occupation, or private reviewer note is committed
or included in the public site. No authenticated NARA Catalog API request was
made for this batch.
