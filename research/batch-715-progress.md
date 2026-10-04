# Batch 715: Oflaherty-Ohara research

Batch 715 covers PDF page 348, rows 1-23, from **Julian A Oflaherty**
through **James W Ohara**. A 300-dpi visual inspection confirmed all 23
printed rows, representing 23 active person entities. The immutable extraction
is unchanged. Original spellings, ranks, grades, box numbers, and the source
note **possibly** attached to Marbury B Ogle remain recoverable. The rows span
Boxes 569-570 at location 230/86/37/07.

Six people receive high-confidence identity matches from the official Army
bulk file. Thomas A Ogden, Ezra G Ogletree, Warren A Ogren, Edward C Ohara,
and James F Ohara have exact names plus nonshared protected identifiers.
Louis Oguss appears twice in the Army bulk file with the same exact name and
protected identifier; both official rows remain in the private audit trail and
are treated as duplicate source entries, not as two people. Those duplicate
rows account for seven accepted candidate decisions across six people. Ezra's
**Jr.** suffix is preserved as a documented variant. No coded Army occupation
was converted into an occupation or employer claim.

The eighth Army candidate is a material conflict. The visually verified index
prints **Edward Ogden**, while the protected identifier points to **OGDEE
EDWARD**. That candidate is formally rejected, neither spelling overwrites the
other, and Box 569 is required before any merge.

The best-supported employment profile is **Marbury B Ogle**, identified at
high confidence as Marbury Bladen Ogle Jr. A Purdue-authored obituary explicitly
states that he served as senior organizational analyst in a Department of
Justice special war policy unit in 1943-44 and then joined the OSS Analysis
Branch. The site therefore distinguishes his immediate pre-OSS government
assignment from his last civilian employer, Western Reserve University
(1937-42), and from his earlier employment as an Ohio State political-science
instructor through 1937. Western Reserve's historical name is preserved rather
than replaced by its modern successor.

**John F Oglevee** remains a probable identity. Official Ohio State Board of
Trustees minutes document a John F. Oglevee as a Reader in History effective
January 1, 1944. That affiliation is published at medium confidence with
`temporal_relation_uncertain`; it is not labeled immediate pre-OSS or last
civilian employment until Box 569 establishes the sequence. The nineteenth-
century John Finley Oglevee was rejected as a namesake.

**Dorothy T Ogata** remains a probable identity. Brian Masaru Hayashi's
scholarly study names a Dorothy Ogata as an OSS colleague, but omits the middle
initial and supplies no pre-OSS employer. **Patrick Ohanlon** reaches
high-confidence identity as British Intelligence Corps lieutenant-colonel
Patrick Hudson O'Hanlon through the uncommon name, matching rank, and official
London Gazette notice of a U.S. Medal of Freedom with Bronze Palm. The profile
does not label the Intelligence Corps role an immediate predecessor because the
notice does not state an OSS transition date.

Postwar directory leads for Phyllis Ogrean, a younger Shirley Ogren namesake,
Louis Oguss correspondence in National Maritime Union papers, common O'Hara
officers, genealogy pages, and modern people-search results were rejected or
kept as private discovery leads. None establishes a defensible pre-OSS
employer.

The CIA and Library of Congress adapters each made one bounded attempt and
failed closed. The web adapter recorded 23 deterministic planned queries
without making live requests. Manual staged review completed official,
exact-name OSS, employment, occupation, obituary, institutional, newspaper,
directory, military, and archival search families for every person.

The cohort ends with 18 `no_reliable_result_after_protocol`, two
`requires_archival_review`, one `completed`, one `needs_temporal_review`, and
one `conflicting_sources` outcome. Identity statuses are eight
`high_confidence`, two `probable`, one `conflicting`, and 12 `unresolved`.
The reviewed bundle imports six sources, three organizations, four
affiliations, 15 claims, 26 claim-source links, 23 person updates, and 23
consolidated research attempts. Eight manual identity-review decisions are
recorded: seven accepted identity matches and one rejected surname conflict.

Rebuilt coverage is **23,978/23,978** linked source rows and **23,939** active
person entities. Research-attempt coverage is **9,483/23,939 (39.6132%)**;
confirmed/high verified-employer coverage is **326/23,939 (1.3618%)**;
confirmed/high verified-affiliation coverage is **722/23,939 (3.0160%)**;
archival-review disposition coverage is **7,941/23,939 (33.1718%)**. There are
**14,451** `not_started` people, **523** possible-duplicate groups, and **296**
active conflicts. SQLite stores **17,214** attempts or plans and **6,106**
claims: 1,352 confirmed, 2,793 high, 1,504 medium, 198 low, 257 conflicting,
and two unresolved. It contains **5,584** citation records and **2,800** unique
source documents. The public projection contains **2,431** affiliations,
**837** organizations, **4,365** sources, and **5,899** claims. Full-index
historical research remains unfinished.

## Replay and continuation

After importing prior durable batches into private SQLite:

```sh
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
python3 -m oss_research assign-page-batch --batch-name batch-715 --page 348 --first-row 1 --last-row 23
python3 -m oss_research research --source cia --batch batch-715 --max-queries 23
python3 -m oss_research research --source loc --batch batch-715 --max-queries 23
python3 -m oss_research research --source web --batch batch-715 --resume --max-queries 23 --dry-run
python3 -m oss_research import-review-decisions research/identity_review_decisions_2026-10-04_batch715.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page348-oflaherty-ohara-review_batch-715_2026-10-04.json
python3 -m oss_research export-adapter-checkpoints
python3 -m oss_research export-derived
python3 -m oss_research export-review-queue
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
```

Adapter checkpoints must be imported before final reviewed decisions and
evidence so temporary discovery states cannot supersede reviewed dispositions.
The next research boundary begins at PDF page 348, row 24 (**John H Ohara**).

No API key, full service number, raw Catalog or LoC API response, copyrighted
page image, unrelated Army coded occupation, street address, modern
people-finder record, or private reviewer note is committed or included in the
public site. No authenticated NARA Catalog API request was made for this batch.
