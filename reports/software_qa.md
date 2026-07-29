# Software QA

Run: 2026-07-29 UTC

- Python unit tests: **27 / 27 passed**
- Astro type/content diagnostics: **0 errors, 0 warnings, 0 hints**
- Production dependency audit: **0 known vulnerabilities**
- Static production build: **23,957 pages**
- Internal link check: **23,957 HTML files passed**
- Browser and accessibility suite: **42 / 42 passed**
- Deterministic stratified profile audit: **200 / 200 passed all checks**
- Public redaction build: **passed**
- Public search rows: **23,941**
- Public source rows represented: **23,978**
- Public full service-number fields: **0**
- Runtime authenticated API calls: **0**
- Reviewed public sources: **4**
- Published, qualified affiliations: **9**
- Published claims: **12**
- GitHub Actions test workflow for this release: **pending deployment**
- GitHub Pages deployment workflow for this release: **pending deployment**
- Production route smoke tests: **pending deployment**

GitHub emitted a non-blocking annotation that several official actions still
target Node.js 20 internally and were forced onto Node.js 24 by the runner. It
did not affect either workflow result.

The initial dependency range resolved to an older Astro major with current
security advisories. The project was upgraded to Astro 7.1.5 and sharp 0.35.3;
the production audit then passed.
