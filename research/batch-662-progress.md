# Batch 662: Miller-Millett research

The contiguous queue on PDF page 322 rows 10-31, from `Robert L. Miller`
through `Stephen C. Millett`, contains **22 source rows and 21 cautious person
entities**. Every person has a saved, reviewed outcome grounded in the NARA
index, official Army bulk identity comparison where applicable, exact-name and
rank or grade OSS searches, employment and occupation searches, and
institutional, newspaper, obituary, military-roster, or archival checks as
applicable. No authenticated NARA Catalog request was made.

The page image was visually checked against all 22 stored rows. The printed
index gives the same protected identifier to Technician Fifth Grade Robert L.
Miller and Sergeant Robert H. Miller, so both remain separate and visibly
conflicted. It also prints two First Lieutenant William R. Miller rows, one in
Box 527 and one in Box 526 with the note `526/527`. Those source rows remain
immutable and separate while the evidence supports linking them to one cautious
person entity.

The CIA Reading Room search located a potentially relevant Stephen C. Millett
record, but the original document and PDF could not be inspected because the
links redirected during review. Its search-result text was not promoted into a
law-practice or employer claim. The Library of Congress and CIA adapter access
limits remain recorded as checkpoints rather than negative findings. The
previously exposed NARA API key remains unused and must be rotated before
authenticated Catalog research resumes.

The reviewed findings preserve identity and chronology limits:

- Nonshared protected Army matches establish high-confidence identities for
  **Robert E. Miller, Staff Sergeant Walter Miller, Walter H. Miller, William
  H. Miller, and William S. Miller**. Army occupation codes remain private
  identity context and are not converted into employer claims.
- **Technician Fifth Grade Robert L. Miller** is a probable Army match, not a
  high-confidence one, because the index prints the same protected identifier
  for Robert H. Miller.
- **Robert H. Miller, Technician Sergeant Robert L. Miller, Stuart D. Miller,
  Victor L. Miller, and the unranked Walter Miller** remain conflicting. Each
  has a shared identifier, a mismatching official Army name, or both. Victor's
  exact name and grade in the Greek Operational Group roster corroborate an OSS
  context but do not override the official Army-identifier conflict.
- **William R. Miller** is high confidence as one cautious person represented
  by two preserved index rows; neither row supplies employment evidence.
- A directly inspected 2005 *Texas Jewish Post* obituary explicitly sequences
  **Roberta Miller's** work as Edward R. Murrow's assistant at CBS before her
  move to Washington and OSS work. The rare name, civilian index grade, and
  chronology support a qualified medium-confidence immediate pre-OSS and last
  civilian employer finding, but the Box 526 personnel file is still needed
  for confirmation.
- **Stephen C. Millett** and the seven other unresolved people remain routed to
  archival review rather than receiving unsupported biographical claims.

The cohort ends with five `conflicting_sources`, one
`documented_prewar_employer_found`, and 15 `requires_archival_review` statuses.
Identity statuses are six `high_confidence`, two `probable`, five
`conflicting`, and eight `unresolved`. The reviewed bundle adds **13 claims**:
six high, two medium, and five conflicting. All 16 generated candidates have
decisions: five accepted, one probable, and ten conflicting. Zero candidates
remain unreviewed in the cohort.

Rebuilt coverage is **23,978/23,978** linked source rows and **23,939** active
person entities. Research-attempt coverage is **8,314/23,939 (34.7299%)**;
confirmed/high verified-employer coverage is **295/23,939 (1.2323%)**;
confirmed/high verified-affiliation coverage is **655/23,939 (2.7361%)**;
archival-review disposition coverage is **6,770/23,939 (28.2802%)**. There are
**15,620** `not_started` people, **505** possible-duplicate groups, and **209**
active conflicts. SQLite stores **14,669** attempts or plans and **5,275**
claims: 1,323 confirmed, 2,159 high, 1,420 medium, 189 low, and 184
conflicting. It contains **5,210** citation records and **2,497** unique source
documents. The public projection contains **2,292** affiliations, **754**
organizations, **4,000** sources, and **5,082** claims.

The oil-company category remains prominent at the top of the personnel
directory and on its dedicated page. It remains evidence-scoped to **eight
people across ten historically named companies**; no Batch 662 identity-only
record was misclassified as historical oil-company employment. Full-index
historical research is unfinished.

## Replay and continuation

After importing prior durable batches into private SQLite:

```sh
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
python3 -m oss_research import-review-decisions research/identity_review_decisions_2026-09-23_batch662.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page322-miller-millett-review_batch-662_2026-09-23.json
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
