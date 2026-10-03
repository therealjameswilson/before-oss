# Batch 687: Mullen-Mundy research

Batch 687 covers PDF page 334, rows 1-23, from `Edward P Mullen` through
`Roy L Mundy`. Fresh visual inspection and layout-text comparison confirmed
all 23 printed rows. Every source row remains linked to its own person entity,
and the original index spelling remains recoverable.

Official Army data supports high-confidence identities for **Patrick A.
Mullen, Bennie Mullins, and Joseph E. Mulroy**. Exact names and nonshared
protected identifiers support the matches, but coded Army occupations are not
converted into employers. The protected identifier attached to **Edward P.
Mullen** instead appears with official Army name Edward B. Mullen; that
middle-initial conflict remains explicit. The adjacent **Gerhardt H.
Mundinger** and **Robert G. Mundinger** rows remain separate people despite
sharing a protected identifier.

The distinctive **Lewis Mumford** row is a high-confidence identity match to
the writer documented among the OSS Presentation Division designers. The New
Yorker employed him from 1931, but Stanford faculty work began in 1942 and the
chronology overlaps. The site therefore publishes The New Yorker only as
`documented_prewar`, not as his immediate pre-OSS affiliation or last civilian
employer.

Danish biographical and national-museum sources establish **Hans Ebbe Munck**
as the indexed Ebbe Munck and document his work for Berlingske Tidende from
1929, including as Stockholm correspondent from 1940. Berlingske is published
as his strongly date-bounded last named civilian employer before and during
his early wartime intelligence work. The evidence does not date or define a
formal OSS appointment, so the newspaper is not labeled his immediate pre-OSS
affiliation.

Official Army special-operations history identifies **Van I. Mumma** as
Captain Van Mumma of OSS SO Team YIELD in Thailand in August 1945. That source
supports identity and OSS context only; Team YIELD is not transformed into a
predecessor employer. A 1946 Congressional Record list makes **Eugene G.
Mulling, Junior** a probable identity, but the absent protected-identifier
bridge prevents a stronger assessment. A famous Walther von Mumm biography
and multiple Thomas P. Mulvey service candidates were rejected because they
lacked an adequate bridge to these index rows.

The cohort ends with 18 `no_reliable_result_after_protocol`, three
`conflicting_sources`, one `documented_prewar_employer_found`, and one
`verified_employer_found` outcome. Identity statuses are six
`high_confidence`, one `probable`, three `conflicting`, and 13 `unresolved`.
No negative online result is represented as proof that prior employment did
not exist; unresolved questions route to the indexed Box 545 personnel files.

The evidence bundle imports nine sources, two organizations, two
affiliations, 35 claims, 52 claim-source links, 23 person updates, and 23
consolidated research attempts. Six reviewed Army candidate decisions are
preserved separately: three accepted identity matches and three conflicts.

Rebuilt coverage is **23,978/23,978** linked source rows and **23,939** active
person entities. Research-attempt coverage is **8,850/23,939 (36.9690%)**;
confirmed/high verified-employer coverage is **310/23,939 (1.2950%)**;
confirmed/high verified-affiliation coverage is **687/23,939 (2.8698%)**;
archival-review disposition coverage is **7,307/23,939 (30.5234%)**. There are
**15,084** `not_started` people, **515** possible-duplicate groups, and **249**
active conflicts. SQLite stores **16,008** attempts or plans and **5,638**
claims: 1,336 confirmed, 2,428 high, 1,456 medium, 196 low, and 222
conflicting. It contains **5,399** citation records and **2,649** unique source
documents. The public projection contains **2,358** affiliations, **790**
organizations, **4,182** sources, and **5,435** claims. The featured oil-company
category remains **nine people across 11 historically named companies**.
Full-index historical research remains unfinished.

## Replay and continuation

After importing prior durable batches into private SQLite:

```sh
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
python3 -m oss_research import-review-decisions research/identity_review_decisions_2026-10-01_batch687.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page334-mullen-mundy-review_batch-687_2026-10-01.json
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
or included in the public site.
