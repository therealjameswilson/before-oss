# Batch 684: Moulton-Moye research

Batch 684 covers PDF page 332, rows 24-46, from `Albert Moulton` through
`Leon L Moye`. Visual inspection and layout-text comparison confirmed all 23
printed rows. Every source row remains linked to its own person entity and the
original spelling remains recoverable.

Official NARA and Marine Corps sources support a high-confidence identity for
**John A. Mowinckel** and document his earlier work as head of European
operations for the Standard Oil Company of New Jersey. That role is published
as documented prewar employment, not as an immediate predecessor to OSS,
because the available sources do not establish the transition date. It adds
Mowinckel to the featured oil-company category, which now contains **nine
people across 11 historically named companies**.

The adjacent **John W. Mowinckel** row remains a separate, confirmed entity.
An official Marine Corps history supplies the full name John Wallendahl
Mowinckel, Princeton modern-languages study, Marine Corps Reserve service,
October 1943 commission, and subsequent OSS detail. His immediate predecessor
is therefore modeled as the Marine Corps Reserve. Princeton is student status,
not employment, and his father's Standard Oil work is not transferred to him.

A 1945 NARA-released OSS award roster prints **Andre G. Mourquet** with an
identifier one digit different from the index's **Andre G Mourqet** row. The
records agree on given name, middle initial, enlisted grade, and most
identifier digits. Both spellings and the digit disagreement remain visible,
the identity stays `conflicting`, and no full identifier is published.

Official Army bulk data produces two further surname conflicts under matching
protected identifiers: Andrew S. Mousilinas/Mousalimas and Frederick O.
Moussean/Mousseau. Frank Mowinski's indexed identifier instead points to the
unrelated Army name Clyde E. White, a severe unresolved conflict. A digitized
U.S. government document agrees with Arno Mowitz Jr.'s surname, suffix, rank,
and protected officer identifier but prints middle initial P rather than D.
All variants remain public and require personnel-jacket review.

Exact names and nonshared protected identifiers support high-confidence Army
identities for **Chin M. Mow** and **James T. Moy**, but no employer is inferred
from the Army source. Two official French archival inventories support a
high-confidence identity for **Thérèse Joséphine Mouzon**, also indexed as
Thérèse André; a secondary network history supplies OSS context. No reliable
pre-OSS employer was found.

The uncommon exact name, WAE context, Library of Congress chronology, and NARA
documentation of 1940 collaboration with William Donovan support a
high-confidence identity for journalist **Edgar A. Mowrer**. The accessible
sources do not establish an OSS accession date, so no immediate predecessor is
published.

A detailed San Francisco Chronicle family obituary supports a high-confidence
identity for **Clarence Moy** through exact name, compatible Army rank
progression, language training, and explicit OSS China translation-unit
service. It supports qualified medium-confidence claims for the U.S. Army as
his immediate predecessor and for the Territory of Hawaii Department of
Institutions, where he worked as a social worker, as his last civilian
employer. Both claims remain qualified pending the Box 543 jacket and
territorial personnel records.

Potential famous-person and exact-name leads were rejected when they lacked a
second identity bridge. These include sound director Thomas T. Moulton, veteran
Chris G. Moustakis, French prisoner Gaston Mousis, and a 1935 yearbook entry
placing a Leon L. Moye at Atlanta Gas Light Company. None is promoted into a
public employment fact.

Fifteen people reached `no_reliable_result_after_protocol`; five retain
`conflicting_sources`; two have `documented_prewar_employer_found`; and John W.
Mowinckel is `completed`. The staged protocol covered the official index and
Army bulk source, exact-name OSS and employment searches, CIA-domain searches,
Library of Congress and newspaper attempts, institutional sources, obituaries,
directories, and archival finding aids. Current CIA robots restrictions and a
bounded Library of Congress adapter timeout are recorded as access limitations,
not as negative evidence.

The evidence bundle imports 13 sources, five organizations, five affiliations,
17 claims, 35 claim-source links, 23 person updates, and 23 consolidated
research attempts. Five reviewed Army candidate decisions are preserved
separately: two accepted matches and three conflict decisions.

Rebuilt coverage is **23,978/23,978** linked source rows and **23,939** active
person entities. Research-attempt coverage is **8,781/23,939 (36.6807%)**;
confirmed/high verified-employer coverage is **308/23,939 (1.2866%)**;
confirmed/high verified-affiliation coverage is **683/23,939 (2.8531%)**;
archival-review disposition coverage is **7,238/23,939 (30.2352%)**. There are
**15,153** `not_started` people, **514** possible-duplicate groups, and **244**
active conflicts. SQLite stores **15,916** attempts or plans and **5,557**
claims: 1,332 confirmed, 2,358 high, 1,454 medium, 196 low, and 217 conflicting.
It contains **5,380** citation records and **2,633** unique source documents.
The public projection contains **2,352** affiliations, **784** organizations,
**4,163** sources, and **5,354** claims. Full-index historical research remains
unfinished.

## Replay and continuation

After importing prior durable batches into private SQLite:

```sh
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
python3 -m oss_research import-review-decisions research/identity_review_decisions_2026-09-25_batch684.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page332-moulton-moye-review_batch-684_2026-09-25.json
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
