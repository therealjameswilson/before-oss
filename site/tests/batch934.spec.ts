import fs from "node:fs";
import { expect, test } from "@playwright/test";

const evidence = fs.readFileSync(
  new URL(
    "../../research/evidence-page457-james-a-sweatte-to-frank-l-sweetser-review_batch-934_2026-10-27.json",
    import.meta.url,
  ),
  "utf8",
);

const profiles = [
  ["0d7a18fb-d090-53ee-bc1a-fabc925f35c1", "James A Sweatte"],
  ["c136aa83-99a4-5012-8d3b-a7fe6f4b6205", "Bernard Swedloff"],
  ["59adfad9-f19b-54ad-936e-aacdc831ad1e", "Elizabeth Sweeka"],
  ["d6b51654-69c3-533c-93b4-ae95ba12d407", "Lois E Sweeley"],
  ["db758e9a-5aeb-5fda-8823-ffb3942ff064", "Barbara P Sweeney"],
  ["ae367bc5-46ff-5f52-8cb8-05f48c242ba3", "James S Sweeney"],
  ["f62adfa3-3bee-578d-a1d2-3b0aa552e622", "Joseph M Sweeney"],
  ["19544301-a933-5438-a865-c53b61a00169", "Joseph M Sweeney"],
  ["3b7319af-74d7-59fe-900a-2b3ab69c1c99", "Patrick J Sweeney"],
  ["3585ad1f-cdbd-5643-84f0-365e1dc43671", "Rae Sweeney"],
  ["07716dc8-d660-5f9b-a104-fb5f793c2787", "Robert G Sweeney"],
  ["2cabc942-d942-54ef-9a8c-1e1da1d4deeb", "Ruth E Sweeney"],
  ["10239687-5a89-5853-b0a5-3432b8094e3e", "Arabella Sweet"],
  ["0dcbdae1-4a16-5fca-bbd9-8ac24e9403b7", "Arthur P Sweet"],
  ["38f49725-f884-5673-af3c-d0177b454316", "Earl P Sweet"],
  ["e424a19b-9ebd-56b8-8940-ebc8f9cde496", "Florence H Sweet"],
  ["cb620f27-eab1-5efc-901c-2bd26fc0142f", "Joyeuse Sweet"],
  ["12efa622-83d0-5c8d-85f0-f86c4387b424", "Paul Sweet"],
  ["52839b7b-b20f-5e43-9d08-a869e5f6047f", "Paul R Sweet"],
  ["d302baf2-5f79-5d8c-bb24-c6e952a74aeb", "Paul R Sweet"],
  ["e282916a-cbf7-5f18-9e7f-b72c9c45ab7b", "Walden E Sweet"],
  ["0bc1344f-24f1-5892-8848-22294c9acdd7", "Adelaide V Sweetser"],
  ["046a86b6-7fbe-5a18-82dd-e52adb1b6957", "Frank L Sweetser"],
] as const;

test("Batch 934 publishes all 23 indexed-row entities with terminal outcomes", async ({ page }) => {
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

test("the two Joseph Sweeney rows stay separate and only row 30 receives the Army occupation", async ({ request, page }) => {
  await page.goto("./people/f62adfa3-3bee-578d-a1d2-3b0aa552e622/");
  let main = page.locator("main");
  await expect(main).toContainText("Secretaries");
  await expect(main).toContainText("no employer or workplace");
  await expect(main).toContainText("occupation only found");

  await page.goto("./people/19544301-a933-5438-a865-c53b61a00169/");
  main = page.locator("main");
  await expect(main).toContainText("different protected identifier from row 30");
  await expect(main).not.toContainText("Secretaries");

  const response = await request.get("./data/people/j.json");
  const people = await response.json();
  const accepted = people.find((item: { person_id: string }) => item.person_id === "f62adfa3-3bee-578d-a1d2-3b0aa552e622");
  const separate = people.find((item: { person_id: string }) => item.person_id === "19544301-a933-5438-a865-c53b61a00169");
  expect(accepted.person_id).not.toBe(separate.person_id);
  expect(accepted.other_pre_oss_affiliations[0].occupation).toBe("Secretaries");
  expect(separate.other_pre_oss_affiliations).toHaveLength(0);
});

test("three Army findings stay occupation-only and employer-free", async ({ page }) => {
  for (const [id, phrase] of [
    ["f62adfa3-3bee-578d-a1d2-3b0aa552e622", "Secretaries"],
    ["0dcbdae1-4a16-5fca-bbd9-8ac24e9403b7", "Retail managers"],
    ["38f49725-f884-5673-af3c-d0177b454316", "Nonprocess occupations in manufacturing"],
  ] as const) {
    await page.goto(`./people/${id}/`);
    const main = page.locator("main");
    await expect(main).toContainText(phrase);
    await expect(main).toContainText("no employer or workplace");
    await expect(main).not.toContainText("Last civilian employer before wartime service");
  }
});

test("Joyeuse Sweet publishes a qualified student affiliation and visible date disagreement", async ({ request, page }) => {
  await page.goto("./people/cb620f27-eab1-5efc-901c-2bd26fc0142f/");
  const main = page.locator("main");
  await expect(main).toContainText("Mount Holyoke College");
  await expect(main).toContainText("B.A. in Economics");
  await expect(main).toContainText("probable");
  await expect(main).toContainText("1923 versus 1922");
  await expect(main).not.toContainText("Last civilian employer before wartime service");

  const response = await request.get("./data/people/j.json");
  const people = await response.json();
  const joyeuse = people.find((item: { person_id: string }) => item.person_id === "cb620f27-eab1-5efc-901c-2bd26fc0142f");
  expect(joyeuse.identity_status).toBe("probable");
  expect(joyeuse.other_pre_oss_affiliations[0].relationship_type).toBe("student");
  expect(joyeuse.last_civilian_pre_service).toHaveLength(0);
});

test("Dr Paul Sweet publishes Bates while the no-rank row remains separate", async ({ request, page }) => {
  await page.goto("./people/52839b7b-b20f-5e43-9d08-a869e5f6047f/");
  let main = page.locator("main");
  await expect(main).toContainText("Bates College");
  await expect(main).toContainText("Professor of German history");
  await expect(main).toContainText("Last civilian employer before service");
  await expect(main).toContainText("exact leave, separation and transition dates not stated");

  await page.goto("./people/d302baf2-5f79-5d8c-bb24-c6e952a74aeb/");
  main = page.locator("main");
  await expect(main).toContainText("Do not merge the printed rows");
  await expect(main).not.toContainText("Bates College");

  const response = await request.get("./data/people/p.json");
  const people = await response.json();
  const doctor = people.find((item: { person_id: string }) => item.person_id === "52839b7b-b20f-5e43-9d08-a869e5f6047f");
  const noRank = people.find((item: { person_id: string }) => item.person_id === "d302baf2-5f79-5d8c-bb24-c6e952a74aeb");
  expect(doctor.possible_duplicate_group).toMatch(/^duplicate-[0-9a-f]{12}$/);
  expect(doctor.possible_duplicate_group).toBe(noRank.possible_duplicate_group);
  expect(doctor.last_civilian_pre_service[0].canonical_organization).toBe("Bates College");
  expect(noRank.last_civilian_pre_service).toHaveLength(0);
});

test("Frank Sweetser separates Columbia student status from WRA employment", async ({ request, page }) => {
  await page.goto("./people/046a86b6-7fbe-5a18-82dd-e52adb1b6957/");
  const main = page.locator("main");
  await expect(main).toContainText("War Relocation Authority");
  await expect(main).toContainText("Initial assistant director");
  await expect(main).toContainText("Columbia University");
  await expect(main).toContainText("Doctoral student");
  await expect(main).toContainText("Navy-to-OSS sequence");

  const response = await request.get("./data/people/f.json");
  const people = await response.json();
  const frank = people.find((item: { person_id: string }) => item.person_id === "046a86b6-7fbe-5a18-82dd-e52adb1b6957");
  expect(frank.commissioned_officer).toBe(true);
  expect(frank.last_civilian_pre_service[0].canonical_organization).toBe("War Relocation Authority");
  expect(frank.last_civilian_pre_service[0].relationship_type).toBe("employment");
  expect(frank.other_pre_oss_affiliations[0].relationship_type).toBe("student");
  expect(frank.immediate_pre_oss_affiliations).toHaveLength(0);
});

test("Batch 934 does not change the evidence-defined oil-company category", async ({ page }) => {
  await page.goto("./oil-companies/");
  const main = page.locator("main");
  await expect(main).toContainText("14 people");
  await expect(main).toContainText("15 historically named");
  await expect(main).not.toContainText("Bates College");
  await expect(main).not.toContainText("War Relocation Authority");
});

test("Batch 934 evidence excludes credentials and protected identifier fields", () => {
  expect(evidence).not.toMatch(/"serial_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toMatch(/"service_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toContain("NARA_API_KEY");
  expect(evidence).not.toContain("x-api-key");
  expect(evidence).not.toMatch(/serial-conflict:\d/);
});

test("Batch 934 publishes its exact coverage counters", async ({ request }) => {
  const response = await request.get("./data/stats.json");
  expect(response.ok()).toBeTruthy();
  const stats = await response.json();
  expect(stats).toMatchObject({
    source_rows: 23_978,
    person_entities: 23_936,
    possible_duplicate_groups: 632,
    research_attempted_people: 14_428,
    verified_affiliation_people: 1_023,
    verified_employer_people: 462,
    archival_review_assessed_people: 12_901,
    published_claims: 8_884,
    public_sources: 5_863,
  });
});
