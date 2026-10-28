import fs from "node:fs";
import { expect, test } from "@playwright/test";

const evidence = fs.readFileSync(
  new URL(
    "../../research/evidence-page458-paul-m-sweezy-to-ardeth-g-swoyer-review_batch-935_2026-10-27.json",
    import.meta.url,
  ),
  "utf8",
);

const profiles = [
  ["ead0d460-6fcd-51cd-a6d4-01862ecc82f8", "Paul M Sweezy"],
  ["8686bb8e-3b16-5aa2-bb72-bdd2e6a6f3aa", "Paul M Sweezy"],
  ["c9b7d9f5-98f1-59a1-8e0a-8d643f54c836", "William H Sweezy"],
  ["42e969fc-831d-5694-8def-3fa1ae9bc063", "Thomas T Sweigart"],
  ["a2761d25-38eb-5bb3-adb5-888b7e86b976", "Mildred M Sweiven"],
  ["b32bda9e-0f87-5349-8295-5eed630cf55e", "James J Swensen"],
  ["5e771570-d7a2-5818-bc1b-d11f552dd40a", "John W Swensen"],
  ["47405c7a-b8cb-518d-9c10-efe83bc67588", "Sigurd M Swenson"],
  ["8754c3cd-4deb-59a1-bb64-a27660fc132c", "Judith Swerdloff"],
  ["1f497093-a7d0-52a4-8850-62bacd564f87", "John W Swetish"],
  ["2ce271ea-ff12-53f1-b078-e4641e595135", "Andrew L Swider"],
  ["a3672823-a79c-5c58-b74e-71f94571ecf2", "Gertrude T Swidler"],
  ["4c018d36-d9e1-54dc-8b94-79ff9bf1636d", "Henry R Swierat"],
  ["e9dc5d67-dbf5-51a9-8805-17111ba5b93e", "Carleton B Swift"],
  ["f9095d98-30c0-5d33-8bc6-480b69fee15c", "Frank R Swift"],
  ["b37cbcdc-c931-5136-902f-636a7dcd3881", "Helen G Swift"],
  ["d28f5516-3542-5fb6-a6b9-6931d7b69c2d", "John L Swift"],
  ["706ed1af-148d-5ea7-bd31-1cc6468955c5", "Robert S Swift"],
  ["6edd27e8-41b1-5b78-a5b9-71ad5f4e0b5b", "Walter S Swift"],
  ["c8d7ec94-a521-5ca1-85c8-1908acdddb91", "Richard M Swinhart"],
  ["c92f224b-0f73-57c8-918a-b93ffe1fac0b", "Marion A Swiss"],
  ["b47f4bff-6090-505d-88d0-c4a89900d368", "Alfred R Switgall"],
  ["f77f5aea-ea0d-5cc6-8c5b-dc8c29ac1b4d", "Ardeth G Swoyer"],
] as const;

test("Batch 935 publishes all 23 indexed-row entities with terminal outcomes", async ({ page }) => {
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

test("Paul Sweezy publishes Harvard and Army only on the supported row", async ({ request, page }) => {
  await page.goto("./people/ead0d460-6fcd-51cd-a6d4-01862ecc82f8/");
  let main = page.locator("main");
  await expect(main).toContainText("Harvard University");
  await expect(main).toContainText("Assistant Professor of Economics");
  await expect(main).toContainText("United States Army");
  await expect(main).toContainText("taken from the Army into the intelligence apparatus");

  await page.goto("./people/8686bb8e-3b16-5aa2-bb72-bdd2e6a6f3aa/");
  main = page.locator("main");
  await expect(main).toContainText("different protected identifiers");
  await expect(main).not.toContainText("Harvard University");
  await expect(main).not.toContainText("United States Army");

  const response = await request.get("./data/people/p.json");
  const people = await response.json();
  const supported = people.find((item: { person_id: string }) => item.person_id === "ead0d460-6fcd-51cd-a6d4-01862ecc82f8");
  const separate = people.find((item: { person_id: string }) => item.person_id === "8686bb8e-3b16-5aa2-bb72-bdd2e6a6f3aa");
  expect(supported.possible_duplicate_group).toMatch(/^duplicate-[0-9a-f]{12}$/);
  expect(supported.possible_duplicate_group).toBe(separate.possible_duplicate_group);
  expect(supported.last_civilian_pre_service[0].canonical_organization).toBe("Harvard University");
  expect(supported.immediate_pre_oss_affiliations[0].canonical_organization).toBe("United States Army");
  expect(separate.last_civilian_pre_service).toHaveLength(0);
  expect(separate.immediate_pre_oss_affiliations).toHaveLength(0);
});

test("Carleton Swift keeps the middle-initial conflict and qualified chronology", async ({ request, page }) => {
  await page.goto("./people/e9dc5d67-dbf5-51a9-8805-17111ba5b93e/");
  const main = page.locator("main");
  await expect(main).toContainText("Carleton A. Swift");
  await expect(main).toContainText("middle initial A rather than indexed B/Byron");
  await expect(main).toContainText("United States Navy");
  await expect(main).toContainText("Swift & Company");
  await expect(main).toContainText("medium");
  await expect(main).toContainText("qualified");

  const response = await request.get("./data/people/c.json");
  const people = await response.json();
  const carleton = people.find((item: { person_id: string }) => item.person_id === "e9dc5d67-dbf5-51a9-8805-17111ba5b93e");
  expect(carleton.personnel_category).toBe("commissioned_naval_officer");
  expect(carleton.commissioned_officer).toBe(true);
  expect(carleton.immediate_pre_oss_affiliations[0].claim_confidence).toBe("medium");
  expect(carleton.last_civilian_pre_service[0].claim_confidence).toBe("medium");
});

test("Army categories stay employer-free and student codes stay student status", async ({ request, page }) => {
  for (const [id, phrase] of [
    ["42e969fc-831d-5694-8def-3fa1ae9bc063", "Students"],
    ["5e771570-d7a2-5818-bc1b-d11f552dd40a", "Routemen"],
    ["47405c7a-b8cb-518d-9c10-efe83bc67588", "Students"],
    ["2ce271ea-ff12-53f1-b078-e4641e595135", "Occupations in manufacture of radios and phonographs"],
    ["4c018d36-d9e1-54dc-8b94-79ff9bf1636d", "Occupations in manufacture of miscellaneous products"],
  ] as const) {
    await page.goto(`./people/${id}/`);
    const main = page.locator("main");
    await expect(main).toContainText(phrase);
    await expect(main).toContainText("no employer or workplace");
    await expect(main).not.toContainText("Last civilian employer before wartime service");
  }

  const response = await request.get("./data/people/t.json");
  const people = await response.json();
  const thomas = people.find((item: { person_id: string }) => item.person_id === "42e969fc-831d-5694-8def-3fa1ae9bc063");
  expect(thomas.other_pre_oss_affiliations[0].relationship_type).toBe("student");
  expect(thomas.last_civilian_pre_service).toHaveLength(0);
});

test("John Swensen preserves the Army surname variant without changing the indexed name", async ({ request, page }) => {
  await page.goto("./people/5e771570-d7a2-5818-bc1b-d11f552dd40a/");
  const main = page.locator("main");
  await expect(page.getByRole("heading", { name: "John W Swensen", level: 1 })).toBeVisible();
  await expect(main).toContainText("John W Swenson");
  await expect(main).toContainText("one-letter surname difference");

  const response = await request.get("./data/people/j.json");
  const people = await response.json();
  const john = people.find((item: { person_id: string }) => item.person_id === "5e771570-d7a2-5818-bc1b-d11f552dd40a");
  expect(john.display_name).toBe("John W Swensen");
  expect(john.name_variants).toContain("John W Swenson");
});

test("Robert Swift's rejected Army namesake contributes no occupation", async ({ request, page }) => {
  await page.goto("./people/706ed1af-148d-5ea7-bd31-1cc6468955c5/");
  const main = page.locator("main");
  await expect(main).toContainText("different-name Army candidate was rejected");
  await expect(main).toContainText("requires archival review");

  const response = await request.get("./data/people/r.json");
  const people = await response.json();
  const robert = people.find((item: { person_id: string }) => item.person_id === "706ed1af-148d-5ea7-bd31-1cc6468955c5");
  expect(robert.other_pre_oss_affiliations).toHaveLength(0);
  expect(robert.immediate_pre_oss_affiliations).toHaveLength(0);
  expect(robert.last_civilian_pre_service).toHaveLength(0);
});

test("Batch 935 does not change the evidence-defined oil-company category", async ({ page }) => {
  await page.goto("./oil-companies/");
  const main = page.locator("main");
  await expect(main).toContainText("14 people");
  await expect(main).toContainText("15 historically named");
  await expect(main).not.toContainText("Swift & Company");
  await expect(main).not.toContainText("Harvard University");
});

test("Batch 935 evidence excludes credentials and protected identifier fields", () => {
  expect(evidence).not.toMatch(/"serial_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toMatch(/"service_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toContain("NARA_API_KEY");
  expect(evidence).not.toContain("x-api-key");
  expect(evidence).not.toMatch(/serial-conflict:\d/);
});

test("Batch 935 publishes its exact coverage counters", async ({ request }) => {
  const response = await request.get("./data/stats.json");
  expect(response.ok()).toBeTruthy();
  const stats = await response.json();
  expect(stats).toMatchObject({
    source_rows: 23_978,
    person_entities: 23_936,
    possible_duplicate_groups: 632,
    research_attempted_people: 14_449,
    verified_affiliation_people: 1_024,
    verified_employer_people: 463,
    archival_review_assessed_people: 12_922,
    published_claims: 8_901,
    public_sources: 5_872,
  });
});
