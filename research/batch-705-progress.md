# Batch 705: Nielsen-Nipper research

Batch 705 covers PDF page 342, row 46, and page 343, rows 1-22, from
**Arthur H Nielsen** through **Verne F Nipper**. Fresh visual inspection of both
rendered source pages confirmed all 23 printed rows, representing 23 active
person entities. The immutable extraction is unchanged.

**Julian M Niemczyk** is confirmed through the Library of Congress Foreign
Affairs Oral History Collection. His interview documents University of Oklahoma
student status, induction into the 45th Division, promotion from artillery
technical sergeant through Officer Candidate School to second lieutenant and
battery commander, and direct OSS recruitment from his artillery battalion.
The profile therefore distinguishes a confirmed immediate pre-OSS military
assignment from documented prewar student status; neither is mislabeled as a
civilian employer.

**Henry R Nigrelli** is a high-confidence identity match to the University of
North Carolina graduate hired as a WPTF announcer in 1940 and documented as
WPTF's public-relations director when drafted in 1941. A separate scholarly OSS
history identifies Captain Henry R. Nigrelli in Genoa. WPTF is recorded as the
last civilian employer before military service, not as an explicitly immediate
pre-OSS employer.

**Boonyong Nikrodananda** is a high-confidence identity match supported by
Cornell registers and its Early Asian Alumni project, a contemporary Harvard
Crimson account, and a scholarly name cross-reference connecting historical
spellings. Cornell University and Harvard University are recorded as student
relationships, not employers. His documented Free Thai activity remains a
qualified medium-confidence volunteer affiliation. His source classification is
corrected to foreign or Allied military personnel while preserving the original
rank and indexed spelling.

**Halver H Nipe** is confirmed as **Halvor H Nipe** through exact identifier
evidence and a published Operation Rype roster. The historical account states
that the OSS recruited the Norwegian-speaking volunteers from the 99th Infantry
Battalion (Separate), supporting a high-confidence immediate pre-OSS military
assignment. The original index spelling remains fully recoverable.

Official Army bulk evidence supports high-confidence identity-only decisions
for **Carl A Nielsen**, **Milton H Nielsen**, **Robert B Nielsen**, **John E
Nightingale**, and **Nils C Nilson**. Coded Army occupations are not converted
into employer claims. **Lester C Nieman** remains conflicting because his
identifier is shared with a separate **Lester C Neimann** source row and the
Army spelling is *Niemann*; the records remain visible and unmerged. A possible
*Ninomiya* variant for **Toshio Nimomiya**, a postwar Red Cross lead for Dorothy,
and Omaha radio/engineering leads for Verne Nipper were rejected because they
did not establish the indexed person's identity and pre-OSS chronology.

The CIA adapter failed closed without sending a usable search request. Bounded
Library of Congress checks also failed closed, while exact-name OSS,
employment, occupation, institutional, newspaper, obituary, military, and
archival searches were reviewed for all 23 people.

The cohort ends with 18 `no_reliable_result_after_protocol`, three `completed`,
one `conflicting_sources`, and one `verified_employer_found` outcome. Identity
statuses are two `confirmed`, seven `high_confidence`, one `conflicting`, and
13 `unresolved`. The evidence bundle imports 12 sources, seven organizations,
seven affiliations, 16 claims, 34 claim-source links, 23 person updates, and 23
consolidated research attempts. Claim publication decisions comprise four
confirmed claims, 11 high-confidence claims, and one visibly qualified
medium-confidence claim. Review decisions accept six identity candidates and
preserve two probable conflict candidates without merging.

Rebuilt coverage is **23,978/23,978** linked source rows and **23,939** active
person entities. Research-attempt coverage is **9,254/23,939 (38.6566%)**;
confirmed/high verified-employer coverage is **320/23,939 (1.3367%)**;
confirmed/high verified-affiliation coverage is **711/23,939 (2.9700%)**;
archival-review disposition coverage is **7,712/23,939 (32.2152%)**. There are
**14,680** `not_started` people, **523** possible-duplicate groups, and **274**
active conflicts. SQLite stores **16,700** attempts or plans and **5,978**
claims: 1,351 confirmed, 2,702 high, 1,479 medium, 196 low, 248 conflicting,
and two unresolved. It contains **5,518** citation records and **2,746** unique
source documents. The public projection contains **2,408** affiliations,
**823** organizations, **4,301** sources, and **5,773** claims. Full-index
historical research remains unfinished.

## Replay and continuation

After importing prior durable batches into private SQLite:

```sh
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
python3 -m oss_research assign-page-batch --batch-name batch-705a --page 342 --first-row 46 --last-row 46
python3 -m oss_research assign-page-batch --batch-name batch-705b --page 343 --first-row 1 --last-row 22
python3 -m oss_research research --source cia --batch batch-705a --max-queries 1
python3 -m oss_research research --source loc --batch batch-705a --max-queries 1
python3 -m oss_research research --source loc --batch batch-705b --max-queries 6
python3 -m oss_research research --source web --batch batch-705a --resume --max-queries 1
python3 -m oss_research research --source web --batch batch-705b --resume --max-queries 22
python3 -m oss_research import-review-decisions research/identity_review_decisions_2026-10-03_batch705.csv
python3 -m oss_research import-reviewed-evidence research/evidence-pages342-343-nielsen-nipper-review_batch-705_2026-10-03.json
python3 -m oss_research export-adapter-checkpoints
python3 -m oss_research export-derived
python3 -m oss_research export-review-queue
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
```

Adapter checkpoints must be imported before final reviewed decisions and
evidence so temporary discovery states cannot supersede reviewed dispositions.
The next research boundary begins at PDF page 343, row 23 (**George H Nishi**).

No API key, full service number, raw Catalog or LoC API response, copyrighted
page image, unrelated Army coded occupation, street address, or private
reviewer note is committed or included in the public site. No authenticated
NARA Catalog API request was made for this batch.
