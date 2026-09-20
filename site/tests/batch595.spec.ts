import { expect, test } from "@playwright/test";

test("George Doundoulakis has an Army pathway, not an invented civilian employer", async ({ page }) => {
  await page.goto("./people/a2b4dafa-878e-5de0-8f04-31a0ecea4933/");
  await expect(page.getByRole("heading", { name: "George J Doundoulakis", level: 1 })).toBeVisible();
  await expect(page.getByRole("link", { name: "Page 123" })).toBeVisible();
  await expect(page.locator('section[aria-labelledby="immediate-affiliation"]')
    .getByRole("link", { name: "United States Army" })).toBeVisible();
  await expect(page.locator('section[aria-labelledby="civilian-employer"] .affiliation-card')).toHaveCount(0);
  await expect(page.getByRole("link", { name: "Oral History: Doundoulakis, Helias" }).first()).toBeVisible();
});

test("Helias Doundoulakis is classified as enlisted and keeps civilian work unresolved", async ({ page }) => {
  await page.goto("./people/1a853afd-b422-501f-8834-6ad8e293ceac/");
  await expect(page.getByRole("heading", { name: "Helias J Doundoulakis", level: 1 })).toBeVisible();
  await expect(page.getByRole("link", { name: "Page 123" })).toBeVisible();
  await expect(page.locator('section[aria-labelledby="immediate-affiliation"]')
    .getByRole("link", { name: "United States Army" })).toBeVisible();
  await expect(page.locator('section[aria-labelledby="civilian-employer"] .affiliation-card')).toHaveCount(0);
  await expect(page.locator("main")).toContainText("enlisted army personnel");
});

test("Theodore d'Oultremont remains an archival lead without a pre-OSS employer", async ({ page }) => {
  await page.goto("./people/38cfc8c6-f3da-5fd6-b4b0-5558fa8b6805/");
  await expect(page.getByRole("heading", { name: "Theodore D'Oultremont", level: 1 })).toBeVisible();
  await expect(page.getByRole("link", { name: "Page 123" })).toBeVisible();
  await expect(page.locator(".identity-note")).toContainText("original dossier");
  await expect(page.locator('section[aria-labelledby="immediate-affiliation"] .affiliation-card')).toHaveCount(0);
  await expect(page.locator('section[aria-labelledby="civilian-employer"] .affiliation-card')).toHaveCount(0);
});

test("the two Jean Douglas index rows remain separate people", async ({ page }) => {
  await page.goto("./people/259a8b03-728f-52c4-94b8-48beb6822822/");
  await expect(page.getByRole("heading", { name: "Jean B Douglas", level: 1 })).toBeVisible();
  await page.goto("./people/1f15c63d-a650-5c91-be63-cb4811c74986/");
  await expect(page.getByRole("heading", { name: "Jean L Douglas", level: 1 })).toBeVisible();
});

test("previously cited Downes and Dow affiliations remain distinct", async ({ page }) => {
  await page.goto("./people/f443009b-dd5f-542b-9a0c-3af2d21f8611/");
  await expect(page.locator('section[aria-labelledby="immediate-affiliation"]')
    .getByRole("link", { name: "Free World Association" })).toBeVisible();
  await page.goto("./people/4626fb9d-f7ed-56b4-a7ec-492c76374b2b/");
  await expect(page.locator('section[aria-labelledby="immediate-affiliation"]')
    .getByRole("link", { name: "United States Army" })).toBeVisible();
  await expect(page.locator('section[aria-labelledby="immediate-affiliation"]'))
    .toContainText("Military Police");
});
