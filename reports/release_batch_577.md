# Batch 577 public release verification

Verified 2026-09-19 UTC. [Pull request
#277](https://github.com/therealjameswilson/before-oss/pull/277) passed Test
run 35471004533 and merged as
`0b398a8b2a3e2d04ac03df90a1c63bebf133e313`. The merged-main Test run
35471638814 and Pages run 35471638818 both completed successfully.

The unauthenticated, read-only verifier compared the live [Before OSS
site](https://therealjameswilson.github.io/before-oss/) to that immutable
merge commit. All 67 public-manifest assets (96,027,685 bytes), seven core
routes and the ten Batch 577 direct person URLs matched. Manifest SHA-256:
`5a4cd9164a29e7a9d42c8434390488d2c361b19ec8702acce0e0b409358ff818`.
Two consecutive local production builds gave the same 24,693-file tree
hash, `082d598f5a28984a8a9e09f40800add328c80d105642b32801e2a879fb2e49f2`.
This is reproducible output from the current validated data, not proof that
all 23,940 people have been researched.

## Coverage and evidence

| Measure | Exact count |
| --- | ---: |
| Printed source rows linked | 23,978 / 23,978 |
| Active cautious person entities | 23,940 |
| People with saved non-planned research attempts | 5,534 (23.1161%) |
| People with verified employers | 261 (1.0902%) |
| People with archival disposition assessed | 5,489 (22.9282%) |
| Active people not started | 18,406 |
| Possible-duplicate groups | 256 |
| Private durable attempts | 10,065 |
| Claim confidence: confirmed / high / medium / low / conflicting | 1,307 / 1,745 / 1,355 / 183 / 129 |
| Public affiliations / organizations / sources / claims | 2,163 / 673 / 3,680 / 4,532 |

The ten reviewed people occupy page 116 rows 17-26, Boxes 183-184. All ten
have terminal `requires_archival_review` outcomes after saved CIA, Library of
Congress and manual cross-source checks. Joseph H Devlin, Carl Devoe and
Charles E DeVogel gained high-confidence Army identity links; none gained a
verified pre-OSS employer. The original OSS Cairo report names a USNR Carl
Devoe, but its link to the indexed Carl is unproven. Philippe de Vomécourt's
1940 railway-company job likewise belongs to a plausible SOE candidate,
**not** a confirmed identity for the indexed `Phillippe DeVomecourt`.
The detailed rejection reasons and Box questions are in
`research/batch-577-discovery-checkpoint.md` and the reviewed evidence bundle.

## Quality checks and remaining work

- `validate-ingest`: 522/522 PDF pages represented, 23,978 rows linked,
  warnings visually resolved and SQLite integrity checks passed.
- Python unit tests: 98/98 passed; 200-profile structural audit passed all
  seven checks. The public-identifier audit found zero unexpected full-number
  boundary matches across 24,693 production artifacts.
- Static build: 24,621 direct HTML pages and zero Astro diagnostics. All
  internal links resolved. 50,089 unique external URLs were inventoried but
  not exhaustively visited.
- Bounded release browser suite: 69/69 passed across desktop, phone and
  tablet, including 27 axe accessibility checks. Earlier intermittent macOS
  navigation timeouts were traced to waiting for the full `load` event; the
  affected static-route tests now wait for DOM content and still assert the
  rendered evidence. The final aggregate release run exited successfully.

Resume at PDF page 116, row 27 (Cornelis Devries) with bounded official,
exact-name, employment and archival checks. The NARA Catalog adapter still
requires a local `NARA_API_KEY` at runtime; it is not in the repository or
public site. The objective is not complete while 18,406 people remain
`not_started`, and a query alone is not a reviewable employer outcome.
