# Batch 657: Mierzejewski-Milbauer research

The PDF-page 319-320 queue from `William S. Mierzejewski` through `Eugene
Milbauer` contains **22 source rows and 22 cautious person entities**. Every
person has a saved, reviewed outcome grounded in the NARA index, official Army
bulk identity comparison where applicable, exact-name OSS and employment
searches, and institutional, newspaper, obituary, genealogy, or archival
checks as applicable. No authenticated NARA Catalog request was made.

The CIA Reading Room adapter stopped at the collection's robots restriction;
that access failure was recorded and was not treated as a negative search
result. The Library of Congress adapter completed all nine page-319 searches
and produced one newspaper candidate. Page-320 LoC requests repeatedly
returned a transient 503 before useful results; alternate institutional,
obituary, directory, cemetery, genealogy, and archival searches were used, and
the unavailable LoC checks were not represented as negative evidence. The one
saved newspaper candidate named a John L. Mihelich on an Ohio claims board in
1939, but it lacked a military, hometown, or other bridge to the indexed OSS
technician and was rejected as an unverified namesake lead.

The reviewed findings preserve identity and evidentiary limits:

- **William S. Mierzejewski** is a high-confidence identity match to the OSS
  staff sergeant identified in an IPN study of 1944 operations in Yugoslavia.
  The operational history does not identify his earlier employer.
- **John L. Mihelich** is confirmed by the NARA index, an official Army bulk
  entry, and a contemporary Detachment 101 order. The separate **Wallace J.
  Mihelich** row repeats the protected identifier but has a different given
  name and grade; official Army and unit evidence points to John. Both Box 523
  files remain separate and require comparison.
- **Rafael P. Miettunen** remains conflicting with `Rafael P. Mettuhen`, whose
  row is in Box 520 and repeats the protected identifier printed for the Box
  522 Miettunen row. Neither spelling or entity is silently preferred.
- **Casimir J. Migon** is supported by an exact official Army match and the
  same contemporary Detachment 101 order. Thirteen other official Army
  crosswalks support identities only. The source's occupation codes are not
  converted into employers.
- `Amelie Migliaccio` and `Huber E. Miglioli` are retained as documented Army
  name variants for the indexed Amelio Migliaccio and Huber E. Migliolo.
- No reliable predecessor employer was found online for anyone in the cohort.
  Each profile states the accessible-source limitation and routes the open
  question to Box 522 or 523; this is not evidence that no prior employment
  existed.

The cohort ends with **20** `requires_archival_review` and two
`conflicting_sources` statuses. Identity statuses are one `confirmed`, 14
`high_confidence`, two `conflicting`, and five `unresolved`. The reviewed
bundle adds **17 identity claims**: one confirmed, 14 high, and two conflicting;
it adds zero employer or affiliation claims and four cited source documents.
All **19** generated candidates received decisions: 14 accepted as identity
evidence, four marked conflicting, and one rejected. Zero candidates remain
unreviewed in the cohort.

A rank-normalization repair now maps printed `T-Sgt`, `S-Sgt`, and `Tec-4`
variants into the existing enlisted-Army taxonomy. Six source rows now
classify correctly; the database refresh changed five person entities because
Paul G. Mihos had already been corrected in the reviewed bundle.

Rebuilt coverage is **23,978/23,978** linked source rows and **23,939** active
person entities. Research-attempt coverage is **8,206/23,939 (34.2788%)**;
confirmed/high verified-employer coverage is **293/23,939 (1.2239%)**;
confirmed/high verified-affiliation coverage is **650/23,939 (2.7152%)**;
archival-review disposition coverage is **6,662/23,939 (27.8291%)**. There are
**15,728** `not_started` people, **497** possible-duplicate groups, and **199**
active conflicts. SQLite stores **14,286** attempts or plans and **5,217**
claims: 1,316 confirmed, 2,122 high, 1,416 medium, 189 low, and 174 conflicting.
It contains **5,188** citation records and **2,481** unique source documents.
The public projection contains **2,282** affiliations, **750** organizations,
**3,978** sources, and **5,024** claims.

The oil-company category remains prominent at the top of the personnel
directory and on its dedicated page. It remains evidence-scoped to **eight
people across ten historically named companies**; no Army identity record in
Batch 657 is misclassified as oil-company employment. Full-index historical
research is unfinished.

## Replay and continuation

After importing prior durable batches into private SQLite:

```sh
python3 -m oss_research import-review-decisions research/identity_review_decisions_2026-09-23_batch657.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page319-320-mierzejewski-milbauer-review_batch-657_2026-09-23.json
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
python3 -m oss_research refresh-classifications
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
