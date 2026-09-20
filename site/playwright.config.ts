import { defineConfig, devices } from "@playwright/test";

const testPort = Number(process.env.BEFORE_OSS_TEST_PORT ?? "4321");

export default defineConfig({
  testDir: "./tests",
  timeout: 45_000,
  fullyParallel: true,
  workers: 1,
  forbidOnly: Boolean(process.env.CI),
  retries: process.env.CI ? 1 : 0,
  reporter: [["list"], ["html", { open: "never" }]],
  use: {
    baseURL: `http://127.0.0.1:${testPort}/before-oss/`,
    headless: true,
    launchOptions: { args: ["--disable-gpu"] },
    trace: "retain-on-failure",
    screenshot: "only-on-failure",
  },
  projects: [
    { name: "desktop", use: { ...devices["Desktop Chrome"] } },
    {
      name: "phone",
      use: { ...devices["iPhone 13"], browserName: "chromium" },
    },
    {
      name: "tablet",
      use: { ...devices["iPad (gen 7)"], browserName: "chromium" },
    },
  ],
  webServer: {
    command: `python3 scripts/serve_static.py --port ${testPort}`,
    url: `http://127.0.0.1:${testPort}/before-oss/`,
    reuseExistingServer: !process.env.CI,
    timeout: 120_000,
  },
});
