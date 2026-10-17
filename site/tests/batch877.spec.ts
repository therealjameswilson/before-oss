import { expect, test } from "@playwright/test";

const profiles = [
  ["fbac1d5b-2d40-5e03-b759-58733997cda6", "Irimie Simion"],
  ["6cc327c5-99b9-5488-803b-adcdac33dd67", "Arthur T Simmons"],
  ["bede3114-a627-50da-9656-b6c01c411818", "Aubrey E Simmons"],
  ["0823a9b9-d275-5460-9774-e48ca47ba2f1", "Clara A Simmons"],
  ["f09be7f9-262d-571c-8c8b-9ee6b0112b08", "David H Simmons"],
  ["9b587470-30a3-5a56-93af-efa519bed8d0", "Frederick R Simmons"],
  ["07f43751-ae0b-5cd6-b94e-16c08202a9ad", "Harry C Simmons"],
  ["33611393-112d-5977-925e-b28f0d582cf2", "Henerson B Simmons"],
  ["67960699-bde4-5ed5-88aa-7cd0365da9eb", "Howard E Simmons"],
  ["b400f02a-cd59-593f-9c09-9edb100eb5cd", "James U Simmons"],
  ["72890b84-5f5b-577f-8e03-47fac57c288c", "Theodore M Simmons"],
  ["d4d50f65-0385-5941-8e12-50a35f4b31ac", "Clarence E Simms"],
  ["7cb0dfda-1090-5565-879f-444547c4e1a0", "Louis T Simms"],
  ["3ce317ad-0c2a-5aa2-b654-0056318b7409", "Semeon Simollari"],
  ["866e4bc5-0439-535a-8f85-8827eaf0a4ef", "Alfred Simon"],
  ["cb86bafe-d0da-56cf-81c0-4726696b7f85", "Alfred Simon"],
  ["53833694-69ae-5b69-8a5d-4497da8b67aa", "Arthur Simon"],
  ["b29bd8cf-a36a-51e6-b72c-aaaf46ce57aa", "Arthur Simon"],
  ["ad9ddd0d-bd6d-5ce7-b795-176e1cbed2bb", "Bertram Simon"],
  ["ea571cc7-f709-5573-8b54-2809e120c94a", "Bessie Simon"],
  ["58378aa0-c1b4-5d2c-8e5d-bf98b20ebf68", "Charles E Simon"],
  ["29747340-7f13-58ae-be10-db002df19c65", "Edward Simon"],
  ["c6c0038d-f035-5446-8ef6-12dae4a24dbc", "Frederick J Simon"],
] as const;

test("Batch 877 publishes all 23 profiles with terminal outcomes and masked identifiers", async ({ page }) => {
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

test("Batch 877 documents Semeon Simollari's Army-to-OSS pathway without recasting his postwar business", async ({ page }) => {
  await page.goto("./people/3ce317ad-0c2a-5aa2-b654-0056318b7409/");
  const main = page.locator("main");
  await expect(main).toContainText("Identity statusconfirmed");
  await expect(main).toContainText("United States Army");
  await expect(main).toContainText("Private");
  await expect(main).toContainText("military assignment");
  await expect(main).toContainText("explicit immediate");
  await expect(main).toContainText("recruited from the Army by OSS");
  await expect(main).toContainText("Last civilian employer before serviceNo reliable pre-OSS employer has yet been identified");
  await expect(main).not.toContainText("foreign car shop");
});

test("Batch 877 identifies James Simmons without inventing a 15th Infantry chronology", async ({ page }) => {
  await page.goto("./people/b400f02a-cd59-593f-9c09-9edb100eb5cd/");
  const main = page.locator("main");
  await expect(main).toContainText("Identity statushigh confidence");
  await expect(main).toContainText("Technical Sergeant James U. Simmons");
  await expect(main).toContainText("does not establish the sequence between conventional Army service and OSS");
  await expect(main).toContainText("Immediate pre-OSS affiliationNo reviewed claim currently meets the publication threshold");
});

test("Batch 877 preserves the rejected Clarence Simms namesake", async ({ page }) => {
  await page.goto("./people/d4d50f65-0385-5941-8e12-50a35f4b31ac/");
  const main = page.locator("main");
  await expect(main).toContainText("Identity statushigh confidence");
  await expect(main).toContainText("different Clarence Edward Simms with a different service identifier is rejected");
  await expect(main).toContainText("his employment is not transferred");
  await expect(main).not.toContainText("Booster Produce Company");
});

test("Batch 877 keeps the Bessie Simon Peace Now lead unassigned", async ({ page }) => {
  await page.goto("./people/ea571cc7-f709-5573-8b54-2809e120c94a/");
  const main = page.locator("main");
  await expect(main).toContainText("Identity statusunresolved");
  await expect(main).toContainText("Peace Now Movement");
  await expect(main).toContainText("America First Committee");
  await expect(main).toContainText("no identifier or OSS personnel-file bridge");
  await expect(main).toContainText("Immediate pre-OSS affiliationNo reviewed claim currently meets the publication threshold");
});

test("Batch 877 keeps same-name Alfred and Arthur records as separate profiles", async ({ request }) => {
  const ids = profiles.filter(([, name]) => name === "Alfred Simon" || name === "Arthur Simon").map(([id]) => id);
  expect(new Set(ids).size).toBe(4);
  for (const id of ids) {
    const response = await request.get(`./people/${id}/`);
    expect(response.ok()).toBeTruthy();
  }
});

test("Batch 877 publishes its exact coverage counters", async ({ request }) => {
  const response = await request.get("./data/stats.json");
  expect(response.ok()).toBeTruthy();
  const stats = await response.json();
  expect(stats).toMatchObject({
    source_rows: 23_978,
    person_entities: 23_937,
    possible_duplicate_groups: 583,
    research_attempted_people: 13_134,
    verified_affiliation_people: 951,
    verified_employer_people: 431,
    archival_review_assessed_people: 11_601,
    published_claims: 7_922,
    public_sources: 5_384,
  });
});
