import fs from "node:fs";
import { expect, test } from "@playwright/test";

const evidence = fs.readFileSync(
  new URL(
    "../../research/evidence-page447-steininger-to-stenzel-review_batch-913_2026-10-25.json",
    import.meta.url,
  ),
  "utf8",
);

const profiles = [
  ["1eaeb281-1dcb-503a-a169-2b66fca72fcb", "Irene H Steininger"],
  ["d5f8eeb4-d8cb-58d4-9889-dfd09dd238e1", "Bernard K Steinitz"],
  ["008efcab-4288-538a-88b0-2ec07cdfc550", "L J Steinlein"],
  ["adf8d830-5132-5f94-8525-4556d43a4c63", "Robert J Steinmetz"],
  ["f95e7e8e-b70c-50a7-93f2-624e63d10ae5", "Elizabeth Steinway"],
  ["41542d8f-5226-5d34-8a55-829ed6ba5d57", "Bernard Steinzor"],
  ["47f94246-6f13-5a6c-be03-605942ff0723", "Richard Steinzor"],
  ["49e25661-ad4b-56d0-a74c-885f68c9a923", "Eliot Stellar"],
  ["3e1a4718-993d-5aae-856d-eb968cebc1ba", "Charles C Stelle"],
  ["6b35efae-c413-5e60-853f-8e53f5979dba", "Jean C Stellhorn"],
  ["ce3dba94-abf0-5148-9636-f5b2051a8559", "John L Stelling"],
  ["b8179964-193f-56f2-9f64-2786822d508b", "Karl H Stello"],
  ["4690a353-0a65-5040-b6d2-504bbff25ae9", "Chester R Stelman"],
  ["49dda36a-e8c2-5e03-a04e-b9cdd780d924", "Helmut A Steltermann"],
  ["3c791167-9e98-5f0b-a7c9-fe98b337d885", "Charles H Stember"],
  ["f3c4ad5a-b44d-5308-b1ca-38a93573921b", "Morton Stemberg"],
  ["9ef5a9d6-e409-560b-8637-adc38b4166da", "Reba A Stemmermann"],
  ["b926ff5b-6798-5239-a2d2-acbab9b234f4", "Leonard V Stemnock"],
  ["7c5e76d6-bb6f-529e-9220-ba36cdde0e38", "Marcel Stempher"],
  ["33b8ee52-4e70-5229-be93-8c9de8581ef5", "Robert R Stengel"],
  ["ee22d8cb-a8c8-55cc-8507-ae6a166372b5", "Alex D Stenhous"],
  ["07968dc2-b2d2-59ca-a4e8-986e8ea2dbb4", "Mark D Stenson"],
  ["603ba0b1-79ee-5431-92de-90365a4ebdc6", "Joachim A Stenzel"],
] as const;

test("Batch 913 publishes all 23 people with saved outcomes and masked identifiers", async ({ page }) => {
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

test("Bernard K Steinitz separates the Army pathway from qualified tire-company evidence", async ({ page }) => {
  await page.goto("./people/d5f8eeb4-d8cb-58d4-9889-dfd09dd238e1/");
  const main = page.locator("main");
  await expect(main).toContainText("documented immediate pathway into OSS special training");
  await expect(main).toContainText("Johnson Tire Company");
  await expect(main).toContainText("its sequence relative to Army and OSS service remains uncertain");
  await expect(main).toContainText("not claimed as immediate or last civilian employment");
});

test("Eliot Stellar separates military, government, and student affiliations", async ({ page }) => {
  await page.goto("./people/49e25661-ad4b-56d0-a74c-885f68c9a923/");
  const main = page.locator("main");
  await expect(main).toContainText("Classification Psychologist");
  await expect(main).toContainText("immediate pre-OSS affiliation was the wartime Air Force");
  await expect(main).toContainText("National Defense Research Council");
  await expect(main).toContainText("student status is not employment");
  await expect(main).toContainText("Not counted as a civilian employer");
});

test("Jean C Stellhorn remains probable and omits the directory residence", async ({ page }) => {
  await page.goto("./people/6b35efae-c413-5e60-853f-8e53f5979dba/");
  const main = page.locator("main");
  await expect(main).toContainText("probable match");
  await expect(main).toContainText("occupation as waiter; no employer is named");
  await expect(main).toContainText("not proven to be the immediate pre-OSS role or last civilian employment");
  await expect(main).not.toContainText("3114 India");
});

test("Leonard V Stamnock and Stemnock remain separate pending joint file review", async ({ page }) => {
  await page.goto("./people/b926ff5b-6798-5239-a2d2-acbab9b234f4/");
  let main = page.locator("main");
  await expect(page.getByRole("heading", { name: "Leonard V Stemnock", level: 1 })).toBeVisible();
  await expect(main).toContainText("Box 743 Stemnock and Box 736 Stamnock");
  await expect(main).toContainText("similar names are not merged");

  await page.goto("./people/15f9a410-37d7-57b8-83e6-98ce98e51fb3/");
  main = page.locator("main");
  await expect(page.getByRole("heading", { name: "Leonard V Stamnock", level: 1 })).toBeVisible();
  await expect(main).toContainText("Box 736 Stamnock and Box 743 Stemnock");
  await expect(main).toContainText("similar names are not merged");
});

test("Robert R Stengel keeps malformed grade P53 uninterpreted", async ({ page }) => {
  await page.goto("./people/33b8ee52-4e70-5229-be93-8c9de8581ef5/");
  const main = page.locator("main");
  await expect(main).toContainText("printing-and-publishing category names no employer");
  await expect(main).toContainText("malformed grade value P53 remains uninterpreted");
});

test("Batch 913 evidence excludes credentials, addresses, and protected identifier fields", () => {
  expect(evidence).not.toMatch(/"serial_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toMatch(/"service_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toContain("3114 India");
  expect(evidence).not.toContain("NARA_API_KEY");
  expect(evidence).not.toContain("x-api-key");
});

test("Batch 913 publishes its exact coverage counters", async ({ request }) => {
  const response = await request.get("./data/stats.json");
  expect(response.ok()).toBeTruthy();
  const stats = await response.json();
  expect(stats).toMatchObject({
    source_rows: 23_978,
    person_entities: 23_936,
    possible_duplicate_groups: 615,
    research_attempted_people: 13_948,
    verified_affiliation_people: 1_000,
    verified_employer_people: 450,
    archival_review_assessed_people: 12_421,
    published_claims: 8_543,
    public_sources: 5_692,
  });
});
