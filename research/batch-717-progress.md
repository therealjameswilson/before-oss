# Batch 717: Olafsen-Oliver research

Batch 717 covers PDF page 349, rows 1-23, from **Paul N Olafsen** through
**Louise L Oliver**. A 300-dpi visual inspection confirmed all 23 printed
rows, representing 23 active person entities. The immutable extraction is
unchanged. Original spellings, ranks, box numbers, notes, and archival
locations remain recoverable. Every row is in Box 571 at location
230/86/37/07.

Seven people receive accepted identity matches from the official Army bulk
file: **Paul N Olafsen**, **Karl L Olberg**, **David Oldashi**, **Ross C
Oldford**, **John G Oldiges**, **Arthur R Oldrey**, and **Darwin G Oliver**.
Each match uses the exact printed name plus a nonshared protected identifier.
The identifier remains private, and no coded Army occupation was converted
into an occupation or employer claim.

**James H Oliver** is probably the classicist James Henry Oliver. The exact
name and middle initial, indexed major rank, Barnard College career ending in
1942, wartime gap, and 1946 return to academic employment form a coherent
chronology. Columbia's 1936 annual report announces his appointment as an
assistant professor responsible for ancient history, while the Rutgers
Database of Classical Scholars dates the Barnard employment from 1936 through
1942. Because no direct personnel-file or unique-identifier bridge was found,
the identity and Barnard claim remain `probable` / `medium` and visibly
qualified. Barnard is modeled as the likely last civilian employer before
wartime service, not as the immediate pre-OSS affiliation.

**George T Olden** is not silently merged with the famous OSS graphic designer
Georg Olden. The index row visibly prints middle initial `T`, while the
biographical candidate was George Elliott Olden. The CIA source establishes
that Georg Olden served as an OSS graphic designer, but supplies no bridge to
the indexed Box 571 row. The profile therefore publishes the identity conflict
and withholds the designer's student and career history from this entity.

**Roy A Oleary** and **Roy A Olerud** remain separate source-derived entities.
Fresh visual inspection confirms that the adjacent rows share a protected
identifier despite materially different surnames. Contemporary trade sources
give Olerud a coherent postwar broadcast-engineering career, but do not
establish prewar employment or resolve the duplicate. The two profiles share a
possible-duplicate group and require comparison of both Box 571 files before
any merge or spelling correction.

The printed `one fold` note for Courtenay Olden and `also AS` note for David A
Olds remain recoverable without expansion. Both require archival examination.
Common-name and incomplete-identifier cases remain unresolved rather than
being attached to convenient biographies.

The CIA and Library of Congress adapters each made one bounded attempt and
failed closed. The web adapter recorded 23 deterministic planned queries
without making live requests. Manual staged review completed official,
exact-name OSS, employment, occupation, obituary, institutional, newspaper,
directory, military, and archival search families for every person.

The cohort ends with 17 `no_reliable_result_after_protocol`, three
`conflicting_sources`, two `requires_archival_review`, and one
`documented_prewar_employer_found` outcome. Identity statuses are seven
`high_confidence`, 12 `unresolved`, two `probable`, one `ambiguous`, and one
`conflicting`. The reviewed bundle imports six sources, one organization, one
affiliation, 10 claims, 22 claim-source links, 23 person updates, and 23
consolidated research attempts. Seven accepted identity-review decisions are
recorded.

Rebuilt coverage is **23,978/23,978** linked source rows and **23,939** active
person entities. Research-attempt coverage is **9,529/23,939 (39.8053%)**;
confirmed/high verified-employer coverage is **326/23,939 (1.3618%)**;
confirmed/high verified-affiliation coverage is **724/23,939 (3.0244%)**;
archival-review disposition coverage is **7,987/23,939 (33.3640%)**. There are
**14,405** `not_started` people, **523** possible-duplicate groups, and **299**
active conflicts. SQLite stores **17,310** attempts or plans and **6,127**
claims: 1,352 confirmed, 2,809 high, 1,508 medium, 198 low, 258 conflicting,
and two unresolved. It contains **5,596** citation records and **2,809** unique
source documents. The public projection contains **2,438** affiliations,
**843** organizations, **4,377** sources, and **5,920** claims. Full-index
historical research remains unfinished.

## Replay and continuation

After importing prior durable batches into private SQLite:

```sh
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
python3 -m oss_research assign-page-batch --batch-name batch-717 --page 349 --first-row 1 --last-row 23
python3 -m oss_research research --source cia --batch batch-717 --max-queries 23
python3 -m oss_research research --source loc --batch batch-717 --max-queries 23
python3 -m oss_research research --source web --batch batch-717 --resume --max-queries 23 --dry-run
python3 -m oss_research import-review-decisions research/identity_review_decisions_2026-10-04_batch717.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page349-olafsen-oliver-review_batch-717_2026-10-04.json
python3 -m oss_research export-adapter-checkpoints
python3 -m oss_research export-derived
python3 -m oss_research export-review-queue
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
```

Adapter checkpoints must be imported before final reviewed decisions and
evidence so temporary discovery states cannot supersede reviewed dispositions.
The next research boundary begins at PDF page 349, row 24 (Maida O Oliver) and
runs through row 46 (Clinton L Olson).

No API key, full service number, raw Catalog or LoC API response, copyrighted
page image, unrelated Army coded occupation, street address, modern
people-finder record, or private reviewer note is committed or included in the
public site. No authenticated NARA Catalog API request was made for this batch.
