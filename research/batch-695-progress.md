# Batch 695: Nash-Nawrocki research

Batch 695 covers PDF page 337, row 46, and page 338, rows 1-22, from
**Warren E Nash** through **Walter T Nawrocki**. Fresh visual inspection of
both rendered pages confirmed all 23 printed rows. The immutable extraction
remains unchanged.

**Robert R Nathan** is a confirmed identity match. His exact name and
nonshared protected identifier agree between the OSS index and official Army
bulk data, while his edited Truman Library oral history directly supplies the
chronology: he chaired the War Production Board Planning Committee through
May 1943, entered the Army that month, completed basic training, and was then
assigned to OSS. The public profile therefore records the **U.S. Army** as his
immediate pre-OSS military assignment and the **War Production Board Planning
Committee** separately as his last civilian pre-service government
affiliation. The two categories are not conflated.

**Leonard H Nason** is a high-confidence identity match. A contemporary May
13, 1940 TIME article identifies the unusually named writer and Army officer
as **Mutual Broadcasting System's military analyst**; Norwich University
material independently supports his identity and service. Mutual is published
only as documented prewar employment. The reviewed evidence does not establish
that it was his immediate pre-OSS affiliation.

**Malia G Natirbov** remains a probable identity match. A reproduced Department
of State biographical guide expands the rare indexed name to Malia Giurey
Natirbov and documents wartime translator and liaison work plus later CIA
service, but it does not provide the required bridge to an OSS assignment or a
pre-OSS employer. The public profile preserves that qualification and does not
publish an employer.

**Charles J Naura** is a high-confidence match to **Charles J Nuara**. The
index and official Army record share a nonshared protected identifier, and a
36th Infantry Division roster independently supplies the Nuara spelling at the
same Pfc grade. Both spellings remain visible. **Frank Navellou** is
conflicting because the printed protected identifier resolves to Army Private
Kenneth Pulver, a different name and grade. **James K Naughan** is conflicting
because the same protected identifier is also printed for James K Vaughn.
Neither conflict is silently resolved, and neither receives an employer.

Official Army evidence supports high-confidence identity-only decisions for
**Thomas N Nassoor**, **Orlando P Nastri**, **Richard Natali**, **Arthur R
Natho**, **Anthony E Natoli**, **Lambro J Naumoff**, **Santos C Navarro**, and
**Walter T Nawrocki**. Their coded occupations are not converted into employer
claims. **John F Navarro** retains his previously reviewed high-confidence
identity and occupation-only outcome: the accessible evidence describes a New
England restaurateur and a family Boston restaurant, but does not name a
qualifying employer.

The cohort ends with one `verified_employer_found`, one
`documented_prewar_employer_found`, one `occupation_only_found`, two
`conflicting_sources`, and 18 `no_reliable_result_after_protocol` outcomes.
Identity statuses are one `confirmed`, 11 `high_confidence`, one `probable`,
two `conflicting`, and eight `unresolved`. The evidence bundle imports seven
sources, three reused organizations, three affiliations, 17 claims, 36
claim-source links, 23 person updates, and 22 new consolidated research
attempts; John F Navarro's prior attempt remains authoritative. Ten official
identity candidates are accepted and two are recorded as conflicts.

Rebuilt coverage is **23,978/23,978** linked source rows and **23,939** active
person entities. Research-attempt coverage is **9,029/23,939 (37.7167%)**;
confirmed/high verified-employer coverage is **317/23,939 (1.3242%)**;
confirmed/high verified-affiliation coverage is **700/23,939 (2.9241%)**;
archival-review disposition coverage is **7,486/23,939 (31.2711%)**. There are
**14,905** `not_started` people, **520** possible-duplicate groups, and **261**
active conflicts. SQLite stores **16,233** attempts or plans and **5,842**
claims: 1,343 confirmed, 2,609 high, 1,460 medium, 196 low, and 234
conflicting. It contains **5,445** citation records and **2,686** unique source
documents. The public projection contains **2,376** affiliations, **800**
organizations, **4,228** sources, and **5,639** claims. Full-index historical
research remains unfinished.

## Replay and continuation

After importing prior durable batches into private SQLite:

```sh
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
python3 -m oss_research assign-page-batch --batch-name batch-695-boundary --page 337 --first-row 46 --last-row 46
python3 -m oss_research assign-page-batch --batch-name batch-695 --page 338 --first-row 1 --last-row 22
python3 -m oss_research import-review-decisions research/identity_review_decisions_2026-10-03_batch695.csv
python3 -m oss_research import-reviewed-evidence research/evidence-pages337-338-nash-nawrocki-review_batch-695_2026-10-03.json
python3 -m oss_research export-adapter-checkpoints
python3 -m oss_research export-derived
python3 -m oss_research export-review-queue
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
```

Adapter checkpoints must be imported before final reviewed decisions and
evidence so temporary discovery states cannot supersede reviewed dispositions.
The next research boundary begins at PDF page 338, row 23.

No API key, full service number, raw Catalog API response, copyrighted page
image, unrelated Army coded occupation, street address, or private reviewer
note is committed or included in the public site. No authenticated NARA
Catalog API request was made for this batch.
