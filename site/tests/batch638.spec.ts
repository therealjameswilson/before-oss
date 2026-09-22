import { expect, test } from "@playwright/test";

test("Batch 638 publishes qualified Army identities without inventing employers", async ({
  page,
}) => {
  const profiles = [
    ["a574c48c-ad3b-57a1-ae43-c985d9c94364", "Barry McGill"],
    ["4f730acf-788d-5f0f-b340-fae1209bf8ca", "William L McGill"],
    ["d6d56580-d0ae-5cc5-91bb-9e52e746ba4f", "William H McGill"],
    ["00711a15-d463-54d9-b64e-1774dcbb8b40", "Edward M McGinnis"],
    ["5e66c7f7-38aa-567d-99cd-9c9c826932b8", "Edward J McGlynn"],
    ["46f824d1-5a14-57ae-88d3-edcc9bb87e04", "Harlan McGonigal"],
    ["968ba99c-f60f-51d5-a7a0-f7e4dba3c44d", "John J McGourty"],
    ["770cf847-09bb-50f8-a57c-0e03d10e8a68", "William C McGovern"],
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

test("Batch 638 preserves suffix and fixed-width name variants", async ({ page }) => {
  await page.goto("./people/4f730acf-788d-5f0f-b340-fae1209bf8ca/");
  await expect(page.locator("main")).toContainText("William L McGill Jr.");

  await page.goto("./people/5e66c7f7-38aa-567d-99cd-9c9c826932b8/");
  await expect(page.locator("main")).toContainText("Edward J McGlynn Jr.");

  await page.goto("./people/46f824d1-5a14-57ae-88d3-edcc9bb87e04/");
  await expect(page.locator("main")).toContainText("Harl N McGonigal");
  await expect(page.locator("main")).toContainText("Box 506");
});

test("Batch 638 keeps the Leon McGinnis initial conflict qualified", async ({ page }) => {
  await page.goto("./people/f466bb16-1781-5ad5-b65f-d35f17033d3c/");
  await expect(page.getByRole("heading", { name: "Leon A McGinnis", level: 1 })).toBeVisible();
  await expect(page.locator("main")).toContainText("conflicting");
  await expect(page.locator("main")).toContainText("middle initial is D rather than A");
  await expect(page.locator("main")).toContainText(
    "No publishable pre-OSS affiliation is recorded yet",
  );
});

test("Batch 638 keeps both David K McGinnis rows separate and ambiguous", async ({ page }) => {
  const profiles = [
    ["19527627-c8ef-5beb-9c82-4eb2b082fed0", "Box 505"],
    ["4d925235-45a5-5159-a7a5-a62ecfa8f571", "Box 506"],
  ];

  for (const [personId, box] of profiles) {
    await page.goto(`./people/${personId}/`);
    await expect(page.getByRole("heading", { name: "David K McGinnis", level: 1 })).toBeVisible();
    await expect(page.locator("main")).toContainText("ambiguous");
    await expect(page.locator("main")).toContainText(box);
    await expect(page.locator("main")).toContainText(
      "No publishable pre-OSS affiliation is recorded yet",
    );
  }
});

test("rejected Batch 638 newspaper namesakes stay out of public profiles", async ({ page }) => {
  await page.goto("./people/f2ba7ece-afb3-59e6-8667-ba0d1d64a3cd/");
  await expect(page.locator("main")).not.toContainText("Senate sergeant at arms");

  await page.goto("./people/5e66c7f7-38aa-567d-99cd-9c9c826932b8/");
  await expect(page.locator("main")).not.toContainText("Beltsville");
  await expect(page.locator("main")).not.toContainText("ration book");

  await page.goto("./people/80e851c4-c1ae-5bd5-b591-9ec4c92a351a/");
  await expect(page.locator("main")).not.toContainText("Northwestern University");
  await expect(page.locator("main")).not.toContainText("professor of political science");
});

test("Batch 638 publishes the exact coverage checkpoint and retains the oil category", async ({
  page,
}) => {
  await page.goto("./");
  await expect(page.locator("body")).toContainText("7,786");
  await expect(page.locator("body")).toContainText("32.52%");

  await page.goto("./oil-companies/");
  await expect(page.locator(".oil-directory__person")).toHaveCount(7);
  await expect(page.locator(".oil-directory__list")).not.toContainText("McGill");
  await expect(page.locator(".oil-directory__list")).not.toContainText("McGovern");
});
