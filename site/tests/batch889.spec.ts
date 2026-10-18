import fs from "node:fs";
import { expect, test } from "@playwright/test";

const evidence = fs.readFileSync(
  new URL(
    "../../research/evidence-page434-smith-review_batch-889_2026-10-18.json",
    import.meta.url,
  ),
  "utf8",
);

const profiles = [
  ["c11f411d-69ee-530b-9aba-fccd1e1bd4bf", "Jesse L Smith", "723"],
  ["132926bf-8ee9-5e83-a576-969542f07e3a", "Jewett J Smith", "723"],
  ["9737939b-6b7d-59d5-b2e8-f18da8261c77", "John D Smith", "723"],
  ["478821db-f60f-5f28-81f1-2a5d1ad5cf41", "John F Smith", "723"],
  ["6ff17383-66a8-5585-ae21-76978cd3ed0e", "John P Smith", "723"],
  ["94e47ae9-b030-5be4-ad2f-06563b74551f", "Joseph W Smith", "723"],
  ["e2dae5f7-48af-5d6b-a334-ade4be3e9c5b", "Judson B Smith", "723"],
  ["18baeb58-f44d-5da1-8053-85da5cd5c2da", "Kate E Smith", "723"],
  ["88718a6b-94e1-5e3c-8b3a-00be135d6951", "Lambert A Smith", "723"],
  ["46b4c673-eb69-52f8-bcf7-593b484f4e99", "Lane M Smith", "723"],
  ["14d3a245-619f-5568-8100-83f9af7c71da", "Lena M Smith", "723"],
  ["50d7ec47-ecec-53e1-bbf0-dc3f7f4222d2", "Leo J Smith", "723"],
  ["900e49a7-bb64-5695-9560-229373ffc677", "Leonard L Smith", "723"],
  ["790eb251-c466-5ecd-adb8-b0405af731cf", "Leslie J Smith", "723"],
  ["ea047b3a-5432-51a9-a2e4-48617dee3bba", "Lewis Y Smith", "723"],
  ["f70dd2d3-21ce-500c-be6b-3ec75b20c275", "Lloyd G Smith", "723"],
  ["2f7f90f8-0760-5ed6-ae34-32a5a23b3464", "Mabel Smith", "723"],
  ["d3aa1a23-cd8d-5140-a319-82263a9c5302", "Marcella A Smith", "723"],
  ["41ee2c06-d132-5afd-b79f-78b35ddac2ae", "Margaret H Smith", "723"],
  ["a81031c7-0306-52de-b488-8c5587c4ffa4", "Marian J Smith", "724"],
  ["09d080e7-b6d6-55fb-a4ac-3e639ee2d697", "Marian W Smith", "724"],
  ["51e4dc75-a4bc-50e1-9ce3-58ddfee0760f", "Marian J Smith", "724"],
  ["2166eee3-53de-5865-99a1-35c876da39ca", "Marie A Smith", "724"],
] as const;

test("Batch 889 publishes all 23 profiles with terminal outcomes and masked identifiers", async ({ page }) => {
  for (const [id, name, box] of profiles) {
    await page.goto(`./people/${id}/`);
    await expect(page.getByRole("heading", { name, level: 1 })).toBeVisible();
    const main = page.locator("main");
    await expect(main).toContainText("Archive box");
    await expect(main).toContainText(box);
    await expect(main).not.toContainText("not started");
    await expect(main).not.toContainText("in progress");
    const serials = await main.locator("dt").filter({ hasText: /^Serial$/ })
      .locator("xpath=following-sibling::dd[1]").allTextContents();
    for (const value of serials) expect(value).not.toMatch(/^[A-Z]?\s?\d{4,9}(?:RA)?$/);
  }
});

test("Batch 889 publishes four qualified occupations without inventing employers", async ({ page }) => {
  const checks = [
    ["c11f411d-69ee-530b-9aba-fccd1e1bd4bf", "Chauffeurs and drivers, bus, taxi, truck, and tractor"],
    ["9737939b-6b7d-59d5-b2e8-f18da8261c77", "Bookkeepers and cashiers, except bank cashiers"],
    ["790eb251-c466-5ecd-adb8-b0405af731cf", "Farm hands, general farms"],
    ["ea047b3a-5432-51a9-a2e4-48617dee3bba", "Salesmen, insurance"],
  ] as const;
  for (const [id, occupation] of checks) {
    await page.goto(`./people/${id}/`);
    const main = page.locator("main");
    await expect(main).toContainText("Identity statushigh confidence");
    await expect(main).toContainText(occupation);
    await expect(main.locator("section[aria-labelledby='civilian-employer']")).toContainText(
      "No reliable pre-OSS employer has yet been identified",
    );
  }
});

test("Jesse Smith retains the Army surname variant without replacing the indexed spelling", async ({ page }) => {
  await page.goto("./people/c11f411d-69ee-530b-9aba-fccd1e1bd4bf/");
  const main = page.locator("main");
  await expect(main).toContainText("Indexed formJesse L Smith");
  await expect(main).toContainText("Documented variantsJesse L Tmith");
  await expect(main).toContainText("one-letter surname variation is preserved");
});

test("unbridged Judson and Marian namesakes do not become public employment facts", async ({ page }) => {
  await page.goto("./people/e2dae5f7-48af-5d6b-a334-ade4be3e9c5b/");
  await expect(page.locator("main")).not.toContainText("General Motors Acceptance Corporation");

  await page.goto("./people/09d080e7-b6d6-55fb-a4ac-3e639ee2d697/");
  const main = page.locator("main");
  await expect(main).not.toContainText("Columbia University");
  await expect(main).not.toContainText("anthropologist");
});

test("both Marian J Smith rows remain separate and visibly grouped", async ({ page, request }) => {
  const ids = [
    "a81031c7-0306-52de-b488-8c5587c4ffa4",
    "51e4dc75-a4bc-50e1-9ce3-58ddfee0760f",
  ];
  for (const id of ids) {
    const response = await request.get(`./people/${id}/`);
    expect(response.ok()).toBeTruthy();
    await page.goto(`./people/${id}/`);
    await expect(page.locator("main")).toContainText("duplicate-9e72414e5e15");
  }
  expect(new Set(ids).size).toBe(ids.length);
});

test("the printed T/4 grade is enlisted and excluded from commissioned results", async ({ page }) => {
  await page.goto("./people/900e49a7-bb64-5695-9560-229373ffc677/");
  const main = page.locator("main");
  await expect(main).toContainText("T/4");
  await expect(main).toContainText(/enlisted army personnel/i);

  await page.goto("./people/?commissioned=true&q=Leonard%20L%20Smith");
  await expect(page.locator("main")).not.toContainText("Leonard L Smith");
});

test("Batch 889 evidence inputs exclude protected identifiers and credentials", () => {
  expect(evidence).not.toMatch(/"serial_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toMatch(/"service_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toContain("NARA_API_KEY");
  expect(evidence).not.toContain("x-api-key");
});

test("Batch 889 publishes its exact coverage counters", async ({ request }) => {
  const response = await request.get("./data/stats.json");
  expect(response.ok()).toBeTruthy();
  const stats = await response.json();
  expect(stats).toMatchObject({
    source_rows: 23_978,
    person_entities: 23_937,
    possible_duplicate_groups: 590,
    research_attempted_people: 13_408,
    verified_affiliation_people: 964,
    verified_employer_people: 435,
    archival_review_assessed_people: 11_876,
    published_claims: 8_105,
    public_sources: 5_468,
  });
});
