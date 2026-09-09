# Batch 440 release verification

2026-09-09 UTC. **Local release candidate; independent release checks
pending.** This report covers PDF page 86 rows 24-33, Martin G Cohn through
Alfred Colandrea, all in Box 133 at location 230/86/28/07.

## Research

Page 86 was rendered at 150 dpi. Every printed name, initial, blank rank,
private identifier or blank, box, note and location in the cohort was visually
matched to the immutable database before research. All ten rows print Box 133;
all ranks and notes are blank. Seven private identifiers remain research-only
and are masked in every public artifact. Raymond T Col remains exactly as
indexed: the project introduces no unreviewed surname expansion or correction.

A complete transient scan of 9,200,232 fixed-width Army merged-file records
tested the printed identifiers literally. Myron Cohn, Theodore Cohn, Trayone J
Cojerian, Raymond T Col, Hugo Colacicco and Alfred Colandrea each have an exact
identifier-and-name match. Myron, Trayone, Raymond, Hugo and Alfred each have
one exact-name Army row; Theodore's identifier selects one of fourteen exact-
name rows. Owen S Coke's shorter six-digit identifier is not padded, truncated
or otherwise repaired to select a candidate. Martin G Cohn, Dorothy E Cokeley
and Vassilia Cokinides have no exact-name Army row. These non-hits are not
negative proof because the Army file is incomplete and is not a comprehensive
military or OSS roster.

Official NARA record-layout and code-list documents support the six enlisted
Army classifications and five occupation descriptions. Myron and Raymond are
recorded as `Accountants and auditors`; Trayone and Hugo as `Machinists`.
Theodore is recorded as a `Student`. Each observation remains medium-
confidence and temporally qualified: none names an employer, client, school,
workplace, specialty or precise transition into OSS. Theodore's student status
is modeled as `student`, never as employment. Hugo's Branch Immaterial value is
not misread as warrant-officer rank.

Alfred's official Army row carries civilian-occupation value 649. A reviewed
secondary code transcription supplies two possible meanings, `Job pressman`
or `Casting-machine operator`. Both alternatives remain visible in one
qualified observation, neither is chosen as the true occupation, and no
printing shop, foundry, employer or industry is inferred. The interpretation
therefore retains D source quality even though the official identifier and
name evidence confirms the person and dated Army entry.

The Library of Congress identifies a Martin G. Cohn, 1893-1953, as film editor
on a 1920 motion picture. The distinctive three-part name and securely prewar
date support only a probable identity because the index row has no identifier,
rank, occupation or direct biographical bridge. Film editing is published at
medium confidence as an earlier `documented_prewar` occupation. The motion-
picture production company is not treated as an employer, and a 1920 role is
not described as Martin's immediate pre-OSS affiliation.

Owen S Coke, Dorothy E Cokeley and Vassilia Cokinides remain unresolved. An
exact-name 1950 Virginia newspaper notice concerning a law graduate named
Vassilia Cokinides is postwar and supplies no OSS, Box 133 or wartime bridge;
it remains only an archival comparison lead. An enthusiast-maintained
Operational Group roster naming Hugo was rejected as final evidence. Cemetery,
obituary, directory, genealogy and similarly named results were rejected when
they lacked the printed middle initial, identifier or direct OSS connection.
All three unresolved profiles retain specific personnel-file questions rather
than a claim that no prior employer existed.

Exact-name OSS and CIA searches, meaningful variants, employment and
occupation searches, institutional archives, obituaries, directories,
newspapers, current Library of Congress discovery, official NARA context and
the complete Army comparison when applicable were recorded for every person.
Commercial people finders, sensitive living-person data, unsourced genealogy,
search snippets and name-only biographies were rejected as final evidence. No
authenticated NARA Catalog request was used.

The reviewed evidence bundle adds six citations, seven affiliations, fourteen
claims, thirty-nine claim-source links, ten person updates and ten saved
research attempts. It adds no organization and no employer claim. See
`research/batch-440-discovery-checkpoint.md` for the adjudication, rejected
leads, source cautions and next actions. All ten records remain on the archival
pull list. Research completion means a saved reviewable outcome, not that a
prior employer has been disproved.

## Exact local coverage

| Measure | Count / denominator | Percent |
|---|---:|---:|
| Index coverage | 23,978 / 23,978 source rows; 522 / 522 pages | 100.0000% |
| Research-attempt coverage | 4,177 / 23,940 active people | 17.4478% |
| Verified-employer coverage | 221 / 23,940 active people | 0.9231% |
| Verified-affiliation coverage | 504 / 23,940 active people | 2.1053% |
| Archival disposition assessed | 4,132 / 23,940 active people | 17.2598% |

There are 23,941 stored entities and one superseded entity; 235 possible
duplicate groups remain visible. Officer classification: 2,238 commissioned,
5,704 noncommissioned and 15,998 indeterminate. Identity: 804 confirmed, 618
high confidence, 138 probable, 106 ambiguous, 79 conflicting and 22,195
unresolved.

| Research status | Active people |
|---|---:|
| not_started | 19,763 |
| in_progress | 44 |
| candidate_found | 7 |
| needs_identity_review | 141 |
| needs_temporal_review | 13 |
| verified_employer_found | 212 |
| documented_prewar_employer_found | 79 |
| occupation_only_found | 729 |
| conflicting_sources | 78 |
| no_reliable_result_after_protocol | 82 |
| requires_archival_review | 2,665 |
| completed | 127 |

| Claim confidence | All claims | Employment/self-employment claims |
|---|---:|---:|
| confirmed | 984 | 35 |
| high | 1,267 | 286 |
| medium | 956 | 92 |
| low | 97 | 1 |
| conflicting | 90 | 2 |

There are 4,001 citation records, 1,859 provisional document keys that are not
certified unique historical documents, and 1,365 distinct stable URLs.
Inventory: 539 organizations, 1,651 affiliations, 3,394 claims, 7,822 claim-
source links and 5,401 attempts/plans. Attempt outcomes: 1,853
`source_reviewed`, 201 `candidate_found`, 675 `candidate_rejected`, 2,085
`no_result` and 587 `planned`. There are 1,654 people with stored claims and
1,573 with public or conflict-visible claims. Composite unresolved export:
22,793 data rows plus header. Conflict count: 83. Pull list: 23,766 data rows
plus header; review queue: 23,940 data rows plus header.

Public projection: 23,940 people, 527 organizations, 1,640 affiliations, 3,294
published, qualified or conflict-visible claims, 2,844 public citations and 26
profile shards. Public downloads contain 23,940 personnel rows, 527
organization rows, 1,640 affiliation rows and 2,844 citation rows.

## Local QA and resume

The evidence validates against the Pydantic schema and repeated import is
idempotent. A fresh replay into a new SQLite database from the frozen 522-page
PDF and every reviewed evidence bundle reproduces the Batch 440 counts and both
output-tree digests byte-for-byte. SQLite `quick_check` returns `ok`, foreign
keys pass, and all 93 Python tests pass in 4.422 seconds. The deterministic
200-profile structural audit passes; it is not independent historical re-
review, and the women stratum remains unavailable without sourced
classification.

The exact Pages-configuration build contains 24,475 HTML pages and 24,547
artifacts with zero Astro errors, warnings or hints. All internal links resolve;
49,653 external destinations are inventoried, not all visited. Identifier
checks inspect all 24,547 built artifacts, 12,926 normalized identifiers, 120
formatted variants and 1,094 candidate substring coincidences with zero
unexpected boundary, aggregate or manifest-size matches. The same audit over
all 70 public-tree files finds 663 candidate coincidences and zero unexpected
matches. The focused Batch 440 browser suite passes all twelve checks across
desktop, phone and tablet in 11.0 seconds after the fresh replay. An initial
focused run exposed one test-only wording expectation across three viewports;
the expectation was aligned with the already correct public page and both the
subsequent pre-replay and post-replay runs pass 12/12. The dependency audit
reports zero vulnerabilities across 379 installed dependency relationships.

The public manifest contains 67 assets / 85,980,837 bytes at SHA-256
`e04cbb7850d2754b9276fb685cb970a1ed9e84cc45f0a8a7974f0061e36f441c`.
The deterministic public-tree digest covers 70 files / 88,327,962 bytes at
SHA-256
`7d89e42d38876490f0dceafd39f4e6af6c7ceaaf469ac595e02e3b015b459917`;
the 24,547-file / 273,006,849-byte production tree is
`df1bd299f5fa17ee29168f1b6546702354c36795ce34adbd31425465b169b1e8`.
The pre-replay and clean-replay exact Pages builds reproduce both tree digests
and file counts.

Batch 439 passed independent pull-request Test `34327575176`, merged through PR
194 as `11a624cd12efc26706c3b0dc53dd4f4c6ebb8625`, deployed through Pages run
`34332364255`, and passed pinned-live verification of all 67 manifest assets,
seven core routes and ten direct profiles. Batch 440 is now rebased on that
release and still requires its own independent pull-request gate, merge,
deployment and pinned-live verification.

```sh
python3 -m oss_research import-reviewed-evidence research/evidence-page-eighty-six-martin-g-cohn-through-alfred-colandrea-pathways_batch-440_2026-09-09.json
python3 -m oss_research export-derived
python3 -m oss_research coverage-report
python3 -m oss_research audit-profiles
python3 -m oss_research build-public-data
cd site
PUBLIC_SITE_URL=https://therealjameswilson.github.io PUBLIC_BASE_PATH=/before-oss npm run build
npx playwright test tests/batch440.spec.ts
npm run check:links
cd ..
python3 scripts/audit_public_identifiers.py --database research/research.sqlite --public-root site/dist
python3 scripts/hash_tree.py site/public site/dist
```

Full replay: `PUBLIC_SITE_URL=https://therealjameswilson.github.io
PUBLIC_BASE_PATH=/before-oss bash scripts/rebuild-all.sh`. The goal remains
active and incomplete, with 19,763 active people still `not_started`. Rotate
the previously exposed credential before authenticated NARA work; public-source
research is not blocked. Unresolved methodological issues remain: automated
profile audit is structural rather than independent historical validation,
source-document identity normalization is provisional, external links are
inventoried rather than exhaustively visited, and most personnel files still
require archival examination.
