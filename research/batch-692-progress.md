# Batch 692: Myers-Nader research

Batch 692 covers PDF page 336, rows 23-45, from `Jack M Myers` through
`Thomas G Nader`. Fresh visual inspection confirmed all 23 printed rows. The
audit preserves the literal note `retained` for Marinus D Myrland and treats
the all-numeric value printed in Thomas G Nader's rank column as a displaced
identifier: it is masked publicly and is not represented as a rank.

**Gunnar G Mykland** is a high-confidence identity match across two
authoritative government sources. A National Park Service note cites his
November 1, 1944 OSS Detachment 202 report and identifies him as the unit's
executive officer. The October 1939 federal *Monthly Catalog* names Gunnar
Mykland as assistant director of the Housing Authority of Austin. That job is
published as documented prewar employment only. No source reviewed proves
that it immediately preceded OSS service or was his last civilian employer
before wartime service.

**Marinus D Myrland** is a high-confidence match to the Operation Rype member
whose rare name and protected identifier appear in a scholarly history and
whose OSS service is independently recorded in a NARA-based Operational
Groups roster. The history describes Myrland as a former ship's engineer.
That is published as a prewar occupation, not as an employer: no vessel,
shipping company, or immediate-pre-OSS chronology is named.

**James H Mysberch** is a high-confidence match to James H Mysbergh. The
official Army bulk record agrees on the protected identifier and name
components across the one-letter spelling difference, while a declassified
1945 OSS Detachment 101 promotion report independently prints James H.
Mysbergh. Both spellings remain searchable. Postwar publications and archival
correspondence were not converted into pre-OSS employment evidence.

Official Army bulk data also supports high-confidence identities for
**Thomas L Myers**, **Walter R Myers**, **William L Myers**, **Richard
Myrick**, and **Joseph E Nadeau**. The review accepts identity only and does
not convert coded Army occupations into employers.

Four identity conflicts remain visible. Jack M Myers shares a protected
identifier with Jack M Entes, whom the Army bulk row names; the two index
records remain separate. Lieutenant Norman M Myers and Captain Norman H
Meyers have different initials, ranks, pages, and boxes despite a shared
identifier. Adjacent captains Cecilia F Mynatt and Cecil F Myrott likewise
have materially different names but share an identifier. None of these
people is merged or assigned another person's evidence.

Kenneth Mygatt remains ambiguous. Official and institutional sources contain
a 1930 travel-company correspondent, a World War I Red Cross officer, and a
War Refugee Board applicant under that name, but none links the person to the
CAF-3 OSS index row. The tempting employer lead therefore remains unpublished
pending Box 549 review.

The cohort ends with 16 `no_reliable_result_after_protocol`, four
`conflicting_sources`, one `needs_identity_review`, one
`occupation_only_found`, and one `documented_prewar_employer_found` outcome.
Identity statuses are eight `high_confidence`, four `conflicting`, one
`ambiguous`, and ten `unresolved`. The evidence bundle imports seven sources,
one organization, one affiliation, 35 claims, 53 claim-source links, 23
person updates, and 23 consolidated research attempts. Six candidate identity
decisions are accepted and five are preserved as conflicts.

Rebuilt coverage is **23,978/23,978** linked source rows and **23,939** active
person entities. Research-attempt coverage is **8,961/23,939 (37.4326%)**;
confirmed/high verified-employer coverage is **313/23,939 (1.3075%)**;
confirmed/high verified-affiliation coverage is **693/23,939 (2.8949%)**;
archival-review disposition coverage is **7,418/23,939 (30.9871%)**. There
are **14,973** `not_started` people, **518** possible-duplicate groups, and
**258** active conflicts. SQLite stores **16,165** attempts or plans and
**5,791** claims: 1,340 confirmed, 2,566 high, 1,458 medium, 196 low, and 231
conflicting. It contains **5,424** citation records and **2,668** unique source
documents. The public projection contains **2,365** affiliations, **792**
organizations, **4,207** sources, and **5,588** claims. The featured
oil-company category remains **nine people across 11 historically named
companies**. Full-index historical research remains unfinished.

## Replay and continuation

After importing prior durable batches into private SQLite:

```sh
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
python3 -m oss_research import-review-decisions research/identity_review_decisions_2026-10-02_batch692.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page336-myers-nader-review_batch-692_2026-10-02.json
python3 -m oss_research export-adapter-checkpoints
python3 -m oss_research export-derived
python3 -m oss_research export-review-queue
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
```

Adapter checkpoints must be imported before final reviewed decisions and
evidence so temporary discovery states cannot supersede reviewed dispositions.

No API key, full service number, raw Catalog API response, copyrighted page
image, unrelated Army coded occupation, street address, or private reviewer
note is committed or included in the public site. No authenticated NARA
Catalog API request was made for this batch.
