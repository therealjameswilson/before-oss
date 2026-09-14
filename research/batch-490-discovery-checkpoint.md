# Batch 490 discovery checkpoint

2026-09-13 UTC. This checkpoint covers personnel-index PDF page 97 rows
18-27, Robert E Cramer through Wallen L Crane. Page 97 was rendered at 180 dpi
and visually checked against the extracted rows. Literal private identifiers
are omitted.

## Cohort and disposition

| PDF row | Source record | Person entity | Indexed name | Box | Disposition |
|---:|---|---|---|---:|---|
| 97:18 | 7b66c951-d545-5607-bf65-1e5b69998f0e | da4dfe5c-22d3-5b67-8f7c-0375a5ec9dcd | Robert E Cramer | 151 | Unresolved; three name-only Army candidates and a middle-initial conflict are insufficient |
| 97:19 | 5543532d-f6e6-58cc-ba3d-ac9b2264533b | 61917fef-ca77-5346-a638-2ecae50cb5af | Joseph Crampes | 152 | Confirmed enlisted Army identity; qualified cook occupation at Army entry, no employer |
| 97:20 | 37ad2f3c-6f31-5f2a-b67d-7063f9bc8149 | 10ab749d-8f12-56b5-a94a-c1125aa02701 | Burton Crane | 152 | High-confidence Louis Burton Crane Jr. identity; New York Times is the best-supported last civilian employer, and The Japan Advertiser is earlier documented employment |
| 97:21 | 294c895a-ef50-57ff-a8c6-9441f830a9c0 | 1e569e97-758d-5ce7-a2b0-d7a062fe81bb | Donald J Crane | 152 | Unresolved; two name-only Army rows cannot be selected |
| 97:22 | 5ede8adb-7891-5b6c-bfa7-6c8e0c884847 | 83211d34-6b53-5b18-a0f3-0cd6b1ca330b | Elizabeth J Crane | 152 | Unresolved; no reliable OSS-linked identity source found |
| 97:23 | ce86499e-f711-51cf-b74c-e653c343b960 | b9bc8f09-be2a-5e00-9d1e-3381de354ebb | Gordon Crane | 152 | Unresolved; the literal seven-digit value was not padded and the name-only Army candidate is not linked |
| 97:24 | ad984e4a-9d77-577c-bd55-954eccb33544 | 5ca1c0c7-4f2e-5bdb-ad48-8f966335cc9e | Milton Crane | 152 | Unresolved; Army, publishing and academic namesakes lack an OSS bridge |
| 97:25 | 33198b56-3e7f-5f4d-baf7-30de9fa877bd | 013ad579-90cc-59a9-8730-176c39ec83a1 | Robert Crane | 152 | Unresolved; incomplete common name and multiple unbridged candidates |
| 97:26 | b3082fc9-3840-57b2-9d01-f0157e1a54da | 15e9302b-486b-5828-835b-d0fa419a11f7 | Rufus S Crane Jr. | 152 | Confirmed enlisted Army identity; qualified actor occupation category at Army entry, no employer |
| 97:27 | 6fdc0c82-8bf9-58fb-9338-4493a4afc3e4 | 51677744-32cc-5e49-bd53-54451ff13c2c | Wallen L Crane | 152 | Confirmed enlisted Army identity; qualified managers/officials occupation category at Army entry, no employer |

All ten rows are at location 230/86/29/03. The next printed row is Virginia
Crate, page 97 row 28, in Box 152.

## Official Army-file adjudication

The complete official Army merged file was scanned once across all 9,200,232
fixed-width records. The downloaded ZIP contained 185,043,578 bytes and had
SHA-256 `80c46e83937c6483d11def47fbb1629cab0ac135694fdfa09268b66d826f1066`;
the extracted data file contained 837,221,112 bytes and had SHA-256
`db10dbf90f0ef95dc327b0e8f8f0489923941b65399cf79bba71ac4b45d07e5b`.
These are transient official inputs and are not committed.

Joseph Crampes, Rufus S. Crane Jr. and Wallen L. Crane have exact full-name
and private-identifier agreements with Army records. Their selected records
date entry as privates on 30 June 1942, 12 February 1942 and 26 April 1944.
Official Code No. 30 defines their recorded civilian-occupation codes as
cooks except private family; actors and actresses; and managers and officials
not elsewhere classified. The categories are published only as medium-
confidence, strongly date-bounded occupations. None supplies a named
employer, workplace, precise role, immediate pre-OSS relationship or the
Army-to-OSS sequence.

Robert E. Cramer, Donald J. Crane, Gordon Crane, Milton Crane and Robert Crane
produced multiple or single exact-name Army rows, but none has a usable
identifier bridge. Gordon Crane's printed seven-digit value remains literal
and was never padded. Elizabeth J. Crane's name non-hit is not negative
evidence: the Army merged file is incomplete and is not a comprehensive OSS,
officer, Navy, women's-service or foreign roster.

## Burton Crane employment evidence

The Franklin Institute's institutional finding aid identifies Louis Burton
Crane Jr., born in 1901 and educated at Princeton, under the professional name
Burton Crane. It states that he was financial editor of The Japan Advertiser
in Tokyo from 1925 to 1936, a financial writer for the New York Times from
1937, and head of OSS intelligence in Kunming during World War II. That
unusually specific same-source chronology supports a high-confidence identity
match and treats the New York Times as the best-supported last civilian
employer before wartime service. The evidence does not say that he left the
newspaper directly to join OSS or give a transfer date, so the temporal basis
is `probable_immediate`, not `explicit_immediate`. The Japan Advertiser role
is retained separately as `documented_prewar` employment.

His commissioned status remains unknown. The finding aid supplies an OSS post
but no military grade, and the index prints no rank. The site therefore does
not turn an intelligence leadership role into an officer classification.

## CIA, Library of Congress and web adjudication

One bounded CIA Reading Room exact-name query and one current Library of
Congress employment query completed for every person, with additional LoC
occupation fallbacks where useful. CIA returned no adapter candidates.
Library of Congress returned ten candidates. Every candidate was opened in
official page JSON/OCR context and rejected through the imported review-
decision CSV; a repeat import skipped all ten as duplicates, proving
idempotency.

The rejected material comprises incompatible middle initials, common-name
Army and Navy notices, unrelated local officials, split-name OCR, fiction and
other namesakes lacking an OSS or Box 151/152 bridge. Exact-name OSS,
employment, occupation, institutional, newspaper, obituary, directory,
military and archival searches were completed for the cohort. No additional
named employer was established, and no claim was inferred from a name-only
match, occupation category, later career or prominent biography.

The tracked adapter checkpoint now contains 2,259 attempts, 455 candidates
and 45 person updates. Batch 490 adds 29 machine attempts and ten adjudicated
candidates; its ten synthesized outcomes are stored separately in the durable
research-attempt history.

## Archival next actions

Box 151 is needed to identify Robert E. Cramer. Box 152 is needed to confirm
Burton Crane's personnel status and exact newspaper-to-OSS chronology;
establish the Army-to-OSS sequence and any named employer for Joseph Crampes,
Rufus S. Crane Jr. and Wallen L. Crane; and identify Donald J., Elizabeth J.,
Gordon, Milton and Robert Crane. Every unresolved profile says that archival
examination may be required rather than asserting that no prior employment
existed.

No authenticated NARA Catalog API request was made.
