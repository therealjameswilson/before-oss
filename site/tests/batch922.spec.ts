import fs from "node:fs";
import { expect, test } from "@playwright/test";

const evidence = fs.readFileSync(
  new URL(
    "../../research/evidence-page451-robert-storey-to-eli-strahinic-review_batch-922_2026-10-26.json",
    import.meta.url,
  ),
  "utf8",
);

const profiles = [
  ["6d05a8b2-fead-50bf-a2f9-71a472244f3d", "Robert G Storey"],
  ["9d98cb3f-f72f-58d9-b62e-7e2668e868d3", "Hans Storhaug"],
  ["1154eca1-e910-5060-b0d9-14a36d684008", "Lee Storm"],
  ["6a5e9ce8-f1c7-5727-8bb7-f7db5458b21f", "Eileen R Stormberg"],
  ["ed72d56b-f275-521a-bc48-ec9a88b3022e", "William H Stormont"],
  ["a0c69ffc-9476-5212-aede-5950930c3c49", "Leroy W Storms"],
  ["d2d7f85e-cda2-5155-bf64-5b3ce5e178ba", "William W Storms"],
  ["255b1730-c44c-5917-99b4-a2e0040dcc88", "Cleveland H Storrs"],
  ["5343e021-48ae-5751-9df1-36f7b7f961e4", "Charles D Story"],
  ["07b8976a-685d-5b4b-ab92-fd9c6b0c99c1", "Willard E Stott"],
  ["18624c6d-6695-5c15-a649-623169ed816e", "Bernard C Stough"],
  ["8d6aeb36-d988-5efe-8242-b2504bb103f2", "Charles Stout"],
  ["2c154491-3bb2-5e5b-8b28-4966d01e088f", "David B Stout"],
  ["f2b9f64b-7639-5471-9a46-2ea1376df006", "Junius J Stout"],
  ["70ff768d-d6d7-5d80-b88d-6c90e869aae6", "Robert Stout"],
  ["7b5272b6-b369-5bd4-afa7-55c87f51a72e", "Ruth E Stout"],
  ["e445044d-5dbf-51bc-ab0c-d29cf96a87f4", "Cecil C Stovall"],
  ["19d969f1-a213-5b05-9165-c78a8b6d516e", "Dean M Stover"],
  ["9c8ad805-f7ef-524a-9a3c-1d1240188386", "Harris Stover"],
  ["8710270f-c604-54ce-b2ee-81931b138886", "Deborah L Stowe"],
  ["9447dc24-7a05-52af-b5a2-fdb2f02abb42", "John L Stoyka"],
  ["4e31d976-918e-5aa0-b07f-54aed36fbc40", "Lelah M Strader"],
  ["49431e62-6925-5e68-862b-bcf66ec4c5e8", "Eli Strahinic"],
] as const;

test("Batch 922 publishes all 23 people with terminal outcomes and masked identifiers", async ({ page }) => {
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

test("Robert Storey publishes qualified Dallas legal practice, not an invented firm", async ({ page }) => {
  await page.goto("./people/6d05a8b2-fead-50bf-a2f9-71a472244f3d/");
  const main = page.locator("main");
  await expect(main).toContainText("private law practice in Dallas");
  await expect(main).toContainText("last documented civilian practice");
  await expect(main).toContainText("May 26, 1941");
  await expect(main).toContainText("do not name his 1941 firm");
  await expect(main).not.toContainText("Storey, Armstrong & Steger");
  await expect(main).not.toContainText("immediate pre-OSS affiliation");
});

test("Hans Storhaug publishes Allied military service without calling it employment", async ({ page }) => {
  await page.goto("./people/9d98cb3f-f72f-58d9-b62e-7e2668e868d3/");
  const main = page.locator("main");
  await expect(main).toContainText("Norwegian Independent Company 1");
  await expect(main).toContainText("December 1940");
  await expect(main).toContainText("sergeant");
  await expect(main).toContainText("military assignment");
  await expect(main).toContainText("not a civilian employer");
});

test("four Army occupation findings remain qualified and employer-free", async ({ page }) => {
  const cases = [
    ["07b8976a-685d-5b4b-ab92-fd9c6b0c99c1", "Farm hands, general farms", "1941-12-29"],
    ["18624c6d-6695-5c15-a649-623169ed816e", "Machinists", "1944-01-27"],
    ["9c8ad805-f7ef-524a-9a3c-1d1240188386", "Students", "1943-07-08"],
    ["9447dc24-7a05-52af-b5a2-fdb2f02abb42", "Teachers and instructors, not elsewhere classified", "1942-12-01"],
  ] as const;

  for (const [id, occupation, date] of cases) {
    await page.goto(`./people/${id}/`);
    const main = page.locator("main");
    await expect(main).toContainText(occupation);
    await expect(main).toContainText(date);
    await expect(main).toContainText(/no (?:school or )?employer is identified/i);
    await expect(main).toContainText("occupation only found");
  }

  await page.goto("./people/18624c6d-6695-5c15-a649-623169ed816e/");
  await expect(page.locator("main")).not.toContainText("P5T");
});

test("Cecil Stovall exposes the C/O identity conflict without transferring Army fields", async ({ page }) => {
  await page.goto("./people/e445044d-5dbf-51bc-ab0c-d29cf96a87f4/");
  const main = page.locator("main");
  await expect(main).toContainText("conflicting sources");
  await expect(main).toContainText("Cecil O Stovall");
  await expect(main).toContainText("middle-initial conflict");
  await expect(main).toContainText("no Army field is transferred");
  await expect(main).not.toContainText("civilian occupation");
});

test("John Stoyka's official OSS identity remains separate from his Army occupation", async ({ page }) => {
  await page.goto("./people/9447dc24-7a05-52af-b5a2-fdb2f02abb42/");
  const main = page.locator("main");
  await expect(main).toContainText("OSS Cat Team radio operator");
  await expect(main).toContainText("National Park Service");
  await expect(main).toContainText("Teachers and instructors, not elsewhere classified");
  await expect(main).toContainText("no employer is identified");
});

test("Batch 922 evidence excludes credentials and protected identifier fields", () => {
  expect(evidence).not.toMatch(/"serial_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toMatch(/"service_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toContain("NARA_API_KEY");
  expect(evidence).not.toContain("x-api-key");
});

test("Batch 922 publishes its exact coverage counters", async ({ request }) => {
  const response = await request.get("./data/stats.json");
  expect(response.ok()).toBeTruthy();
  const stats = await response.json();
  expect(stats).toMatchObject({
    source_rows: 23_978,
    person_entities: 23_936,
    possible_duplicate_groups: 619,
    research_attempted_people: 14_155,
    verified_affiliation_people: 1_006,
    verified_employer_people: 452,
    archival_review_assessed_people: 12_628,
    published_claims: 8_663,
    public_sources: 5_757,
  });
});
