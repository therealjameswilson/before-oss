# Batch 575 public release verification

Verified 2026-09-19 UTC. Pull request [#274](https://github.com/therealjameswilson/before-oss/pull/274)
passed Test run 35461888181 and merged as
`a73cf8d26108001ad5da74fdb1cfa6b8151daa87`. The merged-branch Test
run 35462295431 and Pages run 35462295429 both succeeded.

The unauthenticated verifier checked the live
[Before OSS site](https://therealjameswilson.github.io/before-oss/) against
the immutable merge commit: all 67 public-manifest assets (95,955,642 bytes),
all seven core routes, and the nine new direct profile URLs matched. Manifest
SHA-256: `8cd0c06d7b96538b7c8680e489c6379bca0b64df9cfe0dd8a56e30b8af03189c`.
The [oil-company category](https://therealjameswilson.github.io/before-oss/people/?featured=oil_companies&sort=name_asc)
remains prominent in the top navigation and near the top of the home and
directory pages; live-browser and desktop, phone, and tablet tests show exactly
seven documented employees at nine historically named oil companies. This is
the count found in the current research, not an exhaustive OSS oil-industry
census.

## Research and release counts

| Measure | Exact count |
| --- | ---: |
| Printed source rows linked | 23,978 / 23,978 |
| Active cautious person entities | 23,940 |
| People with saved non-planned research attempts | 5,514 (23.0326%) |
| People with verified employers | 261 (1.0902%) |
| People with archival disposition assessed | 5,469 (22.8446%) |
| Active people not started | 18,426 |
| Possible-duplicate groups | 256 |
| Private durable attempts | 10,005 |
| Claim confidence: confirmed / high / medium / low / conflicting | 1,307 / 1,731 / 1,353 / 183 / 129 |
| Public affiliations / organizations / sources / claims | 2,163 / 673 / 3,673 / 4,516 |

The nine Batch 575 people receive terminal `requires_archival_review`
outcomes, with no newly assigned named employer. The indexed John/Sol Deull
rows remain distinct. The Catherine DeVaney obituary lead is visibly
qualified; its undated jobs do not enter employer analytics. William C
Deutsch and Hector F DeVega gained high-confidence Army identity links, not
employer claims. Reviewable sources, decisions and queries are in
`research/batch-575-discovery-checkpoint.md` and its linked evidence bundle.

## Checks and reproducibility

- `validate-ingest`: all 522 pages represented, 23,978 source rows and all
  parser, warning-row, selected-page, and SQLite checks pass.
- Python unittest: 97/97 pass. The 200-profile structural audit passes all
  seven checks. Public-identifier scan: zero unexpected boundary matches
  across 24,693 production artifacts.
- Static build: 24,621 direct HTML pages; no Astro diagnostics. All internal
  links resolve. Bounded browser release suite: 69/69 pass across desktop,
  phone and tablet, including 27 axe accessibility checks.
- A detached worktree at the merge commit rebuilt from the frozen source PDF,
  adapter checkpoints, review decisions and evidence bundles. Its 70-file
  public tree exactly matched the release tree: SHA-256
  `8411b8c3522371dbd229b044f2d90f8c88c4e5226158ee91fe7ff4b27ab96d71`;
  its 24,693-file production tree also matched exactly: SHA-256
  `a979f6b41ff22cbdb1e836ea5270b51e6fd63ce6b1d87c757613bb4303319e3b`.
  Only generated QA-report timestamps differed in the replay worktree.

The all-history Playwright invocation can exceed the local Node heap during
test discovery because many historical specs independently load the complete
profile JSON. The bounded release suite is the tested CI gate; historical
batch specs remain available individually. This is a test-harness scaling
issue, not a failed production build or live category check.

## Continuing the main research goal

Resume at PDF page 116 row 7 after inspecting the rendered page. Run a
bounded official-source and cross-source search, record candidate rejections,
and import a reviewed evidence bundle. The authenticated NARA Catalog adapter
still requires a local `NARA_API_KEY` at runtime; no key was committed or
placed in public assets. Many unresolved profiles, including this cohort,
require Box 183 or other physical personnel-file review. Completion has not
been claimed while 18,426 active people remain `not_started`.
