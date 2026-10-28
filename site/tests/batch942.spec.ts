import fs from "node:fs";
import { expect, test } from "@playwright/test";
import type { APIRequestContext } from "@playwright/test";

const evidence = fs.readFileSync(
  new URL(
    "../../research/evidence-page461-bernard-tatz-to-jeanne-h-taylor-review_batch-942_2026-10-28.json",
    import.meta.url,
  ),
  "utf8",
);

const profiles = [
  ["9efed2b0-e157-5e59-af87-1db5d4181888", "Bernard Tatz"],
  ["4690c105-7f54-5c08-a0c1-f77d916157a1", "Kurt L Taub"],
  ["93138996-9799-5356-9a98-e66cdca2789c", "J G Tausig"],
  ["1a32bb9c-88e1-5e6a-b8f3-50879aad6cc0", "John G Tausig"],
  ["aee13560-6af5-51b9-bebd-19fe7ccbc248", "Ed E Taves"],
  ["148dde5f-c3db-5b04-b770-ade9b0c4af7a", "William Y Tayenaka"],
  ["f7c97c0e-e6a9-556e-961b-3e1cf287c8d3", "Allen Taylor"],
  ["d591a709-bf9f-5d65-a532-c542f296d771", "Anne V Taylor"],
  ["3bc90b19-829b-503d-ab57-b673c2c219cd", "Chester L Taylor"],
  ["56fee5f9-b773-5597-b1ff-8e78d84394d8", "Dorothy L Taylor"],
  ["d326c13a-a719-5c00-8436-9c220e4372ce", "Earle F Taylor"],
  ["b81ac9d4-5cca-523b-bdd1-d791389cba4a", "Edmond L Taylor"],
  ["972c2618-c2ea-5d07-82fc-fc9b46b12de7", "Edward H Taylor"],
  ["0a5f69a9-ed97-5cb4-9d62-5dfd9bc438fc", "Eleanor V Taylor"],
  ["ba65a7c4-40bc-5d9f-8ca9-a6aa07a5aa6b", "Ellen Taylor"],
  ["99b43df9-36d7-5601-b37f-d46f1f113d95", "Fred J Taylor"],
  ["9c2cb3bd-42f5-58d6-87c9-4509feba9b95", "George S Taylor"],
  ["9609a18b-f205-55bc-9d1b-9c46f19da0ff", "Geraldine B Taylor"],
  ["f6cc4878-76e0-5256-bc43-9e262680cc10", "Gordon L Taylor"],
  ["fda21df8-311a-5dd8-ae31-bcdb141d4445", "Harry E Taylor"],
  ["91a8199c-d31e-5837-94b9-8019a09dbf7d", "Jack H Taylor"],
  ["0ae037cd-3ef3-5424-acb3-6c6d8e8d2fc9", "James C Taylor"],
  ["db23d265-0e22-5004-96ad-ab1762b43b92", "Jeanne H Taylor"],
] as const;

async function peopleShard(request: APIRequestContext, letter: string) {
  const response = await request.get(`./data/people/${letter}.json`);
  expect(response.ok()).toBeTruthy();
  return response.json();
}

test("Batch 942 publishes all 23 indexed-row entities with reviewed outcomes", async ({ page }) => {
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

test("Kurt Taub separates military, final civilian, and earlier employment stages", async ({ request, page }) => {
  const person = (await peopleShard(request, "k")).find((item: { person_id: string }) => item.person_id === "4690c105-7f54-5c08-a0c1-f77d916157a1");
  expect(person.immediate_pre_oss_affiliations[0]).toMatchObject({
    canonical_organization: "United States Army",
    relationship_type: "military_assignment",
    claim_confidence: "high",
  });
  expect(person.last_civilian_pre_service[0]).toMatchObject({
    canonical_organization: null,
    organization_name_as_found: "unnamed upholstery shop in Boston",
    claim_confidence: "medium",
  });
  expect(person.other_pre_oss_affiliations[0]).toMatchObject({
    canonical_organization: "Schenker & Co.",
    relationship_type: "employment",
    claim_confidence: "high",
  });
  await page.goto("./people/4690c105-7f54-5c08-a0c1-f77d916157a1/");
  await expect(page.locator("main")).toContainText("Counter Intelligence Corps");
  await expect(page.locator("main")).toContainText("Schenker & Co.");
});

test("Edmond Taylor keeps COI distinct from earlier Chicago Tribune work", async ({ request }) => {
  const person = (await peopleShard(request, "e")).find((item: { person_id: string }) => item.person_id === "b81ac9d4-5cca-523b-bdd1-d791389cba4a");
  expect(person.immediate_pre_oss_affiliations[0]).toMatchObject({
    canonical_organization: "Office of the Coordinator of Information",
    relationship_type: "government_assignment",
    temporal_basis: "explicit_immediate",
  });
  expect(person.other_pre_oss_affiliations[0]).toMatchObject({
    canonical_organization: "Chicago Tribune",
    relationship_type: "employment",
  });
  expect(person.last_civilian_pre_service).toHaveLength(0);
});

test("Jack Taylor keeps Navy pathway separate from the unnamed dental practice", async ({ request, page }) => {
  const person = (await peopleShard(request, "j")).find((item: { person_id: string }) => item.person_id === "91a8199c-d31e-5837-94b9-8019a09dbf7d");
  expect(person.identity_status).toBe("confirmed");
  expect(person.commissioned_officer).toBe(true);
  expect(person.immediate_pre_oss_affiliations[0]).toMatchObject({
    canonical_organization: "United States Navy",
    relationship_type: "military_assignment",
  });
  expect(person.last_civilian_pre_service[0]).toMatchObject({
    canonical_organization: null,
    organization_name_as_found: "unnamed Los Angeles dental practice",
    occupation: "dentist",
  });
  await page.goto("./people/91a8199c-d31e-5837-94b9-8019a09dbf7d/");
  await expect(page.locator("main")).toContainText("unnamed Los Angeles dental practice");
});

test("J G and John G Tausig remain separate possible duplicates", async ({ request }) => {
  const people = await peopleShard(request, "j");
  const groups = [];
  for (const id of ["93138996-9799-5356-9a98-e66cdca2789c", "1a32bb9c-88e1-5e6a-b8f3-50879aad6cc0"]) {
    const person = people.find((item: { person_id: string }) => item.person_id === id);
    expect(person.identity_status).toBe("ambiguous");
    expect(person.possible_duplicate_group).toBeTruthy();
    groups.push(person.possible_duplicate_group);
    expect(person.immediate_pre_oss_affiliations).toHaveLength(0);
  }
  expect(new Set(groups).size).toBe(1);
});

test("James C Taylor preserves the middle-initial conflict", async ({ request, page }) => {
  const person = (await peopleShard(request, "j")).find((item: { person_id: string }) => item.person_id === "0ae037cd-3ef3-5424-acb3-6c6d8e8d2fc9");
  expect(person.identity_status).toBe("conflicting");
  expect(person.immediate_pre_oss_affiliations).toHaveLength(0);
  expect(person.claims.some((item: { claim_confidence: string }) => item.claim_confidence === "conflicting")).toBeTruthy();
  await page.goto("./people/0ae037cd-3ef3-5424-acb3-6c6d8e8d2fc9/");
  await expect(page.locator("main")).toContainText("middle-initial conflict");
});

test("coded Army occupations remain unnamed qualified occupations", async ({ request }) => {
  const people = await peopleShard(request, "g");
  const george = people.find((item: { person_id: string }) => item.person_id === "9c2cb3bd-42f5-58d6-87c9-4509feba9b95");
  expect(george.other_pre_oss_affiliations[0]).toMatchObject({
    canonical_organization: null,
    occupation: "Clerks, general office",
    claim_confidence: "medium",
  });
  expect(george.last_civilian_pre_service).toHaveLength(0);
});

test("unresolved Batch 942 names receive archival guidance rather than borrowed claims", async ({ request, page }) => {
  await page.goto("./people/aee13560-6af5-51b9-bebd-19fe7ccbc248/");
  const main = page.locator("main");
  await expect(main).toContainText("requires archival review");
  await expect(main).toContainText("No reviewed claim currently meets the publication threshold.");
  const person = (await peopleShard(request, "e")).find((item: { person_id: string }) => item.person_id === "aee13560-6af5-51b9-bebd-19fe7ccbc248");
  expect(person.identity_status).toBe("unresolved");
  expect(person.claims).toHaveLength(0);
});

test("Batch 942 does not change the evidence-defined oil-company category", async ({ page }) => {
  await page.goto("./oil-companies/");
  const main = page.locator("main");
  await expect(main).toContainText("14 people");
  await expect(main).toContainText("15 historically named");
  await expect(main).not.toContainText("Schenker & Co.");
});

test("Batch 942 evidence excludes credentials and protected identifiers", () => {
  expect(evidence).not.toMatch(/"serial_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toMatch(/"service_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toContain("NARA_API_KEY");
  expect(evidence).not.toContain("x-api-key");
});

test("Batch 942 publishes its exact coverage counters", async ({ request }) => {
  const response = await request.get("./data/stats.json");
  expect(response.ok()).toBeTruthy();
  const stats = await response.json();
  expect(stats).toMatchObject({
    source_rows: 23_978,
    person_entities: 23_936,
    possible_duplicate_groups: 640,
    research_attempted_people: 14_608,
    verified_affiliation_people: 1_038,
    verified_employer_people: 466,
    archival_review_assessed_people: 13_082,
    published_claims: 9_039,
    public_sources: 5_960,
  });
});
