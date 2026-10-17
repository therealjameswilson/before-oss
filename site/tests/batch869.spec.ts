import { expect, test } from "@playwright/test";

const profiles = [
  ["ad3bb53e-309f-5eb6-b467-3892cfbe03e4", "John Sherry"],
  ["0f22c2ea-6577-5dc4-af08-6e5150ed100e", "David A Sherwood"],
  ["19747177-bf65-5a25-980e-4f742a4a885a", "David H Sherwood"],
  ["ef4bf234-c28c-5bd7-a852-8296b82d9bc9", "Henrietta H Sherwood"],
  ["184d9662-fd07-5a9f-80bf-dedaf6f06056", "William F Sherwood"],
  ["31f93097-22e6-582c-b717-d4fc16c63d5c", "William H Sherwood"],
  ["13b10031-f321-5480-a334-61af96397b63", "Suzanne Shestople"],
  ["96691036-4a89-5abc-9157-9a0821f13cf7", "Gertrude M Sheva"],
  ["6998c051-1c2b-5974-acf4-8e47c12a156f", "Edward Shevick"],
  ["e254962a-e82c-5f28-b864-ec90ad0d8f9d", "Newson H Shewitz"],
  ["db07cc9b-4624-59dc-a0ed-812a14d3978d", "Tamotsu Shibutani"],
  ["29939c06-bc66-5d6c-ae17-3189c15cf607", "Daniel C Shields"],
  ["2d6a51a7-7d2a-55f8-b290-b1c3ca676509", "Gerard V Shields"],
  ["4b830826-f6e0-5464-87f0-667e9bb64a5a", "Haldor G Shields"],
  ["049bc775-6e28-57a0-afec-f798c76b268b", "John F Shields"],
  ["f46f2ff7-44a9-591d-b7ba-c4605f17e3a5", "John J Shields"],
  ["071b9733-074a-5784-b2e7-98bade9c5c7a", "Justine L Shields"],
  ["09f8a452-c835-5a6a-a6a2-958a990ac869", "William H Shields"],
  ["2155ea9e-faaa-5c7d-9726-668aeac2fe65", "Nathan Shiffman"],
  ["11da5f98-21d4-59bf-bc76-7882437019c0", "Harold S Shiles"],
  ["61638d98-2b07-50f1-b1fd-ee8f1254c3e6", "Edward A Shils"],
  ["5f0e480d-aab6-5d26-b2a0-dbd748d5033f", "Frederick N Shilzony"],
  ["0c6f9b05-ad23-588d-bfa3-6820fe78cdf1", "William L Shimko"],
] as const;

test("Batch 869 publishes all 23 profiles with terminal outcomes and masked identifiers", async ({ page }) => {
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

test("Batch 869 separates Shibutani's last civilian employer from student status", async ({ page }) => {
  await page.goto("./people/db07cc9b-4624-59dc-a0ed-812a14d3978d/");
  const main = page.locator("main");
  await expect(main).toContainText("Identity statushigh confidence");
  await expect(main).toContainText("Japanese American Evacuation and Resettlement Study");
  await expect(main).toContainText("research assistant and participant observer");
  await expect(main).toContainText("Last civilian employer");
  await expect(main).toContainText("strongly date bounded");
  await expect(main).toContainText("University of California, Berkeley");
  await expect(main).toContainText("student");
  await expect(main).toContainText("Immediate pre-OSS affiliationNo reviewed claim currently meets the publication threshold");
});

test("Batch 869 qualifies Shilzony's two 1942 affiliations without making them immediate", async ({ page }) => {
  await page.goto("./people/5f0e480d-aab6-5d26-b2a0-dbd748d5033f/");
  const main = page.locator("main");
  await expect(main).toContainText("Identity statusprobable");
  await expect(main).toContainText("RCA Communications, Inc.");
  await expect(main).toContainText("communications engineer");
  await expect(main).toContainText("Twentieth Century-Fox Film Corporation");
  await expect(main).toContainText("technical advisor for Manila Calling");
  await expect(main).toContainText("documented pre-OSS");
  await expect(main).toContainText("Immediate pre-OSS affiliationNo reviewed claim currently meets the publication threshold");
  await expect(main).toContainText("Last civilian employer before serviceFor this question: No reliable pre-OSS employer has yet been identified");
});

test("Batch 869 confirms Haldor Shields from direct official OSS evidence", async ({ page }) => {
  await page.goto("./people/4b830826-f6e0-5464-87f0-667e9bb64a5a/");
  const main = page.locator("main");
  await expect(main).toContainText("Identity statusconfirmed");
  await expect(main).toContainText("Award of Unit Certificate of Merit");
  await expect(main).toContainText("official Unit Certificate of Merit record");
  await expect(main).toContainText("requires archival review");
  await expect(main).not.toContainText("35223328");
});

test("Batch 869 keeps accepted Army matches as identity-only evidence", async ({ page }) => {
  for (const id of [
    "ad3bb53e-309f-5eb6-b467-3892cfbe03e4",
    "0f22c2ea-6577-5dc4-af08-6e5150ed100e",
    "19747177-bf65-5a25-980e-4f742a4a885a",
    "2d6a51a7-7d2a-55f8-b290-b1c3ca676509",
    "049bc775-6e28-57a0-afec-f798c76b268b",
    "f46f2ff7-44a9-591d-b7ba-c4605f17e3a5",
    "2155ea9e-faaa-5c7d-9726-668aeac2fe65",
    "11da5f98-21d4-59bf-bc76-7882437019c0",
    "0c6f9b05-ad23-588d-bfa3-6820fe78cdf1",
  ]) {
    await page.goto(`./people/${id}/`);
    const main = page.locator("main");
    await expect(main).toContainText("Electronic Army Serial Number Merged File");
    await expect(main).toContainText("not a named employer or Army-to-OSS chronology");
  }
});

test("Batch 869 preserves Edward Shils's earlier reviewed profile", async ({ page }) => {
  await page.goto("./people/61638d98-2b07-50f1-b1fd-ee8f1254c3e6/");
  const main = page.locator("main");
  await expect(main).toContainText("Identity statushigh confidence");
  await expect(main).toContainText("University of Chicago");
  await expect(main).toContainText("Research Assistant; Instructor in the College");
  await expect(main).toContainText("verified employer found");
});

test("Batch 869 publishes its exact coverage counters", async ({ request }) => {
  const response = await request.get("./data/stats.json");
  expect(response.ok()).toBeTruthy();
  const stats = await response.json();
  expect(stats).toMatchObject({
    source_rows: 23_978,
    person_entities: 23_937,
    possible_duplicate_groups: 579,
    research_attempted_people: 12_952,
    verified_affiliation_people: 940,
    verified_employer_people: 428,
    archival_review_assessed_people: 11_419,
    published_claims: 7_825,
    public_sources: 5_334,
  });
});
