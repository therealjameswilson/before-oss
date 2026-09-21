import { expect, test } from "@playwright/test";

test("Charles Hitch separates civilian, government, and military pathways", async ({ page }) => {
  await page.goto("./people/077388e6-27b2-502b-b1c1-8509e3bcbb03/");
  await expect(page.getByRole("heading", { name: "Charles J Hitch", level: 1 })).toBeVisible();
  await expect(page.getByRole("link", { name: "Page 209" })).toBeVisible();

  const immediate = page.locator('section[aria-labelledby="immediate-affiliation"]');
  const civilian = page.locator('section[aria-labelledby="civilian-employer"]');
  await expect(immediate).toContainText("United States Army");
  await expect(immediate).toContainText("explicit immediate");
  await expect(civilian).toContainText("University of Oxford");
  await expect(civilian).toContainText("strongly date bounded");
  await expect(page.locator("main")).toContainText("U.S. War Production Board");
  await expect(page.locator("main")).toContainText("commissioned army officer");
});

test("same-identifier Hoshide variants remain separate with safe duplicate labels", async ({ page }) => {
  const cases = [
    ["a8085c7a-7238-53e9-b86a-418542206445", "Hideo Hoshide"],
    ["562ce43a-5894-5fce-816c-857a19ab5677", "Hoshicle Hideo"],
  ];
  for (const [id, name] of cases) {
    await page.goto(`./people/${id}/`);
    await expect(page.getByRole("heading", { name, level: 1 })).toBeVisible();
    await expect(page.locator("main")).toContainText("Duplicate group");
    await expect(page.locator("main")).toContainText(/same private identifier|repeats the private identifier/);
    await expect(page.locator("main")).not.toContainText(/duplicate-[0-9]{4,}/i);
  }
});

test("same-identifier Hipp and Pipp rows remain distinct", async ({ page }) => {
  const cases = [
    ["2e3cadf2-69e6-5b13-a2ea-e88df3ee1f7b", "Paul P Hipp"],
    ["225d66bc-a7e6-590e-8739-7ec97bb8f3e9", "Paul P Pipp"],
  ];
  for (const [id, name] of cases) {
    await page.goto(`./people/${id}/`);
    await expect(page.getByRole("heading", { name, level: 1 })).toBeVisible();
    await expect(page.locator("main")).toContainText("Duplicate group");
    await expect(page.locator("main")).toContainText(/same private identifier|repeats the private identifier/);
  }
});

test("the oil-company category remains evidence-scoped after batch 613", async ({ page }) => {
  await page.goto("./oil-companies/");
  await expect(page.locator(".oil-directory__person")).toHaveCount(7);
  await expect(page.locator(".oil-directory__list")).not.toContainText("Charles J Hitch");
});
