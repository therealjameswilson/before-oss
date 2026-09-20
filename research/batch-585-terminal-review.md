# Batch 585 — terminal online review, PDF page 118 rows 11–30

Reviewed 2026-09-20 UTC. All twenty printed rows were checked against a
rendered image of [NARA's OSS personnel index](https://www.archives.gov/files/iwg/declassified-records/rg-226-oss/personnel-database.pdf),
PDF page 118. Romeo P Digiulian (row 11) is in Box 186; rows 12–30 are in
Box 187. The source's clipped `British A` note for E P Dillon remains
literal. The row/box sequence is not assumed to be monotonic. Each printed
row stays separate, notably William J and William F Dillon.

All twenty have saved bounded CIA Reading Room and Library of Congress
searches, exact-name OSS and employment/occupation variants, contextual
institutional or archival checks, and a manual terminal review. Eight
[official Army bulk-file](https://catalog.archives.gov/id/1263923)
crosswalks support high-confidence **identity only**: Romeo P Digiulian,
Armand Digliani, Grant Dignall, Alfred Dilello, Donald D Diller, William F
Dillon, John B Dillon Jr, and Alfred H Diloreto. Protected identifiers were
compared privately and never exported. The official Army spellings `Di
Giuliam`, `John B F Dillon Jr`, and `Di Loreto` remain documented variants,
not silent corrections or new employment claims.

[University of Illinois trustee minutes from April 1937](https://www.trustees.uillinois.edu/trustees/minutes/1937/1937-04-14-uibot.pdf),
printed p. 246, list Konrad C Dillow under *Graduate Scholarships and
Fellowships*, Education. The
[February 1938 minutes](https://www.trustees.uillinois.edu/trustees/minutes/1938/1938-02-11-uibot.pdf),
printed p. 635, record resignation as a fellow effective February 1, 1938.
His [Washington Post obituary](https://www.washingtonpost.com/archive/local/1998/05/18/obituaries/c152246f-16fb-443b-ba74-f03e91dc821b/)
independently associates the distinctive full name with Illinois graduate
study and wartime Army service in France. This supports a high-confidence
**student/fellowship affiliation**, not a University of Illinois employer.
The [university's WPA research-project finding aid](https://archon.library.illinois.edu/archives/?id=3207&p=collections%2Fcontrolcard)
mentions Dillow correspondence in 1939–42, but does not name his job or
employer. Box 187 and that correspondence are the next chronology checks.

Eleven LoC candidates were reviewed in official OCR context where available:
eight rejected, three private plausible/unresolved. The
[1944 *Waterbury Democrat* article](https://www.loc.gov/resource/sn82014085/1944-09-19/ed-1/?sp=2)
about **John T** Dillon Jr names First National Warehouse as his
pre-service employer; it cannot be transferred to the indexed **John B**
Dillon Jr, whose Army crosswalk agrees on B and a protected identifier. A
1946 **William J** Dillon captain reference is not evidence for indexed
William F; whether it belongs to the adjacent indexed William J remains
unresolved. Several E P Dillon hits use *Dillon* as a Montana place or name
other initials. An oil advertisement on the same
[1940 *Harlem News* page](https://www.loc.gov/resource/sn86075250/1940-01-05/ed-1/?sp=5)
is not
evidence of E P Dillon working for an oil company. One Laredo text-service
response exceeded the bounded review path, and a George Dill hit had empty
OCR context; both remain private leads for visual or archival review.

An [*Express Times* obituary lead](https://obits.lehighvalleylive.com/us/obituaries/etpa/name/alfred-dilello-obituary?id=15407091)
for Alfred Dilello mentions OSS service and
postwar work, but its host blocked direct reinspection and it does not name
a pre-OSS employer. A
[1958 radio directory](https://vtda.org/docs/radio/IndianapolisRadioClub/IRC_MarionCountryDirectoryRadioAmateurs_Apr58.pdf)
names Carter-Lee Lumber Co for a
Clair F Dillman, but the date is postwar and no Box 187 identity bridge is
present. Neither was promoted into the pre-OSS employer dataset. The NARA
Catalog API was not used; the Army crosswalk is a separate official bulk file.

All twenty have terminal online `requires_archival_review` dispositions.
No new reliable **employer** was established in this cohort. That does not
mean any person had no earlier employer. Index coverage remains
23,978/23,978 linked rows; local research-attempt coverage is
5,630/23,940 (23.5171%); confirmed/high employer coverage is 263/23,940
(1.0986%); confirmed/high affiliation coverage is 602/23,940 (2.5146%);
archival-review assessment is 5,585/23,940 (23.3292%). There remain 18,310
`not_started` people, so the full-index goal is not complete.

Resume or reproduce this cohort against the existing private database:

```bash
python3 -m oss_research assign-page-batch --batch-name batch-585 --page 118 --first-row 11 --last-row 30
python3 -m oss_research research --source cia --batch batch-585 --max-queries 20 --resume
python3 -m oss_research research --source loc --batch batch-585 --max-queries 20 --resume
python3 -m oss_research import-review-decisions research/army_review_decisions_2026-09-20_batch585.csv
python3 -m oss_research import-review-decisions research/loc_review_decisions_2026-09-20_batch585.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page-118-digiulian-through-dilworth_batch-585_2026-09-20.json
python3 -m oss_research export-adapter-checkpoints
python3 -m oss_research export-derived
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
```

Assignments, source fingerprints, decisions and evidence import are
idempotent. LoC candidate decisions require the private discovery rows to
be replayed first. The next bounded cohort begins at PDF page 118, row 31.
