# Batch 716: Ohara-Olafsen research

Batch 716 covers PDF page 348, rows 24-46, from **John H Ohara**
through **Aase Olafsen**. A 300-dpi visual inspection confirmed all 23
printed rows, representing 23 active person entities. The immutable extraction
is unchanged. Original spellings, ranks, box numbers, notes, and archival
locations remain recoverable. The rows span Boxes 570-571 at location
230/86/37/07.

Three people receive accepted identity matches from the official Army bulk
file: **Ole P Oines**, **Leif Oistad**, and **Tito U Okamoto**. Each match uses
the exact printed name plus a nonshared protected identifier. The identifier
remains private, and no coded Army occupation was converted into an occupation
or employer claim.

The strongest immediate-pre-OSS profiles are **Louis A Ojibway** and
**Leif Oistad**. A CIA Center for the Study of Intelligence article identifies
Ojibway as Louis Austin O'Jibway and cites his OSS requisition in Entry 224,
Box 570. It places him as athletic director at the Cavalry Replacement Training
Center at Fort Riley immediately before his 1944 OSS recruitment. His earlier
1st Cavalry Division physical-training assignment and University of New Mexico
petroleum-engineering studies remain separate affiliations. Summer roughneck
work is an occupation-only claim because the source names no oil or steel
employer.

Oistad is identified at high confidence through the exact protected Army
identifier and independently matching rank, unit, NORSO assignment, and
wartime chronology. His immediate pre-OSS affiliation is the 99th Infantry
Battalion (Separate) at Camp Hale, where he was a sergeant and ski instructor.
A reputable obituary says OSS recruited him from that assignment. It also
documents earlier deckhand work on commercial vessels, including the tanker
*Brasil*, but does not identify his employer. The project therefore does not
convert the ship owner's or operator's name into an employer claim and does not
add Oistad to the oil-company directory.

**Takashi Ohta** reaches high-confidence identity through the rare exact name
in the index and a visually inspected April 1945 OSS travel order. A separate
art-history source documents that he was hired as a set designer for the
Provincetown Players in 1928 and became set designer and scenic director at the
Maverick Theatre later that year. Both roles are published at medium
confidence as `documented_prewar`; neither is labeled immediate or last
civilian employment because the intervening chronology is unknown.

**Prince Olaf** remains unresolved. The name and index context do not justify
equating the row with Crown Prince Olav of Norway, and Box 571 requires
archival examination. The printed note `recomm` remains recoverable without
expansion or interpretation. Fred K Okamoto and Mary N Okamoto also require
their personnel files before any identity or relationship can be established.
Common-name and incomplete-name cases remain unresolved rather than being
attached to convenient biographies.

The CIA and Library of Congress adapters each made one bounded attempt for
Daniel G Okeeffe and failed closed. The web adapter recorded deterministic
planned queries without making live requests. Manual staged review completed
official, exact-name OSS, CIA-site, employment, occupation, obituary,
institutional, newspaper, directory, military, and archival search families
for every person.

The cohort ends with 19 `no_reliable_result_after_protocol`, two `completed`,
one `documented_prewar_employer_found`, and one `requires_archival_review`
outcome. Identity statuses are five `high_confidence` and 18 `unresolved`.
The reviewed bundle imports six sources, six organizations, six affiliations,
11 claims, 17 claim-source links, 23 person updates, and 23 consolidated
research attempts. Three accepted identity-review decisions are recorded.

Rebuilt coverage is **23,978/23,978** linked source rows and **23,939** active
person entities. Research-attempt coverage is **9,506/23,939 (39.7093%)**;
confirmed/high verified-employer coverage is **326/23,939 (1.3618%)**;
confirmed/high verified-affiliation coverage is **724/23,939 (3.0244%)**;
archival-review disposition coverage is **7,964/23,939 (33.2679%)**. There are
**14,428** `not_started` people, **523** possible-duplicate groups, and **296**
active conflicts. SQLite stores **17,262** attempts or plans and **6,117**
claims: 1,352 confirmed, 2,802 high, 1,506 medium, 198 low, 257 conflicting,
and two unresolved. It contains **5,590** citation records and **2,805** unique
source documents. The public projection contains **2,437** affiliations,
**842** organizations, **4,371** sources, and **5,910** claims. Full-index
historical research remains unfinished.

## Replay and continuation

After importing prior durable batches into private SQLite:

```sh
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
python3 -m oss_research assign-page-batch --batch-name batch-716 --page 348 --first-row 24 --last-row 46
python3 -m oss_research research --source cia --batch batch-716 --person-id dd626e1f-4269-5679-88e5-40722c9f1213 --max-queries 1
python3 -m oss_research research --source loc --batch batch-716 --person-id dd626e1f-4269-5679-88e5-40722c9f1213 --max-queries 1
python3 -m oss_research research --source web --batch batch-716 --resume --max-queries 23 --dry-run
python3 -m oss_research import-review-decisions research/identity_review_decisions_2026-10-04_batch716.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page348-ohara-olafsen-review_batch-716_2026-10-04.json
python3 -m oss_research export-adapter-checkpoints
python3 -m oss_research export-derived
python3 -m oss_research export-review-queue
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
```

Adapter checkpoints must be imported before final reviewed decisions and
evidence so temporary discovery states cannot supersede reviewed dispositions.
The next research boundary begins at PDF page 349, row 1.

No API key, full service number, raw Catalog or LoC API response, copyrighted
page image, unrelated Army coded occupation, street address, modern
people-finder record, or private reviewer note is committed or included in the
public site. No authenticated NARA Catalog API request was made for this batch.
