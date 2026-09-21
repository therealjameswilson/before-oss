import { expect, test } from "@playwright/test";

test("Reynold W Larson preserves both indexed box references on one reviewed entity", async ({ page }) => {
  await page.goto("./people/c9689f09-1e75-518b-bda3-77fb7592b506/");
  await expect(page.getByRole("heading", { name: "Reynold W Larson", level: 1 })).toBeVisible();
  await expect(page.locator("main")).toContainText("Box 433");
  await expect(page.locator("main")).toContainText("Box 434");
  await expect(page.locator("main")).toContainText("high confidence");
  await expect(page.locator("main")).toContainText(/duplicate-[a-f0-9]{12}/i);
});

test("Walter Kuznecoff and James Volosen remain separate conflict profiles", async ({ page }) => {
  const cases = [
    ["722b7664-7dc8-5876-ba62-bbf1e86c35e6", "Walter M Kuznecoff"],
    ["752029e7-cc27-5f1c-b486-30108e4126ee", "James Volosen"],
  ];
  for (const [id, name] of cases) {
    await page.goto(`./people/${id}/`);
    await expect(page.getByRole("heading", { name, level: 1 })).toBeVisible();
    await expect(page.locator("main")).toContainText("conflicting");
    await expect(page.locator("main")).toContainText(/private identifier/i);
    await expect(page.locator("main")).toContainText(/duplicate-[a-f0-9]{12}/i);
  }
});

test("Braho Kute name-order variants stay separate pending archival review", async ({ page }) => {
  const cases = [
    ["5ca01b4e-a215-5a0a-9f08-cd166c938c39", "Kute Braho"],
    ["b9525047-8e49-510f-a899-1238519988b7", "Braho Kute"],
  ];
  for (const [id, name] of cases) {
    await page.goto(`./people/${id}/`);
    await expect(page.getByRole("heading", { name, level: 1 })).toBeVisible();
    await expect(page.locator("main")).toContainText("ambiguous");
    await expect(page.locator("main")).toContainText(/name order/i);
    await expect(page.locator("main")).toContainText(/duplicate-[a-f0-9]{12}/i);
  }
});

test("Batch 619 keeps the oil-company evidence set unchanged", async ({ page }) => {
  await page.goto("./oil-companies/");
  await expect(page.locator(".oil-directory__person")).toHaveCount(7);
  await expect(page.locator(".oil-directory__list")).not.toContainText("Reynold W Larson");
});
