import { expect, test } from "@playwright/test";

test("Gaevernitz's business activity is qualified rather than called a verified employer", async ({ page }) => {
  await page.goto("./people/8b7344ea-c0e0-54b6-894a-90c64be8db07/");
  await expect(page.getByRole("heading", { name: "Gero V Gaevernitz", level: 1 }))
    .toBeVisible();
  await expect(page.getByRole("link", { name: "Page 159" })).toBeVisible();

  const immediate = page.locator('section[aria-labelledby="immediate-affiliation"]');
  const civilian = page.locator('section[aria-labelledby="civilian-employer"]');
  await expect(immediate).toContainText("Edmund Stinnes");
  await expect(immediate).toContainText("professional affiliation");
  await expect(immediate).toContainText("medium");
  await expect(civilian).not.toContainText("Edmund Stinnes");
  await expect(page.locator('section[aria-labelledby="evidence"]'))
    .toContainText("Probable immediate predecessor");
});

test("Galenson's unnamed accounting firm appears only as earlier documented work", async ({ page }) => {
  await page.goto("./people/30a94b28-903c-51f8-8e80-d36f8c7271fb/");
  await expect(page.getByRole("heading", { name: "Walter Galenson", level: 1 }))
    .toBeVisible();
  await expect(page.getByRole("link", { name: "Page 160" })).toBeVisible();

  const immediate = page.locator('section[aria-labelledby="immediate-affiliation"]');
  const civilian = page.locator('section[aria-labelledby="civilian-employer"]');
  const earlier = page.locator('section[aria-labelledby="earlier-affiliations"]');
  await expect(immediate).not.toContainText("father's accounting firm");
  await expect(civilian).not.toContainText("father's accounting firm");
  await expect(earlier).toContainText("father's accounting firm");
  await expect(earlier).toContainText("documented pre-OSS");
});

test("same-identifier spelling variants remain separate profiles", async ({ page }) => {
  const cases = [
    ["2cc588b4-66d3-5c91-ba3c-bb7126debff0", "Garry G Funari"],
    ["5ab128bc-790b-587f-8618-79825daeccc4", "Garry G Furnari"],
  ];
  for (const [id, name] of cases) {
    await page.goto(`./people/${id}/`);
    await expect(page.getByRole("heading", { name, level: 1 })).toBeVisible();
    await expect(page.getByRole("link", { name: "Page 158" })).toBeVisible();
    await expect(page.locator("main")).toContainText("Duplicate group");
  }
});

test("the oil-company category remains evidence-scoped", async ({ page }) => {
  await page.goto("./oil-companies/");
  await expect(page.locator(".oil-directory__person")).toHaveCount(7);
  await expect(page.locator(".oil-directory__list")).not.toContainText("Gero V Gaevernitz");
  await expect(page.locator(".oil-directory__list")).not.toContainText("Walter Galenson");
});
