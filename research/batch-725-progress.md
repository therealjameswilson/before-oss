# Batch 725: Osterbur-Ottwell research

Batch 725 covers PDF page 353, rows 1-23, from **Robert J Osterbur** through
**Paul O Ottwell**. A 300-dpi visual inspection confirmed all 23 printed rows,
representing 23 active person entities. Embedded text was checked against the
render. Original spelling and uncertainty remain recoverable, including
`Walter S Oswalo`; the incomplete notes `fodler co`, `charge s`, and `folder
se`; and the protected identifiers retained only in the private database.
Rows 1-18 are in Box 578 and rows 19-23 are in Box 579. All use location
230/86/38/01.

Two Army bulk candidates are accepted for identity only. **Robert J
Osterbur** and **Gustav F Osterman** have exact indexed-name and nonshared
protected-identifier agreement. No Army coded occupation was converted into
an occupation or employer claim.

Two protected-identifier results remain conflicting. The Army bulk candidate
for **Raymond R Otake** gives the middle initial K, while the index prints R.
The identifier printed for **Paul O Ottwell** also appears on the index row for
William H Thomas. No mismatched metadata is transferred and the two source
rows are not merged; both conflicts remain pending archival review.

Four profiles receive direct identity or predecessor evidence:

* **Julius Ostroff** is confirmed by an official 1944 OSS Board interview that
  matches his exact name, Navy grade, and protected identifier. His own
  interview identifies his civilian occupation as salesman before entering
  the Navy in February 1942. The site publishes the occupation while leaving
  the employer unnamed and does not claim it was the immediate predecessor to
  either Navy or OSS service.
* **Gjerulf "Gerald" Ottersland** is linked at high confidence through his
  distinctive name, enlisted grade, and OSS/NORSO service. A historical
  account explicitly describes recruitment from the 99th Infantry Battalion
  (Separate) into OSS and says he had worked at an unnamed Brooklyn shipyard
  before enlisting in 1942. Both claims are visibly qualified at medium
  confidence; no shipyard name is guessed.
* **Fred R Ostheimer** is linked at high confidence to an official OSS award
  memorandum naming him in the OSS Mission to France. The record confirms the
  identity but supplies no pre-OSS employment evidence.
* **Roy N Osthus** is linked at high confidence to an official OSS special
  order that matches his name, grade, and protected identifier. It likewise
  supplies no pre-OSS employment evidence.

Unbridged common-name, incomplete-name, and namesake results were rejected.
The CIA and Library of Congress adapters failed closed in bounded attempts,
and the web adapter recorded deterministic query plans without making an
authenticated NARA Catalog request.

The cohort ends with 15 `requires_archival_review`, four
`no_reliable_result_after_protocol`, two `conflicting_sources`, and two
`occupation_only_found` outcomes. Identity statuses are 15 `unresolved`, four
`high_confidence`, two `confirmed`, and two `conflicting`. The reviewed bundle
imports seven sources, one organization, three affiliations, 11 claims, 20
claim-source links, 23 person updates, and 23 consolidated research attempts.
Two accepted and two conflicting identity-review decisions are recorded.

Rebuilt coverage is **23,978/23,978** linked source rows and **23,939** active
person entities. Research-attempt coverage is **9,712/23,939 (40.5698%)**;
confirmed/high verified-employer coverage is **330/23,939 (1.3785%)**;
confirmed/high verified-affiliation coverage is **737/23,939 (3.0787%)**;
archival-review disposition coverage is **8,170/23,939 (34.1284%)**. There
are **14,222** `not_started` people, **523** possible-duplicate groups, and
**316** active conflicts. SQLite stores **17,696** attempts or plans and
**6,238** claims: 1,368 confirmed, 2,874 high, 1,521 medium, 198 low, 275
conflicting, and two unresolved. It contains **5,649** citation records and
**2,847** unique source documents. The public projection contains **2,467**
affiliations, **855** organizations, **4,430** sources, and **6,031** claims.
The oil-company directory remains nine cited people across eleven historically
named companies. Full-index historical research remains unfinished.

## Replay and continuation

After importing prior durable batches into private SQLite:

```sh
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
python3 -m oss_research assign-page-batch --batch-name batch-725 --page 353 --first-row 1 --last-row 23
python3 -m oss_research research --source cia --batch batch-725 --max-queries 23
python3 -m oss_research research --source loc --batch batch-725 --max-queries 23
python3 -m oss_research research --source web --batch batch-725 --resume --max-queries 23 --dry-run
python3 -m oss_research import-review-decisions research/identity_review_decisions_2026-10-04_batch725.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page353-osterbur-ottwell-review_batch-725_2026-10-04.json
python3 -m oss_research export-adapter-checkpoints
python3 -m oss_research export-derived
python3 -m oss_research export-review-queue
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
```

Adapter checkpoints must be imported before final reviewed decisions and
evidence so temporary discovery states cannot supersede reviewed dispositions.
The next research boundary is PDF page 353, rows 24-46.

No API key, full service or officer number, raw Catalog or LoC API response,
copyrighted page image, street address, living-relative detail, modern
people-finder record, or private reviewer note is committed or included in the
public site. No authenticated NARA Catalog API request was made for this batch.
