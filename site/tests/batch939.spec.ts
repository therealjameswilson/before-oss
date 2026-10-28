import fs from "node:fs";
import { expect, test } from "@playwright/test";
import type { APIRequestContext } from "@playwright/test";

const evidence = fs.readFileSync(
  new URL(
    "../../research/evidence-page460-will-s-talbot-to-yasuo-tanaka-review_batch-939_2026-10-28.json",
    import.meta.url,
  ),
  "utf8",
);

const profiles = [
  ["29a23254-9b59-561f-9400-5cbe0bca2311", "Will S Talbot"],
  ["af44fc9e-1e5a-552c-86af-5fc9575bf2cf", "William F Talbot"],
  ["c4df08e3-22a7-554d-9f32-7504b16e9f21", "Edward H Taliaferro"],
  ["762bb7a8-295a-50db-aed3-697065eec185", "Jaunita L Talkington"],
  ["c06a1cb0-fca1-5268-ad2a-19acb1c103fe", "Vangie Tallent"],
  ["6c509447-7d74-5d6f-8b5f-0567d7927226", "David Talley"],
  ["75eb871d-5eb6-59f4-bfeb-ff27594b9fba", "George L Tambakos"],
  ["17baa547-fbe8-5ee4-9a4c-590fbebad012", "Ernest D Tamminga"],
  ["f4d36700-40f6-5e16-88a8-69ce8b2b3933", "Takeo Tanabe"],
  ["ac4881e6-6585-5ef0-a1e5-dbfc6cd6f637", "Hajime W Tanaka"],
  ["eea3292c-810c-5802-9e90-2c1c41cda07e", "Linda Y Tanaka"],
  ["f147656a-bf77-5fb4-8acd-5e886754c7c1", "Paul H Tanaka"],
  ["ceb349c5-6fcd-5943-9511-ca3811bbe6ea", "Sugumu Tanaka"],
  ["6f02d6b8-2686-5a95-a1bc-27b82c27862b", "Yasuo Tanaka"],
  ["aeb197ac-2b0e-564a-9544-4df1d1bffed9", "Lucy Talcott"],
  ["92cd223b-91a3-5797-acc1-f644a5f3ec4b", "Bruno A Talevi"],
  ["e9ae672d-a6a5-57f1-8e79-6a451f2b6eea", "Bernard W Tallaksen"],
  ["988d1d54-de83-5e95-a882-e5d474a0c9b9", "Bob Talmadge"],
  ["d9674002-4998-5c5e-a4cf-b19e59311b83", "James Talmadge"],
  ["bdedb53a-ba1e-5716-900e-5618287b8cfb", "Jack Tamargo"],
  ["559e5784-b401-5c6b-bee4-62c912bb44a9", "Noboru Tamimoto"],
  ["d9828313-3399-5ffb-8706-05564b29b5c7", "Chuzo Tamotsu"],
  ["4adbd14d-83c6-59c5-bcd5-230cef23fb48", "Bunliang Tamthai"],
] as const;

async function peopleShard(request: APIRequestContext, letter: string) {
  const response = await request.get(`./data/people/${letter}.json`);
  expect(response.ok()).toBeTruthy();
  return response.json();
}

test("Batch 939 publishes all 23 indexed-row entities with terminal outcomes", async ({ page }) => {
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

test("Lucy Talcott keeps the Agora role qualified rather than claiming an exact OSS transition", async ({ request, page }) => {
  await page.goto("./people/aeb197ac-2b0e-564a-9544-4df1d1bffed9/");
  const main = page.locator("main");
  await expect(main).toContainText("American School of Classical Studies at Athens");
  await expect(main).toContainText("Secretary of the Agora Excavations");

  const people = await peopleShard(request, "l");
  const person = people.find((item: { person_id: string }) => item.person_id === "aeb197ac-2b0e-564a-9544-4df1d1bffed9");
  expect(person.immediate_pre_oss_affiliations).toHaveLength(0);
  expect(person.last_civilian_pre_service[0]).toMatchObject({
    canonical_organization: "American School of Classical Studies at Athens",
    relationship_type: "employment",
    temporal_basis: "strongly_date_bounded",
    claim_confidence: "medium",
  });
});

test("Bruno Talevi publishes student status without converting the school into an employer", async ({ request }) => {
  const people = await peopleShard(request, "b");
  const person = people.find((item: { person_id: string }) => item.person_id === "92cd223b-91a3-5797-acc1-f644a5f3ec4b");
  expect(person.immediate_pre_oss_affiliations[0]).toMatchObject({
    canonical_organization: "Benjamin Franklin High School",
    relationship_type: "student",
    temporal_basis: "explicit_immediate",
    claim_confidence: "high",
  });
  expect(person.last_civilian_pre_service).toHaveLength(0);
});

test("Bernard Tallaksen publishes a high-confidence 99th Infantry pathway", async ({ request, page }) => {
  await page.goto("./people/e9ae672d-a6a5-57f1-8e79-6a451f2b6eea/");
  await expect(page.locator("main")).toContainText("99th Infantry Battalion");
  const people = await peopleShard(request, "b");
  const person = people.find((item: { person_id: string }) => item.person_id === "e9ae672d-a6a5-57f1-8e79-6a451f2b6eea");
  expect(person.immediate_pre_oss_affiliations[0]).toMatchObject({
    canonical_organization: "United States Army, 99th Infantry Battalion (Separate)",
    relationship_type: "military_assignment",
    claim_confidence: "high",
  });
});

test("the Talmadge profiles publish distinct Coast Guard roles", async ({ request }) => {
  const bob = (await peopleShard(request, "b")).find((item: { person_id: string }) => item.person_id === "988d1d54-de83-5e95-a882-e5d474a0c9b9");
  const james = (await peopleShard(request, "j")).find((item: { person_id: string }) => item.person_id === "d9674002-4998-5c5e-a4cf-b19e59311b83");
  expect(bob.immediate_pre_oss_affiliations[0]).toMatchObject({ canonical_organization: "United States Coast Guard" });
  expect(james.immediate_pre_oss_affiliations[0]).toMatchObject({ canonical_organization: "United States Coast Guard" });
  expect(bob.immediate_pre_oss_affiliations[0].role_title).toContain("Motor Machinist");
  expect(james.immediate_pre_oss_affiliations[0].role_title).toContain("Boatswain");
});

test("Jack Tamargo publishes the qualified Army-to-OSS pathway", async ({ request, page }) => {
  await page.goto("./people/bdedb53a-ba1e-5716-900e-5618287b8cfb/");
  const main = page.locator("main");
  await expect(main).toContainText("Canastel, Algeria");
  await expect(main).not.toContainText("Last civilian employer before wartime service");
  const people = await peopleShard(request, "j");
  const person = people.find((item: { person_id: string }) => item.person_id === "bdedb53a-ba1e-5716-900e-5618287b8cfb");
  expect(person.immediate_pre_oss_affiliations[0]).toMatchObject({
    canonical_organization: "United States Army",
    relationship_type: "military_assignment",
    claim_confidence: "medium",
  });
});

test("Chuzo Tamotsu keeps the Federal Art Project as documented prewar employment", async ({ request, page }) => {
  await page.goto("./people/d9828313-3399-5ffb-8706-05564b29b5c7/");
  await expect(page.locator("main")).toContainText("Federal Art Project");
  const people = await peopleShard(request, "c");
  const person = people.find((item: { person_id: string }) => item.person_id === "d9828313-3399-5ffb-8706-05564b29b5c7");
  expect(person.last_civilian_pre_service[0]).toMatchObject({
    canonical_organization: "Federal Art Project",
    relationship_type: "employment",
    temporal_basis: "documented_prewar",
    claim_confidence: "medium",
  });
});

test("Bunliang Tamthai publishes unnamed student status without inventing an institution", async ({ request }) => {
  const people = await peopleShard(request, "b");
  const person = people.find((item: { person_id: string }) => item.person_id === "4adbd14d-83c6-59c5-bcd5-230cef23fb48");
  expect(person.immediate_pre_oss_affiliations[0]).toMatchObject({
    canonical_organization: null,
    relationship_type: "student",
    temporal_basis: "explicit_immediate",
    claim_confidence: "high",
  });
  expect(person.last_civilian_pre_service).toHaveLength(0);
});

test("Noboru Tamimoto remains a visible unresolved duplicate conflict", async ({ request, page }) => {
  await page.goto("./people/559e5784-b401-5c6b-bee4-62c912bb44a9/");
  const main = page.locator("main");
  await expect(main).toContainText("Noboru Mori Tanimoto");
  await expect(main).toContainText("conflict");
  const people = await peopleShard(request, "n");
  const person = people.find((item: { person_id: string }) => item.person_id === "559e5784-b401-5c6b-bee4-62c912bb44a9");
  expect(person.identity_status).toBe("ambiguous");
  expect(person.possible_duplicate_group).toMatch(/^duplicate-[a-f0-9]{12}$/);
  expect(person.immediate_pre_oss_affiliations).toHaveLength(0);
});

test("unresolved Batch 939 names receive archival guidance rather than borrowed claims", async ({ request, page }) => {
  await page.goto("./people/29a23254-9b59-561f-9400-5cbe0bca2311/");
  const main = page.locator("main");
  await expect(main).toContainText("requires archival review");
  await expect(main).toContainText("No reviewed claim currently meets the publication threshold.");
  const people = await peopleShard(request, "w");
  const person = people.find((item: { person_id: string }) => item.person_id === "29a23254-9b59-561f-9400-5cbe0bca2311");
  expect(person.identity_status).toBe("unresolved");
  expect(person.claims).toHaveLength(0);
});

test("Batch 939 does not change the evidence-defined oil-company category", async ({ page }) => {
  await page.goto("./oil-companies/");
  const main = page.locator("main");
  await expect(main).toContainText("14 people");
  await expect(main).toContainText("15 historically named");
  await expect(main).not.toContainText("Federal Art Project");
  await expect(main).not.toContainText("Benjamin Franklin High School");
});

test("Batch 939 evidence excludes credentials and protected identifiers", () => {
  expect(evidence).not.toMatch(/"serial_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toMatch(/"service_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toContain("NARA_API_KEY");
  expect(evidence).not.toContain("x-api-key");
});

test("Batch 939 publishes its exact coverage counters", async ({ request }) => {
  const response = await request.get("./data/stats.json");
  expect(response.ok()).toBeTruthy();
  const stats = await response.json();
  expect(stats).toMatchObject({
    source_rows: 23_978,
    person_entities: 23_936,
    possible_duplicate_groups: 636,
    research_attempted_people: 14_541,
    verified_affiliation_people: 1_031,
    verified_employer_people: 463,
    archival_review_assessed_people: 13_014,
    published_claims: 8_976,
    public_sources: 5_925,
  });
});
