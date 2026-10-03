# Batch 676: Moran-Moreau research

Batch 676 completes PDF page 328, rows 25-46, from `Grover C Moran`
through `Pierre Moreau`. Fresh rendered-page inspection and layout-text
comparison confirmed all 22 printed rows, including the `possibly` note for
Lawrence J Moran, the `French` note for Pierre Moreau, and the Box 536-537
transition.

Six exact-name matches with nonshared protected identifiers support
high-confidence Army identities: **James P Moran, Lester W Moran, William J
Moravansky, William M Morcock, Daniel A Morea, and Gregory L Moreau**. These
are identity-only findings. The official bulk file's coded occupations remain
private and are not translated into employers.

Two shared-identifier pairs remain deliberately separate. James H Moran and
James R Moran share one protected identifier, while William S Moran and
William J Moran share another. All four people retain `conflicting_sources`
status and critical-priority archival review rather than being silently
merged. Herbert T Morcom is a fifth conflict: the index identifier retrieves
an official Army record under a different name. That unrelated name and its
private fields are excluded from publication.

Three stronger historical outcomes were established:

- The indexed Frantisek Moravec is a high-confidence match to the Czech career
  military-intelligence officer František Moravec. Official Czech Ministry of
  Defence and CIA historical evidence places him in the Czechoslovak General
  Staff's Second Directorate from 1928. This is modeled as a military
  assignment, not civilian employment, and the evidence does not establish it
  as his immediate pre-OSS affiliation.
- Princeton's memorial identifies Wesley C. Morck and documents his prewar
  employment at Brinton & Co. It separately says that he acquired a sizeable
  interest in Clinton Oil Co. Ownership is modeled as a professional
  affiliation, not employment. Morck is therefore excluded from the featured
  oil-company employee category pending stronger evidence of an operating
  role.
- Contemporary newspaper evidence identifies Theodore A. Morde as an
  explorer, while a scholarly documentary history identifies him as an OSS
  agent. The result is `occupation_only_found`; no employer is invented.

Eight people reached `no_reliable_result_after_protocol`: Grover C Moran,
Lawrence J Moran, Vincent P Moran, William E Moran, Edwin J Morby, Paul Morch,
Robert W More, and Pierre Moreau. Each receives a terminal public research-
status page and a high-priority Box 536 or 537 next action. The disposition
means that the accessible sources reviewed did not establish a reliable
result; it does not mean that no prior employment existed.

The staged protocol covered the official NARA index, the official Army bulk
file where applicable, targeted official CIA-domain searches, exact-name OSS
and employment searches, a live Library of Congress pass, institutional and
obituary sources, directories, newspapers, and archival discovery. The direct
CIA adapter failed closed once and was not counted as negative evidence. The
review bundle preserves **48 decisions**: 7 accepted, 37 rejected, and 4
conflicting. The accepted decisions comprise six Army identity candidates and
one Theodore Morde source candidate. Thirty-six Library of Congress discovery
hits and the wrong-name Herbert Morcom Army candidate were rejected with
recorded reasons.

The batch imports seven sources, three organizations, three affiliations, 18
claims, 31 claim-source links, 22 person updates, and 22 research attempts.
The oil-company category remains evidence-scoped to **eight people across ten
historically named companies**.

Rebuilt coverage is **23,978/23,978** linked source rows and **23,939** active
person entities. Research-attempt coverage is **8,602/23,939 (35.9330%)**;
confirmed/high verified-employer coverage is **303/23,939 (1.2657%)**;
confirmed/high verified-affiliation coverage is **672/23,939 (2.8071%)**;
archival-review disposition coverage is **7,058/23,939 (29.4833%)**. There
are **15,332** `not_started` people, **512** possible-duplicate groups, and
**229** active conflicts. SQLite stores **15,541** attempts or plans and
**5,446** claims: 1,326 confirmed, 2,284 high, 1,438 medium, 196 low, and 202
conflicting. It contains **5,314** citation records and **2,581** unique source
documents. The public projection contains **2,326** affiliations, **770**
organizations, **4,097** sources, and **5,243** claims. Full-index historical
research remains unfinished.

## Replay and continuation

After importing prior durable batches into private SQLite:

```sh
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
python3 -m oss_research import-review-decisions research/identity_review_decisions_2026-09-25_batch676.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page328-moran-moreau-review_batch-676_2026-09-25.json
python3 -m oss_research export-adapter-checkpoints
python3 -m oss_research export-derived
python3 -m oss_research export-review-queue
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
```

Adapter checkpoints must be imported before the final reviewed decisions and
evidence so temporary discovery states cannot supersede reviewed dispositions.

No API key, full service number, raw Catalog API response, copyrighted page
image, unrelated Army name, or private reviewer note is committed or included
in the public site.
