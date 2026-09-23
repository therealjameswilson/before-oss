# Batch 654: complete extraction audit and Metters-Meyer research

The final **14** previously unaudited original NARA PDF pages (95-100 and
102-109) were rendered at 180 dpi and compared row by row with the immutable
extraction. Page 101 had already been reviewed. This completes visual review
of **522/522 pages** and all **23,978/23,978 printed rows**: **23,946** reviewed
rows match the extraction and **32** retain documented reviewed corrections.
There are no unaudited pages or rows. Every PDF page is represented, every
parser warning is resolved, and SQLite integrity and foreign-key checks pass.

The page-318 `Ruth T. Metters` through `Herman R. Meyer` queue contains **22
source rows and 22 cautious person entities**. Every person received saved
NARA/index-context, CIA Reading Room, exact-name OSS, employment or occupation,
and institutional, newspaper, obituary, or archival research as applicable.
NARA, CIA, and web adapters remained dry-run plans; no authenticated NARA
Catalog request was made. Two live LoC adapter attempts failed closed on a
transient timeout before issuing a completed query. The errors are preserved
as auditable research outcomes rather than treated as negative search results.

The principal findings preserve identity and chronology limits:

- **Lothar Metzl** is confirmed through a personnel-file-grounded institutional
  biography. His immediate pre-OSS assignment was the U.S. Army's 621st
  Quartermaster Depot Company at Camp Polk, from which he was explicitly
  transferred to OSS Morale Operations in May 1944. His best-supported last
  civilian status was freelance playwright, satirist, author, and radio worker
  before his July 1943 Army induction. A radio appearance is not recast as an
  employer.
- **Lloyd A. Metzler** is identified with high confidence as economist Lloyd
  Appleton Metzler. A University of Chicago finding aid documents Harvard
  instructor and tutor work through his 1942 doctorate. Harvard University is
  published as his best-supported last civilian employer with medium temporal
  confidence because the chronology does not exclude an intervening wartime
  government assignment before OSS.
- **Joshua M. Mewborn** receives a high-confidence identity bridge to a 502nd
  Parachute Infantry second lieutenant. That military record is identity
  context only: it does not establish when or whether that assignment was
  immediately before OSS.
- **Rafael P. Mettuhen** remains conflicting because his protected identifier
  also appears on the separate `Rafael P. Miettunen` index row. The two rows
  remain separate pending comparison of Boxes 520 and 522.
- **Adalbert E. Meyer** remains conflicting because his printed identifier
  resolves to the adjacent `Albert L. Meyer` in the official Army bulk data.
  Both source rows remain intact pending comparison of Boxes 521 and 520.
- Eight further people receive accepted official Army identity bridges without
  invented employers. Unresolved names retain explicit archival next actions.

The cohort ends with **18** `requires_archival_review`, one
`verified_employer_found`, one `documented_prewar_employer_found`, and two
`conflicting_sources` statuses. Identity statuses are one `confirmed`, seven
`high_confidence`, two `probable`, two `conflicting`, and ten `unresolved`.
The reviewed evidence bundle adds **15** claims: one confirmed, nine high,
three medium, and two conflicting.

Rebuilt coverage is **23,978/23,978** linked source rows and **23,939** active
person entities. Research-attempt coverage is **8,140/23,939 (34.0031%)**;
confirmed/high verified-employer coverage is **290/23,939 (1.2114%)**;
confirmed/high verified-affiliation coverage is **645/23,939 (2.6943%)**;
archival-review disposition coverage is **6,596/23,939 (27.5534%)**. There are
**15,794** `not_started` people, **494** possible-duplicate groups, and **192**
active conflicts. SQLite stores **14,074** attempts or plans and **5,160**
claims: 1,312 confirmed, 2,082 high, 1,410 medium, 189 low, and 167
conflicting. It contains **5,159** citation records and **2,457** unique source
documents. The public projection contains **2,268** affiliations, **743**
organizations, **3,949** sources, and **4,967** claims.

The oil-company category remains prominently available at the top of the
personnel directory and on its dedicated page. Its evidence-scoped membership
remains **seven people across nine historically named companies**. None of the
Batch 654 findings is an oil-company employment claim. Full-index historical
research is unfinished.

## Replay and continuation

After importing prior durable batches into private SQLite:

```sh
python3 -m oss_research import-page-reviews research/parser_visual_review_pages95-109_2026-09-23.json
python3 -m oss_research import-review-decisions research/identity_review_decisions_2026-09-23_batch654.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page318-metters-meyer-review_batch-654_2026-09-23.json
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
```

Continue with the next bounded research batch, then run:

```sh
python3 -m oss_research export-adapter-checkpoints
python3 -m oss_research export-derived
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
```

No API key, full service number, raw Catalog API response, copyrighted page
image, or private reviewer note is committed or included in the public site.
