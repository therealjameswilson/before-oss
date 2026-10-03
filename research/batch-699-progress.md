# Batch 699: Nelson-Nenadovich research

Batch 699 continues PDF page 339, row 46, through page 340, row 22,
from **James A Nelson** through **Lubitsa Nenadovich**. Fresh visual inspection
of both rendered pages confirmed all 23 printed rows. The immutable extraction
remains unchanged.

Official Army bulk evidence supports high-confidence identity-only decisions
for **John T Nelson**, **Orval D Nelson**, **Oscar K Nelson Jr.**, **Raymond A
Nelson**, **Vern W Nelson**, and **Peter N Nemeth**. These decisions use exact
indexed names and nonshared protected identifiers. No coded Army occupation is
converted into an employer.

Two protected-identifier conflicts remain visible. The number printed for
**Leonard A Nelson** reaches Army bulk name FELLOWS ROBERT R. The number
printed for **John A Nemecz** reaches Army bulk name RAY ROBERT. Neither record
is merged and no occupation or employer data are transferred.

The current Library of Congress API produced 35 discovery candidates across
eight people. A context reviewer inspected the official OCR page context for
every candidate, using full indexed names, per-request pacing below the
documented limit, bounded retries, and in-memory-only response handling. Every
candidate was rejected as a different initial or name, unrelated namesake,
postwar item, or OCR collision. The CIA adapter failed closed at the site's
robots policy without sending a search request. Targeted official and
institutional web searches produced no defensible pre-OSS employer. Later-life
records for Lubitsa Nenadovich and Walter C Nemetz were not assigned because
they did not establish the indexed identity or bridge the wartime chronology.
No raw LoC or NARA API response is retained.

The cohort ends with two `conflicting_sources` and 21
`no_reliable_result_after_protocol` outcomes. Identity statuses are six
`high_confidence`, two `conflicting`, and 15 `unresolved`. The evidence bundle
imports two sources, no organizations or affiliations, eight identity claims,
16 claim-source links, 23 person updates, and 23 consolidated research
attempts. Six Army identity candidates are accepted, two Army candidates are
recorded as conflicts, and 35 LoC source candidates are rejected.

Rebuilt coverage is **23,978/23,978** linked source rows and **23,939** active
person entities. Research-attempt coverage is **9,121/23,939 (38.1010%)**;
confirmed/high verified-employer coverage is **317/23,939 (1.3242%)**;
confirmed/high verified-affiliation coverage is **703/23,939 (2.9366%)**;
archival-review disposition coverage is **7,578/23,939 (31.6555%)**. There are
**14,813** `not_started` people, **520** possible-duplicate groups, and
**268** active conflicts. SQLite stores **16,428** attempts or plans and
**5,893** claims: 1,343 confirmed, 2,648 high, 1,465 medium, 196 low, and 241
conflicting. It contains **5,472** citation records and **2,707** unique source
documents. The public projection contains **2,383** affiliations, **803**
organizations, **4,255** sources, and **5,690** claims. Full-index historical
research remains unfinished.

## Replay and continuation

After importing prior durable batches into private SQLite:

```sh
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
python3 -m oss_research assign-page-batch --batch-name batch-699 --page 339 --first-row 46 --last-row 46
python3 -m oss_research assign-page-batch --batch-name batch-699 --page 340 --first-row 1 --last-row 22
python3 -m oss_research research --source cia --batch batch-699 --max-queries 23
python3 -m oss_research research --source loc --batch batch-699 --max-queries 23
python3 scripts/inspect_loc_candidates.py --batch batch-699 --max-candidates 35 --delay 3.2
python3 -m oss_research import-review-decisions research/identity_review_decisions_2026-10-03_batch699.csv
python3 -m oss_research import-reviewed-evidence research/evidence-pages339-340-nelson-nenadovich-review_batch-699_2026-10-03.json
python3 -m oss_research export-adapter-checkpoints
python3 -m oss_research export-derived
python3 -m oss_research export-review-queue
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
```

Adapter checkpoints must be imported before final reviewed decisions and
evidence so temporary discovery states cannot supersede reviewed dispositions.
The next research boundary begins at PDF page 340, row 23.

No API key, full service number, raw Catalog or LoC API response, copyrighted
page image, unrelated Army coded occupation, street address, or private
reviewer note is committed or included in the public site. No authenticated
NARA Catalog API request was made for this batch.
