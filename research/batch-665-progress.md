# Batch 665: Minton-Mitchell research

The next contiguous queue spans PDF page 323 rows 30-46 and page 324 rows
1-5, from `Ralph A. Minton` through `Barbara B. Mitchell`. It contains **22
source rows and 22 cautious person entities**. Every person now has a saved,
reviewed outcome grounded in the visually checked NARA index, official Army
bulk identity comparison where applicable, grouped CIA Reading Room and
Library of Congress checks, exact-name and meaningful-variant OSS searches,
employment and occupation searches, and institutional, newspaper, obituary,
military, foreign-language, or archival checks as applicable. No authenticated
NARA Catalog request was made.

The reviewed findings preserve identity, relationship, and chronology limits:

- **Nicholas Mirkovich** is a high-confidence match to Dr. Nikola Mirkovic.
  Contemporary and institutional evidence documents his 1942-43 work in New
  York for the Yugoslav Government Office of Reconstruction. It is published
  as a medium-confidence, date-bounded last civilian/government affiliation,
  not as an explicit immediate predecessor to OSS service.
- **Bernard Mishkin** is a high-confidence identity match. His one-year
  employment contract with the Committee for Inter-American Artistic and
  Intellectual Relations is modeled separately from his documented Visiting
  Curator relationship with the Museo Nacional del Peru. The museum is an
  institutional affiliation, not silently converted into his employer.
- **Bohus Miroslav** is a high-confidence match to Bedrich Neumann, whose
  wartime cover name and career as a Czechoslovak military officer are
  documented. The project publishes the occupation but does not infer an
  immediate pre-OSS assignment.
- **Sylvester Missal** is a high-confidence match to the physician later
  documented as the OSS chief surgeon. His occupation as an otolaryngologist
  is published without inventing a named medical employer.
- **Samuel Mirasole** is a high-confidence Salvatore/Sam name-variant and OSS
  Eighth Army Detachment match. His postwar Pittsburgh Brewing Company work is
  excluded from the pre-OSS employment model.
- Protected Army identifiers support high-confidence identity matches for
  **Walter Mirbach**, **Peter Mirkine**, **Miguel Miro**, **Edward Mischler**,
  and **Joseph Missenda**. Army occupation codes remain private identity
  evidence and are never converted into employers.
- Three protected-identifier conflicts remain public and unresolved:
  **Ralph A. Minton / Ralph A. Monton**, **Harry C. Minutillo / Harry C.
  Menutile**, and **Peter M. Mishopoulos / Peter M. Moshopoulos**. None is
  silently corrected or assigned a namesake biography.
- The remaining nine people receive explicit
  `no_reliable_result_after_protocol` outcomes and archival next actions rather
  than unsupported biographies.

The bundle adds **18 claims**, three affiliations, three organization records,
14 sources, and 43 claim-source links. Eleven generated Army candidates
received review decisions. All 22 people have terminal batch outcomes: three
`conflicting_sources`, two `documented_prewar_employer_found`, nine
`no_reliable_result_after_protocol`, two `occupation_only_found`, and six
`requires_archival_review`. Batch identity outcomes are three `conflicting`,
ten `high_confidence`, and nine `unresolved`.

Rebuilt coverage is **23,978/23,978** linked source rows and **23,939** active
person entities. Research-attempt coverage is **8,380/23,939 (35.0056%)**;
confirmed/high verified-employer coverage is **297/23,939 (1.2407%)**;
confirmed/high verified-affiliation coverage is **659/23,939 (2.7528%)**;
archival-review disposition coverage is **6,836/23,939 (28.5559%)**. There are
**15,554** `not_started` people, **511** possible-duplicate groups, and **215**
active conflicts. SQLite stores **14,794** attempts or plans and **5,320**
claims: 1,323 confirmed, 2,187 high, 1,428 medium, 192 low, and 190 conflicting.
It contains **5,246** citation records and **2,526** unique source documents.
The public projection contains **2,302** affiliations, **759** organizations,
**4,032** sources, and **5,124** claims.

The oil-company category remains prominent at the top of the home page and
personnel directory and on its dedicated route. It remains evidence-scoped to
**eight people across ten historically named companies**. Batch 665 adds no
oil-company member. Full-index historical research is unfinished.

## Replay and continuation

After importing prior durable batches into private SQLite:

```sh
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
python3 -m oss_research import-review-decisions research/identity_review_decisions_2026-09-24_batch665.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page323-minton-mishkin-page324-mitchell-review_batch-665_2026-09-24.json
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
