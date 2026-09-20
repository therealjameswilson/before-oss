# Batch 593 — PDF page 121, Doll through Donovan

Reviewed 2026-09-20 UTC. The original [NARA OSS personnel index](https://www.archives.gov/files/iwg/declassified-records/rg-226-oss/personnel-database.pdf), PDF page 121, contains 46 printed rows. All 46 were compared with the rendered page image and remain linked to 46 separate active person entities. Rows 1–24 are Box 192; rows 25–46 are Box 193. The printed `Donaldosn` spelling, `also AS` note, ranks, identifier-column occupancy, and 230/86/30/02 location are retained. The matching-only visual decision is replayable from `research/parser_visual_review_page121_2026-09-20.json`.

Two same-name pairs remain four separate entities: George J Donish (rows 28–29) and John L Donnelly (rows 37–38). Only one row in each pair has a printed identifier. Both pairs are flagged for side-by-side Box 193 review; neither is merged or assigned the other's identifier.

The current [CIA robots policy](https://www.cia.gov/robots.txt) disallows the adapter's automated Reading Room search route. One narrow query for Mirko P Dominis was made with the legacy adapter before the policy was checked; after that, the route was stopped. The revised adapter fails closed and the recorded prior attempt is not treated as a reviewed CIA document. See `research/source-access-review_2026-09-20.md`.

The [Library of Congress JSON API limit](https://www.loc.gov/apis/json-and-yaml/working-within-limits/) is 20 requests per minute. The revised adapter spaces requests at least 3.2 seconds apart, stops on 429, and keeps a persistent cooldown. One bounded page-121 pass made 46 HTTP-200 LoC discovery requests and saved 44 unreviewed source-candidate links; three already-completed query fingerprints were skipped. These are *discovery* links, not accepted identities, employment evidence, or completed minimum-protocol outcomes. The sanitized attempts and candidates are replayable from `research/adapter_attempt_checkpoints.json`.

Evidence reviewed beyond automated discovery:

- [NARA's Dong Kingman article](https://unwritten-record.blogs.archives.gov/2023/05/23/dong-kingman-watercolor-master/) and the [Museum of Chinese in America biography](https://www.mocanyc.org/collections/stories/dong-kingman/) both place the watercolorist in OSS map work and document earlier WPA work. An exact-name and nonshared protected-identifier match in official Army bulk data supports the indexed Kingman M Dong Sr. identity. Works Progress Administration is published as **earlier documented employment only**. Neither immediate pre-OSS assignment nor last civilian employer before military service has been established. The physical Box 193 file remains a priority.
- The contemporary Clark University Geographical Society's [May 1945 *Monadnock*](https://commons.clarku.edu/monadnock/30/), printed page 9/PDF page 5, explicitly identifies Jocelyn Donaldson in the OSS Topographic Models Section and describes 1942–43 Clark student status. The original scanned page was inspected. Student status is not treated as Clark employment; the actual OSS entry date and pre-OSS employer remain unknown.
- The official Army bulk candidate for Ivan H Doman shares the printed protected identifier but names Harmon Robinson. This is a visible identity conflict, not a biography or employer assignment. Box 192 must resolve it.

The current page-121 queue has one `documented_prewar_employer_found`, one previously `completed` person (Gail F Donnalley), 27 `in_progress`, 11 `candidate_found`, five `needs_identity_review`, and one `needs_temporal_review`. Thus 44 of the 46 still require substantial source review; a successful LoC request is not counted as completion. The new evidence bundle has four public, claim-level cited findings (two identity findings, one earlier-employment finding, and one qualified conflict). The two Army candidate decisions accept one identity and preserve one conflict.

After this batch, project-wide index coverage is **23,978/23,978** source rows; research-attempt coverage is **5,782/23,940** active people (24.1520%); verified-employer coverage is **266/23,940** (1.1111%); verified-affiliation coverage is **607/23,940** (2.5355%); and archival-review assessment covers **5,699/23,940** (23.8053%). There are **18,158** `not_started` people and **261** possible-duplicate groups. The NARA Catalog API key was not used in this batch, and no Catalog response body was stored.

The reproducible 200-profile stratified *structural* audit passed its seven automated consistency checks. It is not a substitute for a historian's 200-profile source-by-source review; the woman/personnel-status stratum cannot be inferred from index names and still needs sourced identity work.

Replay and resume:

```bash
python3 -m oss_research import-page-reviews research/parser_visual_review_page121_2026-09-20.json
python3 -m oss_research assign-page-batch --batch-name page-121-doll-donovan-b593 --page 121 --first-row 1 --last-row 46
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
python3 -m oss_research import-review-decisions research/army_review_decisions_2026-09-20_batch593.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page-121-doll-through-donovan_batch-593_2026-09-20.json
python3 -m oss_research research --source loc --batch page-121-doll-donovan-b593 --max-queries 20 --resume
python3 -m oss_research export-adapter-checkpoints
python3 -m oss_research export-derived
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
```

Do not automate the CIA search route while it remains disallowed. The remaining 44 people need staged official/institutional source checks, namesake rejections, and, where necessary, physical personnel-file requests. A release note and deployment verification are separate from this local research progress report.
