# Batch 666: Mitchell-Mitrougenis research

The next contiguous queue covers PDF page 324 rows 6-27, from `Clark C.
Mitchell` through `Paul A. Mitrougenis`. It contains **22 source rows and 22
cautious person entities**. Every person now has a saved, reviewed outcome
grounded in the visually checked NARA index, official Army bulk identity
comparison where applicable, grouped CIA Reading Room and Library of Congress
checks, exact-name and meaningful-variant OSS searches, employment and
occupation searches, and institutional, newspaper, obituary, directory,
military, or archival checks as applicable. No authenticated NARA Catalog
request was made.

The reviewed findings preserve identity, relationship, and chronology limits:

- **Anne F. Mitcheson** is a high-confidence match to Anne F. Mitcheson
  (Henry) in the Sherborne School for Girls Old Girls' Union register. The
  chronological entry documents wartime censorship work in Liverpool,
  Manchester, and Bermuda before a Washington assignment with "four chiefs of
  staff" and OSS service. The censorship work is published as documented
  pre-OSS government work. The adjacent Washington entry is published only as
  a medium-confidence probable immediate affiliation because the source gives
  neither dates nor a named employing organization.
- The same register places Mitcheson's work as Assistant Personnel Manager at
  Asiatic Petroleum, New York, **after** her OSS service. That oil-company job
  is retained only as excluded identity context and does not make her a member
  of the site's pre-OSS oil-company category.
- Protected Army identifiers support high-confidence identity matches for
  **Denis M. Mitchell**, **Earl L. Mitchell Jr.**, and **Mack C. Mitchell**.
  Army occupation codes remain private identity evidence and are never
  converted into employers.
- **Dorothea D. Mitchell** and **Dorothy D. Mitchell** remain separate people.
  The adjacent index rows are not merged without direct evidence.
- Plausible namesakes for **John W. Mitchell** and postwar employment for
  **Louise Mithoff** are withheld from the pre-OSS findings because the
  identity or chronology does not meet the publication standard.
- The remaining 18 people receive explicit
  `no_reliable_result_after_protocol` outcomes and Box 529 or 530 archival next
  actions rather than unsupported biographies.

The bundle adds **six claims**, two affiliations, three sources, and ten
claim-source links. Thirty-nine generated candidates received review decisions:
three exact protected-identifier Army matches were accepted and 36 unbridged
Library of Congress candidates were rejected. All 22 people have terminal
batch outcomes: one `documented_prewar_employer_found`, 18
`no_reliable_result_after_protocol`, and three `requires_archival_review`.
Batch identity outcomes are four `high_confidence` and 18 `unresolved`.

Rebuilt coverage is **23,978/23,978** linked source rows and **23,939** active
person entities. Research-attempt coverage is **8,402/23,939 (35.0975%)**;
confirmed/high verified-employer coverage is **297/23,939 (1.2407%)**;
confirmed/high verified-affiliation coverage is **660/23,939 (2.7570%)**;
archival-review disposition coverage is **6,858/23,939 (28.6478%)**. There are
**15,532** `not_started` people, **511** possible-duplicate groups, and **215**
active conflicts. SQLite stores **14,905** attempts or plans and **5,326**
claims: 1,323 confirmed, 2,192 high, 1,429 medium, 192 low, and 190
conflicting. It contains **5,249** citation records and **2,528** unique source
documents. The public projection contains **2,304** affiliations, **759**
organizations, **4,035** sources, and **5,130** claims.

The oil-company category remains prominent at the top of the home page and
personnel directory and on its dedicated route. It remains evidence-scoped to
**eight people across ten historically named companies**. Batch 666 adds no
oil-company member because Mitcheson's Asiatic Petroleum employment was
post-OSS. Full-index historical research is unfinished.

## Replay and continuation

After importing prior durable batches into private SQLite:

```sh
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
python3 -m oss_research import-review-decisions research/identity_review_decisions_2026-09-24_batch666.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page324-mitchell-mitrougenis-review_batch-666_2026-09-24.json
python3 -m oss_research export-adapter-checkpoints
python3 -m oss_research export-derived
python3 -m oss_research export-review-queue
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
```

Adapter checkpoints must be imported before the final reviewed decisions and
evidence so temporary adapter states cannot supersede the batch's reviewed
research dispositions.

No API key, full service number, raw Catalog API response, copyrighted page
image, or private reviewer note is committed or included in the public site.
