import { expect, test } from "@playwright/test";

const profiles = [
  ["6de30fde-22eb-5e6e-adcf-5f31fa7f6f25", "David L Shoemaker"],
  ["2ed7bd13-f5f7-5490-9a10-611d58262d54", "Joel Shoemaker"],
  ["21f68ce6-f302-577a-a370-90868364f8d6", "Charles W Shoenhair"],
  ["6a07b2e4-a988-57d7-b0b5-8769c3b4ce23", "Herbert B Sholar"],
  ["31642b74-4ab5-5552-8fb9-6ff12ee33c72", "Herbert B Sholar"],
  ["e84b4b70-b20e-5dd1-b931-d8fc507f612f", "Susan K Sholar"],
  ["307b3568-6423-51ba-a767-ae2eee842739", "Marion F Sholes"],
  ["a8bdf447-4f0c-5121-b6c8-691e35730214", "Edwin L Sholine"],
  ["2416acd9-7618-52cd-9ffa-6f892207bbfd", "Frederick E Shoninger"],
  ["94fdbc53-ab1e-5db0-aa83-09629f97fa4a", "Leon Shoob"],
  ["bb11c2ff-8973-513f-88d4-0dfde7b772fe", "Henrietta R Shook"],
  ["79354e4a-9d7d-5ec6-816e-549c10d69ca3", "Frank Shoonmaker"],
  ["92b2f8ee-7766-5b88-ad35-ebefaf572eb1", "Elizabeth Shoop"],
  ["06667a15-10f6-5349-a163-182a18b478e7", "Max Shoop"],
  ["3a260b2e-c31d-5424-bef7-2d329de42c6f", "Elsic Shoopman"],
  ["19390357-37db-5e79-94bb-cb1bb36f23dd", "George G Shor"],
  ["d82186ab-c0b6-5c26-918e-11899060c604", "George Shorall"],
  ["3944f715-3f69-5d1a-894a-a17ade4b7d40", "Henry Shore"],
  ["8f3f3ede-871c-58ad-8e26-5d2a5ef1dabd", "Blaine Short"],
  ["2e3a75d3-c063-5967-9941-a4eecaafc84d", "Charley Short"],
  ["ad4d462a-19de-52f3-84f5-e43e44ed1daf", "Dorothy Q Short"],
  ["24a807e2-5938-5fa3-9bcb-fd9ab68dd432", "George J Shotzbarger"],
  ["14bf9684-ab7a-5117-bc1f-97a6b90c3417", "Evelyn N Showers"],
] as const;

test("Batch 871 publishes all 23 profiles with terminal outcomes and masked identifiers", async ({ page }) => {
  for (const [id, name] of profiles) {
    await page.goto(`./people/${id}/`);
    await expect(page.getByRole("heading", { name, level: 1 })).toBeVisible();
    const main = page.locator("main");
    await expect(main).toContainText("Archive box");
    await expect(main).not.toContainText("not started");
    await expect(main).not.toContainText("in progress");
    const serials = await main.locator("dt").filter({ hasText: /^Serial$/ })
      .locator("xpath=following-sibling::dd[1]").allTextContents();
    for (const value of serials) expect(value).not.toMatch(/^[A-Z]?\s?\d{4,9}(?:RA)?$/);
  }
});

test("Batch 871 assigns Herbert Sholar's Air Staff role only to the directly matched row", async ({ page }) => {
  await page.goto("./people/6a07b2e4-a988-57d7-b0b5-8769c3b4ce23/");
  let main = page.locator("main");
  await expect(main).toContainText("Identity statusconfirmed");
  await expect(main).toContainText("A-2 Section of the Air Staff, Air Operational Division");
  await expect(main).toContainText("intelligence analyst");
  await expect(main).toContainText("Last civilian employer");
  await expect(main).toContainText("strongly date bounded");
  await expect(main).not.toContainText("33642839");

  await page.goto("./people/31642b74-4ab5-5552-8fb9-6ff12ee33c72/");
  main = page.locator("main");
  await expect(main).toContainText("Identity statusunresolved");
  await expect(main).toContainText("needs identity review");
  await expect(main).toContainText("distinct from the confirmed Herbert B Sholar record");
  await expect(main).not.toContainText("Air Operational Division");
});

test("Batch 871 separates Max Shoop's last civilian employer from immediate OSS affiliation", async ({ page }) => {
  await page.goto("./people/06667a15-10f6-5349-a163-182a18b478e7/");
  const main = page.locator("main");
  await expect(main).toContainText("Identity statusconfirmed");
  await expect(main).toContainText("Sullivan & Cromwell");
  await expect(main).toContainText("lawyer and Paris office head");
  await expect(main).toContainText("Last civilian employer");
  await expect(main).toContainText("strongly date bounded");
  await expect(main).toContainText("Immediate pre-OSS affiliationNo reviewed claim currently meets the publication threshold");
});

test("Batch 871 publishes Henry Shore's RCA role with qualified chronology", async ({ page }) => {
  await page.goto("./people/3944f715-3f69-5d1a-894a-a17ade4b7d40/");
  const main = page.locator("main");
  await expect(main).toContainText("Identity statushigh confidence");
  await expect(main).toContainText("RCA");
  await expect(main).toContainText("radio expert");
  await expect(main).toContainText("documented pre-OSS");
  await expect(main).toContainText("does not explicitly establish immediate recruitment from RCA");
  await expect(main).toContainText("Immediate pre-OSS affiliationNo reviewed claim currently meets the publication threshold");
});

test("Batch 871 keeps the Sholar and Sholine university records as student affiliations", async ({ page }) => {
  await page.goto("./people/e84b4b70-b20e-5dd1-b931-d8fc507f612f/");
  let main = page.locator("main");
  await expect(main).toContainText("University of South Carolina");
  await expect(main).toContainText("student and graduate history student");
  await expect(main).toContainText("student");
  await expect(main).toContainText("not an employer");

  await page.goto("./people/a8bdf447-4f0c-5121-b6c8-691e35730214/");
  main = page.locator("main");
  await expect(main).toContainText("Colorado A&M");
  await expect(main).toContainText("student and basketball letterwinner");
  await expect(main).toContainText("student status, not an employer");
});

test("Batch 871 exposes the Shoonmaker spelling lead without merging the earlier Schoonmaker profile", async ({ page }) => {
  await page.goto("./people/79354e4a-9d7d-5ec6-816e-549c10d69ca3/");
  let main = page.locator("main");
  await expect(main).toContainText("Identity statusambiguous");
  await expect(main).toContainText("needs identity review");
  await expect(main).toContainText("cannot be merged on name similarity alone");
  await expect(main).not.toContainText("Frank Schoonmaker Selections");

  await page.goto("./people/f870eeb7-2f90-5575-8a93-fe5ee59c0e4b/");
  main = page.locator("main");
  await expect(main).toContainText("Identity statushigh confidence");
  await expect(main).toContainText("Frank Schoonmaker Selections");
  await expect(main).toContainText("verified employer found");
});

test("Batch 871 retains accepted Army matches as identity evidence, not employer claims", async ({ page }) => {
  for (const id of [
    "6de30fde-22eb-5e6e-adcf-5f31fa7f6f25",
    "3a260b2e-c31d-5424-bef7-2d329de42c6f",
    "d82186ab-c0b6-5c26-918e-11899060c604",
    "2e3a75d3-c063-5967-9941-a4eecaafc84d",
    "24a807e2-5938-5fa3-9bcb-fd9ab68dd432",
  ]) {
    await page.goto(`./people/${id}/`);
    const main = page.locator("main");
    await expect(main).toContainText("Electronic Army Serial Number Merged File");
    await expect(main).toContainText("No reliable pre-OSS employer has yet been identified");
  }
});

test("Batch 871 publishes its exact coverage counters", async ({ request }) => {
  const response = await request.get("./data/stats.json");
  expect(response.ok()).toBeTruthy();
  const stats = await response.json();
  expect(stats).toMatchObject({
    source_rows: 23_978,
    person_entities: 23_937,
    possible_duplicate_groups: 581,
    research_attempted_people: 12_998,
    verified_affiliation_people: 946,
    verified_employer_people: 430,
    archival_review_assessed_people: 11_465,
    published_claims: 7_853,
    public_sources: 5_352,
  });
});
