# Batch 605: page 137, Pennco, and the oil-company category

The original NARA index PDF page 137 was rendered at 170 dpi and every one
of its **46 printed rows** was compared with the immutable SQLite row. No
parser correction was needed. This newly sampled page raises the distinct
visual-review ledger to **108/522 pages**; **414** remain. The review
preserves the truncated `SP (P) 2/` rank for John W Entz, the out-of-order
Box 221 for Herbert J Ersham, and the index's Swedish note for Eric S
Erickson. `H. Loyd Ericsson` and `Herman Lloyd Ericsson` share Box 222 but
have no identifying number: they are flagged as a possible duplicate pair,
**not merged**. The index's distinct Arthur Erickson and Wallace Erwin
initials also remain separate.

All **46** people on page 137 received one bounded, read-only Library of
Congress first-pass search. There were no adapter errors or budget blocks.
Seven candidate newspaper-page leads for four common-name Erickson rows
were saved as **unreviewed discovery leads**, not employers, identity
matches, or completed multi-source research protocols. No authenticated
NARA Catalog API request was made.

The visually verified index identifies [Eric S Erickson](https://therealjameswilson.github.io/before-oss/people/cd589355-8c39-5c32-9510-a747d795d9d6/)
as Swedish. [CIA's institutional history](https://www.cia.gov/resources/csi/static/oss-project-safehaven.pdf)
identifies a Swedish Eric Erickson working for OSS; a [1943 government
notice](https://library.victoria.ac.nz/databases/nzgazettearchive/pubs/gazettes/1943/1943%20ISSUE%20046.pdf)
supplies `Eric Siegfried Erickson`, and the [1952 Stockholm directory](https://sok.stadsarkivet.stockholm.se/bildarkiv/egenproducerat/rodaboken/Roda_boken_1952_109_126.pdf)
directly names `Eric S Erickson` as director of Bensin AB Pennco. The
directory was streamed and text-inspected without retaining the PDF.
The [authorized publisher description of Stephan Talty's biography](https://books.google.com/books/about/The_Secret_Agent.html?id=pxjqAgAAQBAJ)
places Erickson in the oil business in 1942, while a [Swedish historical
essay](https://globalaeremitaget.com/eric-erickson-den-bortglomda-svenska-storspionen/)
specifically reports that he operated Pennco by 1937. The latter is a
secondary source, and the postwar directory cannot independently prove the
prewar company's exact legal identity. The public claim is therefore
**qualified medium confidence**, modeled as prewar **self-employment** in
his own named oil business. It is neither a proven immediate pre-OSS
affiliation nor a claim that the 1952 legal entity already existed in 1937.
The Box 221 file and prewar Swedish company records remain to be reviewed.

The top-of-site oil-company category now admits cited employment **or
self-employment** at a named oil company, with the own-business and
medium-confidence labels visible. It lists **seven** people, including
Erickson, and still excludes professional affiliations, mere oil-industry
mentions, and namesake leads such as Fred Bielaski and John L Endacott.

At this checkpoint, **23,978/23,978** source rows link to **23,940** active
people. **6,505/23,940** have a nonplanned research attempt (27.1721%);
**271/23,940** have confirmed/high published employer evidence (1.1320%);
**617/23,940** have confirmed/high published affiliation evidence (2.5773%);
and **5,767/23,940** have an assessed archival-review disposition
(24.0894%). **17,435** are `not_started`; there are **280** possible-duplicate
groups. SQLite retains **11,549** attempts or plans, **4,866** claims
(1,311 confirmed, 1,868 high, 1,370 medium, 185 low, 132 conflicting),
**5,003** citations/source records, and **2,332** unique source documents.
The public projection has **2,203** affiliations, **694** organizations,
**3,800** sources, and **4,677** claims. This is not full-index research
completion.

Local QA passed: 122 Python unit tests, 78 bounded release browser and
accessibility checks, 558 affected desktop regression checks, the 200-profile
structural audit, the 24,693-page local internal-link check, the full-number
redaction audit, and the static Astro build. Three older browser expectations
for Eifler, Eddy, and Bielaski had lagged earlier published corrections;
they were updated and the complete affected regression set rerun cleanly.
The 200-profile audit is structural rather than a manual source audit.

## Replay and continuation

After importing earlier batches into the private SQLite database:

```sh
python3 -m oss_research import-page-reviews research/parser_visual_review_page137_2026-09-21.json
python3 -m oss_research assign-page-batch --batch-name page-137-enos-eschweiler-b605 --page 137 --first-row 1 --last-row 46
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
python3 -m oss_research import-reviewed-evidence research/evidence-page137-variant-review_batch-605_2026-09-21.json
python3 -m oss_research import-reviewed-evidence research/evidence-eric-erickson-pennco_batch-605_2026-09-21.json
python3 -m oss_research validate-ingest
python3 -m oss_research export-derived
python3 -m oss_research build-public-data
python3 -m oss_research coverage-report
```

The NARA API key was not used, copied into the repository, or included in
public assets. The SQLite database remains private; replayable adapter
checkpoints retain sanitized attempt metadata, not raw response payloads.
