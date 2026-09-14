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

console.log(
  `Running bounded release suite with ${latestBatchSpec}; ` +
    `${batchSpecs.length} historical batch specifications remain available through npm run test:e2e.`,
);

for (const suite of suites) {
  console.log(`\n=== ${suite.label} ===`);
  const result = spawnSync(
    npx,
    ["--no-install", "playwright", "test", ...suite.args],
    { stdio: "inherit" },
  );

  if (result.error) {
    console.error(result.error.message);
    process.exit(1);
  }

  if (result.status !== 0) {
    process.exit(result.status ?? 1);
  }
}

