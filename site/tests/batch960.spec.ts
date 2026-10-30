import fs from "node:fs";
import { expect, test } from "@playwright/test";
import type { APIRequestContext } from "@playwright/test";

const evidence = fs.readFileSync(
  new URL(
    "../../research/evidence-page470-471-william-tommaselli-to-andrew-torrielli-review_batch-960_2026-10-29.json",
    import.meta.url,
  ),
  "utf8",
);

const profiles = [
  ["992b1460-7ac8-5143-bc1b-c6988825a7dd", "William Tommaselli"],
  ["adb891cf-7fcb-566f-8f65-7cb03759880a", "James Tonas"],
  ["01cdf4be-55c7-5363-8616-6c8d9c30396d", "Albert P Toner"],
  ["8c2fa4a7-79ce-5cb6-94b2-bdd3a62d9cd6", "Williams Tonesk"],
  ["09c6b8d8-d95e-5dd9-8159-157d75226ae8", "Cleo Toney"],
  ["cefa0781-3205-501d-b471-654156ee46e7", "Henry K Tong"],
  ["54afd4bf-9e0c-5128-8a61-8e95af05ab39", "Kam D Tong"],
  ["e0c8562b-11de-5ec4-bd8a-f77ae1d09ec0", "Singkata Tongyai"],
  ["e209f10a-8ffa-57b5-84ae-2bde8d0d6009", "Heldur Tonisson"],
  ["bec54ce9-9f30-585f-a8d3-40f3d69056b9", "Bruce L Tonks"],
  ["646b0a43-8828-59f5-ace4-c3b6eb7a5372", "Carlo D Tonno"],
  ["cdf5e832-7e02-5d0f-8f95-1881bea19c97", "Signa E Toole"],
  ["12d621e0-b818-599b-ba57-06d4ecc185ba", "Alfred G Toombs"],
  ["0c3ec0ff-f10a-5996-b4b1-6559a737d997", "Clarence S Topp"],
  ["37658069-28b0-5005-aa4d-853c327d6a29", "Dwight M Tordter"],
  ["11073e78-1467-5b62-b48b-aaf3c14539ba", "Milton F Torem"],
  ["8cb368fe-7899-505a-a7f3-42c0364eb8f1", "Jean T Torgerson"],
  ["fddc196b-b62a-5af5-a926-57aa5bac6c74", "Alex J Torma"],
  ["0df4d4e9-ca8d-520a-8c72-112be29ca903", "Algot Torneman"],
  ["b6e24bd4-6a99-56f8-a4de-435dcb4a4639", "Norma E Tornquist"],
  ["df1f03f6-c447-5815-9f14-937e93fea776", "Jack Torosky"],
  ["55f01433-3660-5589-81e9-f7fdcd326074", "Christopher Torper"],
  ["961cbce5-a593-57d3-a344-3b7094e38fe5", "Andrew J Torrielli"],
] as const;

const unresolvedIds = new Set([
  "bec54ce9-9f30-585f-a8d3-40f3d69056b9",
  "646b0a43-8828-59f5-ace4-c3b6eb7a5372",
  "cdf5e832-7e02-5d0f-8f95-1881bea19c97",
  "12d621e0-b818-599b-ba57-06d4ecc185ba",
  "0c3ec0ff-f10a-5996-b4b1-6559a737d997",
  "37658069-28b0-5005-aa4d-853c327d6a29",
  "8cb368fe-7899-505a-a7f3-42c0364eb8f1",
  "b6e24bd4-6a99-56f8-a4de-435dcb4a4639",
]);

async function publicPerson(request: APIRequestContext, id: string, name: string) {
  const response = await request.get(`./data/people/${name[0].toLowerCase()}.json`);
  expect(response.ok()).toBeTruthy();
  return (await response.json()).find((item: { person_id: string }) => item.person_id === id);
}

test("Batch 960 publishes 23 audited people with terminal outcomes", async ({ page }) => {
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

test("Albert Toner keeps a government predecessor distinct from civilian employer analytics", async ({ request }) => {
  const person = await publicPerson(request, "01cdf4be-55c7-5363-8616-6c8d9c30396d", "Albert P Toner");
  expect(person).toMatchObject({ identity_status: "confirmed", research_status: "completed" });
  expect(person.immediate_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      canonical_organization: "Public Buildings Administration, Federal Works Agency",
      relationship_type: "government_assignment",
      temporal_basis: "explicit_immediate",
      claim_confidence: "confirmed",
    }),
  ]);
  expect(person.last_civilian_pre_service).toHaveLength(0);
});

test("Williams Tonesk remains probable while preserving each documented pathway", async ({ request, page }) => {
  const person = await publicPerson(request, "8c2fa4a7-79ce-5cb6-94b2-bdd3a62d9cd6", "Williams Tonesk");
  expect(person).toMatchObject({ identity_status: "probable", research_status: "documented_prewar_employer_found" });
  expect(person.name_variants).toContain("William John Tonesk");
  expect(person.last_civilian_pre_service).toEqual([
    expect.objectContaining({ canonical_organization: "Pan American Airways", claim_confidence: "medium" }),
  ]);
  expect(person.immediate_pre_oss_affiliations).toEqual([
    expect.objectContaining({ canonical_organization: "Office of Naval Intelligence", relationship_type: "military_assignment" }),
  ]);
  expect(person.other_pre_oss_affiliations).toEqual(expect.arrayContaining([
    expect.objectContaining({ canonical_organization: "International Telephone and Telegraph Corporation" }),
    expect.objectContaining({ canonical_organization: "Raymond Whitcomb, Inc." }),
  ]));
  await page.goto("./people/8c2fa4a7-79ce-5cb6-94b2-bdd3a62d9cd6/");
  await expect(page.locator("main")).toContainText("probable");
});

test("Army categories remain occupations without invented employers", async ({ request }) => {
  for (const [id, name, occupation] of [
    ["992b1460-7ac8-5143-bc1b-c6988825a7dd", "William Tommaselli", "Chauffeurs and drivers, bus, taxi, truck, tractor"],
    ["09c6b8d8-d95e-5dd9-8159-157d75226ae8", "Cleo Toney", "Miners and mining-machine operators"],
    ["cefa0781-3205-501d-b471-654156ee46e7", "Henry K Tong", "Retail managers"],
    ["fddc196b-b62a-5af5-a926-57aa5bac6c74", "Alex J Torma", "Painters, except construction and maintenance"],
    ["55f01433-3660-5589-81e9-f7fdcd326074", "Christopher Torper", "Blacksmiths, forgemen, and hammermen"],
  ] as const) {
    const person = await publicPerson(request, id, name);
    expect(person).toMatchObject({ identity_status: "high_confidence", research_status: "occupation_only_found" });
    expect(person.immediate_pre_oss_affiliations).toHaveLength(0);
    expect(person.last_civilian_pre_service).toHaveLength(0);
    expect(person.other_pre_oss_affiliations).toEqual([
      expect.objectContaining({ canonical_organization: null, occupation }),
    ]);
  }
});

test("student and foreign institutional affiliations are not labeled as employers", async ({ request }) => {
  for (const [id, name, organization] of [
    ["e0c8562b-11de-5ec4-bd8a-f77ae1d09ec0", "Singkata Tongyai", "Michigan State College"],
    ["e209f10a-8ffa-57b5-84ae-2bde8d0d6009", "Heldur Tonisson", "University of Tartu"],
  ] as const) {
    const person = await publicPerson(request, id, name);
    expect(person.last_civilian_pre_service).toHaveLength(0);
    expect(person.other_pre_oss_affiliations).toEqual([
      expect.objectContaining({ canonical_organization: organization, relationship_type: "student" }),
    ]);
  }
});

test("shared identifiers remain visible conflicts rather than silent merges", async ({ request }) => {
  const james = await publicPerson(request, "adb891cf-7fcb-566f-8f65-7cb03759880a", "James Tonas");
  expect(james).toMatchObject({ identity_status: "conflicting", research_status: "conflicting_sources" });
  expect(james.claims).toEqual([expect.objectContaining({ claim_confidence: "conflicting" })]);
  expect(james.other_pre_oss_affiliations).toHaveLength(0);

  const jack = await publicPerson(request, "df1f03f6-c447-5815-9f14-937e93fea776", "Jack Torosky");
  expect(jack).toMatchObject({ identity_status: "probable", research_status: "occupation_only_found" });
  expect(jack.other_pre_oss_affiliations).toEqual([
    expect.objectContaining({ occupation: "Civil engineers", claim_confidence: "medium" }),
  ]);
});

test("eight unresolved people retain archival outcomes without transferred facts", async ({ request }) => {
  for (const [id, name] of profiles.filter(([id]) => unresolvedIds.has(id))) {
    const person = await publicPerson(request, id, name);
    expect(person).toMatchObject({ identity_status: "unresolved", research_status: "requires_archival_review" });
    expect(person.immediate_pre_oss_affiliations).toHaveLength(0);
    expect(person.last_civilian_pre_service).toHaveLength(0);
    expect(person.other_pre_oss_affiliations).toHaveLength(0);
    expect(person.claims).toHaveLength(0);
  }
});

test("Batch 960 evidence excludes secrets and protected identifiers", () => {
  expect(evidence).not.toMatch(/"serial_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toMatch(/"service_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toContain("NARA_API_KEY");
  expect(evidence).not.toContain("x-api-key");
  expect(evidence).not.toContain("bulk_record_ordinal");
});

test("Batch 960 publishes exact coverage counters without changing the oil category", async ({ request, page }) => {
  const response = await request.get("./data/stats.json");
  expect(response.ok()).toBeTruthy();
  expect(await response.json()).toMatchObject({
    source_rows: 23_978,
    person_entities: 23_936,
    possible_duplicate_groups: 658,
    research_attempted_people: 15_018,
    verified_affiliation_people: 1_078,
    verified_employer_people: 484,
    archival_review_assessed_people: 13_494,
    published_claims: 9_407,
    public_sources: 6_133,
  });
  await page.goto("./oil-companies/");
  const main = page.locator("main");
  await expect(main).toContainText("14 people");
  await expect(main).toContainText("15 historically named");
  await expect(main).not.toContainText("Pan American Airways");
});
