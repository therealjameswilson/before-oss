import fs from "node:fs";
import { expect, test } from "@playwright/test";

const evidence = fs.readFileSync(
  new URL(
    "../../research/evidence-page443-stamoulis-to-stanley-review_batch-907_2026-10-25.json",
    import.meta.url,
  ),
  "utf8",
);

const people = fs.readFileSync(
  new URL("../src/data/generated/people.json", import.meta.url),
  "utf8",
);

const profiles = [
  ["5c4f081c-0157-54b4-8601-ffb36c851ea4", "Thomas S Stamoulis"],
  ["12a33d31-8539-54fc-8778-9604cd57e62e", "Demetrius G Stampados"],
  ["e7d8cb18-535b-5006-8c3c-6d511a997b97", "Susan C Stampados"],
  ["81951af4-37ca-55b8-9ec5-66e80209aff8", "James D Stamper"],
  ["9b9b1467-e3fa-5399-8138-d790378ea4e3", "Vincent C Stampone"],
  ["596a3916-bb44-5955-8e60-4aee9eaf7788", "Basil J Stanberg"],
  ["00c92df5-fea7-5cb8-9f7b-3f5f94634951", "Charles R Standen"],
  ["4275343b-5f88-5dce-80fa-fd3a8d970449", "Victor L Stanek"],
  ["9fa1606f-115c-5344-bed3-f553167530ee", "Phoebe E Stanfield"],
  ["369d4b4a-b7c7-5a5a-af00-a5da9f338583", "Clarence Stanford"],
  ["ce18c2b1-9bd4-5cd7-b957-41a784785cf0", "Dorothy M Stanford"],
  ["49375915-35a5-5c97-a7bf-8b06cfb46a2c", "Ferdinand F Stanford"],
  ["3435d3c4-40df-5661-88fb-e70feb26401a", "George W Stanford"],
  ["1a2b8b12-8b9d-599c-8c3f-6cb21b4ce088", "Marie Stanhope"],
  ["6ca6bc3e-6112-5adf-b829-8a07e27aa133", "William Stanko"],
  ["dc853cf2-d6bb-5d21-921d-09f9a54e953f", "George Stankula"],
  ["6c2ebb81-da8b-50ce-9c20-4f1ce56da92f", "Carl T Stanley"],
  ["340e3e1b-c7b6-52a5-b985-e9c92e8959eb", "Eugene R Stanley"],
  ["e3761d01-ebe3-5fa6-b945-29564cd67251", "Hippolyte L Stanley"],
  ["767d1ad9-6711-5917-95c3-1234d6f003c3", "Joseph W Stanley"],
  ["5b1ac0d8-9131-5113-8d00-8844c26fe9ee", "Katherine J Stanley"],
  ["4c794cd9-83c8-5c28-b2fa-9358d1c739d7", "Leo F Stanley"],
  ["801e5aca-5e7e-5de7-b37b-f8485e333c49", "Robert W Stanley"],
] as const;

test("Batch 907 publishes all 23 people with terminal outcomes and masked identifiers", async ({ page }) => {
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

test("Batch 907 Army bridges publish qualified occupations, not employers", async ({ page }) => {
  const checks = [
    ["9b9b1467-e3fa-5399-8138-d790378ea4e3", "Advertising agents"],
    ["596a3916-bb44-5955-8e60-4aee9eaf7788", "production of clay products"],
    ["4275343b-5f88-5dce-80fa-fd3a8d970449", "Meatcutters"],
    ["49375915-35a5-5c97-a7bf-8b06cfb46a2c", "Carpenters"],
    ["6ca6bc3e-6112-5adf-b829-8a07e27aa133", "Bartenders"],
    ["6c2ebb81-da8b-50ce-9c20-4f1ce56da92f", "Oilers of machinery"],
    ["340e3e1b-c7b6-52a5-b985-e9c92e8959eb", "Draftsmen"],
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

test("Stampados publishes confirmed Greek Air Force service without inventing an immediate or civilian employer", async ({ page }) => {
  await page.goto("./people/12a33d31-8539-54fc-8778-9604cd57e62e/");
  const main = page.locator("main");
  await expect(main).toContainText("Hellenic Royal Air Force");
  await expect(main).toContainText("staff officer");
  await expect(main).toContainText("11 December 1941");
  await expect(main).toContainText("documented pre-OSS");
  await expect(main).toContainText("confirmed");
  await expect(main.locator("section[aria-labelledby='immediate-affiliation']")).toContainText(
    "No reviewed claim currently meets the publication threshold",
  );
  await expect(main.locator("section[aria-labelledby='civilian-employer']")).toContainText(
    "No reliable pre-OSS employer has yet been identified",
  );
});

test("Stamoulis conflict does not transfer the disputed Army occupation", async ({ page }) => {
  await page.goto("./people/5c4f081c-0157-54b4-8601-ffb36c851ea4/");
  const main = page.locator("main");
  await expect(main).toContainText("conflicting");
  await expect(main).toContainText("middle-initial conflict");
  await expect(main).not.toContainText("Hotel and restaurant managers");
  await expect(main.locator("section[aria-labelledby='civilian-employer']")).toContainText(
    "No reliable pre-OSS employer has yet been identified",
  );
});

test("Clarence Stanford namesake leads stay private", async ({ page }) => {
  await page.goto("./people/369d4b4a-b7c7-5a5a-af00-a5da9f338583/");
  const main = page.locator("main");
  await expect(main).not.toContainText("P-101");
  await expect(main).not.toContainText("Stanford Marine Railway");
  await expect(main).not.toContainText("boatbuilder");
  await expect(main).toContainText("archival");
});

test("Batch 907 evidence and public projection exclude credentials and private candidate records", () => {
  expect(evidence).not.toMatch(/"serial_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toMatch(/"service_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toContain("NARA_API_KEY");
  expect(evidence).not.toContain("x-api-key");
  expect(people).not.toContain("b4188863-95c1-5919-84fc-b7fcb2f94a39");
  expect(people).not.toContain("8669cc0c-3b73-5c53-b78e-cf4fab37a80d");
});

test("Batch 907 publishes its exact coverage counters", async ({ request }) => {
  const response = await request.get("./data/stats.json");
  expect(response.ok()).toBeTruthy();
  const stats = await response.json();
  expect(stats).toMatchObject({
    source_rows: 23_978,
    person_entities: 23_936,
    possible_duplicate_groups: 608,
    research_attempted_people: 13_811,
    verified_affiliation_people: 991,
    verified_employer_people: 447,
    archival_review_assessed_people: 12_283,
    published_claims: 8_439,
    public_sources: 5_631,
  });
});
