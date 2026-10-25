import fs from "node:fs";
import { expect, test } from "@playwright/test";

const evidence = fs.readFileSync(
  new URL(
    "../../research/evidence-page439-soustelle-to-spanos-review_batch-899_2026-10-25.json",
    import.meta.url,
  ),
  "utf8",
);

const people = fs.readFileSync(
  new URL("../src/data/generated/people.json", import.meta.url),
  "utf8",
);

const profiles = [
  ["7612d060-972b-53ee-9e51-88652c349247", "M J Soustelle"],
  ["d68746ec-4a97-51e8-a5aa-78f8a9f7a732", "James R Southern"],
  ["0fcf924d-4726-564b-b22a-9b18ec894806", "Richard Southgate"],
  ["7a455dd5-13d3-597a-b17b-3ae1ea7c2ee5", "Faye F Southworth"],
  ["58145339-5a55-546f-8488-e6e8d7e38a3b", "Herbert Southworth"],
  ["a1781a66-d363-5419-bce9-27d0eb65c73a", "Irene Souza"],
  ["edb60948-009c-5a1d-ba0a-354366970e2f", "Katherine F Souza"],
  ["05df6fef-1d47-54ff-af70-3b96bde9d442", "Pedro M Souza"],
  ["7927e30b-daa3-5060-86c7-c87f7162f3b6", "Karel Sovak"],
  ["85efbcee-7ee7-5d9e-a915-aa3b95c8532f", "Lewis W Sowles"],
  ["7fac5efe-d3f3-57bf-b153-5e4cd993fcaf", "Santino R Sozio"],
  ["885163da-87b6-5381-b8c9-c570bd40c063", "Katherine H Spaatz"],
  ["ec06afdf-6bee-55b2-a1c7-92d7d35d1eb4", "Joseph J Spack"],
  ["d859ac79-b0eb-5f62-b2e3-cbca85c2bebc", "John W Spade"],
  ["b47701d2-5ac0-5119-bb1f-d7e866d08b76", "George Spadero"],
  ["e1fbce86-395c-5ca9-ba0d-d2ead53426ba", "Dominick Spagnuolo"],
  ["f8e28fb5-5484-5904-afb9-015e3b123628", "Sylvia E Spain"],
  ["162da5de-df14-5161-9b14-32d9b84f9163", "Walter C Spain"],
  ["206eaa37-01ae-50fc-ae6c-237ad5443656", "Charles F Spalding"],
  ["bc6137ec-35f6-50d9-bbf5-a831452389ef", "Merrill T Spalding"],
  ["9731ca48-f8cf-5e6e-bb9c-107bda39af3d", "Beatrice Spang"],
  ["b97746f6-561a-5d7f-acc6-f5c53696bbba", "Yvonne Spann"],
  ["d1c66f0d-a2e4-5a0c-9bf6-8b8ca545f34c", "Andrew Spanos"],
] as const;

test("Batch 899 publishes all 23 profiles with terminal outcomes and masked identifiers", async ({ page }) => {
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
    ["85efbcee-7ee7-5d9e-a915-aa3b95c8532f", "Clerks, general office"],
    ["ec06afdf-6bee-55b2-a1c7-92d7d35d1eb4", "Chauffeurs and drivers"],
    ["d859ac79-b0eb-5f62-b2e3-cbca85c2bebc", "Farm hands, general farms"],
    ["e1fbce86-395c-5ca9-ba0d-d2ead53426ba", "Chauffeurs and drivers"],
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

test("George Spadero and George Spardo remain a visible unresolved identifier conflict", async ({ page }) => {
  await page.goto("./people/b47701d2-5ac0-5119-bb1f-d7e866d08b76/");
  const main = page.locator("main");
  await expect(main).toContainText("conflicting");
  await expect(main).toContainText("George Spardo");
  await expect(main).toContainText("George Spadaro");
  await expect(main).toContainText(/Duplicate groupduplicate-[a-f0-9]+/);
  await expect(main).not.toContainText("Cooks, except private family");
  await expect(main).not.toContainText("serial-conflict:george-spadero-spardo-pages439-440");
});

test("Herbert Southworth preserves employment, government assignment, and rejected application boundaries", async ({ page }) => {
  await page.goto("./people/58145339-5a55-546f-8488-e6e8d7e38a3b/");
  const main = page.locator("main");
  await expect(main).toContainText("Herbert Rutledge Southworth");
  await expect(main.locator("section[aria-labelledby='immediate-affiliation']")).toContainText(
    "Office of War Information",
  );
  await expect(main.locator("section[aria-labelledby='civilian-employer']")).toContainText(
    "Spanish Information Bureau",
  );
  await expect(main).toContainText("Library of Congress");
  await expect(main).toContainText("Foreign Information Service");
  await expect(main).toContainText("OSS rejected the application");
  await expect(main).toContainText("government assignment");
});

test("Katherine Spaatz publishes identity but withholds an unsupported pre-OSS employer", async ({ page }) => {
  await page.goto("./people/885163da-87b6-5381-b8c9-c570bd40c063/");
  const main = page.locator("main");
  await expect(main).toContainText("Katherine 'Tatti' Spaatz");
  await expect(main).toContainText("American Red Cross");
  await expect(main).toContainText("temporal review");
  await expect(main.locator("section[aria-labelledby='immediate-affiliation']")).toContainText(
    "No reviewed claim currently meets the publication threshold",
  );
  await expect(main.locator("section[aria-labelledby='civilian-employer']")).toContainText(
    "No reliable pre-OSS employer has yet been identified",
  );
});

test("Batch 899 evidence and public projection exclude credential fields", () => {
  expect(evidence).not.toMatch(/"serial_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toMatch(/"service_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toContain("NARA_API_KEY");
  expect(evidence).not.toContain("x-api-key");
  expect(people).not.toContain("serial-conflict:george-spadero-spardo-pages439-440");
});

test("Batch 899 publishes its exact coverage counters", async ({ request }) => {
  const response = await request.get("./data/stats.json");
  expect(response.ok()).toBeTruthy();
  const stats = await response.json();
  expect(stats).toMatchObject({
    source_rows: 23_978,
    person_entities: 23_936,
    possible_duplicate_groups: 603,
    research_attempted_people: 13_634,
    verified_affiliation_people: 978,
    verified_employer_people: 439,
    archival_review_assessed_people: 12_105,
    published_claims: 8_282,
    public_sources: 5_554,
  });
});
