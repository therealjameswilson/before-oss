import { expect, test } from "@playwright/test";

test("William Holohan separates the SEC from an unresolved immediate pathway", async ({ page }) => {
  await page.goto("./people/d9962ab3-e93e-5613-9f03-7021a0f31b28/");
  await expect(page.getByRole("heading", { name: "William V Holohan", level: 1 })).toBeVisible();
  await expect(page.getByRole("link", { name: "Page 213" })).toBeVisible();

  const immediate = page.locator('section[aria-labelledby="immediate-affiliation"]');
  const civilian = page.locator('section[aria-labelledby="civilian-employer"]');
  await expect(immediate).toContainText("No reviewed claim currently meets the publication threshold");
  await expect(civilian).toContainText("U.S. Securities and Exchange Commission");
  await expect(civilian).toContainText("Attorney");
  await expect(civilian).toContainText("strongly date bounded");
  await expect(page.locator("#evidence")).toBeVisible();
  await expect(page.locator("main")).toContainText("Memorandum on the Holohan Case");
  await expect(page.locator("main")).toContainText("Eleventh Annual Report");
});

test("same-identifier Hoffarth and Hoffman variants remain separate with a safe group", async ({ page }) => {
  const cases = [
    ["b34e3644-3611-5c5e-b901-b54041b4505e", "Albert J Hoffarth"],
    ["754fd9e4-9a11-5991-8a71-9fba214d6c83", "Albert J Hoffman"],
  ];
  for (const [id, name] of cases) {
    await page.goto(`./people/${id}/`);
    await expect(page.getByRole("heading", { name, level: 1 })).toBeVisible();
    await expect(page.locator("main")).toContainText("Duplicate group");
    await expect(page.locator("main")).toContainText("same private identifier");
    await expect(page.locator("main")).not.toContainText(/serial-conflict|duplicate-[0-9]{4,}/i);
  }
});

test("the oil-company category stays above the directory controls and employee-only", async ({ page }) => {
  await page.goto("./people/?q=oil&sort=name_asc");
  const category = page.locator(".featured-directory-category");
  await expect(category.getByRole("heading", { name: "People who worked for oil companies" })).toBeVisible();
  await expect(category.locator("li")).toHaveCount(7);
  await expect(category).toContainText("7 people");
  await expect(category).not.toContainText("William V Holohan");
  const categoryTop = await category.evaluate((node) => node.getBoundingClientRect().top);
  const controlsTop = await page.locator("#directory-controls").evaluate((node) => node.getBoundingClientRect().top);
  expect(categoryTop).toBeLessThan(controlsTop);
});

test("the dedicated oil-company page lists only the seven supported workers", async ({ page }) => {
  await page.goto("./oil-companies/");
  await expect(page.getByRole("heading", { name: "People who worked for oil companies", level: 1 })).toBeVisible();
  await expect(page.locator(".oil-directory__person")).toHaveCount(7);
  await expect(page.locator(".oil-directory__list")).not.toContainText("William V Holohan");
});
