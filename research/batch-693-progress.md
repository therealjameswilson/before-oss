# Batch 693: Nadler-Nakamura research

Batch 693 covers the boundary row on PDF page 336 and page 337, rows 1-22,
from `Harry C Nadler` through `Shingi Nakamura`. Fresh visual inspection of
both rendered pages confirmed all 23 printed rows. Harry Nadler's literal,
truncated note `file sent t` remains unchanged. Chiyeko Nakamura's printed
`Caf-5` is normalized as a civilian grade; the immutable extracted row and its
column-shift warning remain auditable.

**Chiyeko Nakamura** now has the cohort's strongest immediate-employment
finding. Brian Masaru Hayashi's personnel-file-based scholarly history dates
her part-time Japanese-language teaching for Columbia University from May
through September 1944 and dates her OSS entry to September 11, 1944. Columbia
is therefore published as both her immediate pre-OSS affiliation and the last
named civilian employer documented before OSS, at high confidence. Her
1933-1935 attendance at the Tokyo Dressmaking Women's Institute is separately
modeled as student status. Unnamed dressmaking jobs remain unnamed rather than
being converted into employers.

**Finn Nagell** is a high-confidence identity match from his rare exact name,
Major rank, Norwegian biographical directory entry, and multi-archival history
of SOE in Norway. The directory jointly associates his 1928-1932 publishing
work with Cappelen and Steenske. They remain separate organizations and neither
is designated the last civilian employer because the source does not allocate
subranges or establish order. His 1941-1944 leadership of the Norwegian
Ministry of Defence Intelligence Office (FD-E) is published as a qualified
wartime government assignment; its sequence relative to the OSS index file is
not established.

**Yoshinao Nakada** is a high-confidence match across the exact indexed name,
protected identifier, and Caltech's April 1946 alumni column. The Caltech
source places him in the class-of-1940 section and identifies him as formerly
with OSS. Caltech is modeled as a prewar student affiliation, not an employer.

**Shingi Nakamura** is a high-confidence match across a declassified April 30,
1945 OSS order and a Densho biography that independently documents Strategic
Bombing Survey service. His 1927-1934 membership and first presidency of the
Zaibei Okinawan Seinenkai are published as a community/professional
affiliation. Gardening and hotel work are published only as occupations because
no employer is named. **Edward S Nakamura** remains only a probable match to
the Edward Nakamura in the same OSS order because the order omits his middle
initial.

Official Army bulk data also supports high-confidence identities for **Donald P
Naetzker**, **Harold E Nail**, **Robert J Naismith**, and **Charles M
Nakamura**. These reviews accept identity only and do not convert coded Army
occupations into employers. **Albin L Nagler** remains a visible conflict: the
protected identifier agrees with an Army row for **Alvin L Nagler**, but no
independent source resolves the first-name difference.

The cohort ends with 18 `no_reliable_result_after_protocol`, two `completed`,
one `conflicting_sources`, one `documented_prewar_employer_found`, and one
`verified_employer_found` outcome. Identity statuses are eight
`high_confidence`, one `probable`, one `conflicting`, and 13 `unresolved`. The
evidence bundle imports eight sources, seven organizations, seven affiliations,
19 claims, 33 claim-source links, 23 person updates, and 23 consolidated
research attempts. Five candidate identity decisions are accepted and one is
preserved as a conflict.

Rebuilt coverage is **23,978/23,978** linked source rows and **23,939** active
person entities. Research-attempt coverage is **8,984/23,939 (37.5287%)**;
confirmed/high verified-employer coverage is **315/23,939 (1.3158%)**;
confirmed/high verified-affiliation coverage is **697/23,939 (2.9116%)**;
archival-review disposition coverage is **7,441/23,939 (31.0832%)**. There are
**14,950** `not_started` people, **519** possible-duplicate groups, and **259**
active conflicts. SQLite stores **16,188** attempts or plans and **5,810**
claims: 1,340 confirmed, 2,583 high, 1,459 medium, 196 low, and 232
conflicting. It contains **5,432** citation records and **2,675** unique source
documents. The public projection contains **2,372** affiliations, **799**
organizations, **4,215** sources, and **5,607** claims. Full-index historical
research remains unfinished.

## Replay and continuation

After importing prior durable batches into private SQLite:

```sh
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
python3 -m oss_research assign-page-batch --batch-name batch-693-boundary --page 336 --first-row 46 --last-row 46
python3 -m oss_research assign-page-batch --batch-name batch-693 --page 337 --first-row 1 --last-row 22
python3 -m oss_research import-review-decisions research/identity_review_decisions_2026-10-03_batch693.csv
python3 -m oss_research import-reviewed-evidence research/evidence-pages336-337-nadler-nakamura-review_batch-693_2026-10-03.json
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
note is committed or included in the public site. No authenticated NARA Catalog
API request was made for this batch.
