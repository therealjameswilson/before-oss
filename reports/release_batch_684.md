# Batch 684 release - Moulton-Moye research

Research and local release date: 2026-09-25 America/New_York.

## Historical work

Batch 684 covers PDF page 332, rows 24-46, from Albert Moulton through Leon L
Moye. Fresh page inspection confirmed all 23 printed rows. Every row remains
linked to its own person entity and its original spelling remains recoverable.

Official NARA and Marine Corps sources support a high-confidence identity for
John A. Mowinckel and document earlier employment as head of European
operations for the Standard Oil Company of New Jersey. The site presents that
role as documented prewar employment, not as an immediate predecessor, because
the accessible evidence does not supply the transition date. The featured
oil-company category now contains **nine people across 11 historically named
companies**.

John W. Mowinckel remains a separate, confirmed person. His official Marine
Corps history supports the full name John Wallendahl Mowinckel, Princeton
student status, Marine Corps Reserve service and subsequent OSS detail. The
Marine Corps Reserve is modeled as his immediate predecessor; Princeton is not
an employer and his father's Standard Oil employment is not transferred to
him.

The index's Andre G Mourqet conflicts with an official 1945 OSS award roster
that prints Andre G. Mourquet and an identifier differing by one digit. Andrew
S Mousilinas/Mousalimas, Frederick O Moussean/Mousseau, Frank Mowinski/Clyde E
White and Arno D/P Mowitz Jr. remain separate, visible official-record
conflicts. Full protected identifiers remain private.

Official Army data supports bounded high-confidence identities for Chin M Mow
and James T Moy without generating employer claims. Official French archival
inventories support Thérèse Joséphine Mouzon, also Thérèse André, while the
uncommon exact name and official institutional sources support Edgar A.
Mowrer. Neither receives an unsupported employer or immediate-predecessor
claim.

Clarence Moy receives a high-confidence identity and two visibly qualified,
medium-confidence pathway claims: the United States Army as his immediate
pre-OSS affiliation and the Territory of Hawaii Department of Institutions,
where he worked as a social worker, as his last civilian employer before Army
service. A personnel jacket and territorial personnel records are still
needed for firmer dating.

Potential famous-person or exact-name leads for Thomas T. Moulton, Chris G.
Moustakis, Gaston Mousis and Leon L. Moye were rejected because no second
identifier connected them to the index. The Atlanta Gas Light yearbook lead
is visible as a rejected identity lead on Leon Moye's profile but is not
published as an affiliation.

Fifteen people have terminal `no_reliable_result_after_protocol` outcomes,
five retain `conflicting_sources`, two have
`documented_prewar_employer_found`, and John W. Mowinckel is `completed`. No
negative search result is represented as proof that prior employment did not
exist. CIA robots restrictions and a bounded Library of Congress adapter
timeout are recorded as source-access limitations rather than negative
evidence.

## Reproducible coverage

| Measure | Count |
| --- | ---: |
| Printed index rows preserved and linked | 23,978 / 23,978 |
| Visually audited extraction | 23,978 / 23,978 rows; 522 / 522 pages |
| Active person entities | 23,939 |
| People with nonplanned research attempts | 8,781 (36.6807%) |
| People with confirmed/high employer evidence | 308 (1.2866%) |
| People with confirmed/high affiliation evidence | 683 (2.8531%) |
| Archival-review dispositions assessed | 7,238 (30.2352%) |
| Not started | 15,153 |
| Possible duplicate groups | 514 |
| Conflicts | 244 |
| Attempts or plans | 15,916 |
| Claims by confidence | confirmed 1,332; high 2,358; medium 1,454; low 196; conflicting 217 |
| Citation records / unique source documents | 5,380 / 2,633 |

Research statuses are: `blocked_by_source_access` 1; `candidate_found` 333;
`completed` 154; `conflicting_sources` 201;
`documented_prewar_employer_found` 146; `in_progress` 1,904;
`needs_identity_review` 440; `needs_temporal_review` 23;
`no_reliable_result_after_protocol` 494; `not_started` 15,153;
`occupation_only_found` 1,034; `requires_archival_review` 3,783; and
`verified_employer_found` 273.

The public projection contains **2,352** published affiliations, **784**
organizations, **4,163** public sources, and **5,354** published claims.
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
- Astro diagnostics: **318 files**, **0 errors, 0 warnings, 0 hints**.
- Production build: **24,759 pages**.
- Browser release suite: **99 / 99 passed** across desktop, phone, and tablet
  (30 Batch 684, 33 core, 6 analytics, and 30 accessibility checks).
- Link check: **24,759 HTML files** checked; every internal link resolved and
  50,489 unique external URLs inventoried for the separate live check.
- Public manifest: **67 assets / 102,100,744 bytes** verified; manifest SHA-256
  `24e791c6978f60f70ff0269600474b45c6cbd63d7ddcd8a99f1565b27efbf7f4`.
- Private-identifier audit: **24,831 artifacts** scanned with **0 unexpected
  boundary matches**.
- Production dependency audit: **0 vulnerabilities**.
- Determinism: two consecutive build trees matched at **24,831 files /
  301,556,848 bytes**, SHA-256
  `26f8a73b41b34e734cffcfc4e6e63364508b4b63268baee2aaf933735bcd6837`.

## Release status

Batch 684 is a local release candidate. It has not been pushed, merged, or
deployed. The public site continues to expose the previously deployed research
state and the already-live oil-company category; the ninth cited person is
present only in this local candidate until an authorized deployment.

## Resume

```sh
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
python3 -m oss_research import-review-decisions research/identity_review_decisions_2026-09-25_batch684.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page332-moulton-moye-review_batch-684_2026-09-25.json
python3 -m oss_research export-adapter-checkpoints
python3 -m oss_research export-derived
python3 -m oss_research export-review-queue
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
```

No API key, raw API response, full service number, copyrighted page image,
unrelated Army coded occupation, or private reviewer note is committed or
published.
