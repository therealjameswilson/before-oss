# Batch 640: PDF pages 471-480 and McGuire-McIntosh research

All **460** printed rows on original NARA PDF pages 471-480 were compared
against SQLite at 180 dpi. Page 472 was also checked at 300 dpi where the
first-name, note, and box columns required closer inspection. Every page
matches the current extraction and requires no correction. None of these ten
pages was already present in the complete-page ledger, so visual review now
covers **398/522 pages** and **18,274/23,978 rows**: **18,242** reviewed rows
match the extraction, **32** retain reviewed corrections, and **5,704** remain
for complete visual comparison.

The page-310 `James A. McGuire` through `Henry D. McIntosh` queue contains 23
source rows representing **23** cautious person entities. Its Library of
Congress pass saved a live outcome for every person. Six people produced 16
discovery candidates, and all 16 item contexts were inspected. Every candidate
was rejected because the name or middle initial conflicts, the item is
postwar, or the mention supplies no OSS, protected-identifier, rank, or Box
507 bridge. The rejected people include Henry T. McIntosh, newspaper figures
named James C., P., or W. McGuire, James F. and James J. McHugh, Joseph F.
McGuire, Thomas A., B., J., and Eugene McGuire, and William R. McGuire. Their
employment, military service, religious work, legal practice, and other roles
are not transferred to the indexed people.

Two official Army bulk candidates received high-confidence identity decisions.
Donald E. McInnis and William T. McGuire each have an exact normalized-name
match and a nonshared protected identifier. The Army entry date recorded for
William T. McGuire is in 1946 and is identity context only; Army entry dates,
grades, and occupation codes are not modeled as pre-OSS employers.

Two protected-identifier conflicts remain visible. The Army entry associated
with Loughlin G. McHugh prints middle initial `F`, and the identifier printed
for Thomas F. McGuire points to a completely different name, Robert N. Durbin.
Both people therefore have `conflicting` identity status, a critical archival
priority, and a Box 507 review instruction. No identity or employer is inferred
through either conflict, and no full identifier is public.

The adjacent Carolyn S. McIntosh row in Box 508 and Carolyn McIntosh, CAF-2,
in Box 507 remain separate person entities. Name similarity alone does not
support a merge. Erie McIlhenny's LoC request ended in recorded blocked and
timeout outcomes. That access failure remains explicit rather than being
converted into a negative search result.

The final 23-person queue state is **21** `in_progress` and two
`conflicting_sources`. All **20** candidates in the cohort have review
decisions: two accepted, two conflicting, and 16 rejected. None remains
unreviewed. This is research-attempt progress, not completion of the minimum
research protocol. No new employer or affiliation claim was made.

Rebuilt coverage remains **23,978/23,978** linked source rows and **23,939**
active person entities. Research-attempt coverage is **7,832/23,939
(32.7165%)**; confirmed/high verified-employer coverage is **280/23,939
(1.1696%)**; confirmed/high verified-affiliation coverage is **628/23,939
(2.6233%)**; archival-review disposition coverage is **6,331/23,939
(26.4464%)**. There are **16,102** `not_started` people, **488** active
possible-duplicate groups, and **167** active people with conflicting identity
or source status. The database stores **12,993** attempts or plans and
**4,966** claims: **1,311** confirmed, **1,951** high, **1,375** medium,
**187** low, and **142** conflicting. It contains **5,072** source/citation
records and **2,388** unique document keys. The public projection contains
**2,224** affiliations, **708** organizations, **3,865** sources, and **4,775**
claims. The oil-company category remains a supported, incomplete evidence set
of seven people across nine companies. Full-index historical research is
unfinished.

## Replay and continuation

After importing prior durable batches into private SQLite:

```sh
python3 -m oss_research import-page-reviews research/parser_visual_review_pages471-480_2026-09-22.json
python3 -m oss_research import-review-decisions research/loc_review_decisions_2026-09-22_batch640.csv
python3 -m oss_research import-review-decisions research/identity_review_decisions_2026-09-22_batch640.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page310-mcguire-mcintosh-review_batch-640_2026-09-22.json
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
