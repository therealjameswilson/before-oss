import { expect, test } from "@playwright/test";

test("Druckenmiller's immediate pathway is Army service, while his civilian employer remains unknown", async ({ page }) => {
  await page.goto("./people/2daf5cc6-9297-5d37-8f77-b5e2cc923489/");
  await expect(page.getByRole("heading", { name: "Martin L Druckenmiller", level: 1 })).toBeVisible();
  await expect(page.getByRole("link", { name: "Page 125" })).toBeVisible();
  await expect(page.locator('section[aria-labelledby="immediate-affiliation"]'))
    .toContainText("United States Army");
  await expect(page.locator('section[aria-labelledby="civilian-employer"] .affiliation-card'))
    .toHaveCount(0);
  await expect(page.locator("main")).toContainText("draftsman in civilian life");
  await expect(page.locator("main")).toContainText("enlisted army personnel");
});

test("Gamble's Packard job is earlier documented work, not his last civilian employer", async ({ page }) => {
  await page.goto("./people/d0f6247c-95a1-5b6b-934d-b3311bf60a23/");
  await expect(page.getByRole("heading", { name: "Robert Gamble", level: 1 })).toBeVisible();
  await expect(page.getByRole("link", { name: "Page 161" })).toBeVisible();
  await expect(page.locator('section[aria-labelledby="immediate-affiliation"]'))
    .toContainText("United States Army");
  await expect(page.locator('section[aria-labelledby="civilian-employer"] .affiliation-card'))
    .toHaveCount(0);
  await expect(page.locator('section[aria-labelledby="earlier-affiliations"]'))
    .toContainText("Packard Car Company");
  await expect(page.locator('section[aria-labelledby="evidence"]'))
    .toContainText("personnel interview board proceedings");
});

test("Koch's conflicting identifier remains an identity lead without an employer", async ({ page }) => {
  await page.goto("./people/8d08b1f5-caa0-54a7-baa4-a8da90fffe45/");
  await expect(page.getByRole("heading", { name: "Robert J Koch", level: 1 })).toBeVisible();
  await expect(page.getByText("needs identity review", { exact: true })).toBeVisible();
  await expect(page.locator('section[aria-labelledby="immediate-affiliation"] .affiliation-card'))
    .toHaveCount(0);
  await expect(page.locator('section[aria-labelledby="civilian-employer"] .affiliation-card'))
    .toHaveCount(0);
  await expect(page.locator('section[aria-labelledby="earlier-affiliations"] .affiliation-card'))
    .toHaveCount(0);
});

test("oil-company category remains limited to supported oil employers", async ({ page }) => {
  await page.goto("./oil-companies/");
  await expect(page.locator(".oil-directory__person")).toHaveCount(7);
  await expect(page.locator("main")).not.toContainText("Packard Car Company");
});
