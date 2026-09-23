import { expect, test } from "@playwright/test";

test("Batch 644 publishes four high-confidence Army identity crosswalks without inventing employers", async ({
  page,
}) => {
  const profiles = [
    ["bac64720-9ef7-5214-a8cc-9c9ce36f5c0b", "Robert E McPeek"],
    ["aeb8dbfb-dd81-5af9-b2e6-e039657363bd", "James F McPoil"],
    ["f8ac2b72-b2e3-5e10-9987-0bf833536f26", "Robert C McQueen"],
    ["c8c087ec-782f-56cd-a71f-a8d7da152c27", "Donald S McVannel"],
  ];

  for (const [personId, displayName] of profiles) {
    await page.goto(`./people/${personId}/`);
    await expect(page.getByRole("heading", { name: displayName, level: 1 })).toBeVisible();
    await expect(page.locator("main")).toContainText("high confidence");
    await expect(page.locator("main")).toContainText("protected identifier");
    await expect(page.locator("main")).toContainText(
      "No publishable pre-OSS affiliation is recorded yet",
    );
  }
});

test("Batch 644 preserves the McParland-McPharland duplicate boundary", async ({ page }) => {
  const profiles = [
    ["baf6c6b1-c49b-5ffd-b858-514918dfce35", "Thomas E McParland"],
    ["5a7c2989-51bc-5df9-a02c-644959675d47", "Thomas E McPharland"],
  ];

  for (const [personId, displayName] of profiles) {
    await page.goto(`./people/${personId}/`);
    const main = page.locator("main");
    await expect(page.getByRole("heading", { name: displayName, level: 1 })).toBeVisible();
    await expect(main).toContainText("probable");
    await expect(main).toContainText("separate person entity");
    await expect(main).toContainText("Box 512");
    await expect(main).toContainText("No publishable pre-OSS affiliation is recorded yet");
  }
});

test("Batch 644 preserves both adjacent McQuiston rows pending jacket review", async ({ page }) => {
  const profiles = [
    ["79e0abb6-1bc6-5caa-b381-a51a3a54a4a8", "Joann W McQuiston"],
    ["1af9856d-8712-5210-b55b-c11c6b2d64b1", "Joanne W Mcquiston"],
  ];

  for (const [personId, displayName] of profiles) {
    await page.goto(`./people/${personId}/`);
    const main = page.locator("main");
    await expect(page.getByRole("heading", { name: displayName, level: 1 })).toBeVisible();
    await expect(main).toContainText("probable");
    await expect(main).toContainText("Box 513");
    await expect(main).toContainText("No publishable pre-OSS affiliation is recorded yet");
  }
});

test("Batch 644 leaves unsupported discovery leads unpublished", async ({ page }) => {
  const profiles: Array<[string, string]> = [
    ["a3a81cec-0d47-560c-a3a5-09595b868488", "John F McPadden"],
    ["a400ecf6-b26a-5c00-8020-64ef702e51d7", "Walter N McPherson"],
    ["c8b8cd04-de56-55ef-b93b-0f4e1dab4e38", "Donald G McRae"],
    ["ef9e2fbb-80d8-51e5-af75-3b794eae6752", "Helen M McTernan"],
  ];

  for (const [personId, displayName] of profiles) {
    await page.goto(`./people/${personId}/`);
    const main = page.locator("main");
    await expect(page.getByRole("heading", { name: displayName, level: 1 })).toBeVisible();
    await expect(main).toContainText("No publishable pre-OSS affiliation is recorded yet");
    await expect(main).not.toContainText("ProgressingAmerica");
  }
});

test("Batch 644 publishes the exact coverage checkpoint and retains the top oil category", async ({
  page,
}) => {
  await page.goto("./");
  await expect(page.locator("body")).toContainText("7,922");
  await expect(page.locator("body")).toContainText("33.09%");
  await expect(page.getByRole("heading", { name: "People who worked for oil companies" })).toBeVisible();

  await page.goto("./oil-companies/");
  await expect(page.locator(".oil-directory__person")).toHaveCount(7);
  await expect(page.locator(".page-hero .lede")).toContainText("9 historically named oil");
  await expect(page.locator(".oil-directory__list")).not.toContainText("McPeek");
  await expect(page.locator(".oil-directory__list")).not.toContainText("McVannel");
});
