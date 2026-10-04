# Batch 732: Panzarella-Papoulias research

Batch 732 covers PDF page 356, rows 24-46, from **Neal M Panzarella**
through **Arthur D Papoulias**. A 300-dpi visual inspection confirmed all 23
printed rows in Boxes 583-584 at location 230/86/38/02. Embedded text was
checked against the render, and original spellings, ranks, grades, notes, and
protected identifiers remain recoverable in the private database.

The review also follows the protected identifier printed for **Arthur A
Pape** and **Arthur A Paper** to a third row, **Arthur A Pope**, on PDF page
373, row 27, Box 612. All three source rows and person entities remain
separate. The shared identifier is published as a conflict requiring physical
file review, not used as authority for an automatic merge.

Five people receive confirmed identities from direct official roster evidence:
**George J Papastrat**, **James Papavassiliou**, **Spiridon Papayiannakis**,
**George Papazoglou**, and **Arthur D Papoulias**. Seven receive
high-confidence identities from official Army bulk matches, sometimes with
explicitly preserved spelling or identifier anomalies: **Neal M Panzarella**,
**William E Paone**, **Athanasios A Papageorgiou**, **Frank M Papale Jr.**,
**Nicholas D Papanu**, **Frederick D Pape**, and **Carl J Papenfuss**. Silvia
Papini remains conflicting because the Army record says Silvio; Constantine
Papadopoulos remains unresolved because a museum narrative about an OSS radio
operator does not supply the indexed naval identifier.

A declassified OSS roster, a Greek Battalion history, and a monument roster
together support a qualified 122nd Infantry Battalion (Separate) pathway for
Nicholas Papanu, George Papastrat, James Papavassiliou, Spiridon
Papayiannakis, George Papazoglou, and Arthur Papoulias. Each relationship is
published as a medium-confidence, probable-immediate **military assignment**.
No individual transfer order was located, and none is labeled a civilian
employer. Papanu/Papapanu's spelling and transposed roster digits,
Papayiannakis/Papayannakis's spelling and middle initial, Papazoglou's first
lieutenant/captain ranks, and Papoulias's D/J middle-initial conflict all
remain visible.

The CIA adapter failed closed under the source's robots policy, and the
Library of Congress adapter encountered a transport timeout on the first
bounded request in each new queue. The web adapter saved deterministic query
plans before manual staged review. No authenticated NARA Catalog API request
was made because the local project did not expose a key to this run.

The 23 page-356 people end with 20 `requires_archival_review` and three
`conflicting_sources` outcomes; the linked Pope profile adds a fourth conflict.
Across the 24 reviewed profiles, identity statuses are five `confirmed`, seven
`high_confidence`, four `conflicting`, and eight `unresolved`. The reviewed
bundle imports six sources, reuses one organization, adds six affiliations,
22 claims, 52 claim-source links, 24 person updates, and 24 consolidated
research attempts. Ten accepted and four conflicting identity-review
decisions are recorded.

Rebuilt coverage is **23,978/23,978** linked source rows and **23,939** active
person entities. Research-attempt coverage is **9,872/23,939 (41.2381%)**;
confirmed/high verified-employer coverage is **333/23,939 (1.3910%)**;
confirmed/high verified-affiliation coverage is **743/23,939 (3.1037%)**;
archival-review disposition coverage is **8,330/23,939 (34.7968%)**. There
are **14,062** `not_started` people, **523** possible-duplicate groups, and
**327** active conflicts. SQLite stores **18,034** attempts or plans and
**6,331** claims: 1,378 confirmed, 2,929 high, 1,535 medium, 198 low, 289
conflicting, and two unresolved. It contains **5,694** citation records and
**2,876** unique source documents. The public projection contains **2,485**
affiliations, **861** organizations, **4,475** sources, and **6,124** claims.
Full-index historical research remains unfinished.

## Replay and continuation

After importing prior durable batches into private SQLite:

```sh
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
python3 -m oss_research assign-page-batch --batch-name batch-732-panzarella-papa --page 356 --first-row 24 --last-row 27
python3 -m oss_research assign-page-batch --batch-name batch-732-papadopoulos-papoulias --page 356 --first-row 29 --last-row 46
python3 -m oss_research assign-page-batch --batch-name batch-732-duplicate-cluster --page 373 --first-row 27 --last-row 27
python3 -m oss_research research --source cia --batch batch-732-panzarella-papa --max-queries 4
python3 -m oss_research research --source loc --batch batch-732-panzarella-papa --max-queries 4
python3 -m oss_research research --source web --batch batch-732-panzarella-papa --resume --max-queries 4 --dry-run
python3 -m oss_research research --source cia --batch batch-732-papadopoulos-papoulias --max-queries 18
python3 -m oss_research research --source loc --batch batch-732-papadopoulos-papoulias --max-queries 18
python3 -m oss_research research --source web --batch batch-732-papadopoulos-papoulias --resume --max-queries 18 --dry-run
python3 -m oss_research import-review-decisions research/identity_review_decisions_2026-10-04_batch732.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page356-panzarella-papoulias-review_batch-732_2026-10-04.json
python3 -m oss_research export-adapter-checkpoints
python3 -m oss_research export-derived
python3 -m oss_research export-review-queue
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
```

Constantine Papadopoulos remains assigned to `pilot-v1`; the Batch 732 review
adds a resumable recheck without overwriting that earlier ownership. Adapter
checkpoints must be imported before final reviewed decisions and evidence so
temporary discovery states cannot supersede reviewed dispositions. The next
research boundary is PDF page 357, rows 1-23, from Charles A Papouschek
through Jean P Parent.

No API key, full service or officer number, raw Catalog or LoC API response,
copyrighted page image, street address, living-relative detail, modern
people-finder record, or private reviewer note is committed or included in
the public site. No authenticated NARA Catalog API request was made for this
batch.
