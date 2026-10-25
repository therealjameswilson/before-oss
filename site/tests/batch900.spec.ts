import fs from "node:fs";
import { expect, test } from "@playwright/test";

const evidence = fs.readFileSync(
  new URL(
    "../../research/evidence-page440-spanum-to-spence-review_batch-900_2026-10-25.json",
    import.meta.url,
  ),
  "utf8",
);

const people = fs.readFileSync(
  new URL("../src/data/generated/people.json", import.meta.url),
  "utf8",
);

const profiles = [
  ["715418af-06ba-5fd8-bef6-1d46cb406672", "Mildred S Spanum"],
  ["148a479f-2daf-551c-9385-4a7f9d7cd797", "George Spardo"],
  ["7ee6d351-7ab5-552d-a795-7f8ab12d01fc", "Giorgio Spardo"],
  ["69f60fa8-e888-526f-b906-3a754aa92a69", "Fred A Sparks"],
  ["63105c95-79e1-54fe-8cca-7c77416b590c", "John C Sparks"],
  ["10da7dfd-0a8a-5bff-b014-c93feb770c69", "William L Sparks"],
  ["f5365a53-ed78-5ed9-909e-19fe93cb0e90", "John P Spauldling"],
  ["861d95a1-53b8-54e4-baa8-2d8e6fd7387e", "John P Spauldling"],
  ["66cad179-2ea7-512a-8c69-a469c30f156e", "Kenneth D Spauldling"],
  ["25346b3c-dd04-544c-bea7-cda89f52d61a", "Robert D Spaur"],
  ["19002111-c5d0-5976-81a2-49dd119cd56f", "Orlando A Spear"],
  ["d33218cd-a453-5e78-9227-73916f76701e", "Donald A Spears"],
  ["f88c68e7-737d-5e5d-90d2-f1db5d7380c8", "Robert S Spears"],
  ["01d29882-ba89-5318-b39c-9112ab97ed49", "Manes Specter"],
  ["2f7c8b24-6d14-59f2-9675-516da7eb79c7", "Samuel I Spector"],
  ["b1ab1f3f-a376-52f0-bd91-fe2a2c5e932e", "David G Speer"],
  ["5ba044cf-6e1f-5c32-9a23-b3acc1792630", "Bruce Spegal"],
  ["d345ac2c-d8e4-5f1b-99c2-895147e13c67", "Joe G Speigler"],
  ["2b95bc92-5a44-5b55-834b-1ea1778ab2fe", "Louis L Speilman"],
  ["6683b0d3-8282-56ee-902d-9308d3059cea", "Ephraim A Speiser"],
  ["cf925e3a-9a9e-5448-92bb-992ad9c6251f", "Francis E Speizer"],
  ["070eccda-462f-5d37-b775-a8c96dfc1212", "Vaughn B Speltz"],
  ["eb1027ba-9a18-521b-87b3-666180fcca77", "John P Spence"],
] as const;

test("Batch 900 publishes all 23 profiles with terminal outcomes and masked identifiers", async ({ page }) => {
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

test("Batch 900 Army bridges remain qualified occupations or student status", async ({ page }) => {
  const checks = [
    ["10da7dfd-0a8a-5bff-b014-c93feb770c69", "Occupations in manufacture of paper and pulp"],
    ["25346b3c-dd04-544c-bea7-cda89f52d61a", "Student; institution not recorded"],
    ["f88c68e7-737d-5e5d-90d2-f1db5d7380c8", "Salesmen and sales agents"],
    ["01d29882-ba89-5318-b39c-9112ab97ed49", "Semiprofessional occupations"],
    ["2f7c8b24-6d14-59f2-9675-516da7eb79c7", "Pattern and model makers"],
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
});

test("Batch 900 keeps both protected-identifier conflicts visible and unmerged", async ({ page }) => {
  await page.goto("./people/148a479f-2daf-551c-9385-4a7f9d7cd797/");
  let main = page.locator("main");
  await expect(main).toContainText("conflicting");
  await expect(main).toContainText("George Spadero");
  await expect(main).toContainText("George Spadaro");
  await expect(main).not.toContainText("Cooks, except private family");

  await page.goto("./people/d345ac2c-d8e4-5f1b-99c2-895147e13c67/");
  main = page.locator("main");
  await expect(main).toContainText("conflicting");
  await expect(main).toContainText("Joe G Spiegler");
  await expect(main).not.toContainText("Clerks, general office");
  await expect(main).not.toContainText("serial-conflict:joe-speigler-spiegler-pages440-441");
});

test("Ephraim Speiser publishes Penn as employer while qualifying immediacy", async ({ page }) => {
  await page.goto("./people/6683b0d3-8282-56ee-902d-9308d3059cea/");
  const main = page.locator("main");
  await expect(main).toContainText("Ephraim Avigdor Speiser");
  await expect(main.locator("section[aria-labelledby='immediate-affiliation']")).toContainText(
    "University of Pennsylvania",
  );
  await expect(main.locator("section[aria-labelledby='civilian-employer']")).toContainText(
    "University of Pennsylvania",
  );
  await expect(main).toContainText("probable immediate");
  await expect(main).toContainText("Near East Section");
});

test("John P Spence remains in identity review and does not publish the swimmer candidate", async ({ page }) => {
  await page.goto("./people/eb1027ba-9a18-521b-87b3-666180fcca77/");
  const main = page.locator("main");
  await expect(main).toContainText("identity review");
  await expect(main).toContainText("Tennessee");
  await expect(main).not.toContainText("last surviving member of the original five");
  await expect(main.locator("section[aria-labelledby='immediate-affiliation']")).toContainText(
    "No reviewed claim currently meets the publication threshold",
  );
  await expect(main.locator("section[aria-labelledby='civilian-employer']")).toContainText(
    "No reliable pre-OSS employer has yet been identified",
  );
});

test("Batch 900 evidence and public projection exclude credential fields", () => {
  expect(evidence).not.toMatch(/"serial_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toMatch(/"service_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toContain("NARA_API_KEY");
  expect(evidence).not.toContain("x-api-key");
  expect(people).not.toContain("serial-conflict:joe-speigler-spiegler-pages440-441");
});

test("Batch 900 publishes its exact coverage counters", async ({ request }) => {
  const response = await request.get("./data/stats.json");
  expect(response.ok()).toBeTruthy();
  const stats = await response.json();
  expect(stats).toMatchObject({
    source_rows: 23_978,
    person_entities: 23_936,
    possible_duplicate_groups: 603,
    research_attempted_people: 13_657,
    verified_affiliation_people: 979,
    verified_employer_people: 440,
    archival_review_assessed_people: 12_128,
    published_claims: 8_297,
    public_sources: 5_559,
  });
});
