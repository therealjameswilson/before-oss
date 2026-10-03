# Batch 668: Moehring-Moloy research

The next contiguous queue covers PDF page 325 rows 4-25, from `Glen E.
Moehring` through `Kenneth Moloy`. It contains **22 source rows and 22 cautious
person entities**. Every person now has a saved, reviewed outcome grounded in
the visually checked NARA index, official Army bulk identity comparison where
applicable, a policy-compliant CIA Reading Room access attempt, a live Library
of Congress query, exact-name and meaningful-variant OSS searches, employment
and occupation searches, and institutional, newspaper, obituary, directory,
military, or archival checks as applicable. No authenticated NARA Catalog
request was made.

The reviewed findings preserve identity, relationship, and chronology limits:

- **Faye K. Mogin** is a probable match to a Washington Post obituary subject
  with the same rare full name. The obituary documents her move to Washington
  in 1941 and work as a secretary at the U.S. Department of Agriculture. The
  affiliation is published as a qualified, medium-confidence, documented
  prewar role—not as an immediate pre-OSS affiliation or last civilian
  employer. The exact rare name and matching wartime Washington clerical
  context are the principal identity evidence; the adjacent Bert Mogin row is
  corroborative only.
- Protected Army identifiers support high-confidence identity matches for
  **John J. Mogavero, Bert Mogin, Charlie Moia, Arthur J. Mokin, Harry J.
  Moles, Anthony N. Molino, Henry C. Moll, Sigmund L. Molnar,** and **Samuel
  H. Molodow**. Army occupation codes remain private identity evidence and are
  never converted into employers.
- The Army form `Sam H Molodow` is preserved as a name variant for the indexed
  `Samuel H Molodow`; the rare surname, matching middle initial, conventional
  first-name variant, and nonshared protected identifier support the match.
- The protected-number candidate for **James Moffat** names Dominic A.
  Centobene and was rejected as a source or column-shift conflict. The indexed
  person remains unresolved rather than being silently overwritten.
- The Library of Congress candidate for **William J. Moeller** concerns a
  namesake named in a 1941 false-pretenses indictment. It supplies no rank,
  identifier, OSS, Box 531, residence, or employment bridge and was rejected.
- Searches for later documentary-film and authorship work by an Arthur Mokin,
  postwar government and Stanford Research Institute work by Bert Mogin, and
  later legal or agricultural publications by Paul O. Mohn were not
  back-projected into pre-OSS employment.
- Every other person remains visible with an explicit archival next action;
  failed online research is not represented as evidence that no earlier
  employment existed.

The bundle adds **11 claims, one affiliation, one reused canonical
organization, three sources, 21 claim-source links, and 22 reviewed research
attempts**. Eleven generated candidates received review decisions: nine exact
or defensible protected-identifier Army matches were accepted and two
unbridged or wrong-name candidates were rejected. All 22 people have terminal
batch outcomes: one `documented_prewar_employer_found`, twelve
`no_reliable_result_after_protocol`, and nine `requires_archival_review`.
Batch identity outcomes are nine `high_confidence`, one `probable`, and twelve
`unresolved`.

Rebuilt coverage is **23,978/23,978** linked source rows and **23,939** active
person entities. Research-attempt coverage is **8,446/23,939 (35.2813%)**;
confirmed/high verified-employer coverage remains **300/23,939 (1.2532%)**;
confirmed/high verified-affiliation coverage remains **664/23,939 (2.7737%)**;
archival-review disposition coverage is **6,902/23,939 (28.8316%)**. There are
**15,488** `not_started` people, **512** possible-duplicate groups, and **216**
active conflicts. SQLite stores **15,039** attempts or plans and **5,358**
claims: 1,325 confirmed, 2,215 high, 1,431 medium, 196 low, and 191
conflicting. It contains **5,264** citation records and **2,541** unique source
documents. The public projection contains **2,314** affiliations, **766**
organizations, **4,048** sources, and **5,158** claims.

The oil-company category remains evidence-scoped to **eight people across ten
historically named companies**. Faye Mogin's federal employment does not alter
that category. Full-index historical research is unfinished.

## Replay and continuation

After importing prior durable batches into private SQLite:

```sh
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
python3 -m oss_research import-review-decisions research/identity_review_decisions_2026-09-25_batch668.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page325-moehring-moloy-review_batch-668_2026-09-25.json
python3 -m oss_research export-adapter-checkpoints
python3 -m oss_research export-derived
python3 -m oss_research export-review-queue
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
```

Adapter checkpoints must be imported before the final reviewed decisions and
evidence so temporary adapter states cannot supersede the batch's reviewed
research dispositions.

No API key, full service number, raw Catalog API response, copyrighted page
image, or private reviewer note is committed or included in the public site.
