import { expect, test } from "@playwright/test";
import fs from "node:fs";
import { oilCompanyEmployees } from "../src/lib/oilCompanies";
import type { Organization } from "../src/types";

const organizations = JSON.parse(
  fs.readFileSync(
    new URL("../src/data/generated/organizations.json", import.meta.url),
    "utf8",
  ),
) as Organization[];
const category = oilCompanyEmployees(organizations);

test("oil-company category requires employment, not mere representation", async ({ page }) => {
  expect(category.employees.length).toBeGreaterThanOrEqual(6);
  expect(category.employees.map((person) => person.name)).not.toContain("Fred Bielaski");
  expect(category.employees.map((person) => person.name)).not.toContain("Martin B Chittick");

  await page.goto("./oil-companies/");
  const list = page.getByRole("region", { name: "Oil company employee list" });
  await expect(list.locator(".oil-directory__person")).toHaveCount(category.employees.length);
  await expect(list.getByRole("link", { name: "Fred Bielaski", exact: true })).toHaveCount(0);
  await expect(list.getByRole("link", { name: "Martin B Chittick", exact: true })).toHaveCount(0);
});

test("qualified earlier representation remains visible on the person's page", async ({ page }) => {
  await page.goto("./people/15a29a44-a8fd-5b29-b86e-f5ec49ccf794/");
  await expect(page.getByRole("heading", { name: "Fred Bielaski", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("employment status is not documented");
  await expect(page.locator("main")).toContainText("Richmond Levering Co., Inc.");
});
