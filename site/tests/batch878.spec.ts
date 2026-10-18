import { expect, test } from "@playwright/test";

const profiles = [
  ["0a133d53-f392-51a2-9b38-7358ff6b50b2", "Harland Simon"],
  ["6e84229d-c02e-5c8e-a75d-16d18303c00f", "Joseph Simon"],
  ["27cd5567-f240-5d50-aaeb-5851a1567f17", "Joseph T Simon"],
  ["d1aba175-815d-58e9-9a33-e52c68d97e83", "Joseph Simon"],
  ["4c772fa4-b323-550a-b9d5-980f23d8d555", "Joseph T Simon"],
  ["11f08ff7-b791-59c1-ae63-8a140ea8dd8b", "Joseph Simon"],
  ["b8395528-a214-5759-be2c-6d0ff77123db", "Julius Simon"],
  ["44c3d56e-0b8d-5df7-ab0e-5b2d9ce8747c", "Martin Simon"],
  ["95421ec2-7bde-5ba0-9f28-4f84545283ae", "Philip Simon"],
  ["1fedfd07-ff3c-56ed-b7d1-c988d988cdc8", "Pierre Simon"],
  ["63142618-27b1-5bdf-b58d-0cfdf31456fc", "Salim I Simon"],
  ["41c851f3-5842-5fdd-aac3-40ee833471df", "Swils Simon"],
  ["2fef1dc1-17c1-5d5f-a433-60b537e76cf0", "Theodore Simon"],
  ["1520673e-0135-5526-8218-2d9a02a23b56", "Roy L Simonds"],
  ["2a3bb9f6-ad23-5e87-9ff4-63d6fc89e8e5", "Philip Simone"],
  ["3e2a786d-7f6d-5d60-a429-897eaf6e17e1", "Yseulte W Simone"],
  ["d7cc2615-652f-50c6-9c30-e3e0a29eef4f", "Henry J Simoneau"],
  ["92eaa7a4-c385-5b86-a5b9-0ba2f0dd9524", "Daniel J Simonelli"],
  ["354b14b6-3b32-5a86-a3cd-3f0302cc7482", "Johnnie S Simoni"],
  ["99d12010-75b9-56da-bebd-12c998d8a971", "Arthur Simons"],
  ["38d387bf-956d-57e0-9212-a9ddda078fbb", "Eliza J Simons"],
  ["61684b52-729c-5e1b-886a-d5e6694671ab", "Fred W Simons"],
  ["8dc403c5-f442-581c-9112-2a9dba40f025", "Hans Simons"],
] as const;

test("Batch 878 publishes all 23 profiles with terminal outcomes and masked identifiers", async ({ page }) => {
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

test("Batch 878 documents Hans Simons's New School employment without overstating recruitment", async ({ page }) => {
  await page.goto("./people/8dc403c5-f442-581c-9112-2a9dba40f025/");
  const main = page.locator("main");
  await expect(main).toContainText("Identity statushigh confidence");
  await expect(main).toContainText("New School for Social Research");
  await expect(main).toContainText("Professor of political science and international relations");
  await expect(main).toContainText("strongly date bounded");
  await expect(main).toContainText("the sources do not use an explicit 'recruited from' formulation");
  await expect(main).toContainText("Last civilian employer before serviceNew School for Social Research");
});

test("Batch 878 keeps Pierre Simon's Army pathway temporally qualified and excludes his postwar company", async ({ page }) => {
  await page.goto("./people/1fedfd07-ff3c-56ed-b7d1-c988d988cdc8/");
  const main = page.locator("main");
  await expect(main).toContainText("Identity statushigh confidence");
  await expect(main).toContainText("United States Army");
  await expect(main).toContainText("OSS/French Resistance liaison");
  await expect(main).toContainText("temporal relation uncertain");
  await expect(main).toContainText("Machine & Products began in 1948 and is excluded");
  await expect(main).toContainText("Immediate pre-OSS affiliationNo reviewed claim currently meets the publication threshold");
});

test("Batch 878 exposes the Joseph Simon conflict while keeping all five rows separate", async ({ page, request }) => {
  const josephIds = profiles.slice(1, 6).map(([id]) => id);
  expect(new Set(josephIds).size).toBe(5);
  for (const id of josephIds) {
    const response = await request.get(`./people/${id}/`);
    expect(response.ok()).toBeTruthy();
  }
  await page.goto("./people/4c772fa4-b323-550a-b9d5-980f23d8d555/");
  const main = page.locator("main");
  await expect(main).toContainText("Identity statusconflicting");
  await expect(main).toContainText("differs by one digit");
  await expect(main).toContainText("All five Joseph Simon source rows remain separate");
  await expect(main).not.toContainText(/\b\d{7,8}\b/);
});

test("Batch 878 keeps Theodore Simon qualified and does not normalize the candidate rank", async ({ page }) => {
  await page.goto("./people/2fef1dc1-17c1-5d5f-a433-60b537e76cf0/");
  const main = page.locator("main");
  await expect(main).toContainText("Identity statusprobable");
  await expect(main).toContainText("Major Theodore Simon at Pontarlier");
  await expect(main).toContainText("does not prove that he is the indexed Theodore Simon");
  await expect(main.getByText("medium", { exact: true })).toBeVisible();
  await expect(main).toContainText("Personnel categoryunknown or indeterminate");
  await expect(main).not.toContainText("Personnel categorycommissioned Army officer");
});

test("Batch 878 does not publish rejected Martin or Julius employer leads", async ({ page }) => {
  await page.goto("./people/44c3d56e-0b8d-5df7-ab0e-5b2d9ce8747c/");
  await expect(page.locator("main")).not.toContainText("Cleveland Orchestra");
  await page.goto("./people/b8395528-a214-5759-be2c-6d0ff77123db/");
  const main = page.locator("main");
  await expect(main).toContainText("Identity statushigh confidence");
  await expect(main).not.toContainText("Royal Green Corp");
});

test("Batch 878 publishes its exact coverage counters", async ({ request }) => {
  const response = await request.get("./data/stats.json");
  expect(response.ok()).toBeTruthy();
  const stats = await response.json();
  expect(stats).toMatchObject({
    source_rows: 23_978,
    person_entities: 23_937,
    possible_duplicate_groups: 584,
    research_attempted_people: 13_157,
    verified_affiliation_people: 952,
    verified_employer_people: 432,
    archival_review_assessed_people: 11_624,
    published_claims: 7_939,
    public_sources: 5_392,
  });
});
