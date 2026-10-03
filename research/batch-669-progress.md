# Batch 669: Molster-Monroe research

The next contiguous queue covers PDF page 325 rows 26-46 and page 326 row 1,
from `John S. Molster` through `Avary C. Monroe`. It contains **22 source rows
and 22 cautious person entities**. Every person now has a saved, reviewed
outcome grounded in the visually checked NARA index, official Army bulk
identity comparison where applicable, a policy-compliant CIA Reading Room
access attempt, live Library of Congress queries, exact-name and
meaningful-variant OSS searches, employment and occupation searches, and
institutional, newspaper, directory, obituary, military, or archival checks
as applicable. No authenticated NARA Catalog request was made.

The reviewed findings preserve identity, relationship, and chronology limits:

- **Negley C. Monett** is a probable match to the person listed in the 1938 and
  1941 Polk San Francisco directories. Those contemporary directories document
  work for the *San Francisco News*. The role is published as qualified,
  medium-confidence, documented prewar employment—not as the immediate pre-OSS
  affiliation or last civilian employer.
- **John J. Monigan** is a high-confidence match to Major John J. Monigan Jr.
  in the Harvard Law School Library Nuremberg Trials Project. The rare name,
  rank, and wartime context support the identity; the source does not establish
  a pre-OSS employer, and no later law firm is back-projected.
- Protected Army identifiers support high-confidence identity matches for
  **Joseph T. Molyson, George F. Monahan, Raymond D. Monahan, Earl M. Moncrief,
  John J. Mondale, Carmine Mongelluzzo, Paul J. Mongrain,** and **Cecil S.
  Monnin**. Army occupation codes remain private identity evidence and are
  never converted into employers. The official forms add `Jr.` for George F.
  Monahan and John J. Mondale; the variants are preserved.
- The official Army candidate for **Marcel P. Monier** names a different
  person and is rejected as a source or column-shift conflict. The protected
  identifier associated with **Billy B. Monk** points to `Billy D. Monk`; that
  middle-initial conflict remains visible and is not forced into a match.
- **Natalene Mongello** versus `Natelene Mengello` and **Avary C. Monroe**
  versus `Avary C. Munroe` remain separate possible-duplicate clusters. Neither
  pair is auto-merged without direct linkage.
- The index spelling **Robert P. Monlvx** is preserved exactly. It is not
  silently corrected to a more familiar surname.
- An 1873 newspaper hit for George F. Monahan is chronologically impossible,
  and a 1946 OCR hit for John J. Monigan concerns other names. Both were
  rejected. Later federal or Foreign Service references for John S. Molster,
  an independent OSS roster lead for Pasquale Mongelluzzo, and corroborative
  genealogy leads were not turned into employer claims.
- Every remaining unresolved person has an explicit Box 532 archival next
  action. Failed online research is not represented as evidence that no prior
  employment existed.

The bundle adds **11 claims, one affiliation, one organization, five sources,
23 claim-source links, and 22 reviewed research attempts**. Twelve generated
identity candidates received review decisions: eight exact or suffix-expanded
protected-identifier Army matches were accepted and four chronologically
impossible, wrong-name, OCR, or middle-initial-conflict candidates were
rejected. All 22 people have terminal batch outcomes: one
`documented_prewar_employer_found`, four `needs_identity_review`, eight
`no_reliable_result_after_protocol`, and nine `requires_archival_review`.
Batch identity outcomes are two `ambiguous`, two `conflicting`, nine
`high_confidence`, one `probable`, and eight `unresolved`.

Rebuilt coverage is **23,978/23,978** linked source rows and **23,939** active
person entities. Research-attempt coverage is **8,467/23,939 (35.3691%)**;
confirmed/high verified-employer coverage remains **300/23,939 (1.2532%)**;
confirmed/high verified-affiliation coverage remains **664/23,939 (2.7737%)**;
archival-review disposition coverage is **6,924/23,939 (28.9235%)**. There are
**15,467** `not_started` people, **512** possible-duplicate groups, and **218**
active conflicts. SQLite stores **15,104** attempts or plans and **5,369**
claims: 1,325 confirmed, 2,224 high, 1,433 medium, 196 low, and 191
conflicting. It contains **5,269** citation records and **2,545** unique source
documents. The public projection contains **2,315** affiliations, **767**
organizations, **4,053** sources, and **5,169** claims.

The oil-company category remains prominent at the top of the home page and
personnel directory and on its dedicated route. It remains evidence-scoped to
**eight people across ten historically named companies**. Batch 669 adds no
oil-company member. Full-index historical research is unfinished.

## Replay and continuation

After importing prior durable batches into private SQLite:

```sh
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
python3 -m oss_research import-review-decisions research/identity_review_decisions_2026-09-25_batch669.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page325-326-molster-monroe-review_batch-669_2026-09-25.json
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
