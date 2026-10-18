import fs from "node:fs";
import { expect, test } from "@playwright/test";

const evidence = fs.readFileSync(
  new URL(
    "../../research/evidence-page436-smith-to-smyser-review_batch-893_2026-10-18.json",
    import.meta.url,
  ),
  "utf8",
);

const profiles = [
  ["da91124a-89fd-5e93-a846-e2411303eca1", "William M Smith"],
  ["3dbc5bde-2890-5e97-89d1-6ce225b533bf", "William H Smith"],
  ["c1c4e791-d7db-5424-a3c2-9f9b15a14021", "William C Smith"],
  ["157e35dc-5ebf-54d0-ab54-17c138da29c4", "William A Smith"],
  ["52f1f635-8b61-5c8f-8d7c-4db2864c48f1", "William Smith"],
  ["a44e8306-6b97-56bb-b79b-daaf4bec5f55", "William J Smith"],
  ["6b5293b4-d121-50da-85bf-9384db948774", "Williard E Smith"],
  ["432ee618-a5b0-5ed8-90c0-de392c13a3f0", "Wilma D Smith"],
  ["b5dcf046-1647-5a06-9d4f-04427707332f", "Wingate Smith"],
  ["a790cb51-5723-5a1e-b72f-e4dbd5c91c50", "Wylie D Smith"],
  ["c2381c10-0242-5f17-9bcb-c2b9537a8d73", "F E Smither"],
  ["a5740231-e0d5-5cb4-a5a6-549184194458", "Jane Smith-Hutton"],
  ["0b2ae5c2-e6e1-57c2-a479-734c39218e2a", "Frank R Smithka"],
  ["eee04cc0-07ae-5122-a7b3-737c40d5efb7", "Edward C Smith-Ross"],
  ["c619eabc-8dd2-55d2-9ced-4b785735f98b", "Andre V Smolianinoff"],
  ["588469b6-d7eb-51ba-97fe-739fa48a9e66", "Frank G Smolinski"],
  ["f836650c-0c21-5ee1-97fd-d61286a7a704", "Carl A Smollar"],
  ["2d2f5d8d-dbd9-5be0-baa0-3e2276a8de58", "Carl A Smollar"],
  ["81d58579-038d-598b-ba59-f7f8ced3e994", "Nick Smoltz"],
  ["19132dd2-ba41-554f-80cd-be5a2293ec28", "Roy W Smurr"],
  ["b13c4730-5346-509d-9509-2d15545b04e2", "Laura Z Smusz"],
  ["6d81be1b-1aa6-5a9c-b710-6201005ad163", "Rost R Smylie"],
  ["de95bdf0-f67e-5e8c-9216-481a3b5e322f", "Richard D Smyser"],
] as const;

test("Batch 893 publishes all 23 profiles with terminal outcomes and masked identifiers", async ({ page }) => {
  for (const [id, name] of profiles) {
    await page.goto(`./people/${id}/`);
    await expect(page.getByRole("heading", { name, level: 1 })).toBeVisible();
    const main = page.locator("main");
    await expect(main).toContainText("Archive box");
    await expect(main).toContainText("726");
    await expect(main).not.toContainText("not started");
    await expect(main).not.toContainText("in progress");
    const serials = await main.locator("dt").filter({ hasText: /^Serial$/ })
      .locator("xpath=following-sibling::dd[1]").allTextContents();
    for (const value of serials) expect(value).not.toMatch(/^[A-Z]?\s?\d{4,9}(?:RA)?$/);
  }
});

test("William Arthur Smith publishes qualified earlier work without inventing the immediate predecessor", async ({ page }) => {
  await page.goto("./people/157e35dc-5ebf-54d0-ab54-17c138da29c4/");
  const main = page.locator("main");
  await expect(main).toContainText("William Arthur Smith");
  await expect(main).toContainText("Scripps-Howard Newspapers");
  await expect(main).toContainText("San Francisco Examiner");
  await expect(main).toContainText("freelance illustrator");
  await expect(main).toContainText("medium documented pre-OSS");
  await expect(main.locator("section[aria-labelledby='immediate-affiliation']")).toContainText(
    "No reviewed claim currently meets the publication threshold",
  );
  await expect(main.locator("section[aria-labelledby='civilian-employer']")).toContainText(
    "No reliable pre-OSS employer has yet been identified",
  );
});

test("Richard D Smyser keeps Penn State student status distinct from employment", async ({ page }) => {
  await page.goto("./people/de95bdf0-f67e-5e8c-9216-481a3b5e322f/");
  const main = page.locator("main");
  await expect(main).toContainText("Dick Smyser");
  await expect(main).toContainText("Pennsylvania State University");
  await expect(main).toContainText("student");
  await expect(main.locator("section[aria-labelledby='civilian-employer']")).toContainText(
    "No reliable pre-OSS employer has yet been identified",
  );
});

test("Edward Smith-Ross and Andre Smolianinoff retain military context without backdating it", async ({ page }) => {
  await page.goto("./people/eee04cc0-07ae-5122-a7b3-737c40d5efb7/");
  let main = page.locator("main");
  await expect(main).toContainText("Edward Charles Smith-Ross");
  await expect(main).toContainText("Royal Air Force");
  await expect(main).toContainText("Flight Lieutenant");
  await expect(main.locator("section[aria-labelledby='immediate-affiliation']")).toContainText(
    "No reviewed claim currently meets the publication threshold",
  );

  await page.goto("./people/c619eabc-8dd2-55d2-9ced-4b785735f98b/");
  main = page.locator("main");
  await expect(main).toContainText("commissioned naval officer");
  await expect(main).toContainText("Lt. Andre Smolianinoff, USN");
  await expect(main.locator("section[aria-labelledby='civilian-employer']")).toContainText(
    "No reliable pre-OSS employer has yet been identified",
  );
});

test("Carl A Smollar rows remain separate and do not share evidence", async ({ page, request }) => {
  const unresolved = "f836650c-0c21-5ee1-97fd-d61286a7a704";
  const matched = "2d2f5d8d-dbd9-5be0-baa0-3e2276a8de58";
  for (const id of [unresolved, matched]) {
    const response = await request.get(`./people/${id}/`);
    expect(response.ok()).toBeTruthy();
    await page.goto(`./people/${id}/`);
    await expect(page.locator("main")).toContainText("duplicate-c58830e3a0b9");
  }
  await page.goto(`./people/${unresolved}/`);
  await expect(page.locator("main")).toContainText("unresolved");
  await expect(page.locator("main")).not.toContainText("Miners and mining-machine operators");
  await page.goto(`./people/${matched}/`);
  await expect(page.locator("main")).toContainText("Miners and mining-machine operators");
});

test("Jane Smith-Hutton is corroborated without an invented role or employer", async ({ page }) => {
  await page.goto("./people/a5740231-e0d5-5cb4-a5a6-549184194458/");
  const main = page.locator("main");
  await expect(main).toContainText("high confidence");
  await expect(main).toContainText("OSS Oral History Project");
  await expect(main).toContainText("biographical information on Jane Smith-Hutton");
  await expect(main.locator("section[aria-labelledby='civilian-employer']")).toContainText(
    "No reliable pre-OSS employer has yet been identified",
  );
});

test("Batch 893 evidence inputs exclude protected identifiers and credentials", () => {
  expect(evidence).not.toMatch(/"serial_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toMatch(/"service_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toContain("NARA_API_KEY");
  expect(evidence).not.toContain("x-api-key");
});

test("Batch 893 publishes its exact coverage counters", async ({ request }) => {
  const response = await request.get("./data/stats.json");
  expect(response.ok()).toBeTruthy();
  const stats = await response.json();
  expect(stats).toMatchObject({
    source_rows: 23_978,
    person_entities: 23_937,
    possible_duplicate_groups: 596,
    research_attempted_people: 13_497,
    verified_affiliation_people: 966,
    verified_employer_people: 435,
    archival_review_assessed_people: 11_967,
    published_claims: 8_167,
    public_sources: 5_492,
  });
});
