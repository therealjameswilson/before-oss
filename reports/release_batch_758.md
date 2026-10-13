# Batch 758 release - Pike-Pillsbury research

Research and local release verification date: 2026-10-12 America/New_York.

## Historical work

Batch 758 publishes reviewed outcomes for PDF page 369, rows 29-46, from
Bertrand F Pike through Mary E Pillsbury. All 18 printed rows were visually
checked against a 300-dpi page render. Original spellings, ranks, boxes,
notes, locations, and protected identifiers remain recoverable in the private
database. Full protected identifiers remain private.

The 18 source rows remain linked to 18 separate person entities. The two
adjacent Edward F Pilley rows remain separate probable duplicate profiles.
Alphonse A Pilliccieri's literal `Also 381` note is preserved and drives a
cross-box archival task rather than an automatic merge.

Six exact-name, nonshared protected-identifier matches in official Army bulk
data establish high-confidence identity for Bertrand F Pike, Adam E Pikul,
Albert L Pilaroscia, Max Pilger, Antonio Pilichi, and Michael A Pilla. A seventh
Army candidate for Alphonse A Pilliccieri remains probable because the official
record gives only the initials A A. These matches establish identity only; no
coded Army occupation is converted into an employer or role.

A Norwich University student newspaper names John Andrew Pillepich, class of
1942, as an assistant editor in November 1940. A separate 1946 institutional
record identifies the same rare-name alumnus as a first lieutenant. Norwich is
therefore published at high confidence as an earlier student affiliation, not
as an employer. The postwar military posting is used only for identity
corroboration.

The *Lamb County Leader* documented an Edward F. Pilley as a resident engineer
on 19 February 1942. The source names no employer, and the index contains two
adjacent identical Edward F Pilley rows without row-specific identifiers. A
medium-confidence, visibly qualified occupation lead is therefore attached to
both profiles while both rows remain separate and excluded from default
employer analytics.

An obituary for the rare Enis H Pike name supports a high-confidence match to
the indexed first lieutenant and his World War II Army identity. Its named
civilian jobs are postwar and are deliberately excluded. A contemporary
Rochester obituary independently corroborates Albert L Pilaroscia's uncommon
full name and World War II Air Force service; his postwar education and legal
practice are likewise not back-projected into pre-OSS affiliation fields.

Later or unbridged leads for Emily G Pike, Edward Pilert, Robert Pillet, John A
Pilley, Paul Pillois, Mary E Pillsbury, and the remaining unresolved people are
recorded as rejections or archival next actions rather than public facts.

The reviewed evidence bundle imports seven sources, one existing organization,
three affiliations, 12 claims, 25 evidence links, 18 person updates, and 18
completed research attempts. Seven row-specific identity decisions were
imported. The final cohort identity statuses are eight high-confidence, three
probable, four ambiguous, and three unresolved. Research statuses are one
`completed`, 11 `requires_archival_review`, four `needs_identity_review`, and
two `occupation_only_found`.

The CIA cohort adapter stopped because the requested path was disallowed by
the retrieved robots policy, and the Library of Congress cohort check stopped
on HTTP 503 after bounded retries. These are recorded as source-access limits
rather than negative evidence. No authenticated NARA Catalog API request was
made, and no API key or raw API response was stored.

## Reproducible coverage

| Measure | Count |
| --- | ---: |
| Printed index rows preserved and linked | 23,978 / 23,978 |
| Visually audited extraction | 23,978 / 23,978 rows; 522 / 522 pages |
| Active person entities | 23,939 |
| People with nonplanned research attempts | 10,462 (43.7027%) |
| People with confirmed/high employer evidence | 345 (1.4412%) |
| People with confirmed/high affiliation evidence | 778 (3.2499%) |
| Archival-review dispositions assessed | 8,921 (37.2655%) |
| Not started | 13,472 |
| Possible duplicate groups | 535 |
| Conflicts | 352 |
| Claims by confidence | confirmed 1,397; high 3,182; medium 1,566; low 198; conflicting 305; unresolved 2 |
| Citation records / unique source documents | 5,850 / 2,992 |

Research statuses are: blocked_by_source_access 1; candidate_found 333;
completed 197; conflicting_sources 296; documented_prewar_employer_found 175;
in_progress 1,902; needs_identity_review 530; needs_temporal_review 24;
no_reliable_result_after_protocol 1,156; not_started 13,472;
occupation_only_found 1,052; requires_archival_review 4,504; and
verified_employer_found 297.

The public projection contains 23,939 person entities, 2,544 published
affiliations, 891 organizations, 4,626 public sources, and 6,443 published
claims. Full-index historical research remains unfinished.

## Local verification

The exact rebuilt tree passed these local release gates:

* Python unit suite: 139 / 139 passed, plus 78 subtests.
* Ingest validation: all seven extraction and SQLite integrity checks passed.
* Stratified profile audit: 200 profiles across all four difficulty tiers and
  required personnel, confidence, duplicate, and conflict strata passed all
  seven structural checks.
* Astro diagnostics: 392 files, 0 errors, 0 warnings, 0 hints.
* Production build: 24,869 pages.
* Browser release suite: 84 / 84 checks passed across desktop, phone, and
  tablet, including 15 Batch 758, 33 core, six analytics, and 30 accessibility
  checks.
* Link check: 24,869 HTML files checked; every internal link resolved and
  50,847 unique external URLs were inventoried for the separate live check.
* Public manifest: 67 assets / 108,071,760 bytes verified; manifest SHA-256
  `d247e1639b452150f1652eaecf0ade3ef5f9abdc4050b0f55ee896af63356cdc`.
* Private-identifier audit: 12,926 normalized identifiers, 120 formatted
  variants, 24,941 public artifacts, and 1,237 candidate substrings checked;
  zero aggregate false positives, manifest-size false positives, or unexpected
  boundary matches.
* Two consecutive production builds reproduced the 24,941-file,
  311,363,011-byte output tree at SHA-256
  `1d05780cc86f460947296fa27c2bf4e05b1f6cb62c749868818d5e2fe96e3ffd`.

## Publication verification

Release commit `ca45eb39463074a9f3b0e61d868d90ba299f5d2b` was pushed to
`main`. The [Test workflow](https://github.com/therealjameswilson/before-oss/actions/runs/38332383941)
completed successfully at `2026-10-13T01:34:15Z`, and the
[GitHub Pages workflow](https://github.com/therealjameswilson/before-oss/actions/runs/38332383903)
completed successfully at `2026-10-13T01:31:29Z`.

An unauthenticated immutable verification at `2026-10-13T01:34:26Z` confirmed
the deployed commit and 67 public assets totaling 108,071,760 bytes, with
manifest SHA-256
`d247e1639b452150f1652eaecf0ade3ef5f9abdc4050b0f55ee896af63356cdc`.
The verifier also checked eight core routes, all 31 source-register pages, and
all 18 direct Batch 758 profile routes at
<https://therealjameswilson.github.io/before-oss/>.

## Resume

~~~sh
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
python3 -m oss_research assign-page-batch --batch-name batch-758-pike-pillsbury --page 369 --first-row 29 --last-row 46
python3 -m oss_research import-review-decisions research/identity_review_decisions_2026-10-12_batch758.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page369-pike-pillsbury-review_batch-758_2026-10-12.json
python3 -m oss_research export-adapter-checkpoints
python3 -m oss_research export-derived
python3 -m oss_research export-review-queue
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
~~~

The next unresearched person boundary is PDF page 370, row 1, Albert V Pilone.
No API key, raw API response, full service or officer number, copyrighted page
image, unrelated Army coded occupation, street address, modern people-finder
record, or private reviewer note is committed or published.
