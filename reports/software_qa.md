# Software QA

Run: 2026-07-30 UTC

- Python unit tests: **30 / 30 passed**
- Astro type/content diagnostics: **0 errors, 0 warnings, 0 hints**
- Production dependency audit: **0 known vulnerabilities**
- Static production build: **24,133 pages**
- Internal link check: **24,133 HTML files passed**
- Browser and accessibility suite: **150 / 150 passed**
- Deterministic stratified profile audit: **200 / 200 passed all checks**
- Deterministic production rebuild: **identical SHA-256 content-tree hashes**
  (`ce0abcb9972286dc6298bf0c170042699e1c19dd0d2b8ed52f148ff5ab485f7f`)
- Public redaction build: **passed**
- Public search rows: **23,941**
- Public source rows represented: **23,978**
- Public full service-number fields: **0**
- Boundary-aware scan of **12,799** distinct normalized private service
  numbers at least six characters long: **0 full-number matches** in **24,213**
  uncompressed public assets, generated site data, or production HTML
- Runtime authenticated API calls: **0**
- Reviewed public sources: **403** public records representing **375** unique documents
- Published, qualified affiliations: **310**
- Published claims: **512**
- Withheld low-confidence identity candidates: **5**
- Verified-affiliation metric: **160** people with confirmed/high published
  evidence of any modeled pre-OSS relationship
- Verified-employer metric: **95** people with confirmed/high published
  employment or self-employment evidence
- Live NARA Catalog API requests: **0**
- GitHub Actions test workflow
  [30504300894](https://github.com/therealjameswilson/before-oss/actions/runs/30504300894)
  for Batch 036 release `0b5f45a`: **passed**
- GitHub Pages deployment workflow
  [30504300872](https://github.com/therealjameswilson/before-oss/actions/runs/30504300872)
  for Batch 036 release `0b5f45a`: **passed**
- Production route and asset smoke tests: **22 / 22 returned HTTP 200 and the
  expected content marker or row count**

GitHub emitted a non-blocking annotation that several official actions still
target Node.js 20 internally and were forced onto Node.js 24 by the runner. It
did not affect either workflow result.

The initial dependency range resolved to an older Astro major with current
security advisories. The project was upgraded to Astro 7.1.5 and sharp 0.35.3;
the production audit then passed.

The metric regression test verifies that student, military, government,
volunteer, and professional affiliations do not inflate verified-employer
coverage. Batch 011 adds explicit browser checks for concurrent civilian
appointments, predecessor-agency and military pathways, an unnamed business
that was not guessed, and a documented professional affiliation that remains
excluded from employer analytics.
Batch 012 adds regression checks for qualified military transitions, unnamed
newspaper employers, student history, expedition participation, and a
documented earlier academic appointment that remains separate from the
immediate pre-OSS field.
Batch 013 adds checks for a career-military pathway without an invented
civilian employer, distinct civilian-cover and earlier academic employment,
the indexed spelling of a probable identity, and medium-confidence employment
that remains visibly qualified and excluded from default analytics.
Batch 014 adds checks for an Allied military transfer, concurrent employers,
student status without an employer inference, a government-to-OSS pathway
separate from the last civilian employer, and an officially documented but
deliberately unnamed self-employed business.
Batch 015 adds checks for an academic-to-government pathway, fashion employment,
a medium-confidence academic predecessor, student status without an employer
inference, and an unnamed printing business followed by three distinct military
assignments.
Batch 016 adds checks for an academic-to-Army pathway, a predecessor intelligence
agency, a design-office recruitment, a qualified War Department transition,
government design assignments, documented name variants, and an occupation-only
result that does not invent an employing school system.
Batch 017 adds checks for an institutional membership that remains distinct
from employment, overlapping academic appointments that are not silently ended
at OSS entry, a visibly qualified Board of Economic Warfare transition, the
Haje/Hajo Holborn indexed-name distinction, and a documented-prewar teaching
history that does not invent a last civilian employer.
Batch 018 adds checks for continuing academic employment, explicit
university-to-Army transitions, graduate-student status that is not converted
into employment, commissioned service kept outside civilian-employer analytics,
and a visibly qualified Princeton-to-OSS chronology with an undocumented
interval.
Batch 019 adds checks for a direct Federal Reserve-to-OSS transition, an
earlier international-bank role kept out of the immediate field, an academic
employer-to-Army-to-OSS sequence, doctoral study that remains non-employment,
and a predecessor-agency appointment from a continuing university position.
Batch 020 adds checks for student status at Ohio State and Columbia, distinct
NBER and Federal Reserve employment, a production-management government
assignment kept separate from Harvard employment, an earlier Labor Department
assignment, and approved unresolved-employer wording for archival review.
Batch 021 adds checks for Columbia and Duke faculty employment, Yale student
status that is not converted into employment, a Federal Reserve Board pathway
kept distinct from an earlier Federal Reserve Bank employer, overlapping NBER
and OPA appointments, and approved unresolved-employer wording where Barrington
Moore Jr.'s accessible institutional biography establishes student status but
not a pre-OSS employer.
Batch 022 adds checks for MoMA employment followed by OSS service, University
of Toronto employment kept distinct from an earlier University of Hawaii
appointment, continuing Columbia and Yale faculty appointments, and Rhoda
Métraux's National Research Council employment kept separate from her earlier
Oxford University Press employment and Yale student status.
Batch 023 adds checks for the COI-to-OSS institutional succession; college,
museum, university, and federal employment; a government-to-Army-to-OSS
sequence; student status that remains outside employer analytics; an unfamiliar
grade that remains unclassified; and source-title discrepancies preserved
rather than silently reconciled.
Batch 024 adds checks for an academic employer followed by an unresolved
British-Army/OSS sequence, a continuing Harvard appointment with explicit
wartime leave, Harvard-to-COI-to-OSS chronology, student status followed by
Army service, private service-number redaction, and a medium-confidence
teaching-assistant lead whose temporal uncertainty is visible and excluded
from default analytics. It also adds the missing temporal-basis badge to all
earlier-affiliation cards.
Batch 025 adds checks for COI and Army predecessor assignments separated from
civilian employment, graduate study modeled as student status, a documented
Army-to-OSS transfer without an invented civilian employer, and two same-name
rows that retain distinct masked service numbers. It also publishes
identity-resolution notes for reviewed non-unresolved profiles while keeping
the low-confidence Paul Marlor Sweezy candidates out of public claims.
Batch 026 adds checks for freelance work modeled as self-employment, a
Women’s Army Corps assignment kept separate from a civilian oil-company job,
two newspaper employers kept in chronological order, Mills College modeled as
student status rather than employment, and an unresolved pre-OSS employer
routed to archival review. The five profile checks also verify item-level
citations and continued service-number masking.
Batch 027 adds checks for a direct university-employment pathway, independent
scholarship modeled as a professional affiliation rather than an employer, a
bank employer kept separate from a naval assignment, an officially documented
finance occupation whose unnamed employer is not guessed, and a contemporary
business-directory affiliation that is not converted into salaried
employment. It also replaces runtime build timestamps with a durable
data-snapshot timestamp and excludes the manifest from hashing itself, making
consecutive public-data builds byte-for-byte identical.
Batch 028 adds checks for an explicit Office of Price Administration pathway,
an earlier unnamed family timber business, and a Brookings fellowship that is
not silently converted into employment. It also verifies a qualified textile
employer with a documented chronology gap; a last civilian investment-bank
employer that is not mislabeled immediate; an Army pathway and Brown student
history without an invented civilian employer; and a wartime Mercersburg
student affiliation that remains qualified and routed to archival review.
Batch 029 adds checks for an explicit British Special Operations Executive
assignment following Shanghai Municipal Police employment; U.S. Navy, Coast
Guard, Signal Corps, and Army Air Corps radio pathways; university attendance
modeled as student status rather than employment; merchant-marine service kept
as a professional affiliation rather than a guessed single employer; and an
officially documented runner occupation whose employer remains unnamed.
Batch 030 adds checks for two named civilian employers followed by Army or
Marine Corps service; an unnamed Oklahoma journalism occupation that is not
converted into an employer; a qualified Federal Bureau of Narcotics pathway;
an explicit Corps of Engineers recruitment sequence; and Penn State
engineering and ROTC participation kept as student status.
Batch 031 adds checks for three Army predecessor pathways, American University,
Washington State, Penn State, and University of Oregon student affiliations,
and a qualified Oregon State athletic association. It preserves the indexed
`Albert Robinso` form, does not invent civilian employers for any of the five
people, and keeps Applegate's two Oregon institutional references distinct.
Batch 032 adds checks for Ainsworth Blogg's Army Military Police pathway and
unnamed Seattle insurance occupation; the visually confirmed Louise D. Cohen
index row that remains unlinked from the Louis/Lewis Cohen candidate; Morris M.
Kessler's qualified probable identity; and Joseph E/M Lazarsky and Leopold
Karwoski's Fort Belvoir Army Engineer pathways. It also restores the manual-
review flag on Edgar A. Prichard's pre-existing service-number conflict group.
Batch 033 adds checks for George S. Wuchinich's qualified Fairbanks-Morse
employment and explicit Army pathway; Hans V. Tofte's distinct Army and British
SOE assignments; Howard E. Manning's individual legal practice without
assigning the separate Manning & Manning firm; and the occupation-only Navarro
and Mero results without invented employers.
Batch 034 adds checks for James F. Ranney's Signal Corps pathway and unnamed
Youngstown radio-station occupation; Spyridon G. Kapponnis's Michigan State
College, Navy, and direct USNR mission evidence; Arthur F. Reinhardt's Army Air
Corps transition; Gail F. Donnalley's Ohio Wesleyan student status; and John W.
Brunner's Army language course and deliberately unnamed pre-draft college.
Batch 035 adds checks for Timothy R. Marsh's explicitly civilian Signal Corps
employment and earlier Coyne Radio School study; Lawrence W. Lowman's CBS
operations leadership; John M. Balsamo's probable, occupation-only Wall Street
telegrapher identification without a guessed firm; William R. Peers's qualified
Army pathway without an invented civilian employer; and Nicol Smith's
self-employed travel writing without assigning a publisher as employer.
Batch 036 adds checks for Lawrence Hollander's documented lawyer occupation
without inventing a firm or private practice; preserves the L. L. Hollander row
as a separate ambiguous entity in the same duplicate-review group; keeps Marvin
S. Flisser's Brooklyn College student affiliation outside employer analytics;
separates Willis S. Georgia Jr.'s Navy assignment from student history; and
records Robert R. Kehoe's Signal Corps pathway and unnamed chemical-plant work
without guessing the company.
