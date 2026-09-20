# Batch 583 — terminal online review, PDF page 117 rows 31–46

Reviewed 2026-09-20 UTC. All sixteen printed rows are in [NARA's OSS
personnel index](https://www.archives.gov/files/iwg/declassified-records/rg-226-oss/personnel-database.pdf),
Box 186, archive location 230/86/30/01. Original rendered pages 117 and 118
were visually inspected. Each row remains an immutable source record linked
to a separate cautious person entity. No Box 186 physical file was inspected.

All sixteen have saved bounded CIA Reading Room and Library of Congress
checks; exact-name OSS and employment/occupation queries; contextual
institutional, newspaper, obituary or archival searches; and importable
manual outcomes. The eleven LoC discovery hits were inspected with the
[official LoC text-service API](https://www.loc.gov/apis/micro-services/text-services/)
using the bounded, read-only `scripts/inspect_loc_candidates.py` helper.
Ten were rejected for mismatched middle initials, separated OCR names, or
irrelevant postwar context. A 1948 item naming Edward T Dickinson Jr remains
a **private plausible lead** only: the indexed row lacks the suffix and
another bridge. None is a published employer source.

Four [official Army bulk-file](https://catalog.archives.gov/id/1263923)
crosswalks support high-confidence wartime identity for Philip C Dickinson,
Doyle E Dickson, Martin Dickson and Angelo DiDomenico. The last two printed
surname conflicts remain explicit: the Army entry says **Diclson** for Doyle
and spaces **Di Domenico** for Angelo. A nonshared protected identifier and
matching given names support each crosswalk; full identifiers remain private.
No Army occupation code was treated as a named employer.

Martin Dickson's [1991 scholarly memorial](https://doi.org/10.1017/S0026318400024937)
by Cornell Fleischer says he entered the U.S. Army after high school and
later the OSS. [Encyclopaedia Iranica](https://www.iranicaonline.org/articles/dickson/)
places his OSS language training in 1943, while the independently matched
official Army entry is from February 1943. The U.S. Army is therefore shown
as a **medium-confidence, probable immediate institutional predecessor**,
qualified because the exact transfer date and Army unit remain unverified.
It is not a civilian employer. Michigan language study was part of OSS
training; Princeton employment was postwar. His last civilian employer
before service remains unidentified.

A [U.S.-courts-hosted biographical exhibit](https://www.rid.uscourts.gov/sites/rid/files/historical/documents/20150908-LawyersWithoutRightsExhibit-Book2.pdf)
describes Wilhelm Dickmann, later William Dickman, as a lawyer and OSS member.
It does **not** yet provide the indexed William **J** Dickman's Box 186/file
linkage, so his former Berlin law office, self-employment, U.S. odd jobs and
law student status are not attributed to the index row. For indexed William
**Diebod** Jr., Council on Foreign Relations economist William **Diebold**
Jr. and a different wartime Army aviator named William Diebold are competing
namesakes; neither is tied to the printed protected identifier. No CFR or
lumber-company employment is assigned.

All sixteen have terminal online `requires_archival_review` dispositions.
Except for Martin's qualified military pathway, no reliable pre-OSS employer
has yet been identified in the accessible sources reviewed. This does not
mean any person lacked a previous employer. Box 186 is the next research
step for identity, employer, and Army-to-OSS chronology questions. The NARA
Catalog API was not used in this batch; the Army data is a separate official
bulk file. See the importable evidence bundle, the Army and LoC review CSVs,
and the private SQLite attempt history.

After import, the local database contains 23,978/23,978 linked source rows
and 23,940 active person entities. Nonplanned research-attempt coverage is
5,600/23,940 (23.3918%); confirmed/high employer coverage is 262/23,940
(1.0944%); confirmed/high affiliation coverage is 600/23,940 (2.5063%);
archival-review assessment is 5,555/23,940 (23.2038%). There remain 18,340
`not_started` people. This batch advances the auditable queue but does not
complete the full-index goal.

Resume or reproduce this cohort against the existing private database with:

```bash
python3 -m oss_research assign-page-batch --batch-name batch-583 --page 117 --first-row 31 --last-row 46
python3 -m oss_research research --source cia --batch batch-583 --max-queries 16 --resume
python3 -m oss_research research --source loc --batch batch-583 --max-queries 16 --resume
python3 -m oss_research import-review-decisions research/army_review_decisions_2026-09-20_batch583.csv
python3 -m oss_research import-review-decisions research/loc_review_decisions_2026-09-20_batch583.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page-117-dickerson-jr-through-diebod_batch-583_2026-09-20.json
python3 -m oss_research export-derived
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
```

The assignment, source fingerprints, review decisions and evidence import are
idempotent. LoC candidate decisions require the underlying private discovery
rows first. The next bounded cohort begins on PDF page 118.
