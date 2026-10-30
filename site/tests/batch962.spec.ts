import fs from "node:fs";
import { expect, test } from "@playwright/test";
import type { APIRequestContext } from "@playwright/test";

const evidence = fs.readFileSync(
  new URL(
    "../../research/evidence-pages471-472-james-townsend-to-charles-traina-review_batch-962_2026-10-29.json",
    import.meta.url,
  ),
  "utf8",
);

const profiles = [
  ["48ff5ccc-e2a8-5543-9206-76a5d36cb222", "James B Townsend"],
  ["1437d5c3-6b63-50bf-b7ac-d9b0a49f74e9", "Jeannette R Townsend"],
  ["d56a05ad-9fe9-561e-9d63-ff7dd098ee0c", "Leo H Townsend"],
  ["8bd5bcba-2e9b-54f9-8f2a-38daa35fb8a7", "Milton E Townsend"],
  ["b1b9d5ca-78c5-527a-9366-3fb396fc7796", "Orlan W Townsend"],
  ["68a2da5e-5333-5f96-a361-5c22854d13e9", "David Toy"],
  ["f3313c26-3558-5377-ad45-cecd72b0f2a4", "William K Toy"],
  ["a1e38e18-c5ae-5cc3-a2db-522d6664ffcb", "Reisuke Toyota"],
  ["f2f63570-ae04-5111-a4a7-d180d6b87d1b", "Alfred M Tozzer"],
  ["241085e9-f6a8-52f7-a727-a514be0b9391", "John J Tozzi"],
  ["63c3f3c6-df53-5c7c-97bc-fe804893d867", "Barney Traban"],
  ["0bda4bcd-cb33-5c31-bd2d-3a8384b26221", "James Traban"],
  ["72befc48-12a9-5333-ab64-fe12e49be23b", "Warren E Trabant"],
  ["7501e285-9ad5-5347-807a-1c894fdaccf7", "Carl H Tracey"],
  ["96d9c3f9-ca3e-5788-938a-21c19c1ee55f", "Mabel J Tracy"],
  ["db981169-19f4-5828-b50b-439d8efc9a51", "Ollie L Tracy"],
  ["6b6c809a-a23d-540a-9485-66e1aaf0267a", "Robert N Tracy"],
  ["b3ce34fe-80ed-5b59-8f98-729839a7f37f", "Thomas J Tracy"],
  ["ac5cf5e8-40ec-5fc6-a5a7-f4ce8bf8a6fd", "Paul J Traficante"],
  ["466461a8-0903-5e7a-bb5b-22f9d2b4509e", "Robert A Trago"],
  ["7fad710b-37d3-56df-92db-a755b1f3ffb8", "Robert A Trago"],
  ["65645d3d-9a3a-5362-a354-1f0ac64b2dbf", "Lufra J Trahan"],
  ["972360b1-2e11-5969-bc8b-29d761b88b00", "Charles J Traina"],
] as const;

const unresolvedIds = new Set([
  "48ff5ccc-e2a8-5543-9206-76a5d36cb222",
  "1437d5c3-6b63-50bf-b7ac-d9b0a49f74e9",
  "d56a05ad-9fe9-561e-9d63-ff7dd098ee0c",
  "8bd5bcba-2e9b-54f9-8f2a-38daa35fb8a7",
  "b1b9d5ca-78c5-527a-9366-3fb396fc7796",
  "68a2da5e-5333-5f96-a361-5c22854d13e9",
  "f3313c26-3558-5377-ad45-cecd72b0f2a4",
  "241085e9-f6a8-52f7-a727-a514be0b9391",
  "72befc48-12a9-5333-ab64-fe12e49be23b",
  "7501e285-9ad5-5347-807a-1c894fdaccf7",
  "96d9c3f9-ca3e-5788-938a-21c19c1ee55f",
  "db981169-19f4-5828-b50b-439d8efc9a51",
  "6b6c809a-a23d-540a-9485-66e1aaf0267a",
  "972360b1-2e11-5969-bc8b-29d761b88b00",
]);

async function publicPerson(request: APIRequestContext, id: string, name: string) {
  const response = await request.get(`./data/people/${name[0].toLowerCase()}.json`);
  expect(response.ok()).toBeTruthy();
  return (await response.json()).find((item: { person_id: string }) => item.person_id === id);
}

test("Batch 962 publishes 23 audited people with terminal outcomes", async ({ page }) => {
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

test("Alfred Tozzer publishes Harvard as the last documented civilian employer", async ({ request }) => {
  const person = await publicPerson(request, "f2f63570-ae04-5111-a4a7-d180d6b87d1b", "Alfred M Tozzer");
  expect(person).toMatchObject({ identity_status: "high_confidence", research_status: "verified_employer_found" });
  expect(person.immediate_pre_oss_affiliations).toHaveLength(0);
  expect(person.last_civilian_pre_service).toEqual([
    expect.objectContaining({
      canonical_organization: "Harvard University",
      relationship_type: "employment",
      role_title: "professor of anthropology",
      temporal_basis: "strongly_date_bounded",
      claim_confidence: "high",
    }),
  ]);
});

test("Barney Traban keeps an explicit Army pathway separate from employment", async ({ request }) => {
  const person = await publicPerson(request, "63c3f3c6-df53-5c7c-97bc-fe804893d867", "Barney Traban");
  expect(person).toMatchObject({ identity_status: "high_confidence", research_status: "completed" });
  expect(person.immediate_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      canonical_organization: "United States Army Replacement Center in Italy",
      relationship_type: "military_assignment",
      temporal_basis: "explicit_immediate",
      claim_confidence: "high",
    }),
  ]);
  expect(person.last_civilian_pre_service).toHaveLength(0);
});

test("James Traban preserves the identifier conflict and receives no transferred facts", async ({ request }) => {
  const person = await publicPerson(request, "0bda4bcd-cb33-5c31-bd2d-3a8384b26221", "James Traban");
  expect(person).toMatchObject({ identity_status: "conflicting", research_status: "conflicting_sources" });
  expect(person.immediate_pre_oss_affiliations).toHaveLength(0);
  expect(person.last_civilian_pre_service).toHaveLength(0);
  expect(person.other_pre_oss_affiliations).toHaveLength(0);
  expect(person.claims).toEqual([
    expect.objectContaining({ claim_type: "identity", claim_confidence: "conflicting", publication_status: "conflicting" }),
  ]);
});

test("Thomas Tracy's Army category remains an occupation without an invented employer", async ({ request }) => {
  const person = await publicPerson(request, "b3ce34fe-80ed-5b59-8f98-729839a7f37f", "Thomas J Tracy");
  expect(person).toMatchObject({ identity_status: "high_confidence", research_status: "occupation_only_found" });
  expect(person.immediate_pre_oss_affiliations).toHaveLength(0);
  expect(person.last_civilian_pre_service).toHaveLength(0);
  expect(person.other_pre_oss_affiliations).toEqual([
    expect.objectContaining({ canonical_organization: null, occupation: "Stock clerks", claim_confidence: "medium" }),
  ]);
});

test("Paul Traficante's confirmed OSS identity does not invent a prior employer", async ({ request }) => {
  const person = await publicPerson(request, "ac5cf5e8-40ec-5fc6-a5a7-f4ce8bf8a6fd", "Paul J Traficante");
  expect(person).toMatchObject({ identity_status: "confirmed", research_status: "requires_archival_review" });
  expect(person.immediate_pre_oss_affiliations).toHaveLength(0);
  expect(person.last_civilian_pre_service).toHaveLength(0);
  expect(person.other_pre_oss_affiliations).toHaveLength(0);
});

test("Lufra Trahan keeps LSU student status distinct from employment", async ({ request }) => {
  const person = await publicPerson(request, "65645d3d-9a3a-5362-a354-1f0ac64b2dbf", "Lufra J Trahan");
  expect(person).toMatchObject({ identity_status: "confirmed", research_status: "requires_archival_review" });
  expect(person.last_civilian_pre_service).toHaveLength(0);
  expect(person.other_pre_oss_affiliations).toEqual([
    expect.objectContaining({ canonical_organization: "Louisiana State University", relationship_type: "student", end_date: "1934" }),
  ]);
});

test("Reisuke Toyota's undated faculty role stays qualified", async ({ request }) => {
  const person = await publicPerson(request, "a1e38e18-c5ae-5cc3-a2db-522d6664ffcb", "Reisuke Toyota");
  expect(person).toMatchObject({ identity_status: "high_confidence", research_status: "requires_archival_review" });
  expect(person.immediate_pre_oss_affiliations).toHaveLength(0);
  expect(person.last_civilian_pre_service).toHaveLength(0);
  expect(person.other_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      canonical_organization: "Military Intelligence Service Language School",
      relationship_type: "government_assignment",
      temporal_basis: "temporal_relation_uncertain",
      claim_confidence: "medium",
    }),
  ]);
});

test("the two Robert Trago rows remain separate ambiguous profiles", async ({ request }) => {
  const first = await publicPerson(request, "466461a8-0903-5e7a-bb5b-22f9d2b4509e", "Robert A Trago");
  const second = await publicPerson(request, "7fad710b-37d3-56df-92db-a755b1f3ffb8", "Robert A Trago");
  expect(first).toMatchObject({ identity_status: "ambiguous", research_status: "requires_archival_review" });
  expect(second).toMatchObject({ identity_status: "ambiguous", research_status: "requires_archival_review" });
  expect(first.person_id).not.toBe(second.person_id);
  expect(first.possible_duplicate_group).toBe(second.possible_duplicate_group);
  expect(first.claims).toHaveLength(0);
  expect(second.claims).toHaveLength(0);
});

test("unresolved people retain archival outcomes without transferred facts", async ({ request }) => {
  for (const [id, name] of profiles.filter(([id]) => unresolvedIds.has(id))) {
    const person = await publicPerson(request, id, name);
    expect(person).toMatchObject({ identity_status: "unresolved", research_status: "requires_archival_review" });
    expect(person.immediate_pre_oss_affiliations).toHaveLength(0);
    expect(person.last_civilian_pre_service).toHaveLength(0);
    expect(person.other_pre_oss_affiliations).toHaveLength(0);
    expect(person.claims).toHaveLength(0);
  }
});

test("Batch 962 evidence excludes secrets and protected identifiers", () => {
  expect(evidence).not.toMatch(/"serial_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toMatch(/"service_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toContain("NARA_API_KEY");
  expect(evidence).not.toContain("x-api-key");
  expect(evidence).not.toContain("bulk_record_ordinal");
});

test("Batch 962 publishes exact coverage counters without changing the oil category", async ({ request, page }) => {
  const response = await request.get("./data/stats.json");
  expect(response.ok()).toBeTruthy();
  expect(await response.json()).toMatchObject({
    source_rows: 23_978,
    person_entities: 23_936,
    possible_duplicate_groups: 662,
    research_attempted_people: 15_064,
    verified_affiliation_people: 1_084,
    verified_employer_people: 486,
    archival_review_assessed_people: 13_540,
    published_claims: 9_449,
    public_sources: 6_159,
  });
  await page.goto("./oil-companies/");
  const main = page.locator("main");
  await expect(main).toContainText("14 people");
  await expect(main).toContainText("15 historically named");
  await expect(main).not.toContainText("Harvard University");
});
