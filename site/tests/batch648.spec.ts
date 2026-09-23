import { expect, test } from "@playwright/test";

test("Batch 648 publishes Ib Melchior's civilian and military pathways separately", async ({ page }) => {
  await page.goto("./people/09119446-f015-5b6e-b512-e2ad4104d5dc/");
  const main = page.locator("main");

  await expect(page.getByRole("heading", { name: "I J Melchior", level: 1 })).toBeVisible();
  await expect(main).toContainText("Ib Jørgen Melchior");
  await expect(main).toContainText("Radio City Music Hall");
  await expect(main).toContainText("Stage manager");
  await expect(main).toContainText("Last civilian employer");
  await expect(main).toContainText("Immediate pre-OSS affiliation");
  await expect(main).toContainText("United States Army");
  await expect(main).toContainText("Los Angeles Times");
});

test("Batch 648 publishes Leif Meland's merchant-sea and unit chronology", async ({ page }) => {
  await page.goto("./people/24a68ddd-d4f3-5d05-a9fb-7f3b382b52a9/");
  const main = page.locator("main");

  await expect(page.getByRole("heading", { name: "Leif E Meland", level: 1 })).toBeVisible();
  await expect(main).toContainText("D/S Cate B");
  await expect(main).toContainText("Fireman");
  await expect(main).toContainText("99th Infantry Battalion (Separate)");
  await expect(main).toContainText("Immediate pre-OSS affiliation");
  await expect(main).toContainText("Other documented work");
  await expect(main).toContainText("Earlier pre-OSS affiliations");
  await expect(main).toContainText("Norwegian War Sailor Register");
});

test("Batch 648 keeps John Meily's father-son identity conflict visible", async ({ page }) => {
  await page.goto("./people/08962f8b-b560-5ce7-a3fc-ed9817e8f99c/");
  const main = page.locator("main");

  await expect(page.getByRole("heading", { name: "John J Meily", level: 1 })).toBeVisible();
  await expect(main).toContainText("conflicting");
  await expect(main).toContainText("Foreign Service officer");
  await expect(main).toContainText("Marine officer son");
  await expect(main).toContainText("No publishable pre-OSS affiliation is recorded yet");
  await expect(main).toContainText("Box 516");
});

test("Batch 648 preserves both Michael Melkonian source rows and the Army spelling conflict", async ({ page }) => {
  await page.goto("./people/2c99f3a1-3b85-543b-b2e0-0cb69b197ded/");
  const main = page.locator("main");

  await expect(page.getByRole("heading", { name: "Michael Melkonian", level: 1 })).toBeVisible();
  await expect(main).toContainText("conflicting");
  await expect(main).toContainText("MILKONIAN MICHAEL");
  await expect(main).toContainText("Index row 1");
  await expect(main).toContainText("Index row 2");
  await expect(main).toContainText("duplicate-443ae3cbb0a4");
});

test("Batch 648 publishes exact coverage while retaining the oil-company category", async ({ page }) => {
  await page.goto("./");
  await expect(page.locator("body")).toContainText("8,010");
  await expect(page.locator("body")).toContainText("33.46%");
  await expect(
    page.getByRole("heading", { name: "People who worked for oil companies" }),
  ).toBeVisible();

  await page.goto("./oil-companies/");
  await expect(page.locator(".oil-directory__person")).toHaveCount(7);
  await expect(page.locator(".oil-directory__list")).not.toContainText("Melchior");
  await expect(page.locator(".oil-directory__list")).not.toContainText("Meland");
});
