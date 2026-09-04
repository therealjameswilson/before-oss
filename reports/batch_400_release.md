# Batch 400: reviewed outcomes and pending release

This checkpoint follows the successfully published and live-verified Batch
399 release. It contains ten individually adjudicated personnel profiles,
not ten successful employer identifications.

## Evidence changes

- Preserve the index spelling Louis Y. Charter; add the identifier-backed
  Army spelling Chartier separately. Publish the broad Lawyers and judges
  occupation as qualified and temporally uncertain, without an employer.
- Confirm only James C. Charr's exact Army record match. Preserve the
  institutional chronology/birth-year discrepancy as a visible conflict;
  hold the Army occupation pending the pre-OSS timing question.
- Keep the Chartrand missionary and Alston Chase academic biographies as
  low-confidence review candidates, excluded from public claims.
- Preserve six unresolved identities with individual Box 119 questions.
- Retain eleven citations, seven claims, twenty claim-source links, one
  affiliation, ten person updates, and ten durable research attempts.
  Reimporting the bundle does not add duplicate records.

## Exact local coverage

| Measure | Count / denominator | Percent |
|---|---:|---:|
| Index coverage | 23,978 / 23,978 source rows | 100.0000% |
| Research attempted | 3,783 / 23,940 active people | 15.8020% |
| Verified affiliation | 485 / 23,940 active people | 2.0259% |
| Verified employer | 211 / 23,940 active people | 0.8814% |
| Archival disposition assessed | 3,736 / 23,940 active people | 15.6057% |

23,941 stored person rows include one retained superseded entity. There are
233 possible duplicate groups; 2,228 commissioned classifications, 5,617
noncommissioned classifications, and 16,095 indeterminate classifications.

Saved status counts: not_started 20,157; in_progress 46; candidate_found 1;
needs_identity_review 106; needs_temporal_review 9; verified_employer_found
207; documented_prewar_employer_found 68; occupation_only_found 626;
conflicting_sources 69; no_reliable_result_after_protocol 82;
requires_archival_review 2,449; completed 120. An archival disposition is not
a claim that the physical file was examined.

All-claim confidence counts: confirmed 917; high 1,153; medium 820; low 57;
conflicting 81. Employment/self-employment claim rows specifically: confirmed
35; high 270; medium 83; low 0; conflicting 2; unresolved 0. These are claim
rows, not the number of verified people.

Citation records: 3,711. Legacy document keys: 1,734. Distinct non-null source
URLs: 1,258. The source-identity audit documents why these are not yet a
certified count of unique historical items. No citations have been merged or
deleted to improve that count.

## Checks at this checkpoint

- 82 Python unittest tests pass; SQLite integrity and foreign keys pass.
- The deterministic 200-profile structural/stratified audit passes.
- All 15 new browser cases pass after correcting the test-only selectors;
  the complete 1,620-case suite is running and remains a release gate.
- Astro diagnostics: zero errors, warnings, and hints; 24,450 static pages.
- All internal targets resolve; 49,551 external URLs were inventoried.
- Ten of eleven citation URLs returned HEAD 200; the Korean award page's
  automated HEAD 403 is recorded separately from its readable browser text.
- All 67 manifest assets match sizes/hashes; 83,181,118 public bytes.
- Consecutive public exports and production builds are identical. Hashes are
  recorded in the link report.
- The identifier scan finds zero unexpected boundary matches across 24,522
  production artifacts. No authenticated NARA request was made.

The npm advisory endpoint was unavailable in the immediately preceding audit;
no current vulnerability count is asserted. Dependencies are unchanged.

## Remaining release gates and research issues

Do not merge or deploy until the full current browser matrix and required
GitHub checks succeed. Verify the deployed manifest and profile routes after
publication. The public site still contains Batch 399 at this checkpoint.

The broader goal is incomplete: 20,157 people remain unstarted, 468 older
occupation-only temporal labels require individual review, and document-key
normalization remains open. Live NARA API work needs a rotated key configured
outside source control; public-source research can continue independently.

Resume the current validation jobs before starting duplicate runs. A fresh
rebuild can use `scripts/rebuild-all.sh`; a focused browser regression is
`cd site && npx playwright test tests/batch400.spec.ts`.
