# Batch 733: Papouschek-Parent research

Batch 733 covers PDF page 357, rows 1-23, from **Charles A
Papouschek** through **Jean P Parent**. A 300-dpi visual inspection confirmed
all 23 printed rows in Boxes 584-585 at location 230/86/38/02. Embedded text
was checked against the render, including George L Pappageorge's clipped
`folder se` note. Original spellings, ranks, grades, notes, and protected
identifiers remain recoverable in the private database.

Two separately printed rows, **Charles S Pappageorge** and **George L
Pappageorge**, share one protected identifier but have different given names
and ranks. Both source rows and person entities remain separate. The shared
identifier is published as a conflict requiring Box 584 review, not used as
authority for an automatic merge.

Three people receive confirmed identities. A declassified OSS Greece roster
matches **George J Pappas** and **Nicholas G Pappas** by full name, rank, and
protected identifier, while an independent Operational Groups roster
corroborates their assignments. The rare full name and major rank of
**Maxwell J Papurt** agree between the index and an official OSS/SCI record.
Seven other people receive high-confidence identities from exact official Army
bulk matches with nonshared protected identifiers: **Charles A Papouschek**,
**Spiro V Pappas**, **Zeff Pappas**, **Frixos P Pappitsas**, **Roland A
Papucci**, **Stephen F Papula**, and **Gaston J Paquette**.

A unit history, monument roster, and declassified OSS roster support qualified
122nd Infantry Battalion (Separate) pathways for George J Pappas and Nicholas
G Pappas. Each relationship is published as a medium-confidence,
probable-immediate **military assignment**. No individual transfer order was
located, and neither is labeled a civilian employer.

A contemporary 26 December 1941 newspaper identifies Maxwell J Papurt as
executive director of the **Pride of Judea Children's Home** in Brooklyn and
as the former chief psychologist of the **New York State Department of
Correction**. Both are published at high confidence as documented prewar
employment. Neither is labeled the immediate pre-OSS affiliation or last
civilian employer because the accessible source does not establish that
sequence.

Two unusual-name leads remain deliberately qualified. French archival and
resistance-network sources make **Jean Lucien Pardimene** a probable match for
the indexed Jean L Pardimene, and Italian archival and naval sources make a
wartime naval officer named **Gastone Pardo** a probable match. Neither lead
has a protected identifier or direct personnel-file linkage, so neither
receives a published affiliation. A memorial entry for an Angelo Pappas in
the Greek Operational Group was rejected as an identity resolution because
the common name lacks the indexed rank and protected identifier.

The CIA adapter failed closed under the source's access policy. The Library of
Congress adapter completed one bounded query and recorded one access error.
The web adapter saved 23 deterministic query plans before manual staged
review. No authenticated NARA Catalog API request was made because a key was
not exposed to this run.

All 23 reviewed people now have terminal dispositions: 20
`requires_archival_review`, two `conflicting_sources`, and one
`documented_prewar_employer_found`. Identity statuses are three
`confirmed`, seven `high_confidence`, two `probable`, two
`conflicting`, and nine `unresolved`. The reviewed bundle imports 13
sources, reuses one organization, adds two organizations and four
affiliations, 16 claims, 33 claim-source links, 23 person updates, and 23
consolidated research attempts. Seven accepted and two conflicting
identity-review decisions are recorded.

Rebuilt coverage is **23,978/23,978** linked source rows and **23,939** active
person entities. Research-attempt coverage is **9,895/23,939 (41.3342%)**;
confirmed/high verified-employer coverage is **334/23,939 (1.3952%)**;
confirmed/high verified-affiliation coverage is **744/23,939 (3.1079%)**;
archival-review disposition coverage is **8,353/23,939 (34.8929%)**. There
are **14,039** `not_started` people, **523** possible-duplicate groups, and
**329** active conflicts. SQLite stores **18,083** attempts or plans and
**6,347** claims: 1,381 confirmed, 2,938 high, 1,537 medium, 198 low, 291
conflicting, and two unresolved. It contains **5,707** citation records and
**2,885** unique source documents. The public projection contains **2,489**
affiliations, **863** organizations, **4,483** sources, and **6,140** claims.
Full-index historical research remains unfinished.

## Replay and continuation

After importing prior durable batches into private SQLite:

```sh
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
python3 -m oss_research assign-page-batch --batch-name batch-733-papouschek-parent --page 357 --first-row 1 --last-row 23
python3 -m oss_research research --source cia --batch batch-733-papouschek-parent --max-queries 23
python3 -m oss_research research --source loc --batch batch-733-papouschek-parent --max-queries 23
python3 -m oss_research research --source web --batch batch-733-papouschek-parent --resume --max-queries 23 --dry-run
python3 -m oss_research import-review-decisions research/identity_review_decisions_2026-10-04_batch733.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page357-papouschek-parent-review_batch-733_2026-10-04.json
python3 -m oss_research export-adapter-checkpoints
python3 -m oss_research export-derived
python3 -m oss_research export-review-queue
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
```

Adapter checkpoints must be imported before final reviewed decisions and
evidence so temporary discovery states cannot supersede reviewed dispositions.
The next research boundary is PDF page 357, rows 24-46, from Robert E Parent
through Hilda B Parker.

No API key, full service or officer number, raw Catalog or LoC API response,
copyrighted page image, street address, living-relative detail, modern
people-finder record, or private reviewer note is committed or included in
the public site. No authenticated NARA Catalog API request was made for this
batch.
