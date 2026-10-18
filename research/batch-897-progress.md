# Batch 897 research progress

Date: 2026-10-18 America/New_York

## Scope and source validation

Batch 897 covers NARA index PDF page 438, rows 24-46, from Henry Sonagere
through Dario Soria. All 23 immutable source rows remain preserved and linked to
23 active person entities. The printed page was checked against layout-
preserving extraction and a rendered page image. Names, initials, ranks,
protected-identifier presence, Box 729 and archive location 230/86/41/02 remain
recoverable. Full protected identifiers remain private.

The source literally prints two separate `Edgar H Sonnanstine` rows. They are
not merged. The protected identifier on the second row points to an Army record
for Brown Owen L, so it remains a conflict and its occupation is not
transferred. Daniel A Sorensen and one Robert W Sorenson row share a protected
identifier in duplicate group `serial-conflict:31326668`; the Army record names
Daniel A Sorenson. Both rows remain separate conflicts. The other Robert W
Sorenson row carries a different protected identifier and remains a separate
unresolved entity.

The next unresearched boundary is page 439, row 1, Gene Sorisi. The page was
rendered and visually checked: the row prints Gene Sorisi, a protected
identifier, Box 730 and archive location 230/86/41/02.

## Research outcomes

- Henry Sonagere is identified at high confidence through a detailed Mariner
  Sands resident profile. The 82nd Airborne Division is published as his
  explicit immediate pre-OSS military assignment. His earlier Detroit
  carpentry training with unnamed uncles is published as an occupation, not a
  firm or last civilian employer.
- Gunnar Sonsteby is identified at high confidence as Gunnar Sønsteby through
  the authoritative Norwegian encyclopedia biography. Gjensidige, Rjukan
  Salpeterfabrikker, an unnamed Oslo audit firm and Milorg remain separate
  relationships. The source documents British SOE recruitment, not a direct
  OSS transfer, and the project does not import Sønsteby's postwar Esso career
  into his pre-OSS history.
- Karl G Sorg's accepted Army bridge remains distinct from his Dartmouth
  student status. The official Army actor/actress category names no employer or
  production. Dartmouth and obituary evidence establish that Army entry in
  1942 interrupted his studies.
- Dario Soria is a probable, not high-confidence, match to émigré businessman
  and broadcaster Dario Pellegrino Soria. Raxor Trading Company, a 1941 food
  venture, Voice of America, CBS and D'Arcy are published only as
  medium-confidence qualified affiliations. None is selected as the immediate
  pre-OSS affiliation or last civilian employer. A Firenze University Press
  statement about OSS cooperation concerns cousin Guido Soria and is not
  misattributed to Dario.
- Official Army protected-identifier bridges for Eddie O Sondeno, Yook L Soo
  Hoo, Salvatore Sorbella/Sorbello, Karl G Sorg and Jack A Sorgenfrei are
  accepted. Their carpenter, student, blacksmith/forgeman/hammerman,
  actor/actress and stock-clerk categories remain qualified occupation evidence
  and identify no institution, employer or workplace.
- The Edgar/Brown and Daniel/Robert identifier conflicts remain visible without
  occupation transfer. The remaining unresolved people receive explicit Box
  729 archival-review outcomes rather than invented employers.

The cohort distribution is seven high-confidence identities, one probable
identity, three conflicting identities and 12 unresolved identities. Research
status is five occupation-only outcomes, one documented-prewar-employer
outcome, three conflict outcomes and 14 archival-review outcomes. No Batch 897
person remains not started or in progress. The batch adds 23 manual research
attempts.

The evidence bundle contains 11 sources, nine organization references, 17
affiliations, 28 claims, 23 person updates, 23 manual research attempts and 54
claim-source links. It contains 14 high-confidence, 11 medium-confidence
qualified and three conflicting public claims. The review file contains five
accepted and five conflicting Army candidate decisions. Reimporting both files
is idempotent. SQLite integrity is `ok` and the foreign-key check returns no
rows.

## Updated project coverage

- Index coverage: 23,978/23,978 linked source rows (100%).
- Active person entities: 23,936; stored entities: 23,941, including five
  superseded entities retained for auditability.
- Research-attempt coverage: 13,588 people (56.7680%).
- Verified-employer coverage: 438 people (1.8299%).
- Verified-affiliation coverage: 976 people (4.0775%).
- Archival-review coverage: 12,059 people (50.3802%).
- Not started: 10,343 people; in progress: 1,889 people.
- Possible duplicate groups: 599.
- Conflicts: 467 people.
- Claim confidence totals: 1,628 confirmed, 4,388 high, 1,835 medium, 212 low,
  395 conflicting and two unresolved.
- Citations: 6,774; unique source documents: 3,688.
- Public projection: 23,936 people, 3,031 affiliations, 1,120 organizations,
  5,530 sources and 8,242 published, qualified or conflict claims.
- Private derived exports: 3,052 affiliations, 1,134 organizations, 6,774
  sources, 27,312 research attempts, 23,611 NARA pull-list rows and 21,943
  unresolved rows.

Relative to Batch 896, research-attempt coverage and archival-review coverage
each increased by 23 people. Verified-affiliation coverage increased by three
and verified-employer coverage by one. Fourteen high-, 11 medium- and three
conflicting claims, 17 public affiliations, six net organizations, 11 public
sources and 28 public claims entered the projection. Citations increased by 11
and unique source documents by seven.

## Validation status

The page assignment, review-decision import, reviewed-evidence import and
idempotency reimports pass in an isolated database and the canonical database.
SQLite integrity and foreign-key checks, regenerated exports, coverage
reporting and public-data redaction pass. The extraction validator accounts for
all 23,978 rows across all 522 PDF pages, and the stratified 200-profile audit
passes all seven checks. All 146 Python tests and 84 parameterized subtests
pass. Astro reports zero errors, warnings or hints across 528 source files and
builds 25,101 static pages. The bounded release suite passes all 96 browser and
accessibility checks across desktop, phone and tablet, including 30 axe scans
with no serious or critical violations. Every internal link resolves. The
private-identifier audit finds zero unexpected matches, all 67 manifest assets
verify locally, the production dependency audit reports zero vulnerabilities,
and two consecutive builds produce identical public and output tree digests.
CI, deployment and unauthenticated verification remain pending release gates.

## Resume inputs

- `research/army_review_decisions_2026-10-18_batch897.csv`
- `research/evidence-page438-sonagere-to-soria-review_batch-897_2026-10-18.json`

Resume Batch 898 at page 439, row 1, Gene Sorisi; the exact boundary has already
been visually confirmed.

## Current blocker

Authenticated NARA Catalog API research remains disabled until the API key
previously exposed in conversation is rotated and supplied through a local
environment or repository secret. This does not block publication or research
through official public sources, the unrestricted Army bulk file and other
configured adapters.
