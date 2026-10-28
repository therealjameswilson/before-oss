import fs from "node:fs";
import { expect, test } from "@playwright/test";

const evidence = fs.readFileSync(
  new URL(
    "../../research/evidence-page456-erwin-summers-to-stanley-sussman-review_batch-931_2026-10-27.json",
    import.meta.url,
  ),
  "utf8",
);

const profiles = [
  ["4daa22b0-e89a-584f-9fdd-d6f0844ce444", "Erwin Summers"],
  ["ea50bf7f-1db6-5a7c-a3d4-d995fa57cb38", "Homer B Summers"],
  ["2df6b26f-bc5c-5425-b7eb-6eea2867abbd", "James Summers"],
  ["d3903566-15af-5cb0-b5ab-12173aa55d82", "John W Summers"],
  ["865a5f77-6cd7-53cd-8dbc-13d3f250c0d7", "John W Summers"],
  ["35f0de37-8be4-52a9-897a-31b605d67dcc", "John B Summers"],
  ["2a15173f-ca36-5c22-b8cd-71478bb2ee3e", "Edna J Sumner"],
  ["4cdd937a-61a3-5c56-9d6f-35351acc2f81", "H Y Sun"],
  ["30736fc0-734c-5937-9365-8f8e5bd4d109", "Robert G Sunday"],
  ["2ccc5346-c6be-5483-902c-76e746d56d9a", "John Sunde"],
  ["b1f9485b-168d-5690-adeb-05394faba3dd", "Jane Sunderland"],
  ["49316a03-2fd8-5f57-a31f-eec022045a15", "Jeanne M Sunderland"],
  ["af893820-db8e-5698-8228-4f385cce5203", "Ragnor N Sundstrom"],
  ["b2fb9b93-9d75-5200-93c9-a6e034e5a076", "Edward S Sununu"],
  ["4b65b46a-0828-5e7a-ba12-68b42aeb27b5", "Konthi Suphamonkol"],
  ["96b42951-d1f0-551c-8efb-ba2d5c28c4f6", "Joan Supple"],
  ["3f4b84e9-9d41-564d-adc6-d1f6e015496a", "Dorothy E Suratt"],
  ["1a4c02a6-5f44-5ebd-9661-a3f511e2cbb3", "Sang P Surh"],
  ["3bad49d2-d74d-5ddf-95cd-b5d687259a50", "Harold A Surle"],
  ["afe4fe93-57d8-55aa-af8d-9e11aeeee672", "Julian C Suso"],
  ["997be5df-41cb-5785-9204-6f44face8b6e", "Carl L Sussman"],
  ["e1c0bc96-2d4b-5e13-a131-d4bec64fa6d3", "Harvey S Sussman"],
  ["0661f296-5917-572d-abc3-c2673294b974", "Stanley Sussman"],
] as const;

test("Batch 931 publishes all 23 people with terminal outcomes and masked identifiers", async ({ page }) => {
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

test("seven Army records remain occupation-only and employer-free", async ({ page }) => {
  for (const [id, occupation] of [
    ["ea50bf7f-1db6-5a7c-a3d4-d995fa57cb38", "Linemen and servicemen"],
    ["2df6b26f-bc5c-5425-b7eb-6eea2867abbd", "Firemen, other than process firemen"],
    ["35f0de37-8be4-52a9-897a-31b605d67dcc", "Accountants and auditors"],
    ["30736fc0-734c-5937-9365-8f8e5bd4d109", "Machine-shop and related occupations"],
    ["2ccc5346-c6be-5483-902c-76e746d56d9a", "Occupations in fabrication of metal products"],
    ["997be5df-41cb-5785-9204-6f44face8b6e", "Photographers"],
    ["e1c0bc96-2d4b-5e13-a131-d4bec64fa6d3", "Managers and officials"],
  ] as const) {
    await page.goto(`./people/${id}/`);
    const main = page.locator("main");
    await expect(main).toContainText(occupation);
    await expect(main).toContainText("no employer or workplace");
    await expect(main).toContainText("occupation only found");
    await expect(main).not.toContainText("Last civilian employer before wartime service");
  }
});

test("Konthi publishes documented education and government roles without inventing an immediate employer", async ({ page }) => {
  await page.goto("./people/4b65b46a-0828-5e7a-ba12-68b42aeb27b5/");
  const main = page.locator("main");
  await expect(main).toContainText("Konthi Suphamongkhon");
  await expect(main).toContainText("University of Moral and Political Sciences");
  await expect(main).toContainText("University of Paris");
  await expect(main).toContainText("Chief of Section, Political Division");
  await expect(main).toContainText("Embassy of Thailand, Tokyo");
  await expect(main).toContainText("Lecturer on public finance");
  await expect(main).toContainText("Free Thai Movement");
  await expect(main).toContainText("requires archival review");
  await expect(main).toContainText("No reviewed claim currently meets the publication threshold");
  await expect(main).toContainText("A single last civilian employer before wartime or military service has not yet been established");
});

test("Konthi organization records preserve historical names and relationship types", async ({ request }) => {
  const response = await request.get("./data/people/k.json");
  const people = await response.json();
  const konthi = people.find((item: { person_id: string }) => item.person_id === "4b65b46a-0828-5e7a-ba12-68b42aeb27b5");
  expect(konthi).toBeTruthy();
  expect(konthi.allied_or_foreign_personnel).toBe(true);
  expect(konthi.immediate_pre_oss_affiliations).toHaveLength(0);
  expect(konthi.last_civilian_pre_service).toHaveLength(0);
  expect(konthi.other_pre_oss_affiliations).toHaveLength(5);
  expect(konthi.other_pre_oss_affiliations.filter((item: { relationship_type: string }) => item.relationship_type === "student")).toHaveLength(2);
  expect(konthi.other_pre_oss_affiliations.filter((item: { relationship_type: string }) => item.relationship_type === "government_assignment")).toHaveLength(2);
  expect(konthi.other_pre_oss_affiliations.filter((item: { relationship_type: string }) => item.relationship_type === "employment")).toHaveLength(1);
});

test("the two John W Summers rows remain separate in one review group", async ({ request }) => {
  const response = await request.get("./data/people/j.json");
  const people = await response.json();
  const johns = people.filter((item: { display_name: string }) => item.display_name === "John W Summers");
  expect(johns).toHaveLength(2);
  expect(new Set(johns.map((item: { possible_duplicate_group: string }) => item.possible_duplicate_group)).size).toBe(1);
  expect(johns.every((item: { research_status: string }) => item.research_status === "requires_archival_review")).toBeTruthy();
  expect(johns.every((item: { identity_status: string }) => item.identity_status === "ambiguous")).toBeTruthy();
});

test("Sang Surh and Stanley Sussman retain conflicts without occupations", async ({ page }) => {
  await page.goto("./people/1a4c02a6-5f44-5ebd-9661-a3f511e2cbb3/");
  let main = page.locator("main");
  await expect(main).toContainText("conflicting");
  await expect(main).toContainText("Charles M Joe");
  await expect(main).toContainText("protected identifier");
  await expect(main).not.toContainText("Semiprofessional occupations");

  await page.goto("./people/0661f296-5917-572d-abc3-c2673294b974/");
  main = page.locator("main");
  await expect(main).toContainText("conflicting");
  await expect(main).toContainText("damaged name");
  await expect(main).toContainText("identity and occupation remain unassigned");
  await expect(main).not.toContainText("Students");
});

test("the Box 758 to 759 boundary and SI note remain recoverable", async ({ page }) => {
  await page.goto("./people/3bad49d2-d74d-5ddf-95cd-b5d687259a50/");
  let main = page.locator("main");
  await expect(main).toContainText("Box 759");

  await page.goto("./people/afe4fe93-57d8-55aa-af8d-9e11aeeee672/");
  main = page.locator("main");
  await expect(main).toContainText("Box 759");
  await expect(main).toContainText("SI");
  await expect(main).toContainText("not expanded");
});

test("Batch 931 does not change the evidence-defined oil-company category", async ({ page }) => {
  await page.goto("./oil-companies/");
  const main = page.locator("main");
  await expect(main).toContainText("14 people");
  await expect(main).toContainText("15 historically named");
  await expect(main).not.toContainText("Ministry of Foreign Affairs, Siam");
});

test("Batch 931 evidence excludes credentials and protected identifier fields", () => {
  expect(evidence).not.toMatch(/"serial_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toMatch(/"service_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toContain("NARA_API_KEY");
  expect(evidence).not.toContain("x-api-key");
  expect(evidence).not.toMatch(/serial-conflict:\d/);
});

test("Batch 931 publishes its exact coverage counters", async ({ request }) => {
  const response = await request.get("./data/stats.json");
  expect(response.ok()).toBeTruthy();
  const stats = await response.json();
  expect(stats).toMatchObject({
    source_rows: 23_978,
    person_entities: 23_936,
    possible_duplicate_groups: 631,
    research_attempted_people: 14_360,
    verified_affiliation_people: 1_018,
    verified_employer_people: 459,
    archival_review_assessed_people: 12_833,
    published_claims: 8_825,
    public_sources: 5_833,
  });
});
