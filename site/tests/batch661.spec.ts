import { expect, test } from "@playwright/test";

const profiles = [
  ["5950828b-cf00-5a1a-9573-d32e4df4e1d2", "John B Miller"],
  ["75b176b4-98bb-5d67-b5ba-bc05ee5abcf5", "Joseph B Miller"],
  ["e25aae44-fd9d-55c0-9749-2e006ed36bb3", "Joseph L Miller"],
  ["30eebc50-9cc7-5ce5-9313-be9b2b3188f3", "Joseph W Miller"],
  ["f731ce1a-b0ef-5b65-894a-0f4225855635", "Josephine M Miller"],
  ["f4925a0a-62a2-5727-a6ee-c5907c68e1f2", "Kenneth P Miller"],
  ["a2605cee-f966-5d20-9905-e13dc4b58b41", "Lane H Miller"],
  ["495f6e19-4b39-5008-940e-19959e9e177b", "Lawrence J Miller"],
  ["46fbaf43-ae97-5874-af4a-ed8d864e5c25", "Linwood R Miller"],
  ["b8dba2e0-6d03-57c6-a963-8c9734932433", "Lloyd L Miller"],
  ["c0f62edc-b807-539e-857f-b739b1599745", "Lou Miller"],
  ["37fa32f4-1551-5561-b3ef-124c5002287b", "Louis E Miller"],
  ["2931f17a-4354-5bf1-a907-e66e225e79cd", "Maxine E Miller"],
  ["22e6888f-21a5-5ffb-b244-9fbbfef74bd1", "Morris I Miller"],
  ["e4b55f43-920c-5b6e-8b20-12d99f060bf2", "Norman H Miller"],
  ["84defffc-a220-5d42-9443-e1b554c70c01", "Paul M Miller"],
  ["c974e4f4-d9ea-5e9f-bcef-8bb019cb9f1f", "Perry G.E. Miller"],
  ["e659c965-83a9-5ef2-a82f-5a8e9fd9dd9e", "Peter Miller"],
  ["84014b80-8022-55d3-948e-ed20d6fc12c6", "Raymond E Miller"],
  ["f87efbff-d8bc-5ed4-b140-2ac96968c167", "Reginald W Miller"],
  ["279d2635-0afb-5bf7-871d-99e2ce6e81fc", "Richard G Miller"],
  ["834ac0a5-32f1-5d8a-9f53-13c7369a3e3f", "Robert D Miller"],
] as const;

test("Batch 661 publishes all 22 direct profile routes", async ({ page }) => {
  for (const [id, name] of profiles) {
    await page.goto(`./people/${id}/`);
    await expect(page.getByRole("heading", { name, level: 1 })).toBeVisible();
  }
});

test("Batch 661 publishes identity-only Army evidence without inventing employment", async ({ page }) => {
  await page.goto("./people/46fbaf43-ae97-5874-af4a-ed8d864e5c25/");
  const main = page.locator("main");

  await expect(main).toContainText("high confidence");
  await expect(main).toContainText("protected identifier");
  await expect(main).toContainText("requires archival review");
  await expect(main).toContainText("Box 526");
  await expect(main).not.toContainText("Verified employer");
});

test("Batch 661 leaves the Raymond Miller fixed-width name conflict visible", async ({ page }) => {
  await page.goto("./people/84014b80-8022-55d3-948e-ed20d6fc12c6/");
  const main = page.locator("main");

  await expect(main).toContainText("conflicting");
  await expect(main).toContainText("MILLER RAY OND E");
  await expect(main).toContainText("Box 526");
  await expect(main).not.toContainText("Verified employer");
});

test("Batch 661 preserves the source index's possibly note", async ({ page }) => {
  await page.goto("./people/279d2635-0afb-5bf7-871d-99e2ce6e81fc/");
  const main = page.locator("main");

  await expect(main).toContainText("possibly");
  await expect(main).toContainText("high confidence");
  await expect(main).toContainText("requires archival review");
});

test("Batch 661 gives unresolved common names a dignified archival next action", async ({ page }) => {
  await page.goto("./people/75b176b4-98bb-5d67-b5ba-bc05ee5abcf5/");
  const main = page.locator("main");

  await expect(main).toContainText("unresolved");
  await expect(main).toContainText("requires archival review");
  await expect(main).toContainText("Box 525");
  await expect(main).not.toContainText("Verified employer");
});

test("Batch 661 preserves Perry Miller's reviewed Harvard chronology", async ({ page }) => {
  await page.goto("./people/c974e4f4-d9ea-5e9f-bcef-8bb019cb9f1f/");
  const main = page.locator("main");

  await expect(main).toContainText("Perry Gilbert Eddy Miller");
  await expect(main).toContainText("Harvard University");
  await expect(main).toContainText("Last civilian employer before service");
  await expect(main).toContainText("verified employer found");
});

test("Batch 661 updates exact coverage while preserving the oil-company category", async ({ page }) => {
  await page.goto("./");
  await expect(page.locator("body")).toContainText("8,293");
  await expect(page.locator("body")).toContainText("34.64%");

  await page.goto("./people/");
  const category = page.locator(".featured-directory-category");
  await expect(page.getByRole("heading", { name: "People who worked for oil companies" })).toBeVisible();
  await expect(category.locator("li")).toHaveCount(8);
  await expect(category).toContainText("10 historically named oil, petroleum, refining, or exploration companies");

  await page.goto("./oil-companies/");
  await expect(page.getByRole("region", { name: "Oil company work list" }).locator(".oil-directory__person")).toHaveCount(8);
});
