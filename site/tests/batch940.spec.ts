import fs from "node:fs";
import { expect, test } from "@playwright/test";
import type { APIRequestContext } from "@playwright/test";

const evidence = fs.readFileSync(
  new URL(
    "../../research/evidence-page460-jefferson-m-tancil-to-mary-b-tarbet-review_batch-940_2026-10-28.json",
    import.meta.url,
  ),
  "utf8",
);

const profiles = [
  ["29fb89c8-10fa-52be-9da2-7748a0478530", "Jefferson M Tancil"],
  ["2ac17d28-008f-56c7-a245-8eb7acd5f46d", "Ernest O Tancous"],
  ["0d6072d9-fb0f-5179-8be6-00f7b0f405be", "Jeanne C Taneyhill"],
  ["0273cc24-59e4-5976-9d06-b1c190308d1e", "Louis L Tang"],
  ["4f134170-2f6e-5f2f-aa6d-4ee3bde139a7", "T Y Tang"],
  ["5223864f-7d5d-5c58-ac61-bdebbaa9e35b", "Wen Shun Tang"],
  ["fb3d4db7-0878-5374-aafa-83fbc9f13c3e", "Corrine M Tanguay"],
  ["ddd7f9db-7681-59b6-90ae-3209bd1890af", "Saburo Tani"],
  ["3230157d-3a4d-5ba4-b86b-0b48c378c0a8", "Noboru M Tanimoto"],
  ["31d4b2c1-44f0-580e-8ed3-21900f6a8046", "Bob F Tanisaki"],
  ["6cc20403-47c9-5e63-a2a1-2af7fd280aae", "Jane M Tanner"],
  ["24e84169-6067-57d5-9df3-ad8326ae318e", "Joe W Tanner"],
  ["13e4cf5e-73fe-5a20-ba99-6749a1fb52d3", "Walter J Tanner"],
  ["87cd2c5b-73f9-5b42-8704-0f8b8afa679c", "Alfred L Tanz"],
  ["8d7b2266-af60-530c-ba8a-46858edc3524", "Ruby K Tape"],
  ["157f8db0-165e-5bdc-86c4-975a11168127", "Charles H Taquey"],
  ["49a969e2-6e4d-555e-ae93-fc81ad342152", "Antielle Taralle"],
  ["ec3a44af-1e99-5769-a770-d75c00cea911", "Carmine Tarallo"],
  ["ca5a6b22-278f-59f3-865f-a007f7ac9e33", "Frank J Tarallo"],
  ["f7f4f0ef-ddbd-5a7a-9355-21fb72882c9a", "Mario Tarantino"],
  ["1227c3d3-25e9-53f2-87d6-1a4db7f9f39d", "Helen Tarasov"],
  ["7d615a84-e4da-511e-b83f-da22dd97b4bd", "William L Tarbert"],
  ["1d8e292c-4ac8-5fcb-abbf-cfb5ec0ff89d", "Mary B Tarbet"],
] as const;

async function peopleShard(request: APIRequestContext, letter: string) {
  const response = await request.get(`./data/people/${letter}.json`);
  expect(response.ok()).toBeTruthy();
  return response.json();
}

test("Batch 940 publishes all 23 indexed-row entities with terminal outcomes", async ({ page }) => {
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

test("Alfred Tanz separates the Army pathway from civilian legal practice", async ({ request, page }) => {
  await page.goto("./people/87cd2c5b-73f9-5b42-8704-0f8b8afa679c/");
  const main = page.locator("main");
  await expect(main).toContainText("United States Army");
  await expect(main).toContainText("Abraham Lincoln Battalion");
  const person = (await peopleShard(request, "a")).find((item: { person_id: string }) => item.person_id === "87cd2c5b-73f9-5b42-8704-0f8b8afa679c");
  expect(person.immediate_pre_oss_affiliations[0]).toMatchObject({
    canonical_organization: "United States Army",
    relationship_type: "military_assignment",
    temporal_basis: "explicit_immediate",
    claim_confidence: "high",
  });
  expect(person.last_civilian_pre_service[0]).toMatchObject({
    canonical_organization: null,
    relationship_type: "self_employment",
    claim_confidence: "medium",
  });
});

test("Charles Taquey preserves civilian, French Army, and U.S. Army stages", async ({ request }) => {
  const person = (await peopleShard(request, "c")).find((item: { person_id: string }) => item.person_id === "157f8db0-165e-5bdc-86c4-975a11168127");
  expect(person.last_civilian_pre_service[0]).toMatchObject({
    canonical_organization: "French Ministry of Foreign Affairs",
    relationship_type: "government_assignment",
    claim_confidence: "high",
  });
  expect(person.other_pre_oss_affiliations[0]).toMatchObject({
    canonical_organization: "French Army",
    relationship_type: "military_assignment",
  });
  expect(person.immediate_pre_oss_affiliations[0]).toMatchObject({
    canonical_organization: "United States Army",
    claim_confidence: "medium",
  });
});

test("student and professional affiliations are not converted into employers", async ({ request }) => {
  const bob = (await peopleShard(request, "b")).find((item: { person_id: string }) => item.person_id === "31d4b2c1-44f0-580e-8ed3-21900f6a8046");
  const william = (await peopleShard(request, "w")).find((item: { person_id: string }) => item.person_id === "7d615a84-e4da-511e-b83f-da22dd97b4bd");
  expect(bob.other_pre_oss_affiliations[0]).toMatchObject({
    canonical_organization: "Manzanar Free Press",
    relationship_type: "professional_affiliation",
  });
  expect(william.other_pre_oss_affiliations[0]).toMatchObject({
    canonical_organization: "University of Maryland",
    relationship_type: "student",
  });
  expect(bob.last_civilian_pre_service).toHaveLength(0);
  expect(william.last_civilian_pre_service).toHaveLength(0);
});

test("Saburo Tani and Helen Tarasov keep temporally qualified institutional claims", async ({ request }) => {
  const saburo = (await peopleShard(request, "s")).find((item: { person_id: string }) => item.person_id === "ddd7f9db-7681-59b6-90ae-3209bd1890af");
  const helen = (await peopleShard(request, "h")).find((item: { person_id: string }) => item.person_id === "1227c3d3-25e9-53f2-87d6-1a4db7f9f39d");
  expect(saburo.other_pre_oss_affiliations[0]).toMatchObject({
    canonical_organization: "University of Colorado",
    claim_confidence: "medium",
    temporal_basis: "temporal_relation_uncertain",
  });
  expect(helen.other_pre_oss_affiliations[0]).toMatchObject({
    canonical_organization: "United States Department of Commerce",
    claim_confidence: "medium",
    temporal_basis: "documented_prewar",
  });
});

test("Noboru Tanimoto and Ruby Tape remain visible identity conflicts", async ({ request, page }) => {
  for (const [letter, id] of [["n", "3230157d-3a4d-5ba4-b86b-0b48c378c0a8"], ["r", "8d7b2266-af60-530c-ba8a-46858edc3524"]]) {
    const person = (await peopleShard(request, letter)).find((item: { person_id: string }) => item.person_id === id);
    expect(["ambiguous", "conflicting"]).toContain(person.identity_status);
    expect(person.immediate_pre_oss_affiliations).toHaveLength(0);
    await page.goto(`./people/${id}/`);
    await expect(page.locator("main")).toContainText("conflict");
  }
});

test("unresolved Batch 940 names receive archival guidance rather than borrowed claims", async ({ request, page }) => {
  await page.goto("./people/29fb89c8-10fa-52be-9da2-7748a0478530/");
  const main = page.locator("main");
  await expect(main).toContainText("requires archival review");
  await expect(main).toContainText("No reviewed claim currently meets the publication threshold.");
  const person = (await peopleShard(request, "j")).find((item: { person_id: string }) => item.person_id === "29fb89c8-10fa-52be-9da2-7748a0478530");
  expect(person.identity_status).toBe("unresolved");
  expect(person.claims).toHaveLength(0);
});

test("Batch 940 does not change the evidence-defined oil-company category", async ({ page }) => {
  await page.goto("./oil-companies/");
  const main = page.locator("main");
  await expect(main).toContainText("14 people");
  await expect(main).toContainText("15 historically named");
  await expect(main).not.toContainText("University of Colorado");
  await expect(main).not.toContainText("French Ministry of Foreign Affairs");
});

test("Batch 940 evidence excludes credentials and protected identifiers", () => {
  expect(evidence).not.toMatch(/"serial_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toMatch(/"service_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toContain("NARA_API_KEY");
  expect(evidence).not.toContain("x-api-key");
});

test("Batch 940 publishes its exact coverage counters", async ({ request }) => {
  const response = await request.get("./data/stats.json");
  expect(response.ok()).toBeTruthy();
  const stats = await response.json();
  expect(stats).toMatchObject({
    source_rows: 23_978,
    person_entities: 23_936,
    possible_duplicate_groups: 637,
    research_attempted_people: 14_564,
    verified_affiliation_people: 1_033,
    verified_employer_people: 463,
    archival_review_assessed_people: 13_037,
    published_claims: 8_999,
    public_sources: 5_942,
  });
});
