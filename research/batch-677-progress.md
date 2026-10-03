# Batch 677: Moree-Morgan research

Batch 677 completes PDF page 329, rows 1-24, from `Irby E Moree` through
`Helen E Morgan`. Fresh rendered-page inspection and layout-text comparison
confirmed all 24 printed rows, Box 537, the `possibly` note for Robert C
Moreno, and Benjamin T Morgan's distinct archival location `230/86/37/01`.

Nine nonshared protected identifiers support high-confidence Army identities:
**Raymound O Morehouse, Bernard Morelli, Emil S Morelli, Ettore Morelli,
Courtland C Morelock, Cesare A Moretti, Benjamin T Morgan, Elliot W Morgan,
and Elwyn W Morgan**. The official Army bulk file's coded occupations remain
private and were not translated into employers. Raymond/Raymound and the two
damaged Army name renderings remain visible as variants instead of silently
replacing the printed index names.

Official CIA and National Park Service histories identify **Irby E. Moree** as
an original Detachment 101 sergeant and Area B trainee. This is a strong
identity and wartime-assignment finding, not evidence of a civilian employer
or immediate pre-OSS affiliation. A secondary mission roster independently
corroborates S/Sgt. **Bernard Morelli** in Operation Spokane, again without
supplying pre-OSS employment.

The strongest civilian-employment finding concerns **Jean Morere**. A French
Service historique de la Défense finding aid identifies the individual dossier
of Jean-Marie Morère, while two independent historical accounts document his
Marseille police service from 1 May 1921 until his resignation in March 1943.
The police service is modeled as his last documented civilian employer before
OSS contact, not as an immediate pre-OSS affiliation: resignation, travel
through Spain, and an attempted Free French pathway intervened.

Thirteen people reached `no_reliable_result_after_protocol`: Obel Moreira Jr.,
Gerard Moreli, Betty Morelli, Robert C Moreno, John T Morey, Anna P Morgan,
Charles P Morgan, Forrest A Morgan, Gabriel W Morgan, George M Morgan, Glen
Morgan, Harry S Morgan, and Helen E Morgan. Each receives a terminal public
research-status page and a high-priority Box 537 next action. This means that
the accessible sources reviewed did not establish a reliable pre-OSS employer;
it does not mean that no such employment existed.

The staged protocol covered the official NARA index, the official Army bulk
file where applicable, targeted official CIA-domain searches, exact-name OSS
and employment searches, 24 live Library of Congress queries, institutional
and obituary sources, directories, newspapers, and archival discovery. The
direct CIA adapter failed closed once and was not counted as negative evidence.
All 13 Library of Congress discovery candidates were rejected because they
were surname-only OCR hits without a corroborating identity bridge. The batch
review file preserves **22 decisions: 9 accepted and 13 rejected**.

The evidence bundle imports eight sources, one organization, one affiliation,
12 claims, 28 claim-source links, 24 person updates, and 24 consolidated
research attempts. The featured oil-company category remains evidence-scoped
to **eight people across ten historically named companies**; no Batch 677
claim qualifies for it.

Rebuilt coverage is **23,978/23,978** linked source rows and **23,939** active
person entities. Research-attempt coverage is **8,626/23,939 (36.0333%)**;
confirmed/high verified-employer coverage is **304/23,939 (1.2699%)**;
confirmed/high verified-affiliation coverage is **673/23,939 (2.8113%)**;
archival-review disposition coverage is **7,082/23,939 (29.5835%)**. There
are **15,308** `not_started` people, **512** possible-duplicate groups, and
**229** active conflicts. SQLite stores **15,590** attempts or plans and
**5,458** claims: 1,326 confirmed, 2,296 high, 1,438 medium, 196 low, and 202
conflicting. It contains **5,322** citation records and **2,588** unique source
documents. The public projection contains **2,327** affiliations, **771**
organizations, **4,105** sources, and **5,255** claims. Full-index historical
research remains unfinished.

## Replay and continuation

After importing prior durable batches into private SQLite:

```sh
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
python3 -m oss_research import-review-decisions research/identity_review_decisions_2026-09-25_batch677.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page329-moree-morgan-review_batch-677_2026-09-25.json
python3 -m oss_research export-adapter-checkpoints
python3 -m oss_research export-derived
python3 -m oss_research export-review-queue
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
```

Adapter checkpoints must be imported before the final reviewed decisions and
evidence so temporary discovery states cannot supersede reviewed dispositions.

No API key, full service number, raw Catalog API response, copyrighted page
image, unrelated Army name, or private reviewer note is committed or included
in the public site.
