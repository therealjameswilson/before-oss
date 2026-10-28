import fs from "node:fs";
import { expect, test } from "@playwright/test";

const evidence = fs.readFileSync(
  new URL(
    "../../research/evidence-page458-edward-d-sybesma-to-stanley-f-szalamacha-review_batch-936_2026-10-27.json",
    import.meta.url,
  ),
  "utf8",
);

const profiles = [
  ["418b8496-43ce-5d57-ba83-66846184d412", "Edward D Sybesma"],
  ["2a52849b-107a-5323-8ac2-cd904d10d7d7", "George M Sylvester"],
  ["1ba6a73b-384d-529d-b0be-98ffaa474216", "Loren H Sylvester"],
  ["d51e9ca8-2451-55db-9884-0a4087d89e78", "Richard C Sylvester"],
  ["f344b7eb-15cf-5e29-be0b-560a0944bbd2", "Stephen J Symanski"],
  ["16ec2597-787b-5430-bb98-b83c28508d64", "Louise Syminyon"],
  ["edb4cff2-1aef-52ac-bb58-a19115af6e2c", "Percival M Symonds"],
  ["0faa01df-72cc-5ec9-9ba0-73347161a55a", "Sidney L Symons"],
  ["125350a5-bab1-5917-81c2-7a28a22f794d", "Fryderyk Synowiec"],
  ["102b2653-669a-5c85-8d6f-b90832a06d73", "Willem K Sypesteyn"],
  ["74c91ced-6cbb-50e5-a9e8-a907707b21ec", "William K Sypesteyn"],
  ["100e38c5-bc8e-5fca-80b6-be988adcb44a", "John W Syphax"],
  ["04556319-8777-5a62-b9d7-7fe2ef158c19", "Ganna M Syro-Boiarsky"],
  ["75c7db38-481e-593b-a784-d054ebc68582", "Morris A Syrstad"],
  ["7a11d7e0-ee8f-5199-86e9-e5f4c99c5dc9", "Stephen J Sysko"],
  ["fcfea34a-7168-5376-b507-a09d9df29740", "Stevan J Sysko"],
  ["2273a4dd-11de-509c-9631-b3498cad2756", "Bertha B Syverud"],
  ["c38713db-05d0-5cf2-a5bd-6f1e7c5d50a8", "Kie Syzdek"],
  ["6e48695f-4e86-52d8-b1ae-2e754ca0bef5", "George M Szabad"],
  ["33908893-ab7a-5d9e-b705-c78866ae3f4e", "Kalman L Szabo"],
  ["1b13a8d4-f5f2-5bf6-8cc1-d144b498659e", "Kazmer J Szabo"],
  ["2dc317c8-8b94-56e3-9778-08d8d1c2e254", "Edward M Szachowicz"],
  ["3709a6cd-b7d5-5701-b630-8996171e1bf9", "Stanley F Szalamacha"],
] as const;

test("Batch 936 publishes all 23 indexed-row entities with terminal outcomes", async ({ page }) => {
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

test("Willem and William Sypesteyn stay separate and only Willem receives official evidence", async ({ request, page }) => {
  await page.goto("./people/102b2653-669a-5c85-8d6f-b90832a06d73/");
  let main = page.locator("main");
  await expect(main).toContainText("Semiprofessional occupations, n.e.c.");
  await expect(main).toContainText("official OSS commendation");
  await expect(main).toContainText("no employer or workplace");

  await page.goto("./people/74c91ced-6cbb-50e5-a9e8-a907707b21ec/");
  main = page.locator("main");
  await expect(main).toContainText("remain separate people");
  await expect(main).not.toContainText("Semiprofessional occupations, n.e.c.");

  const response = await request.get("./data/people/w.json");
  const people = await response.json();
  const willem = people.find((item: { person_id: string }) => item.person_id === "102b2653-669a-5c85-8d6f-b90832a06d73");
  const william = people.find((item: { person_id: string }) => item.person_id === "74c91ced-6cbb-50e5-a9e8-a907707b21ec");
  expect(willem.person_id).not.toBe(william.person_id);
  expect(willem.possible_duplicate_group).toMatch(/^duplicate-[0-9a-f]{12}$/);
  expect(willem.possible_duplicate_group).toBe(william.possible_duplicate_group);
  expect(willem.other_pre_oss_affiliations[0].occupation).toBe("Semiprofessional occupations, n.e.c.");
  expect(william.other_pre_oss_affiliations).toHaveLength(0);
});

test("John Syphax publishes Howard as qualified earlier work, not an immediate or last employer", async ({ request, page }) => {
  await page.goto("./people/100e38c5-bc8e-5fca-80b6-be988adcb44a/");
  const main = page.locator("main");
  await expect(main).toContainText("Howard University");
  await expect(main).toContainText("Political science teacher");
  await expect(main).toContainText("1936–1938");
  await expect(main).not.toContainText("Last civilian employer before wartime service");

  const response = await request.get("./data/people/j.json");
  const people = await response.json();
  const john = people.find((item: { person_id: string }) => item.person_id === "100e38c5-bc8e-5fca-80b6-be988adcb44a");
  expect(john.identity_status).toBe("high_confidence");
  expect(john.other_pre_oss_affiliations[0].canonical_organization).toBe("Howard University");
  expect(john.other_pre_oss_affiliations[0].claim_confidence).toBe("medium");
  expect(john.immediate_pre_oss_affiliations).toHaveLength(0);
  expect(john.last_civilian_pre_service).toHaveLength(0);
});

test("Ganna Syro-Boiarsky keeps a probable qualified secretary role and no invented organization", async ({ request, page }) => {
  await page.goto("./people/04556319-8777-5a62-b9d7-7fe2ef158c19/");
  const main = page.locator("main");
  await expect(main).toContainText("Ganna Mahrt Syro-Boiarsky");
  await expect(main).toContainText("Secretary to General John F. O'Ryan");
  await expect(main).toContainText("probable");
  await expect(main).not.toContainText("Last civilian employer before wartime service");

  const response = await request.get("./data/people/g.json");
  const people = await response.json();
  const ganna = people.find((item: { person_id: string }) => item.person_id === "04556319-8777-5a62-b9d7-7fe2ef158c19");
  expect(ganna.identity_status).toBe("probable");
  expect(ganna.other_pre_oss_affiliations[0].role_title).toContain("General John F. O'Ryan");
  expect(ganna.other_pre_oss_affiliations[0].canonical_organization).toBeNull();
  expect(ganna.immediate_pre_oss_affiliations).toHaveLength(0);
  expect(ganna.last_civilian_pre_service).toHaveLength(0);
});

test("Morris Syrstad publishes a qualified 99th Infantry pathway and no civilian employer", async ({ request, page }) => {
  await page.goto("./people/75c7db38-481e-593b-a784-d054ebc68582/");
  const main = page.locator("main");
  await expect(main).toContainText("99th Infantry Battalion (Separate)");
  await expect(main).toContainText("NORSO II");
  await expect(main).toContainText("probable immediate");
  await expect(main).not.toContainText("Last civilian employer before wartime service");

  const response = await request.get("./data/people/m.json");
  const people = await response.json();
  const morris = people.find((item: { person_id: string }) => item.person_id === "75c7db38-481e-593b-a784-d054ebc68582");
  expect(morris.identity_status).toBe("confirmed");
  expect(morris.immediate_pre_oss_affiliations[0].relationship_type).toBe("military_assignment");
  expect(morris.immediate_pre_oss_affiliations[0].temporal_basis).toBe("probable_immediate");
  expect(morris.immediate_pre_oss_affiliations[0].claim_confidence).toBe("medium");
  expect(morris.last_civilian_pre_service).toHaveLength(0);
});

test("five Army categories remain occupation-only and employer-free", async ({ page }) => {
  for (const [id, phrase] of [
    ["1ba6a73b-384d-529d-b0be-98ffaa474216", "Stock clerks"],
    ["102b2653-669a-5c85-8d6f-b90832a06d73", "Semiprofessional occupations, n.e.c."],
    ["fcfea34a-7168-5376-b507-a09d9df29740", "Occupations in manufacture of paper goods"],
    ["c38713db-05d0-5cf2-a5bd-6f1e7c5d50a8", "Bakers"],
    ["6e48695f-4e86-52d8-b1ae-2e754ca0bef5", "Lawyers and judges"],
  ] as const) {
    await page.goto(`./people/${id}/`);
    const main = page.locator("main");
    await expect(main).toContainText(phrase);
    await expect(main).toContainText("no employer or workplace");
    await expect(main).not.toContainText("Last civilian employer before wartime service");
  }
});

test("Stevan and Stephen Sysko stay separate while the Steven variant remains searchable", async ({ request, page }) => {
  await page.goto("./people/fcfea34a-7168-5376-b507-a09d9df29740/");
  let main = page.locator("main");
  await expect(page.getByRole("heading", { name: "Stevan J Sysko", level: 1 })).toBeVisible();
  await expect(main).toContainText("Steven J Sysko");
  await expect(main).toContainText("Occupations in manufacture of paper goods");

  await page.goto("./people/7a11d7e0-ee8f-5199-86e9-e5f4c99c5dc9/");
  main = page.locator("main");
  await expect(main).toContainText("remain separate people");
  await expect(main).not.toContainText("Occupations in manufacture of paper goods");

  const response = await request.get("./data/people/s.json");
  const people = await response.json();
  const stevan = people.find((item: { person_id: string }) => item.person_id === "fcfea34a-7168-5376-b507-a09d9df29740");
  const stephen = people.find((item: { person_id: string }) => item.person_id === "7a11d7e0-ee8f-5199-86e9-e5f4c99c5dc9");
  expect(stevan.name_variants).toContain("Steven J Sysko");
  expect(stevan.possible_duplicate_group).toBe(stephen.possible_duplicate_group);
  expect(stephen.other_pre_oss_affiliations).toHaveLength(0);
});

test("Stanley Szalamacha exposes the source conflict and receives no Army occupation", async ({ request, page }) => {
  await page.goto("./people/3709a6cd-b7d5-5701-b630-8996171e1bf9/");
  const main = page.locator("main");
  await expect(main).toContainText("source conflict");
  await expect(main).toContainText("conflicting sources");
  await expect(main).not.toContainText("Attendants, hospitals");

  const response = await request.get("./data/people/s.json");
  const people = await response.json();
  const stanley = people.find((item: { person_id: string }) => item.person_id === "3709a6cd-b7d5-5701-b630-8996171e1bf9");
  expect(stanley.identity_status).toBe("conflicting");
  expect(stanley.other_pre_oss_affiliations).toHaveLength(0);
  expect(stanley.immediate_pre_oss_affiliations).toHaveLength(0);
  expect(stanley.last_civilian_pre_service).toHaveLength(0);
});

test("Batch 936 does not change the evidence-defined oil-company category", async ({ page }) => {
  await page.goto("./oil-companies/");
  const main = page.locator("main");
  await expect(main).toContainText("14 people");
  await expect(main).toContainText("15 historically named");
  await expect(main).not.toContainText("Howard University");
  await expect(main).not.toContainText("99th Infantry Battalion");
});

test("Batch 936 evidence excludes credentials and protected identifier fields", () => {
  expect(evidence).not.toMatch(/"serial_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toMatch(/"service_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toContain("NARA_API_KEY");
  expect(evidence).not.toContain("x-api-key");
  expect(evidence).not.toMatch(/serial-conflict:\d/);
});

test("Batch 936 publishes its exact coverage counters", async ({ request }) => {
  const response = await request.get("./data/stats.json");
  expect(response.ok()).toBeTruthy();
  const stats = await response.json();
  expect(stats).toMatchObject({
    source_rows: 23_978,
    person_entities: 23_936,
    possible_duplicate_groups: 634,
    research_attempted_people: 14_472,
    verified_affiliation_people: 1_024,
    verified_employer_people: 463,
    archival_review_assessed_people: 12_945,
    published_claims: 8_917,
    public_sources: 5_882,
  });
});
