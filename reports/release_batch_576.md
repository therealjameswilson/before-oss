# Batch 576 public release verification

Verified 2026-09-19 UTC. Pull request
[#275](https://github.com/therealjameswilson/before-oss/pull/275) passed Test
run 35464527023 and merged as
`35c75c141ca2bf42461a4f3b387525fa2373aa33`. The merged-branch Test
run 35464887846 and Pages run 35464887847 both succeeded.

The unauthenticated, read-only verifier checked the live
[Before OSS site](https://therealjameswilson.github.io/before-oss/) against
the immutable merge commit: all 67 public-manifest assets (95,995,847 bytes),
all seven core routes, and ten new direct profile URLs matched. Manifest
SHA-256: `00806441dd8b863f958c9c2e699338cac526ac6ea6890f44ef1d18f2628f4a69`.
Two consecutive local production builds produced the same 24,693-file tree
hash, `5335159e7b1327d156be94ec84d01e212a97de76402d718762d6edf7fd299a71`.
This tests repeated static output; it is not a complete clean-source replay
of the entire private research database.

## Research and release counts

| Measure | Exact count |
| --- | ---: |
| Printed source rows linked | 23,978 / 23,978 |
| Active cautious person entities | 23,940 |
| People with saved non-planned research attempts | 5,524 (23.0744%) |
| People with verified employers | 261 (1.0902%) |
| People with archival disposition assessed | 5,479 (22.8864%) |
| Active people not started | 18,416 |
| Possible-duplicate groups | 256 |
| Private durable attempts | 10,035 |
| Claim confidence: confirmed / high / medium / low / conflicting | 1,307 / 1,743 / 1,353 / 183 / 129 |
| Public affiliations / organizations / sources / claims | 2,163 / 673 / 3,675 / 4,528 |

The ten Batch 576 people receive terminal `requires_archival_review` outcomes
with no newly assigned employer. Ronnie A DeVico and Gordon D Devins have
high-confidence Army identity links, not employer claims. The Peter P Devivi
Army-name conflict and Robert C Devilbiss trade-paper lead remain unresolved.
The source-level rationale, rejected candidates, and archived query outcomes
are in `research/batch-576-discovery-checkpoint.md` and its reviewed evidence
bundle. The private Army review queue now routes 196 spacing-only and 1,176
substantive name conflicts separately without resolving either automatically.

The [oil-company category](https://therealjameswilson.github.io/before-oss/people/?featured=oil_companies&sort=name_asc)
remains prominent at the top of the site. It lists seven people documented
as employees of nine historically named oil companies in the current
research; this is not an exhaustive OSS oil-industry census.

## Quality checks and remaining work

- `validate-ingest`: all 522 PDF pages represented; 23,978 rows and all
  parser, warning-row, visual-review and SQLite checks pass.
- Python unittest: 98/98 pass. The 200-profile structural audit passes all
  seven checks. Public-identifier audit: zero unexpected boundary matches
  across 24,693 production artifacts.
- Static build: 24,621 direct HTML pages, zero Astro diagnostics. All
  internal links resolve; 50,087 unique external URLs were inventoried but
  not comprehensively visited.
- Bounded release suite: 69/69 pass across desktop, phone and tablet,
  including 27 axe accessibility checks. The full historical Playwright suite
  is not part of this bounded gate; its test-discovery Node heap scaling
  problem remains documented.

Resume at PDF page 116 row 17 with bounded official, exact-name, employment
and archival checks. The authenticated NARA Catalog adapter still requires a
local `NARA_API_KEY` at runtime; the key is neither committed nor included in
public assets. Many unresolved profiles require physical personnel-file
review. The overall goal remains active because 18,416 people still have
`not_started` status; issuing an automated query alone cannot close them.
