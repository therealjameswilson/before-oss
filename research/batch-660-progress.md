# Batch 660: Miller research

The contiguous queue on PDF page 321 rows 12-33, from `Francis P. Miller`
through `John K. Miller`, contains **22 source rows and 22 cautious person
entities**. Every person has a saved, reviewed outcome grounded in the NARA
index, official Army bulk identity comparison where applicable, exact-name and
rank or grade OSS searches, employment and occupation searches, and
institutional, newspaper, obituary, directory, military-roster, or archival
checks as applicable. No authenticated NARA Catalog request was made.

The page image was visually checked against all 22 stored rows. The review
found that the index prints the uncommon rank abbreviation `Cpt` for James G.
Miller. The parser now preserves `Cpt` in the raw field while normalizing it to
`CAPT` and transparently classifying the row as a commissioned Army officer.
The same conservative rule upgrades the only other `Cpt` row in the index.

The CIA Reading Room request encountered its access restriction and was not
treated as a negative result. The Library of Congress adapter completed two
live queries across three people, checkpointed ten candidates, and recorded
one service error; the candidates and direct LoC pages were then reviewed
manually. The previously exposed NARA API key remains unused and must be
rotated before authenticated Catalog research resumes.

The reviewed findings preserve identity and chronology limits:

- **Lieutenant Colonel Francis P. Miller** is a high-confidence match to
  **Francis Pickens Miller**. The George C. Marshall Foundation finding aid,
  official Virginia House history, Campbell University historical summary,
  and contemporary Library of Congress newspapers provide a coherent
  identity and pre-OSS chronology.
- The best-supported last civilian employer and one immediate pre-OSS
  affiliation for Francis Pickens Miller is the **Council on Foreign
  Relations**, where he served as Organization Director from 1938 through
  1941. This is `strongly_date_bounded`, not promoted to `explicit_immediate`,
  because no reviewed source literally says that OSS recruited him from CFR.
- His simultaneous 1938-1941 service in the **Virginia House of Delegates** is
  modeled separately as a government assignment rather than an employer.
- A brief 1934 teaching role at **Yale Divinity School** and later field work
  for the **Foreign Policy Association** are published as medium-confidence,
  documented-prewar employment. Neither is mislabeled as the immediate
  predecessor.
- Nonshared protected Army matches establish high-confidence identities for
  **Fred L. Miller, Harris Miller, Hasbrouck B. Miller, and Jacob H. Miller**.
  Coded Army occupations are not converted into employer claims.
- **Garth H. Miller** remains conflicting because the official Army entry tied
  to the indexed protected identifier instead names **Andrew J. Shima**. No
  Army occupation or identity evidence is transferred across that mismatch.
- The remaining common-name results lacked enough corroborating identifiers or
  an OSS-to-employer bridge. They remain unresolved and direct researchers to
  the indexed Box 524 or 525 jacket.

The cohort ends with one `verified_employer_found`, one
`conflicting_sources`, and 20 `requires_archival_review` statuses. Identity
statuses are five `high_confidence`, one `conflicting`, and 16 `unresolved`.
The reviewed bundle adds **10 claims**: seven high, two medium, and one
conflicting. It adds four Francis Pickens Miller affiliations. All 15 generated
candidates received decisions: six accepted, one conflicting, and eight
rejected. Zero candidates remain unreviewed in the cohort.

Rebuilt coverage is **23,978/23,978** linked source rows and **23,939** active
person entities. Research-attempt coverage is **8,272/23,939 (34.5545%)**;
confirmed/high verified-employer coverage is **295/23,939 (1.2323%)**;
confirmed/high verified-affiliation coverage is **655/23,939 (2.7361%)**;
archival-review disposition coverage is **6,728/23,939 (28.1048%)**. There are
**15,662** `not_started` people, **501** possible-duplicate groups, and
**203** active conflicts. SQLite stores **14,513** attempts or plans and
**5,255** claims: 1,323 confirmed, 2,147 high, 1,418 medium, 189 low, and 178
conflicting. It contains **5,204** citation records and **2,494** unique source
documents. The public projection contains **2,291** affiliations, **754**
organizations, **3,994** sources, and **5,062** claims.

The oil-company category remains prominent at the top of the personnel
directory and on its dedicated page. It remains evidence-scoped to **eight
people across ten historically named companies**; no Batch 660 identity-only
record is misclassified as oil-company employment. Full-index historical
research is unfinished.

## Replay and continuation

After importing prior durable batches into private SQLite:

```sh
python3 -m oss_research refresh-classifications
python3 -m oss_research import-review-decisions research/identity_review_decisions_2026-09-23_batch660.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page321-miller-review_batch-660_2026-09-23.json
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
```

Continue with the next bounded research batch, then run:

```sh
python3 -m oss_research export-adapter-checkpoints
python3 -m oss_research export-derived
python3 -m oss_research export-review-queue
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
```

No API key, full service number, raw Catalog API response, copyrighted page
image, or private reviewer note is committed or included in the public site.
