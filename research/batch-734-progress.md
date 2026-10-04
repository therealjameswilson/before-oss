# Batch 734: Parent-Parker research

Batch 734 covers PDF page 357, rows 24-46, from **Robert E Parent** through
**Hilda B Parker**. A 300-dpi visual inspection confirmed all 23 printed rows
in Boxes 585-586 at location 230/86/38/02. Embedded text was checked against
the render, including the box transition between Evan J Parker Jr. and Frank B
Parker. Original spellings, ranks, grades, and protected identifiers remain
recoverable in the private database.

One identity is confirmed. An official National Park Service OSS history names
**Nelson B Paris** as the naval photographer who recorded the Dawes Mission,
matching his rare indexed full name and naval photographic rating. The source
documents his OSS role, not the organization immediately before OSS service,
so it does not create a pre-OSS affiliation.

Seven people receive high-confidence identities. Exact official Army bulk
matches with nonshared protected identifiers resolve **Robert E Parent**,
**Ernest L Paris**, **Bernard H Parisky**, **Ki B Park**, **Franklin P Parker**,
and **Henry S Parker**. Those matches establish identity only; protected
identifiers and coded Army data remain private and are not converted into
employer claims. A Texas Tech archival interview identifies **Evan J Parker
Jr.** as an OSS Jedburgh veteran, while Cornell institutional class notes
independently place Evan J Parker in the Class of 1941.

Evan Parker's Cornell connection is published as a high-confidence,
documented-prewar **student** affiliation. It is not employment and is not
presented as either his immediate pre-OSS affiliation or last civilian
employer. His indexed Box 585 personnel file remains necessary to establish
that chronology.

The indexed protected identifier for **Jesse Paris** points to an official
Army bulk record named **TRUITT GEORGE S**. The two official names conflict, so
no Army metadata is transferred, no convenient identity is selected, and the
case receives critical Box 585 review priority. Fourteen other people remain
unresolved after staged official-context, exact-name, employment, obituary,
newspaper, institutional, directory, and archival searches. Discovery-only
genealogy and namesake pages were rejected rather than published.

The CIA adapter failed closed under the source's access policy. The Library of
Congress adapter recorded one bounded access error. The web adapter saved 23
deterministic query plans before manual staged review. No authenticated NARA
Catalog API request was made because a key was not exposed to this run.

All 23 reviewed people now have terminal dispositions: 22
`requires_archival_review` and one `conflicting_sources`. Identity statuses
are one `confirmed`, seven `high_confidence`, one `conflicting`, and 14
`unresolved`. The reviewed bundle reuses one organization and imports five
sources, one student affiliation, 10 claims, 21 claim-source links, 23 person
updates, and 23 consolidated research attempts. Six accepted and one
conflicting identity-review decisions are recorded.

Rebuilt coverage is **23,978/23,978** linked source rows and **23,939** active
person entities. Research-attempt coverage is **9,918/23,939 (41.4303%)**;
confirmed/high verified-employer coverage is **334/23,939 (1.3952%)**;
confirmed/high verified-affiliation coverage is **745/23,939 (3.1121%)**;
archival-review disposition coverage is **8,376/23,939 (34.9889%)**. There
are **14,016** `not_started` people, **523** possible-duplicate groups, and
**330** active conflicts. SQLite stores **18,131** attempts or plans and
**6,357** claims: 1,382 confirmed, 2,946 high, 1,537 medium, 198 low, 292
conflicting, and two unresolved. It contains **5,712** citation records and
**2,888** unique source documents. The public projection contains **2,490**
affiliations, **863** organizations, **4,488** sources, and **6,150** claims.
Full-index historical research remains unfinished.

## Replay and continuation

After importing prior durable batches into private SQLite:

```sh
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
python3 -m oss_research assign-page-batch --batch-name batch-734-parent-parker --page 357 --first-row 24 --last-row 46
python3 -m oss_research research --source cia --batch batch-734-parent-parker --max-queries 23
python3 -m oss_research research --source loc --batch batch-734-parent-parker --max-queries 23
python3 -m oss_research research --source web --batch batch-734-parent-parker --resume --max-queries 23 --dry-run
python3 -m oss_research import-review-decisions research/identity_review_decisions_2026-10-04_batch734.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page357-parent-parker-review_batch-734_2026-10-04.json
python3 -m oss_research export-adapter-checkpoints
python3 -m oss_research export-derived
python3 -m oss_research export-review-queue
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
```

Adapter checkpoints must be imported before final reviewed decisions and
evidence so temporary discovery states cannot supersede reviewed dispositions.
The next research boundary is PDF page 358, rows 1-23, from James C Parker
through Marian A Parrott.

No API key, full service or officer number, raw Catalog or LoC API response,
copyrighted page image, street address, living-relative detail, modern
people-finder record, or private reviewer note is committed or included in the
public site. No authenticated NARA Catalog API request was made for this batch.
