# Batch 708: Norberg-Norris research

Batch 708 covers PDF page 344, rows 23-46, from **Willard P Norberg**
through **Karl H Norris**. Fresh 300-dpi visual inspection confirmed all 24
printed rows, representing 24 active person entities. The immutable extraction
is unchanged. Jackson E Nordin's row was already terminal in the pilot queue;
this batch rechecked and retained that archival-review disposition.

Eleven people are high-confidence identity matches. Official Army evidence
supports **Willard P Norberg**, **John B Nordmann**, **Frederick C Nordsiek**,
**Kenneth R Nordwall**, **Maurice O Normandin**, and **Ira E Norrell**. An OSS
Operational Groups roster supports **Albert Nordang** on the NORSO II roster.
A 1944 OSS Cairo report identifies **Harold E Nordblom** at the OSS Cyprus
base, but that wartime assignment is not treated as pre-OSS employer evidence.
Institutional or official records also support **Christopher Sverre Norborg**,
**Johan Nordentoft**, and **Jens Henrik Throne Nordlie**.

Three dated affiliations meet publication standards. The University of
Minnesota's 1940-1941 address book identifies Christopher Norborg as Assistant
Professor of Philosophy. This is published as a documented prewar and last
civilian employer, not as an immediate predecessor to OSS. Danish military
records document Johan Nordentoft as chief of staff of the Danish Army's
Zealand Division from 1942 until 29 August 1943. That record is published only
as a military assignment with uncertain temporal relation to OSS; Nordentoft's
workflow status is `completed`, not an employer-found status. A Norwegian
institutional biography documents Jens Nordlie as office manager at Narvesens
Kioskkompani from 1941 into early 1943. It is published as a strongly
date-bounded last civilian employer, without claiming that it immediately
preceded OSS service.

Two name discrepancies and two duplicate pairs remain visible. **Guy E
Norbert** is not merged with an Army record for Norbert C Guy, and **Carl W
Nordsiek** is not silently corrected to Carl W Nordsieck. **Brunnon C Normand**
and another record with a similar protected identifier remain separate pending
review. The adjacent **Karl H Noris** and **Karl H Norris** rows share a
protected identifier and are linked only as a possible duplicate group; both
source rows and person pages remain intact. Public pages expose only masked
serial suffixes.

The CIA and Library of Congress adapters failed closed without usable results.
Exact-name OSS, employment, occupation, institutional, newspaper, obituary,
military, and archival searches were nevertheless reviewed for every person.
The cohort ends with 15 `no_reliable_result_after_protocol`, five
`conflicting_sources`, one `completed`, one `requires_archival_review`, one
`documented_prewar_employer_found`, and one `verified_employer_found` outcome.
Identity statuses are 11 `high_confidence`, three `probable`, two
`conflicting`, and eight `unresolved`. The reviewed bundle imports nine
sources, three organizations, three affiliations, 19 claims, 39 claim-source
links, 24 person updates, and 24 consolidated research attempts. Claim
decisions comprise 14 high-confidence, three medium-confidence, and two
conflicting claims. Eleven review decisions are recorded and imported.

Rebuilt coverage is **23,978/23,978** linked source rows and **23,939** active
person entities. Research-attempt coverage is **9,323/23,939 (38.9448%)**;
confirmed/high verified-employer coverage is **322/23,939 (1.3451%)**;
confirmed/high verified-affiliation coverage is **713/23,939 (2.9784%)**;
archival-review disposition coverage is **7,781/23,939 (32.5034%)**. There are
**14,611** `not_started` people, **523** possible-duplicate groups, and **283**
active conflicts. SQLite stores **16,872** attempts or plans and **6,024**
claims: 1,352 confirmed, 2,731 high, 1,489 medium, 196 low, 254 conflicting,
and two unresolved. It contains **5,541** citation records and **2,764** unique
source documents. The public projection contains **2,415** affiliations,
**827** organizations, **4,324** sources, and **5,819** claims. Full-index
historical research remains unfinished.

## Replay and continuation

After importing prior durable batches into private SQLite:

```sh
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
python3 -m oss_research assign-page-batch --batch-name batch-708a --page 344 --first-row 23 --last-row 31
python3 -m oss_research assign-page-batch --batch-name batch-708b --page 344 --first-row 33 --last-row 46
python3 -m oss_research research --source cia --batch batch-708a --max-queries 9
python3 -m oss_research research --source cia --batch batch-708b --max-queries 14
python3 -m oss_research research --source loc --batch batch-708a --max-queries 9
python3 -m oss_research research --source loc --batch batch-708b --max-queries 14
python3 -m oss_research research --source web --batch batch-708a --resume --max-queries 9
python3 -m oss_research research --source web --batch batch-708b --resume --max-queries 14
python3 -m oss_research import-review-decisions research/identity_review_decisions_2026-10-03_batch708.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page344-norberg-norris-review_batch-708_2026-10-03.json
python3 -m oss_research export-adapter-checkpoints
python3 -m oss_research export-derived
python3 -m oss_research export-review-queue
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
```

Adapter checkpoints must be imported before final reviewed decisions and
evidence so temporary discovery states cannot supersede reviewed dispositions.
The next research boundary begins at PDF page 345, row 1 (**Laura M Norris**).

No API key, full service number, raw Catalog or LoC API response, copyrighted
page image, unrelated Army coded occupation, street address, or private
reviewer note is committed or included in the public site. No authenticated
NARA Catalog API request was made for this batch.
