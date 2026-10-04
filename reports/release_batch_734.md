# Batch 734 release - Parent-Parker research

Research and local release verification date: 2026-10-04 America/New_York.

## Historical work

Batch 734 publishes reviewed outcomes for PDF page 357, rows 24-46, from
Robert E Parent through Hilda B Parker. All 23 printed rows were visually
checked against a 300-dpi page render. Original spellings, ranks, grades,
boxes, notes, and locations remain recoverable; protected identifiers remain
private.

An official National Park Service OSS history confirms Nelson B Paris as the
naval photographer on the Dawes Mission. Six exact official Army bulk matches
establish high-confidence identities without turning coded Army data into
employer evidence. A Texas Tech archival interview and Cornell institutional
class notes establish Evan J Parker Jr.'s high-confidence identity and Class
of 1941 student affiliation. Cornell is published as student status only and
is excluded from employer analytics.

The protected identifier printed for Jesse Paris points to an official Army
record named TRUITT GEORGE S. The conflict is public, no Army metadata is
transferred, and Box 585 receives critical archival-review priority. Fourteen
other people remain unresolved after the staged protocol; discovery-only
genealogy and namesake results remain rejected candidates rather than facts.

The 23 reviewed people record 22 `requires_archival_review` outcomes and one
`conflicting_sources` outcome. Identity statuses are one confirmed, seven
high-confidence, one conflicting, and 14 unresolved. The reviewed bundle
reuses one organization and imports five sources, one student affiliation, 10
claims, 21 claim-source links, 23 person updates, and 23 consolidated research
attempts. Six accepted and one conflicting identity decisions are recorded.

## Reproducible coverage

| Measure | Count |
| --- | ---: |
| Printed index rows preserved and linked | 23,978 / 23,978 |
| Visually audited extraction | 23,978 / 23,978 rows; 522 / 522 pages |
| Active person entities | 23,939 |
| People with nonplanned research attempts | 9,918 (41.4303%) |
| People with confirmed/high employer evidence | 334 (1.3952%) |
| People with confirmed/high affiliation evidence | 745 (3.1121%) |
| Archival-review dispositions assessed | 8,376 (34.9889%) |
| Not started | 14,016 |
| Possible duplicate groups | 523 |
| Conflicts | 330 |
| Attempts or plans | 18,131 |
| Claims by confidence | confirmed 1,382; high 2,946; medium 1,537; low 198; conflicting 292; unresolved 2 |
| Citation records / unique source documents | 5,712 / 2,888 |

Research statuses are: `blocked_by_source_access` 1; `candidate_found` 333;
`completed` 188; `conflicting_sources` 287;
`documented_prewar_employer_found` 168; `in_progress` 1,903;
`needs_identity_review` 459; `needs_temporal_review` 24;
`no_reliable_result_after_protocol` 1,156; `not_started` 14,016;
`occupation_only_found` 1,047; `requires_archival_review` 4,068; and
`verified_employer_found` 289.

The public projection contains 2,490 published affiliations, 863
organizations, 4,488 public sources, and 6,150 published claims. Full-index
historical research remains unfinished.

## Local verification

The exact rebuilt tree passed these local release gates:

* Python unit suite: 139 / 139 passed, plus generated subtests.
* Astro diagnostics: 368 files, 0 errors, 0 warnings, 0 hints.
* Production build: 24,840 pages.
* Browser release suite: 84 / 84 checks passed across desktop, phone, and
  tablet, including 15 Batch 734, 33 core, six analytics, and 30 accessibility
  checks.
* Link check: 24,840 HTML files checked; every internal link resolved and
  50,745 unique external URLs were inventoried for the separate live check.
* Public manifest: 67 assets / 106,360,198 bytes verified; manifest SHA-256
  `848b1135e7a002a3c3f3875f1fe404bbb8312a18567f07293e77207c89d01ea1`.
* Private-identifier audit: 12,926 normalized identifiers, 120 formatted
  variants, 24,912 public artifacts, and 1,205 candidate substrings checked
  with zero unexpected boundary matches.
* Stratified profile audit: 200 profiles across all four difficulty tiers and
  required personnel, confidence, duplicate, and conflict strata passed all
  seven structural checks.
* Two consecutive production builds reproduced output-tree SHA-256
  `94a2e89a3bc5d514cbec3d900e4fe06840d44ed89c388110fa4ef859b0da7328`.
* The supported bounded release suite completed cleanly; all retained
  historical batch specifications remain available through the unbounded
  command.

## Publication verification

Publication is pending commit, push, GitHub Actions, and immutable live
verification. This section will be replaced with exact run and commit links
after deployment succeeds.

## Resume

```sh
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
python3 -m oss_research assign-page-batch --batch-name batch-734-parent-parker --page 357 --first-row 24 --last-row 46
python3 -m oss_research import-review-decisions research/identity_review_decisions_2026-10-04_batch734.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page357-parent-parker-review_batch-734_2026-10-04.json
python3 -m oss_research export-adapter-checkpoints
python3 -m oss_research export-derived
python3 -m oss_research export-review-queue
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
```

The next research boundary is PDF page 358, rows 1-23, from James C Parker
through Marian A Parrott. No API key, raw API response, full service or officer
number, copyrighted page image, unrelated Army coded occupation, street
address, modern people-finder record, or private reviewer note is committed or
published. No authenticated NARA Catalog API request was made for this batch.
