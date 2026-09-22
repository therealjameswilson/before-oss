import { expect, test } from "@playwright/test";

test("Batch 636 publishes qualified Army identities without inventing employers", async ({
  page,
}) => {
  const profiles = [
    ["43e65fcd-5b93-58f7-b693-51f0f5541fcc", "Charles W McFadden"],
    ["bc76141a-950f-5e91-8578-a9b74be39d47", "Stuart P McFadden"],
  ];

  for (const [personId, displayName] of profiles) {
    await page.goto(`./people/${personId}/`);
    await expect(page.getByRole("heading", { name: displayName, level: 1 })).toBeVisible();
    await expect(page.locator("main")).toContainText("high confidence");
    await expect(page.locator("main")).toContainText("nonshared protected identifier");
    await expect(page.locator("main")).toContainText(
      "No publishable pre-OSS affiliation is recorded yet",
    );
  }

  await page.goto("./people/bc76141a-950f-5e91-8578-a9b74be39d47/");
  await expect(page.locator(".index-record")).toHaveCount(2);
});

test("Batch 636 exposes the McElroy identifier conflict without revealing the other identity", async ({
  page,
}) => {
  await page.goto("./people/7ab9338b-1ec0-5e60-88e6-d9d123907b4d/");
  await expect(page.getByRole("heading", { name: "Edward C McElroy", level: 1 })).toBeVisible();
  await expect(page.locator("main")).toContainText("conflicting");
  await expect(page.locator("main")).toContainText("withheld from public output");
  await expect(page.locator("main")).not.toContainText("Coopersmith");
});

test("Batch 636 retains duplicate McFadden source rows without inflating entities", async ({
  page,
}) => {
  await page.goto("./people/b2850942-a685-52d7-bb47-43a368d1b665/");
  await expect(page.getByRole("heading", { name: "Robert D McFadden", level: 1 })).toBeVisible();
  await expect(page.locator(".index-record")).toHaveCount(2);

  await page.goto("./people/bc76141a-950f-5e91-8578-a9b74be39d47/");
  await expect(page.locator(".index-record")).toHaveCount(2);
});

test("rejected Batch 636 newspaper namesakes stay out of public profiles", async ({ page }) => {
  await page.goto("./people/b4da83c6-ae04-5434-a232-cab6c3ddc305/");
  await expect(page.getByRole("heading", { name: "George H McFadden", level: 1 })).toBeVisible();
  await expect(page.locator("main")).not.toContainText("Elbows");
  await expect(page.locator("main")).not.toContainText("1893 deed");

  await page.goto("./people/a72babc9-ce39-532e-97ce-888a1f71768d/");
  await expect(page.getByRole("heading", { name: "William J McElroy", level: 1 })).toBeVisible();
  await expect(page.locator("main")).not.toContainText("William T. McElroy");
});

test("Batch 636 publishes the exact coverage checkpoint and retains the oil category", async ({
  page,
}) => {
  await page.goto("./");
  await expect(page.locator("body")).toContainText("7,742");
  await expect(page.locator("body")).toContainText("32.34%");

  await page.goto("./oil-companies/");
  await expect(page.locator(".oil-directory__person")).toHaveCount(7);
  await expect(page.locator(".oil-directory__list")).not.toContainText("Charles W McFadden");
  await expect(page.locator(".oil-directory__list")).not.toContainText("Stuart P McFadden");
});
