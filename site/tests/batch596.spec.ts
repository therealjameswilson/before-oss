import { expect, test } from "@playwright/test";

test("oil-company category stays near the top and lists only cited employees", async ({ page }) => {
  await page.goto("./");
  const category = page.locator("#oil-companies");
  await expect(category.getByRole("heading", { name: "People who worked for oil companies" })).toBeVisible();
  await expect(category.locator(".oil-directory__person")).toHaveCount(6);
  await expect(category.getByRole("link", { name: "John Dixon", exact: true })).toHaveCount(0);
  await category.getByRole("link", { name: "Open this category" }).click();
  await expect(page).toHaveURL(/\/oil-companies\/$/);
  await expect(page.locator(".oil-directory__person")).toHaveCount(6);
  await expect(page.getByRole("link", { name: "Review claim-level evidence" })).toHaveCount(6);
});

test("page 124 Dozer separates civilian employer from earlier government assignment", async ({ page }) => {
  await page.goto("./people/b94564fb-2bf0-50bb-96cb-f50e9cc24ea2/");
  await expect(page.getByRole("heading", { name: "Donald M Dozer", level: 1 })).toBeVisible();
  await expect(page.getByRole("link", { name: "Page 124" })).toBeVisible();
  await expect(page.locator('section[aria-labelledby="civilian-employer"]'))
    .toContainText("University of Maryland");
  await expect(page.locator('section[aria-labelledby="immediate-affiliation"] .affiliation-card'))
    .toHaveCount(0);
  await expect(page.locator('section[aria-labelledby="earlier-affiliations"]'))
    .toContainText("Department of State");
  await expect(page.locator('section[aria-labelledby="evidence"]'))
    .toContainText("Maryland Historical Magazine");
});

test("Army crosswalk conflicts receive a distinct evidence section without employers", async ({ page }) => {
  for (const id of [
    "ef3ad527-d48f-5838-ac6e-cf32ce5da7f9",
    "89bfc672-e952-52b8-bcf2-b9ba5bf2068e",
  ]) {
    await page.goto(`./people/${id}/`);
    await expect(page.getByRole("heading", { name: "Evidence conflicts" })).toBeVisible();
    await expect(page.locator('section[aria-labelledby="evidence-conflicts"]'))
      .toContainText("identity");
    await expect(page.locator('section[aria-labelledby="civilian-employer"] .affiliation-card'))
      .toHaveCount(0);
  }
});

test("the two printed Millard Downey rows remain separate profiles", async ({ page }) => {
  for (const id of [
    "543a956a-fd8a-5c89-aefe-78ff368bc38a",
    "771a4b4f-ec22-586b-9e3d-799dedf7ab7b",
  ]) {
    await page.goto(`./people/${id}/`);
    await expect(page.getByRole("heading", { name: "Millard P Downey", level: 1 })).toBeVisible();
    await expect(page.getByRole("link", { name: "Page 124" })).toBeVisible();
  }
});

test("Dragnich remains an identity lead, not an asserted employer", async ({ page }) => {
  await page.goto("./people/7c16eead-094c-52bc-9789-356f0d300f4d/");
  await expect(page.getByRole("heading", { name: "Alexis N Dragnich", level: 1 })).toBeVisible();
  await expect(page.getByText("needs identity review", { exact: true })).toBeVisible();
  await expect(page.locator('section[aria-labelledby="civilian-employer"] .affiliation-card'))
    .toHaveCount(0);
});
