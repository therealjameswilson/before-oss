# Batch 650: pages 55-64 extraction audit and Mendelow-Merante research

All **460** printed rows on original NARA PDF pages 55-64 were compared with
the immutable extraction at 180 dpi. Page 60 was already in the deterministic
visual sample; the other nine pages and **414** rows received their first
complete visual comparison in this batch. Every row matches. Complete-page
visual review now covers **484/522 pages** and **22,230/23,978 rows**:
**22,198** reviewed rows match the extraction, **32** retain reviewed
corrections, and **1,748** remain unaudited. Every PDF page remains represented,
every parser warning is resolved, and SQLite integrity and foreign-key checks
pass.

The page-316 `Sylvia Mendelow` through `Dominic Merante` queue contains **22
source rows and 22 cautious person entities**. Each person received four saved
source-specific query plans and one saved manual review outcome. Four source
families were staged: NARA, CIA Reading Room, Library of Congress, and targeted
web research. The NARA, CIA, and web calls were dry-run plans; the LoC adapter
ran live in one bounded 22-person sequence. Both LoC newspaper candidates were
rejected after review because their middle initials differed and no OSS or
protected-identifier bridge existed. No authenticated NARA Catalog request was
made and no API key was stored or logged.

The principal findings preserve affiliation type and chronology:

- **Joseph A. Mendenhall** is a high-confidence identity based on his exact
  uncommon name, compatible Lieutenant rank, and direct Library of Congress
  oral history. His Harvard Law School relationship is recorded as student
  status, not employment. His earlier Signal Aircraft Warning Service is kept
  separate from his immediate military pathway: Army Air Forces intelligence
  at Yuma, an OSS recruiter interview, brief intervening orders, and an OSS
  summons.
- **Arthur Menken** is a high-confidence identity from his exact uncommon name,
  contemporary war-cameraman record, and a Library of Congress file indexed
  `Arthur Menken, Major`. Paramount News, United Fruit Company, Columbia
  Broadcasting System, and United Press are documented prewar employers. None
  is promoted to immediate or last-civilian status because the accessible
  sources do not date his OSS transition.
- Indexed **Horst Mendershause** remains a probable match to economist Horst
  Mendershausen. Bennington College teaching is published at medium confidence
  with the spelling difference and Box 517 review need visible.
- Indexed **Seldon C. Menefee** remains a probable spelling variant of Selden C.
  Menefee. The Work Projects Administration Research Division is modeled as a
  professional affiliation based on federal research publications, not as
  unqualified payroll employment.
- Indexed **Sir Stewart Menzles** is a high-confidence spelling bridge to Sir
  Stewart Menzies. His November 1939 appointment as chief of the British Secret
  Intelligence Service is an Allied government assignment, not evidence that
  he entered OSS. The person is separately classified as foreign or Allied
  military personnel.
- A republished obituary is only a low-confidence identity and chronology lead
  for **Helen Mensing**. The Air Transport Command affiliation is withheld from
  public facts pending the original obituary or the Box 518 personnel file.

Official Army evidence supplies high-confidence identity bridges for Danny A.
Menna, Donald G. Menn, and Joseph Meo. Amandus I./L. Mendini and
Dominic/Dominick Merante remain probable spelling or initial variants. Joseph
V. Menengas/Menanga, Natelene Mengello/Mongello, and Harry C.
Menutile/Minutillo remain conflicting because protected identifiers connect
different indexed spellings. The records are not merged, and full protected
identifiers remain private.

The cohort ends with **12** `in_progress`, six `needs_identity_review`, three
`conflicting_sources`, and one `documented_prewar_employer_found` status.
Identity statuses are six `high_confidence`, eight `unresolved`, five
`probable`, and three `conflicting`. The evidence bundle adds **25** claims: 14
high, six medium, two low, and three conflicting. The two low claims remain
outside the public projection.

Rebuilt coverage is **23,978/23,978** linked source rows and **23,939** active
person entities. Research-attempt coverage is **8,054/23,939 (33.6438%)**;
confirmed/high verified-employer coverage is **286/23,939 (1.1947%)**;
confirmed/high verified-affiliation coverage is **640/23,939 (2.6735%)**;
archival-review disposition coverage is **6,512/23,939 (27.2025%)**. There are
**15,880** `not_started` people, **492** possible-duplicate groups, and **183**
active conflicts. SQLite stores **13,674** attempts or plans and **5,105**
claims: 1,311 confirmed, 2,047 high, 1,400 medium, 189 low, and 158 conflicting.
It contains **5,132** citation records and **2,435** unique source documents.
The public projection contains **2,253** affiliations, **730** organizations,
**3,922** sources, and **4,912** claims.

The oil-company category remains an evidence-scoped set of **seven people
across nine historically named companies**. Arthur Menken is not included:
United Fruit Company was an agricultural and shipping company, not an oil
employer. Full-index historical research is unfinished.

## Replay and continuation

After importing prior durable batches into private SQLite:

```sh
python3 -m oss_research import-page-reviews research/parser_visual_review_pages55-64_2026-09-23.json
python3 -m oss_research import-review-decisions research/identity_review_decisions_2026-09-23_batch650.csv
python3 -m oss_research import-review-decisions research/loc_review_decisions_2026-09-23_batch650.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page316-mendelow-merante-review_batch-650_2026-09-23.json
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
```

Continue with the next bounded research and extraction-audit batch, then run:

```sh
python3 -m oss_research export-adapter-checkpoints
python3 -m oss_research export-derived
python3 -m oss_research build-public-data
python3 -m oss_research coverage-report
```

No API key, full service number, raw Catalog API response, copyrighted page
image, or private reviewer note is committed or included in the public site.
