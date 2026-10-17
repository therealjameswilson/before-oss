import { expect, test } from "@playwright/test";

const profiles = [
  ["a6c2dd16-4840-5cdc-bf2b-fe84c147fe5d", "R B Sheeks"],
  ["5aee1959-50fe-5d56-a0f0-3bd469bb52e2", "Willard D Sheeler"],
  ["fce2cdd5-a5e3-59aa-b01a-64eb0284a154", "Paul C Sheeline"],
  ["c6fe3937-c888-5a2b-98ba-39144368b7a4", "Henry G Sheen"],
  ["49d86438-ea19-5875-8b0e-216ae39cc950", "Herminia Sheeran"],
  ["1dc490f3-7f66-501f-8c60-b76e10dd581a", "John H Sheerar"],
  ["98126dfc-ab73-583c-99ea-ef50a0effe96", "Stephen J Shefchuck"],
  ["a2baae8d-e874-5ce8-9400-dd08ba95c922", "Avdulla Sheh"],
  ["f880c129-7b9d-50ca-b42f-f27428f33b28", "Alfred Sheinwold"],
  ["6ab8415d-4168-5910-8cc4-84f42cff0e89", "Henry W Sheinwold"],
  ["f249f1f4-85f0-52f0-9c6e-f86bd7d979bd", "Emily L Shek"],
  ["a22cb173-4849-5ccc-9598-1ae6a7786980", "Raymond T Shelby"],
  ["86985088-1f01-59a7-9d82-fc127b46df80", "Arnold H Sheldon"],
  ["b1e52399-0aa4-5588-b6ca-154d1ad6bc64", "George F Sheldon"],
  ["8aac7b46-0f46-55c0-a1c3-21054515db66", "Helen S Sheldon"],
  ["5ec6e697-b883-5661-a7c6-3b7acb5beb03", "Bonnie F Shelley"],
  ["59f03c2c-8604-5c13-9723-9541e542a62d", "Edna E Shelley"],
  ["2e2ab3f0-c697-55b5-834f-1f2de6f07a71", "James G Shelley"],
  ["2c0c592a-5d5c-57fb-b1b9-5a7b86beab80", "Howard W Shelton"],
  ["d273d53f-a0e7-541e-a2d2-77b082439f02", "Ollie M Shelton"],
  ["63347de8-a033-58be-9804-e0f299bb267b", "Lucille M Sheneman"],
  ["a61bdbcc-dc42-5d3e-b264-5b0e82c7f24c", "Gordon Shepard"],
  ["9ecad53e-a7bc-5449-a7d0-3421d215b050", "Hubert L Shepard"],
] as const;

test("Batch 866 publishes all 23 profiles with terminal outcomes and masked identifiers", async ({ page }) => {
  for (const [id, name] of profiles) {
    await page.goto(`./people/${id}/`);
    await expect(page.getByRole("heading", { name, level: 1 })).toBeVisible();
    const main = page.locator("main");
    await expect(main).toContainText("Archive box");
    await expect(main).not.toContainText("not started");
    const serials = await main.locator("dt").filter({ hasText: /^Serial$/ })
      .locator("xpath=following-sibling::dd[1]").allTextContents();
    for (const value of serials) expect(value).not.toMatch(/^[A-Z]?\s?\d{4,9}(?:RA)?$/);
  }
});

test("Batch 866 keeps military, student, employment and unnamed-employer evidence distinct", async ({ page }) => {
  await page.goto("./people/fce2cdd5-a5e3-59aa-b01a-64eb0284a154/");
  let main = page.locator("main");
  await expect(main).toContainText("United States Army Air Forces");
  await expect(main).toContainText("liaison officer with the French Air Force");
  await expect(main).toContainText("military assignment");

  await page.goto("./people/5aee1959-50fe-5d56-a0f0-3bd469bb52e2/");
  main = page.locator("main");
  await expect(main).toContainText("Harvard University");
  await expect(main).toContainText("student");
  await expect(main).toContainText("not employment by Harvard");

  await page.goto("./people/f880c129-7b9d-50ca-b42f-f27428f33b28/");
  main = page.locator("main");
  await expect(main).toContainText("The Bridge World");
  await expect(main).toContainText("unidentified New York newspaper");

  await page.goto("./people/a61bdbcc-dc42-5d3e-b264-5b0e82c7f24c/");
  main = page.locator("main");
  await expect(main).toContainText("Oppenheimer Wolff & Donnelly");
  await expect(main).toContainText("Last civilian employer");
  await expect(main).toContainText("strongly date bounded");
});

test("Batch 866 withholds low-confidence Henry Sheen candidate and preserves Army identity-only boundaries", async ({ page }) => {
  await page.goto("./people/c6fe3937-c888-5a2b-98ba-39144368b7a4/");
  let main = page.locator("main");
  await expect(main).toContainText("Identity statusambiguous");
  await expect(main).toContainText("lacks a direct service-number or personnel-file bridge");
  await expect(main).not.toContainText("The Black Market in Postwar Berlin");

  for (const id of [
    "6ab8415d-4168-5910-8cc4-84f42cff0e89",
    "86985088-1f01-59a7-9d82-fc127b46df80",
    "b1e52399-0aa4-5588-b6ca-154d1ad6bc64",
    "2e2ab3f0-c697-55b5-834f-1f2de6f07a71",
  ]) {
    await page.goto(`./people/${id}/`);
    main = page.locator("main");
    await expect(main).toContainText("official Army bulk record");
    await expect(main).toContainText("not a named employer");
  }
});

test("Batch 866 publishes its exact coverage counters", async ({ request }) => {
  const response = await request.get("./data/stats.json");
  expect(response.ok()).toBeTruthy();
  const stats = await response.json();
  expect(stats).toMatchObject({
    source_rows: 23_978,
    person_entities: 23_937,
    possible_duplicate_groups: 578,
    research_attempted_people: 12_885,
    verified_affiliation_people: 937,
    verified_employer_people: 425,
    archival_review_assessed_people: 11_352,
    published_claims: 7_780,
    public_sources: 5_315,
  });
});
