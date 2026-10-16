# Batch 844 research progress

Date: 2026-10-16 America/New_York

## Scope and source validation

Batch 844 covers the 23 printed personnel rows on NARA index PDF page 412,
rows 1-23, from Henry Scheiber III through Gertrude M. Schiffauer. All 23
immutable source rows remain preserved. A reviewed entity-resolution decision
links the two differently spelled Elwood L. Schexmayder/Schexnayder rows to one
active person, leaving 22 active entities for this batch. The two Stanford L.
Schewel rows and the two Robert M. Schiff rows remain separate, visible
duplicate candidates because name agreement alone is insufficient to merge
them. The next unassigned boundary is PDF page 412, row 24, Marcus A.
Schillace.

## Research outcomes

- A contemporary obituary identifies **Elwood Louis Schexnayder** at high
  confidence and explicitly documents U.S. Army OSS service in Ceylon. The
  obituary's Shell Oil employment occurred after that wartime service, so it
  is excluded from the pre-OSS affiliation data rather than silently moved
  earlier in his chronology.
- Official Army crosswalks support high-confidence identity-only matches for
  **George J. Schell**, indexed **James W. Schenider** (with Schneider retained
  as a documented variant), **Samuel L. Schepps**, **Ludwig R. Scheur**,
  **William O. Schieffelin**, and the numbered **Robert M. Schiff** row. Full
  protected identifiers and coded civilian occupations remain private, and no
  occupation code is converted into a named employer.
- The official Army record associated with **Robert Scheuer**'s protected
  index identifier prints a materially different name. The alternate name,
  protected identifier and coded occupation remain private; the public profile
  reports only the identity conflict and directs research to the indexed
  personnel file.
- The Signal Corps Officer Candidate School Class 10-42 roster documents
  **Alfred D. Schiaffo** graduating at Fort Monmouth on 16 November 1942. With
  no unique identifier or direct bridge from that roster to the OSS index row,
  the match remains probable and visibly qualified rather than promoted to a
  settled identity.
- Contemporary and scholarly postwar records identify a Stanford L. Schewel
  as a U.S. Foreign Service vice consul and economic analyst in Amsterdam.
  They do not securely identify either same-named index row or establish a
  pre-OSS employer, so both index entities remain ambiguous and separate.
- The numbered and unnumbered Robert M. Schiff rows also remain separate. The
  Army identity evidence attaches only to the numbered row and is not copied
  to the unnumbered namesake.
- LoC completed all 23 bounded searches and produced three candidates, all
  rejected after item-level review. CIA automated access failed closed under
  the source's robots policy and is recorded as an access limitation, not as
  negative evidence. NARA Catalog API research remains disabled pending safe
  credential rotation.

The active cohort's identity distribution is seven `high_confidence`, one
`probable`, two `ambiguous`, one `conflicting`, and eleven `unresolved`.
Research status is 21 `requires_archival_review` and one
`conflicting_sources`. The reviewed evidence bundle contains four source
inputs, no organization or affiliation inputs, nine claims, 22 active person
updates, 22 manual research attempts, and 18 claim-source links. Import and
idempotent replay produced identical counts; the seven Army review decisions
and the reviewed Elwood merge also replayed without duplication. SQLite's
foreign-key check returned no rows and integrity check returned `ok`.

## Updated project coverage

- Index coverage: 23,978/23,978 linked source rows (100%).
- Active person entities: 23,937; stored entities: 23,941, including four
  superseded entities retained for auditability.
- Research-attempt coverage: 12,388 people (51.7525%).
- Verified-employer coverage: 407 people (1.7003%).
- Verified-affiliation coverage: 895 people (3.7390%).
- Archival-review coverage: 10,853 people (45.3399%).
- Not started: 11,544 people.
- Possible duplicate groups: 559.
- Conflicts: 441 people.
- Claim confidence totals: 1,588 confirmed, 3,844 high, 1,675 medium,
  202 low, 371 conflicting, and two unresolved.
- Citations: 6,379; unique source documents: 3,402.
- Public projection: 23,937 people, 2,799 affiliations, 1,033 organizations,
  5,149 sources, and 7,474 claims.

## Validation

Local release validation passed. Python reports 145/145 passing tests plus 81
passing subtests. Astro checked 478 files with zero errors, warnings or hints
and built 25,013 static pages. The bounded Playwright release suite passed
93/93 checks across Batch 844, core routes, analytics and accessibility at
desktop, phone and tablet viewports. The stratified 200-profile audit passed
every check. All internal links across 25,013 HTML files resolve; 51,286 unique
external URLs were inventoried separately. The public-identifier audit found
zero unexpected boundary matches after checking 12,926 normalized identifiers
and 120 formatted variants across 25,085 artifacts. The public manifest covers
67 assets totaling 114,677,467 bytes with SHA-256
`47c0cf50967f06fde6eaf79044a5af7aef1eb67c036126cf362154ce272e2efc`.
Two clean builds produced the identical 25,085-file tree hash
`e976a427c7001fb93e4ead6c4a7f66f4e4dbf00128be17189fa2f2fe26cd0bec`.

## Publication status

Published. GitHub Pages run 38888300816 deployed content commit
`48f7443930bf2eed8320b5d15dfcf362543e08cc` successfully, and Test run
38888298899 passed. The immutable unauthenticated verifier matched all 67
public assets (114,677,467 bytes), the release manifest, eight core routes, 35
source-register pages, and all 22 directly affected active profile URLs. Public
URL: https://therealjameswilson.github.io/before-oss/.
