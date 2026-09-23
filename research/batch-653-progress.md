# Batch 653: pages 85-94 extraction audit and Mess-Mettenet research

All **460** printed rows on original NARA PDF pages 85-94 were compared with
the immutable extraction at 180 dpi. Pages 87 and 90 were already in the
visual-review set; pages 85, 86, 88, 89, 91, 92, 93, and 94 and their **368**
rows received their first complete visual comparison in this batch. Every row
matches. Complete-page visual review now covers **508/522 pages** and
**23,334/23,978 rows**: **23,302** reviewed rows match the extraction, **32**
retain reviewed corrections, and **644** remain unaudited. Every PDF page
remains represented, every parser warning is resolved, and SQLite integrity
and foreign-key checks pass.

The page-317/318 `Walter L. Mess` through `William J. Mettenet` queue contains
**22 source rows and 22 cautious person entities**. Each person received saved
NARA/index-context, CIA Reading Room, Library of Congress or equivalent
institutional/newspaper, employment/occupation, and targeted-web research.
NARA, CIA, and web adapters remained dry-run plans; no authenticated NARA
Catalog request was made. The LoC API adapter saved one no-result and two
auditable transient timeouts before the official LoC item and all remaining
names were reviewed through targeted public-source discovery. There were no
unreviewed LoC candidates to accept or reject.

The principal findings preserve identity and chronology limits:

- **Walter L. Mess** is identified with high confidence through the Library of
  Congress Veterans History Project and U.S. Army Special Operations history.
  The latter documents Depression-era entrepreneurial property-management work
  in Washington. It is published as earlier prewar self-employment, not as an
  immediate predecessor to OSS.
- **Prentice Messimer** has a high-confidence official Army identity bridge.
  A 1938 San Francisco city directory names him as a J. Walter Thompson
  copywriter; a 1946 trade notice explicitly places wartime OSS service before
  his postwar advertising job. J. Walter Thompson is published as his
  best-supported last civilian employer with medium confidence because the
  sources do not exclude an intervening civilian role after 1938.
- **Rhoda Métraux** retains her previously confirmed chronology: the Committee
  on Food Habits at the National Research Council is immediate and last
  civilian employment; Yale remains student status and Oxford University Press
  earlier employment.
- **Peter C. Messemer, Anthony P. Messina, Frank J. Messina, Claude Metcalf,
  and William J. Mettenet** receive high-confidence official Army identity
  bridges without inferred employers.
- **Nicholas Metal** remains conflicting. An official CIA OSS history lists
  Corporal Nicholas Metal at Field Base C, matching the index name and rank,
  while the protected index identifier points to official Army Welbert
  Charles. Both facts remain visible and Box 520 review is required.
- The two adjacent **Leon C. Messenger** rows remain separate, share a visible
  possible-duplicate group, and require comparison of the Box 519 and Box 520
  files. A 1946 OCR lead for Lawrence C. Messenger was rejected.
- A later Margaret E. Mettenet obituary was rejected because its subject
  acquired Mettenet by marriage in 1963 and cannot identify the wartime index
  row under that surname.

The cohort ends with **18** `requires_archival_review`, two
`documented_prewar_employer_found`, one `verified_employer_found`, and one
`conflicting_sources` status. Identity statuses are seven `high_confidence`,
13 `unresolved`, one `confirmed`, and one `conflicting`. The reviewed evidence
bundle adds **10** claims: eight high, one medium, and one conflicting.

Rebuilt coverage is **23,978/23,978** linked source rows and **23,939** active
person entities. Research-attempt coverage is **8,118/23,939 (33.9112%)**;
confirmed/high verified-employer coverage is **289/23,939 (1.2072%)**;
confirmed/high verified-affiliation coverage is **644/23,939 (2.6902%)**;
archival-review disposition coverage is **6,574/23,939 (27.4615%)**. There are
**15,816** `not_started` people, **493** possible-duplicate groups, and **190**
active conflicts. SQLite stores **13,985** attempts or plans and **5,145**
claims: 1,311 confirmed, 2,073 high, 1,407 medium, 189 low, and 165
conflicting. It contains **5,152** citation records and **2,451** unique source
documents. The public projection contains **2,265** affiliations, **740**
organizations, **3,942** sources, and **4,952** claims.

The oil-company category remains prominently available at the top of the
personnel directory and on its dedicated page. It remains an evidence-scoped
set of **seven people across nine historically named companies**. None of the
Batch 653 findings is an oil-company employment claim. Full-index historical
research is unfinished.

## Replay and continuation

After importing prior durable batches into private SQLite:

```sh
python3 -m oss_research import-page-reviews research/parser_visual_review_pages85-94_2026-09-23.json
python3 -m oss_research import-review-decisions research/identity_review_decisions_2026-09-23_batch653.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page317-318-mess-mettenet-review_batch-653_2026-09-23.json
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
```

Continue with the next bounded research and extraction-audit batch, then run:

```sh
python3 -m oss_research export-adapter-checkpoints
python3 -m oss_research export-derived
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
```

No API key, full service number, raw Catalog API response, copyrighted page
image, or private reviewer note is committed or included in the public site.

