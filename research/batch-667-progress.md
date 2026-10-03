# Batch 667: Mitschke-Moefred research

The next contiguous queue covers PDF page 324 rows 28-46 and page 325 rows
1-3, from `Clinton E. Mitschke` through `Victor W. Moefred`. It contains **22
source rows and 22 cautious person entities**. Every person now has a saved,
reviewed outcome grounded in the visually checked NARA index, official Army
bulk identity comparison where applicable, grouped CIA Reading Room and
Library of Congress checks, exact-name and meaningful-variant OSS searches,
employment and occupation searches, and institutional, newspaper, obituary,
directory, military, or archival checks as applicable. No authenticated NARA
Catalog request was made.

The reviewed findings preserve identity, relationship, and chronology limits:

- **Henry H. Miwa** is a high-confidence match to Henry Hideo Miwa. The
  Buddhist Churches of America history and contemporary Japanese American
  press document his 1934-1942 service as executive secretary of the Fresno
  Buddhist Church or Fresno Betsuin, published as his last documented civilian
  employer before wartime service. A separate institutional record explicitly
  documents later OSS interpreter service.
- The adjacent **Hideo Miwa** row remains a separate ambiguous person in a
  possible-duplicate group. The records are not merged without protected
  identifiers, personnel-file evidence, or another direct bridge.
- **Tetsuo S. Miyakawa** is a high-confidence match to Tetsuo Scott Miyakawa.
  Archival and institutional sources document work for the South Manchurian
  Railway Office in New York from 1931 to 1940 or 1941. It is published only
  as documented prewar employment because a later unnamed marketing or public
  relations employer intervened before wartime service.
- **Eric E. Mockler-Ferrt** is a high-confidence match to Brigadier Eric Edward
  Mockler-Ferryman. His War Office, Home Forces, Allied Force Headquarters,
  Special Operations Executive, and joint SOE-OSS Special Force assignments
  are published as an Allied military pathway, not as civilian employment.
- **Rudolf Modley** is confirmed by an article that cites his exact RG 226,
  Entry 224, Box 531 personnel-file location. Pictorial Statistics and
  Pictograph Corporation are separated from his later Coordinator of
  Information consulting affiliation; the chronology is not collapsed into a
  generic employer field.
- Protected Army identifiers support high-confidence identity matches for
  **Ernest Mitzner**, **Joseph J. Modiz**, and **Irwin Moed**. Army occupation
  codes remain private identity evidence and are never converted into
  employers.
- The proposed Army match for **Kazyu C. Miyadira** conflicts with the official
  name `MIYABARA KAZUO C`. The disagreement is public and excluded from default
  analytics rather than silently corrected.
- Plausible leads for **Shotaro F. Miyamoto**, **James Moe**, and **Edward O.
  Moe** remain private or qualified because the identity or employment bridge
  does not meet the publication threshold.

The bundle adds **21 claims, 11 affiliations, 10 organizations, 12 sources,
37 claim-source links, and 22 reviewed research attempts**. Seven generated
identity candidates received review decisions: three exact protected-identifier
Army matches were accepted, one conflicting name was retained as a conflict,
and three unbridged or wrong-name candidates were rejected. All 22 people have
terminal batch outcomes: one `completed`, one `conflicting_sources`, two
`documented_prewar_employer_found`, four `needs_identity_review`, ten
`no_reliable_result_after_protocol`, three `requires_archival_review`, and one
`verified_employer_found`. Batch identity outcomes are one `ambiguous`, one
`confirmed`, one `conflicting`, six `high_confidence`, three `probable`, and
ten `unresolved`.

Rebuilt coverage is **23,978/23,978** linked source rows and **23,939** active
person entities. Research-attempt coverage is **8,424/23,939 (35.1894%)**;
confirmed/high verified-employer coverage is **300/23,939 (1.2532%)**;
confirmed/high verified-affiliation coverage is **664/23,939 (2.7737%)**;
archival-review disposition coverage is **6,880/23,939 (28.7397%)**. There are
**15,510** `not_started` people, **512** possible-duplicate groups, and **216**
active conflicts. SQLite stores **14,971** attempts or plans and **5,347**
claims: 1,325 confirmed, 2,206 high, 1,429 medium, 196 low, and 191
conflicting. It contains **5,261** citation records and **2,539** unique source
documents. The public projection contains **2,313** affiliations, **766**
organizations, **4,045** sources, and **5,147** claims.

The oil-company category remains prominent at the top of the home page and
personnel directory and on its dedicated route. It remains evidence-scoped to
**eight people across ten historically named companies**. Batch 667 adds no
oil-company member. Full-index historical research is unfinished.

## Replay and continuation

After importing prior durable batches into private SQLite:

```sh
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
python3 -m oss_research import-review-decisions research/identity_review_decisions_2026-09-24_batch667.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page324-mitschke-moe-page325-moefred-review_batch-667_2026-09-24.json
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
