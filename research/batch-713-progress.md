# Batch 713: Obuckley-Odeneal research

Batch 713 covers PDF page 347, rows 1-23, from **Joseph P Obuckley**
through **John F Odeneal**. A fresh 300-dpi visual inspection confirmed all
23 printed rows, representing 23 active person entities. The immutable
extraction is unchanged. Original index spellings, including **Oconnell**,
**Oconnor**, **Oconor**, **Odea**, and **Odeneal**, remain recoverable. The
page's `also AS` note for Edward V Oconnor is preserved without expansion.
The rows span Boxes 567-568 and locations 230/86/37/06-07.

Five nonshared official Army identifiers support high-confidence identities
for **Joseph S Ochranek**, **Daniel J Oconnell**, **John A Oconnor**, **Joseph
J Oddo**, and **William K Odell**. The Army file records Ochranek with the
suffix `Jr.`, which is retained as a documented variant. Odell's Army entry
date is in 1946; it is used for identity only and is not presented as a
pre-OSS pathway. Army occupation codes were not converted into employer or
occupation claims.

One protected identifier creates a material conflict rather than a match:
the index prints **Joseph F Ochnat**, while the Army file gives **OCHWAT
JOSEPH F**. The candidate is formally rejected, the person remains visibly
`conflicting`, and Box 567 is required before any merge.

The distinctive **Miyoji Oda** identity reaches high confidence through the
exact index name, a wartime War Relocation Authority roster, and a Los
Angeles Times obituary. The latter two independently name siblings Frank,
Kazume, and Lillian. This evidence documents identity and wartime context; it
does not identify an employer or establish the immediate transition into OSS
service. **Gabriel Odalovich** is published only as a probable identity: the
unusual exact name and Army lieutenant status agree with a Veterans
Affairs-derived cemetery transcription, but there is no protected identifier
or direct OSS bridge in the accessible source.

A 1941 Gloucester directory entry for a rare-name **John F Odeneal** student
and a later library authority record with birth year 1920 remain unpublished
leads because neither directly links that person to the OSS index row. An
Evelyn F Oconnor obituary lead and a Raymond R Oconnor veterans-memorial lead
were rejected as unbridged namesakes. Common-name results and other
postwar-only material were excluded.

The CIA and Library of Congress adapters each made one bounded attempt and
failed closed; the web adapter recorded 23 deterministic planned queries
without making live requests. Manual staged review completed the required
official, OSS, employment, occupation, obituary, institutional, newspaper,
directory, military, and archival checks for every person. The current
official Army bulk object was downloaded to a temporary directory, verified,
and scanned transiently across 9,200,232 records. Neither the raw bulk file
nor raw record content is retained in the repository.

The cohort ends with 21 `no_reliable_result_after_protocol`, one
`requires_archival_review`, and one `conflicting_sources` outcome. Identity
statuses are six `high_confidence`, one `probable`, one `conflicting`, and 15
`unresolved`. The reviewed bundle imports five sources, no organization or
affiliation, seven identity claims (six high and one medium), 15 claim-source
links, 23 person updates, and 23 consolidated research attempts. Six manual
identity-review decisions are recorded: five accepted Army matches and one
rejected conflict.

Rebuilt coverage is **23,978/23,978** linked source rows and **23,939** active
person entities. Research-attempt coverage is **9,437/23,939 (39.4210%)**;
confirmed/high verified-employer coverage is **325/23,939 (1.3576%)**;
confirmed/high verified-affiliation coverage is **720/23,939 (3.0076%)**;
archival-review disposition coverage is **7,895/23,939 (32.9797%)**. There are
**14,497** `not_started` people, **523** possible-duplicate groups, and **294**
active conflicts. SQLite stores **17,117** attempts or plans and **6,085**
claims: 1,352 confirmed, 2,779 high, 1,498 medium, 198 low, 256 conflicting,
and two unresolved. It contains **5,572** citation records and **2,790** unique
source documents. The public projection contains **2,425** affiliations,
**832** organizations, **4,353** sources, and **5,878** claims. Full-index
historical research remains unfinished.

## Replay and continuation

After importing prior durable batches into private SQLite:

```sh
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
python3 -m oss_research assign-page-batch --batch-name batch-713 --page 347 --first-row 1 --last-row 23
python3 -m oss_research research --source cia --batch batch-713 --max-queries 23
python3 -m oss_research research --source loc --batch batch-713 --max-queries 23
python3 -m oss_research research --source web --batch batch-713 --resume --max-queries 23
python3 -m oss_research import-review-decisions research/identity_review_decisions_2026-10-03_batch713.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page347-obuckley-odeneal-review_batch-713_2026-10-03.json
python3 -m oss_research export-adapter-checkpoints
python3 -m oss_research export-derived
python3 -m oss_research export-review-queue
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
```

Adapter checkpoints must be imported before final reviewed decisions and
evidence so temporary discovery states cannot supersede reviewed dispositions.
The next research boundary begins at PDF page 347, row 24 (**Mary J Odgers**).

No API key, full service number, raw Catalog or LoC API response, copyrighted
page image, unrelated Army coded occupation, address, phone number, modern
people-finder record, or private reviewer note is committed or included in the
public site. No authenticated NARA Catalog API request was made for this
batch.
