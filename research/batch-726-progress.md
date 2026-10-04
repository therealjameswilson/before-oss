# Batch 726: Otwell-Owens research

Batch 726 covers PDF page 353, rows 24-46, from **Betty N Otwell** through
**David A Owens**. A 300-dpi visual inspection confirmed all 23 printed rows,
representing 23 active person entities. Embedded text was checked against the
render. Original spelling and uncertainty remain recoverable, including the
printed `Oaul Ouer`, `Adrien Outellett`, Betty Otwell's `aka Pall` note, and
George W Overton's incomplete `files on l` note. Row 26 is in Box 571 at
location 230/86/37/07; the other 22 rows are in Box 579 at location
230/86/38/01. Protected identifiers remain only in the private database.

Seven Army bulk candidates are accepted for identity. **Paul L Otwell**,
**Jose R Oural**, **Stephen Ovary**, **Alvin M Overall**, **Sven Overbo**,
**Auburn E Owen**, and **Charles W Owen** have a nonshared protected-identifier
match and agreeing indexed names. The Army row supplies middle initial I for
Sven Overbo and suffix Jr for Auburn E Owen. These additions are preserved as
documented variants. No Army coded occupation is converted into an occupation
or employer claim.

One protected-identifier result remains conflicting. The Army bulk candidate
for **Carla R Overly** gives the first name Carl, while the index prints Carla.
No Army metadata is transferred, and the conflict remains pending Box 579
review.

**José Ramón Oural López** receives the cohort's one published pre-OSS pathway.
The exact index and Army names plus private identifier confirm identity. A
University of South Florida oral-history record and a digitized 1936 passport
corroborate his full name and migration history, while a historical profile
places him on a solo OSS mission in occupied France in May 1944. The official
Army bulk record dates entry into the Army of the United States as a private to
June 17, 1943. The site therefore publishes documented wartime Army service
before the OSS mission. It does **not** label the Army as an explicitly
immediate predecessor, infer an Army unit, treat Army service as a civilian
employer, convert an occupation code, or reuse Oural's postwar
Sherwin-Williams career as prewar evidence.

Rare-name discovery leads for **Jerome H Ourada** and **Nellie J Overhulser**
remain unaccepted. A Wisconsin veteran-burial result lacks Ourada's protected
identifier and a direct OSS bridge. A 1920 Iowa census teacher entry and 1927
alumni lead for Overhulser are too remote and likewise lack a wartime identity
bridge. **Auburn E Owen** has a plausible 1940 student lead, but the three-year
gap before Army entry prevents it from being labeled his last civilian status.

The CIA and Library of Congress adapters failed closed in bounded attempts,
and the web adapter recorded deterministic query plans before the manual
staged review. No authenticated NARA Catalog request was made because the
local project did not expose a key to this run.

The cohort ends with 15 `requires_archival_review`, six
`no_reliable_result_after_protocol`, one `conflicting_sources`, and one
`occupation_only_found` outcome. Identity statuses are 15 `unresolved`, six
`high_confidence`, one `confirmed`, and one `conflicting`. The reviewed bundle
imports five sources, one reused canonical organization, one affiliation, nine
claims, 22 claim-source links, 23 person updates, and 23 consolidated research
attempts. Seven accepted and one conflicting identity-review decisions are
recorded.

Rebuilt coverage is **23,978/23,978** linked source rows and **23,939** active
person entities. Research-attempt coverage is **9,735/23,939 (40.6659%)**;
confirmed/high verified-employer coverage is **330/23,939 (1.3785%)**;
confirmed/high verified-affiliation coverage is **738/23,939 (3.0828%)**;
archival-review disposition coverage is **8,193/23,939 (34.2245%)**. There
are **14,199** `not_started` people, **523** possible-duplicate groups, and
**317** active conflicts. SQLite stores **17,744** attempts or plans and
**6,247** claims: 1,370 confirmed, 2,880 high, 1,521 medium, 198 low, 276
conflicting, and two unresolved. It contains **5,654** citation records and
**2,851** unique source documents. The public projection contains **2,468**
affiliations, **855** organizations, **4,435** sources, and **6,040** claims.
The oil-company directory remains nine cited people across eleven historically
named companies. Full-index historical research remains unfinished.

## Replay and continuation

After importing prior durable batches into private SQLite:

```sh
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
python3 -m oss_research assign-page-batch --batch-name batch-726 --page 353 --first-row 24 --last-row 46
python3 -m oss_research research --source cia --batch batch-726 --max-queries 23
python3 -m oss_research research --source loc --batch batch-726 --max-queries 23
python3 -m oss_research research --source web --batch batch-726 --resume --max-queries 23 --dry-run
python3 -m oss_research import-review-decisions research/identity_review_decisions_2026-10-04_batch726.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page353-otwell-owens-review_batch-726_2026-10-04.json
python3 -m oss_research export-adapter-checkpoints
python3 -m oss_research export-derived
python3 -m oss_research export-review-queue
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
```

Adapter checkpoints must be imported before final reviewed decisions and
evidence so temporary discovery states cannot supersede reviewed dispositions.
The next research boundary is PDF page 354, rows 1-23, from Emily L Owens
through Don S Packer.

No API key, full service or officer number, raw Catalog or LoC API response,
copyrighted page image, street address, living-relative detail, modern
people-finder record, or private reviewer note is committed or included in the
public site. No authenticated NARA Catalog API request was made for this batch.
