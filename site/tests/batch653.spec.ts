import { expect, test } from "@playwright/test";

test("Batch 653 publishes Walter Mess's documented earlier self-employment", async ({ page }) => {
  await page.goto("./people/482ff7b7-4706-5f52-bd7e-908b790b1dcb/");
  const main = page.locator("main");

  await expect(page.getByRole("heading", { name: "Walter L Mess", level: 1 })).toBeVisible();
  await expect(main).toContainText("high confidence");
  await expect(main).toContainText("Earlier pre-OSS affiliations");
  await expect(main).toContainText("Self-employed");
  await expect(main).toContainText("Entrepreneur and property manager");
  await expect(main).toContainText("documented prewar");
  await expect(main).toContainText("AFC/2001/001/7955");
});

test("Batch 653 qualifies Prentice Messimer's J. Walter Thompson chronology", async ({ page }) => {
  await page.goto("./people/e4c7db1b-af21-591a-bf7c-4c9c6d871142/");
  const main = page.locator("main");

  await expect(page.getByRole("heading", { name: "Prentice Messimer", level: 1 })).toBeVisible();
  await expect(main).toContainText("high confidence");
  await expect(main).toContainText("Last civilian employer before service");
  await expect(main).toContainText("J. Walter Thompson Co.");
  await expect(main).toContainText("Copywriter");
  await expect(main).toContainText("probable immediate");
  await expect(main).toContainText("medium probable immediate");
  await expect(main).toContainText("Directory page 1023");
});

test("Batch 653 exposes Nicholas Metal's official-source identity conflict", async ({ page }) => {
  await page.goto("./people/7a376b00-390f-5889-931b-0ac917bfa691/");
  const main = page.locator("main");

  await expect(page.getByRole("heading", { name: "Nicholas Metal", level: 1 })).toBeVisible();
  await expect(main).toContainText("conflicting");
  await expect(main).toContainText("Field Base C");
  await expect(main).toContainText("Welbert Charles");
  await expect(main).toContainText("protected-identifier mismatch");
  await expect(main).toContainText("No publishable pre-OSS affiliation is recorded yet");
});

test("Batch 653 keeps the adjacent Leon Messenger rows separate", async ({ page }) => {
  for (const personId of [
    "58e3360e-1a64-5aa2-998f-9ff9493320fb",
    "ee3fcebc-aa82-529e-94e3-81186cb61751",
  ]) {
    await page.goto(`./people/${personId}/`);
    const main = page.locator("main");
    await expect(page.getByRole("heading", { name: "Leon C Messenger", level: 1 })).toBeVisible();
    await expect(main).toContainText("Duplicate group");
    await expect(main).toContainText("duplicate-ddb19d1c74d2");
    await expect(main).toContainText("requires archival review");
  }
});

test("Batch 653 publishes new coverage while retaining the oil-company category", async ({ page }) => {
  await page.goto("./");
  await expect(page.locator("body")).toContainText("8,118");
  await expect(page.locator("body")).toContainText("33.91%");

  await page.goto("./people/");
  const category = page.locator(".featured-directory-category");
  await expect(page.getByRole("heading", { name: "People who worked for oil companies" })).toBeVisible();
  await expect(category.locator("li")).toHaveCount(7);
  await expect(category).toContainText("9 historically named oil, petroleum, refining, or exploration companies");

  await page.goto("./oil-companies/");
  await expect(page.locator(".oil-directory__person")).toHaveCount(7);
  await expect(page.locator(".oil-directory__list")).not.toContainText("Walter L Mess");
  await expect(page.locator(".oil-directory__list")).not.toContainText("Prentice Messimer");
});
