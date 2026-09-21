import { expect, test } from "@playwright/test";

test("Army crosswalk improves Lawrence Mayer identity without inventing an employer", async ({
  page,
}) => {
  await page.goto("./people/5465f2ab-1a6b-58cb-ab63-30026508180c/");
  await expect(page.getByRole("heading", { name: "Lawrence J Mayer", level: 1 })).toBeVisible();
  await expect(page.locator("main")).toContainText("high confidence");
  await expect(page.locator("main")).toContainText(/official Army bulk entry/i);
  await expect(page.locator("main")).toContainText(/occupation code.*not treated/i);
  await expect(page.locator("main")).toContainText(
    "No publishable pre-OSS affiliation is recorded yet",
  );
});

test("rejected Harold Mayer discovery hits remain unpublished", async ({ page }) => {
  await page.goto("./people/1ffe31e5-43ec-5077-8e2e-88637014eaf9/");
  await expect(page.getByRole("heading", { name: "Harold M Mayer", level: 1 })).toBeVisible();
  await expect(page.locator("main")).toContainText("unresolved");
  await expect(page.locator("main")).toContainText("Research is in progress");
  await expect(page.locator("main")).not.toContainText("St. Paul recorder");
  await expect(page.locator("main")).toContainText(
    "No publishable pre-OSS affiliation is recorded yet",
  );
});

test("Batch 625 publishes the exact coverage checkpoint and retains the oil category", async ({
  page,
}) => {
  await page.goto("./");
  await expect(page.locator("body")).toContainText("7,488");
  await expect(page.locator("body")).toContainText("31.28%");

  await page.goto("./oil-companies/");
  await expect(page.locator(".oil-directory__person")).toHaveCount(7);
  await expect(page.locator(".oil-directory__list")).not.toContainText("Lawrence J Mayer");
});
