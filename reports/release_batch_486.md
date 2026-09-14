# Batch 486 release report

Run: 2026-09-13 UTC

## Scope

Batch 486 preserves and researches ten source rows on personnel-index PDF
page 96, rows 24-33: Marjorie L Cox through Maryette A Coxe. All ten rows are
in Box 150 at archival location 230/86/29/03.

The next unprocessed row is page 96, row 34, Jean L Coyat, Box 151.

## Research outcomes

- Russell C Cox has an exact private-identifier and name match in the complete
  official Army merged-file scan. The Army record establishes enlisted status,
  entry on 19 March 1943 and occupation code 992, Students. The public record
  presents this as qualified student status, not as an employer or an
  immediate pre-OSS affiliation.
- Henry B Coxe is a high-confidence identity and commissioned Army officer.
  Official CIA sources establish his OSS/Jedburgh role. A contemporary 1939
  appellate case identifies him as an attorney of Barratt Coxe. That
  relationship is published at medium confidence as documented prewar
  employment only; it is not labeled immediate or last civilian employment.
- Maryette A Coxe is a high-confidence civilian identity. The official OSS War
  Report identifies her as a contributor and checker. A 1936 directory gives
  no occupation; a 1946 teacher listing is postwar and is excluded from
  pre-OSS employment evidence.
- Norwood S Cox remains a visible identity conflict because the printed private
  identifier belongs to a different Army name. The unrelated person's details
  remain private.
- Marjorie L Cox, Miriam Cox, Nellie P Cox, Richard D Cox, Robin L Cox Jr and
  William N Cox remain unresolved after the minimum online research protocol.
  Their indexed personnel files are routed for archival review.
- Thirteen Library of Congress candidates were opened in official OCR context
  and rejected with recorded reasons. A 1942 Liberty Mutual Insurance lead for
  a William N Cox remains unlinked because no identifier, OSS or Box evidence
  connects that namesake to this source row.

No employer was inferred from occupation, education, a postwar record or a
name-only match.

## Exact coverage after import

| Measure | Count | Denominator | Coverage |
| --- | ---: | ---: | ---: |
| Index rows preserved and linked | 23,978 | 23,978 | 100.0000% |
| Active person entities | 23,940 | — | — |
| Research attempted | 4,629 | 23,940 | 19.3358% |
| Verified affiliation found | 530 | 23,940 | 2.2139% |
| Verified employer found | 235 | 23,940 | 0.9816% |
| Archival disposition assessed | 4,584 | 23,940 | 19.1479% |
| Not started | 19,311 | 23,940 | 80.6642% |

The two new Batch 486 affiliations are medium confidence, so they do not
increase the confirmed/high verified-affiliation or verified-employer counts.

Published data now contains 1,810 affiliations, 3,128 sources, 3,653 claims,
4,294 citations and 1,964 unique source documents. Claim-confidence totals are
1,104 confirmed, 1,365 high, 1,085 medium, 102 low and 102 conflicting.
Ninety-five conflicts and 238 possible-duplicate groups remain visible.

Terminal and active research-status counts:

| Status | Count |
| --- | ---: |
| candidate_found | 7 |
| completed | 133 |
| conflicting_sources | 89 |
| documented_prewar_employer_found | 90 |
| in_progress | 44 |
| needs_identity_review | 203 |
| needs_temporal_review | 15 |
| no_reliable_result_after_protocol | 82 |
| not_started | 19,311 |
| occupation_only_found | 833 |
| requires_archival_review | 2,912 |
| verified_employer_found | 221 |

## Validation

- PDF ingest audit: 522/522 pages processed, 23,978/23,978 rows linked, and all
  32 parser warnings visually resolved.
- Python: 94/94 tests passed.
- Focused browser QA: 15/15 checks passed across desktop, phone and tablet.
- Accessibility: 27/27 isolated axe checks passed across the same viewports.
- Astro: 110 source files checked with zero errors, warnings or hints.
- Production build: 24,508 HTML pages and 24,580 artifacts.
- Link audit: all 24,508 internal HTML pages resolve; 49,776 unique external
  URLs were inventoried.
- Identifier audit: 12,926 normalized identifiers, 120 formatted variants,
  1,095 candidate substrings and zero unexpected boundary, aggregate or
  manifest matches across 24,580 artifacts.
- Stratified profile audit: all seven checks passed across 200 profiles.
- Two clean builds were byte-identical. The 70-file public-tree digest is
  9a0363679f752b7a8672935905c9b9c788ba6a8e559d3594cf9228d8e47021c0.
  The 24,580-file production-tree digest is
  d39fe25fab649c3708f477ccbabc0972612b14619044f36c0c5c363ed6ed919b.
  The 67-file public manifest covers 89,276,473 bytes and has digest
  9f73384e93abfbd61c6e72bc950bbbe1f5640f98e40ef4d5d6cdf8ecc3569b9f.

## Release boundary

This batch is a validated local release candidate. It has not been pushed or
deployed. No authenticated NARA Catalog request was made. The research goal
remains active because 19,311 person entities have not yet started the
research protocol.
