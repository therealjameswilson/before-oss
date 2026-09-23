# Batch 656: Mezoff-Mielziner research

The PDF-page 319 `Eleanor E. Mezoff` through `Jo Mielziner` queue contains
**22 source rows and 22 cautious person entities**. Every person received a
saved, reviewed outcome from the NARA-index context, official Army bulk
identity comparison where applicable, a bounded Library of Congress search,
exact-name OSS searching, employment or occupation searching, and
institutional, obituary, newspaper, or archival searching as applicable. No
authenticated NARA Catalog request was made.

The CIA Reading Room adapter stopped on the source's robots restriction at its
first query. The Library of Congress adapter completed 18 valid name searches;
it saved five newspaper-page candidates for two people and recorded one source
error. All five candidates were reviewed. None became final evidence because
they lacked a sufficient identity or chronological bridge. Three incomplete
or ambiguous names were rejected by adapter validation rather than sent as
unsafe searches.

The principal findings preserve identity, relationship, and chronology limits:

- **Jerry G. Mican** is confirmed from the NARA row, a unique protected Army
  identifier, National Park Service OSS history, and a Defense POW/MIA record.
  The Army is his immediate pre-OSS institutional pathway. Teaching foreign
  languages at an unidentified Chicago high school is retained as an
  occupation-only finding; no school is invented.
- **Roman Michalowski** is confirmed through a Polish state-archive biography
  that explicitly identifies his OSS employment. His 1942 deputy directorship
  at the Interallied Information Center is modeled as his last named civilian
  or government assignment before Army service; Army service is the probable
  immediate OSS pathway, and his earlier editorship of *New Europe* remains a
  separate pre-OSS role.
- **Charles A. Micaud** is a high-confidence identity match to the Bowdoin
  fellow and teaching fellow in French documented in 1939-1941. Bowdoin is a
  documented earlier employer, not an asserted immediate predecessor.
- **Alfredo Michelagnoli** is a high-confidence match to the antifascist known
  as Fred. His English teaching, writing, and acting are occupation-only
  findings. His Allied volunteering and Algeria training remain a qualified
  military pathway because the accessible source does not identify a command.
- **Jo Mielziner** is a high-confidence match to the theatrical designer. Army
  Air Forces camouflage work is his best-supported immediate military pathway
  before OSS transfer. His established theatrical design occupation is not
  converted into a named civilian employer.
- Six additional Army bulk crosswalks are accepted as identity evidence only.
  Army occupation codes are not converted into employer claims. The printed
  `Stevens S. Micheals` spelling remains intact alongside the official Army
  `Michaels` variant.
- **Gimino Michelangelo** remains conflicting because the protected identifier
  points to a completely different Army name. **I. Michel** remains separate
  from `Michel M. Ivy`, whose distinct Box 365 row shares the protected
  identifier. Both cases require personnel-file comparison.
- No reliable predecessor employer was found online for the other people.
  Their profiles identify the indexed file and the archival question that
  remains open; this is not evidence that no earlier employment existed.

The cohort ends with **15** `requires_archival_review`, three
`occupation_only_found`, two `documented_prewar_employer_found`, and two
`conflicting_sources` statuses. Identity statuses are two `confirmed`, eight
`high_confidence`, two `conflicting`, and ten `unresolved`. The reviewed bundle
adds **22 claims**: three confirmed, 16 high, one medium, and two conflicting;
it adds seven affiliations and 15 cited source documents. All 13 generated
candidates were reviewed, leaving zero unreviewed candidates in the cohort.

Rebuilt coverage is **23,978/23,978** linked source rows and **23,939** active
person entities. Research-attempt coverage is **8,184/23,939 (34.1869%)**;
confirmed/high verified-employer coverage is **293/23,939 (1.2239%)**;
confirmed/high verified-affiliation coverage is **650/23,939 (2.7152%)**;
archival-review disposition coverage is **6,640/23,939 (27.7372%)**. There are
**15,750** `not_started` people, **498** possible-duplicate groups, and **197**
active conflicts. SQLite stores **14,230** attempts or plans and **5,200**
claims: 1,315 confirmed, 2,108 high, 1,416 medium, 189 low, and 172
conflicting. It contains **5,184** citation records and **2,478** unique source
documents. The public projection contains **2,282** affiliations, **750**
organizations, **3,974** sources, and **5,007** claims.

The oil-company category remains prominent at the top of the personnel
directory and on its dedicated page. It remains evidence-scoped to **eight
people across ten historically named companies**; no Batch 656 occupation or
military pathway was misclassified as oil-company employment. Full-index
historical research is unfinished.

## Replay and continuation

After importing prior durable batches into private SQLite:

```sh
python3 -m oss_research import-review-decisions research/identity_review_decisions_2026-09-23_batch656.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page319-mezoff-mielziner-review_batch-656_2026-09-23.json
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
```

Continue with the next bounded research batch, then run:

```sh
python3 -m oss_research export-adapter-checkpoints
python3 -m oss_research export-derived
python3 -m oss_research export-review-queue
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
```

No API key, full service number, raw Catalog API response, copyrighted page
image, or private reviewer note is committed or included in the public site.
