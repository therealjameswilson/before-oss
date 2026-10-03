# Batch 698: Nelligan-Nelson research

Batch 698 continues PDF page 339, rows 23-45, from **James G Nelligan**
through **Isadore Nelson**. Fresh visual inspection of the rendered page
confirmed all 23 printed rows. The immutable extraction remains unchanged.

Official Army bulk evidence supports high-confidence identity-only decisions
for **James G Nelligan**, **Andrew E Nelson**, **Clifford R Nelson**,
**Franklin Nelson**, **Gilmer H Nelson**, **Herman Nelson**, **Ingolv
Nelson**, and **Isadore Nelson**. These decisions use exact indexed names and
nonshared protected identifiers. No coded Army occupation is converted into an
employer. Herman Nelson's anomalous coded entry date is not used for wartime
chronology.

Two additional official sources strengthen identity without supplying a
pre-OSS employer. A 9 May 1945 OSS Operational Group special order lists
**Harold G Nelson** with the indexed rank and protected identifier and assigns
him to Company B, Special Reconnaissance Battalion. *Veritas*, the U.S. Army
Special Operations history journal, independently names **Sgt Ingolv Nelson**
on the OSS Maritime Unit P-101 crew during Operation BOSTON. These records
document wartime OSS context, not the affiliation immediately before OSS, and
the site says so explicitly.

Two protected-identifier conflicts remain visible. The number printed for
**Charles H Nelson** reaches Army bulk name THOMALLA EMANUEL V. The number
printed for **Charles W Nelson** reaches the materially different, apparently
malformed Army bulk name NELSENJCHARLES W. Neither record is merged and no
occupation or employer data are transferred.

The current Library of Congress API produced 58 discovery candidates across
the cohort. A context reviewer inspected the official OCR page context for
every candidate, using full indexed names, per-request pacing below the
documented 20-requests-per-minute ceiling, bounded retries, and in-memory-only
response handling. Every candidate was rejected as a different initial or
name, unrelated namesake, postwar item, or OCR collision. The CIA adapter
failed closed at the site's robots policy without sending a search request;
targeted official-domain discovery searches produced no candidate. No raw LoC
or NARA API response is retained.

The cohort ends with two `completed`, two `conflicting_sources`, and 19
`no_reliable_result_after_protocol` outcomes. Identity statuses are nine
`high_confidence`, two `conflicting`, and 12 `unresolved`. The evidence
bundle imports four sources, no organizations or affiliations, 11 identity
claims, 23 claim-source links, 23 person updates, and 23 consolidated research
attempts. Eight Army identity candidates are accepted, two Army candidates are
recorded as conflicts, and 58 LoC source candidates are rejected.

Rebuilt coverage is **23,978/23,978** linked source rows and **23,939** active
person entities. Research-attempt coverage is **9,098/23,939 (38.0049%)**;
confirmed/high verified-employer coverage is **317/23,939 (1.3242%)**;
confirmed/high verified-affiliation coverage is **703/23,939 (2.9366%)**;
archival-review disposition coverage is **7,555/23,939 (31.5594%)**. There are
**14,836** `not_started` people, **520** possible-duplicate groups, and
**266** active conflicts. SQLite stores **16,372** attempts or plans and
**5,885** claims: 1,343 confirmed, 2,642 high, 1,465 medium, 196 low, and 239
conflicting. It contains **5,470** citation records and **2,706** unique source
documents. The public projection contains **2,383** affiliations, **803**
organizations, **4,253** sources, and **5,682** claims. Full-index historical
research remains unfinished.

## Replay and continuation

After importing prior durable batches into private SQLite:

```sh
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
python3 -m oss_research assign-page-batch --batch-name batch-698 --page 339 --first-row 23 --last-row 45
python3 -m oss_research research --source cia --batch batch-698 --max-queries 23
python3 -m oss_research research --source loc --batch batch-698 --max-queries 23
python3 scripts/inspect_loc_candidates.py --batch batch-698 --max-candidates 58 --delay 3.2
python3 -m oss_research import-review-decisions research/identity_review_decisions_2026-10-03_batch698.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page339-nelligan-nelson-review_batch-698_2026-10-03.json
python3 -m oss_research export-adapter-checkpoints
python3 -m oss_research export-derived
python3 -m oss_research export-review-queue
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
```

Adapter checkpoints must be imported before final reviewed decisions and
evidence so temporary discovery states cannot supersede reviewed dispositions.
The next research boundary begins at PDF page 339, row 46.

No API key, full service number, raw Catalog or LoC API response, copyrighted
page image, unrelated Army coded occupation, street address, or private
reviewer note is committed or included in the public site. No authenticated
NARA Catalog API request was made for this batch.
