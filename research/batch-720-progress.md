# Batch 720: Omeara-Oneill research

Batch 720 covers PDF page 350, rows 24-46, from **Eugene F Omeara**
through the second indexed **William F Oneill** row. A 300-dpi visual
inspection confirmed all 23 printed rows, representing 23 active person
entities. Embedded text was checked against the render. The immutable
extraction is unchanged: `OnaHary`, `Onativia`, `Oneal`, `Oneil`, and
`Oneill` remain distinct source spellings. Eugene F Omeara, Walter A Omeara,
and Malcolm B Omelia are in Box 573; the remaining 20 rows are in Box 574 at
location 230/86/37/07.

Four Army bulk candidates are accepted for identity only. **Thomas Oneal**,
**Ray B Oneill**, and **Robert G Oneill** have exact printed-name and
nonshared protected-identifier agreement. **Charles K Oneil** has the same
specific identifier as the Army row for Charles K O'Neill, while a Dartmouth
institutional biography independently documents Charles Kendall O'Neill's
wartime OSS service. The public profile preserves both surname spellings.
No Army coded occupation was converted into an occupation or employer claim.

**Alan L Oneill** remains conflicting. His protected identifier reaches an
Army bulk row for Bruce W Johnson, an incompatible name. No Army name,
occupation, or other metadata is transferred; Box 574 review is required.

Three profiles receive substantive, source-level pre-OSS findings:

* **Walter A. O'Meara** is linked at high identity confidence to the
  advertising executive and OSS chief of planning through the Minnesota
  Historical Society finding aid and a reputable obituary. His 1942 return
  to J. Walter Thompson is published as a *probable*, medium-confidence
  immediate pre-OSS employer because the chronology is close but not
  explicit. Earlier high-confidence employment with Benton & Bowles and the
  Duluth News Tribune is kept separate.
* **Charles Kendall O'Neill** has a high-confidence documented prewar
  occupation as a freelance writer of magazine stories and radio scripts.
  Dartmouth does not establish that work as his immediate pre-OSS
  affiliation, so it is not labeled immediate.
* **Dermot Michael "Pat" O'Neill** is a probable, not settled, identity. A
  Washington Post obituary documents earlier Shanghai international-police
  work and a last civilian government assignment as head of security at the
  British Embassy in Tokyo before 1942 Army service. Both affiliations and
  the identity are medium-confidence qualified claims. The profile does not
  call him an OSS operative or infer an immediate OSS relationship from the
  index file.

**Cornelia Rockwell O'Neill** receives a high-confidence identity match from
a detailed obituary documenting OSS training and assignments in London and
Paris, together with the compatible Charles O'Neill relationship. Smith
College and the University of Minnesota are published as medium-confidence
prewar student affiliations, never as employers. The profile still directs
researchers to Box 574 for an immediate pre-OSS employer or status.

The CIA and Library of Congress adapters each made one bounded attempt and
failed closed. The web adapter recorded 23 deterministic planned queries
without making live requests. Manual staged review completed official,
exact-name OSS, employer, occupation, obituary, institutional, newspaper,
directory, military, punctuation-variant, spelling-variant, and archival
search families for every person. Discovery-only, unbridged, and modern
namesakes were rejected rather than converted into claims. A World War I
Medal of Honor namesake for Richard W O'Neill remains rejected pending a
direct bridge to the Box 574 row.

The cohort ends with 15 `requires_archival_review`, three
`no_reliable_result_after_protocol`, two
`documented_prewar_employer_found`, one `occupation_only_found`, one
`completed`, and one `conflicting_sources` outcome. Identity statuses are 15
`unresolved`, six `high_confidence`, one `probable`, and one `conflicting`.
The reviewed bundle imports seven sources, eight organizations, eight
affiliations, 16 claims, 27 claim-source links, 23 person updates, and 23
consolidated research attempts. Four accepted and one conflicting
identity-review decisions are recorded.

Rebuilt coverage is **23,978/23,978** linked source rows and **23,939** active
person entities. Research-attempt coverage is **9,598/23,939 (40.0936%)**;
confirmed/high verified-employer coverage is **328/23,939 (1.3701%)**;
confirmed/high verified-affiliation coverage is **728/23,939 (3.0411%)**;
archival-review disposition coverage is **8,056/23,939 (33.6522%)**. There
are **14,336** `not_started` people, **523** possible-duplicate groups, and
**305** active conflicts. SQLite stores **17,454** attempts or plans and
**6,165** claims: 1,355 confirmed, 2,832 high, 1,514 medium, 198 low, 264
conflicting, and two unresolved. It contains **5,609** citation records and
**2,819** unique source documents. The public projection contains **2,451**
affiliations, **849** organizations, **4,390** sources, and **5,958** claims.
Full-index historical research remains unfinished.

## Replay and continuation

After importing prior durable batches into private SQLite:

```sh
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
python3 -m oss_research assign-page-batch --batch-name batch-720 --page 350 --first-row 24 --last-row 46
python3 -m oss_research research --source cia --batch batch-720 --max-queries 23
python3 -m oss_research research --source loc --batch batch-720 --max-queries 23
python3 -m oss_research research --source web --batch batch-720 --resume --max-queries 23 --dry-run
python3 -m oss_research import-review-decisions research/identity_review_decisions_2026-10-04_batch720.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page350-omeara-oneill-review_batch-720_2026-10-04.json
python3 -m oss_research export-adapter-checkpoints
python3 -m oss_research export-derived
python3 -m oss_research export-review-queue
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
```

Adapter checkpoints must be imported before final reviewed decisions and
evidence so temporary discovery states cannot supersede reviewed
dispositions. The next research boundary begins at PDF page 351, row 1.

No API key, full service or officer number, raw Catalog or LoC API response,
copyrighted page image, unrelated Army coded occupation, street address,
modern people-finder record, or private reviewer note is committed or
included in the public site. No authenticated NARA Catalog API request was
made for this batch.
