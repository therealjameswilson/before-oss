import { expect, test } from "@playwright/test";

test("Batch 647 publishes Leonard Meeker's civilian-government and military pathways separately", async ({
  page,
}) => {
  await page.goto("./people/a5ef50b1-f406-5e62-a829-2be84a182538/");
  const main = page.locator("main");

  await expect(page.getByRole("heading", { name: "Leonard C Meeker", level: 1 })).toBeVisible();
  await expect(main).toContainText("General Counsel's Office of the U.S. Department of the Treasury");
  await expect(main).toContainText("Office of the Solicitor General");
  await expect(main).toContainText("U.S. Army");
  await expect(main).toContainText("Last civilian employer");
  await expect(main).toContainText("Immediate pre-OSS affiliation");
  await expect(main).toContainText("Ocracoke Observer");
});

test("Batch 647 publishes Gaudens Megaro's Queens College and COI chronology", async ({ page }) => {
  await page.goto("./people/7f5823b9-e766-5a55-9e6e-05ec39b5ad1e/");
  const main = page.locator("main");

  await expect(page.getByRole("heading", { name: "Gaudens Megaro", level: 1 })).toBeVisible();
  await expect(main).toContainText("Queens College");
  await expect(main).toContainText("Coordinator of Information");
  await expect(main).toContainText("Professor of history");
  await expect(main).toContainText("explicit immediate");
  await expect(main).toContainText("The American Historical Review");
});

test("Batch 647 qualifies Lincoln Mei's probable identity without inventing an employer", async ({ page }) => {
  await page.goto("./people/aabc6afc-6a05-5342-b1c2-4ff5d7b48f55/");
  const main = page.locator("main");

  await expect(page.getByRole("heading", { name: "Lincoln Mei", level: 1 })).toBeVisible();
  await expect(main).toContainText("probable");
  await expect(main).toContainText("World War II Army veteran");
  await expect(main).toContainText("No publishable pre-OSS affiliation is recorded yet");
  await expect(main).toContainText("No reviewed claim currently meets the publication threshold");
  await expect(main).toContainText("United States Government Publishing Office");
});

test("Batch 647 keeps the Mehillos and Mehner Army-name conflicts visible", async ({ page }) => {
  for (const [personId, displayName, conflictingName] of [
    ["45dd460f-d1d6-5053-ae37-e7246f5bc02f", "William G Mehillos", "MEHILOS"],
    ["e7928084-3eb3-5b1c-998e-c2c6c2e6fd2c", "Eugene W Mehner", "MOHNER"],
  ]) {
    await page.goto(`./people/${personId}/`);
    const main = page.locator("main");
    await expect(page.getByRole("heading", { name: displayName, level: 1 })).toBeVisible();
    await expect(main).toContainText("conflicting");
    await expect(main).toContainText(conflictingName);
    await expect(main).toContainText("pending file review");
  }
});

test("Batch 647 publishes exact coverage while retaining the oil-company category", async ({ page }) => {
  await page.goto("./");
  await expect(page.locator("body")).toContainText("7,989");
  await expect(page.locator("body")).toContainText("33.37%");
  await expect(
    page.getByRole("heading", { name: "People who worked for oil companies" }),
  ).toBeVisible();

  await page.goto("./oil-companies/");
  await expect(page.locator(".oil-directory__person")).toHaveCount(7);
  await expect(page.locator(".oil-directory__list")).not.toContainText("Meeker");
  await expect(page.locator(".oil-directory__list")).not.toContainText("Megaro");
});
