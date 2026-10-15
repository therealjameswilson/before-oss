import { expect, test } from "@playwright/test";

const profiles = [
  ["d91ee6c5-058d-5f9f-b173-20e1516132f6", "Elizabeth A Rodnick"],
  ["38868e4a-f8c1-524f-a614-48ecb7dae985", "Hellmuth P Rodrian"],
  ["ddab3fc0-6cff-5033-b462-bf8722eec6bc", "Joseph Rodrigo"],
  ["b7a8b35e-6c0f-59fb-bed5-f6ad5ed1fee1", "George R Rodrigues"],
  ["be31b153-b51a-5f61-9a71-371b30c1db9c", "Manuel Rodrigues"],
  ["2de2ab1c-24a2-5458-9aad-9818987df93c", "Pierre P Rodrigues"],
  ["411028ea-e6ef-5d8e-b5c2-574d65e8da21", "Alfonso Rodriguez"],
  ["5e452ee7-eaaf-515a-94b6-73f739bb1c96", "Edward F Rodriguez"],
  ["4a8e7c5c-a3a7-505d-8a4b-c17366366fb0", "Fernando O Rodriguez"],
  ["2374ded3-dad6-5d3b-8a66-2941f495bcd3", "Jose O Rodriguez"],
  ["c12c095e-33a6-5450-8e91-6ca9c9025125", "Harry Rody"],
  ["f05da3c3-77ff-5494-ad3c-8e646683ba46", "Henry F Rodziewicz"],
  ["6d1b5888-3f92-5a41-8ca8-31cf23bca103", "Richard A Roe"],
  ["58ab1c13-ee8b-5d1e-8e77-b4cfbf87c303", "Delmar M Roeder"],
  ["3ba72b86-3401-5a27-9abd-4cc2d8f8620e", "Jose A Roel"],
  ["b49eec0c-cac2-5aaf-9e61-f4f175b26fd4", "Helmuth H Roemer"],
  ["934e5040-c591-5395-91a0-112d12a11303", "William G Roessel"],
  ["11521299-26a4-5844-b639-48520b5d337f", "Charles E Roethe"],
  ["ac4fbe56-cf13-5348-8770-f6f0e54bb4c6", "Louis C Rofrano"],
  ["5b5681e8-1a9e-5870-99e5-58c3e6b16d8f", "Anita M Rogenmoser"],
  ["451900c5-04de-51c4-bd6d-9b1677a639af", "Albert S Rogers"],
  ["54dc2684-3e51-595f-a129-4ee3ec606090", "Alfred C Rogers"],
  ["a397d40c-375e-5d47-ac98-52216693de77", "Bruce Rogers"],
] as const;

test("Batch 815 publishes all 23 profiles with terminal outcomes and masked identifiers", async ({ page }) => {
  for (const [id, name] of profiles) {
    await page.goto("./people/" + id + "/");
    await expect(page.getByRole("heading", { name, level: 1 })).toBeVisible();
    const main = page.locator("main");
    await expect(main).toContainText("Archive box");
    await expect(main).not.toContainText("not started");
    const serials = await main
      .locator("dt")
      .filter({ hasText: /^Serial$/ })
      .locator("xpath=following-sibling::dd[1]")
      .allTextContents();
    for (const value of serials) expect(value).not.toMatch(/^[A-Z]?\s?\d{4,9}(?:RA)?$/);
  }
});

test("Joseph Rodrigo publishes the Farm Credit employer without claiming immediacy", async ({ page }) => {
  await page.goto("./people/ddab3fc0-6cff-5033-b462-bf8722eec6bc/");
  const main = page.locator("main");
  await expect(main).toContainText("Federal Intermediate Credit Bank of Berkeley");
  await expect(main).toContainText("Last civilian employer before service");
  await expect(main).toContainText("strongly date bounded");
  await expect(main).toContainText("The Farm Credit Club Grapevine");
  await expect(main).toContainText("formerly of the FICB of Berkeley");
  await expect(main).toContainText("Immediate pre-OSS affiliation");
  await expect(main).toContainText("No reviewed claim currently meets the publication threshold.");
});

test("Bruce Rogers keeps education and qualified consular service separate", async ({ page }) => {
  await page.goto("./people/a397d40c-375e-5d47-ac98-52216693de77/");
  const main = page.locator("main");
  await expect(main).toContainText("University of Oregon");
  await expect(main).toContainText("student");
  await expect(main).toContainText("United States Consulate in Osaka");
  await expect(main).toContainText("government assignment");
  await expect(main).toContainText("medium documented pre-OSS");
  await expect(main).toContainText("1939 Oregana");
  await expect(main).toContainText("The Closing of Manzanar");
  await expect(main).toContainText("Radio Warfare");
});

test("Delmar Roeder exposes the identifier conflict without merging the namesake", async ({ page }) => {
  await page.goto("./people/58ab1c13-ee8b-5d1e-8e77-b4cfbf87c303/");
  const main = page.locator("main");
  await expect(main).toContainText("conflicting");
  await expect(main).toContainText("CALARY WILLIAM R");
  await expect(main).toContainText("No merge is made");
});

test("accepted Army identities do not become inferred employers", async ({ page }) => {
  for (const id of [
    "be31b153-b51a-5f61-9a71-371b30c1db9c",
    "c12c095e-33a6-5450-8e91-6ca9c9025125",
    "934e5040-c591-5395-91a0-112d12a11303",
    "ac4fbe56-cf13-5348-8770-f6f0e54bb4c6",
    "451900c5-04de-51c4-bd6d-9b1677a639af",
  ]) {
    await page.goto("./people/" + id + "/");
    const main = page.locator("main");
    await expect(main).toContainText("confirmed");
    await expect(main).toContainText("official Army");
    await expect(main).toContainText("No reliable pre-OSS employer");
  }
});

test("space-separated staff sergeant and chief storekeeper ranks classify as enlisted", async ({ page }) => {
  await page.goto("./people/934e5040-c591-5395-91a0-112d12a11303/");
  await expect(page.locator("main")).toContainText("enlisted army personnel");

  await page.goto("./people/6d1b5888-3f92-5a41-8ca8-31cf23bca103/");
  await expect(page.locator("main")).toContainText("enlisted naval personnel");
});

test("home page exposes the rebuilt Batch 815 coverage totals", async ({ page }) => {
  await page.goto("./");
  const home = page.locator("main");
  await expect(home).toContainText("11,729");
  await expect(home).toContainText("49.00%");
  await expect(home).toContainText("12,204");
  await expect(home).toContainText("839");
  await expect(home).toContainText("377");
  await expect(home).toContainText("10,192");
});
