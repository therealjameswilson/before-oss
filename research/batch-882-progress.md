# Batch 882 research progress

Date: 2026-10-17 America/New_York

## Scope and source validation

Batch 882 covers NARA index PDF page 431, rows 1-23, from Arthur A
Skiathitis through Clarence W Skupic. All 23 immutable source rows remain
preserved and link to 23 active person entities. The table was checked against
layout-preserving extraction and a rendered page image. Printed names,
initials, protected identifier columns, Box 716 and archive location
230/86/40/07 remain recoverable. The printed notes R. Norw and Norwegi remain
literal and are not silently expanded. Full service and officer numbers remain
private.

The rendered page establishes the next unresearched boundary as page 431, row
24, Peter J Skurla.

## Research outcomes

- Norsk Industriarbeidermuseum documents Einar Skinnarland as an engineer at
  the Møsvatn dam and later in Mårvatn dam construction. Its chronology
  directly links leaving the latter work on 15 March 1942 with travel to
  Britain and entry into Norwegian Independent Company No. 1. The Mårvatn work
  site is published as his high-confidence explicit immediate affiliation.
  Because the source does not name the legal employer, both dam relationships
  are modeled as relationship unknown and do not increase employer coverage.
- The U.S. Army Special Operations history office confirms Frank J Skokoski's
  OSS identity and places his 79th Infantry Division medic assignment before
  his 541st Parachute Infantry Regiment service, which immediately preceded
  OSS BARDSEA. Both are published as military assignments, not employment.
- Official CIA and War Department records confirm George P Skouras's OSS
  identity and 1944 civilian service. A contemporary Associated Press report
  documents him as a part owner of a major independent motion-picture theater
  chain in 1940. The theater-chain interest is published at medium confidence
  as the latest identified civilian business affiliation, not as an explicitly
  immediate predecessor or an inferred later corporate name.
- A National Academy memoir documents Folke K Skoog at Harvard and Johns
  Hopkins before wartime government service, while a Columbia University study
  documents Sibilla Skidelsky's Washington Post and New York Sun journalism.
  Neither biography supplies a direct OSS bridge, so both identities remain
  probable; all five affiliations are visibly qualified at medium confidence
  and excluded from default analytics.
- Institutional evidence supports high-confidence identity assessments for
  Selby M Skinner and Erling Skogstad but does not establish a pre-OSS employer
  or assignment sequence. Postwar Emile B Skraly and Stanley J Skuk leads were
  rejected for pre-OSS claims.
- Ten official Army identity candidates were accepted, including documented
  source-name disagreements for Nicholson/Nicholas Skilenes and
  Skokos/SKWKOS. Army-coded fields and protected identifiers remain private
  and were not converted into employers.
- The Hakon A Skjolsvik row shares a protected identifier with H Skgolsvik on
  page 430, while the official Army file supplies a third unrelated name.
  Both index entities remain separate in a visible duplicate group, the Army
  candidate is rejected, and joint Box 716 review is required.
- Targeted official, institutional, contemporary newspaper, obituary,
  directory and exact-name searches were recorded for all 23 people. Public
  CIA and Library of Congress transport limitations are recorded rather than
  treated as negative findings. No exposed NARA credential was used.

The cohort distribution is three confirmed, eleven high-confidence, two
probable, six unresolved and one conflicting identity. Research status is one
documented prewar employer, two occupation-only outcomes, nineteen archival-
review cases and one conflict. No Batch 882 person remains not started or in
progress, and every person has one saved non-planned research attempt.

The evidence bundle contains eleven sources, nine organizations, nine
affiliations, 26 claims, 23 person updates, 23 research attempts and 47
claim-source links. It contains two confirmed, sixteen high, seven medium and
one conflicting claim. The Army review file contains ten accepted and two
conflicting decisions. Reimporting both files is idempotent. SQLite integrity
is ok and the foreign-key check returns no rows.

## Updated project coverage

- Index coverage: 23,978/23,978 linked source rows (100%).
- Active person entities: 23,937; stored entities: 23,941, including four
  unlinked superseded entities retained for auditability.
- Research-attempt coverage: 13,248 people (55.3453%).
- Verified-employer coverage: 433 people (1.8089%).
- Verified-affiliation coverage: 961 people (4.0147%).
- Archival-review coverage: 11,715 people (48.9410%).
- Not started: 10,684 people; in progress: 1,893 people.
- Possible duplicate groups: 585.
- Conflicts: 460 people.
- Claim confidence totals: 1,625 confirmed, 4,258 high, 1,741 medium, 212 low,
  388 conflicting and two unresolved.
- Citations: 6,668; unique source documents: 3,629.
- Public projection: 23,937 people, 2,919 affiliations, 1,098 organizations,
  5,424 sources and 8,008 published or qualified claims.
- Private derived exports: 2,940 affiliations, 1,112 organizations, 6,668
  sources, 26,921 research attempts, 23,615 NARA pull-list rows and 22,019
  unresolved rows.

Relative to Batch 881, research-attempt and archival-review coverage each
increased by 23 people. Verified-employer coverage is unchanged. Verified-
affiliation coverage increased by two. Nine affiliations, six canonical
organizations, eleven public sources and 26 public claims entered the public
projection.

## Validation

The evidence imports, idempotency reimports, SQLite integrity check,
foreign-key check, regenerated coverage report, public-data build and
stratified 200-profile audit pass. All 145 Python tests and 81 parameterized
subtests pass. Astro reports zero errors, warnings or hints across 513 source
files and builds 25,080 pages. The bounded release suite passes 90/90 checks:
21 Batch 882 tests across desktop, phone and tablet, 33 core responsive tests,
six analysis tests and 30 axe scans with no serious or critical violations.
All 25,080 internal HTML routes resolve.

The identifier audit checks 12,926 normalized private identifiers and 120
formatted variants across 25,152 artifacts, rejects 1,337 candidate
substrings as non-boundary coincidences, recognizes two allowed aggregate
coincidences and finds zero unexpected matches. The public manifest verifies
67 assets and 118,015,204 bytes at SHA-256
529349e4558c79ceb3479fa736bdcb115b887f035a0f7309beb8197815ea48aa.
Two consecutive builds reproduce output-tree SHA-256
002271f5d4bb2786de88cd3da19b32ad65a6aca3e9b96f3e1e8015c348ab57eb.
The dependency audit reports zero vulnerabilities.

## Publication status

The locally verified Batch 882 release candidate is not a public release until
its immutable content commit passes GitHub's clean Linux Test workflow, the
Pages workflow completes, and the unauthenticated verifier matches that exact
commit.

## Resume commands

Run the standard assign-page-batch, review-decision import, reviewed-evidence
import, adapter-checkpoint export, derived export, public build, coverage
report, profile audit, Python tests, Astro build, bounded browser suite, link
check, deployed-release verification, identifier audit and tree-hash commands
documented in README.md. The Batch 882 inputs are:

- research/army_review_decisions_2026-10-17_batch882.csv
- research/evidence-page431-skiathitis-skupic-review_batch-882_2026-10-17.json

## Current blocker

Authenticated NARA Catalog API research remains disabled until the API key
previously exposed in conversation is rotated and supplied through a local
environment or repository secret. This does not block publication or research
through official public sources and other configured adapters.
