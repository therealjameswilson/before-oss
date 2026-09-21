import { expect, test } from "@playwright/test";

test("Alex Inkeles separates the Signal Corps from Cornell employment", async ({ page }) => {
  await page.goto("./people/2a63f636-b442-5b0e-9b45-5c8c53d8b670/");
  await expect(page.getByRole("heading", { name: "Alex Inkeles", level: 1 })).toBeVisible();
  await expect(page.getByRole("link", { name: "Page 224" })).toBeVisible();

  const immediate = page.locator('section[aria-labelledby="immediate-affiliation"]');
  const civilian = page.locator('section[aria-labelledby="civilian-employer"]');
  await expect(immediate).toContainText("U.S. Army Signal Corps");
  await expect(immediate).toContainText("military assignment");
  await expect(immediate).toContainText("explicit immediate");
  await expect(civilian).toContainText("Cornell University");
  await expect(civilian).toContainText("Assistant in the Department of Sociology and Anthropology");
  await expect(civilian).toContainText("strongly date bounded");
  await expect(page.locator("#evidence")).toBeVisible();
  await expect(page.locator("main")).toContainText("Minutes of the Cornell University Board of Trustees");
  await expect(page.locator("main")).toContainText("Foreign Intelligence");
});

test("exact-name Immel rows remain separate and visibly reviewable", async ({ page }) => {
  const cases = [
    ["2042be06-86fb-57e0-b604-da5c63d7bd29", "Joseph H Immel"],
    ["0ba1bef2-c507-58fe-bef8-fc8e29ef603c", "Joseph H Immel"],
  ];
  for (const [id, name] of cases) {
    await page.goto(`./people/${id}/`);
    await expect(page.getByRole("heading", { name, level: 1 })).toBeVisible();
    await expect(page.locator("main")).toContainText("Duplicate group");
    await expect(page.locator("main")).toContainText("One row has a private identifier and one does not");
    await expect(page.locator("main")).toContainText("Archival-review priorityhigh");
  }
});

test("Lillian Huyck variants remain separate pending Box 360 review", async ({ page }) => {
  const cases = [
    ["5b9ddef0-017f-5bd6-8b88-9aac770aef05", "Lillian S Huyck"],
    ["23f3aeff-f80a-51f4-8593-bd6fed6f0448", "Lillian Huyck"],
  ];
  for (const [id, name] of cases) {
    await page.goto(`./people/${id}/`);
    await expect(page.getByRole("heading", { name, level: 1 })).toBeVisible();
    await expect(page.locator("main")).toContainText("Duplicate group");
    await expect(page.locator("main")).toContainText("adjacent names could be a duplicated or shortened entry");
    await expect(page.locator("main")).toContainText("Archival-review priorityhigh");
  }
});

test("the oil-company category remains a seven-person evidence set", async ({ page }) => {
  await page.goto("./people/?q=oil&sort=name_asc");
  const category = page.locator(".featured-directory-category");
  await expect(category.getByRole("heading", { name: "People who worked for oil companies" })).toBeVisible();
  await expect(category.locator("li")).toHaveCount(7);
  await expect(category).toContainText("7 people");
  await expect(category).not.toContainText("Alex Inkeles");
});
