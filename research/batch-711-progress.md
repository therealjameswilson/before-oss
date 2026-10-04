# Batch 711: Nusbaum-Obata research

Batch 711 covers PDF page 346, rows 1-23, from **Robert C Nusbaum** through
**Chiura Z Obata**. Fresh 300-dpi visual inspection confirmed all 23 printed
rows, representing 23 active person entities. The immutable extraction is
unchanged. The index spellings “Nuttal” and “Nygaro,” Hans A Nyholm's note
“also AS,” and Chiura Z Obata's truncated note “file sent t” are preserved
exactly as printed.

Eight people now have high-confidence identities. Four nonshared official Army
identifiers support **Robert C Nusbaum**, **Julius Nyarady**, **Hugh F Oates**,
and **William J Oates Jr.** Direct institutional or official sources support
**Seymour Nydorf**, **Hans Alfred Nyholm**, **John Bertram Oakes**, and
**Chiura (Zoroku) Obata**. Army occupation codes were used only for identity
resolution and were not converted into employer or occupation claims.

Six affiliations meet publication standards. A Virginia General Assembly
resolution explicitly places Nusbaum in the United States Army and then the
OSS; his Army service is published as the immediate pre-OSS military
assignment. The same source documents interrupted Harvard College study,
which is separately classified as student status, not employment. Columbia
Journalism School and a CIA historical study support John B Oakes's identity,
his last identifiable civilian employer at **The Washington Post**, and his
earlier reporting at the **Trenton Times**. The Washington Post chronology is
strongly date-bounded rather than described as an explicit OSS transfer.

The National Museum of Denmark documents Hans A Nyholm's prewar Royal Danish
Navy career and 1937 promotion to *orlogskaptajn*. UC Berkeley documents
Chiura Z Obata's faculty employment from 1932 until his forced 1942 departure.
Both are published only as documented pre-OSS affiliations: Box 565 or 566 is
still needed to establish the exact sequence relative to OSS service. A
Library of Congress catalog record and contemporaneous publication identify
Seymour Nydorf as an OSS graphic artist, but that OSS occupation is not
misrepresented as a pre-OSS employer.

Protected Army identifiers conflict with the indexed names for **Philip J
Nyquist** and **Dale W Oakley**. Those candidates were rejected and both
profiles remain visibly conflicting; neither mismatched Army occupation code
was published. A rare-name biography makes a chemist identity plausible for
**Willem A Nyland**, but accessible direct evidence did not adequately link
that person to the OSS row or establish a named pre-OSS employer. The lead
remains private and low-confidence, while the public profile directs research
to Box 565.

The CIA and Library of Congress adapters failed closed without usable adapter
results. Exact-name OSS, employment, occupation, institutional, newspaper,
obituary, military, directory, and archival searches were nevertheless
reviewed for every person. The cohort ends with 15
`no_reliable_result_after_protocol`, three `requires_archival_review`, two
`conflicting_sources`, one `completed`, one
`documented_prewar_employer_found`, and one `verified_employer_found` outcome.
Identity statuses are eight `high_confidence`, two `conflicting`, one
`probable`, and 12 `unresolved`. The reviewed bundle imports ten sources, six
organizations, six affiliations, 17 claims, 33 claim-source links, 23 person
updates, and 23 consolidated research attempts. Claim decisions comprise 14
high-confidence published claims, two medium-confidence qualified conflicts,
and one low-confidence withheld lead. Six manual identity-review decisions
are recorded and imported.

Rebuilt coverage is **23,978/23,978** linked source rows and **23,939** active
person entities. Research-attempt coverage is **9,392/23,939 (39.2331%)**;
confirmed/high verified-employer coverage is **325/23,939 (1.3576%)**;
confirmed/high verified-affiliation coverage is **720/23,939 (3.0076%)**;
archival-review disposition coverage is **7,850/23,939 (32.7917%)**. There are
**14,542** `not_started` people, **523** possible-duplicate groups, and **293**
active conflicts. SQLite stores **17,017** attempts or plans and **6,069**
claims: 1,352 confirmed, 2,764 high, 1,497 medium, 198 low, 256 conflicting,
and two unresolved. It contains **5,564** citation records and **2,784** unique
source documents. The public projection contains **2,425** affiliations,
**832** organizations, **4,345** sources, and **5,862** claims. Full-index
historical research remains unfinished.

## Replay and continuation

After importing prior durable batches into private SQLite:

```sh
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
python3 -m oss_research assign-page-batch --batch-name batch-711 --page 346 --first-row 1 --last-row 23
python3 -m oss_research research --source cia --batch batch-711 --max-queries 23
python3 -m oss_research research --source loc --batch batch-711 --max-queries 23
python3 -m oss_research research --source web --batch batch-711 --resume --max-queries 23
python3 -m oss_research import-review-decisions research/identity_review_decisions_2026-10-03_batch711.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page346-nusbaum-obata-review_batch-711_2026-10-03.json
python3 -m oss_research export-adapter-checkpoints
python3 -m oss_research export-derived
python3 -m oss_research export-review-queue
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
```

Adapter checkpoints must be imported before final reviewed decisions and
evidence so temporary discovery states cannot supersede reviewed dispositions.
The next research boundary begins at PDF page 346, row 24 (**Donald W
Obenshain**).

No API key, full service number, raw Catalog or LoC API response, copyrighted
page image, unrelated Army coded occupation, address, phone number, modern
people-finder record, or private reviewer note is committed or included in the
public site. No authenticated NARA Catalog API request was made for this batch.
