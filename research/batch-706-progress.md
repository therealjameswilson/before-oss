# Batch 706: Nishi-Noel research

Batch 706 covers PDF page 343, rows 23-45, from **George H Nishi** through
**James A Noel**. Fresh 300-dpi visual inspection confirmed all 23 printed
rows, representing 23 active person entities. The immutable extraction is
unchanged.

**Katsuma Nishimoto** is a high-confidence identity match to the Military
Intelligence Service Language School student at Camp Savage later documented
as a Southeast Asia translator and intercept specialist. The school is
published as a qualified military assignment with uncertain temporal relation
to OSS service, not as an employer or an immediate pre-OSS affiliation.

**Marshall H Noble** is confirmed through exact name and protected-identifier
evidence across the OSS index, official Army data, and a direct OSS Special
Operations Unit Detachment 101 promotion report. The evidence establishes his
identity and OSS service but does not establish a pre-OSS employer or
affiliation; his full identifier remains private.

**Andre Noel** is a high-confidence match to Second Lieutenant **Andre Noel**,
alias **Andre Ferriere**, the radio operator on OSSEX Team FILAN. A U.S. Army
Special Operations history states that SUSSEX personnel were recruited from
the Free French forces. Because that statement describes the program rather
than an individual transfer order, Free French Forces is published only as a
qualified probable immediate military affiliation. His classification is
corrected to foreign or Allied military personnel while the original index
spelling and rank remain recoverable.

Official Army bulk evidence supports seven additional high-confidence
identity-only decisions: **Donald H Niven**, **Howard D Nixon**, **William B
Nixon**, **George J Niznansky**, **Michael F Noah**, **Alessandro Nocella**, and
**Deane A Noel**. Coded Army occupations are not converted into employer
claims. **Malcolm N Nishioa** remains conflicting with an Army record for
Malcolm M Nishida, and **Yincenzo L Nocella** remains conflicting with an Army
record for Vincenzo L Nocella. Neither pair is silently merged.

The CIA and Library of Congress adapters failed closed without producing a
usable source result. Exact-name OSS, employment, occupation, institutional,
newspaper, obituary, military, and archival searches were nevertheless
reviewed for all 23 people. The cohort ends with two `completed`, two
`conflicting_sources`, and 19 `no_reliable_result_after_protocol` outcomes.
Identity statuses are one `confirmed`, nine `high_confidence`, two
`conflicting`, and 11 `unresolved`.

The reviewed evidence bundle imports six sources, two organizations, two
affiliations, 14 claims, 29 claim-source links, 23 person updates, and 23
consolidated research attempts. Claim decisions comprise one confirmed, nine
high-confidence, two visibly qualified medium-confidence, and two conflicting
claims. Ten review decisions are recorded and imported.

Rebuilt coverage is **23,978/23,978** linked source rows and **23,939** active
person entities. Research-attempt coverage is **9,277/23,939 (38.7527%)**;
confirmed/high verified-employer coverage is **320/23,939 (1.3367%)**;
confirmed/high verified-affiliation coverage is **711/23,939 (2.9700%)**;
archival-review disposition coverage is **7,735/23,939 (32.3113%)**. There are
**14,657** `not_started` people, **523** possible-duplicate groups, and **276**
active conflicts. SQLite stores **16,748** attempts or plans and **5,992**
claims: 1,352 confirmed, 2,711 high, 1,481 medium, 196 low, 250 conflicting,
and two unresolved. It contains **5,524** citation records and **2,751** unique
source documents. The public projection contains **2,410** affiliations,
**823** organizations, **4,307** sources, and **5,787** claims. Full-index
historical research remains unfinished.

## Replay and continuation

After importing prior durable batches into private SQLite:

```sh
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
python3 -m oss_research assign-page-batch --batch-name batch-706 --page 343 --first-row 23 --last-row 45
python3 -m oss_research research --source cia --batch batch-706 --max-queries 23
python3 -m oss_research research --source loc --batch batch-706 --max-queries 23
python3 -m oss_research research --source web --batch batch-706 --resume --max-queries 23
python3 -m oss_research import-review-decisions research/identity_review_decisions_2026-10-03_batch706.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page343-nishi-noel-review_batch-706_2026-10-03.json
python3 -m oss_research export-adapter-checkpoints
python3 -m oss_research export-derived
python3 -m oss_research export-review-queue
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
```

Adapter checkpoints must be imported before final reviewed decisions and
evidence so temporary discovery states cannot supersede reviewed dispositions.
The next research boundary begins at PDF page 343, row 46 (**Joseph L Noel**).

No API key, full service number, raw Catalog or LoC API response, copyrighted
page image, unrelated Army coded occupation, street address, or private
reviewer note is committed or included in the public site. No authenticated
NARA Catalog API request was made for this batch.
