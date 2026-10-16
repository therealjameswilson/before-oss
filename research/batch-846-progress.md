# Batch 846 research progress

Date: 2026-10-16 America/New_York

## Scope and source validation

Batch 846 covers the 23 printed personnel rows on NARA index PDF page 413,
rows 1-23, from William H. Schmagel through William J. Schmidt. All 23
immutable source rows remain preserved and linked to 23 separate active person
entities. The rendered page was visually reviewed at 180 dpi. That review
confirmed the literal, apparently truncated notes `ASN is n` for Horace W.
Schmahl and `Consulta` for Erich F. Schmidt; neither has been silently expanded.
Full service identifiers remain private. The next unassigned boundary is PDF
page 413, row 24.

## Research outcomes

- A Reagan Presidential Library copy of *Who Was Who in America* identifies
  **Adolph William Schmidt** as an officer of Mellon National Bank and affiliated
  organizations from 1929 to 1942, immediately before Army service. Mellon
  National Bank is published as his last civilian employer before military
  service, with high confidence. His Columbia Radiator Company and Pittsburgh
  Coal Company directorships are published separately as professional
  affiliations rather than employers.
- A University of Michigan research edition links **Horace W. Schmahl** to the
  Naturalization Control Unit in the U.S. Attorney's Office for the Southern
  District of New York before his wartime intelligence work. The dated federal
  work is published as a qualified, documented prewar government assignment;
  the evidence does not establish it as his immediate pre-OSS affiliation.
  The edition's broader disputed historical interpretation is not adopted.
- A retrospective family obituary identifies **William Herman Schmagel** as
  the indexed sergeant and describes Signal Corps radio training followed by
  Air Corps radio-and-code instruction before his OSS assignment. Those stages
  are published as qualified military assignments, not civilian employment.
  The source does not name the Minneapolis business college he attended, so no
  school or civilian employer is invented.
- Protected official Army crosswalks support eight high-confidence identity
  matches: Alexander P. Schmalz, Edwin Schmidt, Erling P. Schmidt, Eugene V.
  Schmidt, Everett G. Schmidt, Frank Schmidt, Jack C. Schmidt and Joseph L.
  Schmid. The Army forms' omission of Jack Schmidt's middle initial and addition
  of `Jr.` to Joseph Schmid are retained as variants rather than silent
  corrections. Full identifiers, coded occupations and raw Army rows remain
  private and are not used to infer employers.
- Twenty-four Library of Congress candidate items were reviewed in page or OCR
  context and rejected as namesakes, wrong-initial matches, relatives, postwar
  material or inaccessible OCR. Three timed-out searches remain access
  failures, not negative evidence. CIA automated access failed closed under the
  source's robots policy. NARA Catalog API research remains disabled pending
  safe credential rotation.

The batch identity distribution is 11 `high_confidence` and 12 `unresolved`.
Research status is 22 `requires_archival_review` and one
`verified_employer_found`. The evidence bundle contains five source inputs, six
organization inputs, six affiliations, 17 claims, 23 person updates, 23 manual
research attempts and 28 claim-source links. Fourteen new claims are high
confidence and three are medium confidence and visibly qualified. Evidence and
review-decision replay produced no duplicates. SQLite's foreign-key check
returned no rows and integrity check returned `ok`.

## Updated project coverage

- Index coverage: 23,978/23,978 linked source rows (100%).
- Active person entities: 23,937; stored entities: 23,941, including four
  superseded entities retained for auditability.
- Research-attempt coverage: 12,433 people (51.9405%).
- Verified-employer coverage: 408 people (1.7045%).
- Verified-affiliation coverage: 897 people (3.7473%).
- Archival-review coverage: 10,898 people (45.5278%).
- Not started: 11,499 people.
- Possible duplicate groups: 559.
- Conflicts: 443 people.
- Claim confidence totals: 1,588 confirmed, 3,872 high, 1,680 medium,
  202 low, 373 conflicting and two unresolved.
- Citations: 6,393; unique source documents: 3,413.
- Public projection: 23,937 people, 2,807 affiliations, 1,036 organizations,
  5,163 sources and 7,509 claims.

## Validation

Local release validation passed. Python reports 145/145 passing tests plus 81
passing subtests. Astro checked 480 files with zero errors, warnings or hints
and built 25,016 static pages. The bounded Playwright release suite passed
87/87 checks across Batch 846, core routes, analytics and accessibility at
desktop, phone and tablet viewports. The stratified 200-profile audit passed
every check. All internal links across 25,016 HTML files resolve; 51,295 unique
external URLs were inventoried separately. The public-identifier audit found
zero unexpected boundary matches after checking 12,926 normalized identifiers
and 120 formatted variants across 25,088 built artifacts. The public manifest
covers 67 assets totaling 114,889,466 bytes with SHA-256
`483af74b3dc9f2fe58dfd3bc878d3accf138f95594c7f222e353af7b4d1884b3`.
Two production builds produced the identical 25,088-file tree hash
`2e6c7b57b240d08e0a774c06715ac964ad30de19fcc16a95fc2a7fc74f4f3d14`.

## Publication status

Candidate release validated locally; publication and immutable unauthenticated
verification are pending. Public URL after a successful GitHub Pages deployment:
https://therealjameswilson.github.io/before-oss/.
