# Batch 903 research progress

Date: 2026-10-25 America/New_York

## Scope and source validation

Batch 903 covers NARA index PDF page 441, rows 24-46, from the second Grace M
Spiro row through Henry N Sporborg. All 23 immutable source rows remain
preserved and are linked to 19 active person entities. The printed page was
checked against layout-preserving extraction and a rendered page image. Names,
initials, ranks, protected-identifier presence, Boxes 733-734, the `Br. Army`
note for Sporborg and archive location 230/86/41/02 remain recoverable. Full
protected identifiers remain private.

Four exact duplicate pairs are preserved as eight source rows while each pair
is linked through its shared protected identifier: Peter Spiro, Boris Spiroff,
William J Spiropoulos and Chester J Splawski. The Chester Splawski rows retain
their different printed boxes, 733 and 734, and the second row retains its
`T/Sgt` rank. The two Grace M Spiro rows on page 441 remain separate people in
a visible possible-duplicate group because the index supplies no protected
identifier or other evidence that would justify merging them.

The next unresearched boundary is PDF page 442, row 1, **Leland M Spore**. A
rendered-page review confirms Box 734 and archive location 230/86/41/02. Batch
904 must preserve that row and the remainder of page 442 without treating
name-only similarities as identity evidence.

## Research outcomes

- Boris Robert Spiroff is a confirmed identity match. The Library of Congress
  Veterans History Project documents Army service from 1937 to 1945, his 1943
  recruitment into OSS because of his language skills, and service with the
  Balkans Operational Group. The U.S. Army is published as his explicit
  immediate pre-OSS military affiliation, not as a civilian employer.
- Henry N Sporborg is a confirmed identity match. Official NARA and London
  Gazette records identify him as a British Army lieutenant colonel and a
  senior Special Operations Executive officer. NARA describes his SOE role in
  the cooperation that helped establish OSS's Special Operations branch. SOE
  is therefore published as the documented Allied institutional affiliation
  relevant to the index row; Sporborg is not recast as a U.S. OSS employee.
  An institutional Thames Rowing Club authority record and a University of
  Portsmouth scholarly study document his partnership at Slaughter and May
  before early-war government service. Slaughter and May is published only as
  a medium-confidence, qualified probable last civilian employer because the
  accessible sources do not give the exact departure date.
- Peter Spiro, William J Spiropoulos, Louis Spivack, Joel T Spivey, Chester J
  Splawski and John Spondike have accepted official Army identity bridges.
  Their visually checked historical categories are occupations in mechanical
  treatment of metals not elsewhere classified; radio operators; retail
  managers; bartenders; chauffeurs and drivers of buses, taxis, trucks and
  tractors; and students. The Army record spells Louis Spivack's surname
  `Spivak`; the index spelling remains primary. John Spondike's malformed Army
  grade is withheld. These categories remain qualified occupations and name no
  employer, institution or workplace.
- Chester L Spooner remains conflicting because the protected-identifier Army
  candidate is recorded under the materially different name Peter Messinger.
  No occupation is transferred to Spooner's public profile.
- Both Grace M Spiro rows remain separate, ambiguous identities in a visible
  duplicate-review group. Name-only results do not justify attaching a
  namesake biography.
- Milton A Spitz, Walter F Spitzform, Leo X Spitzmiller, Sydney S Spivack,
  Price C Spivey, Robert D Splain, William Spoeleof, Evalea Spoesser and
  Carlton W Spohn remain unresolved. Each receives a specific archival-review
  outcome rather than an inferred job.

The cohort has one verified-employer outcome, one completed official-affiliation
outcome, six occupation-only outcomes, nine archival-review outcomes, one
identity-review outcome and one conflict outcome. No Batch 903 person remains
not started or in progress. The batch adds 19 manual research attempts. The
qualified Sporborg employer claim does not enter the default confirmed/high
verified-employer aggregate.

The evidence bundle contains nine sources, three organizations, nine
affiliations, 18 claims, 19 person updates and 19 manual research attempts.
Import generated 42 claim-source links. The review file contains nine accepted
official Army decisions and one conflicting decision. Reimports skip all ten
duplicate review decisions and do not duplicate durable evidence rows. SQLite
integrity is `ok` and the foreign-key check returns no rows.

## Updated project coverage

- Index coverage: 23,978/23,978 linked source rows (100%).
- Active person entities: 23,936; stored entities: 23,941, including five
  superseded entities retained for auditability.
- Research-attempt coverage: 13,721 people (57.3237%).
- Verified-employer coverage: 444 people (1.8549%).
- Verified-affiliation coverage: 985 people (4.1151%).
- Archival-review coverage: 12,192 people (50.9358%).
- Not started: 10,210 people; in progress: 1,889 people.
- Possible duplicate groups: 607.
- Conflicts: 474 people.
- Claim confidence totals: 1,632 confirmed, 4,446 high, 1,880 medium, 216 low,
  402 conflicting and two unresolved.
- Citations: 6,839; unique source documents: 3,731.
- Public projection: 23,936 people, 3,085 affiliations, 1,133 organizations,
  5,591 sources and 8,356 published, qualified or conflict claims.
- Private derived exports: 3,106 affiliations, 1,147 organizations, 6,839
  sources, 27,445 research attempts, 23,605 NARA pull-list rows, 21,904
  unresolved rows and 7,364 Army-review queue rows.

Relative to Batch 902, research-attempt and archival-review coverage each
increased by 19 people. Verified-affiliation coverage increased by two through
the reviewed Spiroff/Army and Sporborg/SOE findings. Verified-employer coverage
is unchanged because Sporborg's Slaughter and May chronology is intentionally
qualified at medium confidence. Nine public affiliations, one organization,
nine sources and 18 claims entered the public projection. Citations increased
by nine and unique source documents by five.

## Validation status

The page assignment, review-decision import, reviewed-evidence import and
duplicate-safe reimports pass in isolated and canonical databases. SQLite
integrity and foreign-key checks, regenerated exports, coverage reporting and
public-data redaction pass. The extraction validator accounts for all 23,978
rows across all 522 PDF pages, and the deterministic 200-profile audit passes
all seven checks. All 146 Python tests pass. Astro reports zero errors,
warnings or hints across 534 source files and builds 25,115 static pages. The
targeted Batch 903 matrix passes all 24 browser checks, and the full release
suite passes all 93 browser and accessibility checks across desktop, phone and
tablet, including 30 axe scans with no serious or critical violations. Every
internal link across all 25,115 HTML files resolves. The private-identifier
audit finds zero unexpected matches across the 70-file public tree. All 67
manifest assets verify locally (120,526,819 bytes), the production dependency
audit reports zero vulnerabilities, and two consecutive builds produce
identical public and output tree digests.

Continuous integration and deployed-release verification also pass: content
commit `358f5c382c00b32f48a31b5858be72b1dfae8f85` passed GitHub Actions Test
run `40209624664` and Pages run `40209624590`. The unauthenticated deployed-
release verifier then matched all 67 assets (120,526,819 bytes), eight core
routes, 38 source-register pages and all 19 Batch 903 profiles to that
immutable commit.

## Resume inputs

- `research/army_review_decisions_2026-10-25_batch903.csv`
- `research/evidence-page441-spiro-to-sporborg-review_batch-903_2026-10-25.json`
- `scripts/generate_batch903_bundle.py`

After publication, assign Batch 904 beginning with page 442, row 1, Leland M
Spore. The exact starting boundary has been visually confirmed.

## Current blocker

Authenticated NARA Catalog API research remains disabled until the API key
previously exposed in conversation is rotated and supplied through a local
environment or repository secret. This does not block publication or research
through official public sources, the unrestricted Army bulk file and other
configured adapters.
