# Batch 700: Nesbitt-Neumann research

Batch 700 covers PDF page 340, rows 23-45, from **Frank B Nesbitt** through
**Sigmund Neumann**. Fresh visual inspection of the rendered page confirmed
all 23 printed rows. The immutable extraction remains unchanged.

**Gerhardt Neumann** is the batch's strongest resolved case. The exact
protected identifier printed in the index, the indexed Master Sergeant rank,
official Army evidence, the Smithsonian catalog, a congressional report, and
institutional aerospace sources establish that the indexed spelling refers to
Gerhard Neumann. The published record distinguishes three relationships: his
immediate pre-OSS U.S. Army Air Corps assignment as a Master Sergeant and
aircraft engineering specialist (`strongly_date_bounded`, high confidence),
his earlier American Volunteer Group service as a mechanic (high confidence),
and documented prewar aircraft-maintenance work with the Chinese Nationalist
Air Force (medium confidence, relationship unknown). The last item is not
presented as an employer.

Official Army bulk evidence supports high-confidence identity-only decisions
for **Frank B Nesbitt**, **Rudolph W Ness**, **Thomas E Nettles**, **Arthur J
Neu Jr.**, and **Stanley P Neugebauer**. Exact indexed names and nonshared
protected identifiers agree. No coded Army occupation is converted into an
employer.

Two protected-identifier conflicts remain visible. The number printed for
**Harold E Ness** reaches both NESS HAROLD E and VINEYARD DELMAR I in official
Army evidence. The number printed for **John E Nesline Jr.** reaches NESLINE
JOHN F, disagreeing on the middle initial. Neither conflict is silently
resolved and no occupation or employer data are transferred. The two **Robert
G Neumann** rows remain separate, ambiguous entities in duplicate group
`b700-robert-g-neumann-rows43-44`.

A Beloit College biography is a plausible identity lead for **Paul H
Nesbitt**, but the accessible source does not bridge that person to the index
record with a protected identifier or other sufficiently specific wartime
evidence. His identity remains `probable`, and no Beloit affiliation is
published as fact. Existing verified-employer outcomes for **Franz L Neumann**
and **Sigmund Neumann** are preserved.

The current Library of Congress API produced seven discovery candidates.
Official OCR page context for every candidate was reviewed, and all seven were
rejected as unrelated namesakes or contexts that did not establish identity or
pre-OSS work. The CIA adapter failed closed at the site's robots policy without
sending a search request. Exact-name, employment, obituary, institutional, and
archival searches were completed for the cohort. No raw LoC or NARA API
response is retained.

The cohort ends with one `completed`, two `conflicting_sources`, three
`needs_identity_review`, 15 `no_reliable_result_after_protocol`, and two
pre-existing `verified_employer_found` outcomes. Identity statuses are one
`confirmed`, seven `high_confidence`, two `conflicting`, one `probable`, two
`ambiguous`, and ten `unresolved`. Across the cohort, including the two
pre-existing researched people, claims are one confirmed, 12 high, two medium,
two conflicting, and two unresolved.

The evidence bundle imports seven sources, three organizations, three
affiliations, 13 claims, 29 claim-source links, 21 person updates, and 21
consolidated research attempts. The review decisions accept six Army identity
candidates, preserve three conflicts, and reject seven LoC discovery
candidates.

Rebuilt coverage is **23,978/23,978** linked source rows and **23,939** active
person entities. Research-attempt coverage is **9,142/23,939 (38.1887%)**;
confirmed/high verified-employer coverage is **317/23,939 (1.3242%)**;
confirmed/high verified-affiliation coverage is **704/23,939 (2.9408%)**;
archival-review disposition coverage is **7,599/23,939 (31.7432%)**. There are
**14,792** `not_started` people, **521** possible-duplicate groups, and **270**
active conflicts. SQLite stores **16,473** attempts or plans and **5,906**
claims: 1,344 confirmed, 2,655 high, 1,466 medium, 196 low, 243 conflicting,
and two unresolved. It contains **5,479** citation records and **2,713** unique
source documents. The public projection contains **2,386** affiliations,
**806** organizations, **4,262** sources, and **5,701** claims. Full-index
historical research remains unfinished.

## Replay and continuation

After importing prior durable batches into private SQLite:

```sh
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
python3 -m oss_research assign-page-batch --batch-name batch-700 --page 340 --first-row 23 --last-row 45
python3 -m oss_research research --source cia --batch batch-700 --max-queries 23
python3 -m oss_research research --source loc --batch batch-700 --max-queries 23
python3 scripts/inspect_loc_candidates.py --batch batch-700 --max-candidates 7 --delay 3.2
python3 -m oss_research import-review-decisions research/identity_review_decisions_2026-10-03_batch700.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page340-nesbitt-neumann-review_batch-700_2026-10-03.json
python3 -m oss_research export-adapter-checkpoints
python3 -m oss_research export-derived
python3 -m oss_research export-review-queue
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
```

Adapter checkpoints must be imported before final reviewed decisions and
evidence so temporary discovery states cannot supersede reviewed dispositions.
The next research boundary begins at PDF page 340, row 46.

No API key, full service number, raw Catalog or LoC API response, copyrighted
page image, unrelated Army coded occupation, street address, or private
reviewer note is committed or included in the public site. No authenticated
NARA Catalog API request was made for this batch.
