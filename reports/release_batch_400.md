# Batch 400 published release verification

Verified 2026-09-04 UTC. Public site:
https://therealjameswilson.github.io/before-oss/

PR 157 was merged at 04:12:07 UTC. Reviewed head:
`05c84de43d58af7057583399344bf37de71ab3dc`; merge commit:
`67c36f86e5bf454d5f1b099d4fa7029a88765c0f`.

## Historical outcomes

Ten profiles were reviewed, not ten employers found. The Louis Y. Charter
index spelling remains intact; the identifier-backed Chartier variant and
qualified Army-entry occupational group are visible. James C. Charr's
official record match is separated from a preserved biographical conflict.
Two promising biographies remain withheld candidates; six people remain
unresolved with individual archival questions. No verified employer was added.

## Validation

- Premerge Test run 33832663156 succeeded: 82 Python tests and all 1,620
  browser cases passed (28.1 minutes).
- The local full matrix initially passed 1,618 of 1,620 cases in 37.3 minutes.
  The two older-profile cases lost their Chromium connection. Both passed
  unchanged in the isolated rerun (4.3 seconds); this is not described as a
  clean first local run.
- Pages run 33835929295 and postmerge Test run 33835929305 both succeeded.
- All 67 deployed manifest assets were fetched and matched size and SHA-256:
  83,181,118 bytes. Seven core routes and ten Batch 400 direct profile routes
  returned HTTP 200 and contained a main element.
- Manifest SHA-256:
  `7b20eac5bee16ec329229055c3f081ffa73426416b234320f67098bf57fe10e2`.
- Two local production builds were identical: 24,522 files, tree digest
  `5424c39459324db120e1f86fc97b299681d5b350c3a53a7a7731b120db714ed2`.
- All 24,450 HTML pages passed internal-link checks. The 49,551 external URLs
  were inventoried, not all individually visited.
- Public identifier, manifest and aggregate checks passed; see the preserved
  Batch 400 section of the link report. No authenticated NARA request was made.

## Exact deployed coverage

| Measure | Numerator / denominator | Percent |
|---|---:|---:|
| Index coverage | 23,978 / 23,978 printed rows | 100.0000% |
| Research-attempt coverage | 3,783 / 23,940 active people | 15.8020% |
| Verified-affiliation coverage | 485 / 23,940 active people | 2.0259% |
| Verified-employer coverage | 211 / 23,940 active people | 0.8814% |
| Archival disposition assessed | 3,736 / 23,940 active people | 15.6057% |

23,941 stored entities include one retained superseded record. There are 233
possible duplicate groups. Commissioned classification: 2,228 yes, 5,617 no,
16,095 unknown. Research statuses: not_started 20,157; in_progress 46;
candidate_found 1; needs_identity_review 106; needs_temporal_review 9;
verified_employer_found 207; documented_prewar_employer_found 68;
occupation_only_found 626; conflicting_sources 69;
no_reliable_result_after_protocol 82; requires_archival_review 2,449;
completed 120.

Claim confidence: confirmed 917, high 1,153, medium 820, low 57, conflicting
81. Employment/self-employment claim rows: confirmed 35, high 270, medium 83,
low 0, conflicting 2, unresolved 0. These are not unique-person counts.
Citation records 3,711; legacy document keys 1,734; distinct source URLs 1,258.
Document-key normalization remains under review; the legacy-key count is not
a certified unique-historical-document count.

The overall goal is incomplete. This fixed report describes Batch 400 only;
later local batches must not be represented as deployed until verified.
