# Batch 686: Mueller-Mullaney research

Batch 686 covers PDF page 333, rows 24-46, from `Gustave A Mueller` through
`George E Mullaney`. Fresh visual inspection and layout-text comparison
confirmed all 23 printed rows. Every source row remains linked to its own
person entity and the original index spelling remains recoverable.

Official Army bulk data supports eight high-confidence identities: **John P.
Muench, Armando J. Muglia, Wallace S. Mukai, Gust Mukanos, William L. Mulcahy,
Cornelius A. Mulder, John L. Mulford, and George E. Mullaney**. Each decision
combines an exact name with a nonshared protected identifier. The decisions
establish identity only; protected identifiers remain private and coded Army
occupations are not translated into employers.

A South Jersey Times obituary independently identifies **John Louis "Jack"
Mulford** and explicitly documents both Army and OSS service. It also dates his
ownership of Mulford Tire to 1945. That business is retained as a rejected
postwar employer lead, not promoted into a pre-OSS claim.

A NARA-derived roster independently documents **Gust Mukanos** with Greek
Operational Group V. The roster supports his wartime identity and OSS context,
but it does not establish a pre-OSS employer or predecessor affiliation. No
employment claim is inferred from the unit roster.

The other fifteen identities remain unresolved after staged official,
exact-name OSS, employment, institutional, newspaper, obituary, directory,
and archival searches. Plausible candidates were rejected when no sufficient
identity bridge or pre-OSS chronology connected them to the index. A negative
online result is not represented as proof that prior employment did not exist.
All 23 profiles therefore receive the terminal
`no_reliable_result_after_protocol` status and guidance to the indexed Box
544-545 personnel files.

The evidence bundle imports four sources, no organizations, no affiliations,
31 identity and research-disposition claims, 51 claim-source links, 23 person
updates, and 23 consolidated research attempts. Eight reviewed Army candidate
decisions are preserved separately and accepted as identity matches only.

Rebuilt coverage is **23,978/23,978** linked source rows and **23,939** active
person entities. Research-attempt coverage is **8,827/23,939 (36.8729%)**;
confirmed/high verified-employer coverage is **308/23,939 (1.2866%)**;
confirmed/high verified-affiliation coverage is **685/23,939 (2.8614%)**;
archival-review disposition coverage is **7,284/23,939 (30.4273%)**. There are
**15,107** `not_started` people, **514** possible-duplicate groups, and **246**
active conflicts. SQLite stores **15,985** attempts or plans and **5,603**
claims: 1,336 confirmed, 2,397 high, 1,455 medium, 196 low, and 219 conflicting.
It contains **5,390** citation records and **2,641** unique source documents.
The public projection contains **2,356** affiliations, **788** organizations,
**4,173** sources, and **5,400** claims. The featured oil-company category
remains **nine people across 11 historically named companies**. Full-index
historical research remains unfinished.

## Replay and continuation

After importing prior durable batches into private SQLite:

```sh
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
python3 -m oss_research import-review-decisions research/identity_review_decisions_2026-10-01_batch686.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page333-mueller-mullaney-review_batch-686_2026-10-01.json
python3 -m oss_research export-adapter-checkpoints
python3 -m oss_research export-derived
python3 -m oss_research export-review-queue
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
```

Adapter checkpoints must be imported before final reviewed decisions and
evidence so temporary discovery states cannot supersede reviewed dispositions.

No API key, full service number, raw Catalog API response, copyrighted page
image, unrelated Army coded occupation, or private reviewer note is committed
or included in the public site.
