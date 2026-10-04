# Batch 729: Page-Pallay research

Batch 729 covers PDF page 355, rows 1-23, from **William R Page** through
**George Pallay**. A 300-dpi visual inspection confirmed all 23 printed rows,
representing 23 active person entities in Box 581 at location 230/86/38/01.
Embedded text was checked against the render, and original spellings, grades,
notes, and protected identifiers remain recoverable in the private database.

**Nicholas P Paledes** is confirmed by a direct May 1944 OSS board interview.
The interview records that he entered the Army in September 1941, operated his
own grocery store in civilian life, and was assigned to OSS in October 1943.
The site therefore distinguishes self-employment as his last civilian work
before military service from the United States Army as his immediate pre-OSS
affiliation. The separately indexed Nicholas P Peledes remains unmerged and
conflicting despite the two rows sharing a protected officer identifier.

**Mary J Painter** is linked at high confidence to Mary Jane Painter through a
wartime OSS interview index and a retrospective Reading Eagle account that
identifies her as an Albright College student before Army and OSS service.
Albright College is modeled as a student affiliation, not as employment and
not as an immediate pre-OSS affiliation or last civilian employer. Mary Jane
Painter and Mary Jane Painter Thompson are recorded as documented variants.

**Gus Palans** is linked at high confidence to T/5 Gus L. Palans of Greek
Operational Group II through the National Park Service and OSS Operational
Groups roster. **Gregory M Pahules**, **Joseph A Paiano**, and **Peter G
Paidas** are likewise supported by exact Army evidence plus Operational Groups
rosters. **Albert R Pahl**, **Joseph G Palguta**, and **George Pallay** have
high-confidence Army identity evidence. These matches establish wartime
identity, not a pre-OSS employer, and no Army occupation code is converted into
an occupation or employment claim.

**William G Paletti** remains conflicting because the protected identifier in
his indexed row is also attached to the separately indexed William G Plaetti.
Both source rows and person entities remain separate. **Francis K Paget**
remains ambiguous. The Francis King Paget associated with Standard Oil is a
plausible namesake lead, but the accessible evidence does not bridge that
person to this index row; the oil-company affiliation is not published as a
fact. Other common-name and partial-name results likewise remain rejected or
unresolved rather than being promoted for coverage.

The CIA and Library of Congress adapters failed closed in bounded attempts,
and the web adapter recorded deterministic query plans before manual staged
review. No authenticated NARA Catalog request was made because the local
project did not expose a key to this run.

The cohort ends with one `verified_employer_found`, one
`conflicting_sources`, one `needs_identity_review`, and 20
`requires_archival_review` outcomes. Identity statuses are one `confirmed`,
seven `high_confidence`, one `conflicting`, one `ambiguous`, and 13
`unresolved`. The reviewed bundle imports eight sources, three organizations,
three affiliations, 14 claims, 32 claim-source links, 23 person updates, and
23 consolidated research attempts. Six accepted and three conflicting
identity-review decisions are recorded.

Rebuilt coverage is **23,978/23,978** linked source rows and **23,939** active
person entities. Research-attempt coverage is **9,803/23,939 (40.9499%)**;
confirmed/high verified-employer coverage is **332/23,939 (1.3869%)**;
confirmed/high verified-affiliation coverage is **741/23,939 (3.0954%)**;
archival-review disposition coverage is **8,261/23,939 (34.5085%)**. There
are **14,131** `not_started` people, **523** possible-duplicate groups, and
**322** active conflicts. SQLite stores **17,888** attempts or plans and
**6,285** claims: 1,373 confirmed, 2,905 high, 1,524 medium, 198 low, 283
conflicting, and two unresolved. It contains **5,673** citation records and
**2,864** unique source documents. The public projection contains **2,475**
affiliations, **859** organizations, **4,454** sources, and **6,078** claims.
Full-index historical research remains unfinished.

## Replay and continuation

After importing prior durable batches into private SQLite:

```sh
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
python3 -m oss_research assign-page-batch --batch-name batch-729 --page 355 --first-row 1 --last-row 23
python3 -m oss_research research --source cia --batch batch-729 --max-queries 23
python3 -m oss_research research --source loc --batch batch-729 --max-queries 23
python3 -m oss_research research --source web --batch batch-729 --resume --max-queries 23 --dry-run
python3 -m oss_research import-review-decisions research/identity_review_decisions_2026-10-04_batch729.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page355-page-pallay-review_batch-729_2026-10-04.json
python3 -m oss_research export-adapter-checkpoints
python3 -m oss_research export-derived
python3 -m oss_research export-review-queue
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
```

Adapter checkpoints must be imported before final reviewed decisions and
evidence so temporary discovery states cannot supersede reviewed dispositions.
The next research boundary is PDF page 355, rows 24-46, from Leonard M Pallen
through Quentin S Palmer.

No API key, full service or officer number, raw Catalog or LoC API response,
copyrighted page image, street address, living-relative detail, modern
people-finder record, or private reviewer note is committed or included in the
public site. No authenticated NARA Catalog API request was made for this batch.
