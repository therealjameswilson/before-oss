# Batch 731: Palmer-Panza research

Batch 731 covers PDF page 356, rows 1-23, from **Raye Palmer** through
**Giacomo Panza**. A 300-dpi visual inspection confirmed all 23 printed rows,
representing 23 active person entities in Boxes 582-583 at locations
230/86/38/02 and 230/86/38/03. Embedded text was checked against the render,
and original spellings, ranks, grades, notes, and protected identifiers remain
recoverable in the private database.

Seven people receive high-confidence identity links through exact indexed and
Army names plus nonshared protected identifiers: **Leo J Pampalone**, **Peter
M Panagakos**, **Sotirios Panagiotareas**, **Anthony Panaro**, **Joseph P
Pando**, **Peter N Panos**, and **Kusa Panyarjun**. An OSS Operational Groups
roster independently places Peter Panagakos in Greek Group VII and Anthony
Panaro on the Peedee mission. These sources establish wartime identity, not
pre-OSS employment, and no Army occupation code is converted into an
occupation or employer claim.

**Guido Pantaleoni** receives a confirmed identity and a high-confidence
employment finding. Official Defense POW/MIA Accounting Agency and American
Battle Monuments Commission records identify the exact OSS officer. A
successor-firm publication by his son documents Pantaleoni as a co-founder and
lawyer at **Reavis & Pantaleoni** from 1935 until he went to war in 1943. That
firm is therefore published as both his strongly date-bounded immediate
pre-OSS affiliation and his last civilian employer. The historical firm name
is preserved, and an offered White & Case partnership is not turned into a
separate employment claim.

**Kusa Panyarjun** receives a high-confidence University of Pennsylvania
student affiliation, not an employer finding. A contemporary 1941 newspaper
caption uses the exact indexed spelling, identifies Bangkok as his home, and
places him among Penn's freshman crew candidates. A University of Pennsylvania
alumni publication corroborates the **Kusa Panyarachun** spelling variant and
degree. The affiliation is classified as documented prewar student status; a
postwar World Travel Service role is excluded.

**Theodore D Palmer Jr.** remains probable. A 1943 War Department memorandum
matches the full name, suffix, rank, and period and identifies him as acting
director of the Army Specialized Training Division. Because the document does
not establish the assignment's sequence relative to OSS service, no immediate
pre-OSS affiliation is published. Hiram C Pamplin, Jack C Pamplin, and Arthur
J Panagiotopoul also remain in identity review. All unresolved common-name and
variant-spelling results remain unpublished rather than being promoted for
coverage.

The CIA adapter failed closed under the source's robots policy, and the Library
of Congress adapter timed out on the first bounded query. The web adapter
recorded 23 deterministic query plans before manual staged review. No
authenticated NARA Catalog request was made because the local project did not
expose a key to this run.

The cohort ends with one `verified_employer_found`, four
`needs_identity_review`, and 18 `requires_archival_review` outcomes. Identity
statuses are one `confirmed`, seven `high_confidence`, one `probable`, and 14
`unresolved`. The reviewed bundle imports nine sources, two organizations, two
affiliations, 11 claims, 28 claim-source links, 23 person updates, and 23
consolidated research attempts. Seven accepted identity review decisions are
recorded.

Rebuilt coverage is **23,978/23,978** linked source rows and **23,939** active
person entities. Research-attempt coverage is **9,849/23,939 (41.1421%)**;
confirmed/high verified-employer coverage is **333/23,939 (1.3910%)**;
confirmed/high verified-affiliation coverage is **743/23,939 (3.1037%)**;
archival-review disposition coverage is **8,307/23,939 (34.7007%)**. There
are **14,085** `not_started` people, **523** possible-duplicate groups, and
**323** active conflicts. SQLite stores **17,984** attempts or plans and
**6,309** claims: 1,374 confirmed, 2,922 high, 1,529 medium, 198 low, 284
conflicting, and two unresolved. It contains **5,688** citation records and
**2,875** unique source documents. The public projection contains **2,479**
affiliations, **861** organizations, **4,469** sources, and **6,102** claims.
Full-index historical research remains unfinished.

## Replay and continuation

After importing prior durable batches into private SQLite:

```sh
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
python3 -m oss_research assign-page-batch --batch-name batch-731 --page 356 --first-row 1 --last-row 23
python3 -m oss_research research --source cia --batch batch-731 --max-queries 23
python3 -m oss_research research --source loc --batch batch-731 --max-queries 23
python3 -m oss_research research --source web --batch batch-731 --resume --max-queries 23 --dry-run
python3 -m oss_research import-review-decisions research/identity_review_decisions_2026-10-04_batch731.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page356-palmer-panza-review_batch-731_2026-10-04.json
python3 -m oss_research export-adapter-checkpoints
python3 -m oss_research export-derived
python3 -m oss_research export-review-queue
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
```

Adapter checkpoints must be imported before final reviewed decisions and
evidence so temporary discovery states cannot supersede reviewed dispositions.
The next research boundary is PDF page 356, rows 24-46, from Neal M Panzarella
through Arthur D Papoulias.

No API key, full service or officer number, raw Catalog or LoC API response,
copyrighted page image, street address, living-relative detail, modern
people-finder record, or private reviewer note is committed or included in the
public site. No authenticated NARA Catalog API request was made for this batch.
