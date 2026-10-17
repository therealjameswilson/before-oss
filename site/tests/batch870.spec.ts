import { expect, test } from "@playwright/test";

const profiles = [
  ["8eb0544a-0c25-5136-899c-c7e5b18e6f87", "Naotada Shimomura"],
  ["2bd386f8-b094-5e76-8073-ca4a057444ac", "Walter W Shimon"],
  ["36bc514a-b9f2-5a00-90dd-c605e7dceff1", "John L Shimondle"],
  ["5ee77473-3d1b-5eaf-94d1-af69d6bfd7c7", "Ezra Shine"],
  ["93df4c98-0e4d-516d-b2f7-620ae5c6eee5", "Jack E Shine"],
  ["f99c67d2-428f-54f7-814a-d356e5722b1d", "James S Shinn"],
  ["910a6197-1479-5f5a-8c12-a31bdd7bedb1", "Lee F Shinn"],
  ["05ee6540-0a4a-57ab-bcbf-47c8b6bd56d8", "Paul K Shinsei"],
  ["7ae6a384-afd1-5b17-a196-f32794f22d40", "Harry Shiomos"],
  ["c66e40c1-4794-549f-9538-45d710f2fcb8", "James Shiozaki"],
  ["a2eea974-91bb-517d-b70e-9e41184d6697", "Ralph E Shipley"],
  ["0c996399-3713-52e8-9b4d-1a319d0f42bd", "Archie J Shipman"],
  ["bfbd676d-e206-5bc8-9731-8791b7a8f308", "Raymond Shipman"],
  ["0b4e9757-3969-5f92-9734-53da833023b4", "Saikichi Shirasawa"],
  ["74f04cba-7fc7-5a17-aa9f-1c04c485067e", "Maurice Shire"],
  ["2d075616-376a-53bd-8af5-c68fd400b27d", "Erna B Shirer"],
  ["04c64e73-1281-5978-a45d-321e3cd5ecae", "Clayton L Shirey"],
  ["0b65f30b-b109-5546-b51f-6d258011c83c", "Marion A Shirland"],
  ["9e797ccf-7c94-544c-9927-9290a63d1ea5", "Kenneth O Shirley"],
  ["0f8ebc59-fdda-5a1d-9545-64a3086e455a", "Julius Shiskin"],
  ["c5021dac-db4e-5567-a906-8eb6ae868416", "Ray A Shiver"],
  ["4f6c14cf-6960-5114-89a2-fac41d66d905", "William E Shockley"],
  ["58695810-e9e8-5946-b141-49224f9febd0", "Clifton B Shoemaker"],
] as const;

test("Batch 870 publishes all 23 profiles with terminal outcomes and masked identifiers", async ({ page }) => {
  for (const [id, name] of profiles) {
    await page.goto(`./people/${id}/`);
    await expect(page.getByRole("heading", { name, level: 1 })).toBeVisible();
    const main = page.locator("main");
    await expect(main).toContainText("Archive box");
    await expect(main).not.toContainText("not started");
    const serials = await main.locator("dt").filter({ hasText: /^Serial$/ })
      .locator("xpath=following-sibling::dd[1]").allTextContents();
    for (const value of serials) expect(value).not.toMatch(/^[A-Z]?\s?\d{4,9}(?:RA)?$/);
  }
});

test("Batch 870 confirms Ezra Shine from a direct OSS record without inventing an employer", async ({ page }) => {
  await page.goto("./people/5ee77473-3d1b-5eaf-94d1-af69d6bfd7c7/");
  const main = page.locator("main");
  await expect(main).toContainText("Identity statusconfirmed");
  await expect(main).toContainText("Chief, Schools and Training, OSS Main");
  await expect(main).toContainText("OSS awards and battle-participation records");
  await expect(main).toContainText("requires archival review");
  await expect(main).toContainText("No reliable pre-OSS employer has yet been identified");
  await expect(main).not.toContainText("1110803");
});

test("Batch 870 exposes rather than resolves the Shimondle and Shine identity conflicts", async ({ page }) => {
  for (const id of [
    "36bc514a-b9f2-5a00-90dd-c605e7dceff1",
    "93df4c98-0e4d-516d-b2f7-620ae5c6eee5",
  ]) {
    await page.goto(`./people/${id}/`);
    const main = page.locator("main");
    await expect(main).toContainText("Identity statusconflicting");
    await expect(main).toContainText("conflicting sources");
    await expect(main).toContainText("Electronic Army Serial Number Merged File");
  }
});

test("Batch 870 keeps Shiomos and Maurice Shire identity evidence separate from employer claims", async ({ page }) => {
  await page.goto("./people/7ae6a384-afd1-5b17-a196-f32794f22d40/");
  let main = page.locator("main");
  await expect(main).toContainText("Identity statushigh confidence");
  await expect(main).toContainText("Greek Group VII");
  await expect(main).toContainText("No reliable pre-OSS employer has yet been identified");
  await expect(main).not.toContainText("33776940");

  await page.goto("./people/74f04cba-7fc7-5a17-aa9f-1c04c485067e/");
  main = page.locator("main");
  await expect(main).toContainText("Identity statushigh confidence");
  await expect(main).toContainText("one-digit protected-identifier discrepancy");
  await expect(main).toContainText("No reliable pre-OSS employer has yet been identified");
  await expect(main).not.toContainText("32975656");
});

test("Batch 870 presents Clayton Shirey's Penn State attendance as student status", async ({ page }) => {
  await page.goto("./people/04c64e73-1281-5978-a45d-321e3cd5ecae/");
  const main = page.locator("main");
  await expect(main).toContainText("Identity statushigh confidence");
  await expect(main).toContainText("Pennsylvania State University");
  await expect(main).toContainText("student");
  await expect(main).toContainText("documented pre-OSS");
  await expect(main).toContainText("Immediate pre-OSS affiliationNo reviewed claim currently meets the publication threshold");
  await expect(main).toContainText("Last civilian employer before serviceNo reliable pre-OSS employer has yet been identified");
});

test("Batch 870 qualifies Julius Shiskin's chronology and does not make it immediate pre-OSS", async ({ page }) => {
  await page.goto("./people/0f8ebc59-fdda-5a1d-9545-64a3086e455a/");
  const main = page.locator("main");
  await expect(main).toContainText("Identity statusprobable");
  await expect(main).toContainText("National Bureau of Economic Research");
  await expect(main).toContainText("staff assistant");
  await expect(main).toContainText("Last civilian employer");
  await expect(main).toContainText("Rutgers University");
  await expect(main).toContainText("War Production Board");
  await expect(main).toContainText("temporal relation uncertain");
  await expect(main).toContainText("Immediate pre-OSS affiliationNo reviewed claim currently meets the publication threshold");
});

test("Batch 870 publishes its exact coverage counters", async ({ request }) => {
  const response = await request.get("./data/stats.json");
  expect(response.ok()).toBeTruthy();
  const stats = await response.json();
  expect(stats).toMatchObject({
    source_rows: 23_978,
    person_entities: 23_937,
    possible_duplicate_groups: 579,
    research_attempted_people: 12_975,
    verified_affiliation_people: 941,
    verified_employer_people: 428,
    archival_review_assessed_people: 11_442,
    published_claims: 7_838,
    public_sources: 5_342,
  });
});
