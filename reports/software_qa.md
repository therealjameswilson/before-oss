# Software QA

Run: 2026-07-29 UTC

- Python unit tests: **29 / 29 passed**
- Astro type/content diagnostics: **0 errors, 0 warnings, 0 hints**
- Production dependency audit: **0 known vulnerabilities**
- Static production build: **24,052 pages**
- Internal link check: **24,052 HTML files passed**
- Browser and accessibility suite: **81 / 81 passed**
- Deterministic stratified profile audit: **200 / 200 passed all checks**
- Deterministic production rebuild: **identical SHA-256 content-tree hashes**
- Public redaction build: **passed**
- Public search rows: **23,941**
- Public source rows represented: **23,978**
- Public full service-number fields: **0**
- Runtime authenticated API calls: **0**
- Reviewed public sources: **157** public records representing **152** unique documents
- Published, qualified affiliations: **142**
- Published claims: **217**
- Verified-affiliation metric: **66** people with confirmed/high published
  evidence of any modeled pre-OSS relationship
- Verified-employer metric: **37** people with confirmed/high published
  employment or self-employment evidence
- Live NARA Catalog API requests: **0**
- GitHub Actions test workflow
  [30456073409](https://github.com/therealjameswilson/before-oss/actions/runs/30456073409)
  for Batch 013 release `29d1afd`: **passed**
- GitHub Pages deployment workflow
  [30456078271](https://github.com/therealjameswilson/before-oss/actions/runs/30456078271)
  for Batch 013 release `29d1afd`: **passed**
- Production route smoke tests: **20 / 20 returned HTTP 200**

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
