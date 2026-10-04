# Batch 738: Paterson-Patterson research

Batch 738 completes PDF page 359, rows 24-46, from **Lewis C Paterson**
through **Jere W Patterson**. A 300-dpi visual inspection confirmed all 23
printed rows in Boxes 588-589 at locations 230/86/38/02 and 230/86/38/03.
Embedded text was checked against the page render. Original spellings, ranks,
grades, notes, and protected identifiers remain recoverable in the private
database.

The two adjacent **Lewis C Paterson** entries remain separate source records
and separate person entities. Official Army data supports the enlisted row at
high identity confidence; the second-lieutenant row remains only a probable
match to the same person. Their distinct protected identifiers require direct
comparison of both Box 588 files. The profiles expose the possible-duplicate
group, and no affiliation is copied between them.

Ten people have high-confidence identity assessments based on exact official
Army bulk matches: the enlisted Lewis C Paterson, **John F Patoch Jr.**, **Fred
F Patrone**, **Paul Patsoros**, **Paul B Pattee**, **Alexander R Patterson**,
**Gardner Patterson**, **James L Patterson**, **James P Patterson**, and
**Jere W Patterson**. Jere's two bulk entries are duplicates describing one
identity. These records establish identity only. Protected identifiers and
coded Army data remain private and are not converted into employer or
occupation claims.

Institutional and scholarly sources resolve the printed **Pises Pattaborgse**
at high confidence as **Pises Pattabongse**, also rendered **Phiset
Pattaphong**. Cornell's official early-Asian-alumni index and 1939-40 register
document his mechanical-engineering study from 1938 to 1940 and BME in 1940.
A December 1945 Cornell Alumni News article and E. Bruce Reynolds's scholarly
index corroborate the name variants and Free Thai/OSS context. Cornell is
published strictly as a `student` affiliation, not an employer, and the
accessible sources do not establish his immediate pre-OSS assignment.

The distinctive printed name **Larissa Patrekeyeva** is linked only
probabilistically to the later Library of Congress research analyst of the
same romanized name. That postwar evidence is useful for identity resolution
but does not document pre-OSS employment. Her profile therefore remains
qualified and requests archival review.

The indexed **Gardner Patterson** is not the prominent economist and Navy
officer of the same name. His official Army identifier resolves the indexed
record at high confidence, while the namesake biography documents a
contradictory wartime path. No Treasury, Navy, or academic affiliation from
the namesake is transferred. Likewise, postwar Parker Pen and advertising
leads for Jere W Patterson are not treated as pre-OSS evidence without a
chronological bridge.

All 23 people have terminal dispositions for this batch: 22 require archival
review and one is completed with a documented prewar student affiliation.
Identity statuses are 11 high_confidence, two probable, and ten unresolved.
The reviewed bundle imports eight sources, one organization, one affiliation,
14 claims, 30 claim-source links, 23 person updates, and 23 consolidated
research attempts. Eleven identity-review decisions are accepted, including
two duplicate official bulk rows for Jere W Patterson.

Rebuilt coverage is **23,978/23,978** linked source rows and **23,939** active
person entities. Research-attempt coverage is **10,008/23,939 (41.8063%)**;
confirmed/high verified-employer coverage is **334/23,939 (1.3952%)**;
confirmed/high verified-affiliation coverage is **748/23,939 (3.1246%)**;
archival-review disposition coverage is **8,466/23,939 (35.3649%)**. There
are **13,926** not_started people, **525** possible-duplicate groups, and
**334** active conflicts. SQLite stores **18,321** attempts or plans and
**6,403** claims: 1,383 confirmed, 2,985 high, 1,539 medium, 198 low, 296
conflicting, and two unresolved. It contains **5,733** citation records and
**2,902** unique source documents. The public projection contains **2,495**
affiliations, **866** organizations, **4,509** sources, and **6,196** claims.
Full-index historical research remains unfinished.

## Replay and continuation

After importing prior durable batches into private SQLite:

~~~sh
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
python3 -m oss_research assign-page-batch --batch-name batch-738-paterson-patterson --page 359 --first-row 24 --last-row 46
python3 -m oss_research research --source cia --batch batch-738-paterson-patterson --max-queries 23
python3 -m oss_research research --source loc --batch batch-738-paterson-patterson --max-queries 23
python3 -m oss_research research --source web --batch batch-738-paterson-patterson --resume --max-queries 23 --dry-run
python3 -m oss_research import-review-decisions research/identity_review_decisions_2026-10-04_batch738.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page359-paterson-patterson-review_batch-738_2026-10-04.json
python3 -m oss_research export-adapter-checkpoints
python3 -m oss_research export-derived
python3 -m oss_research export-review-queue
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
~~~

Adapter checkpoints must be imported before final reviewed decisions and
evidence so temporary discovery states cannot supersede reviewed dispositions.
The next research boundary is PDF page 360, rows 1-23, from John B Patterson
through Robert W Paul.

No API key, full service or officer number, raw Catalog or LoC API response,
copyrighted page image, street address, living-relative detail, modern
people-finder record, unrelated Army coded occupation, or private reviewer
note is committed or included in the public site. CIA robots unavailability
and a transient LoC network failure were recorded as source-access failures,
not negative evidence. No authenticated NARA Catalog API request was made for
this batch.
