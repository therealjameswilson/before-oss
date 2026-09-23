# Batch 646: PDF pages 7-17 and Meader-Meedsellen research

All **506** printed rows on original NARA PDF pages 7-17 were compared against
SQLite at 180 dpi. Page 9 had already received a reviewed correction, and all
other rows match the current extraction. The ten newly completed pages add
**460** visually verified rows. Complete-page visual review now covers
**448/522 pages** and **20,574/23,978 rows**: **20,542** reviewed rows match the
extraction, **32** retain reviewed corrections, and **3,404** remain for
complete visual comparison. All parser validation checks pass.

The page-314 `Edwin E. Meader` through `D. Meedsellen` queue contains **22**
source rows representing **22** cautious person entities. All 22 received
staged project query plans and a saved manual review attempt. Nine preexisting
official Army candidates received explicit decisions: six accepted and three
conflicting. The accepted protected-identifier crosswalks cover Edwin E.
Meader, Francis Meadowcraft, Bernard C. Meaton, Henry J. Medieros, Manuel
Medieros, and Herbert G. Medric. The project preserves two Army-record
conflicts for Joseph B. Medagliant and the concatenated-name conflict for Aneo
Mediler; none was silently corrected.

The evidence bundle adds six affiliations. Edwin E. Meader now has a cited
last civilian employer, Kalamazoo Vegetable Parchment Company, plus the Army
as his best-supported immediate institutional pathway into OSS. Contemporary
Foreign Service notices document Donn P. Medalie's State Department career,
but the exact State-to-OSS transition remains unresolved. David C. Meck Jr.'s
John Marshall School of Law and Federal Security Agency roles are published
only as medium-confidence qualified affiliations for a probable identity.
An official CIA history establishes that Coast Guard Chief Warrant Officer
Thomas O. Medlicott was assigned to OSS duty in Operational Swimmer Group II.

Lorraine M. Meader and Lorraine M. Meador remain separate probable entities in
one visible duplicate group pending review of both Box 514 jackets. Joseph
Medaglian and Joseph B. Medagliant also remain separate because their initials,
ranks, and protected identifiers differ. Search-result snippets, people-finder
records, genealogy pages, unrelated namesakes, and Army occupation codes were
not promoted to employment evidence.

The final 22-person queue state is **16** `in_progress`, four
`needs_identity_review`, one `conflicting_sources`, and one
`verified_employer_found`. Full identifiers remain private.

Rebuilt coverage is **23,978/23,978** linked source rows and **23,939** active
person entities. Research-attempt coverage is **7,967/23,939 (33.2804%)**;
confirmed/high verified-employer coverage is **281/23,939 (1.1738%)**;
confirmed/high verified-affiliation coverage is **632/23,939 (2.6400%)**;
archival-review disposition coverage is **6,425/23,939 (26.8390%)**. There are
**15,967** `not_started` people, **492** active possible-duplicate groups, and
**173** active people with conflicting identity or source status. The database
stores **13,239** attempts or plans and **5,030** claims: **1,311** confirmed,
**1,993** high, **1,391** medium, **187** low, and **148** conflicting. It
contains **5,091** source/citation records and **2,400** unique document keys.
The public projection contains **2,232** affiliations, **712** organizations,
**3,884** sources, and **4,839** claims.

The oil-company category remains prominently available at the top of the site
and remains a supported, incomplete evidence set of **seven people across nine
historically named companies**. Full-index historical research is unfinished.

## Replay and continuation

After importing prior durable batches into private SQLite:

```sh
python3 -m oss_research import-page-reviews research/parser_visual_review_pages7-17_2026-09-23.json
python3 -m oss_research import-review-decisions research/identity_review_decisions_2026-09-23_batch646.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page314-meader-meedsellen-review_batch-646_2026-09-23.json
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
```

Continue with the next bounded research and visual-audit batch, then rebuild:

```sh
python3 -m oss_research export-adapter-checkpoints
python3 -m oss_research export-derived
python3 -m oss_research build-public-data
python3 -m oss_research coverage-report
```

No API key, full service number, raw Catalog API response, copyrighted page
image, or private reviewer note is committed or included in the public site.
No authenticated NARA Catalog request was made.
