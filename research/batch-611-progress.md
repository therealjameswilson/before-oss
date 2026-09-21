# Batch 611: PDF pages 181–190 and bounded research

Original NARA PDF pages **181–190** were rendered at 180 dpi. All **460**
printed rows were compared against the immutable SQLite extraction for row
order, indexed spelling, initials, rank, private-identifier column occupancy,
box, notes, and archival location. All ten complete pages match the extraction;
there were no corrections. Page 184 was already represented in the ledger by a
row-specific parser-warning decision, so this ten-page pass adds nine distinct
pages. The replayed visual-review ledger is now **156/522 pages**; **366** pages
remain for complete-page comparison.

The parser-warning row on page 184 prints `6741` in the rank column. Its bbox
position differs from the private-identifier column used elsewhere on the page,
so the unfamiliar numeric rank is preserved exactly and is not silently moved
or decoded.

Nine possible-duplicate or spelling-variant groups were reviewed without
merging any source row or person entity. They include the Stephen F
Greigal/Griegal, Joseph A/L Grenci, duplicate James Grimes, Harry W/A
Grossglaus, Louis W Guadarelli/Guidarelli, Jackson E/no-initial Guernsey, Otto E
Gutman/Guttman, Ernestine Hambeurg/Hamburg, and Major John B/P Hamblet pairs.
The Grossglaus rows carry different private identifiers. The Guadarelli and
Guidarelli rows carry the same private identifier, box, and location, which is
strong duplicate evidence but not authority to destroy either printed row or
merge the people before file review. Every private value remains masked
publicly.

The bounded, read-only Library of Congress first pass completed **46** searches
for the page-146 queue. It created or revisited **58** discovery candidates,
with **21** people ending `candidate_found`, **25** ending `no_result`, one
completed query skipped as a duplicate, and no adapter errors or source-access
blocks. These newspaper-page leads are not accepted identity matches, employer
claims, or completed multi-source protocols. No authenticated NARA Catalog
request was made.

[Moses Hadas](https://therealjameswilson.github.io/before-oss/people/87a20fba-2949-53b1-9a30-b36933e71d23/)
now has a high-confidence Columbia University pathway. A Columbia institutional
biography describes his long classics career and explicitly sequences his work
as professor, OSS service, and return to professorial work. Columbia is
therefore published as both his strongly date-bounded immediate pre-OSS
affiliation and last documented civilian employer before service. The evidence
does not supply exact leave, recruitment, or return dates; Box 302 remains the
next action. A duplicate historical Columbia organization record with no linked
affiliations was removed after Chester L Cooper and Hadas were both confirmed
against the canonical Columbia record.

At this checkpoint, **23,978/23,978** printed rows link to **23,940** active
person entities. Research-attempt coverage is **6,916/23,940 (28.8889%)**;
confirmed/high verified-employer coverage is **273/23,940 (1.1404%)**;
confirmed/high verified-affiliation coverage is **621/23,940 (2.5940%)**;
archival-review disposition coverage is **5,864/23,940 (24.4946%)**. There are
**17,024** `not_started` people, **322** active possible-duplicate groups, and
**128** active people with conflicting identity or source status. The DB stores
**11,969** attempts or plans and **4,878** claims: **1,311** confirmed,
**1,877** high, **1,373** medium, **185** low, and **132** conflicting. It
contains **5,023** source/citation records and **2,350** unique document keys.
The public projection has **2,211** affiliations, **696** organizations,
**3,820** sources, and **4,689** claims. Full-index historical research is
unfinished.

Local QA passed: **126** Python unit tests; **81/81** bounded desktop, phone,
and tablet release checks; the **200-profile structural** audit; the
**24,695-page** internal-link check; the public-number redaction scan across
**24,767** artifacts; and the static Astro build with zero errors, warnings,
or hints across **243** source files. The structural sample is **not** the
required 200-profile manual historical source audit. An unrelated untracked
duplicate Sources route adds 25 local-only pages and is excluded from the clean
release. Clean CI and public deployment require separate verification.

## Replay and continuation

After importing the prior durable batches into private SQLite:

```sh
python3 -m oss_research import-page-reviews research/parser_visual_review_pages181-190_2026-09-21.json
python3 -m oss_research import-reviewed-evidence research/evidence-pages181-190-duplicate-review_batch-611_2026-09-21.json
python3 -m oss_research import-reviewed-evidence research/evidence-moses-hadas_batch-611_2026-09-21.json
python3 -m oss_research import-reviewed-evidence research/evidence-pages-ninety-one-ninety-two-robert-e-coon-through-delia-a-cooper-pathways_batch-465_2026-09-10.json
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
python3 -m oss_research export-derived
python3 -m oss_research build-public-data
python3 -m oss_research coverage-report
```

The page-181 through page-190 queues are assigned durably in private SQLite.
Continue the bounded discovery queue with `python3 -m oss_research research
--source loc --batch page-147-fischer-flaherty-b607 --max-queries 46 --resume`.
No API key, full service number, raw API response, or private reviewer note is
committed or included in the public site.
