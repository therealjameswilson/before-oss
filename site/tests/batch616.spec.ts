import { expect, test } from "@playwright/test";

test("Garson Kanin separates the Signal Corps from RKO employment", async ({ page }) => {
  await page.goto("./people/03835a06-93bb-5db7-846a-aec5e47b58df/");
  await expect(page.getByRole("heading", { name: "Garson Kanin", level: 1 })).toBeVisible();
  await expect(page.getByRole("link", { name: "Page 240" })).toBeVisible();

  const immediate = page.locator('section[aria-labelledby="immediate-affiliation"]');
  const civilian = page.locator('section[aria-labelledby="civilian-employer"]');
  await expect(immediate).toContainText("U.S. Army Signal Corps");
  await expect(immediate).toContainText("military assignment");
  await expect(immediate).toContainText("medium");
  await expect(civilian).toContainText("RKO Radio Pictures, Inc.");
  await expect(civilian).toContainText("Film director");
  await expect(civilian).toContainText("high");
  await expect(page.locator("#evidence")).toBeVisible();
  await expect(page.locator("main")).toContainText("Garson Kanin Papers");
  await expect(page.locator("main")).toContainText("AFI Catalog of Feature Films");
});

test("exact-name John Jett rows remain separate and safely reviewable", async ({ page }) => {
  const ids = [
    "5dd3f402-a16d-5ee6-bb11-0d1f57bb531e",
    "df80bdcc-85be-54c3-9c07-8f49b7bbc031",
  ];
  for (const id of ids) {
    await page.goto(`./people/${id}/`);
    await expect(page.getByRole("heading", { name: "John Jett", level: 1 })).toBeVisible();
    await expect(page.locator("main")).toContainText("Duplicate group");
    await expect(page.locator("main")).toContainText("One row lacks a private identifier and the other has one");
    await expect(page.locator("main")).not.toContainText(/serial-conflict|duplicate-[0-9]{4,}/i);
  }
});

test("Michael and Mike Jozsa remain separate despite a familiar-name variant", async ({ page }) => {
  const cases = [
    ["8fb24f56-2930-5ab5-9488-93df505bab12", "Michael Jozsa"],
    ["142ea202-d95d-58b0-ad56-90ee60c1c1c4", "Mike Jozsa"],
  ];
  for (const [id, name] of cases) {
    await page.goto(`./people/${id}/`);
    await expect(page.getByRole("heading", { name, level: 1 })).toBeVisible();
    await expect(page.locator("main")).toContainText("Duplicate group");
    await expect(page.locator("main")).toContainText("different private identifiers");
    await expect(page.locator("main")).toContainText("Archival-review priorityhigh");
  }
});

test("the oil-company category remains the same seven-person evidence set", async ({ page }) => {
  await page.goto("./oil-companies/");
  await expect(page.locator(".oil-directory__person")).toHaveCount(7);
  await expect(page.locator(".oil-directory__list")).not.toContainText("Garson Kanin");
});
