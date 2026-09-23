# Batch 651: pages 65-74 extraction audit and Mercader-Merrick research

All **460** printed rows on original NARA PDF pages 65-74 were compared with
the immutable extraction at 180 dpi. Pages 69, 70, and 72 were already in the
visual-review set; the other seven pages and **322** rows received their first
complete visual comparison in this batch. Every row matches. Complete-page
visual review now covers **491/522 pages** and **22,552/23,978 rows**:
**22,520** reviewed rows match the extraction, **32** retain reviewed
corrections, and **1,426** remain unaudited. Every PDF page remains represented,
every parser warning is resolved, and SQLite integrity and foreign-key checks
pass.

The page-316/317 `Guillermo Mercader` through `Gordon Merrick` queue contains
**22 source rows and 22 cautious person entities**. Each person received saved
NARA, CIA Reading Room, Library of Congress, and targeted-web source work plus
a reviewed research outcome. NARA, CIA, and web adapters were dry-run plans;
the LoC adapter ran live in a bounded sequence. It produced **15** newspaper
candidates: ten for the two separate A. W. Merriam rows and five for Louis M.
Merly. All 15 were rejected after page-context review because they named other
Merriams, places called Merriam, or postwar OCR false positives, and supplied
no exact-name, service-identifier, OSS, or employment bridge. No authenticated
NARA Catalog request was made and no API key was stored or logged.

The principal findings preserve identity and chronology limits:

- **Benjamin D. Meritt** is a high-confidence identity based on exact uncommon
  name, P-5 context, Institute for Advanced Study records, and the Institute's
  1946 wartime report. His immediate predecessor is modeled as the Foreign
  Nationalities Branch of Donovan's organization, a government assignment that
  the source says became OSS. The Institute for Advanced Study is separately
  recorded as his last civilian employer before that 1941 assignment.
- **Gordon Merrick** is a high-confidence identity from his exact uncommon name
  and two Princeton sources documenting OSS service. The New York Post is his
  strongly date-bounded immediate affiliation and last civilian employer before
  early-1944 OSS training. The Washington Star and Baltimore Sun remain earlier
  documented newspaper employers.
- Indexed **Guillermo Mercader** remains a probable, not settled, match to
  French resistance member Guillaume Mercader. Institutional French sources
  establish the Bayeux cycle shop and Organisation civile et militaire
  chronology, but no source directly equates the Guillermo and Guillaume
  forms or provides an OSS entry date. The site therefore qualifies the
  identity, records the shop as last civilian work before resistance service,
  and does not label OCM an OSS unit or an immediate OSS predecessor.
- **Rene J. Mermet** has a high-confidence official Army identity bridge from
  exact indexed-name alignment and a nonshared protected identifier. No
  employer is inferred from Army occupation codes.
- **Ladislaus S. Merecicki/Marecicki** remains probable because the nonshared
  identifier agrees but one surname vowel differs.
- **David J. Merrell** remains conflicting because the printed identifier points
  to an unrelated official Army name. **William L. Meritts** remains
  conflicting because the same identifier appears with Marritts, Meritts, and
  Merritts source spellings. No records are merged and full identifiers remain
  private.
- The two **A. W. Merriam** rows remain separate: their ranks and protected
  identifiers differ, and all newspaper candidates were rejected.
- The existing **Peter G. Mero** high-confidence occupation result remains
  unchanged. His investment firm is still unidentified, so no employer was
  invented.

The cohort ends with **13** `in_progress`, three `needs_identity_review`, two
`conflicting_sources`, two `verified_employer_found`, one
`documented_prewar_employer_found`, and one `occupation_only_found` status.
Identity statuses are four `high_confidence`, 12 `unresolved`, three
`probable`, two `conflicting`, and one `ambiguous`. The reviewed evidence
bundle adds **15** claims: nine high, four medium, and two conflicting.

Rebuilt coverage is **23,978/23,978** linked source rows and **23,939** active
person entities. Research-attempt coverage is **8,075/23,939 (33.7316%)**;
confirmed/high verified-employer coverage is **288/23,939 (1.2031%)**;
confirmed/high verified-affiliation coverage is **642/23,939 (2.6818%)**;
archival-review disposition coverage is **6,532/23,939 (27.2860%)**. There are
**15,859** `not_started` people, **492** possible-duplicate groups, and **185**
active conflicts. SQLite stores **13,785** attempts or plans and **5,120**
claims: 1,311 confirmed, 2,056 high, 1,404 medium, 189 low, and 160 conflicting.
It contains **5,141** citation records and **2,442** unique source documents.
The public projection contains **2,260** affiliations, **737** organizations,
**3,931** sources, and **4,927** claims.

The oil-company category remains an evidence-scoped set of **seven people
across nine historically named companies**. None of the Batch 651 findings is
an oil-company employment claim. Full-index historical research is unfinished.

## Replay and continuation

After importing prior durable batches into private SQLite:

```sh
python3 -m oss_research import-page-reviews research/parser_visual_review_pages65-74_2026-09-23.json
python3 -m oss_research import-review-decisions research/identity_review_decisions_2026-09-23_batch651.csv
python3 -m oss_research import-review-decisions research/loc_review_decisions_2026-09-23_batch651.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page316-317-mercader-merrick-review_batch-651_2026-09-23.json
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
```

Continue with the next bounded research and extraction-audit batch, then run:

```sh
python3 -m oss_research export-adapter-checkpoints
python3 -m oss_research export-derived
python3 -m oss_research build-public-data
python3 -m oss_research coverage-report
```

No API key, full service number, raw Catalog API response, copyrighted page
image, or private reviewer note is committed or included in the public site.
