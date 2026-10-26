import fs from "node:fs";
import { expect, test } from "@playwright/test";

const evidence = fs.readFileSync(
  new URL(
    "../../research/evidence-page451-franz-stone-to-william-stoppe-review_batch-921_2026-10-26.json",
    import.meta.url,
  ),
  "utf8",
);

const profiles = [
  ["2ae9e581-728c-5e63-b11c-055e82208b3e", "Franz T Stone"],
  ["7c9621d7-a086-501f-83e4-ec804eee8eed", "Franz T Stone"],
  ["4a034e0a-7e12-513f-b9e2-e8c3ea45a895", "George Stone"],
  ["4d430faa-718d-5966-b521-1a5e70d1f0a6", "Harry L Stone"],
  ["ce673b69-e635-5dd6-9623-2cc544325084", "Jack W Stone"],
  ["985f4849-5045-5cfe-982a-c01a8bed3f02", "Katherine T Stone"],
  ["773a3e2c-7d01-542e-93f0-35fc0fa85890", "Katherine D Stone"],
  ["f8d4679d-40c3-59c8-8c09-211c0697dbc5", "Kenneth S Stone"],
  ["b941d58f-625d-555c-931e-62a49ed11c7c", "Kirk H Stone"],
  ["e24c44f9-d71c-5ec5-a45e-f42fdd335e3a", "Martin R Stone"],
  ["c149ac40-bafc-5f8b-952b-fd452a6862b2", "Norman Stone"],
  ["9bd8988a-fa3d-56df-ba0b-ca751a1f93f5", "Orville C Stone"],
  ["b7d45841-06f9-574d-b6a3-ba9808c72a4f", "Stone Stone"],
  ["b7a5d36a-ff2f-5c50-b6de-784bafe5d61c", "Ward S Stone"],
  ["6b0d1d2e-39c7-5e6d-b3e7-db24178335e1", "William M Stone"],
  ["8c317a37-92de-5056-9cf1-44c6fa6fa777", "Donna M Stoner"],
  ["c8c78b53-71ac-532d-ad2e-6925c1953574", "James B Stoner"],
  ["aa4e8983-ee9c-5e01-b227-f5d98c82a648", "Edna F Stonesifer"],
  ["d710a222-4b39-55df-9ab5-81c8eee836ce", "Catherine J Stonitsch"],
  ["807f6052-1c82-5804-9077-59d534add06f", "Oscar Stonorov"],
  ["e2597159-a1af-52ae-a691-db27fff06410", "David K Stookey"],
  ["a9a77b30-9fd3-5c38-9998-5aa3970c67a7", "Berthold J Stoos"],
  ["b0e72372-abb5-5173-8b87-0655201869ac", "William R Stoppe"],
] as const;

test("Batch 921 publishes all 23 people with terminal outcomes and masked identifiers", async ({ page }) => {
  for (const [id, name] of profiles) {
    await page.goto(`./people/${id}/`);
    await expect(page.getByRole("heading", { name, level: 1 })).toBeVisible();
    const main = page.locator("main");
    await expect(main).not.toContainText("not started");
    await expect(main).not.toContainText("in progress");
    const serials = await main.locator("dt").filter({ hasText: /^Serial$/ })
      .locator("xpath=following-sibling::dd[1]").allTextContents();
    for (const value of serials) expect(value).not.toMatch(/^[A-Z]?\s?\d{4,9}(?:RA)?$/);
  }
});

test("the duplicate Franz Stone leads remain separate and withheld", async ({ page }) => {
  for (const id of [
    "2ae9e581-728c-5e63-b11c-055e82208b3e",
    "7c9621d7-a086-501f-83e4-ec804eee8eed",
  ]) {
    await page.goto(`./people/${id}/`);
    const main = page.locator("main");
    await expect(main).toContainText("needs identity review");
    await expect(main).toContainText("adjacent Box 750 Franz T Stone files");
    await expect(main).not.toContainText("Office of Production Management");
    await expect(main).not.toContainText("Special adviser");
  }
});

test("Kirk Stone publishes student affiliations without presenting them as employers", async ({ page }) => {
  await page.goto("./people/b941d58f-625d-555c-931e-62a49ed11c7c/");
  const main = page.locator("main");
  await expect(main).toContainText("University of Michigan");
  await expect(main).toContainText("Syracuse University");
  await expect(main).toContainText("student");
  await expect(main).toContainText("not employment");
  await expect(main).toContainText("Kirk H. Stone to William J. Donovan");
});

test("Oscar Stonorov's unbridged architect lead is withheld", async ({ page }) => {
  await page.goto("./people/807f6052-1c82-5804-9077-59d534add06f/");
  const main = page.locator("main");
  await expect(main).toContainText("needs identity review");
  await expect(main).toContainText("Box 750 personnel file");
  await expect(main).toContainText("No publishable pre-OSS affiliation is recorded yet");
  await expect(main).not.toContainText("Stonorov & Kahn");
  await expect(main).not.toContainText("architect and partner");
});

test("William Stoppe publishes a qualified occupation but no invented employer", async ({ page }) => {
  await page.goto("./people/b0e72372-abb5-5173-8b87-0655201869ac/");
  const main = page.locator("main");
  await expect(main).toContainText("occupations producing bakery products");
  await expect(main).toContainText("no employer is identified");
  await expect(main).toContainText("occupation only found");
  await expect(main).toContainText("May 12, 1943");
});

test("Batch 921 evidence excludes credentials and protected identifier fields", () => {
  expect(evidence).not.toMatch(/"serial_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toMatch(/"service_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toContain("NARA_API_KEY");
  expect(evidence).not.toContain("x-api-key");
});

test("Batch 921 publishes its exact coverage counters", async ({ request }) => {
  const response = await request.get("./data/stats.json");
  expect(response.ok()).toBeTruthy();
  const stats = await response.json();
  expect(stats).toMatchObject({
    source_rows: 23_978,
    person_entities: 23_936,
    possible_duplicate_groups: 619,
    research_attempted_people: 14_132,
    verified_affiliation_people: 1_005,
    verified_employer_people: 452,
    archival_review_assessed_people: 12_605,
    published_claims: 8_651,
    public_sources: 5_748,
  });
});
