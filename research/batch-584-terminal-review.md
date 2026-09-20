# Batch 584 — terminal online review, PDF page 118 rows 1–10

Reviewed 2026-09-20 UTC. Ten printed rows were checked against a rendered
image of [NARA's OSS personnel index](https://www.archives.gov/files/iwg/declassified-records/rg-226-oss/personnel-database.pdf),
page 118. Rows 1–9 are in Box 186; row 10, Gregory A Digiovanni, is in
Box 187. The source's clipped `Norwegi` note for Arne Diesen remains literal;
it has not been expanded into a nationality claim. Each printed row remains
separate, including Augustine M and Gregory A Digiovanni.

All ten have saved bounded CIA Reading Room and Library of Congress searches,
exact-name OSS variants, employment/occupation searches, contextual
institutional or archival checks, and a manual terminal review. The three
LoC OCR hits were inspected in official text-service context. An Oakwood
Press hit names Ruth Dieckman and an 1894 Jersey City notice is a
chronological mismatch; both were rejected. A 1942 *Detroit Evening Times*
story names an Ed Dieckman associated with the San Diego police, but gives
no middle initial, OSS identity bridge, or clear event date. It remains a
**private plausible lead**, not an employer claim.

[University of Florida's archival finding aid](https://findingaids.uflib.ufl.edu/repositories/2/resources/1226),
Ms Coll. 036, explicitly says Sigismond deRudesheim Diettrich joined its
faculty in 1931 and served as an OSS special consultant during World War II.
The contemporary [March 1933 *Deltasig*](https://www.deltasigmapi.org/docs/default-source/DELTASIG-Magazine/1930s/1933-deltasig-vol-25-no-3-march.pdf?sfvrsn=1596699b_2),
printed p. 114, independently calls him a University of Florida economic
geography instructor. This supports a high-confidence **documented prewar
employer**, University of Florida, and a high-confidence identity match.
It does not show the exact OSS start date, whether he took wartime faculty
leave, or when the finding aid's Department of State assignment occurred.
Thus the affiliation is *not* marked immediate or last civilian before
service. Box 186 and university leave records are the next chronology checks.

Two [official Army bulk-file](https://catalog.archives.gov/id/1263923)
crosswalks support high-confidence wartime identity for Reardon Dight and
Augustine M Digiovanni. The Army adds Reardon's middle initial E; it spaces
Augustine's surname as **Di Giovanni** and omits his M. Nonshared protected
identifiers support both matches and remain private. The
[Department of Veterans Affairs memorial](https://www.vlm.cem.va.gov/AUGUSTINEMDIGIOVANNI/98fd12)
independently records Augustine's full indexed name and Army service.
A [509th Parachute Infantry Regiment roster](https://www.509thgeronimo.org/combatjumps/jump2.html)
names an Augustine M Digiovanni, but its compiler explicitly calls the
second-jump list a *best guess*. It is a private unit lead, not proof of
an OSS transition or an immediate pre-OSS assignment. Army occupation codes
were not turned into named employers.

All ten have terminal online `requires_archival_review` dispositions.
Except for Diettrich's documented earlier university employment, no reliable
pre-OSS employer has yet been identified in the accessible sources reviewed.
That does not mean these people had no previous employer. Boxes 186–187 are
the next step. The NARA Catalog API was not used; the Army data is a separate
official bulk file.

After import, local SQLite contains 23,978/23,978 linked source rows and
23,940 active people. Nonplanned research-attempt coverage is 5,610/23,940
(23.4336%); confirmed/high employer coverage is 263/23,940 (1.0986%);
confirmed/high affiliation coverage is 601/23,940 (2.5104%); archival-review
assessment is 5,565/23,940 (23.2456%). There remain 18,330 `not_started`
people. This batch advances the research queue; it does not complete the
full-index goal.

Resume or reproduce this cohort against the existing private database:

```bash
python3 -m oss_research assign-page-batch --batch-name batch-584 --page 118 --first-row 1 --last-row 10
python3 -m oss_research research --source cia --batch batch-584 --max-queries 10 --resume
python3 -m oss_research research --source loc --batch batch-584 --max-queries 10 --resume
python3 -m oss_research import-review-decisions research/army_review_decisions_2026-09-20_batch584.csv
python3 -m oss_research import-review-decisions research/loc_review_decisions_2026-09-20_batch584.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page-118-dieckman-through-digiovanni_batch-584_2026-09-20.json
python3 -m oss_research export-adapter-checkpoints
python3 -m oss_research export-derived
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
```

Assignments, source fingerprints, decisions and evidence import are
idempotent. LoC candidate decisions require the private discovery rows to be
replayed first. The next bounded cohort begins at PDF page 118, row 11.
