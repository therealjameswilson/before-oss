import { expect, test } from "@playwright/test";

test("David Krech preserves the Krechevsky alias and separates earlier employers", async ({ page }) => {
  await page.goto("./people/dcda092a-a3c2-5d38-8677-94a9083a5844/");
  await expect(page.getByRole("heading", { name: "David Krech", level: 1 })).toBeVisible();
  await expect(page.locator("main")).toContainText("Isadore Krechevsky");
  await expect(page.getByRole("link", { name: "Page 258" }).first()).toBeVisible();

  const immediate = page.locator('section[aria-labelledby="immediate-affiliation"]');
  const civilian = page.locator('section[aria-labelledby="civilian-employer"]');
  const earlier = page.locator('section[aria-labelledby="earlier-affiliations"]');
  await expect(immediate).toContainText("No reviewed claim currently meets the publication threshold");
  await expect(civilian).toContainText("A single last civilian employer");
  await expect(earlier).toContainText("Swarthmore College");
  await expect(earlier).toContainText("Research assistant to Wolfgang Köhler");
  await expect(earlier).toContainText("University of Colorado");
  await expect(earlier).toContainText("Faculty member");

  const evidence = page.locator('section[aria-labelledby="evidence"]');
  await expect(evidence).toContainText("Katalog Nachlass Else Frenkel-Brunswik");
  await expect(evidence).toContainText("International Encyclopedia of the Social Sciences");
  await expect(evidence).toContainText("David Krech, Psychology: Berkeley");
});

test("the superseded Isadore Krechevsky entity has no separate public profile", async ({ page }) => {
  const response = await page.goto("./people/ff31b94f-e68d-5cc5-b3a3-b860603813e3/");
  expect(response?.status()).toBe(404);
});

test("Nick Kochopolus and Kuchopolus remain separate with a non-identifying public group", async ({ page }) => {
  const cases = [
    ["2e1db921-c0e9-5568-ad5c-4a12fbd552a0", "Nick Kochopolus"],
    ["26ec588b-b35f-5ca4-b056-1c0e73af0d6c", "Nick Kuchopolus"],
  ];
  for (const [id, name] of cases) {
    await page.goto(`./people/${id}/`);
    await expect(page.getByRole("heading", { name, level: 1 })).toBeVisible();
    await expect(page.locator("main")).toContainText(/private identifier/i);
    await expect(page.locator("main")).toContainText(/duplicate-[a-f0-9]{12}/i);
    await expect(page.locator("main")).not.toContainText(/serial-conflict/i);
  }
});

test("the John Knox and Jean Kohn identifier collision remains an explicit conflict", async ({ page }) => {
  const cases = [
    ["6427139c-d487-56b3-b501-5822d2518ef8", "John J Knox"],
    ["ceee440b-e123-53d9-ac3f-15617a0e34ce", "Jean Kohn"],
  ];
  for (const [id, name] of cases) {
    await page.goto(`./people/${id}/`);
    await expect(page.getByRole("heading", { name, level: 1 })).toBeVisible();
    await expect(page.locator("main")).toContainText("conflicting");
    await expect(page.locator("main")).toContainText(/private identifier/i);
    await expect(page.locator("main")).toContainText(/duplicate-[a-f0-9]{12}/i);
    await expect(page.locator("main")).not.toContainText(/serial-conflict/i);
  }
});

test("Batch 618 keeps the oil-company evidence set unchanged", async ({ page }) => {
  await page.goto("./oil-companies/");
  await expect(page.locator(".oil-directory__person")).toHaveCount(7);
  await expect(page.locator(".oil-directory__list")).not.toContainText("David Krech");
});
