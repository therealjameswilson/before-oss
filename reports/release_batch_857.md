# Batch 857 release report

Date: 2026-10-16

## Release contents

- NARA index PDF page 418, rows 24-46: 23 separately preserved and reviewed
  source rows, from Catherine C Seerley through Max Seitelman.
- 23 saved terminal outcomes: one `verified_employer_found`, one
  `documented_prewar_employer_found`, one `occupation_only_found`, two
  `completed` and 18 `requires_archival_review`.
- One confirmed, 13 high-confidence, one ambiguous and eight unresolved
  identities.
- Eleven sources, seven organizations, seven affiliations, 22 published
  claims, 23 person updates, 23 research attempts and 46 claim-source links.
- Manuel Segal's National Broadcasting Company sound-effects work as last
  civilian employment, separated from the unresolved immediate predecessor.
- Fumiko Segawa's explicit WAAC-to-OSS military pathway and Francis Seidler's
  7th Photographic Intelligence Detachment-to-OSS pathway, neither
  misclassified as civilian employment.
- Gerhart Seger's earlier Neue Volkszeitung editorship and Francis Seidler's
  earlier Austrian Federal Chancellery assignment, both kept temporally
  qualified.
- David Seiferheld's medium-confidence nonprofit roles and unnamed
  textile-executive occupation, without inventing a paid employer.
- Eleven official Army identity bridges based on nonshared protected
  identifiers; coded Army fields are not published as employers or
  affiliations.
- Two Robert N Seiple rows remain separate in an opaque possible-duplicate
  group because their private identifiers differ.

## Data gates

- SQLite integrity check: `ok`.
- SQLite foreign-key check: zero rows.
- Batch `not_started`: zero; all 23 people have non-planned research attempts.
- Evidence-bundle validation: 11 sources, seven organizations, seven
  affiliations, 22 claims, 23 person updates, 23 attempts and 46 claim-source
  links.
- Public projection: 23,978 source rows, 23,937 people, 2,846 affiliations,
  1,062 organizations, 5,252 sources and 7,669 published claims.
- Research-attempt coverage: 12,680/23,937 people (52.9724%).
- Verified-employer coverage: 418/23,937 people (1.7463%).
- Verified-affiliation coverage: 920/23,937 people (3.8434%).
- Archival-review coverage: 11,147/23,937 people (46.5681%).
- Remaining `not_started`: 11,252 people.
- Public redaction checks: passed.

## Software and publication gates

- Python: 145 tests passed.
- Astro: 491 files checked with zero errors, warnings or hints; 25,043 pages
  built.
- Bounded Playwright release suite: 93/93 passed across desktop, phone and
  tablet.
- Stratified profile audit: 200/200 profiles passed all integrity checks.
- Internal link check: 25,043 HTML files, zero broken internal links; 51,379
  external URLs inventoried for separate live review.
- Identifier audit: 12,926 normalized private identifiers, 120 formatted
  variants and 25,115 artifacts checked; zero unexpected boundary matches.
- Public manifest: 67 assets, 115,935,683 bytes, SHA-256
  `8f6e0a80a50c95a486f046108ed323c3abb6cde3ad6532748fae3cc817d374fd`.
- Deterministic production build: two 25,115-file builds matched at SHA-256
  `69dae9dd476b512190341408b3746423acdfccbf89ad202d8c2b47d776c46b91`.

## Publication state

The reviewed content is ready to publish. The content commit, GitHub Pages and
Test workflow run identifiers, and unauthenticated immutable-release check will
be recorded after deployment completes.
