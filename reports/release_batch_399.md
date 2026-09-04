# Batch 399 published release

Verified 2026-09-04 UTC. This report is pinned to the Batch 399 release and
must not be read as the current totals after subsequent imports.

- Public URL: https://therealjameswilson.github.io/before-oss/
- PR: https://github.com/therealjameswilson/before-oss/pull/156
- Reviewed head: `0b4eeb5bba54f42cd70c82fb87ce74f7f725a567`
- Merge: `a416a2422d9a786b5a19748999a8866b8c2b5b2e`
- Required premerge CI: run 33826010891, **success**; 82 Python tests and
  1,605 / 1,605 browser/accessibility cases passed, without a reported retry.
- Pages deployment: run 33828413455, **success**.
- Postmerge Test run 33828413523: **success**, independently checked after
  completion; its outcome is not assumed from the premerge pass.

## Local verification

The full local integration run passed 1,600 cases initially; five older cases
timed out, including three browser-context teardown timeouts. All five passed
in the immediate isolated rerun (4.1 seconds). This is not described as a
clean first run. All new analysis and Batch 399 cases passed initially.

After the whitespace-only chart-caption fix, a fresh production build and
45-case focused/axe suite passed 44 cases initially. The phone sources-page
axe case timed out at 90 seconds, then passed in isolation in 15.7 seconds.
The resulting 45 / 45 unique cases pass; all 27 axe routes/viewports have a
passing result. These local execution timeouts remain documented even though
the independent GitHub suite passed cleanly.

Astro reported zero errors, warnings, and hints; the build contains 24,450
HTML pages and 24,522 total files. Every internal link resolves under the
GitHub Pages base path. The 49,548 external URL inventory is not a claim that
all external destinations were visited.

Two final production builds reproduced sorted-path/content SHA-256 digest
`bef866981d1df5e9a45db6de19ce9cc8d596b229458a60772b7efc66b6efd56a`.
Each digest hashes relative paths, a NUL separator, and binary file hashes.

The full public-identifier audit examined 12,926 normalized identifiers and
120 formatted variants across 24,522 artifacts. It rejected 1,080 substring
coincidences and found zero unexpected boundary matches, zero aggregate false
positives, and zero manifest-size false positives.

## Live verification and coverage

All 67 manifest assets, totaling 83,137,581 bytes, were fetched from GitHub
Pages and matched the local byte sizes and SHA-256 hashes. Manifest hash:
`e0318b0d59442f7291eb4bb5be459e6d47343b2ba5a27a3f7ba18d036093181b`.
Seven core routes and all ten Batch 399 profiles returned successful responses
with page content. A successful deployment is therefore independently checked
against the expected public data, not only the workflow status.

| Coverage | Numerator | Denominator | Percent |
|---|---:|---:|---:|
| Index | 23,978 source rows | 23,978 printed rows | 100.0000% |
| Research attempted | 3,773 people | 23,940 active entities | 15.7602% |
| Verified affiliation | 485 people | 23,940 active entities | 2.0259% |
| Verified employer | 211 people | 23,940 active entities | 0.8814% |
| Archival disposition assessed | 3,726 people | 23,940 active entities | 15.5639% |

Unstarted: 20,167. Conflicting-source profiles: 68. Explicit archival-review
status: 2,443. The reduction in verified affiliations follows the stricter
identity/conflict/temporal gate, not removal of source evidence or profiles.

The dependency advisory service timed out on both recorded attempts. No
current vulnerability count is claimed. No package or lockfile change was
made for this release. NARA API access remains unused; no secret was required
for this static release or the public-source research.
