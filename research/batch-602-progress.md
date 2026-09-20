# Batch 602: NARA index pages 132–134, Edgerton through Ellis

Original NARA personnel-index PDF pages 132–134 were rendered at 170 dpi and
visually compared against every extracted row, 46 per page. All 138 immutable
source rows match the printed names, initials, suffixes, rank and protected-
identifier column occupancy, boxes, notes, and archive locations. The source
itself splits Alger C Ellis Jr.'s rank and identifier between columns; the raw
fields remain unreconstructed. The distinct page-review count is now
**106/522**, with **416** pages still to certify. Ingest validation passes:
**23,978/23,978** rows are linked, all 522 pages are represented, and SQLite
has no foreign-key errors.

Page 132 contains 46 printed rows representing 44 cautiously resolved
people. A rate-limited Library of Congress batch made 44 read-only searches
with no adapter errors or rate-limit blocks. Eight people yielded 28
newspaper-page discovery candidates, all still unreviewed leads. Thirty-six
people had no LoC result in that one source. Their research remains in
progress, not `no_reliable_result_after_protocol`: a single newspaper search
does not satisfy the documented multi-source protocol. The 45 people on page
133 (including one already verified) and 46 on page 134 are assigned to
separate resumable batches but have not received new adapter searches here.

Four possible-duplicate pairs now have explicit private review notes and
separate public profiles: the two Kay Edmonston rows (Boxes 212/213), Charles
F Edson and Charles F Edson Jr. (Boxes 212/213), Robert M Elliot/Elliott
(Box 217), and Herman Ebeling/Hermann Elbeling (Boxes 211/215). The last
pair has different protected identifiers; that difference weighs against a
silent merge. James/James H Edminster already had a serial-conflict group;
the two Eugene D Edmunds, Robert B Edris, and William E Eisemann source-row
pairs remain preserved despite cautious person linkage.

The existing Carl F. Eifler record on page 133 was reviewed against an
[official Army biography](https://www.ikn.army.mil/apps/MIHOF/biographies/Eifler%2C%20Carl.pdf)
and [National Park Service's documented OSS history](https://www.nps.gov/articles/oss-in-action-the-pacific-and-the-far-east.htm).
The Army source records his early-1941 K Company command and 1942 COI
assignment. NPS additionally records a post-Pearl Harbor Hawaii military-
police command between them, and explicitly identifies his pre-service
employer as the U.S. Customs Service. [NARA's RG 226 chronology](https://www.archives.gov/research/holocaust/finding-aid/military/rg-226.html)
dates OSS's succession to COI to 13 June 1942. The profile therefore treats
COI as the immediate institutional predecessor, Customs as the last named
civilian employer, and both Army commands as earlier military assignments.
Exact unit designation, assignment dates, and individual transfer orders
still require Box 214 and military-record review. His father's oil-field
work does **not** place Eifler in the oil-company employee category.

Current coverage: 23,978 linked source rows; 23,940 active people; 6,278
with saved nonplanned attempts (26.2239%); 269 with confirmed/high published
employer evidence (1.1236%); 614 with confirmed/high published affiliation
evidence (2.5647%); 5,751 with archival-review dispositions (24.0226%);
17,662 `not_started`; and 275 possible-duplicate groups. Private claim-
confidence counts are 1,311 confirmed, 1,862 high, 1,368 medium, 185 low,
and 132 conflicting. The full-index minimum research protocol is **not** met.

Replay from the repository root after importing earlier checkpoints:

```sh
python3 -m oss_research import-page-reviews research/parser_visual_review_pages132-134_2026-09-20.json
python3 -m oss_research assign-page-batch --batch-name page-132-edgerton-ehrman-b602 --page 132 --first-row 1 --last-row 46
python3 -m oss_research assign-page-batch --batch-name page-133-ehrsam-elgin-b602 --page 133 --first-row 1 --last-row 46
python3 -m oss_research assign-page-batch --batch-name page-134-elias-ellis-b602 --page 134 --first-row 1 --last-row 46
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
python3 -m oss_research import-reviewed-evidence research/evidence-eifler-timeline-correction_batch-602_2026-09-20.json
python3 -m oss_research import-reviewed-evidence research/evidence-page132-134-duplicate-review_batch-602_2026-09-20.json
python3 -m oss_research validate-ingest
python3 -m oss_research export-derived
python3 -m oss_research build-public-data
python3 -m oss_research coverage-report
```

Next bounded searches can resume with
`python3 -m oss_research research --source loc --batch page-133-ehrsam-elgin-b602 --max-queries 46 --resume`
and the page-134 batch under the same budget. The local SQLite database stays
private; the versioned attempt checkpoint has no raw LoC API payload. The
NARA Catalog API key was not available in the local environment and was not
used or placed in any tracked file.
