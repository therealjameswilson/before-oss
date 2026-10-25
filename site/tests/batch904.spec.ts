import fs from "node:fs";
import { expect, test } from "@playwright/test";

const evidence = fs.readFileSync(
  new URL(
    "../../research/evidence-page442-spore-to-squatrito-review_batch-904_2026-10-25.json",
    import.meta.url,
  ),
  "utf8",
);

const people = fs.readFileSync(
  new URL("../src/data/generated/people.json", import.meta.url),
  "utf8",
);

const profiles = [
  ["0e4c121e-b8ec-53c4-8219-6d33cad480e7", "Leland M Spore"],
  ["7c9f82dc-142b-5566-83c4-495af70f5a9b", "Edith W Spradley"],
  ["58c92e6a-ef6d-54da-a94b-12c52fdcb449", "Jack H Spradlin"],
  ["076fc4ee-8c19-5bfa-8ef1-82ba3e0be35d", "Albert I Spratt"],
  ["ed85c4d6-8e49-5752-afde-7c5eea5f273d", "Roland G Spratt"],
  ["672a4274-ae72-52bf-9bab-dd71e29b3294", "Drexel A Sprecher"],
  ["af55a43e-3770-5b40-89a0-3f5af651de66", "Robert F Spreen"],
  ["ac952b9c-0215-5883-9d22-ceb512908c48", "Rudolph Spreier"],
  ["3fa53ca6-fce8-565b-944b-b872380114aa", "Chester F Sprimont"],
  ["31ca18e1-89a7-58c1-bae3-0a1ee1a467c9", "William W Spring"],
  ["476fe9eb-9662-5271-8eb7-3c2f370115ef", "Elsie S Springer"],
  ["2073d664-3994-5e55-8146-4b004808533b", "Stewart Springer"],
  ["b36e0245-af72-538e-b3d0-5841840320c9", "L P Springs"],
  ["8fcf8ba3-38ce-5b0f-a5bf-ebf8d7cb6819", "Robert B Springsteen"],
  ["b48d9fda-49b5-58a2-98a6-93bbbb61beba", "Harold A Sprinkle"],
  ["ea9b8cab-a554-5f4a-87eb-77ebd07e5229", "J M Sprouse"],
  ["fecbed6a-6fba-503d-b571-d63944ca0320", "Michael Sproveri"],
  ["f2cd23cc-a4d3-56d9-b5e2-9c16cc68f04c", "Donald W Sprung"],
  ["6d2674bf-13cd-57ca-a279-773396e0c696", "Edwin A Sprunger"],
  ["99dfd800-7906-5a3f-b637-14c1ab450fb6", "Lester J Spry"],
  ["054aa915-9d6d-56e0-be23-9baa8cc41dd8", "Enrico Squadra"],
  ["42d57907-48c2-528a-a8d8-2809034a9ef3", "Nicholas C Squadrito"],
  ["504c8c55-3a64-59b8-a686-8c86b1c1ab6d", "Rosario F Squatrito"],
] as const;

test("Batch 904 publishes all 23 people with terminal outcomes and masked identifiers", async ({ page }) => {
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

test("Batch 904 Army occupation bridges stay qualified as occupations", async ({ page }) => {
  const checks = [
    ["58c92e6a-ef6d-54da-a94b-12c52fdcb449", "Filers, grinders, buffers, and polishers"],
    ["076fc4ee-8c19-5bfa-8ef1-82ba3e0be35d", "Printing and publishing clerks"],
    ["ed85c4d6-8e49-5752-afde-7c5eea5f273d", "Stenographers and typists"],
    ["af55a43e-3770-5b40-89a0-3f5af651de66", "Accountants and auditors"],
    ["42d57907-48c2-528a-a8d8-2809034a9ef3", "Waiters and waitresses"],
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

test("Drexel Sprecher separates the Army path from the NLRB employer", async ({ page }) => {
  await page.goto("./people/672a4274-ae72-52bf-9bab-dd71e29b3294/");
  const main = page.locator("main");
  await expect(main.locator("section[aria-labelledby='immediate-affiliation']")).toContainText("United States Army");
  await expect(main.locator("section[aria-labelledby='civilian-employer']")).toContainText("National Labor Relations Board");
  await expect(main).toContainText("trial attorney");
});

test("Stewart Springer's Bass laboratory work remains an earlier role", async ({ page }) => {
  await page.goto("./people/2073d664-3994-5e55-8146-4b004808533b/");
  const main = page.locator("main");
  await expect(main).toContainText("Bass Biological Laboratory");
  await expect(main).toContainText("documented prewar");
  await expect(main.locator("section[aria-labelledby='civilian-employer']")).toContainText(
    "No reliable pre-OSS employer has yet been identified",
  );
});

test("Robert Springsteen separates McGill from the immediate Army assignment", async ({ page }) => {
  await page.goto("./people/8fcf8ba3-38ce-5b0f-a5bf-ebf8d7cb6819/");
  const main = page.locator("main");
  await expect(main).toContainText("Robert Burns Springsteen II");
  await expect(main.locator("section[aria-labelledby='immediate-affiliation']")).toContainText("United States Army");
  await expect(main.locator("section[aria-labelledby='civilian-employer']")).toContainText("McGill Manufacturing Company");
  await expect(main).toContainText("20 April 1944");
});

test("Enrico Squadra's OWI role stays temporally qualified", async ({ page }) => {
  await page.goto("./people/054aa915-9d6d-56e0-be23-9baa8cc41dd8/");
  const main = page.locator("main");
  await expect(main).toContainText("Office of War Information");
  await expect(main).toContainText("associate script editor");
  await expect(main).toContainText("temporal relation uncertain");
});

test("Rosario Squatrito publishes the employer lead and occupation conflict", async ({ page }) => {
  await page.goto("./people/504c8c55-3a64-59b8-a686-8c86b1c1ab6d/");
  const main = page.locator("main");
  await expect(main.locator("section[aria-labelledby='civilian-employer']")).toContainText("Superior Die Cutting");
  await expect(main).toContainText("Longshoremen and stevedores");
  await expect(main).toContainText("tool-and-die");
  await expect(main).toContainText("conflicting");
});

test("Batch 904 evidence and public projection exclude credential fields", () => {
  expect(evidence).not.toMatch(/"serial_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toMatch(/"service_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toContain("NARA_API_KEY");
  expect(evidence).not.toContain("x-api-key");
  expect(people).not.toContain("b0b4d376-62b4-5fa5-b493-a3ad14aec2ed");
  expect(people).not.toContain("96335019-129f-5b44-919c-dc2e8ec658b4");
});

test("Batch 904 publishes its exact coverage counters", async ({ request }) => {
  const response = await request.get("./data/stats.json");
  expect(response.ok()).toBeTruthy();
  const stats = await response.json();
  expect(stats).toMatchObject({
    source_rows: 23_978,
    person_entities: 23_936,
    possible_duplicate_groups: 607,
    research_attempted_people: 13_743,
    verified_affiliation_people: 988,
    verified_employer_people: 447,
    archival_review_assessed_people: 12_215,
    published_claims: 8_380,
    public_sources: 5_607,
  });
});
