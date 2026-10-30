import fs from "node:fs";
import { expect, test } from "@playwright/test";
import type { APIRequestContext } from "@playwright/test";

const evidence = fs.readFileSync(
  new URL(
    "../../research/evidence-page473-michael-troisi-to-john-truden-review_batch-966_2026-10-30.json",
    import.meta.url,
  ),
  "utf8",
);

const profiles = [
  ["3e06b568-db40-5d2d-9cb5-2921372ae0d9", "Michael J Troisi"],
  ["98f948a9-b536-55ce-beeb-6d9b9676af99", "Frank Trojohak"],
  ["8ffd065a-0d35-5dac-9004-68cf33bdb78b", "Adams L Trollinger"],
  ["7affd747-6b2c-59da-b55b-c48217bd611d", "Benny Trombatore"],
  ["239eb1ea-4096-5cb2-9ed6-e83ee3a71a35", "Ferruccio Trombetti"],
  ["d4eae027-85f1-50db-8cfa-5fc4eee7b84f", "Inge Trondsen"],
  ["9d26e766-fb32-5506-a5bf-e1e68036ce38", "Lief Trondstad"],
  ["3771872a-8d0c-5a46-9edb-7f88f7a0ef57", "Marion L Tronoski"],
  ["fddeb05f-ea5b-5e20-8246-67e1df81e9ad", "Louis J Trotta"],
  ["17743b13-54c3-5b87-96b1-6098f864afb9", "Robert E Trotter"],
  ["ecbd4409-0b42-5d07-a33e-5be97302eb1d", "Albert L Troughton"],
  ["8f7035ca-2440-5a65-b7a9-6b51adfe8158", "Peter D Troupos"],
  ["3e39a157-114c-5644-9983-974a621bb097", "Howell B Trousdale"],
  ["a77efd7b-cd86-5e3f-b475-6bd44f2ac20c", "Albert K Trout"],
  ["bb910e68-8372-58d8-bcf7-f98bc0b9ef45", "Harold A Trout"],
  ["1f8b541f-c3b5-5b9e-b136-aeaa9e836a52", "Neva F Troutman"],
  ["2a7d5c3f-f48a-5124-8627-bc9d3a90b1db", "John E Trowbridge"],
  ["0b5434ef-51aa-555f-99e1-d8a2efcc51fa", "Thomas J Troxell"],
  ["99c88a15-886f-554b-9343-400923f57784", "Herbert Troyke"],
  ["a45d3f0c-5c3e-5d3b-936f-3760a14ee36f", "Ernest A Trudeau"],
  ["469cd537-bead-5280-bb00-dbc3b0b963c7", "Francis H Trudeau"],
  ["74b8e18a-d2de-5eb9-bc25-01d7251a5570", "Dorothy J Trudel"],
  ["eaa68846-88e6-53d3-b6e6-48d371cbac27", "John V Truden"],
] as const;

const unresolvedIds = new Set([
  "8ffd065a-0d35-5dac-9004-68cf33bdb78b",
  "7affd747-6b2c-59da-b55b-c48217bd611d",
  "3771872a-8d0c-5a46-9edb-7f88f7a0ef57",
  "ecbd4409-0b42-5d07-a33e-5be97302eb1d",
  "8f7035ca-2440-5a65-b7a9-6b51adfe8158",
  "3e39a157-114c-5644-9983-974a621bb097",
  "a77efd7b-cd86-5e3f-b475-6bd44f2ac20c",
  "1f8b541f-c3b5-5b9e-b136-aeaa9e836a52",
  "2a7d5c3f-f48a-5124-8627-bc9d3a90b1db",
  "99c88a15-886f-554b-9343-400923f57784",
  "469cd537-bead-5280-bb00-dbc3b0b963c7",
  "74b8e18a-d2de-5eb9-bc25-01d7251a5570",
]);

const armyProfiles = [
  ["3e06b568-db40-5d2d-9cb5-2921372ae0d9", "Michael J Troisi", "welder or flame cutter", "unknown"],
  ["fddeb05f-ea5b-5e20-8246-67e1df81e9ad", "Louis J Trotta", "machine-shop occupation, not elsewhere classified", "unknown"],
  ["17743b13-54c3-5b87-96b1-6098f864afb9", "Robert E Trotter", "general-farm hand", "employment"],
  ["bb910e68-8372-58d8-bcf7-f98bc0b9ef45", "Harold A Trout", "general farmer", "unknown"],
  ["0b5434ef-51aa-555f-99e1-d8a2efcc51fa", "Thomas J Troxell", "waiter", "employment"],
  ["a45d3f0c-5c3e-5d3b-936f-3760a14ee36f", "Ernest A Trudeau", "stock clerk", "employment"],
  ["eaa68846-88e6-53d3-b6e6-48d371cbac27", "John V Truden", "student", "student"],
] as const;

async function publicPerson(request: APIRequestContext, id: string, name: string) {
  const response = await request.get(`./data/people/${name[0].toLowerCase()}.json`);
  expect(response.ok()).toBeTruthy();
  return (await response.json()).find((item: { person_id: string }) => item.person_id === id);
}

test("Batch 966 publishes 23 audited people with terminal outcomes", async ({ page }) => {
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

test("seven Army bridges publish occupations or student status without named employers", async ({ request }) => {
  for (const [id, name, occupation, relationshipType] of armyProfiles) {
    const person = await publicPerson(request, id, name);
    expect(person).toMatchObject({
      identity_status: "high_confidence",
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
        relationship_type: relationshipType,
        temporal_basis: "strongly_date_bounded",
        claim_confidence: "medium",
      }),
    ]));
  }
});

test("Frank Trojohak preserves the spelling conflict without post-OSS projection", async ({ request }) => {
  const person = await publicPerson(request, "98f948a9-b536-55ce-beeb-6d9b9676af99", "Frank Trojohak");
  expect(person).toMatchObject({
    identity_status: "high_confidence",
    research_status: "requires_archival_review",
    personnel_category: "unknown_or_indeterminate",
  });
  expect(person.name_variants).toContain("Frank Trojchak");
  expect(person.immediate_pre_oss_affiliations).toHaveLength(0);
  expect(person.last_civilian_pre_service).toHaveLength(0);
  expect(person.other_pre_oss_affiliations).toHaveLength(0);
  expect(JSON.stringify(person)).not.toContain("1945-11-21");
});

test("Ferruccio Trombetti separates immediate Resistance service from earlier work", async ({ request }) => {
  const person = await publicPerson(request, "239eb1ea-4096-5cb2-9ed6-e83ee3a71a35", "Ferruccio Trombetti");
  expect(person).toMatchObject({
    identity_status: "high_confidence",
    personnel_category: "foreign_or_allied_military_personnel",
    commissioned_officer: false,
  });
  expect(person.immediate_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      canonical_organization: "Italian Resistance in Lazio",
      relationship_type: "volunteer",
      temporal_basis: "explicit_immediate",
      claim_confidence: "high",
    }),
  ]);
  expect(person.other_pre_oss_affiliations).toEqual(expect.arrayContaining([
    expect.objectContaining({ occupation: "hemp worker", canonical_organization: null }),
    expect.objectContaining({ canonical_organization: "Royal Italian Army", relationship_type: "military_assignment" }),
  ]));
});

test("Inge Trondsen has confirmed naval identity without a fabricated ship employer", async ({ request }) => {
  const person = await publicPerson(request, "d4eae027-85f1-50db-8cfa-5fc4eee7b84f", "Inge Trondsen");
  expect(person).toMatchObject({
    identity_status: "confirmed",
    personnel_category: "foreign_or_allied_military_personnel",
    commissioned_officer: true,
  });
  expect(person.immediate_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      canonical_organization: "Royal Norwegian Navy",
      relationship_type: "military_assignment",
      temporal_basis: "probable_immediate",
      claim_confidence: "medium",
    }),
  ]);
  expect(person.last_civilian_pre_service).toHaveLength(0);
  expect(person.other_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      organization_name_as_found: "M/S Thalatta (vessel; employing company not named)",
      occupation: "merchant-marine fourth mate",
      relationship_type: "professional_affiliation",
      claim_confidence: "high",
    }),
  ]);
  const serialized = JSON.stringify(person);
  expect(serialized).toContain("krigsseilerregisteret.no/sjofolk/%35%33%33%36%38%32");
  expect(serialized).not.toContain("sjofolk/[private identifier omitted]");
});

test("Lief Trondstad remains a probable spelling-variant identity with qualified employment", async ({ request }) => {
  const person = await publicPerson(request, "9d26e766-fb32-5506-a5bf-e1e68036ce38", "Lief Trondstad");
  expect(person).toMatchObject({
    identity_status: "probable",
    research_status: "documented_prewar_employer_found",
    commissioned_officer: true,
  });
  expect(person.name_variants).toEqual(expect.arrayContaining(["Leif Tronstad", "Leif Hans Larsen Tronstad"]));
  expect(person.last_civilian_pre_service).toEqual([
    expect.objectContaining({
      canonical_organization: "Norwegian Institute of Technology",
      occupation: "chemistry professor",
      relationship_type: "employment",
      temporal_basis: "strongly_date_bounded",
      claim_confidence: "medium",
    }),
  ]);
  expect(person.other_pre_oss_affiliations).toEqual(expect.arrayContaining([
    expect.objectContaining({ canonical_organization: "Norsk Hydro", relationship_type: "professional_affiliation" }),
    expect.objectContaining({ canonical_organization: "Norsk Aluminium Company", relationship_type: "professional_affiliation" }),
  ]));
});

test("twelve unresolved people retain archival outcomes without namesake facts", async ({ request }) => {
  for (const [id, name] of profiles.filter(([id]) => unresolvedIds.has(id))) {
    const person = await publicPerson(request, id, name);
    expect(person).toMatchObject({ identity_status: "unresolved", research_status: "requires_archival_review" });
    expect(person.immediate_pre_oss_affiliations).toHaveLength(0);
    expect(person.last_civilian_pre_service).toHaveLength(0);
    expect(person.other_pre_oss_affiliations).toHaveLength(0);
    expect(person.claims).toHaveLength(0);
  }
});

test("Batch 966 evidence excludes secrets, protected identifiers and raw bulk ordinals", () => {
  expect(evidence).not.toMatch(/"serial_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toMatch(/"service_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toContain("NARA_API_KEY");
  expect(evidence).not.toContain("x-api-key");
  expect(evidence).not.toContain("bulk_record_ordinal");
  for (const identifier of [
    "20220262", "13026536", "119256", "36718239", "31297085",
    "34768666", "32699494", "36671791", "35292877", "1181785",
    "13075067", "36760164", "20123873", "1166199", "36456963",
  ]) expect(evidence).not.toContain(identifier);
});

test("Batch 966 publishes exact coverage counters without changing the oil category", async ({ request, page }) => {
  const response = await request.get("./data/stats.json");
  expect(response.ok()).toBeTruthy();
  expect(await response.json()).toMatchObject({
    source_rows: 23_978,
    person_entities: 23_936,
    possible_duplicate_groups: 663,
    research_attempted_people: 15_154,
    verified_affiliation_people: 1_087,
    verified_employer_people: 486,
    archival_review_assessed_people: 13_630,
    published_claims: 9_539,
    public_sources: 6_197,
  });
  await page.goto("./oil-companies/");
  const main = page.locator("main");
  await expect(main).toContainText("14 people");
  await expect(main).toContainText("15 historically named");
  await expect(main).not.toContainText("Students");
});
