# Batch 683 release - Mosler-Moulder research

Research and local release date: 2026-09-25 America/New_York.

## Historical work

Batch 683 covers PDF page 332, rows 1-23, from Rudolf L Mosler through Helen L
Moulder. Fresh page inspection confirmed all 23 source rows, including the
truncated printed note `docume` for George L Mott. Every row remains linked to
its own person entity.

Geoffrey A. Mott-Smith receives a high-confidence immediate pre-OSS
professional affiliation. A contemporary *Chess Review* obituary explicitly
places his work as problem editor of *The Chess Correspondent* immediately
before his wartime summons to become an OSS cryptography and cryptanalysis
instructor. An ACBL bulletin corroborates his OSS role and documents his
earlier Bridge Bulletin editorship; his *Games Digest* editorship is also
published as an earlier prewar affiliation. None of those relationships is
silently converted into a paid-employment claim.

Independent Artillery OCS and Camp Ritchie rosters support Rudolf L. Mosler's
identity without establishing his immediate predecessor affiliation. Official
Army data supports George H Moss Jr., Frank P Motisi, and George L Mott as
high-confidence identities, but their protected identifiers and coded
occupations remain private and do not generate employer claims.

Arnando/Armando Mostachetti and Ervin E/S Mott remain public identity conflicts
under their respective protected identifiers. Lars Motland remains separate
from the page 326 Laro Montland row despite a shared identifier; both profiles
are in a visible duplicate-review group pending jacket comparison. The famous
artist May Mott-Smith is explicitly rejected as a name-only candidate, and
postwar Mario Motola records are not treated as pre-OSS evidence.

Nineteen people have terminal `no_reliable_result_after_protocol` outcomes,
three retain `conflicting_sources`, and Geoffrey Mott-Smith is `completed`. No
negative search result is represented as proof that prior employment did not
exist.

The featured oil-company category remains at the top of the home page and
personnel directory, with a dedicated category page and shareable filter. It
remains evidence-scoped to **eight people across ten historically named
companies**; ownership-only and unsupported associations remain excluded.

## Reproducible coverage

| Measure | Count |
| --- | ---: |
| Printed index rows preserved and linked | 23,978 / 23,978 |
| Visually audited extraction | 23,978 / 23,978 rows; 522 / 522 pages |
| Active person entities | 23,939 |
| People with nonplanned research attempts | 8,758 (36.5847%) |
| People with confirmed/high employer evidence | 307 (1.2824%) |
| People with confirmed/high affiliation evidence | 681 (2.8447%) |
| Archival-review dispositions assessed | 7,215 (30.1391%) |
| Not started | 15,176 |
| Possible duplicate groups | 514 |
| Conflicts | 239 |
| Attempts or plans | 15,799 |
| Claims by confidence | confirmed 1,329; high 2,351; medium 1,452; low 196; conflicting 212 |
| Citation records / unique source documents | 5,367 / 2,623 |

Research statuses are: `blocked_by_source_access` 1; `candidate_found` 333;
`completed` 153; `conflicting_sources` 196;
`documented_prewar_employer_found` 144; `in_progress` 1,904;
`needs_identity_review` 440; `needs_temporal_review` 23;
`no_reliable_result_after_protocol` 479; `not_started` 15,176;
`occupation_only_found` 1,034; `requires_archival_review` 3,783; and
`verified_employer_found` 273.

The public projection contains **2,347** published affiliations, **779**
organizations, **4,150** public sources, and **5,337** published claims.
Full-index historical research remains unfinished.

## Local verification

The exact rebuilt tree passed these release gates:

- Python unit suite: **139 / 139 passed**.
- Ingest validation: **23,978 / 23,978 rows**, **522 / 522 pages**, SQLite
  quick check `ok`, no foreign-key errors, and all parser-warning rows visually
  resolved.
- Stratified profile audit: **200 profiles**, with every identity, queue,
  commissioned-category, duplicate-review, source-row, and public-projection
  invariant passing.
- Astro diagnostics: **317 files**, **0 errors, 0 warnings, 0 hints**.
- Production build: **24,754 pages**.
- Browser release suite: **90 / 90 passed** across desktop, phone, and tablet
  (21 Batch 683, 33 core, 6 analytics, and 30 accessibility checks).
- Link check: **24,754 HTML files** checked; every internal link resolved and
  50,478 unique external URLs inventoried for the separate live check.
- Public manifest: **67 assets / 101,972,003 bytes** verified; manifest SHA-256
  `cb127c4963ee76afe51a568a48d86aca90250e6a0e5422207fab1df85e5a217c`.
- Private-identifier audit: **24,826 artifacts** scanned with **0 unexpected
  boundary matches**.
- Production dependency audit: **0 vulnerabilities**.
- Determinism: two consecutive build trees matched at **24,826 files /
  301,341,087 bytes**, SHA-256
  `9476505e49a5d5f7609ac330dbe2cd8fd6291cbf84ef7a66079bd27dd73c29c5`.

## Release status

Batch 683 is a local release candidate. It has not been pushed, merged, or
deployed. The public site continues to expose the previously deployed research
state and the already-live oil-company category.

## Resume

```sh
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
python3 -m oss_research import-review-decisions research/identity_review_decisions_2026-09-25_batch683.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page332-mosler-moulder-review_batch-683_2026-09-25.json
python3 -m oss_research export-adapter-checkpoints
python3 -m oss_research export-derived
python3 -m oss_research export-review-queue
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
```

No API key, raw API response, full service number, copyrighted page image,
unrelated Army coded occupation, or private reviewer note is committed or
published.
