# Batch 680: Morrill-Morrison research

Batch 680 completes PDF page 330, rows 24-46, from `Charlotte Morrill`
through `Robert S Morrison`. Visual inspection and layout-text comparison
confirmed all 23 printed rows, including the separate adjacent `H. G Morrison
Jr.` and `Hubert G Morrison` records, their different ranks, and their
different protected identifiers. Every record remains linked to its own person
entity.

Eight official Army bulk candidates support high-confidence identities for
**John E Morris, John F Morris, John P Morris, Thomas E Morris, Donald J
Morrisey, Edward S Morrison, Hugh P Morrison, and Robert S Morrison**. Exact
indexed names and nonshared protected identifiers agree across official
records. The Army file's coded occupations are not named employers and remain
private.

The Army match for **Hubert G Morrison** is not accepted as a simple identity
match. His protected identifier points to an Army record naming H G Morrison
Junior, while the immediately preceding OSS index row is a separate H. G
Morrison Jr. with another rank and protected identifier. Both people remain
separate in possible-duplicate group `p330-hg-hubert-morrison-b680`. Hubert is
`conflicting`; H. G. is `ambiguous`; both require comparison of their Box 539
personnel files.

The substantive employment finding concerns **Phoebe Morrison**. A 1939
*Evening Star* page identifies her as an assistant professor in Yale
University School of Law. The 1941 title page of *Legal Problems in the Far
Eastern Conflict* identifies her as Research Associate in International Law,
Yale University. An official Federal Trade Commission oral history separately
places Phoebe Morrison in OSS Research and Analysis, calls her an international
lawyer, and says she came from Yale; a Hoover Institution item-level record
preserves her April 1945 OSS memo. These independent sources support a
high-confidence identity and high-confidence, published `documented_prewar`
Yale Law School employment affiliation.

Yale is not marked as Phoebe Morrison's immediate pre-OSS affiliation or last
civilian employer. The accessible sources do not establish her exact
recruitment chronology, and a discovery-only claim of intervening OPA work was
not published. Her Box 539 file remains the next step for Question A and
Question B.

The Library of Congress adapter produced 52 source candidates. One—the Phoebe
Morrison Yale notice—was accepted. The other 51 were rejected after page-level
review as namesakes, OCR collisions, chronologically irrelevant results, or
records lacking an OSS or protected-identifier bridge. Together with nine Army
identity candidates, the review ledger contains 61 unique decisions: nine
accepted, one conflicting, and 51 rejected. No result was accepted from a
search snippet alone.

Twenty people reached `no_reliable_result_after_protocol`; one has
`documented_prewar_employer_found`; one retains `conflicting_sources`; and one
has `requires_archival_review`. The staged protocol covered the official NARA
index, official Army bulk data where applicable, exact-name OSS and employment
searches, CIA-domain searches, Library of Congress discovery, institutional
publications, newspapers, obituaries, directories, and archival finding aids.
The direct CIA adapter failed closed and was not treated as negative evidence.

The evidence bundle imports six sources, one canonical Yale Law School
organization, one affiliation, 11 claims, 24 claim-source links, 23 person
updates, and 23 consolidated research attempts. The featured oil-company
category remains evidence-scoped to **eight people across ten historically
named companies**; no Batch 680 person was added without a qualifying cited
work relationship.

Rebuilt coverage is **23,978/23,978** linked source rows and **23,939** active
person entities. Research-attempt coverage is **8,692/23,939 (36.3090%)**;
confirmed/high verified-employer coverage is **306/23,939 (1.2782%)**;
confirmed/high verified-affiliation coverage is **675/23,939 (2.8197%)**;
archival-review disposition coverage is **7,148/23,939 (29.8592%)**. There are
**15,242** `not_started` people, **514** possible-duplicate groups, and **232**
active conflicts. SQLite stores **15,730** attempts or plans and **5,495**
claims: 1,326 confirmed, 2,318 high, 1,450 medium, 196 low, and 205 conflicting.
It contains **5,344** citation records and **2,607** unique source documents.
The public projection contains **2,334** affiliations, **775** organizations,
**4,127** sources, and **5,292** claims. Full-index historical research remains
unfinished.

## Replay and continuation

After importing prior durable batches into private SQLite:

```sh
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
python3 -m oss_research import-review-decisions research/identity_review_decisions_2026-09-25_batch680.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page330-morrill-morrison-review_batch-680_2026-09-25.json
python3 -m oss_research export-adapter-checkpoints
python3 -m oss_research export-derived
python3 -m oss_research export-review-queue
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
```

Adapter checkpoints must be imported before the final reviewed decisions and
evidence so temporary discovery states cannot supersede reviewed dispositions.

No API key, full service number, raw Catalog API response, copyrighted page
image, unrelated Army coded occupation, or private reviewer note is committed
or included in the public site.
