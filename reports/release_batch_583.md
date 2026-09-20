# Batch 583 local release candidate

Date: 2026-09-20 UTC. Branch: `codex/before-oss-batch-583-research`.
Deployment and live verification: pending.

- Source scope: NARA OSS index PDF page 117, rows 31–46, sixteen distinct
  cautious people, all Box 186.
- CIA checks: 16 completed; LoC checks: 16 completed. Eleven LoC OCR leads
  were context-reviewed through the official text-service API; ten rejected,
  one private plausible lead.
- Four official Army identity crosswalks accepted. One medium-confidence,
  qualified U.S. Army pre-OSS pathway published for Martin Dickson; zero
  new confirmed/high civilian employers.
- Importable source review: `research/army_review_decisions_2026-09-20_batch583.csv`,
  `research/loc_review_decisions_2026-09-20_batch583.csv`, and
  `research/evidence-page-117-dickerson-jr-through-diebod_batch-583_2026-09-20.json`.
- Python: 110/110 unit tests passed. Astro: 211 files checked with zero
  errors, warnings or hints; 24,647 static HTML pages built. Bounded
  Playwright release suite: 72/72 passed, including 27 axe checks across
  desktop, phone and tablet. Internal links: 24,647 pages checked, all
  resolved. Public full-identifier audit: zero unexpected matches across
  24,719 artifacts.
- Local public-data manifest: 67 assets / 96,257,044 bytes, SHA-256
  `627cbe5739353460d5be678585e846f3def345622e52ef550a50d0e4f110770d`.
- Current coverage: 23,978/23,978 linked source rows; 23,940 active people;
  5,600 with nonplanned attempts; 262 with confirmed/high published
  employers; 5,555 archival-review assessed; 18,340 `not_started`.

Do not call this live until the branch is reviewed and merged, the GitHub
Pages run succeeds, and the unauthenticated exact-live verifier matches the
merged commit and all sixteen direct profile URLs.
