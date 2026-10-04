# Batch 712: Obenshain-Obucina research

Batch 712 covers PDF page 346, rows 24-46, from **Donald W Obenshain**
through **Joseph D Obucina**. A fresh 300-dpi visual inspection confirmed all
23 printed rows, representing 23 active person entities. The immutable
extraction is unchanged. In particular, the printed forms **Obrien** and
**Obryan** remain unpunctuated, ranks and blank rank fields are preserved, and
the rows remain associated with Boxes 566-567 and location 230/86/37/06.

Ten people now have identities at the default publication threshold. Existing
reviewed CIA and National Park Service evidence continues to confirm **Serge
Obolensky**. Eight nonshared official Army identifiers support **Donald W
Obenshain**, **Roger W Oberg**, **George M Obrien**, **Herbert J Obrien**,
**John C Obrien**, **Joseph P Obrien**, **Michael J Obrien**, and **Richard
Obrien**. The Army record transposes Michael to **Micheal**; that spelling is
preserved as a documented variant rather than silently normalized. A
contemporary OSS Detachment 101 promotion record supports **John M
Obereiner**. Army occupation codes were used only for identity resolution and
were not converted into employer or occupation claims.

No new pre-OSS affiliation met the publication threshold. Obolensky's already
published chronology remains intact: the New York National Guard as his
explicit immediate pre-OSS affiliation, St. Regis Hotel consulting and
promotional work as documented earlier employment, and unnamed banking and
real-estate work as an occupation-only result. The reviewed Detachment 101
record establishes Obereiner's wartime OSS identity but does not identify his
pre-OSS employer. Postwar banking evidence for an exact-name Obereiner was
excluded from the pre-OSS history.

The Library of Congress adapter made four bounded searches and returned ten
newspaper-page candidates for Frank J Obrien and George M Obrien. All ten are
formally rejected as common-name discovery noise because none supplies a
corroborating identifier, direct OSS link, or defensible pre-OSS chronology.
A possible John R O'Brien journalist biography remains an unaccepted lead:
the common name lacks the two corroborating identifiers required for
publication. A Walter E O'Brien casualty lead carries a different officer
identifier and was rejected as a namesake. The CIA adapter failed closed, and
the web adapter produced a deterministic 23-query plan without making live
requests. Manual staged review completed the required official, OSS,
employment, occupation, obituary, institutional, newspaper, directory, and
archival checks for every person.

The cohort ends with 21 `no_reliable_result_after_protocol`, one
`requires_archival_review`, and one `documented_prewar_employer_found`
outcome. Identity statuses are one `confirmed`, nine `high_confidence`, and 13
`unresolved`. The reviewed bundle imports three sources, no new organization
or affiliation, nine high-confidence identity claims, 18 claim-source links,
23 person updates, and 23 consolidated research attempts. Eighteen manual
identity-review decisions are recorded: eight accepted Army matches and ten
rejected newspaper candidates.

Rebuilt coverage is **23,978/23,978** linked source rows and **23,939** active
person entities. Research-attempt coverage is **9,414/23,939 (39.3250%)**;
confirmed/high verified-employer coverage is **325/23,939 (1.3576%)**;
confirmed/high verified-affiliation coverage is **720/23,939 (3.0076%)**;
archival-review disposition coverage is **7,872/23,939 (32.8836%)**. There are
**14,520** `not_started` people, **523** possible-duplicate groups, and **293**
active conflicts. SQLite stores **17,069** attempts or plans and **6,078**
claims: 1,352 confirmed, 2,773 high, 1,497 medium, 198 low, 256 conflicting,
and two unresolved. It contains **5,567** citation records and **2,786** unique
source documents. The public projection contains **2,425** affiliations,
**832** organizations, **4,348** sources, and **5,871** claims. Full-index
historical research remains unfinished.

## Replay and continuation

After importing prior durable batches into private SQLite:

```sh
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
python3 -m oss_research assign-page-batch --batch-name batch-712 --page 346 --first-row 24 --last-row 46
python3 -m oss_research research --source cia --batch batch-712 --max-queries 23
python3 -m oss_research research --source loc --batch batch-712 --max-queries 23
python3 -m oss_research research --source web --batch batch-712 --resume --max-queries 23
python3 -m oss_research import-review-decisions research/identity_review_decisions_2026-10-03_batch712.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page346-obenshain-obucina-review_batch-712_2026-10-03.json
python3 -m oss_research export-adapter-checkpoints
python3 -m oss_research export-derived
python3 -m oss_research export-review-queue
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
```

Adapter checkpoints must be imported before final reviewed decisions and
evidence so temporary discovery states cannot supersede reviewed dispositions.
The next research boundary begins at PDF page 346, row 47 (**Bernard F
O'Connell**).

No API key, full service number, raw Catalog or LoC API response, copyrighted
page image, unrelated Army coded occupation, address, phone number, modern
people-finder record, or private reviewer note is committed or included in the
public site. No authenticated NARA Catalog API request was made for this
batch.
