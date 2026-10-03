# Batch 690: Murray-Musolin research

Batch 690 covers PDF page 335, rows 24-45, from `Helen J Murray` through
`George S Musolin`. Fresh visual inspection confirmed all 22 printed rows.
The audit preserves William S Murray's literal truncated note `possibly`, the
printed spelling `Lirving D Musgrove`, and two identical Walter W Muselin
rows. Those two rows remain immutable source records linked to one cautious
person entity; no printed row was discarded.

The cohort contains 21 active person entities. Henry A Murray and George S
Musolin already had reviewed evidence and were deliberately left unchanged.
Henry retains his high-confidence Harvard Psychological Clinic and U.S. Army
affiliations. George retains the confirmed Musolin/Musulin identity, his
immediate Army assignment, University of Pittsburgh student relationship, and
separately documented pre-Army professional-football occupation.

Official Army bulk data supports high-confidence identities for **James W
Murray**, **John M Murray**, **Robert A Murray**, **Shady Murray**, **Walter W
Muselin**, and **Lawrence A Musella** through exact-name and nonshared
protected-identifier agreement. James W Murray also gains the source-supported
`Jr.` variant. Seven accepted candidate decisions are retained because both
printed Walter W Muselin rows point to the same official Army record. These
decisions establish identity only; Army coded occupations are not converted
into named employers or immediate pre-OSS affiliations.

**Percy L Muschamp** is a probable match to Percy Lawrence Herbert Muschamp.
Dalhousie University's 1929 yearbook says that he taught French and German at
Halifax Academy while continuing his language studies. The site publishes
this only as a medium-confidence, visibly qualified earlier prewar employment
claim. It is not marked immediate or last civilian employment. A Dalhousie
alumni directory associates him with Yale University but does not state the
relationship type, so Yale is not modeled as an employer, student
relationship, or other affiliation.

**Casimer P Musial** is a high-confidence spelling variant of Casimir P.
Musial. An official Michigan Supreme Court opinion says that Musial sold his
grocery in early 1943 while preparing for Army induction and remained in the
Army until December 1945. The unnamed grocery is therefore published as
strongly date-bounded last civilian self-employment before service. It is not
asserted as the immediate predecessor to OSS assignment, and the separate
supermarket acquired in 1946 is not projected backward.

Targeted research rejected superficially attractive leads for Olga Murray,
William S Murray, Rubye Murrell, Lirving/Irving D Musgrove, Lawrence A Musella,
and Sherwood C Murray because the sources lacked the identifiers, chronology,
grade, or OSS bridge required to support the indexed person or a pre-OSS
employer. `Irving D Musgrove` is retained only as an explicit search alias,
not a correction to the printed name.

Among the 19 newly researched people, 17 have
`no_reliable_result_after_protocol`, one has
`documented_prewar_employer_found`, and one has `verified_employer_found`.
Identity statuses are seven `high_confidence`, one `probable`, and 11
`unresolved`. Negative online results are not represented as proof that prior
employment did not exist; unresolved questions route to the indexed Boxes
547-548 personnel jackets and relevant original service records.

The evidence bundle imports five sources, two organization records, two
affiliations, 27 claims, 37 claim-source links, 19 person updates, and 19
consolidated research attempts. Seven accepted identity-review decisions are
preserved separately.

Rebuilt coverage is **23,978/23,978** linked source rows and **23,939** active
person entities. Research-attempt coverage is **8,915/23,939 (37.2405%)**;
confirmed/high verified-employer coverage is **312/23,939 (1.3033%)**;
confirmed/high verified-affiliation coverage is **689/23,939 (2.8781%)**;
archival-review disposition coverage is **7,372/23,939 (30.7949%)**. There are
**15,019** `not_started` people, **518** possible-duplicate groups, and **253**
active conflicts. SQLite stores **16,073** attempts or plans and **5,724**
claims: 1,336 confirmed, 2,508 high, 1,458 medium, 196 low, and 226
conflicting. It contains **5,410** citation records and **2,657** unique source
documents. The public projection contains **2,361** affiliations, **791**
organizations, **4,193** sources, and **5,521** claims. The featured
oil-company category remains **nine people across 11 historically named
companies**. Full-index historical research remains unfinished.

## Replay and continuation

After importing prior durable batches into private SQLite:

```sh
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
python3 -m oss_research import-review-decisions research/identity_review_decisions_2026-10-02_batch690.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page335-murray-musolin-review_batch-690_2026-10-02.json
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
