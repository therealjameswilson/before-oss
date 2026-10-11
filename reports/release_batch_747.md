# Batch 747 release - Perkins-Perry research

Research and local release verification date: 2026-10-11 America/New_York.

## Historical work

Batch 747 publishes reviewed outcomes for PDF page 364, rows 1-23, from Roy
Perkins through Francis Perry. All 23 printed rows were visually checked
against a 300-dpi page render. Original spellings, ranks, boxes, notes,
locations, and protected identifiers remain recoverable in the private
database. Full protected identifiers remain private.

The strongest biographical finding is Francis Perry. An American Battle
Monuments Commission account identifies 1st Lt. Francis Perry with the 2677th
OSS Regiment and the Dawes Team. A corroborative memorial profile reproduces
the nonshared protected officer identifier in the index. The profile reports
that Perry worked in the manufacture of knit goods when he entered the Army in
May 1941 and had earlier worked as a journalist in Austria. Both occupations
are published as medium-confidence, qualified pre-OSS evidence. Neither is
converted into a named employer, and neither is described as the immediate
pre-OSS affiliation.

Henry Gabriel (Eagle) Perley is linked at high confidence to the indexed Henry
G Perley. A Dartmouth obituary documents his student status in the class of
1943 before wartime service and his return in spring 1946 to finish his
studies. Dartmouth is published as student status, not as employment. A 1946
NARA-released communications memorandum supports the identity and radio-
operator context but is explicitly not used to establish a pre-OSS chronology.

Exact-name, nonshared protected-identifier matches in official Army bulk data
are accepted for Roy Perkins, Finis H Perky, Abraham I Perl, Joshua
Perlmutter, Walter S Perlmutter, John Perna, Nicholas L Pernice, Doyle C
Perrigin, and Vincenzo J Perruccio. Those matches establish identity only; no
coded Army occupation is converted into an employer or occupation claim. A
Taylor-Winfield obituary lead for Pernice is not dated closely enough to
establish prewar employment. A 1951 Hartford used-car record for Perruccio is
explicitly rejected as postwar evidence.

The unusual printed name order for Greta Perreau de La and index notes such as
`Extract fr`, `Alias Ro`, `Also in B`, `Also 053`, `British`, and `French` are
preserved. Common-name and incomplete records remain unresolved rather than
inheriting evidence from namesakes. Online evidence gaps are routed to
archival review instead of being described as proof that no prior affiliation
existed.

Exact-name OSS, employment/occupation, obituary, institutional, newspaper,
military, and archival searches were reviewed for all 23 people. The reviewed
evidence bundle imports six sources, one organization, one affiliation, 14
claims, 27 claim-source links, 23 person updates, and 23 completed research
attempts. Nine identity decisions are recorded. No authenticated NARA Catalog
API request was made.

## Reproducible coverage

| Measure | Count |
| --- | ---: |
| Printed index rows preserved and linked | 23,978 / 23,978 |
| Visually audited extraction | 23,978 / 23,978 rows; 522 / 522 pages |
| Active person entities | 23,939 |
| People with nonplanned research attempts | 10,211 (42.6542%) |
| People with confirmed/high employer evidence | 340 (1.4203%) |
| People with confirmed/high affiliation evidence | 763 (3.1873%) |
| Archival-review dispositions assessed | 8,670 (36.2171%) |
| Not started | 13,723 |
| Possible duplicate groups | 530 |
| Conflicts | 339 |
| Claims by confidence | confirmed 1,392; high 3,072; medium 1,551; low 198; conflicting 297; unresolved 2 |
| Citation records / unique source documents | 5,782 / 2,939 |

Research statuses are: blocked_by_source_access 1; candidate_found 333;
completed 194; conflicting_sources 292;
documented_prewar_employer_found 171; in_progress 1,902;
needs_identity_review 481; needs_temporal_review 24;
no_reliable_result_after_protocol 1,156; not_started 13,723;
occupation_only_found 1,050; requires_archival_review 4,318; and
verified_employer_found 294.

The public projection contains 23,939 person entities, 2,518 published
affiliations, 880 organizations, 4,558 public sources, and 6,305 published
claims. Full-index historical research remains unfinished.

## Local verification

The exact rebuilt tree passed these local release gates:

* Python unit suite: 139 / 139 passed, plus 78 generated subtests.
* Ingest validation: all seven extraction and SQLite integrity checks passed.
* Stratified profile audit: 200 profiles across all four difficulty tiers and
  required personnel, confidence, duplicate, and conflict strata passed all
  seven structural checks.
* Astro diagnostics: 381 files, 0 errors, 0 warnings, 0 hints.
* Production build: 24,858 pages.
* Browser release suite: 84 / 84 checks passed across desktop, phone, and
  tablet, including 15 Batch 747, 33 core, six analytics, and 30 accessibility
  checks.
* Link check: 24,858 HTML files checked; every internal link resolved and
  50,794 unique external URLs were inventoried for the separate live check.
* Public manifest: 67 assets / 107,256,824 bytes verified; manifest SHA-256
  `926c52a6a9444f1ad3e110d2f0d7969b8467779b4d89572117b87e0f2fbf96a8`.
* Private-identifier audit: 12,926 normalized identifiers, 120 formatted
  variants, 24,930 public artifacts, and 1,208 candidate substrings checked;
  zero aggregate false positives, manifest-size false positives, or unexpected
  boundary matches.
* Two consecutive production builds reproduced the 24,930-file,
  310,071,068-byte output tree at SHA-256
  `ee8284e5b6f0418bf0584e66a1900e53e4e36bab1439822683b73e89bfcfe16f`.

## Publication verification

Batch 747's reviewed data and public assets were published from commit
[`9caa449`](https://github.com/therealjameswilson/before-oss/commit/9caa44973e2873026fb480661d466e07979428c9).
The [Test workflow](https://github.com/therealjameswilson/before-oss/actions/runs/38176452479)
and [GitHub Pages workflow](https://github.com/therealjameswilson/before-oss/actions/runs/38176452478)
both completed successfully. The test workflow independently rebuilt the
private-identifier audit source and passed the public redaction audit.

Cache-busted, unauthenticated live verification against `9caa449` confirmed
the public counts of 23,939 people, 10,211 research attempts, 763 verified
affiliations, 340 verified employers, 8,670 archival-review assessments, and
13,723 not-started records. The live 67-asset manifest totals 107,256,824
bytes at SHA-256
`926c52a6a9444f1ad3e110d2f0d7969b8467779b4d89572117b87e0f2fbf96a8`.
The Henry G Perley profile displays the qualified Dartmouth student evidence;
the Francis Perry profile displays the Dawes Team identification and qualified
knit-goods occupation evidence. The oil-company category remains available
with 10 people and 12 historically named companies at
<https://therealjameswilson.github.io/before-oss/>.

## Resume

~~~sh
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
python3 -m oss_research assign-page-batch --batch-name batch-747-perkins-perry --page 364 --first-row 1 --last-row 23
python3 -m oss_research import-review-decisions research/identity_review_decisions_2026-10-11_batch747.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page364-perkins-perry-review_batch-747_2026-10-11.json
python3 -m oss_research export-adapter-checkpoints
python3 -m oss_research export-derived
python3 -m oss_research export-review-queue
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
~~~

The next research boundary is PDF page 364, beginning with row 24, Harold C or
Perry. No API key, raw API response, full service or officer number,
copyrighted page image, unrelated Army coded occupation, street address,
modern people-finder record, or private reviewer note is committed or
published.
