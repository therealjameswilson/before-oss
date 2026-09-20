import { expect, test } from "@playwright/test";

test("Dorchain's later federation evidence does not become a pre-OSS employer", async ({ page }) => {
  await page.goto("./people/383199ed-8106-5810-9cf4-400cb086d1f5/");
  await expect(page.getByRole("heading", { name: "Willy Dorchain", level: 1 })).toBeVisible();
  await expect(page.getByRole("link", { name: "Page 122" })).toBeVisible();
  await expect(page.locator(".identity-note")).toContainText("not Dorchain");
  await expect(page.locator('section[aria-labelledby="immediate-affiliation"] .affiliation-card')).toHaveCount(0);
  await expect(page.locator('section[aria-labelledby="civilian-employer"] .affiliation-card')).toHaveCount(0);
  await expect(page.locator('section[aria-labelledby="earlier-affiliations"] .affiliation-card')).toHaveCount(0);
});

test("Doster's inaccessible Colt lead is not published as employment", async ({ page }) => {
  await page.goto("./people/2e457382-a60c-53ad-9b44-9b79afe11351/");
  await expect(page.getByRole("heading", { name: "Alexis Doster Jr.", level: 1 })).toBeVisible();
  await expect(page.getByRole("link", { name: "Page 122" })).toBeVisible();
  await expect(page.locator(".identity-note")).toContainText("could not be accessed");
  await expect(page.locator('section[aria-labelledby="immediate-affiliation"] .affiliation-card')).toHaveCount(0);
  await expect(page.locator('section[aria-labelledby="civilian-employer"] .affiliation-card')).toHaveCount(0);
  await expect(page.locator('section[aria-labelledby="earlier-affiliations"] .affiliation-card')).toHaveCount(0);
});

test("James E and James R Donovan remain different direct profiles", async ({ page }) => {
  await page.goto("./people/66c87b4b-42a1-5477-bdbe-534a84a440da/");
  await expect(page.getByRole("heading", { name: "James E Donovan", level: 1 })).toBeVisible();
  await expect(page.getByRole("link", { name: "Page 122" })).toBeVisible();

  await page.goto("./people/5621d0d6-08f1-514b-8d50-80ae9dc95f23/");
  await expect(page.getByRole("heading", { name: "James R Donovan", level: 1 })).toBeVisible();
  await expect(page.getByRole("link", { name: "Page 122" })).toBeVisible();
});
