# Batch 671: Montgomery-Moon research

The next contiguous queue covers PDF page 326 rows 24-45, from `James A.
Montgomery` through `Lawrence H. Moon`. It contains **22 source rows and 22
cautious person entities**. Every person now has a saved, reviewed outcome
grounded in the visually checked NARA index, official Army bulk identity
comparison where applicable, a targeted CIA or official-source check, Library
of Congress newspaper searches, exact-name and meaningful-variant OSS
searches, employment and occupation searches, and institutional, obituary,
directory, military, or archival checks as applicable. No authenticated NARA
Catalog request was made.

The reviewed findings preserve identity, relationship, and chronology limits:

- Protected Army identifiers support high-confidence identity matches for
  **Anthony Monti, Johnnie L. Montgomery, Joseph A. Montgomery, Lawrence H.
  Moon,** and **Steve G. Monti**. Army occupation codes remain private identity
  evidence and are never converted into employers.
- **Robert K. Montgomery** is a high-confidence match to the major documented
  on Jedburgh Team Tony/Dollar. The direct name, rank, and OSS mission match
  supports identity and assignment only; no predecessor employer is inferred.
- **John J. Montouri** is a probable match to the rare exact name in the
  February 1943 805th Tank Destroyer Battalion roster, Company C, Bradford,
  Pennsylvania. The chronology and rank progression are plausible, but no
  protected identifier or direct OSS transition is available.
- **Tony Monti** is a probable match to the New Mexico man identified in an OSS
  Society history of the Eighth Army Detachment. The source supplies neither a
  rank nor a protected identifier and does not establish a pre-OSS employer.
- **Maurice A. Mook** is a qualified probable identity lead. A Vanderbilt
  finding aid places the rare exact name at American University in 1942-43,
  and later anthropological scholarship corroborates the person. Neither
  source directly bridges him to this OSS personnel row or establishes the
  nature and sequence of the university affiliation, so no employment claim
  is published.
- **John U. Montuori** remains conflicting because the protected identifier
  agrees while the Army record reports middle initial J. **Laro Montland** and
  **Ralph A. Monton** remain conflicting because the protected identifiers
  point to differently spelled Army names that also have separate index rows.
  **Victor S. Montrezza** remains conflicting because the identifier retrieves
  two different nonmatching Army names.
- All **22** Library of Congress candidates were reviewed; 21 newspaper-page
  contexts were false or irrelevant and one malformed James A. Montgomery
  context response could not support a claim. A CIA adapter attempt failed
  closed when robots guidance was unavailable, after which public CIA-domain
  exact-name searches were recorded for all 22 people. That source-access
  failure is not treated as a negative result.
- **Esther T. Moon, Franklin F. Moon, James A. Montgomery, Jeanne E.
  Montgomery, Julia G. Montgomery, Kathleen K. Montgomery, Mary G.
  Montgomery, Mildred E. Montgomery,** and **Walter Montgomery** remain
  unresolved after the full protocol. A 1928-30 Cincinnati city-directory
  proprietor lead for Julia G. Montgomery is retained only as an unsupported
  identity note and is not published as her employment.

The bundle adds **13 identity claims, seven sources, 27 claim-source links,
and 22 reviewed research attempts**. It adds no employer, affiliation, or
organization claim. Thirty-four review decisions record five accepted
identity candidates, five conflicting candidates, and 24 rejected candidates.

All 22 people have terminal batch outcomes: nine
`no_reliable_result_after_protocol`, nine `requires_archival_review`, and four
`conflicting_sources`. The claims comprise six high-confidence published
identity findings, three medium-confidence qualified identity findings, and
four explicitly conflicting identity findings.

Rebuilt coverage is **23,978/23,978** linked source rows and **23,939** active
person entities. Research-attempt coverage is **8,510/23,939 (35.5487%)**;
confirmed/high verified-employer coverage is **302/23,939 (1.2615%)**;
confirmed/high verified-affiliation coverage is **667/23,939 (2.7862%)**;
archival-review disposition coverage is **6,966/23,939 (29.0990%)**. There are
**15,424** `not_started` people, **512** possible-duplicate groups, and **222**
active conflicts. SQLite stores **15,326** attempts or plans and **5,395**
claims: 1,326 confirmed, 2,241 high, 1,436 medium, 196 low, and 196
conflicting. It contains **5,287** citation records and **2,560** unique source
documents. The public projection contains **2,318** affiliations, **767**
organizations, **4,070** sources, and **5,192** claims.

The oil-company category remains prominent at the top of the home page and
personnel directory and on its dedicated route. It remains evidence-scoped to
**eight people across ten historically named companies**. Batch 671 adds no
oil-company member. Full-index historical research is unfinished.

## Replay and continuation

After importing prior durable batches into private SQLite:

```sh
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
python3 -m oss_research import-reviewed-evidence research/evidence-page326-montgomery-moon-review_batch-671_2026-09-25.json
python3 -m oss_research import-review-decisions research/identity_review_decisions_2026-09-25_batch671.csv
python3 -m oss_research export-adapter-checkpoints
python3 -m oss_research export-derived
python3 -m oss_research export-review-queue
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
```

Adapter checkpoints must be imported before the final reviewed evidence and
decisions so temporary adapter states cannot supersede the batch's reviewed
research dispositions.

No API key, full service number, raw Catalog API response, copyrighted page
image, or private reviewer note is committed or included in the public site.
