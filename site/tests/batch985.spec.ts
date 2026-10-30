import fs from "node:fs";
import { expect, test } from "@playwright/test";
import type { APIRequestContext } from "@playwright/test";

const evidence = fs.readFileSync(
  new URL(
    "../../research/evidence-page483-george-vetlesen-to-peter-viezbicke-jr-review_batch-985_2026-10-30.json",
    import.meta.url,
  ),
  "utf8",
);

const profiles = [
  ["bdfb7886-8828-54f8-a9ed-5c0cf4fbec12", "George Vetlesen"],
  ["73ad5483-fde8-5f32-baf8-86c26b587fb0", "Lucienne Vetois"],
  ["ceba63b7-3955-5406-b42e-dc9ade9b2b62", "Earl F Vetter"],
  ["67ca8fac-b73e-5eb2-b6ab-722050536fbe", "Ethel M Vetter"],
  ["852fe132-4da7-54f3-8b43-9e496bb8bc4c", "Rene Veuve"],
  ["2c443b81-1651-50ee-b16a-c6fcaa97f384", "Joseph L Vezina"],
  ["a7005dd5-829e-581c-8152-261fbc4b065b", "Normand H Vezina"],
  ["6a3a0778-935e-59a4-9a93-b1aea9a400d8", "Pauline P Vezzani"],
  ["955a9027-9c32-5d43-bd3d-c011cf788a8a", "Joseph L Vicilante"],
  ["9934387e-de20-5f53-a5bd-3176ba81a74f", "Harold M Vick"],
  ["b0f9e8e5-84f6-5410-9a3a-3d6d66426819", "Billy D Vickers"],
  ["6204dcf0-a6fc-5cc1-b593-1f03b9f21dca", "Francis J Vicovari"],
  ["694d922b-cf1f-59fa-8a69-0266776bcb4b", "Mary M Victory"],
  ["31472523-fd05-5df5-b886-8a40950fb1c1", "Felix G Vidal"],
  ["7d48d498-46f5-5572-9cde-bb8673a72889", "Trinidad B Vidal"],
  ["ce163b3a-7988-579a-a924-7a7faf2437c4", "Livio Vieceli"],
  ["6d9ca923-aed1-5972-8936-ceed76854a23", "Edward C Viegel"],
  ["29d07d6e-5017-59db-a162-c722e8df0a96", "Berthold Viertel"],
  ["3c3aa688-f432-5c3c-a91c-1fa272cc8120", "Peter Viertel"],
  ["a3195826-1cb9-5229-a8be-95a093b6e10c", "Alexander O Vietor"],
  ["0850a43e-53ef-55cf-8b84-2bd15fada613", "Thomas F Vietor Jr."],
  ["fc460dd6-ef38-58f5-af82-942abdaa1e30", "Erik E Vieux"],
  ["efee5b47-6f91-5fb2-a0cf-81b67253cc45", "Peter P Viezbicke Jr."],
] as const;

async function publicPerson(request: APIRequestContext, id: string, name: string) {
  const first = name[0].toLowerCase();
  const shard = /^[a-z]$/.test(first) ? first : "other";
  const response = await request.get(`./data/people/${shard}.json`);
  expect(response.ok()).toBeTruthy();
  return (await response.json()).find((item: { person_id: string }) => item.person_id === id);
}

test("Batch 985 publishes all 23 audited people with terminal outcomes", async ({ page }) => {
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

test("Army bridges publish broad occupations without inventing employers", async ({ request }) => {
  const expected = [
    ["ceba63b7-3955-5406-b42e-dc9ade9b2b62", "Earl F Vetter", "dyer"],
    ["7d48d498-46f5-5572-9cde-bb8673a72889", "Trinidad B Vidal", "miner or mining-machine operator"],
    ["ce163b3a-7988-579a-a924-7a7faf2437c4", "Livio Vieceli", "draftsman"],
    ["efee5b47-6f91-5fb2-a0cf-81b67253cc45", "Peter P Viezbicke Jr.", "sales clerk"],
  ] as const;
  for (const [id, name, occupation] of expected) {
    const person = await publicPerson(request, id, name);
    expect(person.identity_status).toBe("high_confidence");
    expect(person.last_civilian_pre_service).toHaveLength(0);
    expect(person.other_pre_oss_affiliations).toEqual(expect.arrayContaining([
      expect.objectContaining({
        canonical_organization: null,
        occupation,
        temporal_basis: "strongly_date_bounded",
        claim_confidence: "medium",
        publication_status: "publish_qualified",
      }),
    ]));
  }
});

test("Peter Viertel preserves the employer and military-pathway distinction", async ({ request }) => {
  const person = await publicPerson(request, "3c3aa688-f432-5c3c-a91c-1fa272cc8120", "Peter Viertel");
  expect(person).toMatchObject({
    identity_status: "high_confidence",
    research_status: "verified_employer_found",
    commissioned_officer: true,
  });
  expect(person.last_civilian_pre_service).toEqual([
    expect.objectContaining({
      canonical_organization: "Warner Bros.",
      occupation: "screenwriter",
      relationship_type: "employment",
      temporal_basis: "strongly_date_bounded",
      claim_confidence: "high",
    }),
  ]);
  expect(person.immediate_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      canonical_organization: "United States Marine Corps",
      relationship_type: "military_assignment",
      temporal_basis: "explicit_immediate",
      claim_confidence: "high",
    }),
  ]);
});

test("Vicovari, Vietor and Viertel preserve qualified prewar categories", async ({ request }) => {
  const vicovari = await publicPerson(request, "6204dcf0-a6fc-5cc1-b593-1f03b9f21dca", "Francis J Vicovari");
  expect(vicovari).toMatchObject({ identity_status: "probable", research_status: "completed" });
  expect(vicovari.other_pre_oss_affiliations).toEqual(expect.arrayContaining([
    expect.objectContaining({
      canonical_organization: "British American Ambulance Corps",
      relationship_type: "volunteer",
      claim_confidence: "medium",
      publication_status: "publish_qualified",
    }),
  ]));

  const vietor = await publicPerson(request, "a3195826-1cb9-5229-a8be-95a093b6e10c", "Alexander O Vietor");
  expect(vietor).toMatchObject({ identity_status: "probable", research_status: "documented_prewar_employer_found" });
  expect(vietor.last_civilian_pre_service).toHaveLength(0);
  expect(vietor.other_pre_oss_affiliations).toEqual(expect.arrayContaining([
    expect.objectContaining({ canonical_organization: "Cox & Stevens", temporal_basis: "documented_prewar", claim_confidence: "medium" }),
    expect.objectContaining({ canonical_organization: "Yale University", temporal_basis: "documented_prewar", claim_confidence: "medium" }),
  ]));

  const viertel = await publicPerson(request, "29d07d6e-5017-59db-a162-c722e8df0a96", "Berthold Viertel");
  expect(viertel).toMatchObject({ identity_status: "probable", research_status: "occupation_only_found" });
  expect(viertel.other_pre_oss_affiliations).toEqual(expect.arrayContaining([
    expect.objectContaining({ canonical_organization: null, occupation: "writer, theater director and film director", publication_status: "publish_qualified" }),
  ]));
});

test("student status is not converted into employment", async ({ request }) => {
  const person = await publicPerson(request, "0850a43e-53ef-55cf-8b84-2bd15fada613", "Thomas F Vietor Jr.");
  expect(person).toMatchObject({ identity_status: "high_confidence", research_status: "requires_archival_review" });
  expect(person.last_civilian_pre_service).toHaveLength(0);
  expect(person.other_pre_oss_affiliations).toEqual(expect.arrayContaining([
    expect.objectContaining({
      canonical_organization: "Princeton University",
      relationship_type: "student",
      temporal_basis: "documented_prewar",
      claim_confidence: "high",
    }),
  ]));
});

test("the Veigel/Viegel protected-identifier conflict remains separate and public-safe", async ({ request }) => {
  const person = await publicPerson(request, "6d9ca923-aed1-5972-8936-ceed76854a23", "Edward C Viegel");
  expect(person).toMatchObject({ identity_status: "conflicting", research_status: "conflicting_sources" });
  expect(person.possible_duplicate_group).toMatch(/^duplicate-[a-f0-9]{12}$/);
  expect(person.possible_duplicate_group).not.toMatch(/\d{7,9}/);
  expect(person.immediate_pre_oss_affiliations).toHaveLength(0);
  expect(person.last_civilian_pre_service).toHaveLength(0);
  expect(person.other_pre_oss_affiliations).toHaveLength(0);
});

test("unbridged Batch 985 people remain affiliation-free archival cases", async ({ request }) => {
  const names = new Set([
    "Lucienne Vetois", "Ethel M Vetter", "Joseph L Vezina", "Normand H Vezina", "Pauline P Vezzani",
    "Joseph L Vicilante", "Harold M Vick", "Billy D Vickers", "Mary M Victory", "Felix G Vidal", "Erik E Vieux",
  ]);
  for (const [id, name] of profiles.filter(([, name]) => names.has(name))) {
    const person = await publicPerson(request, id, name);
    expect(person.research_status).toBe("requires_archival_review");
    expect(person.immediate_pre_oss_affiliations).toHaveLength(0);
    expect(person.last_civilian_pre_service).toHaveLength(0);
    expect(person.other_pre_oss_affiliations).toHaveLength(0);
  }
});

test("Batch 985 evidence excludes secrets, full identifiers and raw bulk records", () => {
  expect(evidence).not.toMatch(/"serial_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toMatch(/"service_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toContain("NARA_API_KEY");
  expect(evidence).not.toContain("x-api-key");
  expect(evidence).not.toContain("candidate_identifier");
  expect(evidence).not.toContain("bulk_record_ordinal");
  expect(evidence).not.toMatch(/RA\d{8}/);
});

test("Batch 985 publishes exact coverage counters and preserves oil counts", async ({ request, page }) => {
  const response = await request.get("./data/stats.json");
  expect(response.ok()).toBeTruthy();
  expect(await response.json()).toMatchObject({
    source_rows: 23_978,
    person_entities: 23_936,
    possible_duplicate_groups: 672,
    research_attempted_people: 15_587,
    verified_affiliation_people: 1_124,
    verified_employer_people: 505,
    archival_review_assessed_people: 14_063,
    published_claims: 9_941,
    public_sources: 6_419,
  });
  await page.goto("./oil-companies/");
  const main = page.locator("main");
  await expect(main).toContainText("14 people");
  await expect(main).toContainText("15 historically named");
});
