import { expect, test } from "@playwright/test";

test("top oil-company category includes only cited named-company work", async ({ page }) => {
  await page.goto("./");
  const category = page.locator("#oil-companies");
  await expect(category.locator(".oil-directory__person")).toHaveCount(7);
  await expect(category).toContainText("Eric S Erickson");
  await expect(category).toContainText("Pennco (Eric Erickson oil business)");
  await expect(category).toContainText("own business");
  await expect(category).not.toContainText("John L Endacott");
  await expect(category).not.toContainText("Fred Bielaski");
});

test("Erickson's Pennco evidence remains qualified and not immediate", async ({ page }) => {
  await page.goto("./people/cd589355-8c39-5c32-9510-a747d795d9d6/");
  await expect(page.getByRole("heading", { name: "Eric S Erickson", level: 1 }))
    .toBeVisible();
  await expect(page.getByRole("link", { name: "Page 137" })).toBeVisible();
  await expect(page.locator('section[aria-labelledby="immediate-affiliation"]'))
    .not.toContainText("Pennco");
  await expect(page.locator('section[aria-labelledby="civilian-employer"]'))
    .not.toContainText("Pennco");
  await expect(page.locator('section[aria-labelledby="earlier-affiliations"]'))
    .toContainText("Pennco");
  await expect(page.locator('section[aria-labelledby="evidence"]'))
    .toContainText("Globala Eremitaget");
});

test("page 137 similar Ericsson names remain separate people", async ({ page }) => {
  await page.goto("./people/8c90cc9d-c865-5ce0-9228-af5c73030496/");
  await expect(page.getByRole("heading", { name: "H. Loyd Ericsson", level: 1 }))
    .toBeVisible();
  await page.goto("./people/f6cd3541-4660-53d2-a300-498aee2a1789/");
  await expect(page.getByRole("heading", { name: "Herman Lloyd Ericsson", level: 1 }))
    .toBeVisible();
});
