# Batch 723: Ormond-Orth research

Batch 723 covers PDF page 352, rows 1-23, from **Rudolph P Ormond** through
**Theodore P Orth**. A 300-dpi visual inspection confirmed all 23 printed rows,
representing 23 active person entities. Embedded text was checked against the
render. Original spelling and uncertainty remain recoverable, including the
index forms `Orourke`, `Orocchi`, and `Orroch`; R D Orr's initials-only entry;
and Regenia A Orr's incomplete `aka Edw` note. Rows 1-15 are in Box 576 and
rows 16-23 are in Box 577; all use location 230/86/38/01.

Four Army bulk candidates are accepted for identity only. **Louis Oros**,
**Harold R Orr**, **Robert L Ort**, and **Theodore P Orth** have exact or
compatible indexed-name and nonshared protected-identifier agreement. The
Army record supplies the compatible fuller form **Harold R Orr Jr**. No Army
coded occupation was converted into an occupation or employer claim.

Four protected-identifier results remain conflicting. The Army bulk rows for
**Paul E Orr** and **Leo J Ortego** point to different names, so no metadata is
transferred. **Theresa Orocchi** and **Theresa A Orroch** share a protected
identifier despite different indexed surnames, grades, and boxes. They remain
separate entities in a visible possible-duplicate group pending review of both
files.

Three profiles receive substantive identity or pre-OSS evidence:

* **Jacob Ornstein** is confirmed by the rare exact name, doctoral title,
  linguist role, a 1942 professional listing, and an official account of his
  September 1942 civilian OSS employment. The professional listing places him
  at Washington University in St. Louis as an instructor in Spanish and
  Portuguese. The site therefore publishes Washington University as his
  high-confidence, strongly date-bounded immediate affiliation and last
  civilian employer, while noting that neither source literally says he left
  the university to join OSS.
* **Clifford Orourke** is confirmed as Second Lieutenant **Clifford H.
  O'Rourke** by exact private officer-identifier, name, and rank agreement in
  official records. A declassified OSS board report explicitly says he was
  assigned to OSS on January 15, 1944, from a Replacement Center in Cairo.
  This is published as a military assignment, not a civilian employer. His
  civilian-employment question remains open for archival review.
* **Laszlo Ormos** is a probable identity match to the uncommon exact-name
  documentary-film director documented in a 1937 institutional biography.
  The site publishes only a medium-confidence qualified occupation. The source
  names no employer and provides no direct OSS bridge, so the occupation is
  not presented as immediate.

All other exact-name, variant, OSS, employment, occupation, obituary,
institutional, newspaper, directory, military, and archival searches were
reviewed conservatively. A William E Orser Jr obituary was rejected because it
did not bridge the namesake to the index record. A Blackland Army classbook
lead for Theresa Orocchi was retained only as rejected discovery because the
page-level identity bridge was not sufficiently verified. The CIA and Library
of Congress adapters failed closed in bounded attempts, and the web adapter
recorded deterministic query plans without making an authenticated NARA
Catalog request.

The cohort ends with 13 `requires_archival_review`, four
`no_reliable_result_after_protocol`, four `conflicting_sources`, one
`occupation_only_found`, and one `verified_employer_found` outcome. Identity
statuses are 12 `unresolved`, four `high_confidence`, four `conflicting`, two
`confirmed`, and one `probable`. The reviewed bundle imports six sources, two
organizations, three affiliations, 15 claims, 27 claim-source links, 23 person
updates, and 23 consolidated research attempts. Four accepted and four
conflicting identity-review decisions are recorded.

Rebuilt coverage is **23,978/23,978** linked source rows and **23,939** active
person entities. Research-attempt coverage is **9,667/23,939 (40.3818%)**;
confirmed/high verified-employer coverage is **329/23,939 (1.3743%)**;
confirmed/high verified-affiliation coverage is **734/23,939 (3.0661%)**;
archival-review disposition coverage is **8,125/23,939 (33.9404%)**. There
are **14,267** `not_started` people, **523** possible-duplicate groups, and
**312** active conflicts. SQLite stores **17,600** attempts or plans and
**6,216** claims: 1,362 confirmed, 2,864 high, 1,519 medium, 198 low, 271
conflicting, and two unresolved. It contains **5,637** citation records and
**2,839** unique source documents. The public projection contains **2,462**
affiliations, **853** organizations, **4,418** sources, and **6,009** claims.
Full-index historical research remains unfinished.

## Replay and continuation

After importing prior durable batches into private SQLite:

```sh
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
python3 -m oss_research assign-page-batch --batch-name batch-723 --page 352 --first-row 1 --last-row 23
python3 -m oss_research research --source cia --batch batch-723 --max-queries 23
python3 -m oss_research research --source loc --batch batch-723 --max-queries 23
python3 -m oss_research research --source web --batch batch-723 --resume --max-queries 23 --dry-run
python3 -m oss_research import-review-decisions research/identity_review_decisions_2026-10-04_batch723.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page352-ormond-orth-review_batch-723_2026-10-04.json
python3 -m oss_research export-adapter-checkpoints
python3 -m oss_research export-derived
python3 -m oss_research export-review-queue
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
```

Adapter checkpoints must be imported before final reviewed decisions and
evidence so temporary discovery states cannot supersede reviewed dispositions.
The next research boundary begins at PDF page 352, row 24.

No API key, full service or officer number, raw Catalog or LoC API response,
copyrighted page image, street address, modern people-finder record, or private
reviewer note is committed or included in the public site. No authenticated
NARA Catalog API request was made for this batch.
