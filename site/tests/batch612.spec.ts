import { expect, test } from "@playwright/test";

test("Knut Haugland separates a documented civilian employer from an unresolved OSS relationship", async ({ page }) => {
  await page.goto("./people/8a1378f4-e6f0-530d-a153-2581acc176be/");
  await expect(page.getByRole("heading", { name: "Knut Haugland", level: 1 })).toBeVisible();
  await expect(page.getByRole("link", { name: "Page 198" })).toBeVisible();

  const immediate = page.locator('section[aria-labelledby="immediate-affiliation"]');
  const civilian = page.locator('section[aria-labelledby="civilian-employer"]');
  await expect(immediate).not.toContainText("Høvding Radiofabrikk");
  await expect(civilian).toContainText("Høvding Radiofabrikk");
  await expect(civilian).toContainText("strongly date bounded");
  await expect(page.locator("main")).toContainText("foreign or allied military personnel");
  await expect(page.locator('section[aria-labelledby="evidence"]')).toContainText(
    "neither reviewed account establishes a direct OSS assignment",
  );
});

test("same-identifier Haselfeld and Haselfield rows remain separate", async ({ page }) => {
  const cases = [
    ["a3118ad8-b0b2-532f-91b3-f52585447209", "Donald J Haselfeld"],
    ["02475cda-7139-5ce2-be5f-7ff54290f7e5", "Donald J Haselfield"],
  ];
  for (const [id, name] of cases) {
    await page.goto(`./people/${id}/`);
    await expect(page.getByRole("heading", { name, level: 1 })).toBeVisible();
    await expect(page.getByRole("link", { name: "Page 197" })).toBeVisible();
    await expect(page.locator("main")).toContainText("Duplicate group");
    await expect(page.locator("main")).toContainText(/same private identifier|repeats the private identifier/);
  }
});

test("the Harrington identifier collision stays conflicting and unmerged", async ({ page }) => {
  const cases = [
    ["4d40aeef-3e60-5b82-a878-34660f727675", "Simon C Harrington", "Page 194"],
    ["dba8b70e-ef25-5f39-bf15-102d6d4d7440", "Simon C Harrington", "Page 194"],
    ["05eb008a-5478-5d07-a3eb-ce158db68d62", "Stephen H Harrington", "Page 195"],
  ];
  for (const [id, name, sourcePage] of cases) {
    await page.goto(`./people/${id}/`);
    await expect(page.getByRole("heading", { name, level: 1 })).toBeVisible();
    await expect(page.getByRole("link", { name: sourcePage })).toBeVisible();
    await expect(page.locator("main")).toContainText("Duplicate group");
    await expect(page.locator("main")).toContainText(/conflict|different private identifiers/i);
  }
});

test("the oil-company category remains evidence-scoped after batch 612", async ({ page }) => {
  await page.goto("./oil-companies/");
  await expect(page.locator(".oil-directory__person")).toHaveCount(7);
  await expect(page.locator(".oil-directory__list")).not.toContainText("Knut Haugland");
});
