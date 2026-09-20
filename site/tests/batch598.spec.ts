import { expect, test } from "@playwright/test";

test("Duke separates an Army intelligence transfer from his last civilian employer", async ({ page }) => {
  await page.goto("./people/c852d410-a4a4-596c-8781-6bd4bf4c65d6/");
  await expect(page.getByRole("heading", { name: "Florimond D Duke", level: 1 })).toBeVisible();
  await expect(page.getByRole("link", { name: "Page 126" })).toBeVisible();
  await expect(page.locator('section[aria-labelledby="immediate-affiliation"]'))
    .toContainText("Military Intelligence Service");
  await expect(page.locator('section[aria-labelledby="civilian-employer"]'))
    .toContainText("Time, Inc.");
  await expect(page.locator('section[aria-labelledby="earlier-affiliations"]'))
    .toContainText("Newsweek");
  await expect(page.locator('section[aria-labelledby="earlier-affiliations"]'))
    .toContainText("Fortune magazine");
  await expect(page.locator("main")).toContainText("middle initial");
});

test("Duke's claims expose wartime and institutional citations without making Time the OSS predecessor", async ({ page }) => {
  await page.goto("./people/c852d410-a4a4-596c-8781-6bd4bf4c65d6/");
  await expect(page.locator('section[aria-labelledby="evidence"]'))
    .toContainText("South Eastern European Section");
  await expect(page.locator('section[aria-labelledby="evidence"]'))
    .toContainText("Dartmouth Alumni Magazine");
  await expect(page.locator('section[aria-labelledby="immediate-affiliation"]'))
    .not.toContainText("Time, Inc.");
  await expect(page.locator('section[aria-labelledby="civilian-employer"]'))
    .not.toContainText("Military Intelligence Service");
});

test("the two Stevens Dukson rows remain distinct and the shared identifier is a conflict", async ({ page }) => {
  await page.goto("./people/75d84ad9-5c5e-530d-9230-03902d15754a/");
  await expect(page.getByRole("heading", { name: "Stevens Dukson", level: 1 })).toBeVisible();
  await expect(page.getByText("needs identity review", { exact: true })).toBeVisible();
  await expect(page.locator('section[aria-labelledby="civilian-employer"] .affiliation-card'))
    .toHaveCount(0);

  await page.goto("./people/b65b9095-2761-5015-939f-f2150da9c982/");
  await expect(page.getByRole("heading", { name: "Stevens Dukson", level: 1 })).toBeVisible();
  await expect(page.locator('section[aria-labelledby="evidence-conflicts"]'))
    .toContainText("identity");
  await expect(page.locator('section[aria-labelledby="civilian-employer"] .affiliation-card'))
    .toHaveCount(0);
});

test("duplicated Jeanne Duiker rows and different William Duff rows retain direct profiles", async ({ page }) => {
  for (const id of [
    "f72199c9-e871-5149-9f17-4b063f4d9d72",
    "50535c06-2a55-50d9-b501-ace55b4c3548",
  ]) {
    await page.goto(`./people/${id}/`);
    await expect(page.getByRole("heading", { name: "Jeanne S Duiker", level: 1 })).toBeVisible();
    await expect(page.getByRole("link", { name: "Page 126" })).toBeVisible();
  }
  for (const id of [
    "84de88f9-eaa1-5265-8868-17d4e2a6d7cc",
    "1ce0a08f-d741-5d33-89a7-04df957efb26",
  ]) {
    await page.goto(`./people/${id}/`);
    await expect(page.getByRole("heading", { name: "William Duff", level: 1 })).toBeVisible();
    await expect(page.getByRole("link", { name: "Page 126" })).toBeVisible();
  }
});

test("oil-company category at the top stays employee-only after the media claims", async ({ page }) => {
  await page.goto("./");
  const category = page.locator("#oil-companies");
  await expect(category.getByRole("heading", { name: "People who worked for oil companies" }))
    .toBeVisible();
  await expect(category.locator(".oil-directory__person")).toHaveCount(6);
  await expect(category).not.toContainText("Florimond D Duke");
  await category.getByRole("link", { name: "Open this category" }).click();
  await expect(page).toHaveURL(/\/oil-companies\/$/);
  await expect(page.locator(".oil-directory__person")).toHaveCount(6);
});
