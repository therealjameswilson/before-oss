# Batch 595 — PDF page 123, Doucette through Downey

Reviewed 2026-09-20 UTC. The original [NARA OSS personnel index](https://www.archives.gov/files/iwg/declassified-records/rg-226-oss/personnel-database.pdf), PDF page 123, has 46 printed rows. The full-size page image was compared with all 46 stored extractions: names, initials, the two separate Jean Douglas rows, D'Oultremont apostrophe, John Dowditch and Thomas Dowling III suffixes, rank and protected-identifier column occupancy, `British A` and `Belgian` notes, Box 196-to-197 transition, and locations 230/86/30/02-to-03 match. The matching-only decision is replayable from `research/parser_visual_review_page123_2026-09-20.json`.

One bounded [Library of Congress JSON API](https://www.loc.gov/apis/json-and-yaml/working-within-limits/) pass made 46 successful, rate-limited read-only searches, with zero blocked requests and zero errors. It saved 31 **unreviewed discovery links** concerning 12 people. None is an accepted identity or employer claim. Three page-123 people already had saved research outcomes, so project-wide attempted-person coverage rose by 43, not 46. The sanitized adapter attempts and candidates are replayable from `research/adapter_attempt_checkpoints.json`.

Evidence reviewed beyond the automated pass:

- George J and Helias J Doundoulakis, separate Box 196 rows 27–28: the official [NARA Army bulk file](https://catalog.archives.gov/id/1263923) independently matches each full indexed name to a **nonshared protected identifier**, at record ordinals 364286 and 364287. The [National WWII Museum oral history](https://www.ww2online.org/view/helias-doundoulakis) describes the brothers' Cretan resistance work, U.S. Army enlistment in September 1943, and subsequent OSS recruitment. An [edited museum podcast transcript](https://www.nationalww2museum.org/war/podcasts/secret-wwii-spies-special-ops/bonus-episode-voices-secret-wwii) quotes Helias on both brothers entering the Army; it derives from the same witness and is **not** counted as independent corroboration. Two high-confidence immediate-pre-OSS **military assignment** affiliations are published, with claim-level citations. Neither the Army occupation code, earlier SOE-supported resistance, their father's restaurant, nor postwar engineering work is turned into a civilian employer. Exact OSS transfer dates and last civilian employers still require Box 196; both remain `requires_archival_review`. Helias is now classified as enlisted Army personnel on the combined official bulk and oral-history evidence, despite the index's blank rank cell.
- Theodore D'Oultremont, Box 196 row 26: a detailed [Comète Kinship Belgium profile](https://www.cometeline.org/ficheB043.html) names a Belgian reserve officer and later Belgian State Security–OSS liaison, citing Belgian defense dossier OO-46851. The profile's original cited file and the NARA Box 196 file have not been inspected. Its 1943 State Security and OSS liaison roles may overlap rather than form a predecessor sequence. Identity is retained as *probable* and research status as `needs_temporal_review`; no employer or immediate-affiliation claim is published. Search results for Georges, Edouard, and Charles-Emile d'Oultremont are different named people, not substituted for Theodore.
- [Yale's Donald Chase Downes finding aid](https://ead-pdfs.library.yale.edu/3895.pdf), printed pages 4 and 11, and the [National Park Service's OSS history](https://www.nps.gov/articles/oss-in-action-the-mediterranean-and-european-theaters.htm) were rechecked. They corroborate Downes's previously published Free World Association employment after earlier teaching and ONI work. No duplicate claim was created. The separately documented Arden W Dow and Sterling Dow profiles were likewise not reclassified.

The evidence bundle `research/evidence-page-123-doucette-downey_batch-595_2026-09-20.json` adds four sources, two published Army affiliations, four published claims, three manual review attempts, and three person updates. The Army decisions in `research/army_review_decisions_2026-09-20_batch595.csv` are private identity decisions. No authenticated Catalog API call was made and no Catalog response body was stored.

Page-123 statuses are 11 `candidate_found`, one `completed`, 29 `in_progress`, one `needs_temporal_review`, two `requires_archival_review`, and two previously `verified_employer_found`. Thus the LoC pass is not a completed multi-source protocol for the other 40 people. Project-wide index coverage is **23,978/23,978** linked source rows; research-attempt coverage **5,870/23,940** people (24.5196%); verified-employer coverage unchanged at **266/23,940** (1.1111%); verified-affiliation coverage **609/23,940** (2.5439%); archival-review assessment **5,704/23,940** (23.8262%). `not_started` is **18,070**. Private attempts total **10,849**; claim-confidence counts are 1,308 confirmed, 1,847 high, 1,367 medium, 185 low, and 129 conflicting.

Normalization issue surfaced during this batch: the private organizations table has **35 canonical-name collision groups covering 85 rows**, including 11 `United States Army` rows created by earlier independent evidence keys. Batch 595 reused an existing Army organization key rather than creating another. These collisions require a separately reviewed organization-resolution plan; do not silently merge subsidiaries, units, or historically distinct bodies by string equality.

Replay and resume:

```bash
python3 -m oss_research import-page-reviews research/parser_visual_review_page123_2026-09-20.json
python3 -m oss_research assign-page-batch --batch-name page-123-doucette-downey-b595 --page 123 --first-row 1 --last-row 46
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
python3 -m oss_research import-review-decisions research/army_review_decisions_2026-09-20_batch595.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page-123-doucette-downey_batch-595_2026-09-20.json
python3 -m oss_research research --source loc --batch page-123-doucette-downey-b595 --max-queries 20 --resume
python3 -m oss_research export-adapter-checkpoints
python3 -m oss_research export-derived
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
```

Do not automate the CIA Reading Room search route while its current robots policy disallows it. The remaining page-123 people need official and institutional source checks, namesake rejections, and physical personnel-file examination where online sources cannot establish identity or chronology.
