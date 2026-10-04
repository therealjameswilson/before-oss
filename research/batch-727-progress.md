# Batch 727: Owens-Packer research

Batch 727 covers PDF page 354, rows 1-23, from **Emily L Owens** through
**Don S Packer**. A 300-dpi visual inspection confirmed all 23 printed rows,
representing 23 active person entities. Embedded text was checked against the
render. Original spelling and uncertainty remain recoverable, including the
`also AS` notes for Richard C Owens and Axel H Oxholm and the incomplete `* P`
and `* Pacchiotti` rows with `no first n` notes. Rows 1-12 are in Box 579 and
rows 13-23 are in Box 580; all use location 230/86/38/01. Protected identifiers
remain only in the private database.

Six Army bulk candidates are accepted for identity review. **Owen J Owens**,
**Richard C Owens**, **Ned K Owyang**, **Durant L Pace**, **Joseph A Pacheco**,
and **Henry S Pachowicz** have an exact or documented-variant name and
protected-identifier match. The Army row supplies suffix Jr for Richard C
Owens. No coded Army occupation is converted into an occupation or employer.

Three official-record conflicts remain explicit. Henry S Pachowicz has one
exact-name Army bulk row and an adjacent row under the same private identifier
that names Lewis Randall A. **Andre R Pacatte** and a later **Andre R Pagatte**
index row share one private identifier. **George J Packard Jr** and **Mary A
Hawkins** likewise share one. These records remain separate, the full numbers
are not published, and no mismatched metadata is transferred.

**Axel H Oxholm** receives a qualified last-civilian-employer claim. A June
1942 *American Builder* article identifies him as managing director of Pacific
Forest Industries at its Port of Tacoma operation. The index lists him as a
lieutenant colonel, and the National Gallery of Art's 1946 annual report
independently calls him Colonel Axel H. Oxholm. The site therefore publishes
Pacific Forest Industries as the last civilian employer currently identified
before documented wartime officer service, at medium confidence. It does not
claim an immediate OSS transition or invent a military accession date.

**Ned K Owyang** is linked at high confidence to the fuller **Ned Ke-Hung
Owyang** form. The exact indexed and Army names agree with a nonshared private
identifier, while an April 1944 directory records Tri-State College in 1942
and indexes him under radio engineering. The site models this as documented
prewar student status, not as employment, a degree, or an immediate OSS
predecessor. The directory's YMCA line is an address and is not repurposed as
an employer. A later RCA result is postwar and excluded.

**André Pacatte** receives a medium-confidence documented-prewar Berlitz
affiliation. TIME reported that Pacatte ran the Washington school before and
after the war; a later historical article describes him as a French teacher at
the Cleveland school. The shared Berlitz affiliation is published, while the
branch, role, and exact transition date remain qualified. The separate
Pacatte/Pagatte index collision remains visible and requires review of both
Box 580 files.

A Maryland legislator and Army-officer biography remains only a lead for
**George W Owings** because the common name lacks two corroborating identifiers
linking it to this OSS row. Margit Oxholm does not inherit a possible
relative's identity or employment. Modern company results, people-finder
pages, unbridged obituaries, and other namesake material are excluded.

The CIA and Library of Congress adapters failed closed in bounded attempts,
and the web adapter recorded deterministic query plans before the manual
staged review. No authenticated NARA Catalog request was made because the
local project did not expose a key to this run.

The cohort ends with 18 `requires_archival_review`, two
`documented_prewar_employer_found`, two `conflicting_sources`, and one
`occupation_only_found` outcome. Identity statuses are 14 `unresolved`, seven
`high_confidence`, and two `conflicting`. The reviewed bundle imports seven
sources, three organizations, three affiliations, 13 claims, 29 claim-source
links, 23 person updates, and 23 consolidated research attempts. Six accepted
and three conflicting identity-review decisions are recorded.

Rebuilt coverage is **23,978/23,978** linked source rows and **23,939** active
person entities. Research-attempt coverage is **9,758/23,939 (40.7619%)**;
confirmed/high verified-employer coverage is **330/23,939 (1.3785%)**;
confirmed/high verified-affiliation coverage is **738/23,939 (3.0828%)**;
archival-review disposition coverage is **8,216/23,939 (34.3206%)**. There
are **14,176** `not_started` people, **523** possible-duplicate groups, and
**319** active conflicts. SQLite stores **17,792** attempts or plans and
**6,260** claims: 1,370 confirmed, 2,887 high, 1,524 medium, 198 low, 279
conflicting, and two unresolved. It contains **5,661** citation records and
**2,857** unique source documents. The public projection contains **2,471**
affiliations, **858** organizations, **4,442** sources, and **6,053** claims.
The oil-company directory remains nine cited people across eleven historically
named companies. Full-index historical research remains unfinished.

## Replay and continuation

After importing prior durable batches into private SQLite:

```sh
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
python3 -m oss_research assign-page-batch --batch-name batch-727 --page 354 --first-row 1 --last-row 23
python3 -m oss_research research --source cia --batch batch-727 --max-queries 23
python3 -m oss_research research --source loc --batch batch-727 --max-queries 23
python3 -m oss_research research --source web --batch batch-727 --resume --max-queries 23 --dry-run
python3 -m oss_research import-review-decisions research/identity_review_decisions_2026-10-04_batch727.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page354-owens-packer-review_batch-727_2026-10-04.json
python3 -m oss_research export-adapter-checkpoints
python3 -m oss_research export-derived
python3 -m oss_research export-review-queue
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
```

Adapter checkpoints must be imported before final reviewed decisions and
evidence so temporary discovery states cannot supersede reviewed dispositions.
The next research boundary is PDF page 354, rows 24-46, from Charles H Padden
through Wellman Page.

No API key, full service or officer number, raw Catalog or LoC API response,
copyrighted page image, street address, living-relative detail, modern
people-finder record, or private reviewer note is committed or included in the
public site. No authenticated NARA Catalog API request was made for this batch.
