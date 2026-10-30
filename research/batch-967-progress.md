# Batch 967 research progress

Date: 2026-10-30

Scope: NARA OSS personnel index PDF page 474, rows 1-23 (Robert E True
through Ernest Tsikerdanos)

Boxes: 786-787

Archive location: 230/86/42/03

## Extraction and identity safeguards

- Visually audited index page 474 at 200 dpi and preserved all 23 researched
  rows as 23 separate people.
- Accepted six protected-identifier Army identity bridges: Joseph Trunecek,
  John F Trutza, Yueh C Tsai, Ioannis E Tsankaris, Eleftherius Tsantes and
  Ernest Tsikerdanos. Dated Army occupations are published only as qualified
  occupation evidence, never as invented employers.
- Rejected the protected-identifier candidate for Charles V Trupia because it
  names a different person. None of that candidate's biographical fields were
  transferred.
- Protected identifiers were used only for private identity resolution. No
  full identifier, API credential, live API response or raw Army row appears
  in the evidence bundle, public data or downloads. No authenticated NARA
  Catalog API request was used.

## Reviewed outcomes

- Authoritative Danish sources document Svend Truelsen's work for the Danish
  Agricultural Council and his immediate wartime intelligence-network
  affiliation. His Ministry of Agriculture assignment remains a separate
  government relationship.
- University of California evidence documents Robert C Tryon's Berkeley
  employment as both his immediate affiliation and last civilian employer.
- Direct or authoritative evidence supports qualified military pathways for
  Ralph Truex, Shirly Trumps and Ernest Tsikerdanos. A direct OSS document
  bridges Eleftherius Tsantes to the variant Terry/Eleftherios Tsantes.
- Frieda B Tryon's University of North Carolina parenthetical is preserved as
  a professional affiliation, not silently converted into employment.
- Jerry Truhlar and Jerry Truhler remain separate people within their existing
  possible-duplicate group. Charles V Trupia remains conflicting; seven other
  unbridged or incomplete identities retain archival-review outcomes.

## Exact batch outcome

- People researched: 23.
- Terminal statuses: 2 `verified_employer_found`; 12
  `occupation_only_found`; 8 `requires_archival_review`; 1
  `conflicting_sources`.
- Identity statuses: 4 `confirmed`; 8 `high_confidence`; 3 `probable`; 1
  `ambiguous`; 1 `conflicting`; 6 `unresolved`.
- Evidence imported: 19 sources, 10 organization input records, 18
  affiliations, 34 claims, 75 claim-source links, 23 person updates and 23
  research attempts.
- Review decisions imported: 6 accepted and 1 rejected.
- Batch claim confidence: 4 confirmed; 17 high; 13 medium.
- The deterministic evidence bundle SHA-256 is
  `98dc4ee8244508de1f8d924d64c6945cdc39c6b3b7ce27ce4805f00726291276`.

## Exact post-import coverage

- Index coverage: 23,978 / 23,978 linked rows (100.0000%).
- Active people: 23,936.
- Research-attempt coverage: 15,177 / 23,936 (63.4066%).
- Verified-affiliation coverage: 1,092 / 23,936 (4.5622%).
- Verified-employer coverage: 488 / 23,936 (2.0388%).
- Archival-review coverage: 13,653 / 23,936 (57.0396%).
- Not started: 8,754 people; in progress: 1,883 people.
- Durable research attempts or plans: 29,395.
- Possible-duplicate groups: 664.
- Conflicts: 520.
- Claim confidence: 1,704 confirmed; 5,057 high; 2,383 medium; 254 low;
  433 conflicting; 2 unresolved.
- Public projection: 23,936 profiles; 3,712 affiliations; 1,250
  organizations; 6,216 sources; 9,573 published, qualified or conflict claims.
- Private projection: 3,738 affiliations; 1,265 organizations; 7,500 sources;
  21,432 unresolved rows and 23,569 archival pull-list rows.
- Citations: 7,500 across 4,164 unique source documents.

## Verification

- SQLite integrity and foreign-key checks passed after the durable import.
- Evidence and review-decision imports are idempotent on repeated import.
- All 147 Python pipeline tests passed.
- The 200-profile stratified audit passed every check.
- Astro checked 598 files with zero diagnostics and generated 25,236 static
  pages.
- All 27 Batch 967 browser checks passed across desktop, phone and tablet.
- The bounded release suite passed all 96 browser and accessibility checks,
  including 30 axe scans with no serious or critical violations.
- All internal links across 25,236 HTML files resolve; 52,030 unique external
  URLs were inventoried for the separate live check.
- The public identifier audit inspected 1,419 candidate substrings and found
  zero unexpected boundary matches.
- The local public manifest verified all 67 assets totaling 129,429,255 bytes;
  its SHA-256 is
  `da825849226190445d9a225a987e216ac252bf76bc815f547a486d87b7f17153`.
- The known older replay gap disclosed in Batch 959 remains open: 473
  pre-Batch-959 person-status changes are not yet represented in durable replay
  inputs. Batch 967 itself is replayable and idempotent.

## Resume point

Continue with PDF page 474, row 24, **Michalis Tsirmulas**, Box 787, archive
location 230/86/42/03.

## Publication verification

- Immutable public content commit:
  `d44e77e0a557c86c5939e8ecd4790ade0e1f8ac9`.
- GitHub Test run `41002440604` passed.
- GitHub Pages run `41002440687` passed.
- The unauthenticated deployed-release verifier matched all 67 manifest assets,
  eight core routes, 42 source-register pages and all 23 Batch 967 profiles to
  the immutable content commit.
- Public site: <https://therealjameswilson.github.io/before-oss/>.

