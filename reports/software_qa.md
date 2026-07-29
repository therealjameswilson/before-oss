# Software QA

Run: 2026-07-29 UTC

- Python unit tests: **27 / 27 passed**
- Astro type/content diagnostics: **0 errors, 0 warnings, 0 hints**
- Production dependency audit: **0 known vulnerabilities**
- Static production build: **23,982 pages**
- Internal link check: **23,982 HTML files passed**
- Browser and accessibility suite: **51 / 51 passed**
- Deterministic stratified profile audit: **200 / 200 passed all checks**
- Public redaction build: **passed**
- Public search rows: **23,941**
- Public source rows represented: **23,978**
- Public full service-number fields: **0**
- Runtime authenticated API calls: **0**
- Reviewed public sources: **23**
- Published, qualified affiliations: **40**
- Published claims: **59**
- GitHub Actions test workflow
  [30431906852](https://github.com/therealjameswilson/before-oss/actions/runs/30431906852)
  for research release `34bd889`: **passed**
- GitHub Pages deployment workflow
  [30431906457](https://github.com/therealjameswilson/before-oss/actions/runs/30431906457)
  for research release `34bd889`: **passed**
- Production route smoke tests: **7 / 7 returned HTTP 200**

GitHub emitted a non-blocking annotation that several official actions still
target Node.js 20 internally and were forced onto Node.js 24 by the runner. It
did not affect either workflow result.

The initial dependency range resolved to an older Astro major with current
security advisories. The project was upgraded to Astro 7.1.5 and sharp 0.35.3;
the production audit then passed.
