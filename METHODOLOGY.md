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

Ninety-six pages have durable, replayable visual decisions. The current audit
rules select 92 of them; four additional pages retained from earlier checks are
also reviewed. Twenty-three values
are printed in the table's `M I` column while their rank cells are blank: six
civilian grades and seventeen military grades. Their raw cells remain
unchanged. The normalized names omit the displaced grade, the normalized rank
and personnel category use it, and every affected row carries a parser warning
plus a replayable row-specific visual-review decision. Page 117 contains two
independently reviewed military-grade corrections; the importer therefore
validates unique page-row coordinates rather than assuming one correction per
page. Eight additional rows contain all-numeric values visibly printed in the
rank column. Parser version `bbox-columns-v8` preserves those raw cells, emits
`serial_number_printed_in_rank_column`, and normalizes the value as a probable
serial identifier while leaving rank unknown. The public projection masks both
the identifier and the anomalous rank-cell display. Page 46 adds one combined
shift: Wilfred Boulay's printed row places `T/Sgt` under M I, a numeric
identifier under rank, and `Jun-43` under serial. Version `bbox-columns-v8`
normalizes the first two values as rank and private identifier while treating
the third as a date annotation, and emits a dedicated warning. The complete coordinates
and expected raw values are retained in
`research/parser_visual_review_decisions.json`. Parser fixtures cover missing
first names, initials, suffixes, apostrophes, hyphens, foreign notes, civilian
grades, military ranks, numeric rank-column anomalies, the combined
rank/identifier/date shift, multiple column shifts on one page, and unfamiliar
values.

Version `bbox-columns-v8` also recognizes an identical suffix printed in more
than one name column. It emits one normalized suffix while preserving every raw
cell and recording the duplicate-suffix normalization note.

## Rows and entities

A `source_record` is one printed line and is never deduplicated. A
`person_entity` is a cautious resolution target. The first automatic pass merges
rows only when both normalized full name and non-empty normalized service number
match. It does not merge on name alone.

Same service numbers attached to different names are retained as possible
duplicate or conflict groups. Common-name research requires at least two
corroborating identifiers beyond the name. Manual decisions are append-only and
imported from CSV.

When an exact private identifier resolves to a different name in an official
military file, the project records a visible identity conflict rather than
silently correcting either source. The unrelated subject's name and full
identifier are not copied into public evidence, downloads, or conflict text.
The indexed personnel file receives critical archival-review priority because
only the source file can establish whether the index contains a transcription
error, a reassigned identifier, or another documentary problem.

When direct evidence establishes that two differently printed rows represent
one person, a versioned `person_entity` review decision names the canonical
entity and records the rationale. Both source rows and the superseded entity
remain stored for audit; row links, claims, and attempts move to the canonical
entity. Public profiles and coverage denominators count only active entities.
The private `entity_supersessions.csv` export makes every such decision
inspectable and reproducible.

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

First-person or institutional accounts may establish a military-to-OSS transfer
even when no civilian employer is known. Such evidence is published as an
immediate military assignment and never relabeled as employment. If credible
sources agree on an affiliation but disagree on a detail such as duration, the
shared fact may be published with the disputed detail omitted and the conflict
explained in the evidence notes.

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
collection API. It applies configured timeouts and bounded retries, respects
numeric `Retry-After` instructions, and records terminal transport failures in
the durable request audit. Transient terminal failures remain eligible for a
later resumable retry; successful and non-transient completed requests retain
their deterministic fingerprint checkpoint. CIA Reading Room HTML is parsed in memory for
document links; access failures are logged without bypass attempts. General web
searches are exported as reviewable discovery plans instead of scraping
search-result pages.

CIA Reading Room OCR is discovery evidence, not an identity decision. When a
released document is available as an image-only PDF, the relevant page is
rendered and inspected before the document supports a public claim. A document
that confirms wartime OSS context but says nothing about the predecessor role
may strengthen identity while leaving the pre-OSS affiliation unresolved.

The official unrestricted Army Serial Number Merged File is used only for
eligible enlisted records and only when the indexed private identifier and
name agree. Its own documentation warns of transcription errors, missing
ranges, duplicate identifiers, and the absence of officer records. Civilian-
occupation codes are expanded only when NARA's compiled code list supplies an
unambiguous definition. When the official raw-code layout and a retired
derivative interpretation disagree, the code is preserved privately and no
occupation or employer is published. A code describing `STUDENTS` is modeled
as student status, never employment, and no school is inferred.

Adapter audit rows needed to reproduce aggregate coverage are exported to the
tracked `research/adapter_attempt_checkpoints.json` file. This deliberately
sanitized checkpoint retains stable attempt and candidate identifiers,
fingerprints, outcomes, timestamps, and current queue state, but excludes query
text, service identifiers, credentials, response bodies, and private notes.
During a clean rebuild, adapter checkpoints are replayed first, followed by
their contemporaneous human review decisions and then the reviewed evidence
bundles in numeric batch order. This preserves chronology: a later completed
review supersedes an earlier discovery-stage decision.

Parser visual-review decisions are separately preserved in
`research/parser_visual_review_decisions.json`. The rebuild replays those
decisions after extraction and before the validation gate, verifies that every
corrected coordinate still contains the expected raw cells, and then requires
all selected pages and warning rows to have a terminal visual-review state.

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
