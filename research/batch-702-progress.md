# Batch 702: Newman-Nicholas research

Batch 702 covers PDF page 341, rows 23-45, from **Martin D Newman** through
**Blake H Nicholas**. Fresh visual inspection of the rendered source page
confirmed all 23 printed rows, representing 22 active person entities. The
two William L Newman rows remain separately preserved and linked to one
entity; the immutable extraction is unchanged.

**Lester J Newquist** is a probable identity match to the University of
Chicago alumnus and banker documented as joining Brown Brothers Harriman &
Co. in 1936. The employment is published only as medium-confidence,
documented-prewar evidence. Neither the accessible contemporary banking item
nor the institutional corroboration explicitly connects the person to OSS or
establishes Brown Brothers Harriman as his immediate pre-OSS affiliation or
last civilian employer.

Official Army bulk evidence supports high-confidence identity-only decisions
for **Martin D Newman**, **Morton Newman**, **Howard T Newsom**, **Grover R
Newton**, **Vidma Newton**, and **Blake H Nicholas**. Exact indexed names and
nonshared protected identifiers agree. No coded Army occupation is converted
into an employer. A postwar Camco Oil Tool Supply lead for Howard T Newsom is
explicitly excluded from the pre-OSS record and from the oil-company category.

**Earl J Nichelson** may be the same person as the Earl J Nicholson indexed on
the following page: the two records share a protected identifier but differ
in spelling, rank, box, and page. Both source rows and both person entities
remain visible and unmerged pending direct personnel-file evidence. The
cohort's other unresolved people retain explicit archival-review guidance.

The CIA adapter failed closed at the site's robots policy without sending a
search request. The Library of Congress adapter completed four no-result
checks and recorded one timeout before the live batch was stopped rather than
continue repeated slow retries. Exact-name OSS, employment, institutional,
newspaper, obituary, archival, and disambiguation searches were then reviewed
for all 22 people. No raw NARA or LoC API response is retained.

The cohort ends with one `documented_prewar_employer_found`, one
`needs_identity_review`, and 20 `no_reliable_result_after_protocol` outcomes.
Identity statuses are seven `high_confidence`, one `probable`, one
`ambiguous`, and 13 `unresolved`. The evidence bundle imports four sources,
one organization, one affiliation, ten claims, 19 claim-source links, 22
person updates, and 22 consolidated research attempts. Review decisions
accept six Army identity candidates and preserve one probable duplicate
candidate without merging it.

Rebuilt coverage is **23,978/23,978** linked source rows and **23,939** active
person entities. Research-attempt coverage is **9,187/23,939 (38.3767%)**;
confirmed/high verified-employer coverage is **319/23,939 (1.3326%)**;
confirmed/high verified-affiliation coverage is **706/23,939 (2.9492%)**;
archival-review disposition coverage is **7,644/23,939 (31.9312%)**. There are
**14,747** `not_started` people, **521** possible-duplicate groups, and **272**
active conflicts. SQLite stores **16,571** attempts or plans and **5,938**
claims: 1,345 confirmed, 2,678 high, 1,471 medium, 196 low, 246 conflicting,
and two unresolved. It contains **5,493** citation records and **2,725** unique
source documents. The public projection contains **2,395** affiliations,
**815** organizations, **4,276** sources, and **5,733** claims. Full-index
historical research remains unfinished.

## Replay and continuation

After importing prior durable batches into private SQLite:

```sh
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
python3 -m oss_research assign-page-batch --batch-name batch-702 --page 341 --first-row 23 --last-row 45
python3 -m oss_research research --source cia --batch batch-702 --max-queries 22
python3 -m oss_research research --source loc --batch batch-702 --max-queries 22
python3 -m oss_research research --source web --batch batch-702 --max-queries 22
python3 -m oss_research import-review-decisions research/identity_review_decisions_2026-10-03_batch702.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page341-newman-nicholas-review_batch-702_2026-10-03.json
python3 -m oss_research export-adapter-checkpoints
python3 -m oss_research export-derived
python3 -m oss_research export-review-queue
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
```

Adapter checkpoints must be imported before final reviewed decisions and
evidence so temporary discovery states cannot supersede reviewed dispositions.
The next research boundary begins at PDF page 341, row 46 (**Christo
Nicholas**).

No API key, full service number, raw Catalog or LoC API response, copyrighted
page image, unrelated Army coded occupation, postwar employer lead, street
address, or private reviewer note is committed or included in the public
site. No authenticated NARA Catalog API request was made for this batch.
