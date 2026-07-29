# Link check

Run: 2026-07-29 UTC

## Internal static routes

**PASS.** The production build contains 23,995 HTML files. Every relative
`href` and `src` target resolves under the GitHub Pages base path
`/before-oss/`.

The build includes 23,941 person profiles, 46 organization profiles, and the
home, directory, organizations, analysis, methodology, sources, downloads, and
404 pages.

The checker inventoried 47,962 unique external URLs for separate live
verification; external responses do not affect the internal-route pass.

## Representative external targets

| Target | Result |
|---|---|
| NARA OSS personnel records | HTTP 200 |
| NARA OSS records overview | HTTP 200 |
| National Archives Catalog | HTTP 200 |
| NARA Catalog API guidance | HTTP 200 |
| Official personnel index PDF | HTTP 200 |
| Library of Congress APIs | HTTP 200 |
| Chronicling America collection | HTTP 403 to the automated checker; accessible through the public web/API surface during research |
| CIA Reading Room OSS collection | Redirect loop in this environment; logged as a source-access blocker |
| GitHub correction URL | HTTP 200 after the expected GitHub sign-in redirect |

## Production deployment

GitHub Pages deployment
[30437365696](https://github.com/therealjameswilson/before-oss/actions/runs/30437365696)
for research release `a8e2adb` completed successfully.

Live checks returned HTTP 200 for all twelve tested targets:

- the home page and personnel directory;
- the reviewed Peter J Ortiz, Fisher Howe, Betty A Lussier, and Cordelia
  Dodson profiles;
- the United States Marine Corps, Coordinator of Information, Air Transport
  Auxiliary, and U.S. Military Intelligence organization profiles;
- `data/stats.json`; and
- the public personnel CSV download.

The four live profiles preserve military, government, civilian-employment, and
student distinctions, including the explicit role-title fallback for Betty A
Lussier's unnamed aircraft plant. The live statistics report 23,978 source
rows, 23,941 person entities, 95 people with non-planned research attempts, 19
verified-affiliation people, 21 archival-review assessments, 84 published
claims, and 36 public source records. The live CSV header contains
`serial_masked` and no full service-number field.

External link results are diagnostic and are not allowed to transform a source
access problem into a historical no-result conclusion.
