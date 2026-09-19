# Batch 578 public release verification

Verified 2026-09-19 UTC. [Pull request
#279](https://github.com/therealjameswilson/before-oss/pull/279) passed Test
run 35473921285 and merged as
`fa54cf77b5a20f91b7a67df95ecd0a1409c62e12`. The merged-main Pages run
35474409026 completed successfully.

The unauthenticated, read-only verifier compared the live [Before OSS
site](https://therealjameswilson.github.io/before-oss/) to that immutable
merge commit. All 67 public-manifest assets (96,080,763 bytes), seven core
routes, and the ten Batch 578 direct person URLs matched. Manifest SHA-256:
`a83f602a9c1ea7998085761fdca855ac932888d9496fd31c7f651da2f839e8b0`.
The public-data manifest reproduced byte for byte in two local builds.
This verifies publication, not research completion for all indexed people.

## Coverage and evidence

| Measure | Exact count |
| --- | ---: |
| Printed source rows linked | 23,978 / 23,978 |
| Active cautious person entities | 23,940 |
| People with saved non-planned research attempts | 5,544 (23.1579%) |
| People with verified affiliations | 599 (2.5021%) |
| People with verified employers | 261 (1.0902%) |
| People with archival disposition assessed | 5,499 (22.9699%) |
| Active people not started | 18,396 |
| Possible-duplicate groups | 256 |
| Private durable attempts | 10,095 |
| Claim confidence: confirmed / high / medium / low / conflicting | 1,307 / 1,750 / 1,356 / 183 / 129 |
| Public affiliations / organizations / sources / claims | 2,165 / 674 / 3,686 / 4,538 |

The ten reviewed people occupy PDF page 116 rows 27-36, all in Box 184.
All ten have terminal `requires_archival_review` outcomes with saved CIA,
Library of Congress, and manual research attempts. [Contemporaneous OSS
board proceedings](https://digitalcollections.hoover.org/internal/media/dispatcher/331573/full)
support Mike Devyak's 1943 Navy-to-OSS pathway, not a civilian employer.
The [18 May 1940 *Detective Fiction Weekly* masthead](https://s3.us-west-1.wasabisys.com/luminist/PU/DFW_1940_05_18.pdf)
identifies William T Dewart Jr. as Frank A. Munsey Company secretary, but
does not establish pay or a continuous appointment up to OSS service. The
dated office appears only as a professional affiliation. Andre DeWavrins
is not silently merged with the similarly named André Dewavrin. The detailed
rejections and archival questions are in
`research/batch-578-discovery-checkpoint.md` and its reviewed evidence bundle.
No new civilian employer was verified.

## Quality checks and remaining work

- `validate-ingest`: 522/522 PDF pages represented, 23,978 rows linked,
  warnings visually resolved, and SQLite integrity checks passed.
- Python unit tests: 98/98 passed; the 200-profile structural audit passed.
  The public-identifier audit found zero unexpected full-number boundary
  matches across 24,694 production artifacts.
- Static build: 24,622 direct HTML pages and zero Astro diagnostics. All
  internal links resolved. 50,093 unique external URLs were inventoried but
  not exhaustively visited.
- Bounded release browser suite: 69/69 passed across desktop, phone and
  tablet, including 27 axe accessibility checks.
- The top oil-company category remains seven documented employees at nine
  historically named companies, based on cited employment relationships.

Resume at PDF page 116, row 37, after reviewing the next bounded cohort.
The NARA Catalog adapter requires a local `NARA_API_KEY` at runtime; the key
is neither in the repository nor the public site. The objective is not
complete while 18,396 active people remain `not_started`, and a query alone
is not a reviewable employer outcome.
