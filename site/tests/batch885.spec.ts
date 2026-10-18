import fs from "node:fs";
import { expect, test } from "@playwright/test";

const evidence = fs.readFileSync(
  new URL(
    "../../research/evidence-page432-small-smith-review_batch-885_2026-10-18.json",
    import.meta.url,
  ),
  "utf8",
);

const profiles = [
  ["641a6fb4-ac9a-5073-99d3-e09b7a6884b8", "Joe R Small"],
  ["aae930ee-a4a7-50df-9021-905debf82046", "Robert G Smalley"],
  ["5e7aa2ae-6021-56a1-889f-0b1732d83e64", "Jessica M Smart"],
  ["ddb80dd6-e08f-5dc4-864c-7e6fb0d3d6cd", "Thomas W Smart"],
  ["1af2fc03-7251-5e9c-acd8-e6ed7d4f3ae8", "Mary E Smathers"],
  ["ffb749b7-4786-5850-a02f-72b712b13202", "Alvin L Smay"],
  ["6b03a5e4-8063-5476-a64f-96c5f5195096", "Stanley Smeeton"],
  ["9929c280-0260-5e6e-a365-ee60866bec6d", "John C Smeltzer"],
  ["3dca509c-5d97-55d8-bf3b-d2167dcd1935", "Jan Smets"],
  ["50e0c432-19dc-5712-bdb5-87e3fa9366e6", "Jane Smiley"],
  ["6a6a3b03-be44-5024-ad9b-f3727125a02b", "Jane C Smiley"],
  ["15f6dd16-2a26-5774-a914-c310d8e0fa42", "Wiliam C Smiley"],
  ["cf2e2c53-08f4-5fd1-9f88-6abb27f71263", "Thomas T Smillie"],
  ["0d105701-e78d-52df-a417-025d97ef579c", "Walter W Smirnow"],
  ["f5b40785-1b54-51ac-9b9f-7253490327c0", "Alfred G Smith"],
  ["6aa50b1b-d1b4-5433-a59f-e1af47e6db7e", "Aline Smith"],
  ["e0ea0d84-0d8b-59a3-a5e7-d8bbc4784fe5", "Amy E Smith"],
  ["f078df23-27c7-5d63-b5be-20990582319f", "Anne C Smith"],
  ["8edab9f2-9efb-5fa0-a7b5-678b62d53567", "Arline Smith"],
  ["5f8839b9-b84b-5a74-b169-00e195f5e296", "Arthur E Smith"],
  ["4d8a9986-57fa-5f98-b938-df6b0956883c", "Asa A Smith"],
  ["ea0ac3b0-5b13-558c-85ea-a988f57905aa", "Benjamin P Smith"],
  ["600ca71b-9671-529d-9fc1-dd6555cf6975", "Bernarda C Smith"],
] as const;

test("Batch 885 publishes all 23 profiles with terminal outcomes and masked identifiers", async ({ page }) => {
  for (const [id, name] of profiles) {
    await page.goto("./people/" + id + "/");
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

test("Batch 885 keeps the two Jane Smiley rows separate", async ({ page }) => {
  await page.goto("./people/50e0c432-19dc-5712-bdb5-87e3fa9366e6/");
  const jane = page.locator("main");
  await expect(jane).toContainText("Identity statusprobable");
  await expect(jane).toContainText("Jane Smiley Hart");
  const civilian = jane.locator("section[aria-labelledby='civilian-employer']");
  await expect(civilian).toContainText("Unnamed public school in Alfred, New York");
  await expect(civilian).toContainText("English teacher");
  await expect(civilian).toContainText("medium");

  await page.goto("./people/6a6a3b03-be44-5024-ad9b-f3727125a02b/");
  const janeC = page.locator("main");
  await expect(janeC).toContainText("Identity statusunresolved");
  await expect(janeC.locator("section[aria-labelledby='civilian-employer']")).toContainText(
    "No reliable pre-OSS employer has yet been identified",
  );
  await expect(janeC).not.toContainText("Unnamed public school in Alfred");
});

test("Batch 885 publishes Army occupation evidence without inventing employers", async ({ page }) => {
  const checks = [
    ["641a6fb4-ac9a-5073-99d3-e09b7a6884b8", "Student"],
    ["ddb80dd6-e08f-5dc4-864c-7e6fb0d3d6cd", "Managers and officials"],
    ["9929c280-0260-5e6e-a365-ee60866bec6d", "Electricians"],
    ["cf2e2c53-08f4-5fd1-9f88-6abb27f71263", "Gardeners and grounds keepers"],
    ["0d105701-e78d-52df-a417-025d97ef579c", "Linemen and servicemen"],
    ["4d8a9986-57fa-5f98-b938-df6b0956883c", "Bookkeepers and cashiers"],
  ] as const;
  for (const [id, occupation] of checks) {
    await page.goto("./people/" + id + "/");
    const main = page.locator("main");
    await expect(main).toContainText("Identity statushigh confidence");
    await expect(main).toContainText(occupation);
    await expect(main.locator("section[aria-labelledby='civilian-employer']")).toContainText(
      "No reliable pre-OSS employer has yet been identified",
    );
  }
});

test("Batch 885 preserves the printed Smiley spelling and reviewed Army variant", async ({ page }) => {
  await page.goto("./people/15f6dd16-2a26-5774-a914-c310d8e0fa42/");
  const main = page.locator("main");
  await expect(page.getByRole("heading", { name: "Wiliam C Smiley", level: 1 })).toBeVisible();
  await expect(main).toContainText("William C Smiley");
  await expect(main).toContainText("Managers and officials");
});

test("Batch 885 qualifies Jan Smets and preserves the Belgian note", async ({ page }) => {
  await page.goto("./people/3dca509c-5d97-55d8-bf3b-d2167dcd1935/");
  const main = page.locator("main");
  await expect(main).toContainText("Identity statusprobable");
  await expect(main).toContainText("Belgian");
  await expect(main).toContainText("Doctor mission");
  await expect(main.locator("section[aria-labelledby='civilian-employer']")).toContainText(
    "No reliable pre-OSS employer has yet been identified",
  );
});

test("Batch 885 preserves Smith officer classification without over-resolving identity", async ({ page }) => {
  await page.goto("./people/ea0ac3b0-5b13-558c-85ea-a988f57905aa/");
  const main = page.locator("main");
  await expect(main).toContainText("commissioned army officer");
  await expect(main).toContainText("Commissioned officerYes");
  await expect(main).toContainText("Identity statusunresolved");
  await expect(main.locator("section[aria-labelledby='civilian-employer']")).toContainText(
    "No reliable pre-OSS employer has yet been identified",
  );
});

test("Batch 885 evidence bundle excludes private identifiers and credentials", () => {
  expect(evidence).not.toMatch(/"serial_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toMatch(/"service_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toContain("NARA_API_KEY");
  expect(evidence).not.toContain("x-api-key");
});

test("Batch 885 publishes its exact coverage counters", async ({ request }) => {
  const response = await request.get("./data/stats.json");
  expect(response.ok()).toBeTruthy();
  const stats = await response.json();
  expect(stats).toMatchObject({
    source_rows: 23_978,
    person_entities: 23_937,
    possible_duplicate_groups: 585,
    research_attempted_people: 13_316,
    verified_affiliation_people: 964,
    verified_employer_people: 435,
    archival_review_assessed_people: 11_784,
    published_claims: 8_062,
    public_sources: 5_450,
  });
});

