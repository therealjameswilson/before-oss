# Batch 718: Oliver-Olson research

Batch 718 covers PDF page 349, rows 24-46, from **Maida O Oliver** through
**Clinton L Olson**. A 300-dpi visual inspection confirmed all 23 printed
rows, representing 23 active person entities. The immutable extraction is
unchanged. Original spellings, ranks, box numbers, and archival locations
remain recoverable. Nicholas V Olos is in Box 571; the other 22 rows are in
Box 572 at location 230/86/37/07.

Four people receive accepted identity matches from the official Army bulk
file: **Victor M Oliveria**, **Richard P Ollenburg**, **Erling M Olsen**, and
**Rodney E Olsen**. Each match uses the exact printed name plus a nonshared
protected identifier. The identifiers remain private, and no coded Army
occupation was converted into an occupation or employer claim.

**Nicholas V Olos** remains conflicting. His protected identifier reaches an
Army bulk record for **Nicholas V Olds**, but the surname difference cannot be
silently corrected. Both spellings remain visible and the Box 571 file is
required before any merge or correction.

**John E Olsen** remains separate from the source-derived **John E Olson** on
PDF page 350. The Army bulk name agrees with Olsen, but the same protected
identifier is printed on both index rows. The two profiles remain linked in
the `serial-conflict:13175112` possible-duplicate group, while the complete
identifier is excluded from the public site. Boxes 572 and 573 must be
compared before any merge.

**Clinton L Olson** receives a high-confidence identity match from his
first-person Association for Diplomatic Studies and Training oral history.
The distinctive exact name, indexed major rank, Army chronology, and explicit
account of 1944-45 OSS Secret Intelligence service align. His last documented
assignment before OSS was as an Army ordnance officer and deputy in the U.S.
Military Supply Mission to the Soviet Union, beginning in September 1941. It
is published as `probable_immediate`: the chronology is strong, but the
transcript does not explicitly say that he transferred directly from the
mission to OSS. His 1941 Production Control Officer assignment in the Office
of the Chief of Ordnance is published as earlier pre-OSS military service.
His Stanford Graduate School of Business attendance is separately modeled as
student status, never as employment. The transcript mentions unnamed work in
Los Angeles after high school, so no civilian employer is invented.

The CIA and Library of Congress adapters each made one bounded attempt and
failed closed. The web adapter recorded 23 deterministic planned queries
without making live requests. Manual staged review completed official,
exact-name OSS, employment, occupation, obituary, institutional, newspaper,
directory, military, spelling-variant, and archival search families for every
person.

The cohort ends with 15 `no_reliable_result_after_protocol`, five
`requires_archival_review`, two `conflicting_sources`, and one `completed`
outcome. Identity statuses are five `high_confidence`, 16 `unresolved`, one
`ambiguous`, and one `conflicting`. The reviewed bundle imports three sources,
three organizations, three affiliations, 10 claims, 18 claim-source links, 23
person updates, and 23 consolidated research attempts. Four accepted and
three conflicting identity-review decisions are recorded.

Rebuilt coverage is **23,978/23,978** linked source rows and **23,939** active
person entities. Research-attempt coverage is **9,552/23,939 (39.9014%)**;
confirmed/high verified-employer coverage is **326/23,939 (1.3618%)**;
confirmed/high verified-affiliation coverage is **725/23,939 (3.0285%)**;
archival-review disposition coverage is **8,010/23,939 (33.4600%)**. There are
**14,382** `not_started` people, **523** possible-duplicate groups, and **301**
active conflicts. SQLite stores **17,358** attempts or plans and **6,137**
claims: 1,352 confirmed, 2,817 high, 1,508 medium, 198 low, 260 conflicting,
and two unresolved. It contains **5,599** citation records and **2,811** unique
source documents. The public projection contains **2,441** affiliations,
**846** organizations, **4,380** sources, and **5,930** claims. Full-index
historical research remains unfinished.

## Replay and continuation

After importing prior durable batches into private SQLite:

```sh
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
python3 -m oss_research assign-page-batch --batch-name batch-718 --page 349 --first-row 24 --last-row 46
python3 -m oss_research research --source cia --batch batch-718 --max-queries 23
python3 -m oss_research research --source loc --batch batch-718 --max-queries 23
python3 -m oss_research research --source web --batch batch-718 --resume --max-queries 23 --dry-run
python3 -m oss_research import-review-decisions research/identity_review_decisions_2026-10-04_batch718.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page349-oliver-olson-review_batch-718_2026-10-04.json
python3 -m oss_research export-adapter-checkpoints
python3 -m oss_research export-derived
python3 -m oss_research export-review-queue
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
```

Adapter checkpoints must be imported before final reviewed decisions and
evidence so temporary discovery states cannot supersede reviewed
dispositions. The next research boundary begins at PDF page 350, row 1.

No API key, full service number, raw Catalog or LoC API response, copyrighted
page image, unrelated Army coded occupation, street address, modern
people-finder record, or private reviewer note is committed or included in
the public site. No authenticated NARA Catalog API request was made for this
batch.
