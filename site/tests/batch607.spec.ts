import { expect, test } from "@playwright/test";

test("Farish's documented oil-company representation is not presented as employment", async ({ page }) => {
  await page.goto("./people/c9356a0e-8474-5f03-a634-0bff4555e069/");
  await expect(page.getByRole("heading", { name: "Linn M Farish", level: 1 }))
    .toBeVisible();
  await expect(page.getByRole("link", { name: "Page 141" })).toBeVisible();

  const immediate = page.locator('section[aria-labelledby="immediate-affiliation"]');
  const civilian = page.locator('section[aria-labelledby="civilian-employer"]');
  const earlier = page.locator('section[aria-labelledby="earlier-affiliations"]');
  await expect(immediate).not.toContainText("Amiranian Oil Company");
  await expect(civilian).not.toContainText("Amiranian Oil Company");
  await expect(earlier).toContainText("Amiranian Oil Company");
  await expect(earlier).toContainText("professional affiliation");
  await expect(earlier).toContainText("medium");
  await expect(page.locator('section[aria-labelledby="evidence"]'))
    .toContainText("1937");
});

test("oil-company worker list excludes a professional-affiliation-only lead", async ({ page }) => {
  await page.goto("./oil-companies/");
  await expect(page.getByRole("heading", { name: "People who worked for oil companies" }))
    .toBeVisible();
  await expect(page.locator(".oil-directory__person")).toHaveCount(7);
  await expect(page.locator(".oil-directory__list")).not.toContainText("Linn M Farish");
});

test("the Finney possible-duplicate rows retain distinct profiles", async ({ page }) => {
  const cases = [
    ["8f1b7780-7318-52a1-ab11-a38de9f86606", "Harry A Finney"],
    ["0db5945b-0bf7-59ba-a65d-dfb452ff1d2a", "Harry Alvin Finney"],
  ];
  for (const [id, name] of cases) {
    await page.goto(`./people/${id}/`);
    await expect(page.getByRole("heading", { name, level: 1 })).toBeVisible();
    await expect(page.getByRole("link", { name: "Page 146" })).toBeVisible();
    await expect(page.locator("main")).toContainText("Duplicate group");
  }
});
