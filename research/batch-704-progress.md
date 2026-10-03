# Batch 704: Nicholson-Niedner research

Batch 704 covers PDF page 342, rows 23-45, from **Donald Nicholson** through
**Jack B Niedner**. Fresh visual inspection of the rendered source page
confirmed all 23 printed rows, representing 23 active person entities. The
immutable extraction is unchanged.

**Emrich Nicholson** is a probable identity match to the industrial designer
documented in the Museum of Modern Art's 1941 *Organic Design in Home
Furnishings* catalogue. The catalogue identifies him as Otto Kuhler's chief
designer from 1936 through 1938 and a freelance designer from 1938 onward. The
public profile presents both as qualified, medium-confidence documented-prewar
affiliations; neither is labeled the immediate pre-OSS affiliation or the last
civilian employer.

**Harry G Nickles** is confirmed through a direct OSS mission report that
identifies “Lt. Harry G. Nickles, USNR” as the Istanbul security officer. His
personnel category is now commissioned naval officer. This is an OSS wartime
assignment, not evidence of a pre-OSS employer, and the public profile preserves
that distinction.

**Gaspare Nicotri** is a high-confidence identity match to the Sicilian lawyer,
educator, and sociologist documented by Queens College and to the person linked
by a source-attributed historical account to 1942 meetings about aiding the
OSS. A 1940 University of Turin archival description documents his authorship
in *La Parola*. The resulting high-confidence occupation claim and qualified
professional affiliation do not turn the publication into an employer or
claim an immediate pre-OSS relationship.

Official Army bulk evidence supports high-confidence identity-only decisions
for **Guy H Nicholson**, **Peter G Nickles**, **Nick J Nickolas**, **Meredith Z
Nicodemus**, and **Frederick B Nicola**. Coded Army occupations are not treated
as employers. Probable or ambiguous matches remain unmerged for **Earl J
Nicholson / Earl J Nichelson**, **George A Nickolodoulos / George A
Nickolopoulos**, **John M Nicolich / John M Nicholich**, and **Franko M Nicotri
/ Franco Mario Nicotri** because spelling, identifier, rank, or duplicate-row
evidence requires archival review.

The CIA adapter failed closed without sending a usable search request. Six
bounded Library of Congress checks completed or recorded a transient error;
three candidates were rejected as unrelated namesakes or OCR adjacency.
Exact-name OSS, employment, occupation, institutional, newspaper, obituary,
military, and archival searches were reviewed for all 23 people.

The cohort ends with 17 `no_reliable_result_after_protocol`, four
`needs_identity_review`, one `documented_prewar_employer_found`, and one
`occupation_only_found` outcome. Identity statuses are one `confirmed`, six
`high_confidence`, three `probable`, two `ambiguous`, and 11 `unresolved`. The
evidence bundle imports seven sources, three organizations, three affiliations,
12 claims, 23 claim-source links, 23 person updates, and 23 consolidated
research attempts. Review decisions accept five identity candidates, preserve
five probable candidates without merging, and reject three unrelated Library
of Congress candidates.

Rebuilt coverage is **23,978/23,978** linked source rows and **23,939** active
person entities. Research-attempt coverage is **9,231/23,939 (38.5605%)**;
confirmed/high verified-employer coverage is **319/23,939 (1.3326%)**;
confirmed/high verified-affiliation coverage is **707/23,939 (2.9533%)**;
archival-review disposition coverage is **7,689/23,939 (32.1191%)**. There are
**14,703** `not_started` people, **522** possible-duplicate groups, and **273**
active conflicts. SQLite stores **16,651** attempts or plans and **5,962**
claims: 1,347 confirmed, 2,691 high, 1,478 medium, 196 low, 248 conflicting,
and two unresolved. It contains **5,506** citation records and **2,736** unique
source documents. The public projection contains **2,401** affiliations,
**821** organizations, **4,289** sources, and **5,757** claims. Full-index
historical research remains unfinished.

## Replay and continuation

After importing prior durable batches into private SQLite:

```sh
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
python3 -m oss_research assign-page-batch --batch-name batch-704 --page 342 --first-row 23 --last-row 45
python3 -m oss_research research --source cia --batch batch-704 --max-queries 1
python3 -m oss_research research --source loc --batch batch-704 --resume --max-queries 6
python3 -m oss_research research --source web --batch batch-704 --resume --max-queries 23
python3 -m oss_research import-review-decisions research/identity_review_decisions_2026-10-03_batch704.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page342-nicholson-niedner-review_batch-704_2026-10-03.json
python3 -m oss_research export-adapter-checkpoints
python3 -m oss_research export-derived
python3 -m oss_research export-review-queue
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
```

Adapter checkpoints must be imported before final reviewed decisions and
evidence so temporary discovery states cannot supersede reviewed dispositions.
The next research boundary begins at PDF page 342, row 46 (**Arthur H
Nielsen**).

No API key, full service number, raw Catalog or LoC API response, copyrighted
page image, unrelated Army coded occupation, street address, or private
reviewer note is committed or included in the public site. No authenticated
NARA Catalog API request was made for this batch.
