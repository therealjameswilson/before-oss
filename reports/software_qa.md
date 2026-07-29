# Software QA

Run: 2026-07-29 UTC

- Python unit tests: **28 / 28 passed**
- Astro type/content diagnostics: **0 errors, 0 warnings, 0 hints**
- Production dependency audit: **0 known vulnerabilities**
- Static production build: **23,995 pages**
- Internal link check: **23,995 HTML files passed**
- Browser and accessibility suite: **57 / 57 passed**
- Deterministic stratified profile audit: **200 / 200 passed all checks**
- Public redaction build: **passed**
- Public search rows: **23,941**
- Public source rows represented: **23,978**
- Public full service-number fields: **0**
- Runtime authenticated API calls: **0**
- Reviewed public sources: **36** records representing **35** unique documents
- Published, qualified affiliations: **57**
- Published claims: **84**
- GitHub Actions test workflow
  [30437365705](https://github.com/therealjameswilson/before-oss/actions/runs/30437365705)
  for research release `a8e2adb`: **passed**
- GitHub Pages deployment workflow
  [30437365696](https://github.com/therealjameswilson/before-oss/actions/runs/30437365696)
  for research release `a8e2adb`: **passed**
- Production route smoke tests: **12 / 12 returned HTTP 200**

GitHub emitted a non-blocking annotation that several official actions still
target Node.js 20 internally and were forced onto Node.js 24 by the runner. It
did not affect either workflow result.

The initial dependency range resolved to an older Astro major with current
security advisories. The project was upgraded to Astro 7.1.5 and sharp 0.35.3;
the production audit then passed.
