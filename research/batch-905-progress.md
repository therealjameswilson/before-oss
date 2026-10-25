# Batch 905 research audit

## Scope

- Index boundary: NARA personnel index PDF page 442, rows 24-46.
- Printed range: Phillip I Squillacioti through Pierre G St. Sauveur.
- Archive range: Boxes 734 and 735 at 230/86/41/02, plus Joseph T Sranova in Box 752 at 230/86/41/05.
- Preserved source rows: 23.
- Active person entities: 23.
- Terminal outcomes saved: 23.
- Official Army bulk identity bridges accepted: 10.
- Official Army bulk identifier conflicts retained: 2.
- Protected identifiers in public evidence: 0.

## Outcomes

| Outcome | People | Notes |
|---|---:|---|
| Completed | 1 | Anonda Srivardhana; Carnegie Tech student status is separated from employment |
| Conflicting sources | 3 | Aaron Squires; Alice E St. Clair; Ramond P St. Laurent |
| Occupation only found | 6 | Official Army categories name no employer or workplace |
| Requires archival review | 13 | Minimum staged protocol completed; indexed personnel files remain necessary |

All 23 people received a new nonplanned research attempt. Project-wide
research-attempt coverage therefore increased by 23.

## Published evidence decisions

### Army occupation evidence

Seven accepted official Army bridges provide dated historical civilian-
occupation categories. They are published as qualified occupations only and
are excluded from verified-employer analytics.

| Person | Army-entry date | Historical code | Qualified occupation |
|---|---|---:|---|
| Phillip I Squillacioti | 1942-09-04 | 091 | Purchasing agents and buyers, not elsewhere classified |
| Emerson T Squire | 1942-04-09 | 027 | Social and welfare workers |
| Aaron Squires | 1941-01-13 | 056 | Photographers |
| Joseph T Sranova | 1942-01-20 | 819 | Unskilled occupations in manufacture of textiles, not elsewhere classified |
| Antonio L St. Laurent | 1942-11-03 | 678 | Semiskilled machine-shop and related occupations, not elsewhere classified |
| Albert J St. Michel | 1941-02-24 | 819 | Unskilled occupations in manufacture of textiles, not elsewhere classified |
| Pierre G St. Sauveur | 1943-04-23 | 819 | Unskilled occupations in manufacture of textiles, not elsewhere classified |

Phillip/Philip Squillacioti and Sranova/Stranova are preserved as documented
name variants. Emerson T Squire and M/Sgt Emerson Squires remain separate
people in one visible possible-duplicate group.

### Aaron Squires

The official Army bridge supports a dated photographer category. An American
Public University historical-journal caption names Aaron Squires with the OSS
Deer Team, while the National Park Service history calls the photographer
Alan Squires. The first-name disagreement remains visible; the Box 735 file is
needed to resolve it. Neither source establishes a pre-OSS employer.

### Anonda Srivardhana

The 25 July 1944 *Carnegie Tartan* lists Anonda Srivardhana among independent
Carnegie Tech men serving their country and identifies his field as military
intelligence. E. Bruce Reynolds identifies Anond Siwattana/Siwatthana
(Srivardhana) in a person-specific OSS DURIAN training photograph and thanks
him as a wartime participant. Carnegie Institute of Technology is therefore
published as a high-confidence student affiliation, never as an employer.

### Karawek Srivicharn

Reynolds identifies Karawek Siwichan (Srivicharn) among the first Thai
volunteers after their December 1942 commissions as Free Thai officers. The
distinctive variant and compatible OSS/Free Thai context support a high-
confidence identity. The commission is military status, not civilian
employment, and the exact pre-OSS sequence remains for Box 735 review.

### Identity-only Army bridges

Wilfred T St. Laurence, Ivan B St. Onge and Wallace J St. Pierre have accepted
identity bridges only. The St. Laurence and St. Pierre Army-entry records are
post-OSS, and St. Onge's coded occupation is not safely interpretable. No
occupation or employer is transferred from those fields.

### Identifier conflicts

Alice E St. Clair shares a protected identifier with the separately indexed
Alice E Gibson. Ramond P St. Laurent shares one with a separately indexed
Eugene K Matthews row. All source rows and person entities remain separate;
the public profiles describe the conflicts without exposing either identifier.
A legacy identifier-bearing private duplicate-group label for Alice E Gibson
was replaced with a descriptive label before rebuilding public data.

## Rejected and unresolved leads

Nine people received the staged official-context, CIA Reading Room, exact-name,
rank, occupation/employer, obituary, institutional, newspaper, directory,
Library of Congress and archival search protocol without a defensible external
identity bridge. Namesakes and chronologically irrelevant or postwar-only
records were not promoted. Each unresolved profile directs researchers to the
indexed personnel file rather than asserting that no pre-OSS employment
existed.

## Reproducibility

- Evidence generator: `scripts/generate_batch905_bundle.py`
- Reviewed evidence: `research/evidence-page442-squillacioti-to-st-sauveur-review_batch-905_2026-10-25.json`
- Army decisions: `research/army_review_decisions_2026-10-25_batch905.csv`
- Browser regression: `site/tests/batch905.spec.ts`
- Public redaction result: passed.
- SQLite quick check: `ok`.
- Foreign-key errors: 0.
- Extraction validation: 23,978/23,978 rows, all 522 pages represented, every
  parser-warning row visually resolved.

## Release verification

- Published content commit:
  `50caecef5f859cae2fb189218918774e30c7c76c`.
- GitHub Actions Test run `40222176956`: completed successfully, including the
  full Node 24 static build, bounded browser/accessibility release suite,
  checked-in manifest verification and rebuilt-source public-identifier audit.
- GitHub Pages run `40222176957`: build and deployment completed successfully.
- Unauthenticated deployed-release verification matched all 67 public assets
  (120,848,262 bytes), eight core routes, 38 source-register pages and all 24
  directly affected or duplicate-linked profiles.
- Deployed manifest SHA-256:
  `52f278a0b0611ef0a80ec0393148e0cfaf4302a3ca79c556401fc74ed9cca2b5`.
- Workflow annotations concerned action-runtime and runner-image migrations;
  no test, build, redaction, accessibility or deployment gate failed.
