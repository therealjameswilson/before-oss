import fs from "node:fs";
import { expect, test } from "@playwright/test";
import type { APIRequestContext } from "@playwright/test";

const evidence = fs.readFileSync(
  new URL(
    "../../research/evidence-page478-henry-untermeyer-to-robert-vacasovich-review_batch-975_2026-10-30.json",
    import.meta.url,
  ),
  "utf8",
);

const profiles = [
  ["ba2f4d84-a0f3-5e25-922f-6877669645d2", "Henry Untermeyer"],
  ["2f876bbf-66eb-53c1-b830-87ffd9323af3", "Furman H Updike"],
  ["7a1139da-0ce0-5bc6-9a3f-5d20b8981ee0", "George A Upperman"],
  ["6c54eb25-eb8c-5993-8f79-5c681eb61cf9", "Thomas G Upton"],
  ["60d6aa53-3a02-56ed-ad54-3347b4918ae9", "George S Ura"],
  ["f03fb629-1dc6-5031-a484-160ec8130861", "John W Urban"],
  ["ddbdf47a-b4e6-5fdf-a90e-ec5c9ae69a0c", "Louis Urbano"],
  ["7c0c0f78-8e5d-533b-9278-6d0e9e03984e", "Louis J Urbanski"],
  ["753f57cf-1935-5b71-bd36-8a892f15b678", "Sigfried Urdal"],
  ["5ad6dc81-8af9-5abb-a229-3345b8e3d942", "Maurice Urdang"],
  ["e41ca66f-b26c-59c2-a168-ea4a2bc02c2d", "Paul M Ursin"],
  ["b4895c56-bf22-58af-b1e7-c2cc6787a4d0", "Joseph Ursiny"],
  ["af9b0355-8b6f-5c2a-90d4-648a982e909e", "George H Usher"],
  ["a527f98e-c2c8-51d2-863a-85c811a4a9e2", "Martha E Usher"],
  ["da946194-40b9-5bc7-be24-023ceb6646bb", "Richard E Usher"],
  ["0fc49d3a-dfbe-57d3-8152-475b9cecb1aa", "Richard E Usher"],
  ["a33336a7-5b2a-513d-a5c2-ed3499ee4ad6", "Vladimir Ussachevsky"],
  ["f48526a4-8ee2-5232-8d00-2930b2ec3f57", "Yoshisada Usuda"],
  ["caacaa5f-df72-57df-95ad-e93ad5c58f0f", "James C Utrecht"],
  ["8e55df97-f557-53d9-bd5f-14c8778f208a", "Anton S Utz"],
  ["128fcc95-79fa-5d1f-8893-90ba9c5defb6", "Stella T Uzdawinis"],
  ["a8306d70-3613-59d0-b9f2-0abc9384ab1c", "E V Uzes"],
  ["e10018a7-307f-5664-aae2-46b50fc9576c", "Robert Vacasovich"],
] as const;

async function publicPerson(request: APIRequestContext, id: string, name: string) {
  const response = await request.get(`./data/people/${name[0].toLowerCase()}.json`);
  expect(response.ok()).toBeTruthy();
  return (await response.json()).find((item: { person_id: string }) => item.person_id === id);
}

test("Batch 975 publishes all 23 audited people with terminal outcomes", async ({ page }) => {
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

test("five protected Army matches publish occupations or student status, never employers", async ({ request }) => {
  const expected = [
    ["7a1139da-0ce0-5bc6-9a3f-5d20b8981ee0", "George A Upperman", "stenographer or typist", "unknown"],
    ["ddbdf47a-b4e6-5fdf-a90e-ec5c9ae69a0c", "Louis Urbano", "shipping or receiving clerk", "unknown"],
    ["753f57cf-1935-5b71-bd36-8a892f15b678", "Sigfried Urdal", "sailor or deckhand outside the U.S. Navy", "unknown"],
    ["5ad6dc81-8af9-5abb-a229-3345b8e3d942", "Maurice Urdang", "manager or official, not elsewhere classified", "unknown"],
    ["caacaa5f-df72-57df-95ad-e93ad5c58f0f", "James C Utrecht", "student", "student"],
  ] as const;
  for (const [id, name, occupation, relationshipType] of expected) {
    const person = await publicPerson(request, id, name);
    expect(person).toMatchObject({
      identity_status: "high_confidence",
      research_status: "occupation_only_found",
      personnel_category: "enlisted_army_personnel",
      commissioned_officer: false,
    });
    expect(person.immediate_pre_oss_affiliations).toHaveLength(0);
    expect(person.last_civilian_pre_service).toHaveLength(0);
    expect(person.other_pre_oss_affiliations).toEqual([
      expect.objectContaining({
        canonical_organization: null,
        occupation,
        relationship_type: relationshipType,
        claim_confidence: "medium",
        publication_status: "publish_qualified",
      }),
    ]);
  }
});

test("Henry Untermeyer separates WABC employment from his uncertain Army-to-OSS pathway", async ({ request }) => {
  const person = await publicPerson(request, "ba2f4d84-a0f3-5e25-922f-6877669645d2", "Henry Untermeyer");
  expect(person).toMatchObject({
    identity_status: "high_confidence",
    research_status: "documented_prewar_employer_found",
    personnel_category: "commissioned_army_officer",
    commissioned_officer: true,
  });
  expect(person.immediate_pre_oss_affiliations).toHaveLength(0);
  expect(person.last_civilian_pre_service).toEqual([
    expect.objectContaining({
      canonical_organization: "WABC (CBS-owned New York radio station)",
      relationship_type: "employment",
      temporal_basis: "strongly_date_bounded",
      claim_confidence: "high",
    }),
  ]);
  expect(person.other_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      canonical_organization: "United States Army",
      relationship_type: "military_assignment",
      temporal_basis: "temporal_relation_uncertain",
    }),
  ]);
});

test("Paul Ursin publishes the Prague government assignment without inventing an immediate predecessor", async ({ request }) => {
  const person = await publicPerson(request, "e41ca66f-b26c-59c2-a168-ea4a2bc02c2d", "Paul M Ursin");
  expect(person).toMatchObject({ identity_status: "high_confidence", research_status: "completed" });
  expect(person.immediate_pre_oss_affiliations).toHaveLength(0);
  expect(person.last_civilian_pre_service).toHaveLength(0);
  expect(person.other_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      canonical_organization: "United States Department of State",
      organization_name_as_found: "U.S. Embassy in Prague and later the American consulate",
      relationship_type: "government_assignment",
      temporal_basis: "documented_prewar",
      claim_confidence: "high",
    }),
  ]);
});

test("Vladimir Ussachevsky has two concurrent civilian employers and an explicit Army pathway", async ({ request }) => {
  const person = await publicPerson(request, "a33336a7-5b2a-513d-a5c2-ed3499ee4ad6", "Vladimir Ussachevsky");
  expect(person).toMatchObject({
    identity_status: "high_confidence",
    research_status: "verified_employer_found",
    personnel_category: "enlisted_army_personnel",
  });
  expect(person.immediate_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      canonical_organization: "United States Army",
      relationship_type: "military_assignment",
      temporal_basis: "explicit_immediate",
      claim_confidence: "high",
    }),
  ]);
  expect(person.last_civilian_pre_service).toEqual(expect.arrayContaining([
    expect.objectContaining({ canonical_organization: "Pasadena Junior College", relationship_type: "employment" }),
    expect.objectContaining({ canonical_organization: "Roosevelt High School (Los Angeles)", relationship_type: "employment" }),
  ]));
  expect(person.last_civilian_pre_service).toHaveLength(2);
});

test("the two Richard Usher rows remain distinct conflict and ambiguity profiles", async ({ request }) => {
  const conflict = await publicPerson(request, "da946194-40b9-5bc7-be24-023ceb6646bb", "Richard E Usher");
  const ambiguous = await publicPerson(request, "0fc49d3a-dfbe-57d3-8152-475b9cecb1aa", "Richard E Usher");
  expect(conflict).toMatchObject({ identity_status: "conflicting", research_status: "conflicting_sources" });
  expect(ambiguous).toMatchObject({ identity_status: "ambiguous", research_status: "requires_archival_review" });
  expect(conflict.person_id).not.toBe(ambiguous.person_id);
  expect(conflict.possible_duplicate_group).toBe(ambiguous.possible_duplicate_group);
  expect(conflict.possible_duplicate_group).toMatch(/^duplicate-[a-f0-9]{12}$/);
  for (const person of [conflict, ambiguous]) {
    expect(person.immediate_pre_oss_affiliations).toHaveLength(0);
    expect(person.last_civilian_pre_service).toHaveLength(0);
    expect(person.other_pre_oss_affiliations).toHaveLength(0);
  }
});

test("Usuda remains an identity-only civilian and Uzdawinis records the second completed attempt", async ({ request }) => {
  const usuda = await publicPerson(request, "f48526a4-8ee2-5232-8d00-2930b2ec3f57", "Yoshisada Usuda");
  expect(usuda).toMatchObject({
    identity_status: "high_confidence",
    research_status: "requires_archival_review",
    personnel_category: "civilian_professional_or_administrative_grade",
    commissioned_officer: false,
  });
  expect(usuda.name_variants).toContain("Yoshisada Katoi Usuda");
  expect(usuda.other_pre_oss_affiliations).toHaveLength(0);
  expect(usuda.claims).toEqual([
    expect.objectContaining({ claim_type: "identity", claim_confidence: "high", publication_status: "published" }),
  ]);

  const uzdawinis = await publicPerson(request, "128fcc95-79fa-5d1f-8893-90ba9c5defb6", "Stella T Uzdawinis");
  expect(uzdawinis).toMatchObject({
    identity_status: "high_confidence",
    research_status: "requires_archival_review",
    research_attempt_count: 2,
  });
  expect(uzdawinis.immediate_pre_oss_affiliations).toHaveLength(0);
  expect(uzdawinis.last_civilian_pre_service).toHaveLength(0);
});

test("Batch 975 evidence excludes secrets, full identifiers and raw bulk records", () => {
  expect(evidence).not.toMatch(/"serial_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toMatch(/"service_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toContain("NARA_API_KEY");
  expect(evidence).not.toContain("x-api-key");
  expect(evidence).not.toContain("candidate_identifier");
  expect(evidence).not.toContain("bulk_record_ordinal");
  expect(evidence).not.toMatch(/RA\d{8}/);
});

test("Batch 975 publishes exact coverage counters and preserves oil counts", async ({ request, page }) => {
  const response = await request.get("./data/stats.json");
  expect(response.ok()).toBeTruthy();
  expect(await response.json()).toMatchObject({
    source_rows: 23_978,
    person_entities: 23_936,
    possible_duplicate_groups: 665,
    research_attempted_people: 15_360,
    verified_affiliation_people: 1_105,
    verified_employer_people: 495,
    archival_review_assessed_people: 13_836,
    published_claims: 9_749,
    public_sources: 6_305,
  });
  await page.goto("./oil-companies/");
  const main = page.locator("main");
  await expect(main).toContainText("14 people");
  await expect(main).toContainText("15 historically named");
});
