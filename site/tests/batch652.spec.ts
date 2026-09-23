import { expect, test } from "@playwright/test";

test("Batch 652 publishes Frank Mesle's separated and qualified chronology", async ({ page }) => {
  await page.goto("./people/2a2d9879-fa60-5902-8c2c-2edc8c6ab186/");
  const main = page.locator("main");

  await expect(page.getByRole("heading", { name: "Frank C Mesle", level: 1 })).toBeVisible();
  await expect(main).toContainText("high confidence");
  await expect(main).toContainText("Immediate pre-OSS affiliation");
  await expect(main).toContainText("United States Army Corps of Engineers");
  await expect(main).toContainText("probable immediate");
  await expect(main).toContainText("Last civilian employer before service");
  await expect(main).toContainText("Boy Scouts of America");
  await expect(main).toContainText("professional Boy Scout in Camden, N.J.");
  await expect(main).toContainText("Earlier pre-OSS affiliations");
  await expect(main).toContainText("University of Iowa");
  await expect(main).toContainText("student");
  await expect(main).toContainText("Carl Mesle Jr");
});

test("Batch 652 accepts Ray Merrick's Army identity without inventing an employer", async ({ page }) => {
  await page.goto("./people/dbe10c0a-3d2d-5393-bf15-ffd6bdc52570/");
  const main = page.locator("main");

  await expect(page.getByRole("heading", { name: "Ray D Merrick", level: 1 })).toBeVisible();
  await expect(main).toContainText("high confidence");
  await expect(main).toContainText("nonshared protected identifier");
  await expect(main).toContainText("Army codes do not establish a named predecessor employer");
  await expect(main).toContainText("No publishable pre-OSS affiliation is recorded yet");
});

test("Batch 652 exposes Lawrencee Merritt's exact-name conflict", async ({ page }) => {
  await page.goto("./people/388e7b6c-1236-50c8-8d69-eaddb51ec368/");
  const main = page.locator("main");

  await expect(page.getByRole("heading", { name: "Lawrencee N Merritt", level: 1 })).toBeVisible();
  await expect(main).toContainText("conflicting");
  await expect(main).toContainText("Noel L. Merritt");
  await expect(main).toContainText("Army record is not accepted as this person");
  await expect(main).toContainText("No publishable pre-OSS affiliation is recorded yet");
});

test("Batch 652 preserves the Charles Mersereau cluster without merging", async ({ page }) => {
  await page.goto("./people/ff55fb90-c2af-5dfc-984d-c93621164832/");
  const main = page.locator("main");

  await expect(page.getByRole("heading", { name: "Charles P Mersereau", level: 1 })).toBeVisible();
  await expect(main).toContainText("conflicting");
  await expect(main).toContainText("Meserau");
  await expect(main).toContainText("Meysereav");
  await expect(main).toContainText("no merge is made");
});

test("Batch 652 preserves the William Merritts spelling conflict", async ({ page }) => {
  await page.goto("./people/e9a37a58-d576-543c-90c0-77421678dadb/");
  const main = page.locator("main");

  await expect(page.getByRole("heading", { name: "William L Merritts", level: 1 })).toBeVisible();
  await expect(main).toContainText("conflicting");
  await expect(main).toContainText("Marritts");
  await expect(main).toContainText("Meritts");
  await expect(main).toContainText("Merritts");
  await expect(main).toContainText("no merge is made");
});

test("Batch 652 retains F Nevill Merritt's printed field order", async ({ page }) => {
  await page.goto("./people/71423825-bc76-55b7-b936-8c3404040b90/");
  const main = page.locator("main");

  await expect(page.getByRole("heading", { name: "F Nevill Merritt", level: 1 })).toBeVisible();
  await expect(main).toContainText("literally prints F in the first-name field");
  await expect(main).toContainText("no reliable identity or employer bridge");
  await expect(main).toContainText("No publishable pre-OSS affiliation is recorded yet");
});

test("Batch 652 publishes new coverage and keeps the oil-company category at the directory top", async ({ page }) => {
  await page.goto("./");
  await expect(page.locator("body")).toContainText("8,097");
  await expect(page.locator("body")).toContainText("33.82%");

  await page.goto("./people/");
  const heading = page.getByRole("heading", { name: "People who worked for oil companies" });
  await expect(heading).toBeVisible();
  const category = page.locator(".featured-directory-category");
  await expect(category.locator("li")).toHaveCount(7);
  await expect(category).toContainText("9 historically named oil, petroleum, refining, or exploration companies");
  const categoryPrecedesFilters = await category.evaluate((node) => {
    const filters = document.querySelector("#az-nav");
    return Boolean(filters && (node.compareDocumentPosition(filters) & Node.DOCUMENT_POSITION_FOLLOWING));
  });
  expect(categoryPrecedesFilters).toBe(true);

  await page.goto("./oil-companies/");
  await expect(page.locator(".oil-directory__person")).toHaveCount(7);
  await expect(page.locator(".oil-directory__list")).not.toContainText("Frank C Mesle");
});
