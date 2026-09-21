# Batch 617: PDF pages 241–250 and Felix M. Keesing

Original NARA PDF pages **241–250** were rendered at 180 dpi. All **460**
printed rows were compared against the immutable SQLite extraction for row
order, indexed spelling, initials, rank, private-identifier column occupancy,
box, notes, and archival location. All ten complete pages match the extraction;
there were no corrections. The replayed visual-review ledger now covers
**212/522 pages** and **9,718/23,978 rows**; **310** pages remain for
complete-page comparison.

Fourteen possible-duplicate or spelling-variant groups covering 29 people were
reviewed without merging a source row or person entity. The groups include the
Edward Kast cluster; Kauffman/Kaufman/Kaufmann variants; the exact Stanley
Kazinauskas pair; F. Kelley/Kelly and Rita Kelley/Kelly variants; the exact
Thomas Kelly pair; William G. Kemp/Jr.; Betty Kennedy; Marian/Marion Kennedy;
J./Jack B. Kiddie; and the exact Eugene Kingman pair. Even where two rows share
a private identifier, the immutable rows and cautious person entities remain
separate pending direct personnel-file review. Public duplicate labels use
non-identifying hashes rather than the private identifier.

The bounded, read-only Library of Congress first pass completed **46** searches
for the two page-241 queues. It recorded **43** no-result outcomes and **3**
candidate-found outcomes, creating or revisiting **7** unreviewed discovery
candidates. These leads are not accepted identities, employer claims, or
completed multi-source protocols. An initial sandboxed run stopped on local DNS
before making a request; the authorized retry completed without an adapter
error. No authenticated NARA Catalog request was made.

[Felix M. Keesing](https://therealjameswilson.github.io/before-oss/people/207b22e8-a74e-58b1-9c8e-500660f2063c/)
now has a high-confidence identity and separately modeled affiliations. The
University of Hawaiʻi at Mānoa Hamilton Library's archival guide explicitly
states that he left the University of Hawaiʻi for OSS in 1942. The project
therefore records his professorship in Anthropology and Sociology at the
University of Hawaii as both his high-confidence immediate pre-OSS affiliation
and last documented civilian employer. His earlier directorship of research in
the Pacific dependencies for the Institute of Pacific Relations is published
as documented prewar employment, not as the immediate affiliation. Stanford is
not labeled pre-OSS because the archival chronology dates that professorship to
1943. Box 395 remains the next archival action for the exact OSS entry date,
position, assignments, and concurrent wartime teaching chronology.

At this checkpoint, **23,978/23,978** printed rows link to **23,940** active
person entities. Research-attempt coverage is **7,193/23,940 (30.0459%)**;
confirmed/high verified-employer coverage is **279/23,940 (1.1654%)**;
confirmed/high verified-affiliation coverage is **627/23,940 (2.6190%)**;
archival-review disposition coverage is **6,091/23,940 (25.4428%)**. There are
**16,747** `not_started` people, **424** active possible-duplicate groups, and
**131** active people with conflicting identity or source status. The database
stores **12,249** attempts or plans and **4,896** claims: **1,311** confirmed,
**1,894** high, **1,374** medium, **185** low, and **132** conflicting. It
contains **5,041** source/citation records and **2,368** unique document keys.
The public projection has **2,222** affiliations, **706** organizations,
**3,838** sources, and **4,707** claims. The oil-company category remains a
supported, incomplete evidence set of **seven** people across nine companies.
Full-index historical research is unfinished.

## Replay and continuation

After importing the prior durable batches into private SQLite:

```sh
python3 -m oss_research import-page-reviews research/parser_visual_review_pages241-250_2026-09-21.json
python3 -m oss_research import-reviewed-evidence research/evidence-pages241-250-duplicate-review_batch-617_2026-09-21.json
python3 -m oss_research import-reviewed-evidence research/evidence-felix-keesing-hawaii-ipr_batch-617_2026-09-21.json
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
```

Recreate the exact 20 page queues idempotently with these commands:

```sh
python3 -m oss_research assign-page-batch --batch-name page-241-karabatsco-karl-b617 --page 241 --first-row 1 --last-row 23
python3 -m oss_research assign-page-batch --batch-name page-241-karlow-kashitani-b617 --page 241 --first-row 24 --last-row 46
python3 -m oss_research assign-page-batch --batch-name page-242-kasley-kattenburg-b617 --page 242 --first-row 1 --last-row 23
python3 -m oss_research assign-page-batch --batch-name page-242-katwyk-kaurish-b617 --page 242 --first-row 24 --last-row 46
python3 -m oss_research assign-page-batch --batch-name page-243-kavallieros-kazazean-b617 --page 243 --first-row 1 --last-row 23
python3 -m oss_research assign-page-batch --batch-name page-243-kazinauskas-keenan-b617 --page 243 --first-row 24 --last-row 46
python3 -m oss_research assign-page-batch --batch-name page-244-keenan-kellam-b617 --page 244 --first-row 1 --last-row 23
python3 -m oss_research assign-page-batch --batch-name page-244-kelleher-kelley-b617 --page 244 --first-row 24 --last-row 46
python3 -m oss_research assign-page-batch --batch-name page-245-kelley-kelly-b617 --page 245 --first-row 1 --last-row 23
python3 -m oss_research assign-page-batch --batch-name page-245-kelly-kelso-b617 --page 245 --first-row 24 --last-row 46
python3 -m oss_research assign-page-batch --batch-name page-246-kemenyffy-kennedy-b617 --page 246 --first-row 1 --last-row 23
python3 -m oss_research assign-page-batch --batch-name page-246-kennedy-b-b617 --page 246 --first-row 24 --last-row 46
python3 -m oss_research assign-page-batch --batch-name page-247-kennely-kerley-b617 --page 247 --first-row 1 --last-row 23
python3 -m oss_research assign-page-batch --batch-name page-247-kermode-kesting-b617 --page 247 --first-row 24 --last-row 46
python3 -m oss_research assign-page-batch --batch-name page-248-keszthelyi-kibre-b617 --page 248 --first-row 1 --last-row 23
python3 -m oss_research assign-page-batch --batch-name page-248-kida-kilbourn-b617 --page 248 --first-row 24 --last-row 46
python3 -m oss_research assign-page-batch --batch-name page-249-kilbreth-kim-b617 --page 249 --first-row 1 --last-row 23
python3 -m oss_research assign-page-batch --batch-name page-249-kimar-king-b617 --page 249 --first-row 24 --last-row 46
python3 -m oss_research assign-page-batch --batch-name page-250-king-a-b617 --page 250 --first-row 1 --last-row 23
python3 -m oss_research assign-page-batch --batch-name page-250-king-b-kirby-b617 --page 250 --first-row 24 --last-row 46
```

The page-241 Library of Congress passes are already checkpointed. Continue
with the first unsearched queue, then rebuild all derived outputs:

```sh
python3 -m oss_research research --source loc --batch page-242-kasley-kattenburg-b617 --max-queries 23 --resume
python3 -m oss_research export-derived
python3 -m oss_research build-public-data
python3 -m oss_research coverage-report
```

No API key, full service number, raw API response, or private reviewer note is
committed or included in the public site.

## Local release validation

The isolated tracked-only Astro build reports zero errors, warnings, or hints
and produces **24,680** static HTML pages / **24,752** total artifacts. The
bounded Playwright release suite passes **81/81** checks across desktop, phone,
and tablet, including **30** accessibility checks with no serious or critical
axe violations. All **126** Python unit tests pass. Every internal link in the
clean build resolves, and the deterministic 200-profile stratified structural
audit passes all seven checks; it is not the required independent manual
historical audit of 200 profiles. The private-identifier scanner compares
12,926 normalized identifiers and 120 formatted variants against every built
artifact with zero unexpected full-number boundary matches. The local manifest
verifier matches **67 assets / 97,925,474 bytes** at SHA-256
`2b05867e22ee4aa1a8e690829ed4a01601d11e929082fd01dcc2b91adfca461b`.
Two consecutive clean builds reproduce the **24,752-file** production-tree
digest `b9ddea8ce0a0405698b365b451e9af1452ce141c6d059ce87f16f14ca8b7d4c4`.
