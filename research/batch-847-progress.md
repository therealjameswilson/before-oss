# Batch 847 research progress

Date: 2026-10-16 America/New_York

## Scope and source validation

Batch 847 covers the 23 printed personnel rows on NARA index PDF page 413,
rows 24-46, from Bernadotte E. Schmitt through Joseph W. Schneider. All 23
immutable source rows remain preserved and linked to 23 separate active person
entities. The rendered page was visually reviewed at 180 dpi; names, grades,
serial-number fields, box numbers and archival locations align with the source
table. Full service identifiers remain private. The next unassigned boundary is
PDF page 414, row 1.

## Research outcomes

- A University of Chicago institutional history identifies **Bernadotte E.
  Schmitt** as a member of its history faculty from 1924 through 1946. The
  university is published as both his immediate pre-OSS affiliation and last
  civilian employer before wartime service, with high confidence.
- Official Army crosswalk evidence confirms **Robert J. Schmitz** as the
  indexed person and documents his immediate pre-OSS military pathway through
  the U.S. Army Infantry School and Infantry Officer Candidate School at Fort
  Benning. The assignment is published as military service, not civilian
  employment.
- A Smithsonian institutional source identifies **Stefan A. Schnabel** as a
  member of the Mercury Theatre players before the war. The company is
  published as a documented prewar professional affiliation, not as a verified
  immediate employer.
- A contemporary newspaper account identifies **William G. Schneeflock** as an
  Army Air Corps mechanic recruit. Because the identity and chronology are
  probable rather than conclusive, the military assignment is visibly
  qualified at medium confidence.
- Protected official Army crosswalks support nine additional high-confidence
  identity matches: Charles R. Schmitt, Irving Schmitt, William R. Schmitz,
  Solomon H. Schnaps, Alphonse J. Schneider, Anthony G. Schneider, Franklin Q.
  Schneider, John E. Schneider and Joseph W. Schneider. The Army record's
  addition of `Jr.` to Joseph Schneider is preserved as a variant rather than a
  silent correction. Full identifiers, coded occupations and raw Army rows
  remain private and are not used to infer employers.
- A Columbia University and Moses & Singer candidate for **Henry Schneider**
  was rejected because the evidence does not bridge that namesake to the index
  record. A private roster lead for **Lyle Schneeberger** remains discovery-only
  evidence. Other common-name and incomplete-name cases remain unresolved.
- CIA automated access failed closed under the source's robots policy, and
  Library of Congress timeouts remain access failures rather than negative
  evidence. NARA Catalog API research remains disabled pending safe credential
  rotation.

The batch identity distribution is one `confirmed`, 11 `high_confidence`, one
`probable` and ten `unresolved`. Research status is 22
`requires_archival_review` and one `verified_employer_found`. The evidence
bundle contains eight source inputs, four organization inputs, four
affiliations, 18 claims, 23 person updates, 23 manual research attempts and 34
claim-source links. Evidence and review-decision replay produced no duplicates.
SQLite's foreign-key check returned no rows and integrity check returned `ok`.

## Updated project coverage

- Index coverage: 23,978/23,978 linked source rows (100%).
- Active person entities: 23,937; stored entities: 23,941, including four
  superseded entities retained for auditability.
- Research-attempt coverage: 12,456 people (52.0366%).
- Verified-employer coverage: 409 people (1.7087%).
- Verified-affiliation coverage: 900 people (3.7599%).
- Archival-review coverage: 10,921 people (45.6239%).
- Not started: 11,476 people.
- Possible duplicate groups: 559.
- Conflicts: 443 people.
- Claim confidence totals: 1,590 confirmed, 3,886 high, 1,682 medium,
  202 low, 373 conflicting and two unresolved.
- Citations: 6,401; unique source documents: 3,419.
- Public projection: 23,937 people, 2,811 affiliations, 1,037 organizations,
  5,171 sources and 7,527 claims.

## Validation

Local release validation passed. Python reports 145/145 passing tests plus 81
passing subtests. Astro checked 481 files with zero errors, warnings or hints
and built 25,017 static pages. The bounded Playwright release suite passed
90/90 checks across Batch 847, core routes, analytics and accessibility at
desktop, phone and tablet viewports. The stratified 200-profile audit passed
every check. All internal links across 25,017 HTML files resolve; 51,301 unique
external URLs were inventoried separately. The public-identifier audit found
zero unexpected boundary matches after checking 12,926 normalized identifiers
and 120 formatted variants across 25,089 built artifacts. The public manifest
covers 67 assets totaling 114,994,827 bytes with SHA-256
`91b05def7cff1ebe5f2a2940f63597fa599669e8cd2f88dbeabeaa453a4ae7a9`.
Two production builds produced the identical 25,089-file tree hash
`8996a06b204bee8237bca632939bd827948fc28ba2b23710f93f4d70416e15b5`.

## Publication status

Published. GitHub Pages run 38906576101 deployed content commit
`8ff055a7378c4d730fea57c79c5e4e350e8ab9bb` successfully, and Test run
38906576004 passed the independent pipeline, browser and public-identifier
checks. The immutable unauthenticated verifier matched all 67 public assets
(114,994,827 bytes), the release manifest, eight core routes, 35
source-register pages and all 23 directly affected profile URLs. Public URL:
https://therealjameswilson.github.io/before-oss/.
