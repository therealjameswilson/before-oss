# Methodology

## Scope

The default `RESEARCH_SCOPE=all_personnel` includes every printed personnel row,
not only commissioned officers. The index includes military, civilian,
technical, administrative, foreign, and Allied personnel. A separate
commissioned-officer flag supports filtering without redefining the source.

## Source extraction

The frozen source is the official NARA PDF for Record Group 226, Entry A1-224.
Its SHA-256 is
`7268492342ab131d3b6d2697cfa4f6856cbdcd16e0ed3877e8d6a0478f58c02b`.

Extraction uses embedded text rather than indiscriminate OCR:

1. `pdftotext -layout` preserves complete row text.
2. `pdftotext -bbox` supplies word coordinates for column assignment.
3. Page-by-page row counts and line content must agree.
4. Repeated headers and footers are identified by position and content.
5. OCR is reserved for a page or row that embedded text cannot recover.

Raw fields are immutable. Normalized names, ranks, categories, service numbers,
boxes, and locations are separate fields.

## Extraction QA

All 522 pages were processed. Pages 1–521 contain 46 printed rows each; page 522
contains 12, for a total of 23,978. Visual selection includes:

- first five pages;
- middle five pages;
- final five pages;
- 50 deterministic random pages using seed 226224;
- every parser-warning page;
- every anomalous row-count page.

The 65 selected pages were rendered and visually inspected. Parser fixtures
cover missing first names, initials, suffixes, apostrophes, hyphens, foreign
notes, civilian grades, military ranks, column shifts, and unfamiliar values.

## Rows and entities

A `source_record` is one printed line and is never deduplicated. A
`person_entity` is a cautious resolution target. The first automatic pass merges
rows only when both normalized full name and non-empty normalized service number
match. It does not merge on name alone.

Same service numbers attached to different names are retained as possible
duplicate or conflict groups. Common-name research requires at least two
corroborating identifiers beyond the name. Manual decisions are append-only and
imported from CSV.

Identity states are `confirmed`, `high_confidence`, `probable`, `ambiguous`,
`conflicting`, and `unresolved`. Default employer analytics admit only confirmed
or high-confidence identities.

## Affiliation model

The project keeps three questions separate:

1. **Immediate pre-OSS affiliation**: the last documented organization, status,
   or assignment immediately before OSS recruitment, employment, transfer, or
   assignment.
2. **Last civilian employer before wartime service**: the final identifiable
   civilian employer before military service or an intervening wartime
   government assignment.
3. **Other documented pre-OSS employment**: earlier work established as pre-OSS
   without proof that it was immediate.

Relationship types distinguish employment, self-employment, military and
government assignments, student status, unemployment, retirement, volunteering,
professional affiliation, and unknown relationships.

## Time, sources, and confidence

Temporal basis is assessed independently as `explicit_immediate`,
`strongly_date_bounded`, `probable_immediate`, `documented_prewar`, or
`temporal_relation_uncertain`.

Source quality runs from `A_direct_official` through `E_discovery_only`.
Wikipedia, Wikidata, genealogy trees, snippets, and generated summaries may
produce leads but cannot independently support a published employer claim.

Claim confidence is `confirmed`, `high`, `medium`, `low`, `unresolved`, or
`conflicting`.

- Confirmed and high claims may be published as normal facts.
- Medium claims are visibly qualified.
- Low candidates remain in the private review system.
- Conflicts remain visible and are excluded from default aggregates.
- Unresolved profiles remain public with a research-status explanation.

## Minimum completed-research protocol

`no_reliable_result_after_protocol` is permitted only after recording:

- a NARA OSS/index-context check;
- a CIA Reading Room or equivalent official-source check;
- exact-name OSS searches using meaningful variants;
- an employment- or occupation-focused search;
- an applicable institutional, newspaper, obituary, directory, or archival check;
- reasons plausible candidates were rejected;
- whether the indexed physical personnel file should be reviewed.

An automated query alone is not a completed research outcome.

## Source adapters

The NARA adapter reads its key from the process environment, sends it only in
the `x-api-key` header, redacts logs, enforces persistent monthly usage limits,
uses deterministic fingerprints, bounded retries, timeouts, backoff, jitter, and
never persists response bodies. It minimizes live results to stable NAID
pointers and project-authored review notes.

The Library of Congress adapter uses the current loc.gov Chronicling America
collection API. CIA Reading Room HTML is parsed in memory for document links;
access failures are logged without bypass attempts. General web searches are
exported as reviewable discovery plans instead of scraping search-result pages.

## Organization normalization

Names as found are preserved. Canonical organizations are separate records with
historical names, aliases, locations, parent and successor relationships, active
dates, and normalization notes. Subsidiaries, departments, campuses, newspapers,
law-firm variants, and government bureaus are not silently collapsed.

## Public data

The site is a static projection generated from SQLite. It excludes full service
numbers, credentials, private notes, rejected and low-confidence candidates,
restricted data, raw API payloads, and copied source pages. Default aggregates
count unique person entities and exclude unresolved, conflicting, and
low-confidence claims.
