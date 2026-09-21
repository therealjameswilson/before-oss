import { expect, test } from "@playwright/test";

test("Gerschenkron's Federal Reserve role stays earlier and qualified", async ({ page }) => {
  await page.goto("./people/36062bdb-bd0c-5653-8b7e-6b0915258619/");
  await expect(page.getByRole("heading", { name: "Alexander Gerschenkron", level: 1 }))
    .toBeVisible();
  await expect(page.getByRole("link", { name: "Page 166" })).toBeVisible();

  const immediate = page.locator('section[aria-labelledby="immediate-affiliation"]');
  const civilian = page.locator('section[aria-labelledby="civilian-employer"]');
  const earlier = page.locator('section[aria-labelledby="earlier-affiliations"]');
  await expect(immediate).not.toContainText("Federal Reserve");
  await expect(civilian).not.toContainText("Federal Reserve");
  await expect(earlier).toContainText("Board of Governors of the Federal Reserve System");
  await expect(earlier).toContainText("European economic analyst");
  await expect(earlier).toContainText("documented pre-OSS");
  await expect(page.locator('section[aria-labelledby="evidence"]'))
    .toContainText("not proven to be the immediate predecessor");
});

test("different-identifier George Gerbner rows remain separate profiles", async ({ page }) => {
  const cases = [
    ["87360d61-5427-5034-9bf5-94a235db09c6", "George Gerbner"],
    ["207a5f43-7147-5bd6-bc10-91be90a86485", "George Gerbner"],
  ];
  for (const [id, name] of cases) {
    await page.goto(`./people/${id}/`);
    await expect(page.getByRole("heading", { name, level: 1 })).toBeVisible();
    await expect(page.getByRole("link", { name: "Page 166" })).toBeVisible();
    await expect(page.locator("main")).toContainText("Duplicate group");
    await expect(page.locator("main")).toContainText("different private identifiers");
  }
});

test("Rachel Geise and Rachel Giese remain separate variant profiles", async ({ page }) => {
  const cases = [
    ["05a44be9-1df0-5a35-97d1-55b7d1e644e8", "Rachel Geise", "Page 164"],
    ["707c0f20-98ec-58a0-8185-9db9e36debe9", "Rachel Giese", "Page 168"],
  ];
  for (const [id, name, sourcePage] of cases) {
    await page.goto(`./people/${id}/`);
    await expect(page.getByRole("heading", { name, level: 1 })).toBeVisible();
    await expect(page.getByRole("link", { name: sourcePage })).toBeVisible();
    await expect(page.locator("main")).toContainText("Duplicate group");
  }
});

test("the oil-company category remains evidence-scoped after batch 609", async ({ page }) => {
  await page.goto("./oil-companies/");
  await expect(page.locator(".oil-directory__person")).toHaveCount(7);
  await expect(page.locator(".oil-directory__list")).not.toContainText("Alexander Gerschenkron");
});
