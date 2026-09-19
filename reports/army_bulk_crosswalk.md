# Official Army bulk-file identity crosswalk

Run date: 2026-09-19 UTC. Adapter: `army-bulk-identity-v1`.

The project compared eligible private identifiers from the printed OSS index
against every record in NARA's separately published *Electronic Army Serial
Number Merged File* ([file NAID 1263923](https://catalog.archives.gov/id/1263923)).
The source passed the fixed-size, 91-byte-record, record-count, CRLF, and
SHA-256 checks in `data/provenance/army_bulk_manifest.json` before any
candidate write. This is bulk-data use, not an authenticated Catalog API call.

| Measure | Exact count |
|---|---:|
| Official Army records scanned | 9,200,232 |
| Eligible OSS index rows with eight-digit identifiers | 8,986 |
| Distinct eligible indexed people | 8,954 |
| Private identifiers with at least one bulk hit | 7,167 |
| Eligible private identifiers with no bulk hit | 1,663 |
| Candidate row-to-record comparisons checkpointed | 7,364 |
| Distinct indexed people with a checkpointed lead | 7,268 |
| Name agrees under conservative surname/given/middle comparison | 5,857 |
| Surname and given agree, middle absent in Army record | 55 |
| Surname and given agree, middle differs | 80 |
| Indexed and Army names conflict | 1,372 |
| Of those, spelling differs only in spacing or punctuation | 196 |
| Of those, substantive name differences remain | 1,176 |
| Candidate comparisons involving an identifier shared across index people | 198 |
| Candidates still awaiting checkpoint | 0 |
| Research-status changes made by this crosswalk | 0 |
| Employer or affiliation claims created | 0 |

Candidates were stored in the private `candidate_matches` table in bounded,
idempotent batches of at most 500. Deterministic candidate IDs preserve any
later human decision on rerun. The candidate evidence retains the bulk record
ordinal, name-alignment category, and selected uninterpreted Army field codes,
but no full private identifier or raw 91-byte record. The official bulk file
itself is not committed or included in public downloads. `export-derived`
creates a 7,364-row, Git-ignored `research/army_bulk_review_queue.csv` with
masked-by-omission identifier handling and name conflicts sorted first. The
review queue derives `conflict_triage` from the stored indexed and Army names:
196 conflicts collapse to identical names after whitespace and punctuation
are removed, while 1,176 still differ substantively. This is a routing aid,
not an identity decision; a spacing-equivalent name can still be a wrong
record, and a substantive difference can reflect an indexing error.

This crosswalk does **not** count as a completed research attempt. A number
match alone cannot verify an OSS identity: the file has known transcription
problems and duplicate numbers, and the index can itself contain duplicate or
shifted values. A non-hit does not prove a person did not serve in the Army.
The Army file does not contain a full roster of commissioned officers. Its
civilian-occupation code describes the time of Army entry; even a reviewed
code is not a named employer, an immediate pre-OSS affiliation, or an OSS
rank. The 1,372 name conflicts and 198 shared-index-identifier comparisons
require particularly careful review.

As a result, the four primary coverage measures remain unchanged: 23,978 of
23,978 printed rows linked (100% index coverage), 5,505 of 23,940 active
people with a non-planned research attempt (22.9950%), 261 of 23,940 with a
confirmed/high published employer (1.0902%), and 5,460 of 23,940 with an
archival disposition assessment (22.8070%). There are still 18,435 active
`not_started` people. These candidate leads can prioritize future human
research, but they cannot be counted as completed prehistories.

Resume or reproduce with:

```bash
python3 -m oss_research army-bulk-match --file /absolute/path/ASNEF.FIN.DAT --max-candidates 500
```

The command should then report `candidates_checkpointed_this_run: 0` and
`candidates_remaining: 0`. A changed source file fails closed unless its
provenance is deliberately reverified and the expected digest updated.
