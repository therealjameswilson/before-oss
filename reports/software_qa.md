# Software QA

Run: 2026-07-29 UTC

- Python unit tests: **29 / 29 passed**
- Astro type/content diagnostics: **0 errors, 0 warnings, 0 hints**
- Production dependency audit: **0 known vulnerabilities**
- Static production build: **24,099 pages**
- Internal link check: **24,099 HTML files passed**
- Browser and accessibility suite: **111 / 111 passed**
- Deterministic stratified profile audit: **200 / 200 passed all checks**
- Deterministic production rebuild: **identical SHA-256 content-tree hashes**
  (`df99deeac6ff6fc80825e3d673f206f3e71a991038c8d072b23673cb1b2c53f0`)
- Public redaction build: **passed**
- Public search rows: **23,941**
- Public source rows represented: **23,978**
- Public full service-number fields: **0**
- Runtime authenticated API calls: **0**
- Reviewed public sources: **293** public records representing **274** unique documents
- Published, qualified affiliations: **232**
- Published claims: **363**
- Verified-affiliation metric: **113** people with confirmed/high published
  evidence of any modeled pre-OSS relationship
- Verified-employer metric: **78** people with confirmed/high published
  employment or self-employment evidence
- Live NARA Catalog API requests: **0**
- GitHub Actions test workflow
  [30481677007](https://github.com/therealjameswilson/before-oss/actions/runs/30481677007)
  for Batch 024 release `6c6ec57`: **passed**
- GitHub Pages deployment workflow
  [30481677016](https://github.com/therealjameswilson/before-oss/actions/runs/30481677016)
  for Batch 024 release `6c6ec57`: **passed**
- Production route smoke tests: **20 / 20 returned HTTP 200 and the expected content marker**

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
