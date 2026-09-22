import { expect, test } from "@playwright/test";

test("rejected George McAdams namesake remains unpublished", async ({ page }) => {
  await page.goto("./people/31be0bec-6099-5431-856a-5b16f58b1ad4/");
  await expect(page.getByRole("heading", { name: "George F McAdams", level: 1 })).toBeVisible();
  await expect(page.locator("main")).toContainText("Research is in progress");
  await expect(page.locator("main")).not.toContainText("George A. McAdams");
  await expect(page.locator("main")).not.toContainText("Los Angeles Herald");
  await expect(page.locator("main")).toContainText(
    "No publishable pre-OSS affiliation is recorded yet",
  );
});

test("rejected George McBride namesakes remain unpublished", async ({ page }) => {
  await page.goto("./people/8e9688eb-016b-58f6-8f1a-17f3e0128de2/");
  await expect(page.getByRole("heading", { name: "George J McBride", level: 1 })).toBeVisible();
  await expect(page.locator("main")).toContainText("Research is in progress");
  await expect(page.locator("main")).not.toContainText("George Warren McBride");
  await expect(page.locator("main")).not.toContainText("Kinsley Graphic");
});

test("rejected John McBride initial conflicts remain unpublished", async ({ page }) => {
  await page.goto("./people/9e2b51bd-be4e-53c3-9566-cc85d833278f/");
  await expect(page.getByRole("heading", { name: "John J McBride", level: 1 })).toBeVisible();
  await expect(page.locator("main")).toContainText("Research is in progress");
  await expect(page.locator("main")).not.toContainText("John P. McBride");
  await expect(page.locator("main")).not.toContainText("John S. McBride");
  await expect(page.locator("main")).not.toContainText("John E. McBride");
});

test("Batch 627 publishes the exact coverage checkpoint and retains the oil category", async ({
  page,
}) => {
  await page.goto("./");
  await expect(page.locator("body")).toContainText("7,534");
  await expect(page.locator("body")).toContainText("31.47%");

  await page.goto("./oil-companies/");
  await expect(page.locator(".oil-directory__person")).toHaveCount(7);
  await expect(page.locator(".oil-directory__list")).not.toContainText("George F McAdams");
});
