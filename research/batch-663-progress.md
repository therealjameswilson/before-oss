# Batch 663: Millett-Milton research

The contiguous queue on PDF page 322 rows 32-46 and page 323 rows 1-7, from
`Susan C. Millett` through `Billy G. Milton`, contains **22 source rows and 22
cautious person entities**. Every person has a saved, reviewed outcome grounded
in the NARA index, official Army bulk identity comparison where applicable,
exact-name and rank or grade OSS searches, employment and occupation searches,
and institutional, professional-journal, military-history, obituary, or
archival checks as applicable. No authenticated NARA Catalog request was made.

Rendered images of both source pages were checked against the stored rows.
Page 322 ends with Henry E. Mills and page 323 begins with Hiram J. Mills. Anne
Milliken's printed note remains the literal truncated text `British ar`; it was
not silently expanded. All ranks, blank fields, boxes, locations, and private
identifiers in the cohort agree with the page images.

The reviewed findings preserve identity, relationship, and chronology limits:

- **Cary B. Millholland** is a high-confidence match to landscape architect
  Cary Blunt Millholland Parker. The Cultural Landscape Foundation dates her
  own practice to 1937-1942 and then places her in War Department work on OSS
  contour maps. Her practice is the last documented civilian work before
  service, not an immediate pre-OSS affiliation. A contemporary American
  Horticultural Society roster documents her 1942 secretaryship as a
  professional affiliation, not an employer.
- **John R. Milodragovich** is a high-confidence distinctive-name and captain-
  rank match. A contemporary professional journal says he began his U.S.
  Forest Service career on the Deerlodge and Kootenai National Forests before
  World War II; a separate scholarly history corroborates his OSS identity.
  The Forest Service is modeled as his last civilian government assignment,
  not immediate pre-OSS work, because wartime military service intervened.
- **Donald D. Millikin's** wartime New York University cryptography teaching
  is published only as a medium-confidence probable professional affiliation.
  The reviewed source does not establish an employment relationship or an
  immediate OSS transition.
- **Anne Milliken** is a high-confidence match to the woman documented in OSS
  Rome by a university doctoral thesis. The same source's family-company and
  heiress references do not establish her employment, so no company claim was
  published.
- An official National Park Service history identifies **Major Francis B.
  Mills** as Francis Byron "Frank" Mills and corroborates his OSS assignments
  in Europe and northern China. It does not name a pre-OSS civilian employer.
- Exact protected Army matches support high-confidence identities for **Spiro
  H. Millios** and **Hiram J. Mills**. **George T. Milstein** remains probable
  because the Army record omits the indexed middle initial. **Clayton G.
  Milligan** remains conflicting because the official Army record tied to the
  indexed identifier names Clayton G. Millikan. Army occupation codes remain
  private identity context and are not converted into employer claims.
- The remaining thirteen people have explicit terminal no-reliable-result
  outcomes and archival next actions rather than unsupported biographies.

The cohort contains two `verified_employer_found`, one
`occupation_only_found`, one `conflicting_sources`, and 18 terminal unresolved
or archival dispositions. The reviewed bundle adds **13 claims**, four
affiliations, four organizations, nine sources, and 24 claim-source links. All
four generated identity candidates received decisions, and all 22 people have
terminal batch outcomes.

Rebuilt coverage is **23,978/23,978** linked source rows and **23,939** active
person entities. Research-attempt coverage is **8,336/23,939 (34.8218%)**;
confirmed/high verified-employer coverage is **296/23,939 (1.2365%)**;
confirmed/high verified-affiliation coverage is **657/23,939 (2.7445%)**;
archival-review disposition coverage is **6,792/23,939 (28.3721%)**. There are
**15,598** `not_started` people, **506** possible-duplicate groups, and **210**
active conflicts. SQLite stores **14,728** attempts or plans and **5,288**
claims: 1,323 confirmed, 2,168 high, 1,423 medium, 189 low, and 185
conflicting. It contains **5,219** citation records and **2,504** unique source
documents. The public projection contains **2,296** affiliations, **755**
organizations, **4,009** sources, and **5,095** claims.

The oil-company category remains prominent at the top of the personnel
directory and on its dedicated page. It remains evidence-scoped to **eight
people across ten historically named companies**; no Batch 663 identity-only
record was misclassified as historical oil-company employment. Full-index
historical research is unfinished.

## Replay and continuation

After importing prior durable batches into private SQLite:

```sh
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
python3 -m oss_research import-review-decisions research/identity_review_decisions_2026-09-23_batch663.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page322-millett-page323-milton-review_batch-663_2026-09-23.json
python3 -m oss_research export-adapter-checkpoints
python3 -m oss_research export-derived
python3 -m oss_research export-review-queue
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
```

Adapter checkpoints must be imported before the final reviewed decisions and
evidence so temporary adapter states cannot supersede the batch's reviewed
research dispositions.

No API key, full service number, raw Catalog API response, copyrighted page
image, or private reviewer note is committed or included in the public site.
