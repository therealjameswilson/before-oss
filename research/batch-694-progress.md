# Batch 694: Nakao-Nash research

Batch 694 covers PDF page 337, rows 23-45, from **Errol M Nakao** through
**John S Nash**. Fresh visual inspection of the rendered page confirmed all 23
printed rows, including Edward J Napieralski's service identifier displaced
into the rank/serial boundary. The immutable extraction remains unchanged.

**Ann Nash** has the cohort's verified employer finding. A visually reviewed
November 1, 1943 Cornell Alumni News notice identifies **E. Ann Nash** as a
member of the Vogue staff. A visually reviewed June 15, 1945 notice calls her
a former Vogue editorial assistant and places her with a federal agency in
China. A visually reviewed December 1973 Cornell issue reprints a New York
Times Service profile that identifies **Ann Nash Bottorff**, states that she
worked for Vogue for a year, and explicitly says she returned to China in 1945
as an OSS employee. Vogue is therefore published at high claim confidence as
both her best-supported immediate pre-OSS affiliation and her last named
civilian employer. The temporal basis is `strongly_date_bounded`, not
`explicit_immediate`, because no reviewed source uses the phrase "immediately
before joining OSS." Her role is preserved as **editorial assistant**, the
precise title supplied by the contemporaneous 1945 notice.

**Gust Nanos** is a high-confidence match to **T/5 Gus Nanos** in the OSS
Greek Operational Group VII roster. The uncommon surname, transparent
Gust/Gus variant, identical grade, and direct OSS context agree. The roster
corroborates identity and service only; it does not establish a pre-OSS
employer.

Official Army bulk data supports high-confidence identities for **Errol M
Nakao**, **Joe H Nakata**, **Peter T Namkoong**, **Edward J Napieralski**,
**John B Napoles**, **Ralph R Napolitano**, **Dino Nardi**, **Joseph J
Nardi**, **Warren L Nardin**, **Boleslaus V Narewski**, and **John S Nash**.
Each match has exact-name and nonshared protected-identifier agreement. The
reviews accept identity only and do not turn Army civilian-occupation codes
into employers.

**George K Nakashima** remains unresolved; search results for the prominent
architect and other namesakes lack an OSS and identifier bridge. **A
Napombejara** remains unresolved because the index supplies only an initial;
a postwar Cornell directory entry for Charuchai Napombejara has a different
initial and no OSS bridge. **Chok Naranong** also remains unresolved after an
adapted foreign-name and transliteration protocol. Common-name results for
**Charles P Nash**, **Herman T Nash**, and Colonel **John Nash** did not meet
the required disambiguation standard. These and other rejected namesakes are
recorded rather than silently selected.

The cohort ends with 22 `no_reliable_result_after_protocol` outcomes and one
`verified_employer_found` outcome. Identity statuses are 13
`high_confidence` and ten `unresolved`. The evidence bundle imports six
sources, one organization, one affiliation, 15 claims, 33 claim-source links,
23 person updates, and 23 consolidated research attempts. Eleven official
Army identity candidates are accepted.

Rebuilt coverage is **23,978/23,978** linked source rows and **23,939** active
person entities. Research-attempt coverage is **9,007/23,939 (37.6248%)**;
confirmed/high verified-employer coverage is **316/23,939 (1.3200%)**;
confirmed/high verified-affiliation coverage is **698/23,939 (2.9157%)**;
archival-review disposition coverage is **7,464/23,939 (31.1792%)**. There are
**14,927** `not_started` people, **519** possible-duplicate groups, and **259**
active conflicts. SQLite stores **16,211** attempts or plans and **5,825**
claims: 1,340 confirmed, 2,598 high, 1,459 medium, 196 low, and 232
conflicting. It contains **5,438** citation records and **2,680** unique source
documents. The public projection contains **2,373** affiliations, **800**
organizations, **4,221** sources, and **5,622** claims. Full-index historical
research remains unfinished.

## Replay and continuation

After importing prior durable batches into private SQLite:

```sh
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
python3 -m oss_research assign-page-batch --batch-name batch-694 --page 337 --first-row 23 --last-row 45
python3 -m oss_research import-review-decisions research/identity_review_decisions_2026-10-03_batch694.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page337-nakao-nash-review_batch-694_2026-10-03.json
python3 -m oss_research export-adapter-checkpoints
python3 -m oss_research export-derived
python3 -m oss_research export-review-queue
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
```

Adapter checkpoints must be imported before final reviewed decisions and
evidence so temporary discovery states cannot supersede reviewed dispositions.

No API key, full service number, raw Catalog API response, copyrighted page
image, unrelated Army coded occupation, street address, or private reviewer
note is committed or included in the public site. No authenticated NARA Catalog
API request was made for this batch.
