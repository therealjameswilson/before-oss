import { expect, test } from "@playwright/test";
import fs from "node:fs";

type Person = { person_id: string; display_name: string };
const people = JSON.parse(
  fs.readFileSync(new URL("../src/data/generated/people.json", import.meta.url), "utf8"),
) as Person[];
const firstPerson = people[0];

test("home reports the complete index and incomplete research honestly", async ({ page }) => {
  await page.goto("./");
  await expect(page.getByRole("heading", { name: /Who were they before OSS/i })).toBeVisible();
  await expect(page.getByText("23,978", { exact: true }).first()).toBeVisible();
  await expect(page.getByText(/The directory is complete; the historical research is not/i)).toBeVisible();
});

test("directory search, commissioned filter, and URL state work", async ({ page }) => {
  await page.goto("./people/");
  await expect(page.getByText(/23,941 results/)).toBeVisible({ timeout: 30_000 });
  await page
    .getByRole("searchbox", { name: "Search", exact: true })
    .fill(firstPerson.display_name);
  await expect(page.getByRole("link", { name: firstPerson.display_name }).first()).toBeVisible();
  await expect(page).toHaveURL(/q=/);
  await page.getByLabel("Commissioned status").selectOption("true");
  await expect(page).toHaveURL(/commissioned=true/);
  await expect(page.locator("#result-summary")).not.toHaveText(/23,941 results/);
});

test("direct person route preserves source evidence and masks serials", async ({ page }) => {
  await page.goto(`./people/${firstPerson.person_id}/`);
  await expect(page.getByRole("heading", { name: firstPerson.display_name, exact: true })).toBeVisible();
  await expect(page.getByRole("heading", { name: "How the person appears in the index" })).toBeVisible();
  const content = await page.locator("body").innerText();
  expect(content).not.toMatch(/\b\d{7,8}\b/);
});

test("organizations, analysis, methodology, sources, and downloads are direct routes", async ({ page }) => {
  for (const route of ["organizations/", "analysis/", "methodology/", "sources/", "downloads/"]) {
    const response = await page.goto(`./${route}`);
    expect(response?.ok(), route).toBeTruthy();
    await expect(page.locator("h1")).toBeVisible();
  }
  const download = await page.request.get("./downloads/personnel_public.csv");
  expect(download.ok()).toBeTruthy();
  expect((await download.text()).split("\n")[0]).toContain("serial_masked");
});

test("a researched profile displays claim-level citations", async ({ page }) => {
  await page.goto(
    "./people/21a6b6f2-5daa-5569-826e-6d193f387d4a/",
  );
  await expect(page.getByRole("heading", { name: "Evidence and citations" })).toBeVisible();
  await expect(page.getByRole("heading", { name: "Sources for this claim" }).first()).toBeVisible();
  await expect(page.getByRole("link", { name: "Mort Bobrow Obituary (1923–2019)" }).first()).toHaveAttribute(
    "href",
    /legacy\.com/,
  );
  await expect(page.getByText("Accessed 2026-07-29.", { exact: false }).first()).toBeVisible();
});

test("the confirmed McWilliams profile separates immediate and civilian affiliations", async ({
  page,
}) => {
  await page.goto(
    "./people/a417086c-3c99-5b5a-a198-35e1dc27f553/",
  );
  await expect(
    page.getByRole("heading", { name: "Julia C McWilliams", exact: true }),
  ).toBeVisible();
  await expect(page.getByText("Julia Child", { exact: false }).first()).toBeVisible();
  await expect(
    page.getByRole("heading", { name: "Office of War Information", exact: true }),
  ).toBeVisible();
  await expect(
    page.getByRole("heading", { name: "W. & J. Sloane", exact: true }).first(),
  ).toBeVisible();
  await expect(
    page.getByRole("link", { name: "NAID 2180661", exact: true }),
  ).toHaveAttribute("href", "https://catalog.archives.gov/id/2180661");
});
