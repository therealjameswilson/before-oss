# Batch 681: Morrissey-Morwood research

Batch 681 completes PDF page 331, rows 1-23, from `Thomas T Morrison`
through the two adjacent `William G Morwood` entries. Visual inspection and
layout-text comparison confirmed all 23 printed rows. Every record remains
linked to its own person entity.

Eleven official Army bulk candidates support high-confidence identities for
**Thomas T Morrison, Edward F Morrissey, Robert H Morrissey, John E Morrone,
Charlie B Morrow, Lloyd J Morrow, Charles E Morse, George P Morse, Richard
Morse, Arlo G Morton, and the corporal William G Morwood**. Exact indexed names
and nonshared protected identifiers agree across official records. The Army
file's coded occupations remain private and are not treated as employer
evidence.

Two protected-identifier candidates conflict with the printed index. The Army
file names **Harlie B Morse** where the index prints **Harlie P Morse**, and
**Melvin S Mooton** where the index prints **Melvin S Morton**. Both cases are
published as conflicts requiring Box 540 review; neither spelling is silently
substituted for the other.

Institutional and official sources identify three substantive pathways. The
Army record and three Dartmouth Alumni Magazine items make **Richard Morse** a
high-confidence match to Dartmouth's Richard Morse '44, an Army sergeant who
served as an OSS liaison in Burma. His Phi Beta Kappa listing in April 1943
and May 1943 Army-entry date support strongly date-bounded Dartmouth student
status. Dartmouth is not represented as an employer, and his precise
immediate pre-OSS military assignment remains unresolved.

A contemporaneous OSS personnel-review record confirms **Don E Mort** through
his uncommon exact name, lieutenant rank, and protected identifier. It gives
exact dates for his April 1941 Army entry and August 1943 OSS assignment, so
the United States Army is published as his explicit immediate pre-OSS military
pathway. The same record says he had been a salesman in the Midwest. That is
published as occupation-only evidence with no inferred employer.

Lawrence C. Soley's documented history identifies **William Morwood** as a
prewar radio writer who was drafted, completed basic training, transferred to
OSS Morale Operations, and was later promoted from sergeant to lieutenant.
The corporal row has an exact protected-identifier Army match, supporting a
high-confidence Army pathway and occupation-only radio-writer finding. The
adjacent lieutenant row is only a probable match: the rare-name and promotion
chronology are persuasive, but the two indexed protected identifiers differ.
Both source rows remain separate in a possible-duplicate group pending
comparison of their Box 540 files.

**Chandler Morse's** previously reviewed, confirmed Federal Reserve findings
were carried forward without modification: the Federal Reserve Board is his
explicit immediate pre-OSS government assignment, and the Federal Reserve Bank
of New York is his documented earlier civilian employer.

Sixteen people reached `no_reliable_result_after_protocol`; two have
`conflicting_sources`; Richard Morse is `completed`; Don E Mort and the
corporal William G Morwood have `occupation_only_found`; the lieutenant
William G Morwood has `requires_archival_review`; and Chandler Morse retains
`verified_employer_found`. The staged protocol covered the official index and
Army bulk file, exact-name OSS and employment searches, CIA-domain searches,
Library of Congress attempts, institutional publications, newspapers,
obituaries, directories, books, and archival finding aids. The CIA adapter
failed closed and two Library of Congress attempts timed out; these events
were not treated as negative evidence.

The evidence bundle imports seven sources, two reused canonical organizations,
five affiliations, 20 claims, 39 claim-source links, 22 person updates, and 22
consolidated research attempts. Chandler Morse already had a complete saved
attempt. The featured oil-company category remains evidence-scoped to **eight
people across ten historically named companies**; no Batch 681 person was
added without a qualifying cited work relationship.

Rebuilt coverage is **23,978/23,978** linked source rows and **23,939** active
person entities. Research-attempt coverage is **8,714/23,939 (36.4009%)**;
confirmed/high verified-employer coverage is **306/23,939 (1.2782%)**;
confirmed/high verified-affiliation coverage is **678/23,939 (2.8322%)**;
archival-review disposition coverage is **7,170/23,939 (29.9511%)**. There are
**15,220** `not_started` people, **515** possible-duplicate groups, and **234**
active conflicts. SQLite stores **15,754** attempts or plans and **5,515**
claims: 1,329 confirmed, 2,332 high, 1,451 medium, 196 low, and 207 conflicting.
It contains **5,351** citation records and **2,612** unique source documents.
The public projection contains **2,339** affiliations, **775** organizations,
**4,134** sources, and **5,312** claims. Full-index historical research remains
unfinished.

## Replay and continuation

After importing prior durable batches into private SQLite:

```sh
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
python3 -m oss_research import-review-decisions research/identity_review_decisions_2026-09-25_batch681.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page331-morrissey-morse-review_batch-681_2026-09-25.json
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
