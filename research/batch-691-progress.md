# Batch 691: Mussaeus-Myers research

Batch 691 covers PDF page 335, row 46, and page 336, rows 1-22, from
`William T Mussaeus` through `Hugh H Myers`. Fresh visual inspection confirmed
all 23 printed rows. The audit preserves the literal indexed form
`Derrecalde J Muthular`, the truncated notes `file conta` and `folder for`, the
double-u spelling `Lawrence Muurphy`, and the `RA` prefix in that person's
identifier field without treating it as a rank.

**Louis Muti** is confirmed through exact name, corporal grade, and nonshared
protected-identifier agreement among the index, an official Army bulk record,
and a 1944 OSS board report. The board says he entered the Army in August 1943
and then volunteered for OSS special-operations work. The Army is therefore
published as his explicit immediate pre-OSS military affiliation. No civilian
employer is inferred. Louis and the adjacent **Luigi Muti** remain separate
entities in visible possible-duplicate group `p336-louis-luigi-muti-b691`;
Luigi remains ambiguous pending comparison of both Box 548 files.

**Derrecalde J Muthular** is confirmed as Jean-Maurice Muthular d'Errecalde.
A NARA-released 1943 Army order matches the private identifier and full-name
components, while a detailed institutional biography explicitly states that
OSS recruited the U.S. Army infantry lieutenant. That Army assignment is
published as the immediate predecessor. The same biography describes him in
1935 as a director of litigation or legal affairs, but names no employer and
does not establish that occupation as his final civilian role. It therefore
remains a separate documented prewar occupation claim, not an employer.

**Alexander A Muzzey** is a high-confidence match to FBI Special Agent
Alexander A. Muzzey. A contemporary former-agents directory gives service
dates of 1934-45, and an official FBI operational report places Agent Muzzey on
duty in January 1935. The FBI is published only as earlier documented prewar
government service: the date range overlaps the OSS years and does not prove
an immediate transfer.

Official Army bulk data also supports high-confidence identities for
**Nicholas J Muza**, **John C Myer**, **Edwin G Myers**, and **Gerry R Myers**
without turning coded occupations into employers. The protected identifier for
**Frank G Myers** instead points to a malformed row with a nonmatching name and
invalid-looking date and grade fields. That candidate remains an explicit
conflict until the original record and Box 548 jacket can be compared.

Targeted research rejected attractive same-name architect, military, academic,
and institutional candidates for Robert H Mutrux, Chester L Myers, Earl A
Myers, and other common names because the sources lacked a protected
identifier, OSS bridge, or sufficient corroborating facts. Negative online
results are not represented as proof that prior employment did not exist.

The cohort ends with 18 `no_reliable_result_after_protocol`, one
`needs_identity_review`, one `conflicting_sources`, one `completed`, one
`occupation_only_found`, and one `documented_prewar_employer_found` outcome.
Identity statuses are two `confirmed`, five `high_confidence`, one
`ambiguous`, one `conflicting`, and 14 `unresolved`. The evidence bundle
imports seven sources, three affiliations, 32 claims, 50 claim-source links, 23
person updates, and 23 consolidated research attempts. Six official Army
candidate decisions are preserved separately.

Rebuilt coverage is **23,978/23,978** linked source rows and **23,939** active
person entities. Research-attempt coverage is **8,938/23,939 (37.3366%)**;
confirmed/high verified-employer coverage is **312/23,939 (1.3033%)**;
confirmed/high verified-affiliation coverage is **692/23,939 (2.8907%)**;
archival-review disposition coverage is **7,395/23,939 (30.8910%)**. There are
**14,996** `not_started` people, **519** possible-duplicate groups, and **254**
active conflicts. SQLite stores **16,096** attempts or plans and **5,756**
claims: 1,340 confirmed, 2,535 high, 1,458 medium, 196 low, and 227 conflicting.
It contains **5,417** citation records and **2,663** unique source documents.
The public projection contains **2,364** affiliations, **791** organizations,
**4,200** sources, and **5,553** claims. The featured oil-company category
remains **nine people across 11 historically named companies**. Full-index
historical research remains unfinished.

## Replay and continuation

After importing prior durable batches into private SQLite:

```sh
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
python3 -m oss_research import-review-decisions research/identity_review_decisions_2026-10-02_batch691.csv
python3 -m oss_research import-reviewed-evidence research/evidence-pages335-336-mussaeus-myers-review_batch-691_2026-10-02.json
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
note is committed or included in the public site. No authenticated NARA
Catalog API request was made for this batch.
