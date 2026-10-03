# Batch 673: Mooney-Moore research

Batch 673 completes the next contiguous 22-person queue on PDF page 327,
rows 1-22, from `Edward O. Mooney` through `Frank W. Moore`. Rendered-page
inspection confirmed every printed name, rank or grade, blank field, box,
archival location, and private identifier without publishing a full service
identifier.

The reviewed evidence supports these bounded findings:

- Official Army bulk data supplies exact-name and nonshared protected-
  identifier matches for **Edward O. Mooney, Benjamin Moore, Benjamin T.
  Moore, Billy G. Moore, Daniel E. Moore, Frank J. Moore, and Frank W.
  Moore**. Those seven identity matches are high confidence. Their coded Army
  occupations remain private and were not translated into employers. Rank
  differences between the enlistment record and later OSS index are not
  silently harmonized.
- Official CIA History Staff sources identify indexed Lieutenant **Alex
  Moore** as the Chicago-born Army officer who served with a military-
  intelligence interrogation team until his January 1945 transfer to OSS.
  The Army team is published as his immediate pre-OSS military assignment
  with `explicit_immediate` temporal evidence. The same official biography
  documents earlier American Red Cross service in France and England, but it
  does not establish paid employment or volunteer status; the relationship
  therefore remains `unknown`. No last civilian employer was inferred.
- Case Western Reserve University's institutional biography connects indexed
  **Dan T. Moore** to Dan Tyler Moore Jr., Cleveland SEC regional
  administrator, civilian-defense official, and OSS civilian major. SEC and
  official government records date the Cleveland SEC post to 1939-1942. The
  SEC role is published as the best-supported last civilian government
  affiliation before OSS. A concurrent Office of Civilian Defense role is
  published at medium confidence with an explicit warning that the available
  evidence does not show which federal assignment ended last.
- **Barrington Moore's** prior high-confidence identity and Yale student
  affiliation remain intact. Yale is not recast as an employer.

Twelve people reached `no_reliable_result_after_protocol`: Frank E. Mooney,
Mary B. Mooney, Regina Mooney, Thomas F. Mooney, Bernice V. Moore, Dorothy A.
Moore, Douglas S. Moore, Elizabeth S. Moore, Elizabeth C. Moore, Emmett E.
Moore, Ernestine M. Moore, and Eugene W. Moore. Each has a saved negative
research outcome, rejected-candidate reasons where applicable, a dignified
public status page, and a high-priority Box 534 next action. This finding means
no reliable online result was found; it does not mean no prior employment
existed.

The staged protocol included NARA index context, protected-identifier Army
bulk review where available, CIA Reading Room or targeted public CIA-domain
review, exact-name OSS queries with meaningful variants, employment and
occupation queries, Library of Congress newspaper searching, institutional
biographies, official SEC and government records, obituaries, directories,
and archival discovery. The CIA adapter failed closed once and that failure
was not treated as negative evidence. The reviewed queue records **58**
candidate decisions: **8 accepted** and **50 rejected**. Rejections include
Benjamin Moore paint advertisements, name-only notices, different initials,
postwar records, temporally impossible records, and famous namesakes.

The bundle adds **four affiliations, four reused canonical organizations,
thirteen published or qualified claims, nine sources, twenty-nine claim-source
links, twenty-two reviewed research attempts, and twenty-two person
dispositions**. The oil-company category remains evidence-scoped to **eight
people across ten historically named companies**; Batch 673 adds no member.

Rebuilt coverage is **23,978/23,978** linked source rows and **23,939** active
person entities. Research-attempt coverage is **8,532/23,939 (35.6406%)**;
confirmed/high verified-employer coverage is **302/23,939 (1.2615%)**;
confirmed/high verified-affiliation coverage is **670/23,939 (2.7988%)**;
archival-review disposition coverage is **6,988/23,939 (29.1909%)**. There are
**15,402** `not_started` people, **512** possible-duplicate groups, and **222**
active conflicts. SQLite stores **15,374** attempts or plans and **5,410**
claims: 1,326 confirmed, 2,255 high, 1,437 medium, 196 low, and 196
conflicting. It contains **5,302** citation records and **2,571** unique source
documents. The public projection contains **2,323** affiliations, **767**
organizations, **4,085** sources, and **5,207** claims. Full-index historical
research remains unfinished.

## Replay and continuation

After importing prior durable batches into private SQLite:

```sh
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
python3 -m oss_research import-review-decisions research/identity_review_decisions_2026-09-25_batch673.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page327-mooney-moore-review_batch-673_2026-09-25.json
python3 -m oss_research export-adapter-checkpoints
python3 -m oss_research export-derived
python3 -m oss_research export-review-queue
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
```

Adapter checkpoints must be imported before the final reviewed decisions and
evidence so temporary discovery states cannot supersede reviewed dispositions.

No API key, full service number, raw Catalog API response, copyrighted page
image, or private reviewer note is committed or included in the public site.
