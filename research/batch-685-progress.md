# Batch 685: Moyer-Mueller research

Batch 685 covers PDF page 333, rows 1-23, from `Ira F Moyer` through
`Erna L Mueller`. Visual inspection and layout-text comparison confirmed all
23 printed rows. Every source row remains linked to its own person entity and
the original index spelling remains recoverable.

An authoritative CIA history identifies **Robert Edison Moyers** as an Army
Dentist assigned to Cairo when General Donovan recruited him for the OSS. The
Army Dental Corps posting is therefore published as his immediate pre-OSS
military assignment. A scholarly dental-history article independently
documents his December 1942 completion of dental school at the University of
Iowa. Iowa is modeled as earlier student status, not as an employer.

An official Army history identifies **Daniel Mudrinich** and supplies a dated
sequence from Officer Candidate School to the Infantry Replacement Training
Center at Camp Roberts, followed four months later by OSS recruitment. Camp
Roberts is published as his immediate pre-OSS military assignment. No civilian
employer is inferred from that chronology.

The exact full name, compatible wartime context, and an institutional profile
support a high-confidence identity for **John Francis Moynahan**. His 1933
Boston College graduation is published as visibly qualified, earlier student
status. The accessible sources do not establish that Boston College or the
Army Air Forces immediately preceded OSS service, so neither is presented as
an immediate affiliation or civilian employer.

Official Army bulk data supports six additional high-confidence identities:
**Carl J. Moyes, Frank F. Mucciolo, Gordon M. Muchow, Nick Mudrick, Arnold W.
Mueller, and Charles K. Mueller**. Each combines an exact name with a nonshared
protected identifier. The decisions establish identity only; coded Army
occupations are not translated into employer claims.

Two identifier conflicts remain explicit. The indexed **Ira F. Moyer** row
shares a protected identifier with an official Army record for **Edward M.
Malachowski**, an unrelated name. The index prints **Rudolph Mudrick**, while
the matching Army record prints **Rudolph Murdirk**. Neither Army record is
silently transferred to the indexed person, and both Box 543-544 jackets are
flagged for archival review. Full identifiers remain private.

The other twelve identities remain unresolved after staged official, exact-name
OSS, employment, institutional, newspaper, obituary, directory, and archival
searches. Plausible common-name and spelling-variant candidates were rejected
when no second identifier connected them to the index. A negative online result
is not represented as proof that prior employment did not exist.

Nineteen people reached `no_reliable_result_after_protocol`, two retain
`conflicting_sources`, and two are `completed`. The evidence bundle imports six
sources, four organizations, four affiliations, 15 claims, 27 claim-source
links, 23 person updates, and 23 consolidated research attempts. Eight reviewed
Army candidate decisions are preserved separately: six accepted identity
matches and two conflict decisions.

Rebuilt coverage is **23,978/23,978** linked source rows and **23,939** active
person entities. Research-attempt coverage is **8,804/23,939 (36.7768%)**;
confirmed/high verified-employer coverage is **308/23,939 (1.2866%)**;
confirmed/high verified-affiliation coverage is **685/23,939 (2.8614%)**;
archival-review disposition coverage is **7,261/23,939 (30.3313%)**. There are
**15,130** `not_started` people, **514** possible-duplicate groups, and **246**
active conflicts. SQLite stores **15,939** attempts or plans and **5,572**
claims: 1,336 confirmed, 2,366 high, 1,455 medium, 196 low, and 219 conflicting.
It contains **5,386** citation records and **2,638** unique source documents.
The public projection contains **2,356** affiliations, **788** organizations,
**4,169** sources, and **5,369** claims. The featured oil-company category
remains **nine people across 11 historically named companies**. Full-index
historical research remains unfinished.

## Replay and continuation

After importing prior durable batches into private SQLite:

```sh
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
python3 -m oss_research import-review-decisions research/identity_review_decisions_2026-09-25_batch685.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page333-moyer-mueller-review_batch-685_2026-09-25.json
python3 -m oss_research export-adapter-checkpoints
python3 -m oss_research export-derived
python3 -m oss_research export-review-queue
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
```

Adapter checkpoints must be imported before final reviewed decisions and
evidence so temporary discovery states cannot supersede reviewed dispositions.

No API key, full service number, raw Catalog API response, copyrighted page
image, unrelated Army coded occupation, or private reviewer note is committed
or included in the public site.
