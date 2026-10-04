# Batch 714: Odgers-Offut research

Batch 714 covers PDF page 347, rows 24-46, from **Mary J Odgers**
through **Wilma B Offut**. A 300-dpi visual inspection confirmed all 23
printed rows, representing 23 active person entities. The immutable extraction
is unchanged. Original index spellings, including **Odonnell**, **Odonnoghue**,
**Odunne**, **Oen**, **Oesh**, **Oexner**, **Ofax**, and **Offut**, remain
recoverable. The rows span Boxes 568-569 at location 230/86/37/07.

One nonshared official Army identifier supports a high-confidence identity for
**William H Odonnell**. A second identifier creates a material conflict rather
than a match: the index prints **John L Ofax**, while the Army file gives
**OFAK JOHN L**. That candidate is formally rejected, both spellings remain
visible, and Box 569 is required before any merge. Officer numbers and the
letter-prefixed value in this cohort were not padded or forced into the Army
enlisted-file format. Army coded occupations were not converted into employer
or occupation claims.

The distinctive **Bjarne Oen** identity reaches high confidence through the
documented **Bjarne Øen** spelling, compatible Norwegian air-service
leadership, and Norwegian institutional sources. Store norske leksikon places
Øen at the head of the Norwegian Armed Forces High Command's Fourth Office
(FO IV) from 1942. The project publishes FO IV as his best-supported immediate
pre-OSS military assignment with a strongly date-bounded temporal basis. FO
IV remains a Norwegian military organization and is not mislabeled as a
civilian employer or silently merged into OSS.

**Charles Z Offin** is published only as a probable identity. A City College
institutional biography documents the rare exact name and a role as editor and
publisher of *Pictures on Exhibit* beginning in 1937. That is presented as a
medium-confidence documented prewar professional affiliation, not as a proven
immediate predecessor or last civilian employer. **Edward W Oexner** is also
published only as a probable identity: the unusual exact name and
master-sergeant status align with a Veterans Affairs-derived cemetery
transcription, but the source provides no protected identifier, employer, or
OSS transition chronology.

A postwar CIA memorandum signed Justin E. O'Donnell remains an unpublished
lead because it does not bridge its signer to the indexed first lieutenant.
Results for Fred or Frederick Oechsner, including the well-known OSS
journalist, were rejected because the index prints Francis and no direct
source establishes equivalence. Modern people-search, address, postwar-only,
and other namesake results were excluded.

The CIA adapter made one bounded attempt and failed closed; the Library of
Congress adapter searched one query across two people and failed closed. The
web adapter recorded 23 deterministic planned queries without making live
requests. Manual staged review completed official, exact-name OSS,
employment, occupation, obituary, institutional, newspaper, directory,
military, and archival search families for every person. The official Army
bulk object was verified and scanned transiently across 9,200,232 records.
Neither the raw bulk file nor raw record content is retained in the repository.

The cohort ends with 19 `no_reliable_result_after_protocol`, one `completed`,
one `occupation_only_found`, one `requires_archival_review`, and one
`conflicting_sources` outcome. Identity statuses are two `high_confidence`,
two `probable`, one `conflicting`, and 18 `unresolved`. The reviewed bundle
imports six sources, two organizations, two affiliations, six claims (three
high and three medium), 13 claim-source links, 23 person updates, and 23
consolidated research attempts. Two manual identity-review decisions are
recorded: one accepted Army match and one rejected conflict.

Rebuilt coverage is **23,978/23,978** linked source rows and **23,939** active
person entities. Research-attempt coverage is **9,460/23,939 (39.5171%)**;
confirmed/high verified-employer coverage is **325/23,939 (1.3576%)**;
confirmed/high verified-affiliation coverage is **721/23,939 (3.0118%)**;
archival-review disposition coverage is **7,918/23,939 (33.0757%)**. There are
**14,474** `not_started` people, **523** possible-duplicate groups, and **295**
active conflicts. SQLite stores **17,166** attempts or plans and **6,091**
claims: 1,352 confirmed, 2,782 high, 1,501 medium, 198 low, 256 conflicting,
and two unresolved. It contains **5,578** citation records and **2,795** unique
source documents. The public projection contains **2,427** affiliations,
**834** organizations, **4,359** sources, and **5,884** claims. Full-index
historical research remains unfinished.

## Replay and continuation

After importing prior durable batches into private SQLite:

```sh
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
python3 -m oss_research assign-page-batch --batch-name batch-714 --page 347 --first-row 24 --last-row 46
python3 -m oss_research research --source cia --batch batch-714 --max-queries 23
python3 -m oss_research research --source loc --batch batch-714 --max-queries 23
python3 -m oss_research research --source web --batch batch-714 --resume --max-queries 23
python3 -m oss_research import-review-decisions research/identity_review_decisions_2026-10-03_batch714.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page347-odgers-offut-review_batch-714_2026-10-03.json
python3 -m oss_research export-adapter-checkpoints
python3 -m oss_research export-derived
python3 -m oss_research export-review-queue
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
```

Adapter checkpoints must be imported before final reviewed decisions and
evidence so temporary discovery states cannot supersede reviewed dispositions.
The next research boundary begins at PDF page 348, row 1 (**Julian A
Oflaherty**).

No API key, full service number, raw Catalog or LoC API response, copyrighted
page image, unrelated Army coded occupation, address, phone number, modern
people-finder record, or private reviewer note is committed or included in the
public site. No authenticated NARA Catalog API request was made for this
batch.
