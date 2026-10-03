# Batch 688: Munger-Murphy research

Batch 688 covers PDF page 334, rows 24-46, from `Corlyn F Munger` through
`Catherine H Murphy`. Fresh visual inspection and layout-text comparison
confirmed all 23 printed rows, including James O Murdock's literal truncated
note `docume`. Every source row remains linked to its own person entity, and
the original index spelling remains recoverable.

Official Army bulk data supports high-confidence identities for **Tadao
Murata** and **Augustine J Murphy** through exact-name and nonshared protected-
identifier agreement. Those matches establish identity only. Army coded
occupations are not converted into named employers or immediate pre-OSS
affiliations.

Three people retain explicit identity conflicts. **Avary C Munroe** shares a
protected identifier with a separate Avary C Monroe source row in Box 532,
and the Army bulk spelling agrees with Monroe rather than the Box 546 Munroe
row. Both people remain separate. **Nick Murdick** conflicts with Army bulk
name Michael Larrick, while **Joseph Muredon** conflicts with Army bulk name
Joseph Mureddu. No independent source resolves either disagreement, so no
spelling correction, variant, merge, or employer is published.

Targeted research rejected several superficially attractive leads. A
Densho-hosted Tadao or Ted Murata combat-team biography begins Army service in
1943 and conflicts with this person's official Army entry chronology.
Winthrop R Munyan's later law-firm and institutional records remain postwar
and unbridged to the indexed private first class. A wartime train list for
Kanryo Murakami lacks a second identifier, and Heart Mountain and later Ben K
Murayama newspaper references do not bridge the printed `Benk Murayame` row
to OSS. These are documented discovery paths, not public identity or employer
claims.

The cohort ends with 20 `no_reliable_result_after_protocol` and three
`conflicting_sources` outcomes. Identity statuses are two `high_confidence`,
three `conflicting`, and 18 `unresolved`. No negative online result is
represented as proof that prior employment did not exist; unresolved
questions route to the indexed Box 546 personnel jackets and, for Avary C
Munroe, comparison with the Box 532 jacket.

The evidence bundle imports two official sources, 28 claims, 33 claim-source
links, 23 person updates, and 23 consolidated research attempts. Six reviewed
candidate decisions are preserved separately: two accepted identity matches
and four conflict decisions covering three people.

Rebuilt coverage is **23,978/23,978** linked source rows and **23,939** active
person entities. Research-attempt coverage is **8,873/23,939 (37.0650%)**;
confirmed/high verified-employer coverage is **310/23,939 (1.2950%)**;
confirmed/high verified-affiliation coverage is **687/23,939 (2.8698%)**;
archival-review disposition coverage is **7,330/23,939 (30.6195%)**. There are
**15,061** `not_started` people, **517** possible-duplicate groups, and **252**
active conflicts. SQLite stores **16,031** attempts or plans and **5,666**
claims: 1,336 confirmed, 2,453 high, 1,456 medium, 196 low, and 225
conflicting. It contains **5,401** citation records and **2,650** unique source
documents. The public projection contains **2,358** affiliations, **790**
organizations, **4,184** sources, and **5,463** claims. The featured oil-
company category remains **nine people across 11 historically named
companies**. Full-index historical research remains unfinished.

## Replay and continuation

After importing prior durable batches into private SQLite:

```sh
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
python3 -m oss_research import-review-decisions research/identity_review_decisions_2026-10-02_batch688.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page334-munger-murphy-review_batch-688_2026-10-02.json
python3 -m oss_research export-adapter-checkpoints
python3 -m oss_research export-derived
python3 -m oss_research export-review-queue
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
```

Adapter checkpoints must be imported before final reviewed decisions and
evidence so temporary discovery states cannot supersede reviewed dispositions.

No API key, full service number, raw Catalog API response, copyrighted page
image, unrelated Army coded occupation, or private reviewer note is committed
or included in the public site.
