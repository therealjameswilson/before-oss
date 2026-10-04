# Batch 724: Ortiz-Ossman research

Batch 724 covers PDF page 352, rows 24-46, from **Gilbert Ortiz** through
**Harold Ossman**. A 300-dpi visual inspection confirmed all 23 printed rows,
representing 23 active person entities. Embedded text was checked against the
render. Original spelling and uncertainty remain recoverable, including
`Birginia Osborn`; the incomplete notes `Polish Ar`, `possibly`, `folder se`,
and `aka Atna`; and the two adjacent Orwin entries. Rows 24-42 and 44 are in
Box 577; rows 27, 43, 45, and 46 are in Box 578. All use location
230/86/38/01.

Four Army bulk candidates are accepted for identity only. **Robert G
Osborne**, **Stanley Oscar**, **Leonard Oshrain**, and **Francis J Osinskie**
have exact indexed-name and nonshared protected-identifier agreement. No Army
coded occupation was converted into an occupation or employer claim.

Two protected-identifier results remain conflicting. The Army bulk rows for
**Frederic C Osgood** and **Harold Ossman** point to the different names
Shinohara Jasaku and Koken Lee R. No metadata is transferred; both conflicts
remain visible pending review of Boxes 577 and 578.

Three profiles retain or receive substantive evidence:

* **Lithgow Osborne** is confirmed by the rare exact name, his signed 1942 New
  York State report, and the Congressional Record's explicit statement that he
  resigned his state job in 1942 to work for OSS. The site publishes the New
  York State Conservation Department as his confirmed, explicit immediate
  affiliation and last civilian government employer, with his role as
  Conservation Commissioner. The relationship is correctly classified as a
  government assignment rather than private employment.
* **Helen Osmun** is linked at high confidence to Helen Edith Osmun Parker. A
  contemporary Swarthmore yearbook prints the full name; a Washington Post
  obituary gives her 1941 graduation and directly documents wartime OSS work
  as an analyst and translator. Swarthmore is published as a documented
  prewar student affiliation, never as an employer or an immediate
  predecessor. Her immediate pre-OSS affiliation remains open.
* **Peter J Ortiz** retains the already reviewed high-confidence Marine Corps
  and French Foreign Legion evidence. This batch revalidates that profile and
  does not duplicate its affiliations or claims.

A discovery-only reference to a Captain Orwin in SSU Communications was
rejected because it lacks a first name and cannot distinguish Robert Orwin
from Robert J Orwin. A Takashi Osaki namesake, military-language surname
leads, and unbridged common-name results were likewise rejected. The CIA and
Library of Congress adapters failed closed in bounded attempts, and the web
adapter recorded deterministic query plans without making an authenticated
NARA Catalog request.

The cohort ends with 15 `requires_archival_review`, four
`no_reliable_result_after_protocol`, two `conflicting_sources`, and two
`verified_employer_found` outcomes. Identity statuses are 14 `unresolved`,
six `high_confidence`, two `conflicting`, and one `confirmed`. The reviewed
bundle imports six sources, two organizations, two affiliations, 11 claims,
24 claim-source links, 23 person updates, and 23 consolidated research
attempts. Four accepted and two conflicting identity-review decisions are
recorded.

Rebuilt coverage is **23,978/23,978** linked source rows and **23,939** active
person entities. Research-attempt coverage is **9,689/23,939 (40.4737%)**;
confirmed/high verified-employer coverage is **329/23,939 (1.3743%)**;
confirmed/high verified-affiliation coverage is **736/23,939 (3.0745%)**;
archival-review disposition coverage is **8,147/23,939 (34.0323%)**. There
are **14,245** `not_started` people, **523** possible-duplicate groups, and
**314** active conflicts. SQLite stores **17,648** attempts or plans and
**6,227** claims: 1,365 confirmed, 2,870 high, 1,519 medium, 198 low, 273
conflicting, and two unresolved. It contains **5,643** citation records and
**2,844** unique source documents. The public projection contains **2,464**
affiliations, **855** organizations, **4,424** sources, and **6,020** claims.
Full-index historical research remains unfinished.

## Replay and continuation

After importing prior durable batches into private SQLite:

```sh
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
python3 -m oss_research assign-page-batch --batch-name batch-724 --page 352 --first-row 24 --last-row 46
python3 -m oss_research research --source cia --batch batch-724 --max-queries 23
python3 -m oss_research research --source loc --batch batch-724 --max-queries 23
python3 -m oss_research research --source web --batch batch-724 --resume --max-queries 23 --dry-run
python3 -m oss_research import-review-decisions research/identity_review_decisions_2026-10-04_batch724.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page352-ortiz-ossman-review_batch-724_2026-10-04.json
python3 -m oss_research export-adapter-checkpoints
python3 -m oss_research export-derived
python3 -m oss_research export-review-queue
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
```

Adapter checkpoints must be imported before final reviewed decisions and
evidence so temporary discovery states cannot supersede reviewed dispositions.
The next research boundary begins at PDF page 352, row 47.

No API key, full service or officer number, raw Catalog or LoC API response,
copyrighted page image, street address, living-relative detail, modern
people-finder record, or private reviewer note is committed or included in the
public site. No authenticated NARA Catalog API request was made for this batch.
