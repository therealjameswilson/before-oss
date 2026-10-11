# Batch 748 release - Perry-Persky research

Research and local release verification date: 2026-10-11 America/New_York.

## Historical work

Batch 748 publishes reviewed outcomes for PDF page 364, rows 24-46, from
Harold C or Perry through Helen Persky. All 23 printed rows were visually
checked against a 300-dpi page render. Original spellings, ranks, boxes, notes,
locations, and protected identifiers remain recoverable in the private
database. Full protected identifiers remain private.

Hart Perry is linked at high confidence to the indexed first lieutenant. A
scholarly archival study by Siegfried Beer identifies Lieutenant Hart Perry,
codename Pleurisy, with OSS-Austria at Mauthausen in May 1945 and cites Record
Group 226 records. University of Chicago institutional sources identify Hart
Perry, 1918-1991, as an alumnus and as AM'39. The 1939 degree is published as
documented prewar student status, not employment and not the immediate pre-OSS
affiliation. Later Federal Bureau of the Budget, development-finance, and ITT
roles are postwar and are excluded from pre-OSS claims.

Exact-name, nonshared protected-identifier matches in official Army bulk data
are accepted for Harold C Perry, John S Perry, Manuel S Perry, Phillip P Perry,
William R Perry, Anthony Perseo, and William R Pershing. Those matches
establish identity only; no coded Army occupation is converted into an
employer or occupation claim. The index's literal `C or` field for Harold is
preserved, while `Harold C Perry` is retained as a documented search variant
rather than a silent correction.

Two official-record conflicts remain visible. Homer L Perry's protected
identifier points to an Army record for a different name, so that candidate is
not accepted. The James B Perry row in Box 597 shares an identifier with a
separate James B Peery row in Box 593, while the Army bulk name uses Peery.
Both indexed people remain separate, the printed `Remove` note remains
uninterpreted, and the duplicate-group label no longer embeds the protected
identifier. The two distinct Robert Perry source rows in Box 598 also remain
separate; their truncated `Extract fr` and `Also in B` notes are not expanded.

Exact-name OSS, employment/occupation, obituary, institutional, directory,
newspaper, military, and archival searches were reviewed for all 23 people.
The reviewed evidence bundle imports five sources, one reused organization,
one affiliation, 11 claims, 22 claim-source links, 24 person updates including
the linked Peery conflict, and 23 completed research attempts. Nine identity
decisions are recorded: seven accepted and two conflicting. The CIA cohort
adapter was robots-blocked before a search request. The Library of Congress
cohort run completed one no-result query and then encountered a timeout; these
are recorded as source-access limits rather than negative evidence. No
authenticated NARA Catalog API request was made.

## Reproducible coverage

| Measure | Count |
| --- | ---: |
| Printed index rows preserved and linked | 23,978 / 23,978 |
| Visually audited extraction | 23,978 / 23,978 rows; 522 / 522 pages |
| Active person entities | 23,939 |
| People with nonplanned research attempts | 10,234 (42.7503%) |
| People with confirmed/high employer evidence | 340 (1.4203%) |
| People with confirmed/high affiliation evidence | 764 (3.1914%) |
| Archival-review dispositions assessed | 8,693 (36.3131%) |
| Not started | 13,700 |
| Possible duplicate groups | 531 |
| Conflicts | 341 |
| Claims by confidence | confirmed 1,392; high 3,081; medium 1,551; low 198; conflicting 299; unresolved 2 |
| Citation records / unique source documents | 5,787 / 2,943 |

Research statuses are: blocked_by_source_access 1; candidate_found 333;
completed 194; conflicting_sources 294;
documented_prewar_employer_found 171; in_progress 1,902;
needs_identity_review 481; needs_temporal_review 24;
no_reliable_result_after_protocol 1,156; not_started 13,700;
occupation_only_found 1,050; requires_archival_review 4,339; and
verified_employer_found 294.

The public projection contains 23,939 person entities, 2,519 published
affiliations, 880 organizations, 4,563 public sources, and 6,316 published
claims. Full-index historical research remains unfinished.

## Local verification

The exact rebuilt tree passed these local release gates:

* Python unit suite: 139 / 139 passed.
* Ingest validation: all seven extraction and SQLite integrity checks passed.
* Stratified profile audit: 200 profiles across all four difficulty tiers and
  required personnel, confidence, duplicate, and conflict strata passed all
  seven structural checks.
* Astro diagnostics: 382 files, 0 errors, 0 warnings, 0 hints.
* Production build: 24,858 pages.
* Browser release suite: 84 / 84 checks passed across desktop, phone, and
  tablet, including 15 Batch 748, 33 core, six analytics, and 30 accessibility
  checks.
* Link check: 24,858 HTML files checked; every internal link resolved and
  50,797 unique external URLs were inventoried for the separate live check.
* Public manifest: 67 assets / 107,318,961 bytes verified; manifest SHA-256
  `05e9f066227058535937d7368ece9090bd988a4eea2493d9813a09ecc155f3f2`.
* Private-identifier audit: 12,926 normalized identifiers, 120 formatted
  variants, 24,930 public artifacts, and 1,239 candidate substrings checked;
  zero aggregate false positives, manifest-size false positives, or unexpected
  boundary matches.
* Two consecutive production builds reproduced the 24,930-file,
  310,166,877-byte output tree at SHA-256
  `b69894666f4cdec557280835ada919be0b51607c8278e1d8a640b5f14ac2d7e4`.

## Publication verification

Release commit
[`f2c4463f352f33e60beac7c16efff5a739cef496`](https://github.com/therealjameswilson/before-oss/commit/f2c4463f352f33e60beac7c16efff5a739cef496)
was pushed to `main` on 2026-10-11. The independent
[Test workflow](https://github.com/therealjameswilson/before-oss/actions/runs/38178469840)
and
[GitHub Pages workflow](https://github.com/therealjameswilson/before-oss/actions/runs/38178469881)
both completed successfully.

The immutable deployed-release verifier checked the public site against that
commit: 67 assets and 107,318,961 bytes matched manifest SHA-256
`05e9f066227058535937d7368ece9090bd988a4eea2493d9813a09ecc155f3f2`.
It also verified eight core routes, 31 source-register pages, and all 24 direct
profiles referenced by the evidence bundle. Cache-busted live checks confirmed
23,978 source rows, 23,939 people, 764 verified-affiliation people, 340
verified-employer people, 8,693 archival-review dispositions, and 13,700
not-started people.

The live Hart Perry profile displays the qualified University of Chicago
Master of Arts student affiliation and AM'39 evidence. The live Homer L Perry
and James B Perry profiles display the official-record name conflicts. The two
Robert Perry URLs remain separate and preserve their distinct `Extract fr` and
`Also in B` notes. The published site is
<https://therealjameswilson.github.io/before-oss/>.

GitHub emitted non-blocking platform notices that the selected actions are
being forced from deprecated Node.js 20 to Node.js 24 and that the
`ubuntu-latest` label is scheduled to move to Ubuntu 26. Neither notice caused
a test or deployment failure.

## Resume

~~~sh
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
python3 -m oss_research assign-page-batch --batch-name batch-748-perry-persky --page 364 --first-row 24 --last-row 46
python3 -m oss_research import-review-decisions research/identity_review_decisions_2026-10-11_batch748.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page364-perry-persky-review_batch-748_2026-10-11.json
python3 -m oss_research export-adapter-checkpoints
python3 -m oss_research export-derived
python3 -m oss_research export-review-queue
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
~~~

The next research boundary is PDF page 365, beginning with row 1, Edmund
Persons. No API key, raw API response, full service or officer number,
copyrighted page image, unrelated Army coded occupation, street address,
modern people-finder record, or private reviewer note is committed or
published.
