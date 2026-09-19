# Batch 579 release candidate

Built and tested locally on 2026-09-19 UTC. Public deployment and
unauthenticated live verification are **pending**; Batch 578 remains the last
exact-verified public release until those steps succeed.

## Coverage and evidence

| Measure | Exact local count |
| --- | ---: |
| Printed source rows linked | 23,978 / 23,978 |
| Active cautious person entities | 23,940 |
| People with saved non-planned research attempts | 5,554 (23.1997%) |
| People with verified affiliations | 599 (2.5021%) |
| People with verified employers | 261 (1.0902%) |
| People with archival disposition assessed | 5,509 (23.0117%) |
| Active people not started | 18,386 |
| Possible-duplicate groups | 256 |
| Private durable attempts | 10,125 |
| Claim confidence: confirmed / high / medium / low / conflicting | 1,307 / 1,753 / 1,357 / 183 / 129 |
| Public affiliations / organizations / sources / claims | 2,165 / 674 / 3,690 / 4,542 |

The ten reviewed people occupy PDF page 116 rows 37–46 in Box 184. All ten
have terminal `requires_archival_review` outcomes. Robert C DeWeese Jr.,
Howard P Dewitt, and Jack W Dexter have reviewed, high-confidence official
Army identity crosswalks; no Army occupation code was converted to an
employer. The Albert P Dewey / A. Peter Dewey identity lead is published only
as a qualified warning because the public award-order transcription differs
from the printed index by one service-identifier digit. The candidate's
Chicago Daily News career is withheld from the indexed person's employer
fields. No employer or affiliation was added in this batch. Details and
sources: `research/batch-579-discovery-checkpoint.md`.

## Local quality checks

- `validate-ingest`: 522/522 PDF pages represented; 23,978 rows; selected and
  warning-page visual-review checks; SQLite integrity and foreign keys pass.
- Python unit tests: 98/98 pass; 200-profile structural audit passes.
- Astro: zero errors, warnings or hints across 205 checked source files;
  24,622 direct HTML pages built in the Pages configuration.
- Bounded Playwright suite: 69/69 checks pass across desktop, phone and
  tablet, including 27 axe accessibility checks with no serious violations.
- All internal links resolve. 50,094 distinct external URLs are inventoried,
  not all visited.
- Identifier audit: zero unexpected full-identifier matches across 24,694
  production artifacts; 12,926 private normalized identifiers tested.
- Two production builds reproduced the same 24,694-artifact tree digest
  `7fadf768d26459f00c581f1ef7e4934cfea21ea6f93b1aadcf81f5749e1d669c`.
- Local public manifest: 67 assets / 96,107,476 bytes, SHA-256
  `082a37ff32e825cc6acd7a3526f94d70cdc4aff1597f3927e84c1dc487814062`.

Resume research at PDF page 117, row 1, after validating the next bounded
cohort. The current objective remains incomplete with 18,386 active people
`not_started`; a discovery query alone is not a reviewed employer outcome.
