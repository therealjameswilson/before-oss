import { expect, test } from "@playwright/test";

const profiles = [
  ["f7dbfe51-3b04-5d21-b859-f7642cb804da", "John M Shepard"],
  ["ceebff7d-9f6c-5416-87c5-42a0e72a8514", "Stanley J Shepard"],
  ["1aa6fa58-7464-5cbf-acd1-42c898ef37c0", "William B Shepard"],
  ["3f476b5c-bf12-532d-8879-1646130029e0", "Whitney Shepardson"],
  ["d5ed9f49-285c-5854-9ad3-15caaeadb3f0", "Cleatus E Sheperd"],
  ["2f48a903-cde8-5acd-95a7-9cc9f955699a", "Dorothea Sheppard"],
  ["9ec1cbfc-61cb-5fbd-803a-247c4bb32de7", "James A Sheppard"],
  ["41f4659d-9c9c-5e83-8f03-dba3b5ccc17c", "Robert B Sheppard"],
  ["343d4ef4-6af6-5f2c-8ea8-7610090198ac", "Walter L Sheppard"],
  ["4bbc4b0e-d999-5580-882e-2b8385872f58", "William S Sheppard"],
  ["aa97fa9f-d89b-5d44-a8c7-28abdfac42ab", "Charles Sheputa"],
  ["99c59741-0680-5320-8b6c-c451cdcba6b2", "Jesse H Shera"],
  ["453522c1-2c50-5051-a607-cd386229b10a", "Louis W Sherack"],
  ["e43f9e0e-202b-557f-aad2-1687bc59f4dc", "Thomas A Sherard"],
  ["c8cf9698-447d-572d-a64c-a0d18fc48b13", "Robert L Sherbert"],
  ["72c79d68-5f65-577a-8df9-37a03910cc17", "Edith L Sherbine"],
  ["57fb8e93-1fa0-5227-9b22-9a5ec393178c", "Wetzor O P Sherbowita"],
  ["86aa5b63-a100-5b6d-872b-7a3eccaf65b7", "Ervin L Sherbrooke"],
  ["df4e0ae0-7daf-5568-919b-8c6925f373a7", "Lee L Sherdell"],
  ["e899184e-f577-5260-846b-4b56f42165fb", "Bernard T P Sherer"],
  ["bb2d4db3-ad0f-5756-a13d-2a39735d529c", "Oscar Sherer"],
  ["6fefa85c-d2c3-5fe7-a0dc-1d58c1afdc8b", "William H Sherertz"],
  ["6b17f240-a28c-5313-988d-cb6c9844613e", "Harold S Sheridan"],
] as const;

test("Batch 867 publishes all 23 profiles with terminal outcomes and masked identifiers", async ({ page }) => {
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

test("Batch 867 keeps Shera's immediate and earlier affiliations distinct", async ({ page }) => {
  await page.goto("./people/99c59741-0680-5320-8b6c-c451cdcba6b2/");
  const main = page.locator("main");
  await expect(main).toContainText("Library of Congress");
  await expect(main).toContainText("Scripps Foundation for Research in Population Problems");
  await expect(main).toContainText("Last civilian employer");
  await expect(main).toContainText("strongly date bounded");
  await expect(main).toContainText("government assignment");
  await expect(main).toContainText("documented pre-OSS");
});

test("Batch 867 publishes Sherack's conflict without leaking the rejected Army identity", async ({ page }) => {
  await page.goto("./people/453522c1-2c50-5051-a607-cd386229b10a/");
  const main = page.locator("main");
  await expect(main).toContainText("Identity statusconflicting");
  await expect(main).toContainText("cannot presently be reconciled");
  await expect(main).toContainText("names a different person");
  await expect(main).not.toContainText("MAZIARZ");
  await expect(main).not.toContainText("JOHN J");
});

test("Batch 867 withholds low-confidence Sheputa and Sherbine candidate sources", async ({ page }) => {
  await page.goto("./people/aa97fa9f-d89b-5d44-a8c7-28abdfac42ab/");
  let main = page.locator("main");
  await expect(main).toContainText("Identity statusambiguous");
  await expect(main).toContainText("no direct OSS or Box 703 bridge");
  await expect(main).not.toContainText("Charles Sheputa Obituary");

  await page.goto("./people/72c79d68-5f65-577a-8df9-37a03910cc17/");
  main = page.locator("main");
  await expect(main).toContainText("Identity statusambiguous");
  await expect(main).toContainText("no direct OSS or personnel-file bridge");
  await expect(main).not.toContainText("New Castle News Archives");
});

test("Batch 867 preserves Army matches as identity-only evidence", async ({ page }) => {
  for (const id of [
    "e899184e-f577-5260-846b-4b56f42165fb",
    "d5ed9f49-285c-5854-9ad3-15caaeadb3f0",
    "86aa5b63-a100-5b6d-872b-7a3eccaf65b7",
    "f7dbfe51-3b04-5d21-b859-f7642cb804da",
    "df4e0ae0-7daf-5568-919b-8c6925f373a7",
    "c8cf9698-447d-572d-a64c-a0d18fc48b13",
    "ceebff7d-9f6c-5416-87c5-42a0e72a8514",
    "e43f9e0e-202b-557f-aad2-1687bc59f4dc",
    "6fefa85c-d2c3-5fe7-a0dc-1d58c1afdc8b",
    "4bbc4b0e-d999-5580-882e-2b8385872f58",
  ]) {
    await page.goto(`./people/${id}/`);
    const main = page.locator("main");
    await expect(main).toContainText("Electronic Army Serial Number Merged File");
    await expect(main).toContainText("not a named employer or Army-to-OSS chronology");
  }
});

test("Batch 867 publishes its exact coverage counters", async ({ request }) => {
  const response = await request.get("./data/stats.json");
  expect(response.ok()).toBeTruthy();
  const stats = await response.json();
  expect(stats).toMatchObject({
    source_rows: 23_978,
    person_entities: 23_937,
    possible_duplicate_groups: 579,
    research_attempted_people: 12_907,
    verified_affiliation_people: 938,
    verified_employer_people: 426,
    archival_review_assessed_people: 11_374,
    published_claims: 7_795,
    public_sources: 5_320,
  });
});
