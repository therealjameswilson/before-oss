# Software QA

Run: 2026-07-29 UTC

- Python unit tests: **26 / 26 passed**
- Astro type/content diagnostics: **0 errors, 0 warnings, 0 hints**
- Production dependency audit: **0 known vulnerabilities**
- Static production build: **23,951 pages**
- Internal link check: **23,951 HTML files passed**
- Browser and accessibility suite: **39 / 39 passed**
- Deterministic stratified profile audit: **200 / 200 passed all checks**
- Public redaction build: **passed**
- Public search rows: **23,941**
- Public source rows represented: **23,978**
- Public full service-number fields: **0**
- Runtime authenticated API calls: **0**
- Reviewed public sources: **2**
- Published, qualified affiliations: **2**
- GitHub Actions and production deployment for this candidate release:
  **pending push**

The initial dependency range resolved to an older Astro major with current
security advisories. The project was upgraded to Astro 7.1.5 and sharp 0.35.3;
the production audit then passed.
