import { expect, test } from "@playwright/test";

const profiles = [
  ["30a0dcc5-0cf1-550c-af01-ad2473a17adc", "David K Sidbury"],
  ["90787d72-8dc9-53c4-9e13-1333a37bbe46", "Hall A Siddall"],
  ["30bb2be2-763f-5df4-82a8-9de018a49465", "Paul Sideman"],
  ["e58e07ac-2885-5634-8b65-5d22408d559a", "Edward F Sidenius"],
  ["eef014f1-5e66-5461-b4b8-e0eac04817cd", "Gus Sideris"],
  ["68e503f5-ee9c-59cb-a036-089db085afa2", "Constant Sideropoulos"],
  ["8f249653-ab5e-5f86-920f-f8c5f3e2dea1", "Steve Sidianoff"],
  ["2de983df-9b40-593f-9277-63a3c13e6755", "Rosemary Sidley"],
  ["2b3ebbe8-b9c6-5577-8bd0-156b87241072", "Robert K Sieben"],
  ["55bf2d29-a677-5ea7-a99a-7e8285ee1b84", "William J Sieben"],
  ["13056f3e-9e81-5621-8a11-66b43427cfc0", "Elva L Sieber"],
  ["c5ebb779-a3cc-5450-98b6-75959e43dc4c", "Jeanette I Siebert"],
  ["437bf7ab-82cd-5614-9202-0a362d5d55e8", "Joseph G Siebert"],
  ["807a741b-5148-5a24-bf36-13e43605464b", "Frank I Siegel"],
  ["822212c4-72a7-586c-ad60-e2f73acf63f2", "Helen M Siegel"],
  ["7667b2d7-5962-5cb3-9e55-47c0e1842b7e", "Helen E Siegel"],
  ["a459bc8d-e07e-5d8e-a908-5eb4f449ee45", "Marguerite N Siegel"],
  ["29ddcb1d-ba29-58f1-91f1-e2885371d026", "Morris Siegel"],
  ["bd97bc53-03a0-5827-957e-04bb6384e385", "Howard F Siegle"],
  ["e93d5bf5-801f-5c43-9b62-eecdb4e06c1e", "Carol F Siekierski"],
  ["1e35c22e-d997-5629-9005-536697ecf3fe", "August K Siemen"],
  ["da57489e-5f15-523b-986c-e82a2f2f181b", "Walter Siemen"],
  ["06ca0d9d-e306-5b1f-aa48-7167c8e37ff1", "Casimir A Sienkiewicz"],
] as const;

test("Batch 874 publishes all 23 profiles with terminal outcomes and masked identifiers", async ({ page }) => {
  for (const [id, name] of profiles) {
    await page.goto(`./people/${id}/`);
    await expect(page.getByRole("heading", { name, level: 1 })).toBeVisible();
    const main = page.locator("main");
    await expect(main).toContainText("Archive box");
    await expect(main).not.toContainText("not started");
    await expect(main).not.toContainText("in progress");
    const serials = await main.locator("dt").filter({ hasText: /^Serial$/ })
      .locator("xpath=following-sibling::dd[1]").allTextContents();
    for (const value of serials) expect(value).not.toMatch(/^[A-Z]?\s?\d{4,9}(?:RA)?$/);
  }
});

test("Batch 874 qualifies Morris Siegel's prewar education and occupations without inventing an employer", async ({ page }) => {
  await page.goto("./people/29ddcb1d-ba29-58f1-91f1-e2885371d026/");
  const main = page.locator("main");
  await expect(main).toContainText("Identity statusprobable");
  await expect(main).toContainText("Columbia University");
  await expect(main).toContainText("graduate student in anthropology");
  await expect(main).toContainText("New York, New York, United States · student");
  await expect(main).toContainText("family restaurant manager and taxi driver");
  await expect(main).toContainText("No reviewed claim currently meets the publication threshold");
  await expect(main).toContainText("does not order his CIAA and OSS assignments");
});

test("Batch 874 preserves the Sideris-Sideropoulos conflict without merging profiles", async ({ page }) => {
  await page.goto("./people/eef014f1-5e66-5461-b4b8-e0eac04817cd/");
  let main = page.locator("main");
  await expect(main).toContainText("Identity statushigh confidence");
  await expect(main).toContainText("possible duplicate or alias");
  await expect(main).toContainText("Keep the two entities separate");

  await page.goto("./people/68e503f5-ee9c-59cb-a036-089db085afa2/");
  main = page.locator("main");
  await expect(main).toContainText("Identity statusconflicting");
  await expect(main).toContainText("Evidence conflicts");
  await expect(main).toContainText("names Gus Sideris rather than Constant Sideropoulos");
  await expect(main).toContainText("No employer or chronology is inferred");
});

test("Batch 874 keeps Rosemary Sidley qualified and employer-unresolved", async ({ page }) => {
  await page.goto("./people/2de983df-9b40-593f-9277-63a3c13e6755/");
  const main = page.locator("main");
  await expect(main).toContainText("Identity statusprobable");
  await expect(main).toContainText("CIA request log");
  await expect(main).toContainText("Probable, not confirmed");
  await expect(main).toContainText("No reliable pre-OSS employer has yet been identified");
});

test("Batch 874 does not promote the Siddall and Sienkiewicz career leads to affiliations", async ({ page }) => {
  await page.goto("./people/90787d72-8dc9-53c4-9e13-1333a37bbe46/");
  let main = page.locator("main");
  await expect(main).toContainText("Identity statusunresolved");
  await expect(main).toContainText("Review Box 709 before assigning the 1936 Sagada High School teaching record");
  await expect(main).toContainText("Immediate pre-OSS affiliationNo reviewed claim currently meets the publication threshold");

  await page.goto("./people/06ca0d9d-e306-5b1f-aa48-7167c8e37ff1/");
  main = page.locator("main");
  await expect(main).toContainText("Identity statusunresolved");
  await expect(main).toContainText("Review Box 710 before assigning the Federal Reserve System career");
  await expect(main).toContainText("Immediate pre-OSS affiliationNo reviewed claim currently meets the publication threshold");
});

test("Batch 874 publishes its exact coverage counters", async ({ request }) => {
  const response = await request.get("./data/stats.json");
  expect(response.ok()).toBeTruthy();
  const stats = await response.json();
  expect(stats).toMatchObject({
    source_rows: 23_978,
    person_entities: 23_937,
    possible_duplicate_groups: 582,
    research_attempted_people: 13_065,
    verified_affiliation_people: 948,
    verified_employer_people: 431,
    archival_review_assessed_people: 11_532,
    published_claims: 7_888,
    public_sources: 5_369,
  });
});
