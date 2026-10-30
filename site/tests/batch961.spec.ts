import fs from "node:fs";
import { expect, test } from "@playwright/test";
import type { APIRequestContext } from "@playwright/test";

const evidence = fs.readFileSync(
  new URL(
    "../../research/evidence-page471-fulton-torry-to-campbell-townsend-review_batch-961_2026-10-29.json",
    import.meta.url,
  ),
  "utf8",
);

const profiles = [
  ["7cce93cf-1573-5348-8fe2-06eefb1881f1", "Fulton B Torry"],
  ["fadb13e5-8789-5d88-99d6-19899144581f", "Ivan L Tors"],
  ["c196ef9d-7da3-5d21-a76e-d3b6253e1a6d", "Samuel J Toscano"],
  ["bfd0e358-bde8-554e-bcbc-0fa97266da46", "Alvin Toso"],
  ["83f43e3e-486d-5cb6-99b1-57a63f440526", "Louis C Tossy"],
  ["bdc4c7f4-1391-5279-8027-0de411dc2dbe", "Henri S Tosy"],
  ["c0ede82a-f3a6-5a4f-99dd-a543647db0e9", "Charles M Toth"],
  ["1ac4f57c-668e-5957-9783-55f13f4fd885", "Frank S Toth"],
  ["fa84528c-a191-5a70-ae2d-c6f480d35c63", "Gordon K Totten"],
  ["349e5385-11af-5d13-a55a-6720cbd23624", "Lowell S Totton"],
  ["572de7a9-c6e3-53c1-9d1d-7f1ca5516c05", "Calvin A Tottori"],
  ["96db45dd-3f47-5c96-b15f-226b4c8956f2", "John E Toulmin"],
  ["35e93c41-be61-545d-b2c2-1e3b70973b95", "Robert J Tousignant"],
  ["1ee653dc-122f-5dfa-9151-bc0676f56454", "George H Touslay"],
  ["2082513f-fd12-55cd-bdcd-cce06e7e50f0", "Bernardo H Tovar"],
  ["983bf923-9d2c-5849-b479-5e3a0e6fc801", "Bernard A Towell"],
  ["2190dafe-14fd-5973-b94f-21335d626562", "James A Tower"],
  ["e6f0686a-c4c3-5edc-b84a-db3e3da409c6", "James M Towle"],
  ["77e34712-a863-5b34-b0ae-eb3301b302f5", "Frank M Towne"],
  ["5e4380ad-c504-584b-8198-38cb4db9fa4c", "Hazen A Towne"],
  ["58272cdf-0f08-5172-b65d-0b80d251f536", "Elsie S Townlsey"],
  ["4c5aa755-2add-5a7f-9f62-4b7c80830c88", "Marion Towns"],
  ["cc737543-a7a4-5200-be84-326a52ee892a", "Campbell Townsend"],
] as const;

const unresolvedIds = new Set([
  "83f43e3e-486d-5cb6-99b1-57a63f440526",
  "fa84528c-a191-5a70-ae2d-c6f480d35c63",
  "35e93c41-be61-545d-b2c2-1e3b70973b95",
  "1ee653dc-122f-5dfa-9151-bc0676f56454",
  "2190dafe-14fd-5973-b94f-21335d626562",
  "4c5aa755-2add-5a7f-9f62-4b7c80830c88",
]);

async function publicPerson(request: APIRequestContext, id: string, name: string) {
  const response = await request.get(`./data/people/${name[0].toLowerCase()}.json`);
  expect(response.ok()).toBeTruthy();
  return (await response.json()).find((item: { person_id: string }) => item.person_id === id);
}

test("Batch 961 publishes 23 audited people with terminal outcomes", async ({ page }) => {
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

test("John Toulmin publishes a last civilian employer without inventing an immediate transfer", async ({ request }) => {
  const person = await publicPerson(request, "96db45dd-3f47-5c96-b15f-226b4c8956f2", "John E Toulmin");
  expect(person).toMatchObject({ identity_status: "high_confidence", research_status: "verified_employer_found" });
  expect(person.immediate_pre_oss_affiliations).toHaveLength(0);
  expect(person.last_civilian_pre_service).toEqual([
    expect.objectContaining({
      canonical_organization: "First National Bank of Boston",
      relationship_type: "employment",
      role_title: "vice president",
      temporal_basis: "strongly_date_bounded",
      claim_confidence: "high",
    }),
  ]);
});

test("Ivan Tors keeps military, student, and occupational pathways distinct", async ({ request }) => {
  const person = await publicPerson(request, "fadb13e5-8789-5d88-99d6-19899144581f", "Ivan L Tors");
  expect(person).toMatchObject({ identity_status: "high_confidence", research_status: "completed" });
  expect(person.immediate_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      canonical_organization: "United States Army Air Forces",
      relationship_type: "military_assignment",
      temporal_basis: "probable_immediate",
      claim_confidence: "medium",
    }),
  ]);
  expect(person.last_civilian_pre_service).toHaveLength(0);
  expect(person.other_pre_oss_affiliations).toEqual(expect.arrayContaining([
    expect.objectContaining({ canonical_organization: "Fordham University", relationship_type: "student" }),
    expect.objectContaining({ canonical_organization: null, occupation: "playwright" }),
  ]));
});

test("Bernardo Tovar keeps Harvard student status separate from the Army pathway", async ({ request }) => {
  const person = await publicPerson(request, "2082513f-fd12-55cd-bdcd-cce06e7e50f0", "Bernardo H Tovar");
  expect(person).toMatchObject({ identity_status: "high_confidence", research_status: "completed" });
  expect(person.immediate_pre_oss_affiliations).toEqual([
    expect.objectContaining({ canonical_organization: "United States Army", relationship_type: "military_assignment" }),
  ]);
  expect(person.last_civilian_pre_service).toHaveLength(0);
  expect(person.other_pre_oss_affiliations).toEqual([
    expect.objectContaining({ canonical_organization: "Harvard University", relationship_type: "student" }),
  ]);
});

test("Army categories remain occupations without invented employers", async ({ request }) => {
  for (const [id, name, occupation] of [
    ["7cce93cf-1573-5348-8fe2-06eefb1881f1", "Fulton B Torry", "Stock clerks"],
    ["c0ede82a-f3a6-5a4f-99dd-a543647db0e9", "Charles M Toth", "Semiskilled machine-shop and related occupations, n.e.c."],
    ["349e5385-11af-5d13-a55a-6720cbd23624", "Lowell S Totton", "Financial institution clerks, n.e.c."],
    ["e6f0686a-c4c3-5edc-b84a-db3e3da409c6", "James M Towle", "Semiskilled occupations in production of bakery products, n.e.c."],
    ["77e34712-a863-5b34-b0ae-eb3301b302f5", "Frank M Towne", "Teachers (secondary school) and principals"],
    ["cc737543-a7a4-5200-be84-326a52ee892a", "Campbell Townsend", "Architects"],
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

test("confirmed OSS identities do not receive invented pre-OSS affiliations", async ({ request }) => {
  for (const [id, name] of [
    ["c196ef9d-7da3-5d21-a76e-d3b6253e1a6d", "Samuel J Toscano"],
    ["bfd0e358-bde8-554e-bcbc-0fa97266da46", "Alvin Toso"],
    ["983bf923-9d2c-5849-b479-5e3a0e6fc801", "Bernard A Towell"],
  ] as const) {
    const person = await publicPerson(request, id, name);
    expect(person.identity_status).toBe("confirmed");
    expect(person.research_status).toBe("requires_archival_review");
    expect(person.immediate_pre_oss_affiliations).toHaveLength(0);
    expect(person.last_civilian_pre_service).toHaveLength(0);
    expect(person.other_pre_oss_affiliations).toHaveLength(0);
  }
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

test("Elsie Townlsey preserves the printed spelling and qualified Townsley variant", async ({ request }) => {
  const person = await publicPerson(request, "58272cdf-0f08-5172-b65d-0b80d251f536", "Elsie S Townlsey");
  expect(person).toMatchObject({ display_name: "Elsie S Townlsey", identity_status: "ambiguous", research_status: "requires_archival_review" });
  expect(person.name_variants).toContain("Elsie S Townsley");
  expect(person.claims).toHaveLength(0);
});

test("Batch 961 evidence excludes secrets and protected identifiers", () => {
  expect(evidence).not.toMatch(/"serial_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toMatch(/"service_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toContain("NARA_API_KEY");
  expect(evidence).not.toContain("x-api-key");
  expect(evidence).not.toContain("bulk_record_ordinal");
});

test("Batch 961 publishes exact coverage counters without changing the oil category", async ({ request, page }) => {
  const response = await request.get("./data/stats.json");
  expect(response.ok()).toBeTruthy();
  expect(await response.json()).toMatchObject({
    source_rows: 23_978,
    person_entities: 23_936,
    possible_duplicate_groups: 660,
    research_attempted_people: 15_041,
    verified_affiliation_people: 1_081,
    verified_employer_people: 485,
    archival_review_assessed_people: 13_517,
    published_claims: 9_437,
    public_sources: 6_147,
  });
  await page.goto("./oil-companies/");
  const main = page.locator("main");
  await expect(main).toContainText("14 people");
  await expect(main).toContainText("15 historically named");
  await expect(main).not.toContainText("First National Bank of Boston");
});
