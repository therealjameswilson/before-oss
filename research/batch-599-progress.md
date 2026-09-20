# Batch 599: NARA index page 127, Dulac through Dunlap

The original NARA PDF page 127 was rendered and all 46 printed rows were
compared with the extracted source rows. Box transitions 203→204→205,
locations, the `British A` note, and serial-column occupancy match. The
source really spells `Dullles` for Allen W.; the three consecutive l letters
are preserved, with `Dulles` only as an unconfirmed search alias. The
truncated `Dumesnil-Rev` surname and first-name cell `H` are also preserved.
Page 127 had already been visually reviewed, so the distinct-page QA count
remains 100 of 522, not 101. Parser warnings remain resolved.

Forty-five people received a successful Library of Congress Chronicling
America search in two bounded cohorts (`page-127-dulac-dumas-b599` and
`page-127-dumm-dunlap-b599`); `H Dumesnil-Rev` was already in the pilot
research queue. Thirteen newspaper-page discovery candidates were saved.
They are not employer evidence until page context and identity are reviewed.
The one failed sandbox DNS attempt was retried successfully; final adapter
results recorded zero errors and zero rate-limit blocks. Two duplicate
query plans were skipped in the second cohort.

Twelve official Army Serial Number Merged File leads received private
review decisions: ten accepted on exact name plus nonshared protected
identifier (including John C Dumont / `DU MONT JOHN C` as a spacing-only
variant), and two held as probable because of an unexplained extra token
or missing middle initial. These are identity decisions only. Army
occupation codes are not named employers, and no full identifier appears
in public downloads. The repeated Joe B Duncan, repeated Russell Duncan,
and Joseph P Dunckley / Joseph P Dunkley rows remain distinct person
entities with visible possible-duplicate groups and Box 204–205 review
actions.

The page-127 Wilfred A. Dunderdale entry prints `Cmdr` and `British A`.
Zdzisław Jan Kapera's chapter in the Polish Institute of National
Remembrance's *L'Europe occupée* (2014), printed p. 193, places a
Wilfred Dunderdale with the British Secret Intelligence Service as a
Madrid intelligence contact before March 1941. The Polish Office for War
Veterans' *Kombatant* bulletin (October 2009), PDF p. 7, independently
names **Wilfred A. Dunderdale** as an SIS officer. Taken together with
the uncommon name and index's British-officer notation, this supports a
qualified **earlier government affiliation**. The publication is medium
confidence because Box 204 remains unexamined and neither source gives an
OSS transfer date. It is not an immediate-pre-OSS or civilian-employer
claim. [Historical chapter](https://ipn.gov.pl/download/1/1244361/OkupowanaEuropaFr.pdf)
and [veterans bulletin](https://www.kombatanci.gov.pl/images/DOC/Kombatant/2009/200910.pdf).

Two tempting famous-name assignments were withheld. Princeton's Allen W.
Dulles finding aid describes OSS telegrams but does not bridge to the
printed `Dullles` Box 203 entry, so Sullivan & Cromwell is not assigned.
Harvard's Clover Todd Dulles finding aid distinguishes Martha (Clover)
Todd Dulles from her daughter of the same name; a Wilson Center index
identifies the daughter as an OSS participant, but the NARA row lacks the
necessary identifying detail. Both require direct Box 203 file review.

Current local coverage after this batch: 23,978 of 23,978 source rows
linked; 23,940 active people; 6,053 with saved nonplanned research
attempts; 269 with confirmed/high published employer evidence; 613 with
confirmed/high published affiliation evidence; 5,725 with archival-review
dispositions. There are still 17,887 `not_started` people. Claim counts:
1,311 confirmed, 1,857 high, 1,369 medium, 185 low, 132 conflicting.
This batch does **not** satisfy the project-wide terminal-research protocol.

Replay commands from the repository root (with Python dependencies installed):

```sh
python3 -m oss_research import-page-reviews research/parser_visual_review_page127_2026-09-20.json
python3 -m oss_research import-review-decisions research/army_review_decisions_2026-09-20_batch599.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page-127-dulac-dunlap_batch-599_2026-09-20.json
python3 -m oss_research export-adapter-checkpoints
python3 -m oss_research export-derived
python3 -m oss_research build-public-data
python3 -m oss_research coverage-report
```

The durable private SQLite file is local, while the source review files,
sanitized adapter checkpoints, generated public assets, and browser tests
are versioned for reconstruction. A NARA Catalog API key is not present
in this checkout's environment; no authenticated Catalog call was made.
The source's physical personnel files remain the critical identity and
employment follow-up for the unresolved cases.
