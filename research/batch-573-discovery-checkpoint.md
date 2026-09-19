# Batch 573 discovery checkpoint

Date: 2026-09-19 UTC

## Cohort and extraction

Personnel-index PDF page 115 rows 23-32, Christian DeSorbier through Raymond
Deston. Rows 23-27 are in Box 182 (`230/86/29/07`), and rows 28-32 are in Box
183 (`230/86/30/01`). The entire page was rendered at 180 dpi and visually
inspected. Emile Despres (row 29) already had a reviewed Federal Reserve Board
finding; this batch checked that row without duplicating the claim. Four
printed private identifiers remain private and masked in all public data.

The next printed row, Frank J Desuta (row 33, Box 183), resembles Frank J
Desota (row 25, Box 182). The two source rows and person entities remain
separate in a visible possible-duplicate group until their physical files can
be compared. The seven-digit Desota identifier was not padded to create an
Army-file match. Frank J Desuta remains `not_started` until the next research
batch; duplicate flagging is not a completed research attempt.

## Bounded source protocol

- Nine newly researched people received one completed CIA Reading Room check
  and one completed Library of Congress check each, with no accepted result.
  Nine additional web query plans were persisted; their targeted research was
  then carried out in the manual evidence review. The already-researched Emile
  Despres received a consistency-review attempt.
- No authenticated NARA Catalog API request was made. The key and request
  headers did not enter the repository, logs, prompts or public assets.
- A transient, privacy-preserving scan covered all 9,200,232 entries in the
  official Army merged file. Three strict protected-identifier matches were
  accepted. The occupational code definitions were checked against rendered
  pages 171, 173 and 174 of NARA's official code-list PDF.
- A scanned, NARA-released OSS memorandum was OCR-located and its physical PDF
  page 18 visually inspected. The 1941 Newton city-directory OCR was read from
  the Newton Free Library's image-backed original on Internet Archive; its
  printed page 176 lists insurance work but no firm.
- Three original French Service historique de la Défense inventories were
  downloaded and searched directly. They establish an adult Christian de
  Sorbier de Pougnadoresse in the Sussex network and triangulate the indexed
  lieutenant-colonel René Despax with René Louis Auguste/Louis Despax. The
  distinct captain René Jules Despax is not merged.

## Accepted and qualified findings

- Christian DeSorbier: high-confidence French-officer identity from SHD Sussex
  and Resistance cross-references, but no dated immediate pre-OSS military
  assignment or civilian employer. A younger same-name person was rejected.
- Emile F Desormier: confirmed protected-identifier Army match. Code 736
  supports only a chauffeur/vehicle-driver occupation at Army entry in July
  1943, not a company.
- René Despax: high-confidence French-officer identity from three official
  register entries and the indexed rank. No pre-OSS transfer date is known;
  Air Force career status is not promoted into an immediate-predecessor claim.
- Gabriel H Desplaines: confirmed Army match despite the official file's
  `DES PLAINES` spacing. Code 105 supports general-office-clerk occupation at
  Army entry in November 1942, not an employer.
- Jean P Desroberts: high-confidence Army match by private identifier, but the
  Army given name is damaged. Code 475 supports machinist occupation at Army
  entry in February 1942, not a workshop or employer.
- Raymond Deston: a NARA-released OSS memorandum directly documents Lieutenant
  Raymond Deston, USNR, as Chief of Central Information Division in April
  1945. A rare-name 1941 city-directory entry for Raymond W Deston is published
  only as a **medium-confidence, qualified insurance-occupation lead**. It
  names no company and does not prove the last civilian employer. The postwar
  John Hancock directory evidence was deliberately not back-projected to 1941.

Frank J Desota and Dorothy G Dessin remain unresolved beyond the indexed
files. Michel E Despax remains ambiguous: a NARA directors-list search lead
has different initials, and no reviewed source bridges the identities. Emile
Despres keeps the earlier verified Federal Reserve Board claim. No new named
pre-OSS employer was established in this cohort. All nine newly attempted
people have a terminal research disposition; every unresolved profile retains
the exact unresolved-employer statement and archival-review guidance.

## Evidence and QA

- `research/evidence-page-one-hundred-and-fifteen-christian-desorbier-through-raymond-deston_batch-573_2026-09-19.json`
- `site/tests/batch573.spec.ts`
- `research/batch-573-discovery-checkpoint.md`

The reviewed bundle contains eight source documents, four occupation-only
affiliations, nineteen claims, thirty-nine claim-source links, ten person
updates (including the next-row duplicate flag), and ten manual review
attempts. Together with nine CIA checks, nine Library of Congress checks and
nine web plans, the database gained thirty-seven durable attempts. The source
page, source rows and prior Emile Despres evidence were preserved.

## Exact coverage after import

- Index coverage: 23,978 / 23,978 source rows linked (100%)
- Active person entities: 23,940
- Research-attempt coverage: 5,495 / 23,940 (22.9532%)
- Verified-affiliation coverage: 596 / 23,940 (2.4896%)
- Verified-employer coverage: 260 / 23,940 (1.0860%)
- Archival-review disposition coverage: 5,450 / 23,940 (22.7652%)
- Remaining active `not_started`: 18,445
- Possible duplicate groups: 256
- Public affiliations: 2,160; public organizations: 672
- Public sources: 3,665; public claims: 4,491
- Private affiliations: 2,176; private organizations: 686
- Citation records: 4,856; unique source documents: 2,220
- Stored claims: 4,677; durable research attempts: 9,948
- Claim confidence: 1,307 confirmed, 1,707 high, 1,351 medium, 183 low,
  129 conflicting

The 95 Python tests, 200-profile structural audit, ingest validation, static
build, direct-profile browser checks, bounded release suite, internal-link
check and full public-identifier audit passed locally. The release suite was
rerun after its only selector-level test correction; no source or public-data
change followed the production build. This local batch is not yet a verified
GitHub Pages release.

## Next cohort

Continue with PDF page 115 rows 33-42. Compare Frank J Desuta's Box 183 file
with Frank J Desota's Box 182 file before any entity merge. Continue the
staged, source-auditable protocol for every person and do not count unissued
query plans as completed research.
