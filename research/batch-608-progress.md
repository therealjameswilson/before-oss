# Batch 608: PDF pages 151–160 and bounded research

Original NARA PDF pages **151–160** were rendered at 180 dpi. All **460**
printed rows were compared against the immutable SQLite extraction for row
order, indexed spelling, initials, rank, private-identifier column occupancy,
box, notes, and archival location. Pages 151 and 153 already had durable
`reviewed_after_correction` decisions and retain them; pages 152 and 154–160
add eight matching-only decisions. There were no new extraction corrections.
The distinct visual-review ledger is now **129/522 pages**; **393** pages
remain for individual comparison.

Ten new possible-duplicate or spelling-variant groups are marked ambiguous
without merging any source rows or person entities. They include two Walter L
Freund rows with distinct private identifiers, Carl/Karl Fuehrer, three
Franchenstein/Franckenstein/Frankenstein spellings, and same-private-identifier
Funari/Furnari and Gallagin/Galligan pairs. The latter pairs receive critical
manual-review priority, but the public data exposes neither the identifier nor
the private duplicate-group label. The other Fonse/Fosse, Fontenot/Foutenot,
Gallagher, and Gallech/Galleck pairs likewise remain separate pending file-level
comparison.

The bounded, read-only Library of Congress first pass completed **46** searches
for the page-142 queue and saved **15** unreviewed newspaper-page candidates.
The page-143 queue completed **46** searches and saved **32** candidates.
These are discovery leads, not accepted
identity matches, employer claims, or completed multi-source protocols. No
authenticated NARA Catalog request was made.

[Gero V Gaevernitz](https://therealjameswilson.github.io/before-oss/people/8b7344ea-c0e0-54b6-894a-90c64be8db07/)
now has a qualified **medium-confidence probable immediate professional
affiliation**. Gerhard Granier's institutional biography says that from 1939
Gaevernitz managed Edmund Stinnes's Swiss assets and worked as an import-export
merchant, then placed his knowledge and contacts at Allen Dulles's disposal.
A CIA-published history independently identifies him as Dulles's volunteer
assistant in Bern. The sources do not name a business employer, prove that the
civilian activity ended, or erase the distinction between informal assistance
and formal OSS service; Box 257 remains a high-priority archival review.

[Walter Galenson](https://therealjameswilson.github.io/before-oss/people/30a94b28-903c-51f8-8e80-d36f8c7271fb/)
has a **high-confidence earlier documented employment** claim from Cornell's
faculty memorial: after graduating from Columbia in 1935, he joined his
father's accounting firm before returning for the doctorate he received in
1940. The firm is unnamed. The memorial separately identifies War Department
and OSS work but does not establish the transfer chronology, so the profile
does not label either the accounting firm or War Department as the immediate
pre-OSS affiliation. Box 258 review is the next action.

At this checkpoint, **23,978/23,978** printed rows link to **23,940** active
person entities. Research-attempt coverage is **6,776/23,940 (28.3041%)**;
confirmed/high verified-employer coverage is **271/23,940 (1.1320%)**;
confirmed/high verified-affiliation coverage is **618/23,940 (2.5815%)**;
archival-review disposition coverage is **5,809/23,940 (24.2648%)**. There are
**17,164** `not_started` people, **297** possible-duplicate groups, and **128**
active people with conflicting identity or source status. The DB stores
**11,827** attempts or plans and **4,870** claims: **1,311** confirmed,
**1,869** high, **1,373** medium, **185** low, and **132** conflicting. It
contains **5,015** source/citation records and **2,342** unique document keys.
The public projection has **2,207** affiliations, **695** organizations,
**3,812** sources, and **4,681** claims. Full-index
historical research is unfinished.

Local QA passed: **126** Python unit tests; the **81/81** bounded desktop,
phone, and tablet release checks; the **200-profile structural** audit; the
**24,694-page** internal-link
check; the public-number redaction scan; and the static Astro build. The
structural sample is **not** the required 200-profile manual historical source
audit. The link checker inventoried **50,232** external URLs but did
not request every target. Clean CI and public deployment require separate
verification.

## Replay and continuation

After importing the prior durable batches into private SQLite:

```sh
python3 -m oss_research import-page-reviews research/parser_visual_review_pages152_154-160_2026-09-21.json
python3 -m oss_research import-reviewed-evidence research/evidence-pages150-160-duplicate-review_batch-608_2026-09-21.json
python3 -m oss_research import-reviewed-evidence research/evidence-gero-von-schulze-gaevernitz_batch-608_2026-09-21.json
python3 -m oss_research import-reviewed-evidence research/evidence-walter-galenson_batch-608_2026-09-21.json
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
python3 -m oss_research export-derived
python3 -m oss_research build-public-data
python3 -m oss_research coverage-report
```

The page-151 through page-160 queues are assigned durably in private SQLite.
Continue with `python3 -m oss_research research --source loc --batch
page-144-ferguson-feun-b607 --max-queries 46 --resume`. No API key, full
service number, raw API response, or private reviewer note is committed or
included in the public site.
