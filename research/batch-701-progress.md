# Batch 701: Nevada-Newman research

Batch 701 covers PDF page 340, row 46, and page 341, rows 1-22, from
**Arpad J Nevada** through **John R Newman**. Fresh visual inspection of the
two rendered pages confirmed all 23 printed rows. The immutable extraction
remains unchanged.

Five people received newly publishable historical pathways. **Ilhan New** is
confirmed through the exact indexed name, protected identifier, official Army
evidence, and Yuhan's institutional chronology. The public record keeps his
1941 Overseas Korean Congress executive work separate from his earlier Yuhan
Corporation presidency, La Choy self-employment, and University of Southern
California student status. **Theodore M Newcomb** is a high-confidence match
to the social psychologist; the National Academy memoir explicitly places his
University of Michigan faculty work shortly before his FBIS and OSS service.

**Norman N Newhouse** is a high-confidence identity match through the
distinctive name, lieutenant-colonel rank, OSS Mediterranean context, and
contemporary media evidence. The Long Island Press is published only as a
medium-confidence last civilian employer because the accessible sources do
not state his exact military leave date. **Raymond F Newkirk** is a
high-confidence match to the counterintelligence specialist. His FBI work is
published as a qualified government assignment, not a civilian-company
employer, because the exact transfer date remains unlocated. **John W Newett**
is a high-confidence match to a wartime Naval Air Corps pilot-navigator and
OSS veteran, but the order of those assignments remains uncertain and no
employer is inferred.

Official Army bulk evidence supports high-confidence identity-only decisions
for **Louis W Neve**, **Charles H New**, **Victor M Newberg**, **Truman H
Newberry II**, **Edwin S Newman**, and **John R Newman**. Exact indexed names
and nonshared protected identifiers agree. No coded Army occupation is
converted into an employer. The Army evidence tied to the printed identifiers
for **Winton H Newkirk** and **Howard L Newman** materially conflicts with the
indexed names; both conflicts remain visible and no biographical data are
transferred.

The Library of Congress API produced 12 discovery candidates. Official OCR
context for every candidate was inspected, and all 12 were rejected as
unrelated namesakes or contexts that did not establish identity or pre-OSS
work. The CIA adapter failed closed at the site's robots policy without
sending a search request. Exact-name, employment, obituary, institutional,
and archival searches were completed for the cohort. No raw LoC or NARA API
response is retained.

The cohort ends with two `verified_employer_found`, one
`documented_prewar_employer_found`, two `completed`, two
`conflicting_sources`, and 16 `no_reliable_result_after_protocol` outcomes.
Identity statuses are one `confirmed`, ten `high_confidence`, two
`conflicting`, and ten `unresolved`. The evidence bundle imports ten sources,
eight organizations, eight affiliations, 22 claims, 42 claim-source links, 23
person updates, and 23 consolidated research attempts. Review decisions
accept seven Army identity candidates, preserve two conflicts, and reject 12
LoC discovery candidates.

Rebuilt coverage is **23,978/23,978** linked source rows and **23,939** active
person entities. Research-attempt coverage is **9,165/23,939 (38.2848%)**;
confirmed/high verified-employer coverage is **319/23,939 (1.3326%)**;
confirmed/high verified-affiliation coverage is **706/23,939 (2.9492%)**;
archival-review disposition coverage is **7,622/23,939 (31.8393%)**. There are
**14,769** `not_started` people, **521** possible-duplicate groups, and **272**
active conflicts. SQLite stores **16,521** attempts or plans and **5,928**
claims: 1,345 confirmed, 2,671 high, 1,469 medium, 196 low, 245 conflicting,
and two unresolved. It contains **5,489** citation records and **2,722** unique
source documents. The public projection contains **2,394** affiliations,
**814** organizations, **4,272** sources, and **5,723** claims. Full-index
historical research remains unfinished.

## Replay and continuation

After importing prior durable batches into private SQLite:

```sh
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
python3 -m oss_research assign-page-batch --batch-name batch-701 --page 340 --first-row 46 --last-row 46
python3 -m oss_research assign-page-batch --batch-name batch-701-main --page 341 --first-row 1 --last-row 22
python3 -m oss_research research --source cia --batch batch-701 --max-queries 1
python3 -m oss_research research --source cia --batch batch-701-main --max-queries 22
python3 -m oss_research research --source loc --batch batch-701 --max-queries 1
python3 -m oss_research research --source loc --batch batch-701-main --max-queries 22
python3 scripts/inspect_loc_candidates.py --batch batch-701-main --max-candidates 12 --delay 3.2
python3 -m oss_research import-review-decisions research/identity_review_decisions_2026-10-03_batch701.csv
python3 -m oss_research import-reviewed-evidence research/evidence-pages340-341-nevada-newman-review_batch-701_2026-10-03.json
python3 -m oss_research export-adapter-checkpoints
python3 -m oss_research export-derived
python3 -m oss_research export-review-queue
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
```

Adapter checkpoints must be imported before final reviewed decisions and
evidence so temporary discovery states cannot supersede reviewed dispositions.
The next research boundary begins at PDF page 341, row 23.

No API key, full service number, raw Catalog or LoC API response, copyrighted
page image, unrelated Army coded occupation, street address, or private
reviewer note is committed or included in the public site. No authenticated
NARA Catalog API request was made for this batch.
