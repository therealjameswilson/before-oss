import fs from "node:fs";
import { expect, test } from "@playwright/test";
import type { APIRequestContext } from "@playwright/test";

const evidence = fs.readFileSync(
  new URL(
    "../../research/evidence-page483-joseph-viggiani-to-edward-virant-review_batch-986_2026-10-30.json",
    import.meta.url,
  ),
  "utf8",
);

const profiles = [
  ["6f9085ff-c2a2-54f6-8ec2-217a88dcb1f7", "Joseph P Viggiani"],
  ["5f61bbe9-a98c-5670-8453-1de5c265b51e", "Joseph L Vigilante"],
  ["df1f0485-567f-5833-b0b0-2f67080c323c", "Marcel Vigneras"],
  ["c218bf1d-efe0-513b-bb68-ff2c95c2728c", "Edward Vignone"],
  ["56df289c-e56f-5592-95f3-b0b4be5c13d1", "Nick F Vigorito"],
  ["deec61f3-edad-5fb1-b317-eef2184557ed", "Joseph L Vigue"],
  ["3b20f467-2628-5548-a3c9-831fb8c122bd", "Gilberto M Vilante"],
  ["3e21b5fe-181b-5571-867d-0ae43c03e963", "William H Vilas"],
  ["71c7fd47-40ae-57e3-b04e-0fd529039894", "Joe S Villareal"],
  ["5f8a4e41-bba6-55fc-b3a0-232b36f135e1", "Andre L Villere"],
  ["d8849782-5880-557c-83eb-2d4182ae32ed", "Elizabeth E Vilm"],
  ["da7e8a80-a205-589c-b224-df0100bb220f", "Irving Vincent"],
  ["bdf2750a-14af-52c4-a95a-e2485245339d", "Stephen P Vinciguerra"],
  ["f870aed7-663c-5ec1-8fcd-7370ad1babeb", "Sterling N Vines"],
  ["438e4aaf-2eb4-5250-84d3-8f89e7df6d6d", "Noel E Vinette"],
  ["c9b4252e-240c-5cfc-b115-7a0cae99d101", "Harold O Vingers"],
  ["5342a233-a053-5580-a0ad-88c4a8dc85a4", "Jack Vinik"],
  ["a540b58a-56b0-5707-89c5-398a6a8fc1da", "Igor Vinner"],
  ["ca4f9532-b0d9-5591-8dbc-d9b78ff91aa7", "Paul Vinski"],
  ["5723612f-36ad-5320-8894-e6e7b7ad4bbd", "Hal D Vinson"],
  ["81f5edf0-f2fe-5edc-b672-e81cee13e4c2", "John H Vinson"],
  ["41606285-b3f2-5bb5-9589-6aff42ebb110", "Joseph E Viola"],
  ["721e0cdf-3b83-5a07-9096-cfa1be8acd89", "Edward J Virant"],
] as const;

async function publicPerson(request: APIRequestContext, id: string, name: string) {
  const first = name[0].toLowerCase();
  const shard = /^[a-z]$/.test(first) ? first : "other";
  const response = await request.get(`./data/people/${shard}.json`);
  expect(response.ok()).toBeTruthy();
  return (await response.json()).find((item: { person_id: string }) => item.person_id === id);
}

test("Batch 986 publishes all 23 audited people with terminal outcomes", async ({ page }) => {
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

test("reviewed Army bridges preserve broad categories and student status", async ({ request }) => {
  const expected = [
    ["6f9085ff-c2a2-54f6-8ec2-217a88dcb1f7", "Joseph P Viggiani", "unskilled textile-manufacturing occupation", "employment"],
    ["56df289c-e56f-5592-95f3-b0b4be5c13d1", "Nick F Vigorito", "semiskilled paper-goods manufacturing occupation", "employment"],
    ["deec61f3-edad-5fb1-b317-eef2184557ed", "Joseph L Vigue", "hotel or restaurant manager", "employment"],
    ["438e4aaf-2eb4-5250-84d3-8f89e7df6d6d", "Noel E Vinette", "student", "student"],
    ["c9b4252e-240c-5cfc-b115-7a0cae99d101", "Harold O Vingers", "salesperson", "employment"],
    ["5342a233-a053-5580-a0ad-88c4a8dc85a4", "Jack Vinik", "general office clerk", "employment"],
    ["ca4f9532-b0d9-5591-8dbc-d9b78ff91aa7", "Paul Vinski", "machinist", "employment"],
    ["721e0cdf-3b83-5a07-9096-cfa1be8acd89", "Edward J Virant", "unskilled metal-production occupation", "employment"],
  ] as const;
  for (const [id, name, occupation, relationship] of expected) {
    const person = await publicPerson(request, id, name);
    expect(person.identity_status).toBe("high_confidence");
    expect(person.other_pre_oss_affiliations).toEqual(expect.arrayContaining([
      expect.objectContaining({
        canonical_organization: null,
        occupation,
        relationship_type: relationship,
        temporal_basis: "strongly_date_bounded",
        claim_confidence: "medium",
        publication_status: "publish_qualified",
      }),
    ]));
  }
});

test("undefined Army codes create identities but no invented occupations", async ({ request }) => {
  for (const [id, name] of [
    ["71c7fd47-40ae-57e3-b04e-0fd529039894", "Joe S Villareal"],
    ["41606285-b3f2-5bb5-9589-6aff42ebb110", "Joseph E Viola"],
  ] as const) {
    const person = await publicPerson(request, id, name);
    expect(person).toMatchObject({ identity_status: "high_confidence", research_status: "requires_archival_review" });
    expect(person.immediate_pre_oss_affiliations).toHaveLength(0);
    expect(person.last_civilian_pre_service).toHaveLength(0);
    expect(person.other_pre_oss_affiliations).toHaveLength(0);
  }
});

test("Vigneras separates Smith employment from the French Army pathway", async ({ request }) => {
  const person = await publicPerson(request, "df1f0485-567f-5833-b0b0-2f67080c323c", "Marcel Vigneras");
  expect(person).toMatchObject({
    identity_status: "high_confidence",
    research_status: "verified_employer_found",
    personnel_category: "foreign_or_allied_military_personnel",
  });
  expect(person.last_civilian_pre_service).toEqual([
    expect.objectContaining({
      canonical_organization: "Smith College",
      relationship_type: "employment",
      claim_confidence: "high",
    }),
  ]);
  expect(person.immediate_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      canonical_organization: "French Army",
      relationship_type: "military_assignment",
      temporal_basis: "explicit_immediate",
      claim_confidence: "high",
    }),
  ]);
});

test("Vilm separates the Park Service employer from WAC service", async ({ request }) => {
  const person = await publicPerson(request, "d8849782-5880-557c-83eb-2d4182ae32ed", "Elizabeth E Vilm");
  expect(person).toMatchObject({
    identity_status: "high_confidence",
    research_status: "verified_employer_found",
    personnel_category: "commissioned_army_officer",
    commissioned_officer: true,
  });
  expect(person.last_civilian_pre_service).toEqual([
    expect.objectContaining({
      canonical_organization: "National Park Service",
      organization_name_as_found: "Crater Lake National Park Service",
      role_title: "assistant clerk",
      relationship_type: "employment",
    }),
  ]);
  expect(person.other_pre_oss_affiliations).toEqual(expect.arrayContaining([
    expect.objectContaining({
      canonical_organization: "Women's Army Corps",
      relationship_type: "military_assignment",
      temporal_basis: "temporal_relation_uncertain",
    }),
  ]));
});

test("Vinciguerra's Cornell evidence remains student status", async ({ request }) => {
  const person = await publicPerson(request, "bdf2750a-14af-52c4-a95a-e2485245339d", "Stephen P Vinciguerra");
  expect(person).toMatchObject({
    identity_status: "probable",
    research_status: "requires_archival_review",
    personnel_category: "commissioned_army_officer",
  });
  expect(person.last_civilian_pre_service).toHaveLength(0);
  expect(person.other_pre_oss_affiliations).toEqual(expect.arrayContaining([
    expect.objectContaining({
      canonical_organization: "Cornell University",
      relationship_type: "student",
      claim_confidence: "medium",
      publication_status: "publish_qualified",
    }),
  ]));
});

test("Villere's X-2 identity is confirmed without inventing an employer", async ({ request }) => {
  const person = await publicPerson(request, "5f8a4e41-bba6-55fc-b3a0-232b36f135e1", "Andre L Villere");
  expect(person).toMatchObject({
    identity_status: "confirmed",
    personnel_category: "enlisted_army_personnel",
    research_status: "requires_archival_review",
  });
  expect(person.immediate_pre_oss_affiliations).toHaveLength(0);
  expect(person.last_civilian_pre_service).toHaveLength(0);
  expect(person.other_pre_oss_affiliations).toHaveLength(0);
  expect(person.claims).toEqual(expect.arrayContaining([
    expect.objectContaining({ claim_type: "identity", claim_confidence: "confirmed" }),
  ]));
});

test("Vingers preserves earlier Stukins work and the last Kraft job", async ({ request }) => {
  const person = await publicPerson(request, "c9b4252e-240c-5cfc-b115-7a0cae99d101", "Harold O Vingers");
  expect(person).toMatchObject({ identity_status: "high_confidence", research_status: "verified_employer_found" });
  expect(person.last_civilian_pre_service).toEqual([
    expect.objectContaining({
      canonical_organization: "Kraft Cheese Company",
      organization_name_as_found: "Kraft Cheese Co.",
      occupation: "salesperson",
      claim_confidence: "high",
    }),
  ]);
  expect(person.other_pre_oss_affiliations).toEqual(expect.arrayContaining([
    expect.objectContaining({
      canonical_organization: "Stukins Distributing Company",
      occupation: "truck driver",
      temporal_basis: "documented_prewar",
    }),
  ]));
});

test("unbridged Batch 986 people remain affiliation-free archival cases", async ({ request }) => {
  const names = new Set([
    "Joseph L Vigilante", "Edward Vignone", "Gilberto M Vilante", "William H Vilas", "Irving Vincent",
    "Sterling N Vines", "Igor Vinner", "Hal D Vinson", "John H Vinson",
  ]);
  for (const [id, name] of profiles.filter(([, name]) => names.has(name))) {
    const person = await publicPerson(request, id, name);
    expect(person).toMatchObject({ identity_status: "unresolved", research_status: "requires_archival_review" });
    expect(person.immediate_pre_oss_affiliations).toHaveLength(0);
    expect(person.last_civilian_pre_service).toHaveLength(0);
    expect(person.other_pre_oss_affiliations).toHaveLength(0);
  }
});

test("Batch 986 evidence excludes secrets, full identifiers and raw bulk records", () => {
  expect(evidence).not.toMatch(/"serial_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toMatch(/"service_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toContain("NARA_API_KEY");
  expect(evidence).not.toContain("x-api-key");
  expect(evidence).not.toContain("candidate_identifier");
  expect(evidence).not.toContain("bulk_record_ordinal");
  expect(evidence).not.toMatch(/RA\d{8}/);
});

test("Batch 986 publishes exact coverage counters and preserves oil counts", async ({ request, page }) => {
  const response = await request.get("./data/stats.json");
  expect(response.ok()).toBeTruthy();
  expect(await response.json()).toMatchObject({
    source_rows: 23_978,
    person_entities: 23_936,
    possible_duplicate_groups: 672,
    research_attempted_people: 15_610,
    verified_affiliation_people: 1_127,
    verified_employer_people: 508,
    archival_review_assessed_people: 14_086,
    published_claims: 9_970,
    public_sources: 6_429,
  });
  await page.goto("./oil-companies/");
  const main = page.locator("main");
  await expect(main).toContainText("14 people");
  await expect(main).toContainText("15 historically named");
});
