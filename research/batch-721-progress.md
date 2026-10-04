# Batch 721: Oney-Orbach research

Batch 721 covers PDF page 351, rows 1-23, from **Walter Oney**
through **Frederick Orbach**. A 300-dpi visual inspection confirmed all 23
printed rows, representing 23 active person entities. Embedded text was
checked against the render. The immutable extraction is unchanged: Felix E
Oppenheim's note remains `ST. L`, Susan Oppenheim's note remains the incomplete
`aka Gjer`, and Charles D Orangers remains the visually confirmed index
spelling. Walter Oney through Henry Oosthoer are in Box 574; Thaddeus W
Opalinski through Frederick Orbach are in Box 575. All rows use location
230/86/37/07.

Nine Army bulk candidates are accepted for identity only. **Jo K Ong**, **Paul
J Onofer**, **Richard Opfar**, **Arthur Oppedisano**, **Siegfried Oppenheim**,
**Harry Oppenheimer**, **James F Opsahl**, **Donald W Orahood**, and **Frederick
Orbach** have exact indexed-name and nonshared protected-identifier agreement.
No Army coded occupation was converted into an occupation or employer claim.

**Felix E Oppenheim** remains conflicting. His protected identifier reaches an
Army bulk row transcribed as `WPPENHNIM FELIX`. Because the name fields do not
agree, no Army name, occupation, or other metadata is transferred. The printed
`ST. L` note is preserved without expansion. Box 575 review is critical.

Three profiles receive substantive, source-level pre-OSS findings:

* **Arthur Heath Onthank** is a high-confidence identity. A contemporary 1939
  War Department bulletin documents his appointment as Director of Personnel,
  an official Army history identifies A. Heath Onthank as chief of the War
  Department Civilian Personnel Division in 1941, and an NPS archival note
  places Lt. Col. A. H. Onthank in OSS records in July 1942. The personnel role
  is published as his strongly date-bounded last civilian government
  assignment before military service, not as an explicit immediate pre-OSS
  affiliation.
* **Arthur Oppenheimer Jr.** is linked at high identity confidence to the
  indexed major. A contemporary trade journal places him with Bloomingdale
  Brothers in June 1934 without inventing a job title. An April 1942 federal
  Information Digest says he resigned as chief of several Office of Price
  Administration household-goods units to enlist as a private in the Army
  Quartermaster Corps. A November 1944 OSS chart identifies Captain Arthur
  Oppenheimer as chief of the Field Services Unit. The OPA role is published
  as his explicit last civilian assignment before military service; neither
  the Quartermaster Corps nor Bloomingdale is labeled the immediate pre-OSS
  affiliation.
* **James Ball Opsata** is a high-confidence identity and the one profile in
  this cohort with a confirmed immediate institutional predecessor. Federal
  Reserve minutes identify him as COI Personnel Officer in December 1941, and
  NARA documents COI's reorganization into OSS on 13 June 1942. Earlier
  personnel work for the Department of Labor is separately published as a
  medium-confidence, undated pre-OSS government assignment. Discovery-only
  claims about an intervening Federal Security Agency role are not adopted.

**Etienne Oostendorp** receives a high-confidence identity match from an
official 1945 State Department letter that names the Netherlands national and
describes OSS sponsorship. Conflicting birth-year leads and unrelated
sensitive allegations in local-history sources are excluded. No pre-OSS
employer is assigned without Box 574 review.

**Siegfried Oppenheim** is confirmed by exact protected-identifier agreement,
NARA Entry 210, and the Hoover Institution's description of his papers and OSS
assignment in China. A German-Jewish butcher with the same name is rejected as
an unbridged namesake. No pre-OSS employer is inferred.

**Richard Opfar** receives independent OSS identity context from University of
Minnesota Press research citing 1945 Presentation Branch production meetings.
**Harry Oppenheimer** receives compatible OSS Philippines context from a
reputable newspaper's family account. Harry's undated butcher and meat-business
history is not converted into a pre-OSS affiliation. These profiles remain
protocol-complete no-result cases for the central employment question.

The CIA and Library of Congress adapters each made one bounded attempt and
failed closed. The web adapter recorded 23 deterministic planned queries
without making live requests. Manual staged review completed official,
exact-name OSS, employer, occupation, obituary, institutional, newspaper,
directory, military, punctuation-variant, spelling-variant, and archival
search families for every person. Discovery-only, unbridged, postwar, and
modern namesakes were rejected rather than converted into claims.

The cohort ends with 11 `requires_archival_review`, eight
`no_reliable_result_after_protocol`, two
`documented_prewar_employer_found`, one `completed`, and one
`conflicting_sources` outcome. Identity statuses are nine `unresolved`, 12
`high_confidence`, one `confirmed`, and one `conflicting`. The reviewed bundle
imports 16 sources, six organizations, six affiliations, 20 claims, 45
claim-source links, 23 person updates, and 23 consolidated research attempts.
Nine accepted and one conflicting identity-review decisions are recorded.

Rebuilt coverage is **23,978/23,978** linked source rows and **23,939** active
person entities. Research-attempt coverage is **9,621/23,939 (40.1896%)**;
confirmed/high verified-employer coverage is **328/23,939 (1.3701%)**;
confirmed/high verified-affiliation coverage is **731/23,939 (3.0536%)**;
archival-review disposition coverage is **8,079/23,939 (33.7483%)**. There
are **14,313** `not_started` people, **523** possible-duplicate groups, and
**306** active conflicts. SQLite stores **17,502** attempts or plans and
**6,185** claims: 1,357 confirmed, 2,847 high, 1,516 medium, 198 low, 265
conflicting, and two unresolved. It contains **5,624** citation records and
**2,830** unique source documents. The public projection contains **2,457**
affiliations, **851** organizations, **4,405** sources, and **5,978** claims.
Full-index historical research remains unfinished.

## Replay and continuation

After importing prior durable batches into private SQLite:

```sh
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
python3 -m oss_research assign-page-batch --batch-name batch-721 --page 351 --first-row 1 --last-row 23
python3 -m oss_research research --source cia --batch batch-721 --max-queries 23
python3 -m oss_research research --source loc --batch batch-721 --max-queries 23
python3 -m oss_research research --source web --batch batch-721 --resume --max-queries 23 --dry-run
python3 -m oss_research import-review-decisions research/identity_review_decisions_2026-10-04_batch721.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page351-oney-orbach-review_batch-721_2026-10-04.json
python3 -m oss_research export-adapter-checkpoints
python3 -m oss_research export-derived
python3 -m oss_research export-review-queue
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
```

Adapter checkpoints must be imported before final reviewed decisions and
evidence so temporary discovery states cannot supersede reviewed dispositions.
The next research boundary begins at PDF page 351, row 24.

No API key, full service or officer number, raw Catalog or LoC API response,
copyrighted page image, unrelated Army coded occupation, street address,
modern people-finder record, or private reviewer note is committed or included
in the public site. No authenticated NARA Catalog API request was made for this
batch.
