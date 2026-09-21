import { expect, test } from "@playwright/test";

test("Felix Keesing separates immediate Hawaii employment from earlier IPR work", async ({ page }) => {
  await page.goto("./people/207b22e8-a74e-58b1-9c8e-500660f2063c/");
  await expect(page.getByRole("heading", { name: "Felix M Keesing", level: 1 })).toBeVisible();
  await expect(page.getByRole("link", { name: "Page 244" })).toBeVisible();

  const immediate = page.locator('section[aria-labelledby="immediate-affiliation"]');
  const civilian = page.locator('section[aria-labelledby="civilian-employer"]');
  const earlier = page.locator('section[aria-labelledby="earlier-affiliations"]');
  await expect(immediate).toContainText("University of Hawaii");
  await expect(immediate).toContainText("Professor of Anthropology and Sociology");
  await expect(immediate).toContainText("high");
  await expect(civilian).toContainText("University of Hawaii");
  await expect(earlier).toContainText("Institute of Pacific Relations");
  await expect(earlier).toContainText("Director of research in the Pacific dependencies");
  const evidence = page.locator('section[aria-labelledby="evidence"]');
  await expect(evidence).toContainText("Felix M. Keesing Papers");
  await expect(evidence).toContainText("Manuscript A1999:003");
});

test("John F Kelley and Kelly remain separate without exposing their shared identifier", async ({ page }) => {
  const cases = [
    ["18e88baf-8ce3-5708-bbaf-cbb1c56f0dec", "John F Kelley"],
    ["2e5cacb3-f83e-539f-8e95-e68172b67187", "John F Kelly"],
  ];
  for (const [id, name] of cases) {
    await page.goto(`./people/${id}/`);
    await expect(page.getByRole("heading", { name, level: 1 })).toBeVisible();
    await expect(page.locator("main")).toContainText("Duplicate group");
    await expect(page.locator("main")).toContainText("same private identifier");
    await expect(page.locator("main")).not.toContainText(/serial-conflict/i);
    await expect(page.locator("main")).toContainText(/duplicate-[a-f0-9]{12}/i);
  }
});

test("the two Eugene Kingman rows remain separate pending Box 407 review", async ({ page }) => {
  const ids = [
    "b04939ae-1e2e-5ded-833e-3d7db85bbf85",
    "42c9ee77-befc-56ef-b56f-4a1bf42d5dd6",
  ];
  for (const id of ids) {
    await page.goto(`./people/${id}/`);
    await expect(page.getByRole("heading", { name: "Eugene Kingman", level: 1 })).toBeVisible();
    await expect(page.locator("main")).toContainText("Duplicate group");
    await expect(page.locator("main")).toContainText("Box 407");
    await expect(page.locator("main")).toContainText("also-AS note");
  }
});

test("the oil-company category remains the same seven-person evidence set", async ({ page }) => {
  await page.goto("./oil-companies/");
  await expect(page.locator(".oil-directory__person")).toHaveCount(7);
  await expect(page.locator(".oil-directory__list")).not.toContainText("Felix M Keesing");
});
