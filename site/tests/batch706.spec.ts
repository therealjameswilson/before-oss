import { expect, test } from "@playwright/test";

const profiles = [
  ["346d2cfd-c598-5d92-b14d-a5a0219ef3d6", "George H Nishi"],
  ["232f1e33-4581-5756-97ea-030671a2b10c", "Hiroshi Nishi"],
  ["e592ccb7-693f-5064-abe0-81520b9d56f3", "Katsuma Nishimoto"],
  ["e427080c-5a81-5ae3-8fc4-47897c17f504", "Behe N Nishimura"],
  ["a4405081-e1d9-5268-93f5-bf3056277fb2", "Malcolm N Nishioa"],
  ["21207a08-810a-5ba4-8732-5744e545e95a", "Frederick H Nitta"],
  ["cca8b94e-52e2-5b72-81f9-0a7f98eff0de", "Donald H Niven"],
  ["30f0d3b9-0a7b-562d-8a95-8a0a864ead9a", "Charles Niver"],
  ["33188a07-7d76-573c-b817-9eb040d81832", "Blanche R Nixon"],
  ["73fa90ec-fa45-515c-b39b-492daef4558e", "Howard D Nixon"],
  ["0a1bd88a-fe63-5c0b-9900-cc1d080ed04d", "William B Nixon"],
  ["f4b60b11-2fa3-5f9f-a802-4e7f4d04926c", "George J Niznansky"],
  ["5b8c5e81-2dbd-51ab-9f17-ba7588fa3a34", "Michael F Noah"],
  ["667b467e-06b0-5e58-b285-e8339a9c61c0", "Frank Nobilo"],
  ["3dd086ba-5f76-5c2c-87b4-537b67c645ea", "Arthur G Noble"],
  ["49a5bf30-91f8-5ba9-996f-f10a17523cd6", "J S Noble"],
  ["7b9038c2-0765-5cb2-b61e-e80f7b51a27d", "Marshall H Noble"],
  ["6223cc27-b087-5d8a-aa7b-7a0cc76ecd40", "Robert D Noble"],
  ["62898427-3b28-5f99-bbcd-382b52939328", "Alessandro Nocella"],
  ["f8f28c90-19d7-586f-8979-069a494328ba", "Yincenzo L Nocella"],
  ["09744916-bc06-591f-9c8e-9b465aaddd5f", "Andre Noel"],
  ["4d62184f-baa3-5c18-b692-26cef7e4a41c", "Deane A Noel"],
  ["6bf61f2f-36bc-58ee-ba26-25e6ca4a1539", "James A Noel"],
] as const;

test("Batch 706 publishes all 23 direct profile routes with terminal outcomes", async ({ page }) => {
  for (const [id, name] of profiles) {
    await page.goto(`./people/${id}/`);
    await expect(page.getByRole("heading", { name, level: 1 })).toBeVisible();
    const main = page.locator("main");
    await expect(main).toContainText("Archive box");
    await expect(main).not.toContainText("not started");
    const serialValues = await main
      .locator("dt")
      .filter({ hasText: /^Serial$/ })
      .locator("xpath=following-sibling::dd[1]")
      .allTextContents();
    for (const value of serialValues) expect(value).not.toMatch(/^\d{6,8}$/);
  }
});

test("Batch 706 publishes Katsuma Nishimoto's qualified MIS pathway", async ({ page }) => {
  await page.goto("./people/e592ccb7-693f-5064-abe0-81520b9d56f3/");
  const main = page.locator("main");
  await expect(main).toContainText("Identity statushigh confidence");
  await expect(main).toContainText("Military Intelligence Service Language School");
  await expect(main).toContainText("military assignment");
  await expect(main).toContainText("temporal relation uncertain");
  await expect(main).toContainText("No reliable pre-OSS employer has yet been identified");
});

test("Batch 706 confirms Marshall Noble without inventing a pre-OSS affiliation", async ({ page }) => {
  await page.goto("./people/7b9038c2-0765-5cb2-b61e-e80f7b51a27d/");
  const main = page.locator("main");
  await expect(main).toContainText("Identity statusconfirmed");
  await expect(main).toContainText("OSS Detachment 101");
  await expect(main).toContainText("No reliable pre-OSS employer has yet been identified");
  await expect(main).not.toContainText("Detachment 101 was his immediate pre-OSS affiliation");
});

test("Batch 706 publishes Andre Noel's qualified Free French pathway", async ({ page }) => {
  await page.goto("./people/09744916-bc06-591f-9c8e-9b465aaddd5f/");
  const main = page.locator("main");
  await expect(main).toContainText("Identity statushigh confidence");
  await expect(main).toContainText("foreign or allied military personnel");
  await expect(main).toContainText("André Noël");
  await expect(main).toContainText("André Ferrière");
  await expect(main).toContainText("Free French Forces");
  await expect(main).toContainText("probable immediate");
});

test("Batch 706 preserves both name conflicts", async ({ page }) => {
  await page.goto("./people/a4405081-e1d9-5268-93f5-bf3056277fb2/");
  await expect(page.locator("main")).toContainText("Malcolm M Nishida");
  await expect(page.locator("main")).toContainText("Identity statusconflicting");

  await page.goto("./people/f8f28c90-19d7-586f-8979-069a494328ba/");
  await expect(page.locator("main")).toContainText("Vincenzo L Nocella");
  await expect(page.locator("main")).toContainText("Identity statusconflicting");
});

test("Batch 706 updates exact coverage while preserving the oil-company directory", async ({ page }) => {
  await page.goto("./");
  const main = page.locator("main");
  await expect(main).toContainText("9,277");
  await expect(main).toContainText("38.75%");
  await expect(main).toContainText("320");
  await expect(main).toContainText("14,657");

  const oilCategory = page.locator("#oil-companies");
  await expect(oilCategory.locator(".oil-directory__person")).toHaveCount(9);
  await expect(oilCategory).toContainText("11 historically named oil companies");
});
