# Contributing

Corrections and research contributions are welcome when they preserve evidence,
uncertainty, and the distinction between source rows and resolved people.

## A useful correction includes

- person ID and indexed name;
- the exact claim being corrected or proposed;
- a stable source URL or archival identifier;
- source title, creator, repository, date, and locator when available;
- an evidence paraphrase and excerpt of no more than 25 words;
- identity-match reasoning;
- temporal reasoning explaining whether the role was immediate, last civilian,
  merely prewar, or chronologically uncertain;
- any credible competing identity or claim.

Do not submit full service numbers, home addresses, Social Security numbers,
medical files, living-descendant details, copyrighted page copies, paywalled
material, or AI-generated summaries as evidence.

## Review workflow

Generated CSV, JSON, and site files are not edited directly. Export the queue,
enter append-only decisions in a CSV containing:

```text
target_type,target_id,decision,rationale,reviewer,decision_version
```

Then run:

```bash
python3 -m oss_research import-review-decisions review_decisions.csv
python3 -m oss_research export-derived
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
```

Reviewed presentation corrections use `target_type=person_entity` and a
`decision` beginning `display_name:` followed by a JSON object containing
`expected` and `replacement` names. The importer fails if the current name
is neither the expected old value nor the already-applied replacement. It
records the reviewer and rationale, preserves the original as a search alias,
and changes neither raw index fields nor identity confidence. Replay CSVs
belong in `research/*_review_decisions_*.csv`; never edit generated profiles.

Candidate decisions may be `plausible`, `probable`, `accepted`, `rejected`, or
`conflicting`. Research-status decisions must use the controlled values in
`DATA_DICTIONARY.md` and the database schema.

## Tests

```bash
python3 -m unittest discover -s tests -v
cd site
npm run test:ci
```

`npm run test:ci` builds the complete static site and runs the newest batch
specification, bounded core-route checks, analysis checks, the accessibility
suite, and the generated-site link audit. The release runner discovers the
highest numbered `batchNNN.spec.ts` automatically so a new batch cannot leave
CI pinned to an older cohort. This bounded suite keeps each Playwright process
below the memory ceiling of a standard GitHub-hosted runner.

`npm test` remains the exhaustive historical browser matrix. Run it on a host
with sufficient memory when performing a full regression audit; its component
specifications can also be run in bounded groups with `npm run test:e2e --
tests/<spec>.spec.ts`.

No test may consume a live NARA API request. Adapter tests use synthetic,
hand-authored fixtures.
