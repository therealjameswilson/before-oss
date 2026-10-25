import fs from "node:fs";
import { expect, test } from "@playwright/test";

const evidence = fs.readFileSync(
  new URL(
    "../../research/evidence-page445-starr-to-stauski-review_batch-909_2026-10-25.json",
    import.meta.url,
  ),
  "utf8",
);

const people = fs.readFileSync(
  new URL("../src/data/generated/people.json", import.meta.url),
  "utf8",
);

const profiles = [
  ["b1685cc0-d3cf-54d2-a9c7-3b92852ac8f8", "Roy C Starr"],
  ["9563b55e-8c83-5f50-b973-487895c64674", "Deane W Starret"],
  ["86100598-9e66-5137-8559-5c852307cc51", "Dean W Starrett"],
  ["3ff1fc9b-5a54-5f9c-9eaa-ef99ea9e38a8", "Mason B Starring"],
  ["62d18c8f-69b7-5962-8666-6aef2daaf3ab", "William T Starry"],
  ["aab8d590-c457-5db9-91e7-a6ca3c505597", "Kenneth E Startin"],
  ["9109e767-6ce5-5178-bd4d-baf402786df2", "William T Starube"],
  ["ab3758cd-057e-5e6c-8409-3ede780bfad4", "John G Stary"],
  ["5dbb75e0-b230-582d-b728-792e44598543", "Edward Starz"],
  ["a5228d9e-ffe2-5b64-915b-f8a6f4f686e2", "Edward A Starz"],
  ["20a2b661-e75a-5fd1-b0ff-ff13b891fae4", "Albert E Stasik"],
  ["6314c9c2-b677-51a6-96b2-4fa806ab07fc", "Ernest A Stasik"],
  ["4a522807-5f4b-5e86-8f9d-65517629ada0", "Marion F Staszewski"],
  ["7c036c19-c382-5e31-90bb-96db7e27f6e1", "James F Stathakos"],
  ["476f017e-56e5-5bb9-9f73-c8cc70d84be4", "George J Stathis"],
  ["de0f3b3e-b86f-5da3-b4c4-8b1656610639", "Joseph M Staub"],
  ["62cf1bb0-6d6e-5819-9d76-649968d9fc1f", "Robert Staub"],
  ["f6ea5939-6163-59f6-a9b3-3fe7e848fc26", "Robert Staub"],
  ["18006384-c6a7-5e5f-b4b0-a38c3c5d91c1", "Robert W Stauder"],
  ["e1b3b47a-313f-561c-854a-dbc208ebe40b", "Harold D Stauffer"],
  ["2644026f-3e34-5d35-81a6-d9416b6d1fe5", "John R Stauffer"],
  ["c70de78a-8c12-559d-b5d3-83fddb11f3d7", "Theodore R Stauffer"],
  ["b06886da-6567-55a5-a875-762ed33b51d3", "Joe F Stauski"],
] as const;

test("Batch 909 publishes all 23 people with terminal outcomes and masked identifiers", async ({ page }) => {
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

test("Batch 909 Army bridges publish qualified categories rather than employers", async ({ page }) => {
  const checks = [
    ["b1685cc0-d3cf-54d2-a9c7-3b92852ac8f8", "Paymasters, payroll clerks, and timekeepers"],
    ["62d18c8f-69b7-5962-8666-6aef2daaf3ab", "Actors and actresses"],
    ["ab3758cd-057e-5e6c-8409-3ede780bfad4", "Students"],
    ["62cf1bb0-6d6e-5819-9d76-649968d9fc1f", "Ticket, station, and express agents"],
    ["c70de78a-8c12-559d-b5d3-83fddb11f3d7", "Gardeners and grounds keepers"],
    ["b06886da-6567-55a5-a875-762ed33b51d3", "Occupations in extraction of minerals"],
  ] as const;

  for (const [id, occupation] of checks) {
    await page.goto(`./people/${id}/`);
    const main = page.locator("main");
    await expect(main).toContainText(occupation);
    await expect(main).toContainText("no employer is identified");
    await expect(main.locator("section[aria-labelledby='civilian-employer']")).toContainText(
      "No reliable pre-OSS employer has yet been identified",
    );
  }
});

test("Edward A Starz publishes the official OSS role while the no-initial row stays unresolved", async ({ page }) => {
  await page.goto("./people/a5228d9e-ffe2-5b64-915b-f8a6f4f686e2/");
  let main = page.locator("main");
  await expect(main).toContainText("Operation Cardinal");
  await expect(main).toContainText("radio operator");
  await expect(main.locator("section[aria-labelledby='civilian-employer']")).toContainText(
    "No reliable pre-OSS employer has yet been identified",
  );

  await page.goto("./people/5dbb75e0-b230-582d-b728-792e44598543/");
  main = page.locator("main");
  await expect(main.locator("section[aria-labelledby='evidence']")).toHaveCount(0);
});

test("James F Stathakos displays the conflict and student status without inventing employment", async ({ page }) => {
  await page.goto("./people/7c036c19-c382-5e31-90bb-96db7e27f6e1/");
  const main = page.locator("main");
  await expect(main).toContainText("conflict");
  await expect(main).toContainText("University of Texas");
  await expect(main).toContainText("1939 baseball letterwinner");
  await expect(main).toContainText("not classified as his employer");
  await expect(main).not.toContainText("1287963");
  await expect(main).not.toContainText("0128793");
});

test("George J Stathis keeps a qualified restaurant association separate from employer status", async ({ page }) => {
  await page.goto("./people/476f017e-56e5-5bb9-9f73-c8cc70d84be4/");
  const main = page.locator("main");
  await expect(main).toContainText("Hotel and restaurant managers");
  await expect(main).toContainText("Seaford Restaurant");
  await expect(main).toContainText("does not identify his earlier role");
  await expect(main.locator("section[aria-labelledby='civilian-employer']")).toContainText(
    "No reliable pre-OSS employer has yet been identified",
  );
});

test("same-name and spelling-variant clusters remain separate and evidence-specific", async ({ page }) => {
  await page.goto("./people/9563b55e-8c83-5f50-b973-487895c64674/");
  await expect(page.locator("main")).not.toContainText("Training Materials and Research Section");
  await page.goto("./people/86100598-9e66-5137-8559-5c852307cc51/");
  await expect(page.locator("main")).not.toContainText("Training Materials and Research Section");

  await page.goto("./people/62cf1bb0-6d6e-5819-9d76-649968d9fc1f/");
  await expect(page.locator("main")).toContainText("Ticket, station, and express agents");
  await expect(page.locator("section[aria-labelledby='evidence']")).not.toContainText("Operation Varsity");
  await page.goto("./people/f6ea5939-6163-59f6-a9b3-3fe7e848fc26/");
  await expect(page.locator("main")).not.toContainText("Ticket, station, and express agents");
  await expect(page.locator("section[aria-labelledby='evidence']")).toHaveCount(0);
});

test("Batch 909 evidence and public projection exclude credentials, full identifiers, and private candidates", () => {
  expect(evidence).not.toMatch(/"serial_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toMatch(/"service_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toContain("1287963");
  expect(evidence).not.toContain("0128793");
  expect(evidence).not.toContain("NARA_API_KEY");
  expect(evidence).not.toContain("x-api-key");
  expect(people).not.toContain("candidate-deane-w-starret-row2-starrett-b909");
  expect(people).not.toContain("candidate-robert-staub-row18-varsity-b909");
});

test("Batch 909 publishes its exact coverage counters", async ({ request }) => {
  const response = await request.get("./data/stats.json");
  expect(response.ok()).toBeTruthy();
  const stats = await response.json();
  expect(stats).toMatchObject({
    source_rows: 23_978,
    person_entities: 23_936,
    possible_duplicate_groups: 612,
    research_attempted_people: 13_856,
    verified_affiliation_people: 992,
    verified_employer_people: 447,
    archival_review_assessed_people: 12_329,
    published_claims: 8_469,
    public_sources: 5_648,
  });
});
