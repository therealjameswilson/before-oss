# Batch 618: PDF pages 251–260 and David Krech / Isadore Krechevsky

Original NARA PDF pages **251–260** were rendered at 180 dpi. All **460**
printed rows were compared against the immutable SQLite extraction for row
order, indexed spelling, initials, rank, private-identifier column occupancy,
box, notes, and archival location. All ten complete pages match the extraction;
there were no corrections. The replayed visual-review ledger now covers
**219/522 pages** and **10,040/23,978 rows**. Of those reviewed rows, **10,009**
matched the extraction and **31** retain previously reviewed corrections;
**13,938** rows remain for complete visual comparison.

Thirteen possible-duplicate, spelling-variant, or identifier-conflict groups
covering 26 active people were reviewed without merging them. These include
Victor A/E Kirouac; Maurice J. Kleibert/Kliebert; Eugene/Gene L. Kocherga;
Nick Kochopolus/Kuchopolus; two Charles E. Kopp records with different private
identifiers; two Lawrence Korpita records; two Elizabeth Krishna records;
Francis J/S Kruckosky; two Virginia J. Kuch records; M. G./William G. Konos;
the John J. Knox/Jean Kohn identifier conflict; Joseph Kubachka/Kubuchka; and
Paul L. Kraus/Krauss. Public duplicate-group labels are deterministic hashes;
private identifiers remain restricted.

The David Krech and Isadore Krechevsky rows were merged at the person-entity
layer after direct identity review. Both printed rows remain immutable and now
link to the canonical David Krech entity. The University of Graz archival
finding aid explicitly documents Isadore Krechevsky as David Krech's name from
1913 through 1943, and Lewis Petrinovich's 1979 scholarly biography identifies
the same person by both names and places his 1942 Army service in an OSS
assessment station. The person entity is therefore high confidence.

Two earlier employers are published separately: Krech's 1937 research
assistantship at Swarthmore College and his 1938–1939 University of Colorado
faculty appointment. Neither is labeled immediate pre-OSS or last civilian
employment. The University of California memorial reports later unnamed
nonacademic jobs and pre-Army attitude-survey work but does not identify the
precise employer behind the latter. Box 420 and Krech's 1974 autobiography
remain the next actions; the immediate and last-civilian questions remain
explicitly unresolved.

The bounded, read-only Library of Congress discovery pass completed **46**
searches for the two page-251 queues. It recorded **22** candidate-match
outcomes and no adapter errors. Candidate counts are discovery outcomes only;
they are not accepted identities, employer claims, or completed multi-source
protocols. An initial sandboxed request stopped on local DNS before making a
request, and the authorized retry completed. No authenticated NARA Catalog
request was made.

At this checkpoint, **23,978/23,978** printed rows link to **23,939** active
person entities. Research-attempt coverage is **7,239/23,939 (30.2394%)**;
confirmed/high verified-employer coverage is **280/23,939 (1.1696%)**;
confirmed/high verified-affiliation coverage is **628/23,939 (2.6233%)**;
archival-review disposition coverage is **6,118/23,939 (25.5566%)**. There are
**16,700** `not_started` people, **435** active possible-duplicate groups, and
**133** active people with conflicting identity or source status. The database
stores **12,296** attempts or plans and **4,900** claims: **1,311** confirmed,
**1,898** high, **1,374** medium, **185** low, and **132** conflicting. It
contains **5,045** source/citation records and **2,372** unique document keys.
The public projection has **2,224** affiliations, **708** organizations,
**3,842** sources, and **4,711** claims. The oil-company category remains a
supported, incomplete evidence set of **seven** people across nine companies.
Full-index historical research is unfinished.

## Local release validation

The clean tracked-only release candidate passed 126 Python unit tests, a
200-profile deterministic structural audit, and 84 bounded Playwright tests
(including 30 accessibility cases with no serious or critical axe findings).
Astro reported zero errors, warnings, or hints and emitted 24,681 HTML pages
among 24,753 total artifacts. All internal links resolved. The public-
identifier audit found no unexpected matches, aggregate false positives, or
manifest-size false positives. Two clean production builds produced the same
24,753-file tree SHA-256:
`27d7e4704d6fbacaa03d6dee0196b64b4c3b4db717bbd85a05c0172ef5965891`.
The 67-asset release manifest covers 97,982,649 bytes and has SHA-256
`4978362fdd3cab50c7f3b5c386948795a85562e7255f90b11653bd40e564174a`.

## Replay and continuation

After importing the prior durable batches into private SQLite:

```sh
python3 -m oss_research import-page-reviews research/parser_visual_review_pages251-260_2026-09-21.json
python3 -m oss_research import-review-decisions research/entity_review_decisions_2026-09-21_batch618.csv
python3 -m oss_research import-reviewed-evidence research/evidence-pages251-260-duplicate-review_batch-618_2026-09-21.json
python3 -m oss_research import-reviewed-evidence research/evidence-david-krech-isadore-krechevsky_batch-618_2026-09-21.json
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
```

Recreate the exact 20 page queues idempotently with these commands:

```sh
python3 -m oss_research assign-page-batch --batch-name page-251-kirby-kirkpatrick-b618 --page 251 --first-row 1 --last-row 23
python3 -m oss_research assign-page-batch --batch-name page-251-kirlin-kitakis-b618 --page 251 --first-row 24 --last-row 46
python3 -m oss_research assign-page-batch --batch-name page-252-kitatas-kleeman-b618 --page 252 --first-row 1 --last-row 23
python3 -m oss_research assign-page-batch --batch-name page-252-kleibert-kline-b618 --page 252 --first-row 24 --last-row 46
python3 -m oss_research assign-page-batch --batch-name page-253-kline-knapp-b618 --page 253 --first-row 1 --last-row 23
python3 -m oss_research assign-page-batch --batch-name page-253-knapp-knight-b618 --page 253 --first-row 24 --last-row 46
python3 -m oss_research assign-page-batch --batch-name page-254-knight-knudtson-b618 --page 254 --first-row 1 --last-row 23
python3 -m oss_research assign-page-batch --batch-name page-254-knur-kochian-b618 --page 254 --first-row 24 --last-row 46
python3 -m oss_research assign-page-batch --batch-name page-255-kochopolus-kogon-b618 --page 255 --first-row 1 --last-row 23
python3 -m oss_research assign-page-batch --batch-name page-255-kohler-kondo-b618 --page 255 --first-row 24 --last-row 46
python3 -m oss_research assign-page-batch --batch-name page-256-kondo-kopacz-b618 --page 256 --first-row 1 --last-row 23
python3 -m oss_research assign-page-batch --batch-name page-256-kopcha-kormier-b618 --page 256 --first-row 24 --last-row 46
python3 -m oss_research assign-page-batch --batch-name page-257-kornbaum-kotzer-b618 --page 257 --first-row 1 --last-row 23
python3 -m oss_research assign-page-batch --batch-name page-257-kouka-kozera-b618 --page 257 --first-row 24 --last-row 46
python3 -m oss_research assign-page-batch --batch-name page-258-kozesnik-kranstover-b618 --page 258 --first-row 1 --last-row 23
python3 -m oss_research assign-page-batch --batch-name page-258-krantz-kreis-b618 --page 258 --first-row 24 --last-row 46
python3 -m oss_research assign-page-batch --batch-name page-259-kreisser-krisch-b618 --page 259 --first-row 1 --last-row 23
python3 -m oss_research assign-page-batch --batch-name page-259-krishna-kruger-b618 --page 259 --first-row 24 --last-row 46
python3 -m oss_research assign-page-batch --batch-name page-260-kruger-kuchopolus-b618 --page 260 --first-row 1 --last-row 23
python3 -m oss_research assign-page-batch --batch-name page-260-kudlek-kunjara-b618 --page 260 --first-row 24 --last-row 46
```

The page-251 Library of Congress passes are already checkpointed. Continue
with the first unsearched queue, then rebuild all derived outputs:

```sh
python3 -m oss_research research --source loc --batch page-252-kitatas-kleeman-b618 --max-queries 23 --resume
python3 -m oss_research export-derived
python3 -m oss_research build-public-data
python3 -m oss_research coverage-report
```

No API key, full service number, raw API response, or private reviewer note is
committed or included in the public site.
