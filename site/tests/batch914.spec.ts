import fs from "node:fs";
import { expect, test } from "@playwright/test";

const evidence = fs.readFileSync(
  new URL(
    "../../research/evidence-page447-stenzel-to-stern-review_batch-914_2026-10-25.json",
    import.meta.url,
  ),
  "utf8",
);

const profiles = [
  ["e0290893-9d54-54b3-93a0-5ad26c83bab0", "Joachim A Stenzel"],
  ["fb1fc5c2-4ba6-59a4-9261-e8e07be58310", "Joseph J Stepaniak"],
  ["dc76e348-18c1-5c94-a065-3ba63d564fac", "Chica M Stephens"],
  ["56b53769-7e4b-531c-b0e1-086eb15dcd1a", "Edward J Stephens"],
  ["4b841b5a-a7a7-58a2-b892-309858539786", "John Stephens"],
  ["43b8e4e5-d436-57ed-ad05-5ad83c93a5e6", "Lillian S Stephens"],
  ["e37fa599-a281-51c5-800f-c769fc428c08", "Raymond R Stephens"],
  ["fd7da39e-45f2-57f4-8dc7-4c680d450f55", "Robert G Stephens"],
  ["6ef6c3ce-1283-5548-8023-4f5b3678f5c8", "William R Stephens"],
  ["65972bde-7b36-5004-a0f4-c878f0a7e725", "Bernice T Stephenson"],
  ["e41f4957-18c0-5c32-ab88-4a772031ba15", "Eleanor F Stephenson"],
  ["fe86dc5a-4569-5932-b300-d9a4f1f30b0d", "John H Stephenson"],
  ["70eccb43-d69c-52d3-8ef0-baca5b8c1af0", "Otis V Stephenson"],
  ["627229bf-03ee-5f9c-b167-c18a0650edc2", "William S Stephenson"],
  ["b0ade786-4c0a-50b3-a43a-4d8326d31d23", "Harry J Steppenbacke"],
  ["45d40362-ad03-5e1f-bfaf-4e293ea4ea3e", "Henry S Sterling"],
  ["e7fbbf6c-9892-5eb8-bb18-603aa8d3a4fc", "Aaron R Stern"],
  ["2d895519-5853-52a6-9dcd-0f813e695e6a", "Alfred Stern"],
  ["dc4da7b2-2f52-52bc-8094-0645afe65ee5", "Barry Stern"],
  ["c19e4bf4-14ed-59fe-8dfd-61fe8affae2c", "David S Stern"],
  ["523f18b9-69f4-5186-b64e-4b52ff68343e", "Floyd L Stern"],
  ["020c0d6f-48a7-5fcb-8808-4f984d44292a", "Ludwig S Stern"],
  ["1002cc50-504e-5d26-a5cd-a09e4b8cd0f0", "Michael F Stern"],
] as const;

test("Batch 914 publishes all 23 people with saved outcomes and masked identifiers", async ({ page }) => {
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

test("Batch 914 Army categories remain occupations rather than employers", async ({ page }) => {
  const cases = [
    ["e37fa599-a281-51c5-800f-c769fc428c08", "Barbers, beauticians, and manicurists"],
    ["fe86dc5a-4569-5932-b300-d9a4f1f30b0d", "production of bakery products"],
    ["e7fbbf6c-9892-5eb8-bb18-603aa8d3a4fc", "Foremen, manufacturing"],
    ["2d895519-5853-52a6-9dcd-0f813e695e6a", "chauffeurs and drivers"],
    ["c19e4bf4-14ed-59fe-8dfd-61fe8affae2c", "Students"],
    ["523f18b9-69f4-5186-b64e-4b52ff68343e", "fabrication of metal products"],
    ["1002cc50-504e-5d26-a5cd-a09e4b8cd0f0", "Stenographers and typists"],
  ] as const;
  for (const [id, label] of cases) {
    await page.goto(`./people/${id}/`);
    const main = page.locator("main");
    await expect(main).toContainText(label);
    await expect(main).toContainText("no employer is identified");
  }
});

test("the two Joachim A Stenzel rows remain separate", async ({ page }) => {
  for (const id of [
    "603ba0b1-79ee-5431-92de-90365a4ebdc6",
    "e0290893-9d54-54b3-93a0-5ad26c83bab0",
  ]) {
    await page.goto(`./people/${id}/`);
    const main = page.locator("main");
    await expect(page.getByRole("heading", { name: "Joachim A Stenzel", level: 1 })).toBeVisible();
    await expect(main).toContainText("different protected identifier");
    await expect(main).toContainText("Review both Box 744");
  }
});

test("Barry Stern exposes the conflict without publishing the disputed occupation", async ({ page }) => {
  await page.goto("./people/dc4da7b2-2f52-52bc-8094-0645afe65ee5/");
  const main = page.locator("main");
  await expect(main).toContainText("separately preserved Barry Steen");
  await expect(main).toContainText("do not transfer Army occupation code 108");
  await expect(main).not.toContainText("Insurance clerks");
});

test("Batch 914 evidence excludes credentials and protected identifier fields", () => {
  expect(evidence).not.toMatch(/"serial_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toMatch(/"service_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toContain("NARA_API_KEY");
  expect(evidence).not.toContain("x-api-key");
});

test("Batch 914 publishes its exact coverage counters", async ({ request }) => {
  const response = await request.get("./data/stats.json");
  expect(response.ok()).toBeTruthy();
  const stats = await response.json();
  expect(stats).toMatchObject({
    source_rows: 23_978,
    person_entities: 23_936,
    possible_duplicate_groups: 615,
    research_attempted_people: 13_971,
    verified_affiliation_people: 1_000,
    verified_employer_people: 450,
    archival_review_assessed_people: 12_444,
    published_claims: 8_557,
    public_sources: 5_696,
  });
});
