# Batch 661: Miller research

The contiguous queue on PDF page 321 rows 34-46 and page 322 rows 1-9,
from `John B. Miller` through `Robert D. Miller`, contains **22 source rows and
22 cautious person entities**. Every person has a saved, reviewed outcome
grounded in the NARA index, official Army bulk identity comparison where
applicable, exact-name and rank or grade OSS searches, employment and
occupation searches, and institutional, newspaper, obituary, directory,
military-roster, or archival checks as applicable. No authenticated NARA
Catalog request was made.

Both page images were visually checked against all 22 stored rows. Page 322
row 8 visibly prints the note `possibly` beside Richard G. Miller; the raw note
and the resulting uncertainty remain visible. Unfamiliar grades such as `CBM`,
`PA`, and `P-2` were preserved rather than expanded without evidence.

The CIA Reading Room and Library of Congress adapter requests encountered
access or service errors and were not treated as negative results. Their
checkpoints remain in SQLite. The previously exposed NARA API key remains
unused and must be rotated before authenticated Catalog research resumes.

The reviewed findings preserve identity and chronology limits:

- Nonshared protected Army matches establish high-confidence identities for
  **Linwood R. Miller, Lou Miller, Morris I. Miller, Peter Miller, Richard G.
  Miller, and Robert D. Miller**. Army occupation codes remain private
  identity context and are not converted into employer claims.
- **Richard G. Miller** remains a high-priority archival review even with the
  strong Army comparison because the source index itself qualifies his row
  with `possibly`.
- **Raymond E. Miller** remains conflicting because the Army entry tied to the
  indexed protected identifier prints `MILLER RAY OND E`. The likely-looking
  spacing or transcription defect was not silently corrected, and no
  occupation evidence was transferred.
- **Perry G.E. Miller's** existing high-confidence identity and reviewed
  Harvard University last-civilian-employer chronology remain unchanged.
- The other 14 people lack enough corroborating identifiers or an OSS-to-
  employer bridge. Search results were dominated by modern professionals,
  common-name cemetery and obituary entries, and other military namesakes.
  Those leads were rejected rather than converted into claims.

The cohort ends with one `verified_employer_found`, one
`conflicting_sources`, and 20 `requires_archival_review` statuses. Identity
statuses are seven `high_confidence`, one `conflicting`, and 14 `unresolved`.
The reviewed bundle adds **seven claims**: six high and one conflicting. All
seven Army candidates received decisions: six accepted and one conflicting.
Zero candidates remain unreviewed in the cohort.

Rebuilt coverage is **23,978/23,978** linked source rows and **23,939** active
person entities. Research-attempt coverage is **8,293/23,939 (34.6422%)**;
confirmed/high verified-employer coverage is **295/23,939 (1.2323%)**;
confirmed/high verified-affiliation coverage is **655/23,939 (2.7361%)**;
archival-review disposition coverage is **6,749/23,939 (28.1925%)**. There are
**15,641** `not_started` people, **502** possible-duplicate groups, and **204**
active conflicts. SQLite stores **14,583** attempts or plans and **5,262**
claims: 1,323 confirmed, 2,153 high, 1,418 medium, 189 low, and 179
conflicting. It contains **5,206** citation records and **2,495** unique source
documents. The public projection contains **2,291** affiliations, **754**
organizations, **3,996** sources, and **5,069** claims.

The oil-company category remains prominent at the top of the personnel
directory and on its dedicated page. It remains evidence-scoped to **eight
people across ten historically named companies**; no Batch 661 identity-only
record or rejected modern oil-company namesake was misclassified as historical
oil-company employment. Full-index historical research is unfinished.

## Replay and continuation

After importing prior durable batches into private SQLite:

```sh
python3 -m oss_research import-review-decisions research/identity_review_decisions_2026-09-23_batch661.csv
python3 -m oss_research import-reviewed-evidence research/evidence-pages321-322-miller-review_batch-661_2026-09-23.json
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
python3 -m oss_research export-adapter-checkpoints
python3 -m oss_research export-derived
python3 -m oss_research export-review-queue
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
```

No API key, full service number, raw Catalog API response, copyrighted page
image, or private reviewer note is committed or included in the public site.
