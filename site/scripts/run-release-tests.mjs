import { readdirSync } from "node:fs";
import { spawnSync } from "node:child_process";

const testDirectory = new URL("../tests/", import.meta.url);
const batchPattern = /^batch(\d+)\.spec\.ts$/;

const batchSpecs = readdirSync(testDirectory)
  .map((filename) => {
    const match = filename.match(batchPattern);
    return match ? { filename, batch: Number(match[1]) } : null;
  })
  .filter(Boolean)
  .sort((left, right) => right.batch - left.batch);

if (batchSpecs.length === 0) {
  console.error("No batchNNN.spec.ts release test was found.");
  process.exit(1);
}

const latestBatchSpec = `tests/${batchSpecs[0].filename}`;
const suites = [
  {
    label: `latest research batch (${latestBatchSpec})`,
    args: [latestBatchSpec],
  },
  {
    label: "bounded core routes and interactions",
    args: ["tests/site.spec.ts", "--grep-invert", "Batch"],
  },
  {
    label: "analysis routes and confidence-aware charts",
    args: ["tests/analysis.spec.ts"],
  },
  {
    label: "accessibility",
    args: ["tests/accessibility.spec.ts"],
  },
];

const npx = process.platform === "win32" ? "npx.cmd" : "npx";
const releaseBasePort = Number(
  process.env.BEFORE_OSS_RELEASE_TEST_PORT ?? "4421",
);

if (!Number.isInteger(releaseBasePort) || releaseBasePort < 1024 || releaseBasePort > 65531) {
  console.error(
    "BEFORE_OSS_RELEASE_TEST_PORT must be an integer from 1024 through 65531.",
  );
  process.exit(1);
}

console.log(
  `Running bounded release suite with ${latestBatchSpec}; ` +
    `${batchSpecs.length} historical batch specifications remain available through npm run test:e2e.`,
);

for (const [suiteIndex, suite] of suites.entries()) {
  console.log(`\n=== ${suite.label} ===`);
  const result = spawnSync(
    npx,
    ["--no-install", "playwright", "test", ...suite.args],
    {
      stdio: "inherit",
      env: {
        ...process.env,
        // A separate port prevents the next Playwright invocation from
        // reusing a static server that the preceding invocation is tearing
        // down. That race otherwise appears as mid-suite connection refusals.
        BEFORE_OSS_TEST_PORT: String(releaseBasePort + suiteIndex),
      },
    },
  );

  if (result.error) {
    console.error(result.error.message);
    process.exit(1);
  }

  if (result.status !== 0) {
    process.exit(result.status ?? 1);
  }
}
