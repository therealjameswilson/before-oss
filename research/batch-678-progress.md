# Batch 678: Morgan-Mori research

Batch 678 completes PDF page 329, rows 25-46, from `Horace F Morgan` through
`Charles Y Mori`. Fresh rendered-page inspection and layout-text comparison
confirmed all 22 printed rows, the transition from Box 537 to Box 538, and the
separate adjacent `Melvin Morgan` and `Melvin Morgen` entries.

Seven reviewed Army candidates support accepted identities: **Horace F
Morgan, Joseph E Morgan, Morgan H Morgan, Ralph D Morgan, Raymond F Morgan,
Thomas B Morgan, and Melvin Morgen**. Six are high-confidence identities;
Melvin Morgen is tied to the exact Army name but remains linked to a duplicate
warning because the adjacent Melvin Morgan row carries the same protected
identifier. Melvin Morgan remains a probable, ambiguous match pending Box 538
review. The Army candidate for Stern S Morgen was rejected because the record
actually names `MORGENSTEM SAMUEL`. No coded Army occupation was converted
into an employer.

The strongest employment finding concerns **Shepard Morgan**. A 1941 National
Bureau of Economic Research institutional roster names him as a vice-president
of Chase National Bank, while Barry M. Katz's scholarly history places Shepard
Morgan directing R&A/London when it opened in May 1942. Chase is therefore
published as the last identified civilian employer with a `strongly_date_bounded`
temporal basis, not as an explicitly documented immediate pre-OSS affiliation.
His separate NBER office is not conflated with bank employment.

An official NARA JFK-release document names **Mrs Thelma Morgan** and records
an approved Unit Commander's Certificate of Merit. Because the common name is
not joined to the index row by a unique identifier, this remains a qualified
probable identity lead and requires Box 538 review. Nearby text about an
administrative assistant belongs to Doris C. Pearse and was not attributed to
Morgan.

Sixteen people reached `no_reliable_result_after_protocol`; two remain in
`needs_identity_review`, one in `requires_archival_review`, one has an
`occupation_only_found` outcome, and two retain `verified_employer_found`
outcomes. Each negative online result is framed as an accessible-source result,
not proof that no prior employment existed.

The staged protocol covered the official NARA index, the official Army bulk
file where applicable, targeted official CIA-domain searches, exact-name OSS
and employment searches, 42 Library of Congress discovery candidates,
institutional and obituary sources, newspapers, directories, and archival
discovery. The direct CIA adapter failed closed once and was not counted as
negative evidence. All 42 Library of Congress candidates were rejected as
name-only or surname-only newspaper OCR leads without a corroborating OSS,
protected-identifier, or archival bridge. Together with the Stern Morgen Army
mismatch, the review file preserves **51 decisions: 7 accepted, 1 probable,
and 43 rejected**.

The evidence bundle imports five sources, one organization, one affiliation,
10 claims, 21 claim-source links, 22 person updates, and 22 consolidated
research attempts. The featured oil-company category remains evidence-scoped
to **eight people across ten historically named companies**. Chase National
Bank is a bank and does not qualify for that category.

Rebuilt coverage is **23,978/23,978** linked source rows and **23,939** active
person entities. Research-attempt coverage is **8,646/23,939 (36.1168%)**;
confirmed/high verified-employer coverage is **305/23,939 (1.2741%)**;
confirmed/high verified-affiliation coverage is **674/23,939 (2.8155%)**;
archival-review disposition coverage is **7,102/23,939 (29.6671%)**. There
are **15,288** `not_started` people, **512** possible-duplicate groups, and
**229** active conflicts. SQLite stores **15,635** attempts or plans and
**5,468** claims: 1,326 confirmed, 2,304 high, 1,440 medium, 196 low, and 202
conflicting. It contains **5,327** citation records and **2,592** unique source
documents. The public projection contains **2,328** affiliations, **772**
organizations, **4,110** sources, and **5,265** claims. Full-index historical
research remains unfinished.

## Replay and continuation

After importing prior durable batches into private SQLite:

```sh
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
python3 -m oss_research import-review-decisions research/identity_review_decisions_2026-09-25_batch678.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page329-morgan-mori-review_batch-678_2026-09-25.json
python3 -m oss_research export-adapter-checkpoints
python3 -m oss_research export-derived
python3 -m oss_research export-review-queue
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
```

Adapter checkpoints must be imported before the final reviewed decisions and
evidence so temporary discovery states cannot supersede reviewed dispositions.

No API key, full service number, raw Catalog API response, copyrighted page
image, unrelated Army name, or private reviewer note is committed or included
in the public site.
