import { expect, test } from "@playwright/test";

test("William Eddy's COI, Marine, and civilian pathways remain distinct", async ({ page }) => {
  await page.goto("./people/495e4e73-3aa2-5afa-b5b3-838e28cc7957/");
  await expect(page.getByRole("heading", { name: "William A Eddy", level: 1 })).toBeVisible();
  await expect(page.locator('section[aria-labelledby="immediate-affiliation"]'))
    .toContainText("Coordinator of Information");
  await expect(page.locator('section[aria-labelledby="civilian-employer"]'))
    .toContainText("Hobart College");
  await expect(page.locator('section[aria-labelledby="earlier-affiliations"]'))
    .toContainText("United States Marine Corps");
  await expect(page.locator('section[aria-labelledby="evidence"]'))
    .toContainText("The Echo 1943");
  await expect(page.locator('section[aria-labelledby="evidence"]'))
    .toContainText("Herringbone Cloak");
});

test("same-name John A Dykes rows remain separate for Box 209 review", async ({ page }) => {
  const groups: string[] = [];
  for (const id of [
    "f77ee94b-fb8c-53bc-8ea6-3137e022d712",
    "e5f66339-afd2-5e75-9a5f-4438ea23a5f4",
  ]) {
    await page.goto(`./people/${id}/`);
    await expect(page.getByRole("heading", { name: "John A Dykes", level: 1 })).toBeVisible();
    const group = (await page.locator('dt:has-text("Duplicate group") + dd').textContent())?.trim();
    expect(group).toMatch(/^duplicate-[a-f0-9]{12}$/);
    groups.push(group ?? "");
    await expect(page.locator('section[aria-labelledby="civilian-employer"] .affiliation-card'))
      .toHaveCount(0);
  }
  expect(groups[0]).toBe(groups[1]);
});

test("featured oil-company category remains a dedicated list above directory filters", async ({ page }) => {
  await page.goto("./people/");
  await expect(page.getByRole("heading", { name: "People who worked for oil companies", level: 2 })).toBeVisible();
  await expect(page.locator(".featured-directory-category__list > li")).toHaveCount(7);
  await expect(page.locator(".featured-directory-category + .az-nav")).toHaveCount(1);
  await page.getByRole("link", { name: "See the full category and evidence status" }).click();
  await expect(page).toHaveURL(/\/oil-companies\/$/);
  await expect(page.getByRole("heading", { name: "People who worked for oil companies", level: 1 }))
    .toBeVisible();
});
