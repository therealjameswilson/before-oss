import fs from "node:fs";
import { expect, test } from "@playwright/test";

const evidence = fs.readFileSync(
  new URL(
    "../../research/evidence-page442-squillacioti-to-st-sauveur-review_batch-905_2026-10-25.json",
    import.meta.url,
  ),
  "utf8",
);

const people = fs.readFileSync(
  new URL("../src/data/generated/people.json", import.meta.url),
  "utf8",
);

const profiles = [
  ["bc08ab60-1f86-5122-81dd-eeb3c5ec4cc7", "Phillip I Squillacioti"],
  ["20b2395a-763a-5af4-b883-a3706d91ec7f", "Emerson T Squire"],
  ["5f455f1d-7dda-53a6-9752-6321d305ed9f", "Loren D Squire"],
  ["329e3c54-16ab-5811-bbe7-968bc959039b", "Aaron Squires"],
  ["ca2acceb-bbbd-5a88-b6ab-e634031ffeac", "Emerson Squires"],
  ["8d5414b6-2613-5a7f-a186-7b99db380802", "Roy W Squires"],
  ["ac5a7cd5-3bd0-52ca-940f-f8a3a082e2da", "Joseph T Sranova"],
  ["ee345694-fb4f-514b-948c-ce155de19d9f", "Anonda Srivardhana"],
  ["09b75d60-426c-5791-b9ff-6da5e5c15729", "Karawek Srivicharn"],
  ["91af211a-42ce-51ff-a200-80a2851aea05", "Philemon A St. Amant"],
  ["522e731e-4043-5cf9-9ad9-9f6047976f8d", "Alice E St. Clair"],
  ["613d537b-f9a6-5dae-9a5c-baf52c014968", "James T St. Clair"],
  ["15ee567b-7398-5018-9ef6-71101a57e7cd", "Rodman A St. Clair"],
  ["cd7dcd2b-b166-5ce2-97f0-b36f09585d73", "Joseph R St. Gelais"],
  ["d85572a8-0a71-50f4-a847-8602b3463c55", "Laurent M St. Georges"],
  ["f36e01b2-1d6c-5814-b067-103f9ea9512a", "Lawrence S St. Jean"],
  ["09f2177d-1c37-5d8b-b236-1dc3ba175b1a", "Wilfred T St. Laurence"],
  ["d1a8fa3a-f5e3-57db-a76b-31c97f044a17", "Antonio L St. Laurent"],
  ["e56f66cd-9fe3-5322-926b-a103a02141cf", "Ramond P St. Laurent"],
  ["1c21abe6-b6e6-599c-ba12-57d6d0e007ae", "Albert J St. Michel"],
  ["50dc58a1-51f3-5532-a8ef-c7b0d6f85894", "Ivan B St. Onge"],
  ["51dd54e1-a3d7-5976-acf5-4e9d09e836c5", "Wallace J St. Pierre"],
  ["7e87391c-bc9d-5311-9151-a0a31793b7ba", "Pierre G St. Sauveur"],
] as const;

test("Batch 905 publishes all 23 people with terminal outcomes and masked identifiers", async ({ page }) => {
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

test("Batch 905 Army occupation bridges stay qualified as occupations", async ({ page }) => {
  const checks = [
    ["bc08ab60-1f86-5122-81dd-eeb3c5ec4cc7", "Purchasing agents and buyers"],
    ["20b2395a-763a-5af4-b883-a3706d91ec7f", "Social and welfare workers"],
    ["329e3c54-16ab-5811-bbe7-968bc959039b", "Photographers"],
    ["ac5a7cd5-3bd0-52ca-940f-f8a3a082e2da", "manufacture of textiles"],
    ["d1a8fa3a-f5e3-57db-a76b-31c97f044a17", "Semiskilled machine-shop"],
    ["1c21abe6-b6e6-599c-ba12-57d6d0e007ae", "manufacture of textiles"],
    ["7e87391c-bc9d-5311-9151-a0a31793b7ba", "manufacture of textiles"],
  ] as const;

  for (const [id, occupation] of checks) {
    await page.goto(`./people/${id}/`);
    const main = page.locator("main");
    await expect(main).toContainText(occupation);
    await expect(main).toContainText("no employer is identified");
    await expect(main.locator("section[aria-labelledby='civilian-employer']")).toContainText(
      "No reliable pre-OSS employer has yet been identified",
    );
  }
});

test("Anonda Srivardhana publishes Carnegie as student status, not employment", async ({ page }) => {
  await page.goto("./people/ee345694-fb4f-514b-948c-ce155de19d9f/");
  const main = page.locator("main");
  await expect(main).toContainText("Carnegie Institute of Technology");
  await expect(main).toContainText("student");
  await expect(main).toContainText("Anond Siwatthana");
  await expect(main).toContainText("military intelligence");
  await expect(main.locator("section[aria-labelledby='civilian-employer']")).toContainText(
    "No reliable pre-OSS employer has yet been identified",
  );
});

test("Aaron Squires preserves the Aaron and Alan Deer Team discrepancy", async ({ page }) => {
  await page.goto("./people/329e3c54-16ab-5811-bbe7-968bc959039b/");
  const main = page.locator("main");
  await expect(main).toContainText("OSS Deer Team");
  await expect(main).toContainText("Alan Squires");
  await expect(main).toContainText("conflicting");
  await expect(main).toContainText("Photographers");
});

test("Karawek Srivicharn keeps the Free Thai officer role and variant", async ({ page }) => {
  await page.goto("./people/09b75d60-426c-5791-b9ff-6da5e5c15729/");
  const main = page.locator("main");
  await expect(main).toContainText("Karawek Siwichan");
  await expect(main).toContainText("Free Thai officers");
  await expect(main).toContainText("December 1942");
  await expect(main.locator("section[aria-labelledby='civilian-employer']")).toContainText(
    "No reliable pre-OSS employer has yet been identified",
  );
});

test("Batch 905 keeps identifier conflicts visible without merging people", async ({ page }) => {
  await page.goto("./people/522e731e-4043-5cf9-9ad9-9f6047976f8d/");
  await expect(page.locator("main")).toContainText("Alice E Gibson");
  await expect(page.locator("main")).toContainText("conflict remains unresolved");

  await page.goto("./people/e56f66cd-9fe3-5322-926b-a103a02141cf/");
  await expect(page.locator("main")).toContainText("Eugene K Matthews");
  await expect(page.locator("main")).toContainText("conflict remains unresolved");
});

test("Identity-only Army bridges do not publish unsafe occupation values", async ({ page }) => {
  for (const id of [
    "09f2177d-1c37-5d8b-b236-1dc3ba175b1a",
    "50dc58a1-51f3-5532-a8ef-c7b0d6f85894",
    "51dd54e1-a3d7-5976-acf5-4e9d09e836c5",
  ]) {
    await page.goto(`./people/${id}/`);
    const main = page.locator("main");
    await expect(main).not.toContainText("occupation value 999");
    await expect(main).not.toContainText("occupation code 195");
    await expect(main).not.toContainText("occupation code 345");
    await expect(main.locator("section[aria-labelledby='civilian-employer']")).toContainText(
      "No reliable pre-OSS employer has yet been identified",
    );
  }
});

test("Batch 905 evidence and public projection exclude credential and protected fields", () => {
  expect(evidence).not.toMatch(/"serial_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toMatch(/"service_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toContain("NARA_API_KEY");
  expect(evidence).not.toContain("x-api-key");
  expect(evidence).not.toContain("A1005159");
  expect(evidence).not.toContain("1012824");
  expect(people).not.toContain("8487e9c0-ca5b-5685-90d3-fff81f2ba3c7");
  expect(people).not.toContain("b14884c7-bb41-518a-aca8-d13a8a9118da");
  expect(people).not.toContain("2b260a8e-5846-5db4-8ccf-238361ab4f24");
});

test("Batch 905 publishes its exact coverage counters", async ({ request }) => {
  const response = await request.get("./data/stats.json");
  expect(response.ok()).toBeTruthy();
  const stats = await response.json();
  expect(stats).toMatchObject({
    source_rows: 23_978,
    person_entities: 23_936,
    possible_duplicate_groups: 608,
    research_attempted_people: 13_766,
    verified_affiliation_people: 989,
    verified_employer_people: 447,
    archival_review_assessed_people: 12_237,
    published_claims: 8_403,
    public_sources: 5_616,
  });
});
