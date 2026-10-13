import { expect, test } from "@playwright/test";

const profiles = [
  ["6da494f3-274f-53c8-a4f2-f13bf9cd03bb", "Eleanor A Powell"],
  ["cf417249-e57b-57e6-a5b7-c5bbb40c7a85", "Ferdinand Powell"],
  ["b12ec55f-9cc4-53bb-bcf4-0a52190a6666", "Garland W Powell"],
  ["c2035ed9-07aa-59ca-80ca-d7916f819574", "James W Powell"],
  ["d116aa6d-7bea-5478-a1bc-50c2bb036340", "John Powell"],
  ["341a3649-153c-5e03-bcbf-eaba7881be53", "Louis G Powell"],
  ["59df410e-35ae-52c3-8fb4-b72e0766e609", "Orville S Powell"],
  ["62c3e9e8-ca76-5a4c-8c5c-e05c4cf7de82", "Robert G Powell"],
  ["089e85f3-3f1f-5c9a-ab51-ad7ff14aaedd", "Robert I Powell"],
  ["4b360625-1661-5dc2-9d3c-b192aa6c498a", "Roy E Powell"],
  ["d1dc6403-6ad5-5c82-9b51-65d2857d2707", "Sidney Powell"],
  ["57192468-d721-5fa3-92ab-708ad8ff1b98", "Thomas A Powell"],
  ["29590bbf-2864-566c-9e07-c0bcf47fc259", "Vernon B Powell"],
  ["ba151141-e4a8-556b-b4b1-973d6a044379", "Eugene B Power"],
  ["4c31e53f-0535-564d-8dc4-54008dd9dbfc", "John L Power"],
  ["6b796b1e-af8c-5d59-b9ce-f28172003f73", "Stuart E Power"],
  ["aee075fd-d9a5-58d1-8853-d471076b68aa", "George H Powers"],
  ["9282e0ee-bf95-538e-bd54-bab257440402", "John B Powers"],
  ["fd9ab033-2198-52ed-ad17-e8269829f348", "Justin J Powers"],
  ["4f92129e-6b1a-521f-96d8-959853c2a675", "Louis W Powers"],
  ["b47e57a0-7376-5ead-9811-614836cd8c4a", "Margaret Powers"],
  ["a5618bec-f20d-5f67-b789-2fac18bec0d4", "Richard W Powers"],
] as const;

test("Batch 771 publishes all 22 profiles with terminal attempted outcomes", async ({ page }) => {
  for (const [id, name] of profiles) {
    await page.goto("./people/" + id + "/");
    await expect(page.getByRole("heading", { name, level: 1 })).toBeVisible();
    const main = page.locator("main");
    await expect(main).toContainText("Archive box");
    await expect(main).not.toContainText("not started");
    const serialValues = await main
      .locator("dt")
      .filter({ hasText: /^Serial$/ })
      .locator("xpath=following-sibling::dd[1]")
      .allTextContents();
    for (const value of serialValues) expect(value).not.toMatch(/^[A-Z]?\s?\d{4,9}$/);
  }
});

test("Batch 771 publishes Eugene Power's qualified civilian chronology without calling it immediate", async ({ page }) => {
  await page.goto("./people/ba151141-e4a8-556b-b4b1-973d6a044379/");
  const main = page.locator("main");
  await expect(main).toContainText("Eugene Barnum Power");
  await expect(main).toContainText("University Microfilms");
  await expect(main).toContainText("founder");
  await expect(main).toContainText("Edwards Brothers");
  await expect(main).toContainText("vice president");
  await expect(main).toContainText("probable");
  await expect(main.locator("section[aria-labelledby='immediate-affiliation']")).toContainText("No reviewed claim currently meets the publication threshold");
});

test("Batch 771 exposes the John Powell identifier-name conflict without adopting Powelczak as an alias", async ({ page }) => {
  await page.goto("./people/d116aa6d-7bea-5478-a1bc-50c2bb036340/");
  const main = page.locator("main");
  await expect(main).toContainText("conflicting");
  await expect(main).toContainText("POWELCZAK JOHN");
  await expect(main).toContainText("surname conflict");
  await expect(main.locator("section[aria-labelledby='civilian-employer']")).toContainText("No reliable pre-OSS employer");
});

test("Batch 771 publishes Robert I Powell's rank-and-France identity evidence but no employer", async ({ page }) => {
  await page.goto("./people/089e85f3-3f1f-5c9a-ab51-ad7ff14aaedd/");
  const main = page.locator("main");
  await expect(main).toContainText("Lt. Col");
  await expect(main).toContainText("Robert I Powell, lieutenant colonel");
  await expect(main).toContainText("wartime France");
  await expect(main.locator("section[aria-labelledby='civilian-employer']")).toContainText("No reliable pre-OSS employer");
});

test("Batch 771 Army identity matches never turn coded occupations into employers", async ({ page }) => {
  for (const [id] of [profiles[2], profiles[5], profiles[9], profiles[10], profiles[18], profiles[21]]) {
    await page.goto("./people/" + id + "/");
    const main = page.locator("main");
    await expect(main).toContainText(/official Army|Official Army/);
    await expect(main).toContainText("enlisted army personnel");
    await expect(main.locator("section[aria-labelledby='civilian-employer']")).toContainText("No reliable pre-OSS employer");
  }
});

test("Batch 771 classifies indexed T/5 John L Power as enlisted without resolving a namesake", async ({ page }) => {
  await page.goto("./people/4c31e53f-0535-564d-8dc4-54008dd9dbfc/");
  const main = page.locator("main");
  await expect(main).toContainText("T/5");
  await expect(main).toContainText("enlisted army personnel");
  await expect(main).toContainText("naval officer inconsistent with the indexed Army T/5 rank");
});

test("home page exposes the rebuilt Batch 771 coverage totals", async ({ page }) => {
  await page.goto("./");
  const home = page.locator("main");
  await expect(home).toContainText("10,735");
  await expect(home).toContainText("44.84%");
  await expect(home).toContainText("13,199");
  await expect(home).toContainText("790");
  await expect(home).toContainText("351");
  await expect(home).toContainText("9,193");
});
