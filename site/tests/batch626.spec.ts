import { expect, test } from "@playwright/test";

test("Army crosswalk improves John Mayher identity without inventing an employer", async ({
  page,
}) => {
  await page.goto("./people/b6ec052d-deda-5185-a93c-fc980c72c9cc/");
  await expect(page.getByRole("heading", { name: "John T Mayher", level: 1 })).toBeVisible();
  await expect(page.locator("main")).toContainText("high confidence");
  await expect(page.locator("main")).toContainText(/official Army bulk entry/i);
  await expect(page.locator("main")).toContainText(/occupation code.*not treated/i);
  await expect(page.locator("main")).toContainText(
    "No publishable pre-OSS affiliation is recorded yet",
  );
});

test("rejected William Mayhew newborn namesake remains unpublished", async ({ page }) => {
  await page.goto("./people/64514777-cbc8-53f9-a54e-e1cbe39eaf02/");
  await expect(page.getByRole("heading", { name: "William A Mayhew", level: 1 })).toBeVisible();
  await expect(page.locator("main")).toContainText("Research is in progress");
  await expect(page.locator("main")).not.toContainText("William James Mayhew");
  await expect(page.locator("main")).not.toContainText("Milford Chronicle");
  await expect(page.locator("main")).toContainText(
    "No publishable pre-OSS affiliation is recorded yet",
  );
});

test("rejected Thomas Mays probate namesake remains unpublished", async ({ page }) => {
  await page.goto("./people/8913704c-6a7b-5f5f-892b-f4a587484017/");
  await expect(page.getByRole("heading", { name: "Thomas J Mays", level: 1 })).toBeVisible();
  await expect(page.locator("main")).toContainText("Research is in progress");
  await expect(page.locator("main")).not.toContainText("Thomas G. Mays");
  await expect(page.locator("main")).not.toContainText("probate notice");
});

test("Batch 626 publishes the exact coverage checkpoint and retains the oil category", async ({
  page,
}) => {
  await page.goto("./");
  await expect(page.locator("body")).toContainText("7,511");
  await expect(page.locator("body")).toContainText("31.38%");

  await page.goto("./oil-companies/");
  await expect(page.locator(".oil-directory__person")).toHaveCount(7);
  await expect(page.locator(".oil-directory__list")).not.toContainText("John T Mayher");
});
