# Batch 682: Mory-Mosler research

Batch 682 completes PDF page 331, rows 24-46, from `Chalen Mory` through
`Rosa Mosler`. Visual inspection and layout-text comparison confirmed all 23
printed rows. Every record remains linked to its own person entity. Philip E
Mosely already had a completed, verified research outcome, so this batch
preserves that outcome and adds 22 new consolidated attempts rather than
duplicating his research record.

Four official Army bulk candidates support high-confidence identities for
**George Moschinsky, Robert K Mosher, Jerome J Moskol, and Theodore Moskowitz**.
Exact indexed names and nonshared protected identifiers agree across the
records; the official Army middle initial `J` is retained as a documented
variant for Jerome Moskol. Army coded occupations remain private discovery
clues and are not treated as named-employer evidence.

Three people receive newly publishable pathway findings. A 1941 federal
bulletin identifies **Jacob L. Mosak** as a University of Chicago economics
instructor on leave for the Office of Price Administration, and the university
obituary corroborates the identity and federal wartime chronology. The
University of Chicago is published as his strongly date-bounded last civilian
employer. OPA is separately modeled as an earlier documented government
assignment, not conflated with either civilian employment or an explicit
immediate pre-OSS affiliation.

New York's official Adjutant General report places **Amos D. Moscrip Jr.** in
the 101st Anti-Tank Battalion before its January 1941 federal induction. An
official CIA historical study later identifies Lieutenant Colonel Moscrip as
an SSU theater commander. The uncommon name and rank progression support a
high-confidence identity. The United States Army is published as the strongly
date-bounded immediate military pathway and the 101st as an earlier military
assignment. No civilian employer is inferred.

The State Bar of California dates **Edward A. Mosk's** admission to December
1940. An institutional legal-history article says that he returned to legal
practice after OSS service in Italy and Yugoslavia, and a scholarly OSS roster
corroborates his wartime role. His pre-OSS private legal practice is therefore
published at medium confidence as self-employment and a strongly date-bounded
last civilian occupation. No law firm is named or invented, and the profile
asks for Box 541 and directory review.

Two identity conflicts remain deliberately unresolved. A declassified Defense
Department review calls one historical `John Moseley` reference a probable
error for **Philip E. Mosely**, but the personnel index preserves separate John
Moseley and Philip Mosely rows in Box 541. John receives no Cornell, COI, or
employer history from Philip's record. **Peter M. Moshopoulos** has an exact
official Army and 1944 OSS spelling match, but the index also contains a
separate Peter M. Mishopoulos row under the same protected identifier. Both
profiles remain separate in one visible duplicate-review group pending Box 529
and Box 541 jacket comparison; no military biography or employer is assigned
exclusively to either row.

Seventeen people reached `no_reliable_result_after_protocol`; John Moseley and
Peter Moshopoulos have `conflicting_sources`; Amos Moscrip is `completed`;
Edward Mosk has `documented_prewar_employer_found`; Jacob Mosak has
`verified_employer_found`; and Philip Mosely retains his prior
`verified_employer_found` outcome. The staged protocol covered the official
index and Army bulk file, exact-name OSS and employment searches, CIA-domain
searches, Library of Congress and newspaper attempts, institutional sources,
obituaries, directories, and archival finding aids. A Maryland court-index
result for Margaret Moseley and legal records belonging to Amos Moscrip's
father were rejected rather than used as namesake evidence. A negative online
result is never represented as proof that earlier employment did not exist.

The evidence bundle imports 11 sources, four organizations, five affiliations,
14 claims, 33 claim-source links, 22 person updates, and 22 consolidated
research attempts. The featured oil-company category remains evidence-scoped
to **eight people across ten historically named companies**; no Batch 682
person was added without a qualifying cited work relationship.

Rebuilt coverage is **23,978/23,978** linked source rows and **23,939** active
person entities. Research-attempt coverage is **8,736/23,939 (36.4928%)**;
confirmed/high verified-employer coverage is **307/23,939 (1.2824%)**;
confirmed/high verified-affiliation coverage is **680/23,939 (2.8406%)**;
archival-review disposition coverage is **7,192/23,939 (30.0430%)**. There are
**15,198** `not_started` people, **514** possible-duplicate groups, and **236**
active conflicts. SQLite stores **15,776** attempts or plans and **5,529**
claims: 1,329 confirmed, 2,343 high, 1,452 medium, 196 low, and 209 conflicting.
It contains **5,361** citation records and **2,618** unique source documents.
The public projection contains **2,344** affiliations, **776** organizations,
**4,144** sources, and **5,326** claims. Full-index historical research remains
unfinished.

## Replay and continuation

After importing prior durable batches into private SQLite:

```sh
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
python3 -m oss_research import-review-decisions research/identity_review_decisions_2026-09-25_batch682.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page331-mory-mosler-review_batch-682_2026-09-25.json
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
