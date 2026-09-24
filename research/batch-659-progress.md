# Batch 659: Miller research

The contiguous queue across PDF page 320 rows 36-46 and page 321 rows 1-11,
from `Arthur R. Miller` through `Francis Miller`, contains **22 source rows
and 22 cautious person entities**. Every person has a saved, reviewed outcome
grounded in the NARA index, official Army bulk identity comparison where
applicable, exact-name and rank or grade OSS searches, employment and
occupation searches, and institutional, newspaper, obituary, directory,
military-roster, or archival checks as applicable. No authenticated NARA
Catalog request was made.

The CIA Reading Room adapter stopped at the collection's robots restriction;
that access failure was recorded and was not treated as a negative result. The
Library of Congress adapter stopped after a repeated service failure; direct
LoC web searches and other official or institutional sources were reviewed,
and the failed adapter request was not represented as a negative search. The
previously exposed API key remains unused and must be rotated before
authenticated NARA research resumes.

The reviewed findings preserve identity limits:

- Eight nonshared protected Army matches establish high-confidence identities
  for **Carl W. Miller, Claire D. Miller, Clarence A. Miller, David Miller,
  Edward N. Miller, Edwin Miller, Ernest L. Miller, and Francis Miller**.
  Coded Army occupations are not converted into employer claims. Ernest L.
  Miller's unusual coded entry date is not used to infer chronology.
- **Bernard L. Miller** remains conflicting because the Army entry tied to the
  indexed identifier spells the given name `Benard`. The project preserves
  both spellings pending review of the Box 524 jacket.
- **Eli D. Miller** remains conflicting because the Army entry tied to the
  indexed identifier instead names **Charles E. Tallent**. No Army occupation
  or identity evidence is transferred before the personnel file is compared.
- **Francis Pickens Miller** is rejected as the indexed corporal: the
  well-documented OSS figure was an officer, and no protected identifier links
  him to this row.
- Patent, city-directory, cemetery, obituary, company, newspaper, military,
  and genealogy leads for the remaining common names lacked a corroborating
  identifier or OSS bridge. They remain unlinked namesakes rather than
  published employers.
- The index's own `possible` note for initials-only **E. W. Miller** and
  `possibly` note for Yeoman First Class **Edwin J. Miller** remain visible
  and unresolved.
- **Captain Edward C. Miller** received enhanced officer disambiguation, but
  award lists and biographies still lacked a branch, unit, identifier, or
  Box 524 bridge.

The cohort ends with **20** `requires_archival_review` and two
`conflicting_sources` statuses. Identity statuses are eight
`high_confidence`, two `conflicting`, and twelve `unresolved`. The
reviewed bundle adds **10 identity claims**: eight high and two conflicting.
All ten generated Army candidates received decisions: eight accepted for
identity and two marked conflicting. Zero candidates remain unreviewed in the
cohort. No employer or affiliation claim was added.

Rebuilt coverage is **23,978/23,978** linked source rows and **23,939** active
person entities. Research-attempt coverage is **8,250/23,939 (34.4626%)**;
confirmed/high verified-employer coverage is **294/23,939 (1.2281%)**;
confirmed/high verified-affiliation coverage is **654/23,939 (2.7319%)**;
archival-review disposition coverage is **6,706/23,939 (28.0129%)**. There are
**15,684** `not_started` people, **500** possible-duplicate groups, and
**202** active conflicts. SQLite stores **14,380** attempts or plans and
**5,245** claims: 1,323 confirmed, 2,140 high, 1,416 medium, 189 low, and 177
conflicting. It contains **5,197** citation records and **2,488** unique source
documents. The public projection contains **2,287** affiliations, **751**
organizations, **3,987** sources, and **5,052** claims.

The oil-company category remains prominent at the top of the personnel
directory and on its dedicated page. It remains evidence-scoped to **eight
people across ten historically named companies**; no Batch 659 identity-only
record is misclassified as oil-company employment. Full-index historical
research is unfinished.

## Replay and continuation

After importing prior durable batches into private SQLite:

```sh
python3 -m oss_research import-review-decisions research/identity_review_decisions_2026-09-23_batch659.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page320-321-miller-review_batch-659_2026-09-23.json
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
```

Continue with the next bounded research batch, then run:

```sh
python3 -m oss_research export-adapter-checkpoints
python3 -m oss_research export-derived
python3 -m oss_research export-review-queue
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
```

No API key, full service number, raw Catalog API response, copyrighted page
image, or private reviewer note is committed or included in the public site.
