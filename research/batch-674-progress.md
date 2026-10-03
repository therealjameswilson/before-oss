# Batch 674: Moore research

Batch 674 completes the next contiguous 24-person queue on PDF page 327,
rows 23-46, from `George R. Moore` through `Russell C. Moore`. A fresh
160-dpi rendering and layout-text comparison confirmed every printed name,
initial, rank or grade, blank cell, box, note, archival location, and private
identifier. The index's spelling `Margeret` is preserved rather than silently
corrected. Robert D. Moore's printed `possible` note is also preserved.

The reviewed evidence supports ten high-confidence identity resolutions:
**George R. Moore, James L. Moore, John H. Moore, John F. Moore, Prentis
Moore, Price W. Moore, Richard H. Moore, Robert D. Moore, Ruben E. Moore,
and Russell C. Moore**. In each case, exact name and a nonshared protected
identifier agree between the OSS index and the official Army Serial Number
Merged File. These are identity-only findings. Coded Army occupations remain
private and were neither translated nor used as employer evidence.

Two discrepancies remain explicit. The official Army record for Robert D.
Moore includes a `Jr.` suffix absent from the index; the nonshared protected
identifier supports the identity while the source spellings remain distinct.
For Richard H. Moore, the Army entry record gives private as the entry grade
while the OSS index prints `Col`. Identity remains high confidence because the
protected identifier agrees, but the sharp rank discrepancy has a terminal
`conflicting_sources` status and requires Box 535 review. It is not silently
harmonized.

Fourteen people reached `no_reliable_result_after_protocol`: Hannah Moore,
Harold E. Moore, Henry W. Moore, James W. Moore, John R. Moore, Justine Moore,
Margeret A. Moore, Milton Moore, Phyllis Y. Moore, Raymond E. Moore, Robert J.
Moore, Robert K. Moore, Robert B. Moore, and Roy D. Moore. Each receives a
dignified public research-status page and a high-priority Box 534 or 535 next
action. This means no reliable online result was found; it does not mean no
prior employment existed.

The minimum staged protocol covered the official NARA index, the official
Army bulk file where applicable, exact-name OSS and employment searches,
targeted CIA Reading Room domain searches, a live Library of Congress API
query, institutional and obituary discovery, directories, and archival
searches. The direct CIA adapter failed closed once; targeted public
CIA-domain searches substituted, and the adapter failure was not treated as
negative evidence. The bounded Library of Congress retry completed 24
queries without errors and produced 87 discovery candidates. All 87 were
rejected because they were name-only OCR hits or postwar items without an
OSS, rank or grade, protected-identifier, or archival bridge. Ten Army
identity candidates were accepted, for **97 reviewed decisions total**.

No reliable immediate pre-OSS affiliation or last civilian employer was
established in this batch. It therefore adds no affiliation or organization
and does not change the oil-company category, which remains evidence-scoped
to **eight people across ten historically named companies**.

Rebuilt coverage is **23,978/23,978** linked source rows and **23,939** active
person entities. Research-attempt coverage is **8,556/23,939 (35.7408%)**;
confirmed/high verified-employer coverage is **302/23,939 (1.2615%)**;
confirmed/high verified-affiliation coverage is **670/23,939 (2.7988%)**;
archival-review disposition coverage is **7,012/23,939 (29.2911%)**. There
are **15,378** `not_started` people, **512** possible-duplicate groups, and
**223** active conflicts. SQLite stores **15,447** attempts or plans and
**5,420** claims: 1,326 confirmed, 2,265 high, 1,437 medium, 196 low, and 196
conflicting. It contains **5,304** citation records and **2,573** unique source
documents. The public projection contains **2,323** affiliations, **767**
organizations, **4,087** sources, and **5,217** claims. Full-index historical
research remains unfinished.

## Replay and continuation

After importing prior durable batches into private SQLite:

```sh
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
python3 -m oss_research import-review-decisions research/identity_review_decisions_2026-09-25_batch674.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page327-moore-review_batch-674_2026-09-25.json
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
