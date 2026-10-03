# Batch 679: Moriarity-Morrell research

Batch 679 completes PDF page 330, rows 1-23, from `William J Moriarity`
through `Doris J Morrell`. Visual inspection and layout-text comparison
confirmed all 23 printed rows, including the exact indexed spelling
`Mauriyio Moris`, the two adjacent Mario Morpurgo rows with different ranks
and protected identifiers, and the separate Brunnon E Mormand row whose
identifier also appears on the later Brunnon C Normand row.

Three official Army bulk candidates support high-confidence identities for
**Richard P Moriarty, Alfred J Morin, and Leo J Morin**. Exact indexed names
and nonshared protected identifiers agree across official records. The Army
file's coded occupations are not treated as named-employer evidence and remain
private.

The strongest employment finding concerns **Charles Morley**. An American
Historical Association obituary places his teaching at the University of
North Dakota, the University of Nebraska, and the University of Wisconsin in
the chronology before his 1943-44 OSS research-analyst service. An Ohio State
institutional obituary independently confirms one year with OSS before his
1944 Ohio State appointment. The three teaching affiliations are published as
qualified, medium-confidence `documented_prewar` employment; none is marked as
the immediate affiliation or last civilian employer because the sources do
not establish which appointment came last.

A 1942 Johns Hopkins University circular names **Panos Morphopoulos** as an
instructor in Romance Languages and preserves 1937 as the appointment-year
notation. A family history corroborates the rare-name OSS identity and the
Morphos variant but is not used as employer evidence. The university
affiliation is therefore a probable, qualified, temporally uncertain finding,
not an immediate or last-civilian claim.

The Military Intelligence Service Language School registry lists **Miki
Moriwaki** as civilian faculty. Because the compiled registry does not provide
individual appointment dates or a unique identifier, the match remains
probable and the relationship is modeled as a government assignment with
uncertain sequence, not as a civilian employer.

Official War Relocation Authority and National Park Service records provide a
probable identity lead for **George Y Morishita**, but no direct personnel-file
link or pre-OSS employer. **Herve F Morisseau** remains conflicting because
the protected identifier leads to an Army record for Joseph H F Morisseau,
while Rhode Island and Bryant records support Herve F Morisseau. **Brunnon E
Mormand** remains conflicting with the later Brunnon C Normand index row; the
two people and source rows are not merged.

The two Mario Morpurgo entries remain separate ambiguous entities in one
possible-duplicate group. Their different ranks, protected identifiers, and
archive locations prohibit an automatic merge. A discovery-only National
Archives (UK) lead does not establish identity or employment. Twelve people
reached `no_reliable_result_after_protocol`, seven require archival review,
two retain `conflicting_sources`, one has `occupation_only_found`, and Charles
Morley has `documented_prewar_employer_found`. Every one of the 23 people now
has a terminal batch outcome.

The staged protocol covered the official NARA index, official Army bulk data
where applicable, exact-name OSS and employment searches, CIA-domain searches,
Library of Congress discovery, institutional publications, newspapers,
obituaries, rosters, and archival finding aids. The direct CIA adapter failed
closed once and was not treated as negative evidence. Two unrelated Library
of Congress candidates were rejected. The seven review decisions comprise
three accepted Army identities, two preserved conflicts, and two rejected
namesakes.

The evidence bundle imports 11 sources, five organizations, five affiliations,
16 claims, 29 claim-source links, 23 person updates, and 23 consolidated
research attempts. The featured oil-company category remains evidence-scoped
to **eight people across ten historically named companies**; no Batch 679
person was added without a qualifying cited work relationship.

Rebuilt coverage is **23,978/23,978** linked source rows and **23,939** active
person entities. Research-attempt coverage is **8,669/23,939 (36.2129%)**;
confirmed/high verified-employer coverage is **305/23,939 (1.2741%)**;
confirmed/high verified-affiliation coverage is **674/23,939 (2.8155%)**;
archival-review disposition coverage is **7,125/23,939 (29.7631%)**. There
are **15,265** `not_started` people, **513** possible-duplicate groups, and
**231** active conflicts. SQLite stores **15,682** attempts or plans and
**5,484** claims: 1,326 confirmed, 2,308 high, 1,450 medium, 196 low, and 204
conflicting. It contains **5,338** citation records and **2,602** unique source
documents. The public projection contains **2,333** affiliations, **775**
organizations, **4,121** sources, and **5,281** claims. Full-index historical
research remains unfinished.

## Replay and continuation

After importing prior durable batches into private SQLite:

```sh
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
python3 -m oss_research import-review-decisions research/identity_review_decisions_2026-09-25_batch679.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page330-moriarity-morrell-review_batch-679_2026-09-25.json
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
