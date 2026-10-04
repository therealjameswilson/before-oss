# Batch 722: Orban-Ormiston research

Batch 722 covers PDF page 351, rows 24-46, from **John Orban** through
**David Ormiston**. A 300-dpi visual inspection confirmed all 23 printed rows,
representing 23 active person entities. Embedded text was checked against the
render. The immutable extraction is unchanged: Alekos X Orkoulas's note remains
the unexplained `also AS`; `Pampeil Orlando` and `John Orlowsci` remain the
printed name forms; Joseph S Orlowski's unfamiliar rank remains `Pc`. John
Orban through Joseph Orefice are in Box 575; the remaining rows are in Box 576.
All rows use location 230/86/38/01.

Eight Army bulk candidates are accepted for identity only. **John Orban**,
**Melvin E Orchard**, **Edward Ordynowicz**, **Joseph Orefice**, **Julien A
Orgeron**, **Joseph S Orlowski**, **Jesse M Orme**, and **David Ormiston** have
exact or compatible indexed-name and nonshared protected-identifier agreement.
The Army record supplies the compatible fuller form **David K Ormiston**. No
Army coded occupation was converted into an occupation or employer claim.

Two protected-identifier matches remain conflicting. The Army bulk row renders
**Liberio Orlando** as `ORLANDO LIBORIO` and **John Orlowsci** as `ORLOWSKI
JOHN`. The index spellings remain authoritative for display, no Army metadata
is transferred, and Box 576 review is critical.

Four profiles receive substantive identity or pre-OSS evidence:

* **Joseph J Orlan** is a high-confidence identity. A contemporary 1946
  Ukrainian Weekly memorial identifies Lieutenant Joseph Orlan as an OSS
  communications officer, reports that he volunteered in 1940, and places him
  with the Signal Corps at Pearl Harbor. A signed 1936 contribution says
  amateur radio had become his vocation. Amateur radio is published as a
  medium-confidence documented prewar occupation, and the Signal Corps as a
  high-confidence earlier military assignment. Neither is presented as his
  immediate pre-OSS affiliation, and no civilian employer is invented.
* **Alekos X Orkoulas** is confirmed by a declassified RG 226 roster matching
  his rare exact name, Technician Fifth Grade, and protected identifier. The
  index's incomplete `also AS` note is preserved without expansion. A
  postwar restaurant-owner lead is excluded from pre-OSS analysis.
* **John Orisek** is confirmed by OSS Operational Group Command Special Orders
  No. 9 of 9 May 1945, which matches his exact name, grade, and protected
  identifier. The order proves an OSS assignment, not pre-OSS employment.
* **Peter C Orlich** is linked at high confidence to the Technician Fifth Grade
  radio operator on the OSS Weihsien rescue mission. A direct-witness
  compilation says his family needed him to work rather than attend Columbia,
  but it names neither employer nor occupation, so no affiliation is created.

All other exact-name, variant, OSS, employment, occupation, obituary,
institutional, newspaper, directory, military, and archival searches were
reviewed conservatively. Edward Ordynowicz's later Massachusetts namesake,
Julien Orgeron's burial lead, modern people-finder results, and a different
Edward Orler service record were rejected rather than converted into claims.
The CIA and Library of Congress adapters failed closed in bounded attempts, and
the web adapter recorded deterministic query plans without making an
authenticated NARA Catalog request.

The cohort ends with 12 `requires_archival_review`, eight
`no_reliable_result_after_protocol`, two `conflicting_sources`, and one
`occupation_only_found` outcome. Identity statuses are nine `unresolved`,
ten `high_confidence`, two `confirmed`, and two `conflicting`. The
reviewed bundle imports seven sources, one reused canonical organization, two
affiliations, 16 claims, 30 claim-source links, 23 person updates, and 23
consolidated research attempts. Eight accepted and two conflicting
identity-review decisions are recorded.

Rebuilt coverage is **23,978/23,978** linked source rows and **23,939** active
person entities. Research-attempt coverage is **9,644/23,939 (40.2857%)**;
confirmed/high verified-employer coverage is **328/23,939 (1.3701%)**;
confirmed/high verified-affiliation coverage is **732/23,939 (3.0578%)**;
archival-review disposition coverage is **8,102/23,939 (33.8444%)**. There
are **14,290** `not_started` people, **523** possible-duplicate groups, and
**308** active conflicts. SQLite stores **17,550** attempts or plans and
**6,201** claims: 1,359 confirmed, 2,858 high, 1,517 medium, 198 low, 267
conflicting, and two unresolved. It contains **5,631** citation records and
**2,834** unique source documents. The public projection contains **2,459**
affiliations, **851** organizations, **4,412** sources, and **5,994** claims.
Full-index historical research remains unfinished.

## Replay and continuation

After importing prior durable batches into private SQLite:

```sh
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
python3 -m oss_research assign-page-batch --batch-name batch-722 --page 351 --first-row 24 --last-row 46
python3 -m oss_research research --source cia --batch batch-722 --max-queries 23
python3 -m oss_research research --source loc --batch batch-722 --max-queries 23
python3 -m oss_research research --source web --batch batch-722 --resume --max-queries 23 --dry-run
python3 -m oss_research import-review-decisions research/identity_review_decisions_2026-10-04_batch722.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page351-orban-ormiston-review_batch-722_2026-10-04.json
python3 -m oss_research export-adapter-checkpoints
python3 -m oss_research export-derived
python3 -m oss_research export-review-queue
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
```

Adapter checkpoints must be imported before final reviewed decisions and
evidence so temporary discovery states cannot supersede reviewed dispositions.
The next research boundary begins at PDF page 352, row 1.

No API key, full service or officer number, raw Catalog or LoC API response,
copyrighted page image, street address, modern people-finder record, or private
reviewer note is committed or included in the public site. No authenticated
NARA Catalog API request was made for this batch.
