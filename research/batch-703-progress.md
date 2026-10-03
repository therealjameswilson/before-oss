# Batch 703: Nicholas-Nichols research

Batch 703 covers PDF page 341, row 46, and page 342, rows 1-22, from
**Christo Nicholas** through **Willard A Nichols**. Fresh visual inspection of
both rendered source pages confirmed all 23 printed rows, representing 23
active person entities. The immutable extraction is unchanged. In particular,
Robert C Nicholas's unusually short printed identifier remains exactly as
indexed and was not padded or forced into an Army match.

**Frederick W Nicholls** is confirmed as the British Royal Corps of Signals
officer Frederick William Nicholls through an exact distinctive name and
matching official British Army identifier. A detailed record-cited service
chronology explicitly places him as a General Staff Officer at the British War
Office immediately before he was posted to the Special Operations Executive
on 2 November 1942. The public claim identifies this as the immediate
pre-secret-service military assignment for an Allied person in the OSS index;
it does not conflate SOE with OSS.

**Osgood M Nichols** is a probable match to the federal public-information
official whom the Congressional Record placed in the Wage and Hour Division's
Information Branch in August 1940 and whom an official 1942 Bureau of Labor
Statistics report identified as the National Defense Mediation Board's
Director of Information from 27 March 1941 through 12 January 1942. Both
assignments are published as qualified, medium-confidence documented-prewar
government affiliations. Neither is labeled the immediate pre-OSS affiliation
because the accessible sources do not establish that transition.

Official Army bulk evidence supports high-confidence identity-only decisions
for **Christo Nicholas**, **Paul B Nicholas**, **Richard Nicholas**, **Calvin J
Nichols**, **Warren Nichols**, and the already researched **Edward E Nicholas
Jr.** Exact indexed names and nonshared protected identifiers agree. No coded
Army occupation is converted into an employer.

**John M Nicholich**, **John N Nicholich**, and a later **John M Nicolich**
index row share one protected identifier, but their spelling, middle initial,
rank, and box data conflict. The official Army record reads John M Nicolich.
All three printed rows and all three person entities remain visible and
unmerged. The two profiles in this cohort receive explicit ambiguity or
conflict notes and critical archival-review priority.

The CIA adapter failed closed without sending a usable search request. Three
bounded Library of Congress checks also recorded errors without retaining raw
responses. Exact-name OSS, employment, occupation, institutional, newspaper,
obituary, military, and archival searches were reviewed for all 23 people.
Common-name burial, genealogy, and modern professional results were rejected
when they lacked corroborating identifiers or wartime chronology.

The cohort ends with three `completed`, one `needs_identity_review`, one
`conflicting_sources`, and 18 `no_reliable_result_after_protocol` outcomes.
Identity statuses are one `confirmed`, six `high_confidence`, one `probable`,
one `ambiguous`, one `conflicting`, and 13 `unresolved`. The evidence bundle
imports six sources, three organizations, three affiliations, 12 claims, 23
claim-source links, 22 person updates, and 22 consolidated research attempts;
Edward E Nicholas Jr.'s earlier reviewed evidence remains unchanged. Review
decisions accept six Army identity candidates and preserve four probable
conflict or duplicate candidates without merging them.

Rebuilt coverage is **23,978/23,978** linked source rows and **23,939** active
person entities. Research-attempt coverage is **9,208/23,939 (38.4644%)**;
confirmed/high verified-employer coverage is **319/23,939 (1.3326%)**;
confirmed/high verified-affiliation coverage is **707/23,939 (2.9533%)**;
archival-review disposition coverage is **7,666/23,939 (32.0231%)**. There are
**14,726** `not_started` people, **522** possible-duplicate groups, and **273**
active conflicts. SQLite stores **16,619** attempts or plans and **5,950**
claims: 1,346 confirmed, 2,684 high, 1,474 medium, 196 low, 248 conflicting,
and two unresolved. It contains **5,499** citation records and **2,730** unique
source documents. The public projection contains **2,398** affiliations,
**818** organizations, **4,282** sources, and **5,745** claims. Full-index
historical research remains unfinished.

## Replay and continuation

After importing prior durable batches into private SQLite:

```sh
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
python3 -m oss_research assign-page-batch --batch-name batch-703a --page 341 --first-row 46 --last-row 46
python3 -m oss_research assign-page-batch --batch-name batch-703b --page 342 --first-row 1 --last-row 14
python3 -m oss_research assign-page-batch --batch-name batch-703c --page 342 --first-row 16 --last-row 22
python3 -m oss_research research --source cia --batch batch-703a --max-queries 1
python3 -m oss_research research --source loc --person-id 49b3f759-c330-570c-9a97-fd5c4e557ae0 --max-queries 1
python3 -m oss_research research --source loc --person-id bee40827-db33-5114-b31c-5b027c029d9a --max-queries 1
python3 -m oss_research research --source web --batch batch-703a --max-queries 1
python3 -m oss_research research --source web --batch batch-703b --max-queries 14
python3 -m oss_research research --source web --batch batch-703c --max-queries 7
python3 -m oss_research research --source web --person-id 72026b46-fb17-5749-922c-28f57e576e65 --max-queries 1
python3 -m oss_research import-review-decisions research/identity_review_decisions_2026-10-03_batch703.csv
python3 -m oss_research import-reviewed-evidence research/evidence-pages341-342-nicholas-nichols-review_batch-703_2026-10-03.json
python3 -m oss_research export-adapter-checkpoints
python3 -m oss_research export-derived
python3 -m oss_research export-review-queue
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
```

Adapter checkpoints must be imported before final reviewed decisions and
evidence so temporary discovery states cannot supersede reviewed dispositions.
The next research boundary begins at PDF page 342, row 23 (**Donald
Nicholson**).

No API key, full service number, raw Catalog or LoC API response, copyrighted
page image, unrelated Army coded occupation, street address, or private
reviewer note is committed or included in the public site. No authenticated
NARA Catalog API request was made for this batch.
