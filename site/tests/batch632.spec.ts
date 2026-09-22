import { expect, test } from "@playwright/test";

test("Batch 632 publishes four qualified Army identity crosswalks without inventing employers", async ({
  page,
}) => {
  const profiles = [
    ["bfbff01f-9da6-51ce-84bf-b9a70d5a1e24", "John N McConnaughe"],
    ["125bfabb-acda-5899-90be-19611f290c1e", "Robert J McConnachie"],
    ["2dea82f8-ef50-5603-821f-1f03c5f3ea0b", "Wallack H McCord"],
    ["b5e20e5d-89ca-55d0-8e18-04dbb0146402", "William M McCormack"],
  ];

  for (const [personId, displayName] of profiles) {
    await page.goto(`./people/${personId}/`);
    await expect(page.getByRole("heading", { name: displayName, level: 1 })).toBeVisible();
    await expect(page.locator("main")).toContainText("high confidence");
    await expect(page.locator("main")).toContainText("nonshared protected identifier");
    await expect(page.locator("main")).toContainText("No publishable pre-OSS affiliation is recorded yet");
  }
});

test("Batch 632 keeps source spelling differences visible and qualified", async ({ page }) => {
  await page.goto("./people/bfbff01f-9da6-51ce-84bf-b9a70d5a1e24/");
  await expect(page.locator("main")).toContainText("John N McConnaughey");
  await expect(page.locator("main")).toContainText("adds a final y");

  await page.goto("./people/125bfabb-acda-5899-90be-19611f290c1e/");
  await expect(page.locator("main")).toContainText("omits the middle initial");

  await page.goto("./people/2dea82f8-ef50-5603-821f-1f03c5f3ea0b/");
  await expect(page.locator("main")).toContainText("Hallack H McCord");
  await expect(page.locator("main")).toContainText("Wallack/Hallack");

  await page.goto("./people/b5e20e5d-89ca-55d0-8e18-04dbb0146402/");
  await expect(page.locator("main")).toContainText("fixed-width MC CORMACK surname spacing");
});

test("rejected Batch 632 newspaper candidates stay out of public profiles", async ({ page }) => {
  await page.goto("./people/bc697771-2b32-5d6b-86ab-7688e9d55c4b/");
  await expect(page.getByRole("heading", { name: "George R McCone", level: 1 })).toBeVisible();
  await expect(page.locator("main")).not.toContainText("George Conkin");
  await expect(page.locator('a[href*="sn85042379"]')).toHaveCount(0);

  await page.goto("./people/6845608b-2e9f-5f12-95d0-81a068c3f28a/");
  await expect(page.getByRole("heading", { name: "John W McConnell", level: 1 })).toBeVisible();
  await expect(page.locator("main")).not.toContainText("mother, Hendersonville");
  await expect(page.locator('a[href*="sn78002169"]')).toHaveCount(0);

  await page.goto("./people/0d41e55c-f979-5993-b500-86ac19a851b8/");
  await expect(page.getByRole("heading", { name: "Charles H McCormick", level: 1 })).toBeVisible();
  await expect(page.locator("main")).not.toContainText("Charles T. McCormick");
  await expect(page.locator('a[href*="sn86089568"]')).toHaveCount(0);
});

test("Batch 632 publishes the exact coverage checkpoint and retains the oil category", async ({
  page,
}) => {
  await page.goto("./");
  await expect(page.locator("body")).toContainText("7,652");
  await expect(page.locator("body")).toContainText("31.96%");

  await page.goto("./oil-companies/");
  await expect(page.locator(".oil-directory__person")).toHaveCount(7);
  await expect(page.locator(".oil-directory__list")).not.toContainText("William M McCormack");
  await expect(page.locator(".oil-directory__list")).not.toContainText("Charles H McCormick");
});
