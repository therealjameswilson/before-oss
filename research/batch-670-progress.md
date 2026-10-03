# Batch 670: Monroe-Montgomery research

The next contiguous queue covers PDF page 326 rows 2-23, from `Barbara R.
Monroe` through `Hugh Montgomery`. It contains **22 source rows and 22 cautious
person entities**. Every person now has a saved, reviewed outcome grounded in
the visually checked NARA index, official Army bulk identity comparison where
applicable, a targeted CIA or official-source check, Library of Congress
newspaper searches, exact-name and meaningful-variant OSS searches, employment
and occupation searches, and institutional, obituary, directory, military, or
archival checks as applicable. No authenticated NARA Catalog request was made.

The reviewed findings preserve identity, relationship, and chronology limits:

- **James Montante** is a high-confidence match to the Detroit attorney and OSS
  captain documented in contemporary 1941 and 1947 *Grosse Pointe Review* and
  *Grosse Pointe News* pages. His private Detroit law practice is published as
  self-employment and the last civilian affiliation before service, with a
  strongly date-bounded temporal basis. No unnamed law firm is invented.
- **Hobart C. Montee** is a high-confidence match to the United Press staff
  correspondent whose exact rare name appears in five 1939-40 contemporary
  newspaper bylines. This is documented prewar employment, not evidence of an
  immediate pre-OSS affiliation or last civilian employer.
- **Frank Monteleone** is a high-confidence match to the Navy radio operator
  documented immediately before OSS service. The Navy role is modeled as a
  military assignment, not a civilian employer; the last civilian employer is
  unresolved and the indexed file remains an archival-review priority.
- **Hugh Montgomery** is a confirmed identity match supported by an official
  CIA history and independent military reporting. Harvard is modeled only as
  student status; the U.S. Army and airborne service are the immediate military
  pathway into OSS. Sources disagree whether enlistment occurred in 1941 or
  1942, and that conflict remains explicit.
- Protected Army identifiers support high-confidence identity matches for
  **Donald K. Monroe, Ernest M. Montefalco,** and **Henry I. Montgomery**.
  Army occupation codes remain private identity evidence and are never
  converted into employers.
- **John N. Monroe** shares a protected identifier with a differently named
  person and remains conflicting. **Charles P. Montanard/Charles P.
  Montanaro** and **Dan C. Montanell/Dan C. Montanelli** remain probable
  spelling variants rather than forced matches. All require identity review.
- All **27** Library of Congress candidates were reviewed: five exact Hobart
  C. Montee bylines were accepted and 22 false or irrelevant candidates were
  rejected. A grouped CIA search produced no direct Reading Room item and is
  not treated as proof that no record exists.
- Every remaining unresolved person has an explicit Box 532 archival next
  action. Failed online research is not represented as evidence that no prior
  employment existed.

The bundle adds **13 claims, five affiliations, five organization upserts, 13
sources, 33 claim-source links, and 22 reviewed research attempts**. Forty
review decisions record nine accepted identity candidates, two conflicting
candidates, two probable variants, 22 rejected candidates, and five rejected
superseded Hugh Montgomery publication records. Superseded records remain in
SQLite with auditable publication decisions rather than being deleted.

All 22 people have terminal batch outcomes: one `completed`, one
`documented_prewar_employer_found`, three `needs_identity_review`, 12
`no_reliable_result_after_protocol`, four `requires_archival_review`, and one
`verified_employer_found`. Batch identity outcomes are one `confirmed`, one
`conflicting`, six `high_confidence`, two `probable`, and 12 `unresolved`.

Rebuilt coverage is **23,978/23,978** linked source rows and **23,939** active
person entities. Research-attempt coverage is **8,488/23,939 (35.4568%)**;
confirmed/high verified-employer coverage is **302/23,939 (1.2615%)**;
confirmed/high verified-affiliation coverage is **667/23,939 (2.7862%)**;
archival-review disposition coverage is **6,944/23,939 (29.0071%)**. There are
**15,446** `not_started` people, **512** possible-duplicate groups, and **218**
active conflicts. SQLite stores **15,281** attempts or plans and **5,382**
claims: 1,326 confirmed, 2,235 high, 1,433 medium, 196 low, and 192
conflicting. It contains **5,281** citation records and **2,555** unique source
documents. The public projection contains **2,318** affiliations, **767**
organizations, **4,064** sources, and **5,179** claims.

The oil-company category remains prominent at the top of the home page and
personnel directory and on its dedicated route. It remains evidence-scoped to
**eight people across ten historically named companies**. Batch 670 adds no
oil-company member. Full-index historical research is unfinished.

## Replay and continuation

After importing prior durable batches into private SQLite:

```sh
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
python3 -m oss_research import-reviewed-evidence research/evidence-page326-monroe-montgomery-review_batch-670_2026-09-25.json
python3 -m oss_research import-review-decisions research/identity_review_decisions_2026-09-25_batch670.csv
python3 -m oss_research export-adapter-checkpoints
python3 -m oss_research export-derived
python3 -m oss_research export-review-queue
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
```

Adapter checkpoints must be imported before the final reviewed evidence and
decisions so temporary adapter states cannot supersede the batch's reviewed
research dispositions.

No API key, full service number, raw Catalog API response, copyrighted page
image, or private reviewer note is committed or included in the public site.
