# Batch 845 research progress

Date: 2026-10-16 America/New_York

## Scope and source validation

Batch 845 covers the 23 printed personnel rows on NARA index PDF page 412,
rows 24-46, from Marcus A. Schillace through Claymer Schluter. All 23
immutable source rows remain preserved and linked to 23 separate active person
entities. The rendered page was visually reviewed at 180 dpi. That review
confirmed the indexed forms `Schlickenmaie` and `Claymer`, the A-prefixed
private identifier for Aline B. Schletter, and the unusual nine-digit private
identifier on the Frederick C. Schlein row. Full identifiers remain private.
The next unassigned boundary is PDF page 413, row 1.

## Research outcomes

- An authoritative National Park Service history identifies **Robert
  Schlangen** in the June 1942 Advanced OSS Special Operations class and says
  that he came from the State Department. The State Department is therefore
  published as his immediate pre-OSS government assignment, not as a private
  employer or last civilian employer.
- Official OSS sources identify **Reeve Schley Jr.** as the indexed Captain.
  A family death notice supplies a qualified pre-OSS U.S. Cavalry assignment
  at Fort Riley. His father's Chase banking career is explicitly excluded and
  no civilian employer is assigned to the son.
- Existing official evidence for **Arthur M. Schlesinger Jr.** remains the
  authority for his immediate Office of War Information assignment. A
  contemporary 1940 item adds scholar-and-author context only; Harvard is not
  silently converted into an employer, and the Harvard Society of Fellows
  remains a professional affiliation.
- Institutional records make **Edmond Robert Schlesinger** a probable match
  to the indexed Edmond Schlesinger. The result is published only as qualified
  identity context. Cornell, journalism and any other employer remain
  unassigned pending Box 683 and NYPL file review.
- A direct 1949 CIA memorandum confirms the distinctive **Claymer Schluter**
  identity in OSS, CIC Germany and SSU context. Because the document is
  post-OSS, it supports identity continuity only and is not used to infer a
  pre-OSS affiliation.
- Protected official Army crosswalks support ten high-confidence identity
  matches: Adrian A. Schlaht, Arthur M. Schlesinger Jr., Charles J. Schimpf,
  Francis J. Schlack, Hollis R. Schilt, James C. Schindler, Marcus A.
  Schillace, Stuart B. Schimmel, indexed Herbert W. Schlickenmaie, and indexed
  Louis A. Schlafani. `Schlickenmaier` and `Sclafani` are retained as source
  variants rather than silent corrections. Full identifiers, coded
  occupations and raw Army rows remain private.
- The Army rows associated with protected identifiers for **Peter F.
  Schinchirimini** and **Frederick C. Schlien** print materially different
  names. Both public profiles expose the conflict without publishing either
  alternate name, identifier or occupation code.
- LoC completed all 23 bounded searches and produced two Arthur Schlesinger
  candidates: the 1940 occupation-context item was accepted and a 1963
  postwar roundup was rejected. CIA automated access failed closed under the
  source's robots policy and is recorded as an access limitation, not as
  negative evidence. NARA Catalog API research remains disabled pending safe
  credential rotation.

The batch identity distribution is 13 `high_confidence`, one `probable`, two
`conflicting`, and seven `unresolved`. Research status is 19
`requires_archival_review`, two `conflicting_sources`, one `completed`, and one
`verified_employer_found` from Arthur Schlesinger's existing reviewed record.
The evidence bundle contains ten source inputs, two reused canonical
organizations, two affiliations, 18 claims, 23 person updates, 23 manual
research attempts, and 36 claim-source links. Fourteen new claims are high
confidence and published, two are medium and visibly qualified, and two are
conflicting. Evidence and review-decision replay produced no duplicates.
SQLite's foreign-key check returned no rows and integrity check returned
`ok`.

## Updated project coverage

- Index coverage: 23,978/23,978 linked source rows (100%).
- Active person entities: 23,937; stored entities: 23,941, including four
  superseded entities retained for auditability.
- Research-attempt coverage: 12,410 people (51.8444%).
- Verified-employer coverage: 407 people (1.7003%).
- Verified-affiliation coverage: 896 people (3.7432%).
- Archival-review coverage: 10,875 people (45.4318%).
- Not started: 11,522 people.
- Possible duplicate groups: 559.
- Conflicts: 443 people.
- Claim confidence totals: 1,588 confirmed, 3,858 high, 1,677 medium,
  202 low, 373 conflicting, and two unresolved.
- Citations: 6,388; unique source documents: 3,409.
- Public projection: 23,937 people, 2,801 affiliations, 1,033 organizations,
  5,158 sources, and 7,492 claims.

## Validation

Local release validation passed. Python reports 145/145 passing tests plus 81
passing subtests. Astro checked 479 files with zero errors, warnings or hints
and built 25,013 static pages. The bounded Playwright release suite passed
93/93 checks across Batch 845, core routes, analytics and accessibility at
desktop, phone and tablet viewports. The stratified 200-profile audit passed
every check. All internal links across 25,013 HTML files resolve; 51,290 unique
external URLs were inventoried separately. Public-identifier audits of both
the source assets and built site found zero unexpected boundary matches after
checking 12,926 normalized identifiers and 120 formatted variants across
25,085 built artifacts. The public manifest covers 67 assets totaling
114,780,854 bytes with SHA-256
`10f32736b7ffb326eb0c0c62552a31a04c069adb827ae5762f31ec7e9782b407`.
Two production builds produced the identical 25,085-file tree hash
`aa7d17b6b4eddd35cf1a3cb0599e934186d01886dc5650b84537fad5ecbe8684`.

## Publication status

Publication pending. The reviewed data, public projection, regression tests
and local release checks are complete; GitHub Pages and immutable live-release
verification have not yet run for this batch.
