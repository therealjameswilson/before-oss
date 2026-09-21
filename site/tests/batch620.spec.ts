import { expect, test } from "@playwright/test";

test("Frank and Franklin Lindsay remain separate reviewed variants", async ({ page }) => {
  const cases = [
    ["8e2121ad-ac78-5ed3-b066-33258ba3dcc0", "Frank Lindsay"],
    ["f10209b9-429e-568b-aaec-7310078b0915", "Franklin A Lindsay"],
  ];
  for (const [id, name] of cases) {
    await page.goto(`./people/${id}/`);
    await expect(page.getByRole("heading", { name, level: 1 })).toBeVisible();
    await expect(page.locator("main")).toContainText("ambiguous");
    await expect(page.locator("main")).toContainText(
      /same private identifier|repeats the private identifier/i,
    );
    await expect(page.locator("main")).toContainText(/duplicate-[a-f0-9]{12}/i);
  }
});
test("Stacey Lloyd and Kwong W Lo expose the identifier conflict without merging", async ({ page }) => {
  const cases = [
    ["06f247a0-afc6-5203-86b7-c331b49f15f3", "Stacey Lloyd"],
    ["8537d52c-6ad0-5eeb-b7e7-ea6ae63bb08e", "Kwong W Lo"],
  ];
  for (const [id, name] of cases) {
    await page.goto(`./people/${id}/`);
    await expect(page.getByRole("heading", { name, level: 1 })).toBeVisible();
    await expect(page.locator("main")).toContainText("conflicting");
    await expect(page.locator("main")).toContainText(/same private identifier/i);
    await expect(page.locator("main")).toContainText(/critical/i);
    await expect(page.locator("main")).toContainText(/duplicate-[a-f0-9]{12}/i);
  }
});

test("Page and Paige Linton retain all three separate index profiles", async ({ page }) => {
  const cases = [
    ["f23acb11-30ef-528c-a4bf-cbd84689dffb", "Page K Linton"],
    ["dfe14b8a-9d6b-5dcf-8231-5201ad288ced", "Paige K Linton"],
    ["1c0dbb47-b101-5fc9-b63a-003e9d316200", "Paige K Linton"],
  ];
  for (const [id, name] of cases) {
    await page.goto(`./people/${id}/`);
    await expect(page.getByRole("heading", { name, level: 1 })).toBeVisible();
    await expect(page.locator("main")).toContainText("ambiguous");
    await expect(page.locator("main")).toContainText(/duplicate-[a-f0-9]{12}/i);
  }
});

test("Batch 620 keeps the oil-company evidence set unchanged", async ({ page }) => {
  await page.goto("./oil-companies/");
  await expect(page.locator(".oil-directory__person")).toHaveCount(7);
  await expect(page.locator(".oil-directory__list")).not.toContainText("Frank Lindsay");
});
