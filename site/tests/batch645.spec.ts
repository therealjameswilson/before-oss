import { expect, test } from "@playwright/test";

test("Batch 645 publishes Robert H McWilliams's separate ONI and Denver pathways", async ({
  page,
}) => {
  await page.goto("./people/05b64e26-6fd7-52b4-b44d-b55381b7ac15/");
  const main = page.locator("main");

  await expect(
    page.getByRole("heading", { name: "Robert H McWilliams", level: 1 }),
  ).toBeVisible();
  await expect(main).toContainText("Office of Naval Intelligence");
  await expect(main).toContainText("Special agent");
  await expect(main).toContainText("Denver District Attorney's Office");
  await expect(main).toContainText("Deputy district attorney");
  await expect(main).toContainText("strongly date bounded");
  await expect(main).toContainText("Federal Judicial Center");
  await expect(main).toContainText("Robert Hugh McWilliams Jr.");
});

test("Batch 645 publishes accepted Army identity crosswalks without inventing employers", async ({
  page,
}) => {
  const profiles = [
    ["a3b30365-2a1f-5f2e-8e9c-a7a1a2987551", "Francis C McVarish"],
    ["28c74028-bb9f-585e-8afa-521e14a920c3", "Charles F McVey"],
    ["71e6a694-3a2a-5b6f-a615-60a3630cc05f", "Chastain McWilliams"],
    ["636ecf8a-9eca-553f-9335-fba09f37be6a", "George G Mead"],
    ["2a1bf552-169d-50d3-a246-1a62df82fc29", "Gerard E Mead"],
  ];

  for (const [personId, displayName] of profiles) {
    await page.goto(`./people/${personId}/`);
    const main = page.locator("main");
    await expect(page.getByRole("heading", { name: displayName, level: 1 })).toBeVisible();
    await expect(main).toContainText("high confidence");
    await expect(main).toContainText("protected identifier");
    await expect(main).toContainText("No publishable pre-OSS affiliation is recorded yet");
  }
});

test("Batch 645 keeps the McVickerst Army-name conflict visible", async ({ page }) => {
  await page.goto("./people/51318818-d94a-5cd1-ab8d-5500883da0ea/");
  const main = page.locator("main");

  await expect(page.getByRole("heading", { name: "R McVickerst", level: 1 })).toBeVisible();
  await expect(main).toContainText("conflicting");
  await expect(main).toContainText("MC VICKER T R");
  await expect(main).toContainText("name fields require personnel-file review");
  await expect(main).toContainText("No publishable pre-OSS affiliation is recorded yet");
});

test("Batch 645 preserves both Mary P Meade rows pending jacket review", async ({ page }) => {
  const profiles = [
    "948cd939-1937-5ccb-b3e2-fd58bf08434b",
    "5745d57e-cc7f-57c1-9a11-3673f61baa9e",
  ];

  for (const personId of profiles) {
    await page.goto(`./people/${personId}/`);
    const main = page.locator("main");
    await expect(page.getByRole("heading", { name: "Mary P Meade", level: 1 })).toBeVisible();
    await expect(main).toContainText("probable");
    await expect(main).toContainText("separate person entity");
    await expect(main).toContainText("Box 514");
    await expect(main).toContainText("No publishable pre-OSS affiliation is recorded yet");
  }
});

test("Batch 645 publishes exact coverage while retaining the top oil-company category", async ({
  page,
}) => {
  await page.goto("./");
  await expect(page.locator("body")).toContainText("7,945");
  await expect(page.locator("body")).toContainText("33.19%");
  await expect(
    page.getByRole("heading", { name: "People who worked for oil companies" }),
  ).toBeVisible();

  await page.goto("./people/");
  const category = page.locator(".featured-directory-category");
  await expect(category).toBeVisible();
  await expect(category).toContainText("7 people");

  await page.goto("./oil-companies/");
  await expect(page.locator(".oil-directory__person")).toHaveCount(7);
  await expect(page.locator(".oil-directory__list")).not.toContainText("McWilliams");
});
