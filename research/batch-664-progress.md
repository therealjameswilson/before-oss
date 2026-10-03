# Batch 664: Milton-Mins research

The next contiguous queue on PDF page 323 rows 8-29, from `Jules Milton`
through the two separately preserved `Leonard E. Mins` rows, contains **22
source rows and 22 cautious person entities**. Every person now has a saved,
reviewed outcome grounded in the visually checked NARA index, official Army
bulk identity comparison where applicable, grouped CIA Reading Room and
Library of Congress checks, exact-name and meaningful-variant OSS searches,
employment and occupation searches, and institutional, newspaper, obituary,
military, foreign-language, or archival checks as applicable. No authenticated
NARA Catalog request was made.

The reviewed findings preserve identity, relationship, and chronology limits:

- **Emil Mincu** is a high-confidence match to a Romanian merchant-marine
  officer. An institutional maritime study and archive-cited career account
  document his work for Serviciul Maritim Român aboard `Mangalia`, followed by
  work for an unnamed American private shipping company. SMR is published as
  documented prewar employment, not immediate pre-OSS work. The later company
  is qualified and deliberately left unnamed and unnormalized.
- **John P. Minogianis** is a high-confidence official Army and OSS-roster
  match. The 122nd Infantry Battalion recruiting route into Greek Operational
  Group V is published as a medium-confidence probable immediate military
  pathway, not a civilian employer.
- **Emile R. Minerault** is a high-confidence identity match in official U.S.
  and French records, but the index's Sergeant grade conflicts with the DPAA
  First Lieutenant record. The rank conflict remains public and no pre-OSS
  employer is invented.
- Exact protected Army matches support high-confidence identities for
  **Harold E. Miner**, **Thomas G. Minas**, and **Orin P. Minnis**. **Joseph G.
  Miner** remains probable because the Army record adds `Jr.`. **Terrence W.
  Miltower** remains conflicting because the official Army record tied to the
  protected identifier says `Miltner`. Army occupation codes remain private
  identity evidence and are never converted into employers.
- **Feodor Minorsky** remains only a probable archival lead. A discovery list
  points to UK file `HS 9/1039/5`, but the underlying file and any SOE-to-OSS
  transfer evidence still require review.
- The two adjacent **Leonard E. Mins** rows in Boxes 528 and 527 remain separate
  ambiguous people in a visible duplicate group. Official records identify a
  Leonard Emil Mins candidate but do not assign that biography to either
  personnel jacket. Politically charged Congressional statements are treated
  as evidence that the statements were made, not as proof that every allegation
  was true. No employer affiliation is created for either row.
- The remaining eleven people receive explicit
  `no_reliable_result_after_protocol` outcomes and archival next actions rather
  than unsupported biographies.

The bundle adds **14 claims**, three affiliations, two organization records,
13 sources, and 31 claim-source links. Six generated Army candidates received
review decisions. All 22 people have terminal batch outcomes: one `completed`,
one `documented_prewar_employer_found`, two `conflicting_sources`, seven
`requires_archival_review`, and eleven
`no_reliable_result_after_protocol`.

Rebuilt coverage is **23,978/23,978** linked source rows and **23,939** active
person entities. Research-attempt coverage is **8,358/23,939 (34.9137%)**;
confirmed/high verified-employer coverage is **297/23,939 (1.2407%)**;
confirmed/high verified-affiliation coverage is **658/23,939 (2.7487%)**;
archival-review disposition coverage is **6,814/23,939 (28.4640%)**. There are
**15,576** `not_started` people, **508** possible-duplicate groups, and **212**
active conflicts. SQLite stores **14,772** attempts or plans and **5,302**
claims: 1,323 confirmed, 2,174 high, 1,426 medium, 192 low, and 187 conflicting.
It contains **5,232** citation records and **2,514** unique source documents.
The public projection contains **2,299** affiliations, **756** organizations,
**4,018** sources, and **5,106** claims.

The oil-company category remains prominent at the top of the home page and
personnel directory and on its dedicated route. It remains evidence-scoped to
**eight people across ten historically named companies**. Batch 664 adds no
oil-company member: maritime shipping employment is not an oil-company claim.
Full-index historical research is unfinished.

## Replay and continuation

After importing prior durable batches into private SQLite:

```sh
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
python3 -m oss_research import-review-decisions research/identity_review_decisions_2026-09-24_batch664.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page323-milton-mins-review_batch-664_2026-09-24.json
python3 -m oss_research export-adapter-checkpoints
python3 -m oss_research export-derived
python3 -m oss_research export-review-queue
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
```

Adapter checkpoints must be imported before the final reviewed decisions and
evidence so temporary adapter states cannot supersede the batch's reviewed
research dispositions.

No API key, full service number, raw Catalog API response, copyrighted page
image, or private reviewer note is committed or included in the public site.
