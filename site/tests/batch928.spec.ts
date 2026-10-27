import fs from "node:fs";
import { expect, test } from "@playwright/test";

const evidence = fs.readFileSync(
  new URL(
    "../../research/evidence-page454-donald-b-sturtevant-to-pearl-e-sugerman-review_batch-928_2026-10-27.json",
    import.meta.url,
  ),
  "utf8",
);

const profiles = [
  ["05f86065-b7d2-59da-a5df-e5585608b028", "Donald B Sturtevant"],
  ["87a79df2-11c7-5a7a-b694-c3ce1e6b6f49", "Warren B Sturtevant"],
  ["90d1c4fb-99b4-54b6-b0a6-1f348a055535", "Warren Stutler"],
  ["04f65c85-7d87-513c-ae7d-91942da15d9c", "Carl A Stutz"],
  ["bd4e5dd6-6147-54e2-a7f3-a10f9bc086fd", "Sherwood S Stutz"],
  ["e2e0804f-ed19-57d7-a501-39422a01e10a", "Duane H Stutzman"],
  ["b45dfb7f-0ee5-5197-9577-89ade3f34693", "Alan R Stuyvesant"],
  ["b1065589-d21a-50cb-ade6-ff326413ff71", "John H Styer"],
  ["26f6008b-fb70-500b-89b3-0a51aa7e9cf6", "Mitchell Styma"],
  ["39a5e6cf-0a32-5641-b2df-4c895e8ef402", "Peter A Stymfal"],
  ["8d36048e-55b5-54fb-8a1f-9f04f64a1583", "Lauritz E Styve"],
  ["8bb20ea2-0b9f-5b23-9bf3-2823930fcb1e", "Ju Sung Su"],
  ["c9aa82ba-73de-5616-8645-4df4c4f39a2e", "Alfred M Suarez"],
  ["b3b31bb1-f477-5a28-96eb-1d69a1df1201", "Robert Suarez"],
  ["ade8798b-d25b-57f6-b47c-49c026f0ed97", "Nicholas M Suban"],
  ["936f8c8c-5b71-5892-b0e3-964fe595412b", "Sukontha B Subhats"],
  ["395cf2ec-41c3-516e-989b-6a49e983543c", "Vivian B. Suchards"],
  ["670c1d13-5f3f-5cf5-a261-9de3acb32552", "Carlos V Sucre"],
  ["5a43db91-5b7d-513e-b8a2-5df17c517288", "Piscot Sudasna"],
  ["0b2bf8f8-0fd8-51f8-8723-aa2c6b37111a", "Kay K Sugahara"],
  ["630c03c4-c927-5520-986c-07339921cf4d", "Kelichi K Sugahara"],
  ["c4cad75d-0f5e-5d9a-9898-879ded80aad3", "Tomio Sugano"],
  ["1a4e3c57-6db8-504c-aad9-e93363f1925b", "Pearl E Sugerman"],
] as const;

test("Batch 928 publishes all 23 people with terminal outcomes and masked identifiers", async ({ page }) => {
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

test("Kay Sugahara publishes the named customs brokerage as last civilian work", async ({ page }) => {
  await page.goto("./people/0b2bf8f8-0fd8-51f8-8723-aa2c6b37111a/");
  const main = page.locator("main");
  await expect(main).toContainText("Kay Keiichi Sugahara");
  await expect(main).toContainText("Universal Foreign Service Company");
  await expect(main).toContainText("founder and owner");
  await expect(main).toContainText("customs broker");
  await expect(main).toContainText("Last civilian employer before service");
  await expect(main).toContainText("About – Sugahara Project");
  await expect(main).toContainText("Japanese-American Service Members");
  await expect(main).toContainText("verified employer found");
});

test("Kay and Kelichi Sugahara remain separate and only Kay receives the employer", async ({ request, page }) => {
  const response = await request.get("./data/people/k.json");
  const people = await response.json();
  const ids = [
    "0b2bf8f8-0fd8-51f8-8723-aa2c6b37111a",
    "630c03c4-c927-5520-986c-07339921cf4d",
  ] as const;
  const rows = people.filter((item: { person_id: string }) =>
    (ids as readonly string[]).includes(item.person_id),
  );
  expect(rows).toHaveLength(2);
  expect(rows[0].possible_duplicate_group).toBe(rows[1].possible_duplicate_group);
  const kay = rows.find((item: { person_id: string }) => item.person_id === ids[0]);
  const kelichi = rows.find((item: { person_id: string }) => item.person_id === ids[1]);
  expect(kay.last_civilian_pre_service).toHaveLength(1);
  expect(kelichi.last_civilian_pre_service).toEqual([]);
  expect(kelichi.other_pre_oss_affiliations).toEqual([]);

  await page.goto(`./people/${ids[1]}/`);
  const main = page.locator("main");
  await expect(main).toContainText("Possible duplicate group");
  await expect(main).toContainText("requires archival review");
  await expect(main).not.toContainText("Universal Foreign Service Company");
  await expect(page.locator(`a[href*="/people/${ids[0]}/"]`)).toContainText("Kay K Sugahara");
});

test("Mitchell Styma separates documented courier work from the Army occupation category", async ({ page }) => {
  await page.goto("./people/26f6008b-fb70-500b-89b3-0a51aa7e9cf6/");
  const main = page.locator("main");
  await expect(main).toContainText("confirmed");
  await expect(main).toContainText("courier runs to Lisbon");
  await expect(main).toContainText("Machine shop and related occupations, n.e.c.");
  await expect(main).toContainText("Yugoslavia Country Reader");
  await expect(main).toContainText("OSS citations and related records");
  await expect(main).toContainText("occupation only found");
  await expect(main).toContainText("No reviewed claim currently meets the publication threshold");
});

test("Peter Stymfal and Carlos Sucre keep employer-free Army categories qualified", async ({ page }) => {
  for (const [id, occupation, source] of [
    ["39a5e6cf-0a32-5641-b2df-4c895e8ef402", "Students", "Athens personnel list of 1 January 1945"],
    ["670c1d13-5f3f-5cf5-a261-9de3acb32552", "Wholesale managers", "NARA Compiled Code Lists"],
  ] as const) {
    await page.goto(`./people/${id}/`);
    const main = page.locator("main");
    await expect(main).toContainText(occupation);
    await expect(main).toContainText(source);
    await expect(main).toContainText("no employer");
    await expect(main).toContainText("occupation only found");
  }
  await expect(page.locator("main")).toContainText("Carlos U Sucre");
});

test("Carl Stutz keeps undefined Army code 047 out of public affiliations", async ({ request, page }) => {
  const response = await request.get("./data/people/c.json");
  const people = await response.json();
  const person = people.find((item: { person_id: string }) =>
    item.person_id === "04f65c85-7d87-513c-ae7d-91942da15d9c"
  );
  expect(person.immediate_pre_oss_affiliations).toEqual([]);
  expect(person.last_civilian_pre_service).toEqual([]);
  expect(person.other_pre_oss_affiliations).toEqual([]);
  await page.goto("./people/04f65c85-7d87-513c-ae7d-91942da15d9c/");
  await expect(page.locator("main")).toContainText("code 047 remains uninterpreted");
});

test("postwar oil activity does not add Kay Sugahara to the oil-company category", async ({ page }) => {
  await page.goto("./oil-companies/");
  const main = page.locator("main");
  await expect(main).toContainText("14 people");
  await expect(main).toContainText("15 historically named");
  await expect(main).not.toContainText("Kay K Sugahara");
  await expect(main).not.toContainText("Universal Foreign Service Company");
});

test("Batch 928 evidence excludes credentials and protected identifier fields", () => {
  expect(evidence).not.toMatch(/"serial_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toMatch(/"service_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toContain("NARA_API_KEY");
  expect(evidence).not.toContain("x-api-key");
});

test("Batch 928 publishes its exact coverage counters", async ({ request }) => {
  const response = await request.get("./data/stats.json");
  expect(response.ok()).toBeTruthy();
  const stats = await response.json();
  expect(stats).toMatchObject({
    source_rows: 23_978,
    person_entities: 23_936,
    possible_duplicate_groups: 628,
    research_attempted_people: 14_291,
    verified_affiliation_people: 1_014,
    verified_employer_people: 458,
    archival_review_assessed_people: 12_764,
    published_claims: 8_768,
    public_sources: 5_806,
  });
});
