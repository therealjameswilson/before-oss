# Batch 728: Padden-Page research

Batch 728 covers PDF page 354, rows 24-46, from **Charles H Padden** through
**Wellman Page**. A 300-dpi visual inspection confirmed all 23 printed rows,
representing 23 active person entities in Box 580 at location 230/86/38/01.
Embedded text was checked against the render. Original spellings, grades, and
notes remain recoverable. In particular, Lewis W Page's printed note is
truncated to `aka Silvi`; the project preserves that fragment without guessing
the rest. Protected identifiers remain only in the private database.

Seven Army bulk candidates are accepted for identity review. **Fred M
Padgett**, **Harold E Padgett**, **Joseph Padula**, **Joseph M Pagano**,
**George K Page**, **Jimmie Page**, and **Keith A Page** have exact-name and
nonshared protected-identifier matches. No coded Army occupation is converted
into an occupation or employer.

Two official-record conflicts remain explicit. The indexed **Vincent A Pado**
identifier points to an Army row for Vincent A Pade Jr, creating a surname and
suffix conflict. **Andre R Pagatte** shares an indexed private identifier with
the separately researched Andre R Pacatte. The rows remain separate, the full
numbers are not published, and no employment or coded metadata is transferred.

**Henry M Paechter** is linked at high confidence to historian **Henry M.
Pachter**, born **Heinz Maximilian Paechter**. The University at Albany finding
aid explicitly supplies the birth name and records Pachter's OSS work. It also
documents work as a freelance writer and lecturer in Berlin from 1930 through
1933. The site publishes that work as high-confidence, documented-prewar
self-employment. It is not labeled immediate or the last civilian employer:
Pachter's exile and overlapping 1941-1945 OWI and OSS appointments intervene,
and the accessible source does not establish their exact sequence.

**Joseph Padula** is additionally corroborated by the OSS Operational Groups
Simcol roster, which lists T5 Joseph Padula and points to the final reports in
NARA RG 226, Entry 143, Box 9, pages 35-66. This supports wartime identity and
assignment, not a pre-OSS employer. **Saul K Padover** retains his previously
reviewed high-confidence Department of the Interior affiliation; this batch
records a fresh protocol review without duplicating the existing claim.

A 1937 San Diego salesman named Harold E Padgett lacks a corroborating
identifier and is rejected. Census and genealogy results for Sosteno Padilla,
common-name obituaries and directories for the Page cohort, ambassador material
for Walter H Page, and modern people-finder results do not establish the
indexed people's identities or pre-OSS employment. No namesake lead is
promoted to a public fact.

The CIA and Library of Congress adapters failed closed in bounded attempts,
and the web adapter recorded deterministic query plans before manual staged
review. No authenticated NARA Catalog request was made because the local
project did not expose a key to this run.

The cohort ends with 19 `requires_archival_review`, two
`conflicting_sources`, one `documented_prewar_employer_found`, and one existing
`verified_employer_found` outcome. Identity statuses are 12 `unresolved`, nine
`high_confidence`, and two `conflicting`. The reviewed bundle imports four
sources, one canonical-organization reuse, one affiliation, 11 claims, 21
claim-source links, 23 person updates, and 23 consolidated research attempts.
Seven accepted and two conflicting identity-review decisions are recorded.

Rebuilt coverage is **23,978/23,978** linked source rows and **23,939** active
person entities. Research-attempt coverage is **9,780/23,939 (40.8538%)**;
confirmed/high verified-employer coverage is **331/23,939 (1.3827%)**;
confirmed/high verified-affiliation coverage is **739/23,939 (3.0870%)**;
archival-review disposition coverage is **8,238/23,939 (34.4125%)**. There
are **14,154** `not_started` people, **523** possible-duplicate groups, and
**321** active conflicts. SQLite stores **17,840** attempts or plans and
**6,271** claims: 1,370 confirmed, 2,896 high, 1,524 medium, 198 low, 281
conflicting, and two unresolved. It contains **5,665** citation records and
**2,859** unique source documents. The public projection contains **2,472**
affiliations, **858** organizations, **4,446** sources, and **6,064** claims.
The oil-company directory remains nine cited people across eleven historically
named companies. Full-index historical research remains unfinished.

## Replay and continuation

After importing prior durable batches into private SQLite:

```sh
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
python3 -m oss_research assign-page-batch --batch-name batch-728 --page 354 --first-row 24 --last-row 46
python3 -m oss_research research --source cia --batch batch-728 --max-queries 23
python3 -m oss_research research --source loc --batch batch-728 --max-queries 23
python3 -m oss_research research --source web --batch batch-728 --resume --max-queries 23 --dry-run
python3 -m oss_research import-review-decisions research/identity_review_decisions_2026-10-04_batch728.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page354-padden-page-review_batch-728_2026-10-04.json
python3 -m oss_research export-adapter-checkpoints
python3 -m oss_research export-derived
python3 -m oss_research export-review-queue
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
```

Adapter checkpoints must be imported before final reviewed decisions and
evidence so temporary discovery states cannot supersede reviewed dispositions.
The next research boundary is PDF page 355, rows 1-23, from William R Page
through George Pallay.

No API key, full service or officer number, raw Catalog or LoC API response,
copyrighted page image, street address, living-relative detail, modern
people-finder record, or private reviewer note is committed or included in the
public site. No authenticated NARA Catalog API request was made for this batch.
