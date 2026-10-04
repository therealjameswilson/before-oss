# Batch 709: Norris-Novak research

Batch 709 covers PDF page 345, rows 1-23, from **Laura M Norris** through
**Charles J Novak**. Fresh 300-dpi visual inspection confirmed all 23 printed
rows, representing 23 active person entities. The immutable extraction is
unchanged. The render confirms that Leonard E Norris's row prints the
four-digit value `5633`, and that the adjacent Wilson K Norton and William A
Norwood rows print the same identifier. Those anomalies are preserved rather
than silently repaired.

Seven people are high-confidence identity matches. Official Army evidence
supports **Steve F Norsic Jr.**, **Irving M Norton**, **William A Norton**,
**William A Notbohm**, **Theodore Notides**, and **Charles J Novak**. Cornell's
1941 commencement record and a contemporary Troy newspaper together support
**Robert P Northup** through exact name, Round Lake locality, captain rank, Army
Air Forces context, and mechanical-engineering education.

Three affiliations meet publication standards. Robert Northup's June 1941
Mechanical Engineering degree is published strictly as a Cornell University
student affiliation, never as employment. A contemporary banking journal
digitized by the Federal Reserve Bank of St. Louis documents Theodore Notides
at Manufacturers Trust Company beginning in 1941; official Army evidence dates
his entry to 26 August 1942, making this a strongly date-bounded last civilian
employer without claiming immediate succession to OSS. The same journal
documents three earlier years at Corn Exchange Bank & Trust Company, published
as earlier prewar employment. A Library of Congress finding aid independently
corroborates the Notides-Manufacturers Trust association.

Four identity conflicts remain visible. The Army file associated with **David
T Northault** prints David T Northcutt, and the one associated with **Rudolf S
Nothmann** prints Nothman. Both spelling variants remain visible and neither is
treated as a correction. The adjacent **Wilson K Norton** and **William A
Norwood** rows remain separate people in one possible-duplicate group pending
comparison of their Box 564 files. Public pages expose only masked serial
suffixes. Leonard Norris, Mary T Norris, and Genevieve M Noto receive explicit
archival-review outcomes because the short printed value, `folders s` note,
and `possible` note require file-level context.

The CIA and Library of Congress adapters failed closed without usable adapter
results. Exact-name OSS, employment, occupation, institutional, newspaper,
obituary, military, directory, and archival searches were nevertheless
reviewed for every person. The cohort ends with 14
`no_reliable_result_after_protocol`, four `conflicting_sources`, three
`requires_archival_review`, one `completed`, and one
`verified_employer_found` outcome. Identity statuses are seven
`high_confidence`, two `probable`, two `conflicting`, and 12 `unresolved`. The
reviewed bundle imports six sources, three organizations, three affiliations,
14 claims, 28 claim-source links, 23 person updates, and 23 consolidated
research attempts. Claim decisions comprise ten high-confidence, two
medium-confidence, and two conflicting claims. Ten review decisions are
recorded and imported.

Rebuilt coverage is **23,978/23,978** linked source rows and **23,939** active
person entities. Research-attempt coverage is **9,346/23,939 (39.0409%)**;
confirmed/high verified-employer coverage is **323/23,939 (1.3493%)**;
confirmed/high verified-affiliation coverage is **715/23,939 (2.9868%)**;
archival-review disposition coverage is **7,804/23,939 (32.5995%)**. There are
**14,588** `not_started` people, **523** possible-duplicate groups, and **287**
active conflicts. SQLite stores **16,920** attempts or plans and **6,038**
claims: 1,352 confirmed, 2,741 high, 1,491 medium, 196 low, 256 conflicting,
and two unresolved. It contains **5,547** citation records and **2,769** unique
source documents. The public projection contains **2,418** affiliations,
**830** organizations, **4,330** sources, and **5,833** claims. Full-index
historical research remains unfinished.

## Replay and continuation

After importing prior durable batches into private SQLite:

```sh
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
python3 -m oss_research assign-page-batch --batch-name batch-709 --page 345 --first-row 1 --last-row 23
python3 -m oss_research research --source cia --batch batch-709 --max-queries 23
python3 -m oss_research research --source loc --batch batch-709 --max-queries 23
python3 -m oss_research research --source web --batch batch-709 --resume --max-queries 23
python3 -m oss_research import-review-decisions research/identity_review_decisions_2026-10-03_batch709.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page345-norris-novak-review_batch-709_2026-10-03.json
python3 -m oss_research export-adapter-checkpoints
python3 -m oss_research export-derived
python3 -m oss_research export-review-queue
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
```

Adapter checkpoints must be imported before final reviewed decisions and
evidence so temporary discovery states cannot supersede reviewed dispositions.
The next research boundary begins at PDF page 345, row 24 (**Francis J Novak**).

No API key, full service number, raw Catalog or LoC API response, copyrighted
page image, unrelated Army coded occupation, address, phone number, modern
people-finder record, or private reviewer note is committed or included in the
public site. No authenticated NARA Catalog API request was made for this batch.
