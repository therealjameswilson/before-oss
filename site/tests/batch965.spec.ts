import fs from "node:fs";
import { expect, test } from "@playwright/test";
import type { APIRequestContext } from "@playwright/test";

const evidence = fs.readFileSync(
  new URL(
    "../../research/evidence-page473-edward-trevaskis-to-barry-trivers-review_batch-965_2026-10-29.json",
    import.meta.url,
  ),
  "utf8",
);

const profiles = [
  ["a86f8f5e-1b90-507d-8b07-156121038784", "Edward M Trevaskis"],
  ["cc6c821b-f2dd-5a1c-aea7-7075d9ed9f75", "Curtis D Trevathan"],
  ["01d9f8cd-245b-5f1d-931a-1bfde4a8846e", "Richard S Trevett"],
  ["849c7517-d88a-5db9-87e5-eb8d45592c13", "Arthur G Trevor Wilson"],
  ["53fea1d3-d777-5d70-b6e1-44d86bb73fab", "Glenn T Trewartha"],
  ["3805afc8-7986-5daf-9a0b-deca137f4390", "Leonard G Trexler"],
  ["e9ee2cd1-b2bf-5f49-9cf9-5b4e9dc92b29", "Philip Trezise"],
  ["a03f9a5e-c228-5651-bba5-20e98ad00c52", "Andre Tricard"],
  ["342ecd8d-85bb-5c7c-ab27-709c7bc95573", "Arthur Triebwasser"],
  ["e674cc03-2add-5526-b953-d389e2093d5e", "John E Triesner"],
  ["5cbcdd94-4fee-5e50-9bc2-51c4031de526", "Samuel L Trifiletti"],
  ["6bfa53b8-ca2d-5f76-9b0e-fbcdbb2d8e00", "Vincent J Trifletti"],
  ["01afa479-d58b-5c99-bc78-26a7f5b6f897", "Norman M Trigalet"],
  ["3d0e3029-78ca-510c-ae1f-32aafa4c5d0d", "Harold R Trimble"],
  ["3a2f3978-8978-58b2-a5c7-52df9fea8dbd", "Bonnell L Tripcony"],
  ["ab62ea6f-75de-567e-9524-8af26054a8d8", "Cecil L Triplett"],
  ["df5f7faa-df5d-5f9c-8a72-9587c69299a1", "Raymond E Triplett"],
  ["d2e3f6f2-942f-5d3e-b850-0913d39ba058", "Louis C Trippel"],
  ["04a73096-7a1f-5c3a-8aec-36b2a1320ab3", "George R Triska"],
  ["6eec0862-b778-5316-8dac-ac5a78be8dec", "Arthur A Tritsch"],
  ["a4007d7c-1236-5e83-b91b-9714712011e1", "Madeline E Tritsch"],
  ["3b46fb9d-a240-5366-856c-4db2e7c9fbf8", "Vaso Trivanovitch"],
  ["36192a2e-94fe-54fb-88bf-2b5d14d3c1b4", "Barry Trivers"],
] as const;

const unresolvedIds = new Set([
  "a03f9a5e-c228-5651-bba5-20e98ad00c52",
  "342ecd8d-85bb-5c7c-ab27-709c7bc95573",
  "3d0e3029-78ca-510c-ae1f-32aafa4c5d0d",
  "ab62ea6f-75de-567e-9524-8af26054a8d8",
  "d2e3f6f2-942f-5d3e-b850-0913d39ba058",
  "04a73096-7a1f-5c3a-8aec-36b2a1320ab3",
  "a4007d7c-1236-5e83-b91b-9714712011e1",
]);

const conflictIds = new Set([
  "a86f8f5e-1b90-507d-8b07-156121038784",
  "5cbcdd94-4fee-5e50-9bc2-51c4031de526",
]);

const armyProfiles = [
  ["cc6c821b-f2dd-5a1c-aea7-7075d9ed9f75", "Curtis D Trevathan", "apprentice to another trade", "high_confidence"],
  ["01d9f8cd-245b-5f1d-931a-1bfde4a8846e", "Richard S Trevett", "general office clerk", "confirmed"],
  ["3805afc8-7986-5daf-9a0b-deca137f4390", "Leonard G Trexler", "unskilled clay-products production occupation", "high_confidence"],
  ["e674cc03-2add-5526-b953-d389e2093d5e", "John E Triesner", "electrical engineer", "high_confidence"],
  ["01afa479-d58b-5c99-bc78-26a7f5b6f897", "Norman M Trigalet", "bartender", "high_confidence"],
  ["df5f7faa-df5d-5f9c-8a72-9587c69299a1", "Raymond E Triplett", "photographer", "high_confidence"],
] as const;

async function publicPerson(request: APIRequestContext, id: string, name: string) {
  const response = await request.get(`./data/people/${name[0].toLowerCase()}.json`);
  expect(response.ok()).toBeTruthy();
  return (await response.json()).find((item: { person_id: string }) => item.person_id === id);
}

test("Batch 965 publishes 23 audited people with terminal outcomes", async ({ page }) => {
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

test("six Army bridges publish dated occupation categories but no named employer", async ({ request }) => {
  for (const [id, name, occupation, identityStatus] of armyProfiles) {
    const person = await publicPerson(request, id, name);
    expect(person).toMatchObject({
      identity_status: identityStatus,
      personnel_category: "enlisted_army_personnel",
      commissioned_officer: false,
      research_status: "occupation_only_found",
    });
    expect(person.immediate_pre_oss_affiliations).toHaveLength(0);
    expect(person.last_civilian_pre_service).toHaveLength(0);
    expect(person.other_pre_oss_affiliations).toEqual(expect.arrayContaining([
      expect.objectContaining({
        canonical_organization: null,
        occupation,
        relationship_type: "employment",
        temporal_basis: "strongly_date_bounded",
        claim_confidence: "medium",
      }),
    ]));
  }
});

test("Philip Trezise has an explicit Navy-to-OSS affiliation and no invented university job", async ({ request }) => {
  const person = await publicPerson(request, "e9ee2cd1-b2bf-5f49-9cf9-5b4e9dc92b29", "Philip Trezise");
  expect(person).toMatchObject({ identity_status: "confirmed", research_status: "requires_archival_review" });
  expect(person.immediate_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      canonical_organization: "United States Navy",
      relationship_type: "military_assignment",
      temporal_basis: "explicit_immediate",
      claim_confidence: "confirmed",
    }),
  ]);
  expect(JSON.stringify([
    ...person.immediate_pre_oss_affiliations,
    ...person.last_civilian_pre_service,
    ...person.other_pre_oss_affiliations,
  ])).not.toContain("St. John's University");
});

test("documented prewar employment remains visibly qualified", async ({ request }) => {
  const trewartha = await publicPerson(request, "53fea1d3-d777-5d70-b6e1-44d86bb73fab", "Glenn T Trewartha");
  expect(trewartha).toMatchObject({ identity_status: "probable", research_status: "documented_prewar_employer_found" });
  expect(trewartha.other_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      canonical_organization: "University of Wisconsin-Madison",
      occupation: "geography professor",
      end_date: null,
      temporal_basis: "documented_prewar",
      claim_confidence: "medium",
    }),
  ]);

  const trivanovitch = await publicPerson(request, "3b46fb9d-a240-5366-856c-4db2e7c9fbf8", "Vaso Trivanovitch");
  expect(trivanovitch).toMatchObject({ identity_status: "probable", research_status: "documented_prewar_employer_found" });
  expect(trivanovitch.other_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      canonical_organization: "National Industrial Conference Board",
      occupation: "economist",
      temporal_basis: "documented_prewar",
      claim_confidence: "medium",
    }),
  ]);
});

test("two rejected Army candidates remain conflicts without transferred fields", async ({ request }) => {
  for (const [id, name] of profiles.filter(([id]) => conflictIds.has(id))) {
    const person = await publicPerson(request, id, name);
    expect(person).toMatchObject({ identity_status: "conflicting", research_status: "conflicting_sources" });
    expect(person.immediate_pre_oss_affiliations).toHaveLength(0);
    expect(person.last_civilian_pre_service).toHaveLength(0);
    expect(person.other_pre_oss_affiliations).toHaveLength(0);
    expect(person.claims).toEqual([
      expect.objectContaining({ claim_type: "identity", claim_confidence: "conflicting" }),
    ]);
  }
});

test("seven unresolved people retain archival outcomes without namesake facts", async ({ request }) => {
  for (const [id, name] of profiles.filter(([id]) => unresolvedIds.has(id))) {
    const person = await publicPerson(request, id, name);
    expect(person).toMatchObject({ identity_status: "unresolved", research_status: "requires_archival_review" });
    expect(person.immediate_pre_oss_affiliations).toHaveLength(0);
    expect(person.last_civilian_pre_service).toHaveLength(0);
    expect(person.other_pre_oss_affiliations).toHaveLength(0);
    expect(person.claims).toHaveLength(0);
  }
});

test("Vincent Trifletti uses an archival identifier without linking a hijacked host", async ({ request }) => {
  const person = await publicPerson(request, "6bfa53b8-ca2d-5f76-9b0e-fbcdbb2d8e00", "Vincent J Trifletti");
  const serialized = JSON.stringify(person);
  expect(serialized).toContain("NND 87790");
  expect(serialized).not.toContain("javadc.org");
});

test("Batch 965 evidence excludes secrets and protected identifiers", () => {
  expect(evidence).not.toMatch(/"serial_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toMatch(/"service_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toContain("NARA_API_KEY");
  expect(evidence).not.toContain("x-api-key");
  expect(evidence).not.toContain("bulk_record_ordinal");
});

test("Batch 965 publishes exact coverage counters without changing the oil category", async ({ request, page }) => {
  const response = await request.get("./data/stats.json");
  expect(response.ok()).toBeTruthy();
  expect(await response.json()).toMatchObject({
    source_rows: 23_978,
    person_entities: 23_936,
    possible_duplicate_groups: 663,
    research_attempted_people: 15_131,
    verified_affiliation_people: 1_085,
    verified_employer_people: 486,
    archival_review_assessed_people: 13_607,
    published_claims: 9_513,
    public_sources: 6_187,
  });
  await page.goto("./oil-companies/");
  const main = page.locator("main");
  await expect(main).toContainText("14 people");
  await expect(main).toContainText("15 historically named");
  await expect(main).not.toContainText("Students");
});
