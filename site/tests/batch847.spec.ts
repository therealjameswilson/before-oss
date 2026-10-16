import { expect, test } from "@playwright/test";

const profiles = [
  ["fe7d32f6-0a70-5cf5-a57f-8515a9d9d945", "Bernadotte E Schmitt"],
  ["8b9f3289-e0e5-5f9e-920f-a2c31b73a219", "Charles R Schmitt"],
  ["2d53b1b7-c80f-576e-b752-1b20b8afb77b", "Dorothy H Schmitt"],
  ["51951073-47e4-5ae3-99d3-05d22a8be512", "Irving Schmitt"],
  ["d469a280-1e8e-59c0-bf34-8d3f673e91db", "Robert J Schmitz"],
  ["59f204f9-dfc8-5603-9048-34724092e637", "William R Schmitz"],
  ["ffa831da-d92c-5dbc-a6b2-4329fe47f553", "Alice M Schmutz"],
  ["07d68c4c-f757-5f8c-877e-456b26b4aa00", "Stefan A Schnabel"],
  ["ff6d84f8-b8e2-545a-991e-ea84ae44ee3b", "Herbert M Schnall"],
  ["c0a24d41-5100-50ee-8b1d-de521147b01f", "Solomon H Schnaps"],
  ["159386b0-05dc-5dfa-8dcc-413c9f7f1098", "Lyle M Schneeberger"],
  ["bcf44f3d-8bee-56ae-acb8-b30d16b542cf", "William G Schneeflock"],
  ["9be34020-93ea-50a9-9c3c-9d963640defa", "Alphonse J Schneider"],
  ["02c08794-1d16-512d-bd13-7df83f92db61", "Anthony G Schneider"],
  ["7b303448-1cc8-5133-b16b-8988c9bca651", "Franklin Q Schneider"],
  ["e1b83792-9caf-5434-b886-ffb580e675da", "George M Schneider"],
  ["97ca39ad-0b1c-5293-8f33-7656822190e1", "Harold J Schneider"],
  ["36d1a048-1581-5939-9bde-65fa729750b7", "Henry Schneider"],
  ["fdd94e72-1093-5f31-ba8e-169a479c9116", "Inez G Schneider"],
  ["217c0308-0a1e-5b0b-807e-e4e067a6e98a", "James Schneider"],
  ["84127360-8703-5f98-914a-8a52cad82d64", "Jerome C Schneider"],
  ["1576769f-9db8-5d98-ab5f-9854438ee0fc", "John E Schneider"],
  ["1f976482-5a5a-5550-9573-0bd9caab2204", "Joseph W Schneider"],
] as const;

test("Batch 847 publishes all 23 reviewed profiles with masked identifiers", async ({ page }) => {
  for (const [id, name] of profiles) {
    await page.goto(`./people/${id}/`);
    await expect(page.getByRole("heading", { name, level: 1 })).toBeVisible();
    const main = page.locator("main");
    await expect(main).toContainText("Archive box");
    await expect(main).not.toContainText("not started");
    const serials = await main.locator("dt").filter({ hasText: /^Serial$/ })
      .locator("xpath=following-sibling::dd[1]").allTextContents();
    for (const value of serials) expect(value).not.toMatch(/^[A-Z]?\s?\d{4,9}(?:RA)?$/);
  }
});

test("Bernadotte Schmitt keeps the immediate affiliation and last civilian employer explicit", async ({ page }) => {
  await page.goto("./people/fe7d32f6-0a70-5cf5-a57f-8515a9d9d945/");
  const main = page.locator("main");
  await expect(main).toContainText("Identity statushigh confidence");
  await expect(main).toContainText("Bernadotte Everly Schmitt");
  await expect(main).toContainText("University of Chicago");
  await expect(main).toContainText("Immediate pre-OSS affiliation");
  await expect(main).toContainText("Last civilian employer before service");
  await expect(main).toContainText("Professor of Modern European History");
  await expect(main).toContainText("1924–1946");
  await expect(main).toContainText("strongly date bounded");
  await expect(main).toContainText("recruitment from it is not asserted");
});

test("Robert Schmitz publishes an explicit military pathway without inventing a civilian employer", async ({ page }) => {
  await page.goto("./people/d469a280-1e8e-59c0-bf34-8d3f673e91db/");
  const main = page.locator("main");
  await expect(main).toContainText("Identity statusconfirmed");
  await expect(main).toContainText("U.S. Army Infantry School");
  await expect(main).toContainText("Officer candidate; commissioned second lieutenant");
  await expect(main).toContainText("explicit immediate");
  await expect(main).toContainText("OSS assignment to June 23, 1943");
  await expect(main).toContainText("No reliable pre-OSS employer has yet been identified");
});

test("Stefan Schnabel publishes the Mercury Theatre as an earlier professional affiliation", async ({ page }) => {
  await page.goto("./people/07d68c4c-f757-5f8c-877e-456b26b4aa00/");
  const main = page.locator("main");
  await expect(main).toContainText("Identity statushigh confidence");
  await expect(main).toContainText("Mercury Theatre");
  await expect(main).toContainText("Metellus Cimber in Julius Caesar");
  await expect(main).toContainText("professional affiliation");
  await expect(main).toContainText("documented pre-OSS");
  await expect(main).toContainText("does not establish that Mercury Theatre was his immediate pre-OSS employer");
  await expect(main).toContainText("No reliable pre-OSS employer has yet been identified");
});

test("William Schneeflock remains qualified pending a direct identity bridge", async ({ page }) => {
  await page.goto("./people/bcf44f3d-8bee-56ae-acb8-b30d16b542cf/");
  const main = page.locator("main");
  await expect(main).toContainText("Identity statusprobable");
  await expect(main).toContainText("United States Army Air Corps");
  await expect(main).toContainText("Mechanic recruit");
  await expect(main).toContainText("direct personnel-file confirmation is still required");
  await expect(main).toContainText("documented pre-OSS");
  await expect(main).toContainText("announcement date");
  await expect(main).toContainText("No reliable pre-OSS employer has yet been identified");
});

test("Army crosswalks publish only identity evidence and preserve the Joseph Schneider suffix", async ({ page }) => {
  await page.goto("./people/1f976482-5a5a-5550-9573-0bd9caab2204/");
  let main = page.locator("main");
  await expect(main).toContainText("Identity statushigh confidence");
  await expect(main).toContainText("Joseph W Schneider Jr");
  await expect(main).toContainText("Army row adds the suffix Jr");
  await expect(main).not.toContainText("civilian occupation code");

  await page.goto("./people/1576769f-9db8-5d98-ab5f-9854438ee0fc/");
  main = page.locator("main");
  await expect(main).toContainText("Identity statushigh confidence");
  await expect(main).toContainText("enlisted army personnel");
  await expect(main).toContainText("No reliable pre-OSS employer has yet been identified");
  await expect(main).not.toContainText("civilian occupation code");
});

test("Henry Schneider keeps the plausible Columbia namesake rejected", async ({ page }) => {
  await page.goto("./people/36d1a048-1581-5939-9bde-65fa729750b7/");
  const main = page.locator("main");
  await expect(main).toContainText("Identity statusunresolved");
  await expect(main).toContainText("requires archival review");
  await expect(main).toContainText("rejected Columbia candidate");
  await expect(main).not.toContainText("Moses & Singer");
  await expect(main).toContainText("No reliable pre-OSS employer has yet been identified");
});
