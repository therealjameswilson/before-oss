import { expect, test } from "@playwright/test";

test("Moses Hadas has a qualified Columbia-to-OSS pathway", async ({ page }) => {
  await page.goto("./people/87a20fba-2949-53b1-9a30-b36933e71d23/");
  await expect(page.getByRole("heading", { name: "Moses Hadas", level: 1 })).toBeVisible();
  await expect(page.getByRole("link", { name: "Page 187" })).toBeVisible();

  const immediate = page.locator('section[aria-labelledby="immediate-affiliation"]');
  const civilian = page.locator('section[aria-labelledby="civilian-employer"]');
  await expect(immediate).toContainText("Columbia University");
  await expect(immediate).toContainText("strongly date bounded");
  await expect(civilian).toContainText("Columbia University");
  await expect(page.locator('section[aria-labelledby="evidence"]'))
    .toContainText("professor-to-OSS-to-professor sequence");
});

test("same-identifier Guadarelli and Guidarelli rows remain separate", async ({ page }) => {
  const cases = [
    ["b8fdedfd-7562-57ab-9fd9-f6ae42f07e32", "Louis W Guadarelli", "Page 184"],
    ["13cd560f-9f53-5453-b69d-fd9966476a4f", "Louis W Guidarelli", "Page 185"],
  ];
  for (const [id, name, sourcePage] of cases) {
    await page.goto(`./people/${id}/`);
    await expect(page.getByRole("heading", { name, level: 1 })).toBeVisible();
    await expect(page.getByRole("link", { name: sourcePage })).toBeVisible();
    await expect(page.locator("main")).toContainText("Duplicate group");
    await expect(page.locator("main")).toContainText(
      /same private identifier|repeats the private identifier/,
    );
  }
});

test("different-identifier Grossglaus rows remain separate profiles", async ({ page }) => {
  const cases = [
    ["847a7fa2-8d00-5967-a71e-9f331d0a365b", "Harry W Grossglaus"],
    ["0e75b6c4-b8fe-5998-9922-c342f87b3003", "Harry A Grossglaus"],
  ];
  for (const [id, name] of cases) {
    await page.goto(`./people/${id}/`);
    await expect(page.getByRole("heading", { name, level: 1 })).toBeVisible();
    await expect(page.getByRole("link", { name: "Page 183" })).toBeVisible();
    await expect(page.locator("main")).toContainText(
      /different(?: middle initials and)? private identifiers/,
    );
  }
});

test("the oil-company category remains evidence-scoped after batch 611", async ({ page }) => {
  await page.goto("./oil-companies/");
  await expect(page.locator(".oil-directory__person")).toHaveCount(7);
  await expect(page.locator(".oil-directory__list")).not.toContainText("Moses Hadas");
});
