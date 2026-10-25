import fs from "node:fs";
import { expect, test } from "@playwright/test";

const evidence = fs.readFileSync(
  new URL(
    "../../research/evidence-page439-sorisi-to-soustelle-review_batch-898_2026-10-25.json",
    import.meta.url,
  ),
  "utf8",
);

const people = fs.readFileSync(
  new URL("../src/data/generated/people.json", import.meta.url),
  "utf8",
);

const profiles = [
  ["ee71c5a5-1eb4-5a48-8598-1ed493492e97", "Gene Sorisi"],
  ["a897afa2-fefb-53c0-bb25-4a669abd1852", "Erwin Sorkin"],
  ["9ac2db7b-eeb1-54b0-a571-a771924c8894", "Mildred Sorkin"],
  ["0deeab81-a1e6-54aa-8de3-42fbfb3abd81", "Rolf Sorlie"],
  ["fd09ff01-bb21-555c-a6a7-0d05bdd3ed52", "Morris B Soroka"],
  ["2b24dcc5-3123-53d1-95b1-afbdfb3e9029", "Stephen S Sorota"],
  ["37bc75f5-e853-5362-9c83-89085af31f4e", "Steve S Sorota"],
  ["0241cc2f-f4cb-547c-86a3-f133a64fa472", "Lyman F Sorrels"],
  ["1181bd99-6665-5d6e-83e4-323190728eab", "Henry Sorrese"],
  ["fe2ef923-8ed0-5109-bf02-acfb6f07d1c9", "Victor L Soskice"],
  ["7dbdc435-4f84-5fa5-acd4-93601b01c746", "Victor A Soskice"],
  ["b831851e-8bb7-5ee9-aa1d-7416eabc838f", "Thomas G Soter"],
  ["1c3f3a03-3353-5eb5-890e-727044bef465", "Alexander J Soto"],
  ["b7b61bd5-fad2-5418-aca4-e4a9467bf733", "Edmond Sottile"],
  ["358e5285-5a5f-53e4-8793-ac3d61026b49", "Frederic Souard"],
  ["77abf1b3-af84-5436-838b-051c39e0f4c5", "Romeo A Soucy"],
  ["63cad4b6-bd5f-5bb4-a601-8f94c0b096d4", "John I Soule"],
  ["5e2ddd60-32e7-59d0-852e-e40a7417e178", "George Soulier"],
  ["ba48bbe0-6ff9-57ec-81b2-2caa9eaa4251", "Thomas P Soullas"],
  ["e68fd14e-4d69-5b79-9ce0-51a3266cca58", "Bohuslav Soumar"],
  ["5f764f7b-058d-5b67-9210-b69730bc13a5", "Robert W Sours"],
  ["c915bf7f-a67a-5d45-a936-99d92c2bc3ea", "Mary Sousa"],
  ["827e491a-a547-522d-9b9a-51c3f6fe01db", "Jacques Soustelle"],
] as const;

test("Batch 898 publishes all 23 profiles with terminal outcomes and masked identifiers", async ({ page }) => {
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

test("Army bridges publish qualified occupations without inventing employers", async ({ page }) => {
  const checks = [
    ["ee71c5a5-1eb4-5a48-8598-1ed493492e97", "Stock clerks"],
    ["a897afa2-fefb-53c0-bb25-4a669abd1852", "mechanical treatment of metals"],
    ["b7b61bd5-fad2-5418-aca4-e4a9467bf733", "fabrication of textile products"],
  ] as const;

  for (const [id, occupation] of checks) {
    await page.goto(`./people/${id}/`);
    const main = page.locator("main");
    await expect(main).toContainText(occupation);
    await expect(main).toContainText("qualified lead");
    await expect(main.locator("section[aria-labelledby='civilian-employer']")).toContainText(
      "No reliable pre-OSS employer has yet been identified",
    );
  }

  for (const id of [
    "0241cc2f-f4cb-547c-86a3-f133a64fa472",
    "b831851e-8bb7-5ee9-aa1d-7416eabc838f",
  ]) {
    await page.goto(`./people/${id}/`);
    await expect(page.locator("main")).toContainText("high confidence");
    await expect(page.locator("main")).not.toContainText(/occupation code 0?59|occupation code 999/i);
  }
});

test("Rolf Sorlie remains an engineer lead without an inferred employer or military category", async ({ page }) => {
  await page.goto("./people/0deeab81-a1e6-54aa-8de3-42fbfb3abd81/");
  const main = page.locator("main");
  await expect(main).toContainText("Rolf Sørlie");
  await expect(main).toContainText("engineer");
  await expect(main).toContainText("does not name his employer");
  await expect(main).toContainText("unknown or indeterminate");
  await expect(main).toContainText("not converted into employment at Norsk Hydro");
  await expect(main.locator("section[aria-labelledby='civilian-employer']")).toContainText(
    "No reliable pre-OSS employer has yet been identified",
  );
});

test("Sorota and Soskice variant rows stay separate and qualified", async ({ page }) => {
  await page.goto("./people/2b24dcc5-3123-53d1-95b1-afbdfb3e9029/");
  const stephen = page.locator("main");
  await expect(stephen).toContainText("probable");
  await expect(stephen).toContainText("Phillips Academy");
  await expect(stephen).toContainText("football and track coach");

  await page.goto("./people/37bc75f5-e853-5362-9c83-89085af31f4e/");
  const steve = page.locator("main");
  await expect(steve).toContainText("ambiguous");
  await expect(steve).toContainText("No publishable pre-OSS affiliation is recorded yet");
  await expect(steve).not.toContainText("Claim-level evidence");

  await page.goto("./people/7dbdc435-4f84-5fa5-acd4-93601b01c746/");
  const victorA = page.locator("main");
  await expect(victorA.locator("section[aria-labelledby='immediate-affiliation']")).toContainText(
    "Georgetown University",
  );
  await expect(victorA).toContainText("Lycée Français de New York");
  await expect(victorA).toContainText("student");

  await page.goto("./people/fe2ef923-8ed0-5109-bf02-acfb6f07d1c9/");
  const victorL = page.locator("main");
  await expect(victorL).toContainText("ambiguous");
  await expect(victorL).toContainText("No publishable pre-OSS affiliation is recorded yet");
  await expect(victorL).not.toContainText("Claim-level evidence");
});

test("identity conflicts and foreign-service findings remain bounded", async ({ page }) => {
  await page.goto("./people/1c3f3a03-3353-5eb5-890e-727044bef465/");
  const soto = page.locator("main");
  await expect(soto).toContainText("conflicting");
  await expect(soto).toContainText("William J Smith");
  await expect(soto).toContainText(/Duplicate groupduplicate-[a-f0-9]+/);
  await expect(soto).not.toContainText("serial-conflict:alexander-soto-william-smith-page439");

  await page.goto("./people/358e5285-5a5f-53e4-8793-ac3d61026b49/");
  const souard = page.locator("main");
  await expect(souard).toContainText("Frédéric Souard");
  await expect(souard).toContainText("French military trainee");
  await expect(souard).toContainText("French Increment");
  await expect(souard).toContainText("temporal relation uncertain");

  await page.goto("./people/5e2ddd60-32e7-59d0-852e-e40a7417e178/");
  await expect(page.locator("main")).toContainText("Georges Soulier");

  await page.goto("./people/ba48bbe0-6ff9-57ec-81b2-2caa9eaa4251/");
  await expect(page.locator("main")).toContainText("Technician Fourth Grade Thomas P. Soullas");
});

test("Jacques Soustelle publishes three documented prewar institutions without false immediacy", async ({ page }) => {
  await page.goto("./people/827e491a-a547-522d-9b9a-51c3f6fe01db/");
  const main = page.locator("main");
  await expect(main).toContainText("Musée de l'Homme");
  await expect(main).toContainText("Collège de France");
  await expect(main).toContainText("École nationale de la France d'outre-mer");
  await expect(main).toContainText("documented prewar");
  await expect(main.locator("section[aria-labelledby='immediate-affiliation']")).toContainText(
    "No reviewed claim currently meets the publication threshold",
  );
});

test("Batch 898 evidence and public projection exclude protected identifiers and credentials", () => {
  for (const protectedValue of [
    "7105327", "32904020", "12143281", "32857144", "12004330",
    "33474567", "238196", "12086189", "2044517",
  ]) {
    expect(evidence).not.toContain(protectedValue);
    expect(people).not.toContain(protectedValue);
  }
  expect(evidence).not.toMatch(/"serial_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toMatch(/"service_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toContain("NARA_API_KEY");
  expect(evidence).not.toContain("x-api-key");
});

test("Batch 898 publishes its exact coverage counters", async ({ request }) => {
  const response = await request.get("./data/stats.json");
  expect(response.ok()).toBeTruthy();
  const stats = await response.json();
  expect(stats).toMatchObject({
    source_rows: 23_978,
    person_entities: 23_936,
    possible_duplicate_groups: 602,
    research_attempted_people: 13_611,
    verified_affiliation_people: 978,
    verified_employer_people: 439,
    archival_review_assessed_people: 12_082,
    published_claims: 8_267,
    public_sources: 5_546,
  });
});
