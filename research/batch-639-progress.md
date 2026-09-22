# Batch 639: PDF pages 461-470 and McGowan-McGuire research

All **460** printed rows on original NARA PDF pages 461-470 were compared
against SQLite at 180 dpi. Page 470 was also checked at 300 dpi where the
name and initial columns required closer inspection. Every page matches the
current extraction and requires no correction. Pages 463 and 468 were already
present in the deterministic random audit, so this batch adds eight pages and
368 rows to the complete-page ledger. Visual review now covers **388/522
pages** and **17,814/23,978 rows**: **17,782** reviewed rows match the
extraction, **32** retain reviewed corrections, and **6,164** remain for
complete visual comparison.

The page-309 `Arthur P. McGowan` through `Ernest F. McGuire` queue contains 23
source rows representing **23** cautious person entities. Its Library of
Congress pass saved an attempt for every person. Ten people produced 29
discovery candidates, and all 29 item contexts were inspected. Every candidate
was rejected as a conflicting name or initial, a deceased namesake, a spousal
reference, or a common-name mention without an OSS, protected-identifier, rank,
or archival-box bridge. In particular, a 1940 obituary rules out the East
Liverpool pottery-union official James J. McGowan; his Homer Laughlin
employment and union role are not assigned to the indexed person.

Five official Army bulk candidates received high-confidence identity decisions
from nonshared protected identifiers and exact normalized names or an explicit
variant. The fixed-width `MC GOWN` rendering for Arthur P. McGowan remains a
sourced variant and still requires Box 506 review. Full identifiers stay
private. Differing Army grade snapshots and Army occupation codes were not
converted into employers or predecessor affiliations.

The two adjacent John E. McGowan rows remain separate ambiguous entities: the
lieutenant and Technician Third Grade entries have different protected
identifiers, and none of the rejected newspaper candidates bridges either row.
Both require comparison of their Box 506 personnel files. Two bounded LoC
requests, for Terrence P. McGowan and Thomas H. McGrath, failed again with
redacted connection errors. Those attempts remain explicit source-access
failures, not negative results.

The final 23-person queue state is **21** `in_progress` and two
`needs_identity_review`. All **34** candidates in the cohort now have review
decisions: five accepted and 29 rejected. None remains unreviewed. This is
research-attempt progress, not completion of the minimum research protocol. No
new employer or affiliation claim was made.

Rebuilt coverage remains **23,978/23,978** linked source rows and **23,939**
active person entities. Research-attempt coverage is **7,809/23,939
(32.6204%)**; confirmed/high verified-employer coverage is **280/23,939
(1.1696%)**; confirmed/high verified-affiliation coverage is **628/23,939
(2.6233%)**; archival-review disposition coverage is **6,327/23,939
(26.4297%)**. There are **16,125** `not_started` people, **488** active
possible-duplicate groups, and **165** active people with conflicting identity
or source status. The database stores **12,960** attempts or plans and
**4,962** claims: **1,311** confirmed, **1,949** high, **1,375** medium,
**187** low, and **140** conflicting. It contains **5,070** source/citation
records and **2,387** unique document keys. The public projection contains
**2,224** affiliations, **708** organizations, **3,863** sources, and **4,771**
claims. The oil-company category remains a supported, incomplete evidence set
of seven people across nine companies. Full-index historical research is
unfinished.

## Replay and continuation

After importing prior durable batches into private SQLite:

```sh
python3 -m oss_research import-page-reviews research/parser_visual_review_pages461-470_2026-09-22.json
python3 -m oss_research import-review-decisions research/loc_review_decisions_2026-09-22_batch639.csv
python3 -m oss_research import-review-decisions research/identity_review_decisions_2026-09-22_batch639.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page309-mcgowan-mcguire-review_batch-639_2026-09-22.json
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
```

Continue with the next bounded research and visual-audit batch, then rebuild:

```sh
python3 -m oss_research export-adapter-checkpoints
python3 -m oss_research export-derived
python3 -m oss_research build-public-data
python3 -m oss_research coverage-report
```

No API key, full service number, raw API response, copyrighted page image, or
private reviewer note is committed or included in the public site. No
authenticated NARA Catalog request was made.
