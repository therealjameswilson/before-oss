import { expect, test } from "@playwright/test";

const profiles = [
  ["4516ad3a-ce4c-5299-b096-82619b3d7ee2", "Francis P Miller"],
  ["e99676d0-a722-5060-ab9c-39020a206e6e", "Fred L Miller"],
  ["e06e68ed-7fde-50f5-b455-53785b3c3396", "Garth H Miller"],
  ["5e5c5bbd-5ed0-5fad-a24a-af2a8d95158f", "George W Miller"],
  ["7762e200-2bca-50dc-91da-a90546882e8a", "Gerald E Miller"],
  ["f300bcec-4163-5786-b083-38e0f2b8a392", "Gloria N Miller"],
  ["abd2051f-0d23-5f36-adee-8aaa5d94640c", "Gordon L Miller"],
  ["cc602a29-1615-530f-b5ce-22cbe8472086", "Grace E Miller"],
  ["ee114d5c-a0a1-57bb-934f-f431ce58fb25", "Harold A Miller"],
  ["a16581b1-1c01-5778-8788-5572fc64b62a", "Harris Miller"],
  ["010496a9-8f74-5546-b33f-4e20ef892ad5", "Harry H Miller"],
  ["363bee5e-849c-5e8c-aaad-23bef7ee021d", "Hasbrouck B Miller"],
  ["e7342ff9-9772-5dc9-9950-f1c0b676ed68", "Helen R Miller"],
  ["514e77c1-53be-55ba-9992-3ec8386291c8", "Jacob H Miller"],
  ["ec20d34d-04bd-53c5-aabd-50c9a9baf459", "James E Miller"],
  ["c2da7542-fcd7-5f7b-9f52-35b78c0b47cd", "James G Miller"],
  ["82f8df50-7536-5592-b9a4-0e0ac2f071f9", "James C Miller"],
  ["00e309d8-23f2-58b8-866c-32f8d22a02aa", "Jean M Miller"],
  ["3d0065a5-d74f-50bb-a0bf-45d5f5003e5b", "Jessie R Miller"],
  ["0243898c-b4d9-536b-8ecb-986f526cc0f1", "Joan Miller"],
  ["dab85cb0-69ad-589d-b1c9-0745b2262322", "John G Miller"],
  ["ce7b7a1e-18e0-5f32-84d9-ca227dd8b20c", "John K Miller"],
] as const;

test("Batch 660 publishes all 22 direct profile routes", async ({ page }) => {
  for (const [id, name] of profiles) {
    await page.goto(`./people/${id}/`);
    await expect(page.getByRole("heading", { name, level: 1 })).toBeVisible();
  }
});

test("Batch 660 publishes Francis Pickens Miller's layered chronology", async ({ page }) => {
  await page.goto("./people/4516ad3a-ce4c-5299-b096-82619b3d7ee2/");
  const main = page.locator("main");

  await expect(main).toContainText("Francis Pickens Miller");
  await expect(main).toContainText("high confidence");
  await expect(main).toContainText("Immediate pre-OSS affiliation");
  await expect(main).toContainText("Last civilian employer before service");
  await expect(main).toContainText("Council on Foreign Relations");
  await expect(main).toContainText("Organization Director");
  await expect(main).toContainText("Virginia House of Delegates");
  await expect(main).toContainText("Yale Divinity School");
  await expect(main).toContainText("Foreign Policy Association");
  await expect(main).toContainText("strongly date bounded");
  await expect(main).toContainText("documented pre-OSS");
});

test("Batch 660 leaves the Garth Miller identity conflict visible", async ({ page }) => {
  await page.goto("./people/e06e68ed-7fde-50f5-b455-53785b3c3396/");
  const main = page.locator("main");

  await expect(main).toContainText("conflicting");
  await expect(main).toContainText("Andrew J. Shima");
  await expect(main).toContainText("Box 524");
  await expect(main).toContainText("before resolving the identity");
  await expect(main).not.toContainText("Verified employer");
});

test("Batch 660 preserves Cpt while classifying the row as commissioned", async ({ page }) => {
  await page.goto("./people/c2da7542-fcd7-5f7b-9f52-35b78c0b47cd/");
  const main = page.locator("main");

  await expect(main).toContainText("Cpt");
  await expect(main).toContainText("commissioned army officer");
  await expect(main).toContainText("requires archival review");
});

test("Batch 660 keeps identity-only Army evidence separate from employment", async ({ page }) => {
  await page.goto("./people/e99676d0-a722-5060-ab9c-39020a206e6e/");
  const main = page.locator("main");

  await expect(main).toContainText("high confidence");
  await expect(main).toContainText("protected identifier");
  await expect(main).toContainText("requires archival review");
  await expect(main).not.toContainText("Verified employer");
});

test("Batch 660 updates exact coverage while preserving the oil-company category", async ({ page }) => {
  await page.goto("./");
  await expect(page.locator("body")).toContainText("8,272");
  await expect(page.locator("body")).toContainText("34.55%");

  await page.goto("./people/");
  const category = page.locator(".featured-directory-category");
  await expect(page.getByRole("heading", { name: "People who worked for oil companies" })).toBeVisible();
  await expect(category.locator("li")).toHaveCount(8);
  await expect(category).toContainText("10 historically named oil, petroleum, refining, or exploration companies");

  await page.goto("./oil-companies/");
  await expect(page.getByRole("region", { name: "Oil company work list" }).locator(".oil-directory__person")).toHaveCount(8);
});
