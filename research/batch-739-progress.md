# Batch 739: Patterson-Paul research

Batch 739 completes PDF page 360, rows 1-23, from **John B Patterson**
through **Robert W Paul**. A 300-dpi visual inspection confirmed all 23
printed rows in Boxes 589-590 at location 230/86/38/03. Embedded text was
checked against the page render. Original spellings, ranks, civilian grades,
notes, and protected identifiers remain recoverable in the private database.
The visibly truncated note **“Danish c”** for Troy Patterson is preserved
literally rather than expanded by inference.

Four people have new high-confidence identity assessments based on exact
official Army name-and-protected-identifier agreement: **Joseph A
Patterson**, **William W Patterson**, **Joseph D Patti**, and **John B
Patton**. The Army entry-grade sequence for John B Patton is compatible with
the later staff-sergeant rank in the OSS index. Joseph D Patti's printed
**French** note remains authoritative context; the Army match does not
silently reclassify his nationality or relationship to OSS. These official
matches establish identity only. Protected identifiers and coded Army data
remain private and are not converted into employer or occupation claims.

**Archimedes L Patti** retains a high-confidence identity link to OSS officer
Archimedes L. A. Patti. Official National Park Service and wartime records
document his OSS service, but the accessible evidence reviewed in this batch
does not establish the exact immediate pre-OSS affiliation. A discovery-only
claim that the 1940 census described him as a War Department special agent is
not published because the underlying census image was not verified. His Box
589 personnel file and the original census image remain the next evidence
targets.

The remaining common, initials-only, and incomplete names could not be
resolved safely. Searches rejected modern professionals, athletes, an
unrelated Medal of Honor recipient, Civil War records, ambiguous obituaries
and directories, and the British film pioneer Robert W. Paul, who died in
1943. None had the corroborating identifiers and chronology required for
publication. CIA Reading Room robots unavailability and a transient Library
of Congress adapter failure are recorded as access failures, never as
negative evidence.

All 23 people have terminal `requires_archival_review` dispositions. Identity
statuses are five `high_confidence` and 18 `unresolved`. The reviewed bundle
imports two sources, four identity claims, eight claim-source links, 23 person
updates, and 23 consolidated research attempts. Four identity-review
decisions are accepted. No employer or other affiliation is added without
supporting evidence.

Rebuilt coverage is **23,978/23,978** linked source rows and **23,939** active
person entities. Research-attempt coverage is **10,029/23,939 (41.8940%)**;
confirmed/high verified-employer coverage is **334/23,939 (1.3952%)**;
confirmed/high verified-affiliation coverage is **748/23,939 (3.1246%)**;
archival-review disposition coverage is **8,488/23,939 (35.4568%)**. There
are **13,905** `not_started` people, **525** possible-duplicate groups, and
**334** active conflicts. SQLite stores **18,368** attempts or plans and
**6,407** claims: 1,383 confirmed, 2,989 high, 1,539 medium, 198 low, 296
conflicting, and two unresolved. It contains **5,735** citation records and
**2,903** unique source documents. The public projection contains **2,495**
affiliations, **866** organizations, **4,511** sources, and **6,200** claims.
Full-index historical research remains unfinished.

## Replay and continuation

After importing prior durable batches into private SQLite:

~~~sh
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
python3 -m oss_research assign-page-batch --batch-name batch-739-patterson-paul --page 360 --first-row 1 --last-row 23
python3 -m oss_research research --source cia --batch batch-739-patterson-paul --max-queries 23
python3 -m oss_research research --source loc --batch batch-739-patterson-paul --max-queries 23
python3 -m oss_research research --source web --batch batch-739-patterson-paul --resume --max-queries 23 --dry-run
python3 -m oss_research import-review-decisions research/identity_review_decisions_2026-10-04_batch739.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page360-patterson-paul-review_batch-739_2026-10-04.json
python3 -m oss_research export-adapter-checkpoints
python3 -m oss_research export-derived
python3 -m oss_research export-review-queue
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
~~~

Adapter checkpoints must be imported before final reviewed decisions and
evidence so temporary discovery states cannot supersede reviewed dispositions.
The next research boundary is PDF page 360, rows 24-46, from Victoria A Paul
through Eugene D Pawley.

No API key, full service or officer number, raw Catalog or LoC API response,
copyrighted page image, street address, living-relative detail, modern
people-finder record, unrelated Army coded occupation, or private reviewer
note is committed or included in the public site. No authenticated NARA
Catalog API request was made for this batch.
