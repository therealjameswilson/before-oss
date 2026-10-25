# Batch 907 research audit

Batch 907 covers NARA personnel-index PDF page 443, rows 24-46, from
**Thomas S Stamoulis** through **Robert W Stanley**. All 23 printed rows remain
separate and are linked to 23 separate active person entities. The batch was
researched with the staged official-context, exact-name, occupation/employer,
obituary, institutional, newspaper, directory, Library of Congress and
archival protocol. All 23 people now have terminal research outcomes.

## Reviewed outcomes

- Seven nonshared protected-identifier matches were accepted against the
  official Army merged file: Vincent C Stampone, Basil J Stanberg, Victor L
  Stanek, Ferdinand F Stanford, William Stanko, Carl T Stanley and Eugene R
  Stanley.
- The official historical civilian-occupation codes are published only as
  qualified occupation categories. They identify no employer, workplace or
  immediate pre-OSS affiliation.
- Captain Demetrius G. Stampados is confirmed through a direct 4 May 1944 OSS
  report that repeats his name, rank and officer number. The report documents
  earlier staff-officer service in the Greek Air Force and entry into OSS as a
  civilian on 11 December 1941. The military affiliation is published as
  documented prewar service, not as an immediate predecessor or civilian
  employer.
- Thomas S Stamoulis remains conflicting. A protected identifier agrees with
  an official Army row for Thomas G Stamoulis, but the different middle
  initial prevents transferring the candidate's identity or occupation.
- A USASOC history identifies a P-101 veteran named Clarence Stanford, while
  a regional plan profiles a postwar boatbuilder of that name. The index has
  no middle initial, rank or identifier. Both remain private candidate leads,
  and no public identity or affiliation claim is assigned.
- Fourteen people require personnel-file review after namesakes,
  chronologically irrelevant results and unsupported candidates were
  rejected. Their public profiles state that accessible evidence has not yet
  identified a reliable pre-OSS employer; they do not claim that none existed.

## Source audit

The reviewed bundle contains eight citation records:

1. NARA's complete OSS personnel index, PDF page 443, rows 24-46.
2. The official Electronic Army Serial Number Merged File, NAID 1263923.
3. NARA's technical documentation for the Army merged file.
4. NARA's compiled historical occupation-code lists, with the relevant code
   pages checked against the official PDF.
5. The 4 May 1944 OSS board proceedings in Hoover Digital Collections,
   viewer pages 48-49, for Demetrius G. Stampados.
6. The Hellenic Air Force Academy's official history, used only to normalize
   the historical Greek military organization.
7. The USASOC History Office's Operation BOSTON study, retained only as a
   private Clarence Stanford candidate lead.
8. A Middle Peninsula regional maritime plan, retained only as a private
   Clarence Stanford namesake lead.

Search-result snippets were used for discovery only. The CIA and Library of
Congress adapters failed closed when their source-access checks could not be
completed; indexed official-domain searches were also reviewed. No paywall,
CAPTCHA, robots restriction or access control was bypassed. No exposed NARA
API credential was used or persisted.

## Exact coverage after import

- Index coverage: 23,978/23,978 source rows linked (100%).
- Active person entities: 23,936.
- Research attempted: 13,811/23,936 (57.6997%).
- Verified employer: 447/23,936 (1.8675%).
- Verified affiliation: 991/23,936 (4.1402%).
- Archival-review assessed: 12,283/23,936 (51.3160%).
- Not started: 10,120.
- Possible-duplicate groups: 608.
- Conflicts: 478.
- Claim confidence: 1,639 confirmed; 4,485 high; 1,912 medium; 218 low;
  407 conflicting; 2 unresolved.
- Public projection: 3,124 affiliations; 1,138 organizations; 5,631 sources;
  8,439 published, qualified or conflict claims.

## Reproducibility

- Evidence generator: `scripts/generate_batch907_bundle.py`
- Reviewed evidence:
  `research/evidence-page443-stamoulis-to-stanley-review_batch-907_2026-10-25.json`
- Army decisions: `research/army_review_decisions_2026-10-25_batch907.csv`
- Browser regression: `site/tests/batch907.spec.ts`
- Isolated import and duplicate-safe replay: passed.
- SQLite quick check: `ok`.
- Foreign-key errors: 0.
- Extraction validation: 23,978/23,978 rows, all 522 pages represented, every
  parser-warning row visually resolved.

The next indexed boundary is PDF page 444, row 1, **William S Stanley**, in
Box 737.
