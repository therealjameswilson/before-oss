# Batch 582 — terminal online review, PDF page 117 rows 21–30

Reviewed 2026-09-20 UTC. The ten printed rows in [NARA's OSS personnel
index](https://www.archives.gov/files/iwg/declassified-records/rg-226-oss/personnel-database.pdf)
were checked against a rendering of page 117. Ann J Dick, Doris R Dick, and
David H Dickason are in Box 185; the next seven people, through Harold E
Dickerson, are in Box 186. Each remains a distinct source row and cautious
person entity. The index visibly spells **Gelnn O Dickerson**; the official
Army record spells **Glenn O Dickerson**. Neither reading was silently
substituted for the other. No physical personnel file was inspected.

All ten people have saved bounded CIA Reading Room and Library of Congress
checks, exact-name OSS and employment/occupation searches, contextual
institutional or newspaper checks, and an importable manual review outcome.
The four LoC discovery hits for Ann J Dick and Harold E Dickerson were
examined through the [official LoC text-service
API](https://www.loc.gov/apis/micro-services/text-services/), after the
ordinary resource pages returned an access challenge. Two hits joined
separate first and surnames in OCR; the other two did not match Harold's
middle initial/name and offered no pre-OSS employer. All four were explicitly
rejected in `loc_review_decisions_2026-09-20_batch582.csv`. The OCR contexts
were used to reject leads, not as affirmative identity or employment proof.

Three [official Army bulk-file](https://catalog.archives.gov/id/1263923)
crosswalks—Roger H Dickens, the indexed Gelnn/Army Glenn O Dickerson, and
Harold E Dickerson—support high-confidence wartime identity from a matching
name or documented spelling variant and a nonshared protected identifier.
Full identifiers remain private. These are identity-only claims: Army
occupation coding is not a named employer, and Harold's May 1945 Army entry
does not establish the order of Army and OSS service. The other seven people
remain unresolved beyond the index. A David Howard Dickason literary-scholar
lead and a Frederick Garrett Dickason missionary/Judson College lead lacked
an OSS file or independent identity bridge and were not promoted to claims.
Other namesake, obituary, genealogy, and modern-directory leads were likewise
withheld.

All ten received terminal online `requires_archival_review` dispositions.
**No reliable pre-OSS employer has yet been identified in the accessible
sources reviewed** for this cohort; this is not evidence that any person had
no prior employer. Boxes 185–186 are the next research step. The NARA Catalog
API was not used in this batch; the Army data is from a separate official
bulk file. See the importable `evidence-page-117-dick-through-dickerson_batch-582_2026-09-20.json`,
the Army and LoC review-decision CSVs, and the durable private SQLite attempt
history.

After import, the local database has 23,978/23,978 linked source rows and
23,940 active person entities. Nonplanned research-attempt coverage is
5,584/23,940 (23.3250%); confirmed/high published employer coverage is
262/23,940 (1.0944%); broader verified-affiliation coverage is 600/23,940
(2.5063%); and archival-review assessment is 5,539/23,940 (23.1370%).
There are still 18,356 `not_started` people. This batch advances the
auditable research queue but does not complete the full-index goal.

Resume or reproduce the cohort on the existing private database with:

```bash
python3 -m oss_research assign-page-batch --batch-name batch-582 --page 117 --first-row 21 --last-row 30
python3 -m oss_research import-review-decisions research/army_review_decisions_2026-09-20_batch582.csv
python3 -m oss_research import-review-decisions research/loc_review_decisions_2026-09-20_batch582.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page-117-dick-through-dickerson_batch-582_2026-09-20.json
python3 -m oss_research export-derived
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
```

The assignment and reviewed-evidence import are idempotent. Candidate review
decisions require their private candidate rows to exist first. The next
bounded page cohort starts at page 117, row 31.
