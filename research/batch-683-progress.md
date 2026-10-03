# Batch 683: Mosler-Moulder research

Batch 683 covers PDF page 332, rows 1-23, from `Rudolf L Mosler` through
`Helen L Moulder`. Visual inspection and layout-text comparison confirmed all
23 printed rows, including George L Mott's truncated printed note `docume`.
Every source row remains linked to its own person entity. Samuel Mossious
already had 16 recorded attempts; this batch adds one consolidated attempt
rather than replacing or duplicating that history.

One person receives a newly publishable immediate affiliation. A contemporary
*Chess Review* obituary says **Geoffrey A. Mott-Smith's** tenure as problem
editor of *The Chess Correspondent* ended when wartime Washington summoned him
as the OSS chief instructor in cryptography and cryptanalysis. An American
Contract Bridge League bulletin independently identifies him as a 1935-1936
editor of the ACBL Bridge Bulletin and as an OSS chief instructor. The rare
name, occupation, and specific OSS role support a high-confidence identity.
The Chess Correspondent is published as an explicit immediate professional
affiliation, while the ACBL Bulletin and *Games Digest* are separate earlier
prewar affiliations. These editorial relationships are not labeled paid
employment, and no last civilian employer is invented.

Two independent specialist rosters support a high-confidence identity for
**Rudolf L. Mosler**: the Artillery Officer Candidate School list places him
in class 35-42 and the Camp Ritchie roster independently repeats the name.
Those sources establish a military-training identity but do not establish the
sequence immediately before OSS service or a civilian employer, so his
predecessor affiliation remains unresolved.

Official Army data supports high-confidence identities for **George H. Moss
Jr., Frank P. Motisi, and George L. Mott** through exact indexed names and
nonshared protected identifiers. The added suffix for Moss is retained as a
documented variant. Full identifiers and coded Army occupations remain private
and are not promoted into employer claims.

Three identity conflicts remain deliberately unresolved. The index prints
**Arnando Mostachetti**, while the official Army source prints Armando under
the same protected identifier. It prints **Ervin E. Mott**, while the Army
source prints Ervin S. under the same identifier. The Army spelling **Lars
Motland** agrees with this page, but the identifier is also printed for the
separate Laro Montland row on page 326. All affected entities remain separate,
the disagreements are public, and the cases require personnel-jacket review.

A well-known artist named **May Mott-Smith** was considered and explicitly
rejected as a name-only candidate because no source bridges her to the indexed
P-2 personnel row or to OSS service. Postwar military and business-directory
records found for **Mario Motola** were also rejected as evidence of his
pre-OSS affiliation. These leads remain review notes rather than biographical
claims.

Nineteen people reached `no_reliable_result_after_protocol`; three retain
`conflicting_sources`; and Geoffrey Mott-Smith is `completed`. The staged
protocol covered the official index and Army bulk source, exact-name OSS and
employment searches, CIA-domain searches, Library of Congress and newspaper
attempts, institutional sources, obituaries, directories, and archival
finding aids. A negative online result is never represented as proof that
earlier employment did not exist.

The evidence bundle imports six sources, three organizations, three
affiliations, 11 claims, 21 claim-source links, 23 person updates, and 23
consolidated research attempts. Seven reviewed Army candidate decisions are
preserved separately: three accepted matches and four conflict decisions. The
featured oil-company category remains evidence-scoped to **eight people across
ten historically named companies**; no Batch 683 person was added without a
qualifying cited work relationship.

Rebuilt coverage is **23,978/23,978** linked source rows and **23,939** active
person entities. Research-attempt coverage is **8,758/23,939 (36.5847%)**;
confirmed/high verified-employer coverage is **307/23,939 (1.2824%)**;
confirmed/high verified-affiliation coverage is **681/23,939 (2.8447%)**;
archival-review disposition coverage is **7,215/23,939 (30.1391%)**. There are
**15,176** `not_started` people, **514** possible-duplicate groups, and **239**
active conflicts. SQLite stores **15,799** attempts or plans and **5,540**
claims: 1,329 confirmed, 2,351 high, 1,452 medium, 196 low, and 212
conflicting. It contains **5,367** citation records and **2,623** unique source
documents. The public projection contains **2,347** affiliations, **779**
organizations, **4,150** sources, and **5,337** claims. Full-index historical
research remains unfinished.

## Replay and continuation

After importing prior durable batches into private SQLite:

```sh
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
python3 -m oss_research import-review-decisions research/identity_review_decisions_2026-09-25_batch683.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page332-mosler-moulder-review_batch-683_2026-09-25.json
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
