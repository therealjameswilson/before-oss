import fs from "node:fs";
import { expect, test } from "@playwright/test";

const evidence = fs.readFileSync(
  new URL(
    "../../research/evidence-page455-mitsue-m-sugimachi-to-john-l-sullivan-review_batch-929_2026-10-27.json",
    import.meta.url,
  ),
  "utf8",
);

const profiles = [
  ["4b9ee9ae-406e-5052-acfb-3342458b1a0e", "Mitsue M Sugimachi"],
  ["c3272091-5088-51b8-a22a-ed9686c963db", "Yaemitsu Sugimachi"],
  ["e7f51c31-fef5-5a95-861a-2b216f1d62b1", "David M Sugimoto"],
  ["faf7bbe1-a238-51b8-83fc-2728936d170c", "Sang P Suh"],
  ["9d148818-62e7-5f99-a98f-96829d17b157", "Young Wan Suh"],
  ["f4f5e550-d483-542b-877a-c29ead135b2b", "William G Suhling"],
  ["656be164-41d6-5db8-b90b-5a5800c8d62a", "Joseph Suhovich"],
  ["949dff8a-61ee-59cc-908b-cc72c2a066ab", "Jacques Suissa"],
  ["ecad2fa4-9c31-5190-81ba-dd5ec303143d", "Albert F Suitor"],
  ["a9d32691-f8c4-5f45-b96d-6dc02418f59d", "Orman Suker"],
  ["c27ef2e8-8fb2-5d4a-aa2e-29fc47eca4e2", "Awat B Sulaiman"],
  ["8173b048-fdfc-5637-b358-26f402110775", "Boyd Sullivan"],
  ["566d31ed-9087-5e94-bf31-54c481724905", "Charles C Sullivan"],
  ["e1667c65-fa29-50f2-91a1-cfe51fd86368", "Dorothy F Sullivan"],
  ["5ca8a9e4-b2a3-5b59-9eb6-60bf037ea1f9", "Edmund F Sullivan"],
  ["c0ec7141-053c-5395-82bc-23cf3f2b0f4f", "Eileen B Sullivan"],
  ["3a75805e-7d9a-5d41-a472-37ecfd6c91c4", "Francis Sullivan"],
  ["90c20580-29f1-5c8e-bfa6-3602da404576", "Herbert M Sullivan"],
  ["b11e3f9d-a49a-5692-9b93-42677d73b9ca", "James A Sullivan"],
  ["537b148b-dded-55a5-9efb-cbe45ae0d5e7", "James M Sullivan"],
  ["5403327d-921c-523c-aaff-84ee6645e0e2", "John A Sullivan"],
  ["143102f8-5932-59ae-b577-9005ebbe6c99", "John E Sullivan"],
  ["8aaf8dbf-7222-50a3-87a3-229778ac91d5", "John L Sullivan"],
] as const;

test("Batch 929 publishes all 23 people with terminal outcomes and masked identifiers", async ({ page }) => {
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

test("Suhling publishes the 1939 company only as qualified earlier employment", async ({ page }) => {
  await page.goto("./people/f4f5e550-d483-542b-877a-c29ead135b2b/");
  const main = page.locator("main");
  await expect(main).toContainText("William Gerhard Suhling Jr.");
  await expect(main).toContainText("Suhling & Co., Inc.");
  await expect(main).toContainText("president");
  await expect(main).toContainText("leaf-tobacco");
  await expect(main).toContainText("Earlier pre-OSS affiliations");
  await expect(main).not.toContainText("Immediate pre-OSS affiliation\nSuhling & Co.");
  await expect(main).toContainText("documented prewar employer found");
});

test("Yaemitsu Sugimachi keeps probable identity, reporter employment and teacher occupation qualified", async ({ page }) => {
  await page.goto("./people/c3272091-5088-51b8-a22a-ed9686c963db/");
  const main = page.locator("main");
  await expect(main).toContainText("probable");
  await expect(main).toContainText("Rafu Shimpo");
  await expect(main).toContainText("reporter");
  await expect(main).toContainText("teacher");
  await expect(main).toContainText("no school or employer is identified");
  await expect(main).toContainText("do not establish an OSS role");
});

test("Suissa and Suker publish military identities without inventing civilian employers", async ({ page }) => {
  await page.goto("./people/949dff8a-61ee-59cc-908b-cc72c2a066ab/");
  let main = page.locator("main");
  await expect(main).toContainText("Sussex (Proust)");
  await expect(main).toContainText("foreign or allied military personnel");
  await expect(main).toContainText("Commissioned officer");
  await expect(main).toContainText("does not supply a pre-OSS employer");

  await page.goto("./people/a9d32691-f8c4-5f45-b96d-6dc02418f59d/");
  main = page.locator("main");
  await expect(main).toContainText("class 72-43");
  await expect(main).toContainText("15 April to 7 July 1943");
  await expect(main).toContainText("Military training, not civilian employment.");
  await expect(main).toContainText("commissioned army officer");
});

test("Army occupation categories remain employer-free and Boyd's post-OSS record is identity-only", async ({ page }) => {
  for (const [id, occupation] of [
    ["656be164-41d6-5db8-b90b-5a5800c8d62a", "Chauffeurs and drivers"],
    ["ecad2fa4-9c31-5190-81ba-dd5ec303143d", "Dairy farmers"],
    ["5ca8a9e4-b2a3-5b59-9eb6-60bf037ea1f9", "Statistical clerks and compilers"],
    ["3a75805e-7d9a-5d41-a472-37ecfd6c91c4", "Chauffeurs and drivers"],
    ["90c20580-29f1-5c8e-bfa6-3602da404576", "Students"],
  ] as const) {
    await page.goto(`./people/${id}/`);
    const main = page.locator("main");
    await expect(main).toContainText(occupation);
    await expect(main).toContainText("no employer");
    await expect(main).toContainText("occupation only found");
  }

  await page.goto("./people/8173b048-fdfc-5637-b358-26f402110775/");
  const main = page.locator("main");
  await expect(main).toContainText("1946-01-21");
  await expect(main).toContainText("after OSS dissolution");
  await expect(main).not.toContainText("Day workers");
});

test("the first John L Sullivan row remains separate and flagged for joint archival review", async ({ page, request }) => {
  const response = await request.get("./data/people/j.json");
  const people = await response.json();
  const johns = people.filter((item: { display_name: string }) => item.display_name === "John L Sullivan");
  expect(johns).toHaveLength(3);
  const reviewed = johns.find((item: { person_id: string }) => item.person_id === "8aaf8dbf-7222-50a3-87a3-229778ac91d5");
  expect(reviewed.possible_duplicate_group).toBeTruthy();
  expect(johns.filter((item: { research_status: string }) => item.research_status === "not_started")).toHaveLength(2);

  await page.goto("./people/8aaf8dbf-7222-50a3-87a3-229778ac91d5/");
  const main = page.locator("main");
  await expect(main).toContainText("Possible duplicate group");
  await expect(main).toContainText("Three separately printed John L Sullivan rows");
  await expect(main).toContainText("Review all three Box 757");
});

test("Batch 929 does not change the evidence-defined oil-company category", async ({ page }) => {
  await page.goto("./oil-companies/");
  const main = page.locator("main");
  await expect(main).toContainText("14 people");
  await expect(main).toContainText("15 historically named");
  await expect(main).not.toContainText("Suhling & Co.");
  await expect(main).not.toContainText("Rafu Shimpo");
});

test("Batch 929 evidence excludes credentials and protected identifier fields", () => {
  expect(evidence).not.toMatch(/"serial_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toMatch(/"service_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toContain("NARA_API_KEY");
  expect(evidence).not.toContain("x-api-key");
});

test("Batch 929 publishes its exact coverage counters", async ({ request }) => {
  const response = await request.get("./data/stats.json");
  expect(response.ok()).toBeTruthy();
  const stats = await response.json();
  expect(stats).toMatchObject({
    source_rows: 23_978,
    person_entities: 23_936,
    possible_duplicate_groups: 629,
    research_attempted_people: 14_314,
    verified_affiliation_people: 1_014,
    verified_employer_people: 458,
    archival_review_assessed_people: 12_787,
    published_claims: 8_788,
    public_sources: 5_820,
  });
});
