# Batch 655: Meyer-Meysereav research

The PDF-page 318-319 `Jack L. Meyer` through `C. P. Meysereav` queue contains
**22 source rows and 22 cautious person entities**. Every person received a
saved, reviewed outcome from staged NARA-index context, official Army bulk
identity comparison where applicable, exact-name OSS searching, employment or
occupation searching, and institutional, obituary, newspaper, or archival
searching as applicable. No authenticated NARA Catalog request was made.

The CIA Reading Room adapter stopped on the source's robots restriction at the
first query in each bounded sub-batch. The Library of Congress adapter stopped
on a timeout at the first query in each sub-batch. These source-level failures
are retained as errors, not recast as completed negative searches. Manual
exact-name and institutional web review continued for all 22 people.

The principal findings preserve identity and chronology limits:

- **Hans Meyerhoff** appears in two adjacent Box 521 rows, one lieutenant and
  one master sergeant, with different protected identifiers. They remain two
  entities. The master-sergeant row has an exact official Army crosswalk and
  independent UCLA evidence. His immediate pre-OSS affiliation is the Army of
  the United States; UCLA teaching-assistant work is separately recorded as
  his last named civilian employment, while UCLA student status remains a
  distinct relationship. An unnamed 1942-1943 federal-government affiliation
  is qualified rather than assigned to an invented agency.
- **Emile Meyran** is linked with high identity confidence to French official
  Service historique de la Défense files. Archive-cited secondary research
  documents engineering work for Compagnie Française de Raffinage from 1935
  until his April 1943 departure from Paris and subsequent recruitment into
  the OSS-affiliated NANA network. This is published as a qualified
  medium-confidence immediate and last-civilian-employer claim pending review
  of the underlying personnel files. Earlier Compagnie des Eaux de Paris work
  and his 1939-1940 French Army assignment are modeled separately. The
  secondary narrative's 1 April 1910 birth date conflicts with the official
  file's 1 August 1910 date and is disclosed rather than silently resolved.
- **Norman H. Meyers** and `Norman M. Myers` share a protected identifier but
  differ in middle initial, rank, page, and box. Both rows remain separate.
- **C. P. Meysereav**, `Charles P. Mersereau`, and `Charles P. Meserau` share a
  protected identifier across three differently spelled rows. The official
  Army spelling favors Mersereau, but no merge or correction is authorized.
- Six additional official Army crosswalks were accepted as identity evidence
  only. Army occupation codes were not converted into employer claims.
- No reliable predecessor employer was found online for the other people.
  Their profiles identify the indexed file and the archival question that
  remains open.

The cohort ends with **17** `requires_archival_review`, three
`conflicting_sources`, one `verified_employer_found`, and one
`documented_prewar_employer_found` statuses. Identity statuses are seven
`high_confidence`, three `conflicting`, and 12 `unresolved`. The reviewed
bundle adds **18 claims**: ten high, five medium, and three conflicting; it
also adds seven affiliations, all kept in their correct relationship category.

Rebuilt coverage is **23,978/23,978** linked source rows and **23,939** active
person entities. Research-attempt coverage is **8,162/23,939 (34.0950%)**;
confirmed/high verified-employer coverage is **291/23,939 (1.2156%)**;
confirmed/high verified-affiliation coverage is **646/23,939 (2.6985%)**;
archival-review disposition coverage is **6,618/23,939 (27.6453%)**. There are
**15,772** `not_started` people, **497** possible-duplicate groups, and **195**
active conflicts. SQLite stores **14,166** attempts or plans and **5,178**
claims: 1,312 confirmed, 2,092 high, 1,415 medium, 189 low, and 170
conflicting. It contains **5,169** citation records and **2,465** unique source
documents. The public projection contains **2,275** affiliations, **747**
organizations, **3,959** sources, and **4,985** claims.

The oil-company category remains prominent at the top of the personnel
directory and on its dedicated page. Emile Meyran's qualified claim expands
the evidence-scoped category to **eight people across ten historically named
companies**. Full-index historical research is unfinished.

## Replay and continuation

After importing prior durable batches into private SQLite:

```sh
python3 -m oss_research import-review-decisions research/identity_review_decisions_2026-09-23_batch655.csv
python3 -m oss_research import-reviewed-evidence research/evidence-pages318-319-meyer-meysereav-review_batch-655_2026-09-23.json
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
```

Continue with the next bounded research batch, then run:

```sh
python3 -m oss_research export-adapter-checkpoints
python3 -m oss_research export-derived
python3 -m oss_research export-review-queue
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
```

No API key, full service number, raw Catalog API response, copyrighted page
image, or private reviewer note is committed or included in the public site.
