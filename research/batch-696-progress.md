# Batch 696: Naylor-Neff research

Batch 696 covers PDF page 338, rows 23-45, from **Glenn R Naylor** through
**Charles R Neff**. Fresh visual inspection of the rendered page confirmed all
23 printed rows. The immutable extraction remains unchanged.

**Robert D Neasse** is a high-confidence identity match. His exact name and
nonshared protected identifier agree between the OSS index and official Army
bulk data. An Arizona Republic obituary supplies the chronology: he enlisted
in 1942, graduated from Ohio Wesleyan University in 1943, and after his March
1944 wedding moved to Washington while on detached service with OSS. The
public profile therefore records the **United States Army** as his immediate
pre-OSS military assignment and **Ohio Wesleyan University** separately as a
student affiliation. The university is not presented as an employer.

**Charles F Neave** is a high-confidence match to the officer listed in the
1916 Field Artillery Journal directory. The site publishes his first-lieutenant
assignment in Battery B of Connecticut's Tenth Militia Field Artillery as
earlier documented military service only. It does not infer that this 1916
post immediately preceded OSS service, and it does not interpret the unit's
historical Yale wording as university employment or attendance.

**Harry M Neben** is a high-confidence identity match. National Park Service
history and ARRL material identify the unusually named Illinois amateur radio
operator W9QB and describe his recruitment to install radio equipment at OSS
Area C in December 1942. The profile publishes **amateur radio operator** as an
occupation-only finding; postwar employers are excluded and no pre-OSS
employer is invented.

**Paul Nebenzahl** is a high-confidence identity match to the T/4 P. Nebenzahl
listed with OSS Operational Group BLACKBERRY; the matching grade and rare name
are corroborated by an obituary. **Martin E Nedell** remains a probable match
to the Martin E. Nedell in an official OSS training-office personnel report.
Neither profile receives a pre-OSS employer claim. **Dean B Needham** is a
high-confidence identity match through official Army data and an obituary that
documents OSS service, but the accessible evidence does not date his education
or identify a pre-OSS employer.

Official Army evidence also supports high-confidence identity-only decisions
for **Glenn R Naylor**, **Herman E Naylor Jr.**, and **Joseph Nechunskas**.
Their Army coded occupations are not converted into employer claims. **Adam M
Neely** is conflicting because his printed protected identifier resolves to a
different Army spelling and grade; that candidate remains visible and is not
merged. The remaining people receive transparent no-result outcomes after the
minimum staged protocol.

The cohort ends with two `completed`, one `occupation_only_found`, one
`conflicting_sources`, and 19 `no_reliable_result_after_protocol` outcomes.
Identity statuses are eight `high_confidence`, one `probable`, one
`conflicting`, and 13 `unresolved`. The evidence bundle imports 11 sources,
three organizations (two reused), three affiliations, 14 claims, 32
claim-source links, 23 person updates, and 23 consolidated research attempts.
Five official identity candidates are accepted and one is recorded as a
conflict.

Rebuilt coverage is **23,978/23,978** linked source rows and **23,939** active
person entities. Research-attempt coverage is **9,052/23,939 (37.8128%)**;
confirmed/high verified-employer coverage is **317/23,939 (1.3242%)**;
confirmed/high verified-affiliation coverage is **702/23,939 (2.9325%)**;
archival-review disposition coverage is **7,509/23,939 (31.3672%)**. There are
**14,882** `not_started` people, **520** possible-duplicate groups, and **262**
active conflicts. SQLite stores **16,256** attempts or plans and **5,856**
claims: 1,343 confirmed, 2,621 high, 1,461 medium, 196 low, and 235
conflicting. It contains **5,456** citation records and **2,695** unique source
documents. The public projection contains **2,379** affiliations, **801**
organizations, **4,239** sources, and **5,653** claims. Full-index historical
research remains unfinished.

## Replay and continuation

After importing prior durable batches into private SQLite:

```sh
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
python3 -m oss_research assign-page-batch --batch-name batch-696 --page 338 --first-row 23 --last-row 45
python3 -m oss_research import-review-decisions research/identity_review_decisions_2026-10-03_batch696.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page338-naylor-neff-review_batch-696_2026-10-03.json
python3 -m oss_research export-adapter-checkpoints
python3 -m oss_research export-derived
python3 -m oss_research export-review-queue
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
```

Adapter checkpoints must be imported before final reviewed decisions and
evidence so temporary discovery states cannot supersede reviewed dispositions.
The next research boundary begins at PDF page 338, row 46.

No API key, full service number, raw Catalog API response, copyrighted page
image, unrelated Army coded occupation, street address, or private reviewer
note is committed or included in the public site. No authenticated NARA
Catalog API request was made for this batch.
