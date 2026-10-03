# Batch 675: Moore-Moran research

Batch 675 completes the next contiguous 24-person queue on PDF page 328,
rows 1-24, from `Springs R Moore` through `George B Moran`. Fresh rendered-
page inspection and layout-text comparison confirmed every printed name,
initial, rank or grade, blank cell, box, note, archival location, and private
identifier. The truncated index notes `file is ch` and `docume` remain
preserved as printed rather than silently expanded.

The reviewed evidence supports six high-confidence Army identity resolutions:
**Wallace J Moore, Walter A Moore, Gordon A Moote, Domenic J Morabito, Daniel J
Moran, and George B Moran**. In each case, exact name and a nonshared protected
identifier agree between the OSS index and the official Army Serial Number
Merged File. These are identity-only findings. Coded Army occupations remain
private and were neither translated nor used as employer evidence. Walter A
Moore's Army source adds a `Jr.` suffix absent from the index, while the
index's unfamiliar `PUT` grade remains uninterpreted.

An official NARA archival guide supplies a seventh high-confidence identity
bridge. Record Group 226, Entry 210, Box 201, WN#08587 identifies Clarence
Moran with the Field Photo Branch and the same distinctive `C SP-P` grade
printed in the personnel index. This establishes an OSS assignment bridge;
it does not establish a pre-OSS employer.

One discrepancy remains explicit. Wayne E Moore's printed protected
identifier retrieves a different name in the official Army file. The project
does not publish that unrelated name. Wayne Moore retains a terminal
`conflicting_sources` status and a critical-priority Box 536 review rather
than being attached to the wrong identity.

Sixteen people reached `no_reliable_result_after_protocol`: Springs R Moore,
William B Moore, William C Moore, William R Moore, Wilson H Moore, Ethel H
Moorhead, Tommie J Moorman, Joseph L Moortgat, Edward J Moraghan, Victor M
Morales, Alfred B Moran, Avis M Moran, Cecilia A Moran, Charles Moran, Finis G
Moran, and Frank W Moran. Each receives a dignified public research-status
page and a high-priority Box 535 or 536 next action. This means no reliable
online result was found; it does not mean no prior employment existed.

The minimum staged protocol covered the official NARA index, the official
Army bulk file where applicable, exact-name OSS and employment searches,
targeted CIA Reading Room domain searches, a live Library of Congress API
query, institutional and obituary discovery, directories, and archival
searches. The direct CIA adapter failed closed once; targeted public
CIA-domain searches substituted, and the adapter failure was not treated as
negative evidence. The bounded Library of Congress pass completed 24 queries
and produced 27 discovery candidates. All 27 were rejected because they were
name-only or temporally unsuitable results without an OSS, rank or grade,
protected-identifier, or archival bridge. The only CIA-domain result was a
1955 naval-history author named Charles Moran and was rejected as a namesake.
Six Army candidates were accepted and one wrong-name Army result rejected,
for **34 reviewed decisions total**.

No reliable immediate pre-OSS affiliation or last civilian employer was
established in this batch. It therefore adds no affiliation or organization
and does not change the oil-company category, which remains evidence-scoped
to **eight people across ten historically named companies**.

Rebuilt coverage is **23,978/23,978** linked source rows and **23,939** active
person entities. Research-attempt coverage is **8,580/23,939 (35.8411%)**;
confirmed/high verified-employer coverage is **302/23,939 (1.2615%)**;
confirmed/high verified-affiliation coverage is **670/23,939 (2.7988%)**;
archival-review disposition coverage is **7,036/23,939 (29.3914%)**. There
are **15,354** `not_started` people, **512** possible-duplicate groups, and
**224** active conflicts. SQLite stores **15,496** attempts or plans and
**5,428** claims: 1,326 confirmed, 2,272 high, 1,437 medium, 196 low, and 197
conflicting. It contains **5,307** citation records and **2,575** unique source
documents. The public projection contains **2,323** affiliations, **767**
organizations, **4,090** sources, and **5,225** claims. Full-index historical
research remains unfinished.

## Replay and continuation

After importing prior durable batches into private SQLite:

```sh
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
python3 -m oss_research import-review-decisions research/identity_review_decisions_2026-09-25_batch675.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page328-moore-moran-review_batch-675_2026-09-25.json
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
