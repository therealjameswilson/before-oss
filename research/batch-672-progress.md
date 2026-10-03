# Batch 672: Thomas N. Moon research

Batch 672 completes the remaining printed record on PDF page 326: row 46,
`Thomas N. Moon`, T-3, Box 534. Rendered-page inspection confirmed the indexed
name, rank, box, archival location, and private identifier without publishing
the full identifier.

The reviewed evidence supports two bounded findings:

- The exact Army name and nonshared protected identifier establish a strong
  identity bridge. An official U.S. Army Special Operations history independently
  identifies **T/5 Thomas N. Moon** in the KNOTHEAD group of OSS Detachment 101
  and captions an early-1944 photograph with his full name.
- A direct 1992 Los Angeles Times interview says Moon was a nineteen-year-old
  draftee from Lincoln, Nebraska, who was transferred from the **Engineer
  Corps in Louisiana** to OSS. The database therefore records the United
  States Army Corps of Engineers as his immediate pre-OSS **military
  assignment**, with temporal basis `explicit_immediate` and high claim
  confidence. It is not represented as a civilian employer.

The rank difference between the index's T-3 and the official history's T/5 in
early 1944 remains explicit. It may reflect promotion or timing, but the
available online sources do not establish the sequence. The official Army
bulk file's coded occupation is retained only in private identity review and
is not translated into an employer.

No reliable last civilian employer before Moon's January 1943 military entry
was identified. His profile remains `requires_archival_review`; the next
action is to inspect the Box 534 personnel file and California State
University, Fullerton oral-history transcript **OH 2395** for his pre-Army
biography and exact assignment dates. Postwar writing and insurance work were
not back-projected.

The staged protocol included the NARA index context, official Army bulk data,
an official U.S. Army historical article, a CIA-domain official-source check,
a live Library of Congress search, exact-name and meaningful-variant searches,
employment and occupation searches, a contemporary retrospective interview,
an institutional oral-history pointer, and publisher and scholarly checks. The
CIA adapter failed closed when its robots policy could not be retrieved; this
was not treated as negative evidence. A public CIA-domain source supplied only
Detachment 101 bibliographic context. The unrelated Library of Congress radio
listing was rejected.

The bundle adds **one affiliation, one reused canonical organization, two
high-confidence published claims, six sources, nine claim-source links, and
one reviewed research attempt**. Two review decisions record one accepted Army
identity candidate and one rejected LoC candidate. The oil-company category
remains at **eight people across ten historically named companies**; Thomas N.
Moon is not included.

Rebuilt coverage is **23,978/23,978** linked source rows and **23,939** active
person entities. Research-attempt coverage is **8,511/23,939 (35.5529%)**;
confirmed/high verified-employer coverage is **302/23,939 (1.2615%)**;
confirmed/high verified-affiliation coverage is **668/23,939 (2.7904%)**;
archival-review disposition coverage is **6,967/23,939 (29.1031%)**. There are
**15,423** `not_started` people, **512** possible-duplicate groups, and **222**
active conflicts. SQLite stores **15,329** attempts or plans and **5,397**
claims: 1,326 confirmed, 2,243 high, 1,436 medium, 196 low, and 196
conflicting. It contains **5,293** citation records and **2,563** unique source
documents. The public projection contains **2,319** affiliations, **767**
organizations, **4,076** sources, and **5,194** claims. Full-index historical
research remains unfinished.

## Replay and continuation

After importing prior durable batches into private SQLite:

```sh
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
python3 -m oss_research import-reviewed-evidence research/evidence-page326-moon-review_batch-672_2026-09-25.json
python3 -m oss_research import-review-decisions research/identity_review_decisions_2026-09-25_batch672.csv
python3 -m oss_research export-adapter-checkpoints
python3 -m oss_research export-derived
python3 -m oss_research export-review-queue
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
```

Adapter checkpoints must be imported before the final reviewed evidence and
decisions so temporary discovery states cannot supersede the reviewed
disposition.

No API key, full service number, raw Catalog API response, copyrighted page
image, or private reviewer note is committed or included in the public site.
