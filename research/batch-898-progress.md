# Batch 898 research progress

Date: 2026-10-25 America/New_York

## Scope and source validation

Batch 898 covers NARA index PDF page 439, rows 1-23, from Gene Sorisi
through Jacques Soustelle. All 23 immutable source rows remain preserved and
linked to 23 active person entities. The printed page was checked against
layout-preserving extraction and a rendered page image. Names, initials,
ranks, protected-identifier presence, Boxes 729-730 and archive location
230/86/41/02 remain recoverable. Full protected identifiers remain private.

Stephen S Sorota and Steve S Sorota remain separate people in a visible
possible-duplicate group. Victor L Soskice and Victor A Soskice likewise
remain separate because the printed middle initials conflict. The documented
Georgetown and Lycée Français chronology belongs only to Victor A Soskice.
Alexander J Soto shares a protected identifier with a separately printed
William J Smith row; both people remain separate, the conflict is public, and
no occupation or employer evidence is transferred.

The next unresearched boundary is page 439, row 24, M J Soustelle. The page
was rendered and visually checked: the row prints Soustelle, first name M,
middle initial J, the note `Fr. Civili`, Box 730 and archive location
230/86/41/02.

## Research outcomes

- Gene Sorisi, Erwin Sorkin and Edmond Sottile have high-confidence official
  Army identity bridges. Their dated stock-clerk, metal-treatment and textile-
  product-fabrication categories are published as qualified occupations only.
  None names an employer, institution or workplace.
- Lyman F Sorrels and Thomas G Soter have high-confidence Army identity
  bridges but no usable occupation finding. Sorrels's reviewed Army entry is
  postwar and its code is undefined in the inspected official table; Soter's
  residual code is not interpreted.
- Rolf Sorlie is a high-confidence match to Norwegian engineer and resistance
  participant Rolf Sørlie. Institutional evidence supports the engineer
  occupation but does not name an employer. The Vemork context is not converted
  into employment at Norsk Hydro, and no formal military category is inferred.
- Stephen S Sorota is a probable match to Stephen S. “Steve” Sorota, documented
  by an institutional profile as a Phillips Academy football and track coach
  beginning in 1936. The finding remains medium-confidence and documented
  prewar because no OSS or protected-identifier bridge establishes the indexed
  identity or immediate chronology. The separate Steve S Sorota profile does
  not receive the Phillips claim.
- Victor A Soskice is identified at high confidence as Victor Andrew Soskice.
  Student status at Georgetown University is the best-supported immediate
  pre-OSS affiliation, while earlier Lycée Français de New York study remains
  separate. Both are medium-confidence qualified findings from a reputable
  secondary biography review; neither is a civilian employer. Victor L
  Soskice remains ambiguous and receives neither affiliation.
- Frédéric Souard's 1935-1937 French military-trainee record and late-1943
  executive-officer assignment with the French Increment of U.S. Fifth Army
  are published separately. The latter's temporal relation to the OSS file is
  uncertain. Georges Soulier and Thomas P Soullas receive high-confidence
  wartime identity findings without invented pre-OSS employers.
- Jacques Soustelle is identified at high confidence. The Académie française
  biography supports three high-confidence documented-prewar employment
  relationships: deputy director of the Musée de l'Homme and lecturer at the
  Collège de France and École nationale de la France d'outre-mer. The source
  does not establish which was his immediate predecessor or single last
  civilian employer, so none is promoted to those fields.
- Bohuslav Soumar remains ambiguous between unbridged candidates. Mildred
  Sorkin, Morris B Soroka, Henry Sorrese, Romeo A Soucy, John I Soule, Robert W
  Sours and Mary Sousa remain unresolved. Every case has an explicit Box
  729/730 archival-review outcome rather than an invented employer.

The cohort distribution is 11 high-confidence identities, one probable
identity, three ambiguous identities, one conflicting identity and seven
unresolved identities. Research status is four occupation-only outcomes, one
documented-prewar-employer outcome, one conflict outcome and 17 archival-
review outcomes. No Batch 898 person remains not started or in progress. The
batch adds 23 manual research attempts.

The evidence bundle contains 16 sources, seven organization references, 12
affiliations, 25 claims, 23 person updates, 23 manual research attempts and 48
claim-source links. It contains 15 high-confidence, nine medium-confidence
qualified and one conflicting public claim. The review file contains five
accepted and one conflicting Army candidate decisions. Reimporting both files
is idempotent. SQLite integrity is `ok` and the foreign-key check returns no
rows.

## Updated project coverage

- Index coverage: 23,978/23,978 linked source rows (100%).
- Active person entities: 23,936; stored entities: 23,941, including five
  superseded entities retained for auditability.
- Research-attempt coverage: 13,611 people (56.8641%).
- Verified-employer coverage: 439 people (1.8341%).
- Verified-affiliation coverage: 978 people (4.0859%).
- Archival-review coverage: 12,082 people (50.4763%).
- Not started: 10,320 people; in progress: 1,889 people.
- Possible duplicate groups: 602.
- Conflicts: 468 people.
- Claim confidence totals: 1,628 confirmed, 4,403 high, 1,844 medium, 212 low,
  396 conflicting and two unresolved.
- Citations: 6,790; unique source documents: 3,700.
- Public projection: 23,936 people, 3,043 affiliations, 1,125 organizations,
  5,546 sources and 8,267 published, qualified or conflict claims.
- Private derived exports: 3,064 affiliations, 1,139 organizations, 6,790
  sources, 27,335 research attempts, 23,611 NARA pull-list rows and 21,938
  unresolved rows.

Relative to Batch 897, research-attempt coverage and archival-review coverage
each increased by 23 people. Verified-affiliation coverage increased by two
and verified-employer coverage by one. Fifteen high-, nine medium- and one
conflicting claim, 12 public affiliations, five net organizations, 16 public
sources and 25 public claims entered the projection. Citations increased by 16
and unique source documents by 12.

## Validation status

The page assignment, review-decision import, reviewed-evidence import and
idempotency reimports pass in an isolated database and the canonical database.
SQLite integrity and foreign-key checks, regenerated exports, coverage
reporting and public-data redaction pass. The extraction validator accounts for
all 23,978 rows across all 522 PDF pages, and the stratified 200-profile audit
passes all seven checks. All 146 Python tests and 84 parameterized subtests
pass. Astro reports zero errors, warnings or hints across 529 source files and
builds 25,106 static pages. The bounded release suite passes all 93 browser and
accessibility checks across desktop, phone and tablet, including 30 axe scans
with no serious or critical violations. Every internal link resolves. The
private-identifier audit finds zero unexpected matches across 25,178
artifacts, all 67 manifest assets verify locally, the production dependency
audit reports zero vulnerabilities, and two consecutive builds produce
identical public and output tree digests. GitHub Actions deployment and
unauthenticated public verification are pending the release commit.

## Resume inputs

- `research/army_review_decisions_2026-10-25_batch898.csv`
- `research/evidence-page439-sorisi-to-soustelle-review_batch-898_2026-10-25.json`

Resume Batch 899 at page 439, row 24, M J Soustelle; the exact boundary has
already been visually confirmed.

## Current blocker

Authenticated NARA Catalog API research remains disabled until the API key
previously exposed in conversation is rotated and supplied through a local
environment or repository secret. This does not block publication or research
through official public sources, the unrestricted Army bulk file and other
configured adapters.
