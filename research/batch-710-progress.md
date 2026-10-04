# Batch 710: Novak-Nupen research

Batch 710 covers PDF page 345, rows 24-46, from **Francis J Novak** through
**Edly D Nupen**. Fresh 300-dpi visual inspection confirmed all 23 printed
rows, representing 23 active person entities. The immutable extraction is
unchanged.

Eight people now have high-confidence identities. Official Army records
support **John J Novak**, **Michael J Novosel**, **Chester S Nowik**, **Robert
P Noyes**, **Benjamin B Null**, **Jose R Nunez**, and **Guy T Nunn Jr.** A
Little Norway personnel roster and a later Department of Justice report
support **Edly Daniel Nupen** while leaving his chronology relative to OSS
unresolved. The Army occupation codes were used only for identity resolution
and were not converted into employment claims.

One affiliation meets publication standards. An official Army history and the
Michael J. Novosel Foundation biography establish Novosel's Army air-service
path into four months of OSS special duty in 1943. The site publishes this as
a strongly date-bounded **military assignment** with the historical wording
“Army Air Corps,” not as a civilian employer. No Batch 710 civilian employer
claim met the publication threshold.

Four source rows remain distinct within two shared-identifier conflicts:
**Joseph A Novatnik / Joseph A Novotnik** and **Robert S Nowell / Robin S
Nowell**. No same-name or same-number merge was made. A 1947 *Interiors*
article documents a designer named Dorothy Q. Noyes, but the evidence does not
identify the OSS index person. That lead remains private and low-confidence;
Dorothy's public profile instead directs researchers to the indexed Box 564
file. Public identifiers remain masked.

The CIA and Library of Congress adapters failed closed without usable adapter
results. Exact-name OSS, employment, occupation, institutional, newspaper,
obituary, military, directory, and archival searches were nevertheless
reviewed for every person. The cohort ends with 15
`no_reliable_result_after_protocol`, four `conflicting_sources`, three
`requires_archival_review`, and one `completed` outcome. Identity statuses are
eight `high_confidence`, four `probable`, and 11 `unresolved`. The reviewed
bundle imports seven sources, one organization, one affiliation, 14 claims,
25 claim-source links, 23 person updates, and 23 consolidated research
attempts. Claim decisions comprise nine high-confidence published claims,
four medium-confidence qualified claims, and one low-confidence withheld
lead. Ten review decisions are recorded and imported.

Rebuilt coverage is **23,978/23,978** linked source rows and **23,939** active
person entities. Research-attempt coverage is **9,369/23,939 (39.1370%)**;
confirmed/high verified-employer coverage is **323/23,939 (1.3493%)**;
confirmed/high verified-affiliation coverage is **716/23,939 (2.9909%)**;
archival-review disposition coverage is **7,827/23,939 (32.6956%)**. There are
**14,565** `not_started` people, **523** possible-duplicate groups, and **291**
active conflicts. SQLite stores **16,969** attempts or plans and **6,052**
claims: 1,352 confirmed, 2,750 high, 1,495 medium, 197 low, 256 conflicting,
and two unresolved. It contains **5,554** citation records and **2,775** unique
source documents. The public projection contains **2,419** affiliations,
**830** organizations, **4,336** sources, and **5,846** claims. Full-index
historical research remains unfinished.

## Replay and continuation

After importing prior durable batches into private SQLite:

```sh
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
python3 -m oss_research assign-page-batch --batch-name batch-710 --page 345 --first-row 24 --last-row 46
python3 -m oss_research research --source cia --batch batch-710 --max-queries 23
python3 -m oss_research research --source loc --batch batch-710 --max-queries 23
python3 -m oss_research research --source web --batch batch-710 --resume --max-queries 23
python3 -m oss_research import-review-decisions research/identity_review_decisions_2026-10-03_batch710.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page345-novak-nupen-review_batch-710_2026-10-03.json
python3 -m oss_research export-adapter-checkpoints
python3 -m oss_research export-derived
python3 -m oss_research export-review-queue
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
```

Adapter checkpoints must be imported before final reviewed decisions and
evidence so temporary discovery states cannot supersede reviewed dispositions.
The next research boundary begins at PDF page 346, row 1 (**Robert C Nusbaum**).

No API key, full service number, raw Catalog or LoC API response, copyrighted
page image, unrelated Army coded occupation, address, phone number, modern
people-finder record, or private reviewer note is committed or included in the
public site. No authenticated NARA Catalog API request was made for this batch.
