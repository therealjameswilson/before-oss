# Batch 658: Mileff-Miller research

The PDF-page 320 queue from `Christie E. Mileff` through `Alice E. Miller`
contains **22 source rows and 22 cautious person entities**. Every person has a
saved, reviewed outcome grounded in the NARA index, official Army bulk identity
comparison where applicable, exact-name OSS and employment searches, and
institutional, newspaper, obituary, directory, or archival checks as
applicable. No authenticated NARA Catalog request was made.

The CIA Reading Room adapter stopped at the collection's robots restriction;
that access failure was recorded and was not treated as a negative result. The
Library of Congress adapter stopped after a repeated transient 503; alternate
official and institutional sources were reviewed, and the failed request was
not represented as a negative search. The previously exposed API key remains
unused and must be rotated before authenticated NARA research resumes.

The reviewed findings preserve identity and temporal limits:

- **Newton Scott Miler** is confirmed by a direct 75-page federal OSS/SSU file.
  In August 1946 he was a Dartmouth College student and described himself as
  unemployed while still attending school. His Navy V-12/NROTC training ended
  on 1 July 1946. The public profile labels this as immediate pre-SSU status,
  not a wartime OSS employer or proof of wartime OSS service. Brief unnamed
  store jobs do not support a named employer claim.
- **Milton Edward Miles** is a high-confidence match to the career naval
  officer. His official Navy biography places him on the Navy Department
  Interior Control Board from July 1939 through March 1942, immediately before
  China command beginning 4 May 1942. The profile treats this as a military
  assignment and states that the biography does not provide a formal OSS
  transfer date.
- **Lloyd S. Millegan** has a high-confidence, evidence-bounded last civilian
  employer: the Library of Congress. A November 1942 scholarly byline gives
  that affiliation, and a 1960 newspaper chronology places Library employment
  after his 1939 graduation and before wartime Army service. The sources do not
  prove direct Library-to-OSS recruitment.
- **George Milkovich** is confirmed by a contemporary OSS personnel report.
  It explicitly dates Army entry, commissioning, and assignment to OSS on 10
  August 1943. It calls him a mechanical engineer in civilian life but names no
  company, so the result remains occupation-only.
- Six protected, nonshared Army matches establish high-confidence identities
  for Christie E. Mileff, Joseph M. Miles, Anthony J. Milikas, Harris R. Mill,
  Robert R. Millar, and Aaron H. Miller. Their coded Army occupations are not
  converted into employer claims.
- **Walter E. Millen** remains separate from a later **Walter Miller** row in
  Box 526 despite a shared protected identifier. The official Army entry names
  Millen, but neither indexed entity is merged or corrected before both
  personnel files are compared.
- The other eleven identities remain unresolved. An officer-class booklet
  containing William H. Miley's name lacked the identifiers and OSS context
  needed for acceptance. Each unresolved profile routes the question to Box
  523 or 524 without implying that no earlier employment existed.

The cohort ends with **17** `requires_archival_review`, three
`occupation_only_found`, one `documented_prewar_employer_found`, and one
`conflicting_sources` status. Identity statuses are two `confirmed`, eight
`high_confidence`, one `conflicting`, and eleven `unresolved`. The reviewed
bundle adds **18 claims**: seven confirmed, ten high, and one conflicting. It
adds five published affiliations and seven cited source documents. All eight
generated candidates received decisions: six accepted for identity and two
marked conflicting. Zero candidates remain unreviewed in the cohort.

Rebuilt coverage is **23,978/23,978** linked source rows and **23,939** active
person entities. Research-attempt coverage is **8,228/23,939 (34.3707%)**;
confirmed/high verified-employer coverage is **294/23,939 (1.2281%)**;
confirmed/high verified-affiliation coverage is **654/23,939 (2.7319%)**;
archival-review disposition coverage is **6,684/23,939 (27.9210%)**. There are
**15,706** `not_started` people, **498** possible-duplicate groups, and **200**
active conflicts. SQLite stores **14,332** attempts or plans and **5,235**
claims: 1,323 confirmed, 2,132 high, 1,416 medium, 189 low, and 175 conflicting.
It contains **5,195** citation records and **2,487** unique source documents.
The public projection contains **2,287** affiliations, **751** organizations,
**3,985** sources, and **5,042** claims.

The oil-company category remains prominent at the top of the personnel
directory and on its dedicated page. It remains evidence-scoped to **eight
people across ten historically named companies**; no Batch 658 identity-only
record is misclassified as oil-company employment. Full-index historical
research is unfinished.

## Replay and continuation

After importing prior durable batches into private SQLite:

```sh
python3 -m oss_research import-review-decisions research/identity_review_decisions_2026-09-23_batch658.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page320-mileff-miller-review_batch-658_2026-09-23.json
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
