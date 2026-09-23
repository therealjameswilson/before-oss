import { expect, test } from "@playwright/test";

test("Batch 654 publishes Lothar Metzl's separated military and civilian chronology", async ({ page }) => {
  await page.goto("./people/f790320a-6d8f-556f-95a7-858fb1d1ee6c/");
  const main = page.locator("main");

  await expect(page.getByRole("heading", { name: "Lothar Metzl", level: 1 })).toBeVisible();
  await expect(main).toContainText("confirmed");
  await expect(main).toContainText("Immediate pre-OSS affiliation");
  await expect(main).toContainText("621st Quartermaster Depot Company");
  await expect(main).toContainText("May 1944");
  await expect(main).toContainText("Last civilian employer before service");
  await expect(main).toContainText("Self-employed");
  await expect(main).toContainText("Freelance playwright, satirist, and author");
  await expect(main).toContainText("freelance writing and radio work");
});

test("Batch 654 qualifies Lloyd Metzler's Harvard chronology", async ({ page }) => {
  await page.goto("./people/ac9f7c21-1ca0-5b18-9e9c-d3eca0ef5257/");
  const main = page.locator("main");

  await expect(page.getByRole("heading", { name: "Lloyd A Metzler", level: 1 })).toBeVisible();
  await expect(main).toContainText("high confidence");
  await expect(main).toContainText("Last civilian employer before service");
  await expect(main).toContainText("Harvard University");
  await expect(main).toContainText("Instructor and tutor");
  await expect(main).toContainText("medium");
  await expect(main).toContainText("multiple government assignments in 1943-1946");
});

test("Batch 654 treats Joshua Mewborn's Army record as identity evidence only", async ({ page }) => {
  await page.goto("./people/9d8ce8e4-3638-583f-9c65-3ab281474768/");
  const main = page.locator("main");

  await expect(page.getByRole("heading", { name: "Joshua M Mewborn", level: 1 })).toBeVisible();
  await expect(main).toContainText("high confidence");
  await expect(main).toContainText("502nd Parachute Infantry");
  await expect(main).toContainText("does not establish when he entered OSS");
  await expect(main).toContainText("No publishable pre-OSS affiliation is recorded yet");
});

test("Batch 654 exposes both protected-identifier conflicts", async ({ page }) => {
  for (const conflict of [
    {
      id: "16bd8c0d-3b2d-5656-90d0-f8774e2162ad",
      name: "Rafael P Mettuhen",
      evidence: "Rafael P. Miettunen",
    },
    {
      id: "daa07933-61a6-5c20-b38f-7fc083ae4eae",
      name: "Adalbert E Meyer",
      evidence: "Albert L. Meyer",
    },
  ]) {
    await page.goto(`./people/${conflict.id}/`);
    const main = page.locator("main");
    await expect(page.getByRole("heading", { name: conflict.name, level: 1 })).toBeVisible();
    await expect(main).toContainText("conflicting");
    await expect(main).toContainText(conflict.evidence);
    await expect(main).toContainText("No publishable pre-OSS affiliation is recorded yet");
  }
});

test("Batch 654 publishes new coverage and keeps the oil-company category at the directory top", async ({ page }) => {
  await page.goto("./");
  await expect(page.locator("body")).toContainText("8,140");
  await expect(page.locator("body")).toContainText("34.00%");

  await page.goto("./people/");
  const category = page.locator(".featured-directory-category");
  await expect(page.getByRole("heading", { name: "People who worked for oil companies" })).toBeVisible();
  await expect(category.locator("li")).toHaveCount(7);
  await expect(category).toContainText("9 historically named oil, petroleum, refining, or exploration companies");
  const categoryPrecedesFilters = await category.evaluate((node) => {
    const filters = document.querySelector("#az-nav");
    return Boolean(filters && (node.compareDocumentPosition(filters) & Node.DOCUMENT_POSITION_FOLLOWING));
  });
  expect(categoryPrecedesFilters).toBe(true);

  await page.goto("./oil-companies/");
  await expect(page.locator(".oil-directory__person")).toHaveCount(7);
  await expect(page.locator(".oil-directory__list")).not.toContainText("Lothar Metzl");
  await expect(page.locator(".oil-directory__list")).not.toContainText("Lloyd A Metzler");
});
