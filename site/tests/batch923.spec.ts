import fs from "node:fs";
import { expect, test } from "@playwright/test";

const evidence = fs.readFileSync(
  new URL(
    "../../research/evidence-page452-carl-strahle-to-william-j-strauss-review_batch-923_2026-10-26.json",
    import.meta.url,
  ),
  "utf8",
);

const profiles = [
  ["8cbb3774-7e59-5d55-bffb-53acecd22cd2", "Carl A Strahle"],
  ["f9da7ec5-13c9-58b9-82b6-d23563f5f9f7", "David C Strain"],
  ["87f3b2ad-f8df-51eb-b329-2e6f130f09c0", "Chester U Strait"],
  ["c94b3848-9fd5-5853-ba51-7d70a707f844", "Eric W Strait"],
  ["972a7829-ca52-58bc-9597-b70e0a545af6", "Mario C Strambi"],
  ["f756f79c-5861-5b36-b2e8-0a2439f88282", "Carl O Strand"],
  ["fa55068c-e7b6-5df7-8b60-c9d6f53b4719", "Philip R Strand"],
  ["ea04c4d9-241f-52fe-950c-4527a4c5de5a", "Gloria Strashun"],
  ["b2bac5dc-7654-5841-a2bb-8bd0ec1e87a1", "David T Strasinger"],
  ["8a29e7f0-d5a9-592c-bad5-39061fd0a0f1", "Irving H Strasmich"],
  ["1933c580-1550-57b5-b64b-a552134b0674", "John G Stratford"],
  ["2cd8072e-ab12-5eb2-958a-ee82f5e17bd1", "Ralph N Stratis"],
  ["17cdb2c1-6f4e-5de8-843c-b623c8b630e3", "Arthur Stratton"],
  ["e12f553f-c269-5280-83cd-a93ce1d9b25e", "Donald Stratton"],
  ["6a9c043b-80ce-5712-a398-4f494790d7ac", "Joseph M Straub"],
  ["4ee4ac5f-f8de-5020-b864-1f0a4d49d393", "Suzanne Straub"],
  ["a85c5a8e-d1a6-552c-8fd1-1f158bb6a41c", "Charles Straughn"],
  ["6891cabd-4f97-54fc-9124-8e47cc99cbe5", "Kenneth H Straus"],
  ["f36cfcbc-5657-5640-a1a9-5a790c938a5e", "Walter Straus"],
  ["80763df7-ed6d-5048-ab8d-0b02bfb25db2", "Frances C Strauss"],
  ["5e5dee83-05e7-57de-9f5c-516b74de4492", "Jean S Strauss"],
  ["445357d5-dcbd-553d-be0a-ce3195fef4aa", "Otto Strauss"],
  ["a0685439-62bd-583d-8ee2-402a9bdf6282", "William J Strauss"],
] as const;

test("Batch 923 publishes all 23 people with terminal outcomes and masked identifiers", async ({ page }) => {
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

test("Arthur Stratton publishes the explicit Robert College to OSS transition", async ({ page }) => {
  await page.goto("./people/17cdb2c1-6f4e-5de8-843c-b623c8b630e3/");
  const main = page.locator("main");
  await expect(main).toContainText("Arthur Mills Stratton");
  await expect(main).toContainText("Robert College");
  await expect(main).toContainText("English teacher");
  await expect(main).toContainText("1942 to 1944");
  await expect(main).toContainText(/immediate pre-OSS affiliation/i);
  await expect(main).toContainText("Bowdoin College");
});

test("Irving Strasmich preserves concurrent law and Rhode Island tax roles", async ({ page }) => {
  await page.goto("./people/8a29e7f0-d5a9-592c-bad5-39061fd0a0f1/");
  const main = page.locator("main");
  await expect(main).toContainText("Rhode Island Division of Taxation");
  await expect(main).toContainText("tax research director");
  await expect(main).toContainText("lawyer, 171 Westminster, room 312");
  await expect(main).toContainText("concurrent");
  await expect(main).toContainText("1943-10-27");
  await expect(main).not.toContainText("immediate pre-OSS affiliation");
});

test("Chester Strait publishes documented missionary work without claiming immediacy", async ({ page }) => {
  await page.goto("./people/87f3b2ad-f8df-51eb-b329-2e6f130f09c0/");
  const main = page.locator("main");
  await expect(main).toContainText("American Baptist");
  await expect(main).toContainText("missionary and Bible-school founder");
  await expect(main).toContainText("Hakha");
  await expect(main).toContainText("documented prewar");
  await expect(main).not.toContainText("explicit immediate");
});

test("eight Army occupation findings remain qualified and employer-free", async ({ page }) => {
  const cases = [
    ["f9da7ec5-13c9-58b9-82b6-d23563f5f9f7", "Meatcutters, except in slaughtering and packing houses", "1941-03-31"],
    ["b2bac5dc-7654-5841-a2bb-8bd0ec1e87a1", "Students", "1943-04-02"],
    ["e12f553f-c269-5280-83cd-a93ce1d9b25e", "Clerks, general office", "1940-10-15"],
    ["6a9c043b-80ce-5712-a398-4f494790d7ac", "Cooks, except private family", "1941-01-27"],
    ["6891cabd-4f97-54fc-9124-8e47cc99cbe5", "Students", "1943-06-11"],
    ["f36cfcbc-5657-5640-a1a9-5a790c938a5e", "Agents and appraisers, not elsewhere classified", "1943-03-15"],
    ["445357d5-dcbd-553d-be0a-ce3195fef4aa", "Nonprocess occupations in manufacturing, not elsewhere classified", "1942-10-16"],
    ["a0685439-62bd-583d-8ee2-402a9bdf6282", "Dairy farmers", "1943-03-08"],
  ] as const;

  for (const [id, occupation, date] of cases) {
    await page.goto(`./people/${id}/`);
    const main = page.locator("main");
    await expect(main).toContainText(occupation);
    await expect(main).toContainText(date);
    await expect(main).toContainText(/no (?:school or )?employer is identified/i);
    await expect(main).toContainText("occupation only found");
  }
});

test("Ralph Stratis exposes the rejected protected-identifier conflict", async ({ page }) => {
  await page.goto("./people/2cd8072e-ab12-5eb2-958a-ee82f5e17bd1/");
  const main = page.locator("main");
  await expect(main).toContainText("conflicting sources");
  await expect(main).toContainText("George Norman F");
  await expect(main).toContainText("T/SGT Ralph N. Stratis");
  await expect(main).toContainText("blocks transfer of every Army field");
  await expect(main).toContainText("No occupation code from the rejected Army row is transferred");
});

test("Jean Strauss keeps qualified French military evidence separate from employment", async ({ page }) => {
  await page.goto("./people/5e5dee83-05e7-57de-9f5c-516b74de4492/");
  const main = page.locator("main");
  await expect(main).toContainText("Jean Sagan");
  await expect(main).toContainText("SAS FAFL");
  await expect(main).toContainText("military assignment");
  await expect(main).toContainText("medium");
  await expect(main).toContainText("requires archival review");
  const civilianEmployer = page.locator('section[aria-labelledby="civilian-employer"]');
  await expect(civilianEmployer).toContainText(
    "No reliable pre-OSS employer has yet been identified in the accessible sources reviewed",
  );
  await expect(civilianEmployer).not.toContainText("SAS FAFL");
});

test("Batch 923 evidence excludes credentials and protected identifier fields", () => {
  expect(evidence).not.toMatch(/"serial_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toMatch(/"service_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toContain("NARA_API_KEY");
  expect(evidence).not.toContain("x-api-key");
});

test("Batch 923 publishes its exact coverage counters", async ({ request }) => {
  const response = await request.get("./data/stats.json");
  expect(response.ok()).toBeTruthy();
  const stats = await response.json();
  expect(stats).toMatchObject({
    source_rows: 23_978,
    person_entities: 23_936,
    possible_duplicate_groups: 619,
    research_attempted_people: 14_178,
    verified_affiliation_people: 1_009,
    verified_employer_people: 455,
    archival_review_assessed_people: 12_651,
    published_claims: 8_689,
    public_sources: 5_769,
  });
});
