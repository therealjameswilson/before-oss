# Batch 737: Pascuzzi-Paterson research

Batch 737 completes PDF page 359, rows 1-23, from **Angeline Pascuzzi**
through **Jane Paterson**. A 300-dpi visual inspection confirmed all 23
printed rows in Boxes 587-588 at location 230/86/38/02. Embedded text was
checked against the page render. Original spellings, ranks, grades, notes,
and protected identifiers remain recoverable in the private database.

The inspection preserves unusual printed forms rather than silently
expanding them. **Arthur Pashcow** appears out of sequence in Box 587;
**Michael H Passarella** carries the visibly incomplete note `Extracte`;
and **Lloyd E Patch** has the printed rank `Cpt`. The two **Paul J Paterni**
rows—one first lieutenant and one corporal—remain separate source records
and separate person entities.

Seven high-confidence identities come from compatible official Army bulk
matches with nonshared protected identifiers: **Arthur Pashcow**, **Kalman
Pasichnyek**, **Frank A Pasquale**, **Michael H Passarella**, **David A
Passet**, **Connie Patane**, and **John J Pater**. These matches establish
identity only. Protected identifiers and coded Army data remain private and
are not converted into employer or occupation claims. The Army record for
Frank A Pasquale includes a `Jr.` suffix, retained as a search variant rather
than an alteration to the index.

NARA's Entry 220 page independently links exact-name, exact-rank **Major
Felix Pasqualino** to OSS work in Rome. A Connecticut state historic-context
report and the Marine Corps History Division's biography-file index establish
high-confidence identity for **Sebastian J Passanesi** and document his 1935
architecture degree from the Catholic University of America. That university
relationship is published as `student`, not employment. The report's later
architectural-firm information is not projected backward into the pre-OSS
period. **Lloyd Edwin Patch** is also linked at high confidence by name, rank,
and protected identifier; his 506th Parachute Infantry service remains
identity context because the accessible chronology does not show that unit
immediately preceded OSS.

The strongest employment chronology in the batch belongs to **Paul J
Paterni**. A May 3, 1944 wartime OSS report says he entered the Army in
February 1943 and was assigned to OSS in September 1943. A 2022 University
of Trieste catalogue states that he first worked for the U.S. Veterans
Administration, then the U.S. Secret Service, and obtained permission to
join the Army in 1942; a Washington Post obituary independently corroborates
the Secret Service-Army-OSS sequence. The published profile therefore
distinguishes the Army as his immediate pre-OSS military assignment, the
Secret Service as his last civilian affiliation before service, and the
Veterans Administration as earlier prewar government employment. A nearby
wartime phrase describing a paint spreader belongs to Michael A. Grandinetti
and is explicitly not attributed to Paterni.

The second Paterni row remains only a probable match. The rare name and
documented enlisted-to-officer progression are persuasive, but no accessible
source directly ties the corporal identifier to the officer identifier.
Both profiles expose a possible-duplicate group and request comparison of the
two Box 588 files; the officer's affiliations are not copied to the corporal.

**John Pastilock** remains conflicting because his printed protected
identifier reaches an official Army record whose name reads `PAST OCK JOHN`.
An initials-only operational-groups roster lead does not repair the mismatch.
No coded Army metadata is transferred, and the file receives critical
archival-review priority.

All 23 people have terminal dispositions: 20 require archival review, one is
completed with a documented student affiliation, one has conflicting sources,
and one has a verified pre-OSS chronology. Identity statuses are 11
high_confidence, one probable, one conflicting, and ten unresolved. The
reviewed bundle imports nine sources, four organizations, four affiliations,
16 claims, 33 claim-source links, 23 person updates, and 23 consolidated
research attempts. Seven accepted and one conflicting identity-review
decisions are recorded.

Rebuilt coverage is **23,978/23,978** linked source rows and **23,939** active
person entities. Research-attempt coverage is **9,985/23,939 (41.7102%)**;
confirmed/high verified-employer coverage is **334/23,939 (1.3952%)**;
confirmed/high verified-affiliation coverage is **747/23,939 (3.1204%)**;
archival-review disposition coverage is **8,443/23,939 (35.2688%)**. There
are **13,949** not_started people, **524** possible-duplicate groups, and
**334** active conflicts. SQLite stores **18,273** attempts or plans and
**6,389** claims: 1,383 confirmed, 2,973 high, 1,537 medium, 198 low, 296
conflicting, and two unresolved. It contains **5,725** citation records and
**2,898** unique source documents. The public projection contains **2,494**
affiliations, **865** organizations, **4,501** sources, and **6,182** claims.
Full-index historical research remains unfinished.

## Replay and continuation

After importing prior durable batches into private SQLite:

~~~sh
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
python3 -m oss_research assign-page-batch --batch-name batch-737-pascuzzi-paterson --page 359 --first-row 1 --last-row 23
python3 -m oss_research research --source cia --batch batch-737-pascuzzi-paterson --max-queries 23
python3 -m oss_research research --source loc --batch batch-737-pascuzzi-paterson --max-queries 23
python3 -m oss_research research --source web --batch batch-737-pascuzzi-paterson --resume --max-queries 23 --dry-run
python3 -m oss_research import-review-decisions research/identity_review_decisions_2026-10-04_batch737.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page359-pascuzzi-paterson-review_batch-737_2026-10-04.json
python3 -m oss_research export-adapter-checkpoints
python3 -m oss_research export-derived
python3 -m oss_research export-review-queue
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
~~~

Adapter checkpoints must be imported before final reviewed decisions and
evidence so temporary discovery states cannot supersede reviewed dispositions.
The next research boundary is PDF page 359, rows 24-46, from Lewis C Paterson
through Jere W Patterson.

No API key, full service or officer number, raw Catalog or LoC API response,
copyrighted page image, street address, living-relative detail, modern
people-finder record, unrelated Army coded occupation, or private reviewer
note is committed or included in the public site. No authenticated NARA
Catalog API request was made for this batch.
