# Batch 682 release - Mory-Mosler research

Research and local release date: 2026-09-25 America/New_York.

## Historical work

Batch 682 completes PDF page 331, rows 24-46, from Chalen Mory through Rosa
Mosler. Fresh page inspection confirmed all 23 source rows. Philip E Mosely's
prior verified Cornell and COI findings remain intact; 22 other people receive
new terminal research outcomes.

Four protected-identifier-supported Army matches were accepted for George
Moschinsky, Robert K Mosher, Jerome J Moskol, and Theodore Moskowitz. The coded
occupations were not promoted into employer claims.

Jacob L. Mosak receives a high-confidence University of Chicago last-civilian-
employer claim, kept separate from his documented Office of Price
Administration government assignment. Amos D. Moscrip Jr. receives a
high-confidence Army immediate pathway and earlier 101st Anti-Tank Battalion
assignment, with no civilian employer invented. Edward A. Mosk's private legal
practice is published as a medium-confidence last civilian self-employment
claim; no law firm is named.

John Moseley remains separate from Philip E. Mosely despite an official
declassification-review note calling one historical reference a probable
error. Peter M. Moshopoulos remains separate from the earlier Peter M.
Mishopoulos index row despite their shared protected identifier. Both cases
are public conflicts requiring personnel-jacket review.

Seventeen people have terminal `no_reliable_result_after_protocol` outcomes,
two retain `conflicting_sources`, Amos Moscrip is `completed`, Edward Mosk has
`documented_prewar_employer_found`, Jacob Mosak has
`verified_employer_found`, and Philip Mosely retains
`verified_employer_found`. No negative search result is represented as proof
that prior employment did not exist.

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
| People with nonplanned research attempts | 8,736 (36.4928%) |
| People with confirmed/high employer evidence | 307 (1.2824%) |
| People with confirmed/high affiliation evidence | 680 (2.8406%) |
| Archival-review dispositions assessed | 7,192 (30.0430%) |
| Not started | 15,198 |
| Possible duplicate groups | 514 |
| Conflicts | 236 |
| Attempts or plans | 15,776 |
| Claims by confidence | confirmed 1,329; high 2,343; medium 1,452; low 196; conflicting 209 |
| Citation records / unique source documents | 5,361 / 2,618 |

Research statuses are: `blocked_by_source_access` 1; `candidate_found` 333;
`completed` 152; `conflicting_sources` 193;
`documented_prewar_employer_found` 144; `in_progress` 1,905;
`needs_identity_review` 440; `needs_temporal_review` 23;
`no_reliable_result_after_protocol` 460; `not_started` 15,198;
`occupation_only_found` 1,034; `requires_archival_review` 3,783; and
`verified_employer_found` 273.

The public projection contains **2,344** published affiliations, **776**
organizations, **4,144** public sources, and **5,326** published claims.
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
- Astro diagnostics: **316 files**, **0 errors, 0 warnings, 0 hints**.
- Production build: **24,751 pages**.
- Browser release suite: **93 / 93 passed** across desktop, phone, and tablet
  (24 Batch 682, 33 core, 6 analytics, and 30 accessibility checks).
- Link check: **24,751 HTML files** checked; every internal link resolved and
  50,471 unique external URLs inventoried for the separate live check.
- Public manifest: **67 assets / 101,899,881 bytes** verified; manifest SHA-256
  `ab6709ec2b6a22583b166429d7adf6e48e4c7515b1564ab4fc8a0c1df5440203`.
- Private-identifier audit: **24,823 artifacts** scanned with **0 unexpected
  boundary matches**.
- Production dependency audit: **0 vulnerabilities**.
- Determinism: two consecutive build trees matched at **24,823 files /
  301,217,145 bytes**, SHA-256
  `56d783f710202101af001b3bef8445b4754b8ecfc631e1dba77e0aba9bdf0769`.

## Release status

Batch 682 is a local release candidate. It has not been pushed, merged, or
deployed. The public site continues to expose the previously deployed research
state and the already-live oil-company category.

## Resume

```sh
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
python3 -m oss_research import-review-decisions research/identity_review_decisions_2026-09-25_batch682.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page331-mory-mosler-review_batch-682_2026-09-25.json
python3 -m oss_research export-adapter-checkpoints
python3 -m oss_research export-derived
python3 -m oss_research export-review-queue
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
```

No API key, raw API response, full service number, copyrighted page image,
unrelated Army coded occupation, or private reviewer note is committed or
published.
