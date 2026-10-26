import fs from "node:fs";
import { expect, test } from "@playwright/test";

const evidence = fs.readFileSync(
  new URL(
    "../../research/evidence-page448-stern-to-stevens-review_batch-915_2026-10-25.json",
    import.meta.url,
  ),
  "utf8",
);

const profiles = [
  ["3f7f9e19-f869-5e70-a564-020dc20ef000", "Samuel Stern"],
  ["c6431844-8e4d-557e-b04c-716b91b62574", "Louis Stern II"],
  ["3cd66e21-0ede-57f6-8ff1-024d079d6b16", "Ann Sterrett"],
  ["5afe2046-fe34-5561-8681-4dcc3ef0095a", "Robert E Stettler"],
  ["892b24cb-ca39-5186-97ba-6f84a016e1f7", "Henry L Steuben"],
  ["e8c7d51a-405a-5c6f-a7ee-cab51cc37ac8", "James M Steuber"],
  ["61cad98d-40a2-5194-b6c1-40b98534dd19", "Julian Steuer"],
  ["8e3ad75e-d90e-5d5e-a81a-16fb05bf4b58", "Eugene A Steuert"],
  ["6bb9642b-7be4-5724-9919-7d414ec5815a", "Robert G Steuert"],
  ["2d365fc2-da2c-53fe-b2f5-b9dc98986790", "Anthony Stevens"],
  ["23438d88-83f0-5667-9fe3-053023cbec0d", "Charles R Stevens"],
  ["a94b6c77-e585-5017-8403-1cc185e2975b", "Dorothy Stevens"],
  ["6c69c02c-9785-5468-849a-ba65c52486da", "Edmund Stevens"],
  ["05de92f2-8874-5824-8f2e-f20fbd59adc9", "Eldora K Stevens"],
  ["aaab3951-f2b4-538a-ab05-07c7418b8469", "Elinor N Stevens"],
  ["9832a83e-ae77-54e0-bb3a-a2bea584a4fe", "Evelyn M Stevens"],
  ["481dcee9-df77-599c-8d17-5c98e48049ab", "Frances W Stevens"],
  ["66a93bda-db9a-54dd-8e37-bec5c85a78c7", "Frank E Stevens"],
  ["a66e64a5-9747-528f-9fd4-9c8765da3cf7", "George Stevens"],
  ["87f86752-2ab4-5fc9-bc9f-36b343a8ddff", "Harley C Stevens"],
  ["ad2adb6a-4846-5fc2-959e-9ba25d198d8c", "John A Stevens"],
  ["26117ce0-c1d9-5bf3-a036-63c23c6b868e", "Lawrence N Stevens"],
  ["c086e4e0-577e-5b04-937c-7968e5e74186", "Mary E Stevens"],
] as const;

test("Batch 915 publishes all 23 people with saved outcomes and masked identifiers", async ({ page }) => {
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

test("Batch 915 Army categories remain occupations or student status rather than employers", async ({ page }) => {
  const cases = [
    ["c6431844-8e4d-557e-b04c-716b91b62574", "Managers and officials, not elsewhere classified"],
    ["892b24cb-ca39-5186-97ba-6f84a016e1f7", "Laboratory technicians and assistants"],
    ["61cad98d-40a2-5194-b6c1-40b98534dd19", "Students"],
    ["ad2adb6a-4846-5fc2-959e-9ba25d198d8c", "Farm hands, general farms"],
  ] as const;
  for (const [id, label] of cases) {
    await page.goto(`./people/${id}/`);
    const main = page.locator("main");
    await expect(main).toContainText(label);
    await expect(main).toContainText("no employer is identified");
  }
});

test("Harley C Stevens publishes the separated law and oil-company chronology", async ({ page }) => {
  await page.goto("./people/87f86752-2ab4-5fc9-bc9f-36b343a8ddff/");
  const main = page.locator("main");
  await expect(main).toContainText("Standard Oil Company of California");
  await expect(main).toContainText("Pillsbury Madison & Sutro");
  await expect(main).toContainText("commander of the OSS detachment in Chungking");
  await expect(main).toContainText("strongly date bounded");

  await page.goto("./oil-companies/");
  await expect(page.getByRole("heading", { name: "People who worked for oil companies", level: 1 })).toBeVisible();
  await expect(page.locator("main")).toContainText("14 people");
  await expect(page.locator("main")).toContainText("15 historically named");
  await expect(page.getByRole("link", { name: "Harley C Stevens" })).toBeVisible();

  await page.goto("./organizations/656018b6-ac9c-5305-acee-2e630a6ee0e9/");
  await expect(page.getByRole("heading", { name: "Standard Oil Company of California", level: 1 })).toBeVisible();
  await expect(page.locator("main")).toContainText("Harley C Stevens");
});

test("the Steuber and Strueber rows expose one conflict without an Army occupation transfer", async ({ page }) => {
  for (const [id, name] of [
    ["e8c7d51a-405a-5c6f-a7ee-cab51cc37ac8", "James M Steuber"],
    ["5b7b3a9e-8a78-50d8-82c7-d677b1b8df42", "James M Strueber"],
  ] as const) {
    await page.goto(`./people/${id}/`);
    await expect(page.getByRole("heading", { name, level: 1 })).toBeVisible();
    const main = page.locator("main");
    await expect(main).toContainText("Army row spells the surname Stueber");
    await expect(main).toContainText("remain separate");
    await expect(main).not.toContainText("occupation code 583");
  }
});

test("Batch 915 evidence excludes credentials and protected identifier fields", () => {
  expect(evidence).not.toMatch(/"serial_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toMatch(/"service_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toContain("NARA_API_KEY");
  expect(evidence).not.toContain("x-api-key");
});

test("Batch 915 publishes its exact coverage counters", async ({ request }) => {
  const response = await request.get("./data/stats.json");
  expect(response.ok()).toBeTruthy();
  const stats = await response.json();
  expect(stats).toMatchObject({
    source_rows: 23_978,
    person_entities: 23_936,
    possible_duplicate_groups: 615,
    research_attempted_people: 13_994,
    verified_affiliation_people: 1_001,
    verified_employer_people: 451,
    archival_review_assessed_people: 12_467,
    published_claims: 8_571,
    public_sources: 5_703,
  });
});
