# Batch 740: Paul-Pawley research

Batch 740 completes PDF page 360, rows 24-46, from **Victoria A Paul**
through **Eugene D Pawley**. A 300-dpi visual inspection confirmed all 23
printed rows in Boxes 590-591 at location 230/86/38/03. Embedded text was
checked against the page render. Original spellings, ranks, civilian grades,
notes, and protected identifiers remain recoverable in the private database.

Eight people have accepted identity assessments based on exact official Army
name-and-protected-identifier agreement: **Alf H Paulson**, **Leo Paur**,
**Arthur A Pava**, **Angelo J Pavan**, **Vincent Pavia**, **George Pavik**,
**Joseph Pavlacka**, and **Miles Pavlovich**. These bulk records establish
identity, Army entry chronology where used, and no employer by themselves.
Protected identifiers and coded Army data remain private.

**Arthur A Pava** has a high-confidence, evidence-backed pathway. Cornell and
New York State Agricultural Experiment Station records document part-time and
temporary entomology research appointments in 1941-1942. An obituary places
him at Cornell when he enlisted and explicitly sequences Army enlistment
before OSS acceptance. The Station is therefore modeled as his last
documented civilian employer, Cornell separately as student status, and the
United States Army as his immediate pre-OSS affiliation. The precise
appointment end and Army-to-OSS transfer date remain open.

Two direct wartime records add other carefully bounded findings. A 1944 OSS
interview says **Daniel Pavletich** was a radio operator on a merchant ship;
the ship and employing company are not named, so the profile publishes an
occupation-only affiliation without inventing an organization. A 1944 OSS
report identifies **Miles J. Pavlovich**, dates his Army entry to March 15,
1938, and says he was assigned to OSS in June 1943. His immediate predecessor
is modeled as the United States Army; no civilian employer is inferred.

A direct OSS order confirms **Charles Paveloi** through exact name, rank, and
protected identifier, and a NARA-published history corroborates **Vincent
Pavia** on a 1943 OSS team. Those records establish identities but not
pre-OSS employers or predecessor units. Their profiles remain explicit
archival-review cases.

**Eugene D Pawley** receives a qualified, medium-confidence affiliation with
the China National Aviation Corporation. A visually checked CNAC association
history places him in its Hong Kong evacuation context and membership list,
and a research essay describes him as formerly with CNAC before repatriation
in 1942. The evidence does not establish his job title, exact dates, or that
CNAC was immediately before OSS, so the affiliation is published only as
documented prewar employment and excluded from default high-confidence
analytics.

The other common, incomplete, or insufficiently bridged names remain
unresolved rather than being attached to plausible namesakes. CIA Reading
Room robots unavailability and a transient Library of Congress adapter
failure are recorded as access failures, never as negative evidence. All 23
people now have a reviewable research outcome and a next action. The bundle
imports 11 sources, 14 claims, 31 claim-source links, six affiliations, four
organizations, 23 person updates, and 23 consolidated research attempts.

Rebuilt coverage is **23,978/23,978** linked source rows and **23,939** active
person entities. Research-attempt coverage is **10,052/23,939 (41.9901%)**;
confirmed/high verified-employer coverage is **335/23,939 (1.3994%)**;
confirmed/high verified-affiliation coverage is **751/23,939 (3.1371%)**;
archival-review disposition coverage is **8,511/23,939 (35.5529%)**. There
are **13,882** `not_started` people, **525** possible-duplicate groups, and
**334** active conflicts. SQLite stores **18,416** attempts or plans and
**6,421** claims: 1,385 confirmed, 3,000 high, 1,540 medium, 198 low, 296
conflicting, and two unresolved. It contains **5,746** citation records and
**2,913** unique source documents. The public projection contains **2,501**
affiliations, **868** organizations, **4,522** sources, and **6,214** claims.
Full-index historical research remains unfinished.

## Replay and continuation

After importing prior durable batches into private SQLite:

~~~sh
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
python3 -m oss_research assign-page-batch --batch-name batch-740-paul-pawley --page 360 --first-row 24 --last-row 46
python3 -m oss_research research --source cia --batch batch-740-paul-pawley --max-queries 23
python3 -m oss_research research --source loc --batch batch-740-paul-pawley --max-queries 23
python3 -m oss_research research --source web --batch batch-740-paul-pawley --resume --max-queries 23 --dry-run
python3 -m oss_research import-review-decisions research/identity_review_decisions_2026-10-04_batch740.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page360-paul-pawley-review_batch-740_2026-10-04.json
python3 -m oss_research export-adapter-checkpoints
python3 -m oss_research export-derived
python3 -m oss_research export-review-queue
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
~~~

Adapter checkpoints must be imported before final reviewed decisions and
evidence so temporary discovery states cannot supersede reviewed dispositions.
The next research boundary is PDF page 361, beginning with the first printed
personnel row after Eugene D Pawley.

No API key, full service or officer number, raw Catalog or LoC API response,
copyrighted page image, street address, living-relative detail, modern
people-finder record, unrelated Army coded occupation, or private reviewer
note is committed or included in the public site. No authenticated NARA
Catalog API request was made for this batch.
