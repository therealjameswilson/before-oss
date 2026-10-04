# Batch 735: Parker-Parrott research

Batch 735 covers PDF page 358, rows 1-23, from **James C Parker** through
**Marian A Parrott**. A 300-dpi visual inspection confirmed all 23 printed
rows in Boxes 586-587 at location 230/86/38/02. Embedded text was checked
against the render, including the box transition between Paul S Parlati and
Devereux Parle. Original spellings, ranks, grades, and protected identifiers
remain recoverable in the private database.

The inspection preserves two unusual printed forms rather than silently
normalizing them. **Lester Parkes** has Pfc printed in the middle-initial
column while the rank column is blank. **Robert R Parrish** has the unfamiliar
grade CSP P, which remains unexpanded and classified as indeterminate.

Six new high-confidence identities come from exact official Army bulk matches
with nonshared protected identifiers: **James C Parker**, **Pierre E Parker**,
**Robert P Parkinson**, **Devereux Parle**, **Otmar B Parolla**, and
**Lawrence E Parr**. These matches establish identity only. Protected
identifiers and coded Army data remain private and are not converted into
employer or occupation claims.

The indexed protected identifier for **Lester Parkes** is also printed for a
separate Robert L Miller row, while the official Army bulk file contains two
exact-name Lester N Parkes records. All three candidate decisions remain
conflicting. No Army metadata is transferred, and Box 586 plus the related
Miller file receive critical archival-review priority.

Two people on this page already had stronger reviewed evidence in durable
earlier bundles. **Charles M Parkin Jr.** retains his high-confidence identity
and confirmed immediate Army Corps of Engineers School assignment at Fort
Belvoir; his Penn State relationship remains student status rather than
employment. **Robert R Parrish** retains his high-confidence film-editor
identity and documented prewar assistant- and sound-editing occupation. No
studio is inferred as his employer, and neither outcome is duplicated in this
batch.

Fourteen people remain unresolved after staged official-context, exact-name,
employment, obituary, newspaper, institutional, directory, and archival
searches. Discovery-only genealogy, modern people-finder, search-snippet, and
unbridged namesake results were rejected rather than published.

The CIA adapter failed closed under the source's access policy. The Library of
Congress adapter recorded one bounded access error. The web adapter saved 23
deterministic query plans before manual staged review. No authenticated NARA
Catalog API request was made because a key was not exposed to this run.

All 23 people have terminal dispositions: 20 requires_archival_review, one
conflicting_sources, one completed, and one occupation_only_found. Identity
statuses are eight high_confidence, one conflicting, and 14 unresolved. The
reviewed bundle imports two sources, seven claims, 14 claim-source links, 23
person updates, and 21 consolidated research attempts; it deliberately reuses
the two earlier completed research outcomes. Six accepted and three
conflicting identity-review decisions are recorded.

Rebuilt coverage is **23,978/23,978** linked source rows and **23,939** active
person entities. Research-attempt coverage is **9,939/23,939 (41.5180%)**;
confirmed/high verified-employer coverage is **334/23,939 (1.3952%)**;
confirmed/high verified-affiliation coverage is **745/23,939 (3.1121%)**;
archival-review disposition coverage is **8,397/23,939 (35.0767%)**. There
are **13,995** not_started people, **523** possible-duplicate groups, and
**331** active conflicts. SQLite stores **18,177** attempts or plans and
**6,364** claims: 1,382 confirmed, 2,952 high, 1,537 medium, 198 low, 293
conflicting, and two unresolved. It contains **5,714** citation records and
**2,889** unique source documents. The public projection contains **2,490**
affiliations, **863** organizations, **4,490** sources, and **6,157** claims.
Full-index historical research remains unfinished.

## Replay and continuation

After importing prior durable batches into private SQLite:

~~~sh
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
python3 -m oss_research assign-page-batch --batch-name batch-735-parker-parrott --page 358 --first-row 1 --last-row 23
python3 -m oss_research research --source cia --batch batch-735-parker-parrott --max-queries 23
python3 -m oss_research research --source loc --batch batch-735-parker-parrott --max-queries 23
python3 -m oss_research research --source web --batch batch-735-parker-parrott --resume --max-queries 23 --dry-run
python3 -m oss_research import-review-decisions research/identity_review_decisions_2026-10-04_batch735.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page358-parker-parrott-review_batch-735_2026-10-04.json
python3 -m oss_research export-adapter-checkpoints
python3 -m oss_research export-derived
python3 -m oss_research export-review-queue
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
~~~

Adapter checkpoints must be imported before final reviewed decisions and
evidence so temporary discovery states cannot supersede reviewed dispositions.
The next research boundary is PDF page 358, rows 24-46, from Arthur J Parry
through John Pascone.

No API key, full service or officer number, raw Catalog or LoC API response,
copyrighted page image, street address, living-relative detail, modern
people-finder record, or private reviewer note is committed or included in the
public site. No authenticated NARA Catalog API request was made for this batch.
