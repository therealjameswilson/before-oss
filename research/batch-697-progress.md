# Batch 697: Neff-Nellhaus research

Batch 697 closes the page boundary at PDF page 338, row 46, and continues
through page 339, rows 1-22, from **Jacqueline H Neff** through **Gerhardt
Nellhaus**. Fresh visual inspection of both rendered pages confirmed all 23
printed rows. The immutable extraction remains unchanged.

Official Army bulk evidence supports high-confidence identity-only decisions
for **Ralph R Neff**, **Robert P/R Neff**, **Nicholas Nefopulas**, **Stanley
Nehmer**, **Bernard R Nehring**, **Leroy A Neigh**, **Malcolm W Neill**, **John
W Neilson**, **Ben Neivert**, and **Harold Nelchin**. No coded Army occupation
is converted into an employer. Robert Neff's ambiguous indexed middle initial
is preserved rather than silently corrected.

**Stanley Nehmer** also has a documented prewar student affiliation. A May
1942 scholarly review carries a City College of New York affiliation, and a
Washington Post obituary says that he graduated there before beginning his
federal career in OSS. The site records City College as a school attended, not
an employer and not a proven immediate predecessor to OSS. Postwar State and
Commerce Department work is excluded from the pre-OSS answer.

**Julian M Neimczylc** is published as a probable match to **Julian Martin
Niemczyk**, not as a settled identity. His Library of Congress-hosted oral
history explicitly sequences University of Oklahoma attendance, fall 1940
National Guard induction, artillery service and battery command, an OSS
recruitment interview, and a War Department transfer to OSS. The site
therefore publishes the United States Army as the qualified immediate pre-OSS
military assignment and the university separately as earlier student status.
Neither institution is labeled a civilian employer. A CIA-hosted Veterans of
OSS roster independently corroborates the Niemczyk spelling and OSS
association.

**Gerhardt Nellhaus** is a high-confidence match to **Gerhard Nellhaus** in
99th Bomb Group Historical Society records: the uncommon name, second-
lieutenant rank, and protected identifier agree. The profile publishes his
German radio-message intercept work with the 348th Squadron, 99th Bomb Group,
as a wartime Army Air Forces assignment. Because the reviewed sources do not
establish its sequence relative to OSS service, it remains earlier wartime
context with `temporal_relation_uncertain`, not an immediate pre-OSS claim.

Two conflicts remain visible. National Park Service history documents an OSS
Captain **Eldon N Nehring**, but the protected identifier printed in the index
reaches a different Army name and grade. **Lester C Neimann** has an Army
surname variation and shares his protected identifier with a second index
entity spelled Nieman. Neither case is merged, and neither Army row supplies
employment evidence. The other nine people remain unresolved after the
minimum staged protocol and receive explicit archival-review guidance.

The cohort ends with three `completed`, two `conflicting_sources`, and 18
`no_reliable_result_after_protocol` outcomes. Identity statuses are 11
`high_confidence`, one `probable`, two `conflicting`, and nine `unresolved`.
The evidence bundle imports ten sources, four organizations (two reused), four
affiliations, 18 claims, 39 claim-source links, 23 person updates, and 23
consolidated research attempts. Ten official identity candidates are accepted
and three candidate rows are recorded as conflicts.

Rebuilt coverage is **23,978/23,978** linked source rows and **23,939** active
person entities. Research-attempt coverage is **9,075/23,939 (37.9089%)**;
confirmed/high verified-employer coverage is **317/23,939 (1.3242%)**;
confirmed/high verified-affiliation coverage is **703/23,939 (2.9366%)**;
archival-review disposition coverage is **7,532/23,939 (31.4633%)**. There are
**14,859** `not_started` people, **520** possible-duplicate groups, and **264**
active conflicts. SQLite stores **16,279** attempts or plans and **5,874**
claims: 1,343 confirmed, 2,633 high, 1,465 medium, 196 low, and 237
conflicting. It contains **5,466** citation records and **2,703** unique source
documents. The public projection contains **2,383** affiliations, **803**
organizations, **4,249** sources, and **5,671** claims. Full-index historical
research remains unfinished.

## Replay and continuation

After importing prior durable batches into private SQLite:

```sh
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
python3 -m oss_research assign-page-batch --batch-name batch-697-boundary --page 338 --first-row 46 --last-row 46
python3 -m oss_research assign-page-batch --batch-name batch-697 --page 339 --first-row 1 --last-row 22
python3 -m oss_research import-review-decisions research/identity_review_decisions_2026-10-03_batch697.csv
python3 -m oss_research import-reviewed-evidence research/evidence-pages338-339-neff-nellhaus-review_batch-697_2026-10-03.json
python3 -m oss_research export-adapter-checkpoints
python3 -m oss_research export-derived
python3 -m oss_research export-review-queue
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
```

Adapter checkpoints must be imported before final reviewed decisions and
evidence so temporary discovery states cannot supersede reviewed dispositions.
The next research boundary begins at PDF page 339, row 23.

No API key, full service number, raw Catalog API response, copyrighted page
image, unrelated Army coded occupation, street address, or private reviewer
note is committed or included in the public site. No authenticated NARA
Catalog API request was made for this batch.
