import fs from "node:fs";
import { expect, test } from "@playwright/test";

const evidence = fs.readFileSync(
  new URL(
    "../../research/evidence-page457-fred-g-swafford-to-victor-h-swearingen-review_batch-933_2026-10-27.json",
    import.meta.url,
  ),
  "utf8",
);

const profiles = [
  ["c64a56f3-6fc6-52a5-968c-29f3cf050365", "Fred G Swafford"],
  ["f8868ded-ef9e-5573-a291-990bd6d38ff5", "John E Swain"],
  ["ac6f5af1-3a00-56d4-858e-cff941235d2a", "Robert A Swain"],
  ["62a7c1a6-98d2-5b5d-be9d-4fa3515c8441", "George L Swan"],
  ["7a42a7ad-813b-5603-bf41-4a983d5bb0e4", "George E Swan"],
  ["69a6f0c3-d2cc-5083-8699-c20a004aca7c", "Fletcher B Swank"],
  ["0bf5a230-67ef-5df0-ba1b-8cd327338508", "Lawrence E Swank"],
  ["427ff312-d569-53c2-a7d7-2eb8dbf41b37", "Paul A Swank"],
  ["5d27bd4f-fb95-5364-88f0-4aef6bdc2422", "William A Swank"],
  ["044b7354-3fee-595a-9bd7-708c4870e94e", "David E Swanson"],
  ["d3ba048a-e197-5f90-8f14-f44837eba600", "Helen C Swanson"],
  ["bfea9036-7f70-5511-b915-9a9a5bd5c136", "John C Swanson"],
  ["787c4af9-a4c3-5820-831f-4f79cb549a3e", "Joseph E Swanson"],
  ["a81f7f88-2c1a-5303-af3c-dee96deebc96", "Raymond W Swanson"],
  ["40bfd075-e0ce-54f0-821f-c41d599f57f8", "Anthony I Swarowsky"],
  ["cffcba38-a8cf-5fe1-ae21-9a88f06ee1fd", "Harvey R Swarts"],
  ["ad45604e-a553-582c-b770-f8b1b5cc9bfc", "Anthony P Swartz"],
  ["5c4f6716-7192-5fcd-9a61-a39859e05756", "Jacobs R Swartz"],
  ["d39ac391-f0e5-516b-a120-4bffed927329", "Robert C Swartz"],
  ["1c765e0e-e385-5464-aa5c-c36787644da3", "Thomas J Swartz"],
  ["96fd44f3-f0c1-5f97-863b-248fa3f75a2f", "William E Swartzenburg"],
  ["a58739d6-74a7-5c8f-a055-267bf3c8c90c", "John A Swayze"],
  ["2ce81670-f2ec-5178-bf58-36cfa5c16e2a", "Victor H Swearingen"],
] as const;

test("Batch 933 publishes all 23 indexed-row entities with terminal outcomes", async ({ page }) => {
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

test("Lawrence Swank publishes West Point and the explicit engineer pathway without a civilian employer", async ({ request, page }) => {
  await page.goto("./people/0bf5a230-67ef-5df0-ba1b-8cd327338508/");
  const main = page.locator("main");
  await expect(main).toContainText("United States Military Academy");
  await expect(main).toContainText("United States Army Corps of Engineers");
  await expect(main).toContainText("explicit immediate");
  await expect(main).toContainText("military assignment");
  await expect(main).not.toContainText("Last civilian employer before wartime service");

  const response = await request.get("./data/people/l.json");
  const people = await response.json();
  const lawrence = people.find((item: { person_id: string }) => item.person_id === "0bf5a230-67ef-5df0-ba1b-8cd327338508");
  expect(lawrence.commissioned_officer).toBe(true);
  expect(lawrence.immediate_pre_oss_affiliations).toHaveLength(1);
  expect(lawrence.immediate_pre_oss_affiliations[0].relationship_type).toBe("military_assignment");
  expect(lawrence.last_civilian_pre_service).toHaveLength(0);
});

test("Paul Swank publishes the Camp Claiborne Army pathway and keeps Lawrence separate", async ({ request, page }) => {
  await page.goto("./people/427ff312-d569-53c2-a7d7-2eb8dbf41b37/");
  const main = page.locator("main");
  await expect(main).toContainText("Camp Claiborne");
  await expect(main).toContainText("United States Army");
  await expect(main).toContainText("First Lieutenant");
  await expect(main).toContainText("not related to Lawrence Swank");
  await expect(main).not.toContainText("Last civilian employer before wartime service");

  const response = await request.get("./data/people/p.json");
  const people = await response.json();
  const paul = people.find((item: { person_id: string }) => item.person_id === "427ff312-d569-53c2-a7d7-2eb8dbf41b37");
  expect(paul.commissioned_officer).toBe(true);
  expect(paul.immediate_pre_oss_affiliations).toHaveLength(1);
  expect(paul.immediate_pre_oss_affiliations[0].temporal_basis).toBe("explicit_immediate");
  expect(paul.last_civilian_pre_service).toHaveLength(0);
});

test("four Army findings remain occupation or student status only and employer-free", async ({ page }) => {
  for (const [id, phrase] of [
    ["5d27bd4f-fb95-5364-88f0-4aef6bdc2422", "Students"],
    ["1c765e0e-e385-5464-aa5c-c36787644da3", "Warehousing, storekeeping"],
    ["96fd44f3-f0c1-5f97-863b-248fa3f75a2f", "Students"],
    ["2ce81670-f2ec-5178-bf58-36cfa5c16e2a", "Chauffeurs and drivers"],
  ] as const) {
    await page.goto(`./people/${id}/`);
    const main = page.locator("main");
    await expect(main).toContainText(phrase);
    await expect(main).toContainText("no employer or workplace");
    await expect(main).toContainText("occupation only found");
    await expect(main).not.toContainText("Last civilian employer before wartime service");
  }
});

test("Thomas Swartz preserves the damaged grade without interpreting it", async ({ page }) => {
  await page.goto("./people/1c765e0e-e385-5464-aa5c-c36787644da3/");
  const main = page.locator("main");
  await expect(main).toContainText("damaged grade value PV0 is not interpreted");
  await expect(main).toContainText("unknown or indeterminate");
});

test("Anthony Swarowsky and Harvey Swarts expose conflicts without transferring identities", async ({ request, page }) => {
  await page.goto("./people/40bfd075-e0ce-54f0-821f-c41d599f57f8/");
  let main = page.locator("main");
  await expect(main).toContainText("materially different full name");
  await expect(main).toContainText("conflicting");
  await expect(main).not.toContainText("Last civilian employer before wartime service");

  await page.goto("./people/cffcba38-a8cf-5fe1-ae21-9a88f06ee1fd/");
  main = page.locator("main");
  await expect(main).toContainText("Fred S Watson Jr");
  await expect(main).toContainText("both entities remain separate");

  const harveyResponse = await request.get("./data/people/h.json");
  const harveyPeople = await harveyResponse.json();
  const harvey = harveyPeople.find((item: { person_id: string }) => item.person_id === "cffcba38-a8cf-5fe1-ae21-9a88f06ee1fd");
  const fredResponse = await request.get("./data/people/f.json");
  const fredPeople = await fredResponse.json();
  const fred = fredPeople.find((item: { person_id: string }) => item.person_id === "eb26f905-3ac1-562f-b6df-d3b617b95212");
  expect(harvey.identity_status).toBe("conflicting");
  expect(harvey.possible_duplicate_group).toMatch(/^duplicate-[0-9a-f]{12}$/);
  expect(harvey.possible_duplicate_group).toBe(fred.possible_duplicate_group);
});

test("Batch 933 does not change the evidence-defined oil-company category", async ({ page }) => {
  await page.goto("./oil-companies/");
  const main = page.locator("main");
  await expect(main).toContainText("14 people");
  await expect(main).toContainText("15 historically named");
  await expect(main).not.toContainText("Camp Claiborne");
});

test("Batch 933 evidence excludes credentials and protected identifier fields", () => {
  expect(evidence).not.toMatch(/"serial_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toMatch(/"service_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toContain("NARA_API_KEY");
  expect(evidence).not.toContain("x-api-key");
  expect(evidence).not.toMatch(/serial-conflict:\d/);
});

test("Batch 933 publishes its exact coverage counters", async ({ request }) => {
  const response = await request.get("./data/stats.json");
  expect(response.ok()).toBeTruthy();
  const stats = await response.json();
  expect(stats).toMatchObject({
    source_rows: 23_978,
    person_entities: 23_936,
    possible_duplicate_groups: 631,
    research_attempted_people: 14_405,
    verified_affiliation_people: 1_021,
    verified_employer_people: 460,
    archival_review_assessed_people: 12_878,
    published_claims: 8_871,
    public_sources: 5_851,
  });
});
