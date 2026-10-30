import fs from "node:fs";
import { expect, test } from "@playwright/test";
import type { APIRequestContext } from "@playwright/test";

const evidence = fs.readFileSync(
  new URL(
    "../../research/evidence-page486-voyer-to-vydra-review_batch-991_2026-10-30.json",
    import.meta.url,
  ),
  "utf8",
);

const profiles = [
  ["c7fba76e-2498-56be-bb26-d6fabae7a123", "Jacques Voyer"],
  ["ce0ab4b5-f21b-5692-aa64-b75e024beaef", "Sylvia F Voyles"],
  ["6abcba2e-783d-55a6-b766-376e028a33d8", "Lazareth Vracarich"],
  ["1c11845b-68ff-54a0-8645-8a4ebf2f2b25", "Mary T Vranesh"],
  ["83743d27-49fa-5a7b-91fe-76973264d6e9", "John Vratimos"],
  ["92938c9b-c1b6-5108-84c8-ca104fa63ec6", "George Vrbanic"],
  ["0fd3f691-04d3-5f03-8b44-c21c04131eaf", "George W Vredenburg"],
  ["e4f9dedb-6239-548e-acb9-7d54c35b477d", "Herbert H Vreeland"],
  ["926e67d9-b099-5b96-96a8-ca1eb5773d20", "Guysbert B Vroom Jr."],
  ["25d86241-bfc2-5cbe-ac77-a27fb02568a1", "Frances Elinor Vrydaugh"],
  ["5a881663-52ef-5d08-aaf9-cb63b2e82226", "James B Vuchetich"],
  ["efb61ce0-073d-5e9b-9bba-8b431269cbd4", "Alexander S Vuchinich"],
  ["a738b368-bb5d-5d15-aa15-b0a4fd9fd4cf", "Alexander S Vuchinich"],
  ["afb6d918-6040-5af6-91c7-a3c7beb785d0", "Wayne S Vucinich"],
  ["15d3793e-4e8d-59a5-a457-456c88f81599", "Pierre A Vuille"],
  ["9804bef2-1724-5eb1-a183-8af866b465e5", "Daniel Vujnovich"],
  ["c6369989-bb69-50c3-9261-c23238fce451", "George M Vujnovich"],
  ["0dda0a24-099e-5087-be8b-4ec6ddc8bc8b", "Daniel Vujovick"],
  ["ed3b928f-c092-5c14-9fe3-7b37d76383d5", "Theodore Vukelich"],
  ["4cafb9d4-5abb-5f62-9c6f-0027da1298e8", "Joseph Vukmanic"],
  ["0979107f-5ea1-5f62-ad16-eda43ef9d254", "George Vuletic"],
  ["134d38fa-2e4a-5271-95a3-a4345cfce0ac", "Carr Vuletich"],
  ["5c7062aa-6ba5-589e-9437-48cacb2995b9", "Ladislav Hugh Vydra"],
] as const;

async function publicPerson(request: APIRequestContext, id: string, name: string) {
  const first = name[0].toLowerCase();
  const shard = /^[a-z]$/.test(first) ? first : "other";
  const response = await request.get(`./data/people/${shard}.json`);
  expect(response.ok()).toBeTruthy();
  return (await response.json()).find((item: { person_id: string }) => item.person_id === id);
}

test("Batch 991 publishes all 23 audited people with terminal outcomes", async ({ page }) => {
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

test("Jacques Voyer keeps Free French service separate from the qualified BCRA pathway", async ({ request }) => {
  const person = await publicPerson(request, profiles[0][0], profiles[0][1]);
  expect(person).toMatchObject({
    identity_status: "high_confidence",
    personnel_category: "foreign_or_allied_military_personnel",
    research_status: "completed",
  });
  expect(person.immediate_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      canonical_organization: "Bureau Central de Renseignements et d'Action",
      relationship_type: "government_assignment",
      temporal_basis: "probable_immediate",
      claim_confidence: "medium",
      publication_status: "publish_qualified",
    }),
  ]);
  expect(person.other_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      canonical_organization: "Free French Forces",
      relationship_type: "military_assignment",
      claim_confidence: "high",
    }),
  ]);
  expect(person.last_civilian_pre_service).toHaveLength(0);
});

test("Wayne Vucinich publishes Berkeley as employment rather than education", async ({ request }) => {
  const person = await publicPerson(request, profiles[13][0], profiles[13][1]);
  expect(person).toMatchObject({
    identity_status: "high_confidence",
    personnel_category: "commissioned_naval_officer",
    research_status: "verified_employer_found",
  });
  expect(person.immediate_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      canonical_organization: "University of California, Berkeley",
      relationship_type: "employment",
      temporal_basis: "strongly_date_bounded",
    }),
  ]);
  expect(person.last_civilian_pre_service).toEqual([
    expect.objectContaining({
      canonical_organization: "University of California, Berkeley",
      role_title: "teaching assistant in history",
      relationship_type: "employment",
      claim_confidence: "high",
    }),
  ]);
});

test("George Vujnovich publishes student, civilian and Army stages separately", async ({ request }) => {
  const person = await publicPerson(request, profiles[16][0], profiles[16][1]);
  expect(person).toMatchObject({
    identity_status: "high_confidence",
    personnel_category: "commissioned_army_officer",
    research_status: "verified_employer_found",
  });
  expect(person.immediate_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      canonical_organization: "United States Army",
      relationship_type: "military_assignment",
      temporal_basis: "explicit_immediate",
    }),
  ]);
  expect(person.last_civilian_pre_service).toEqual([
    expect.objectContaining({
      canonical_organization: "Pan American Airways",
      role_title: "airbase employee",
      relationship_type: "employment",
      claim_confidence: "high",
    }),
  ]);
  expect(person.other_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      canonical_organization: "University of Belgrade",
      relationship_type: "student",
    }),
  ]);
});

test("Army occupation categories never become named employers", async ({ request }) => {
  const vratimos = await publicPerson(request, profiles[4][0], profiles[4][1]);
  expect(vratimos).toMatchObject({ identity_status: "confirmed", research_status: "occupation_only_found" });
  expect(vratimos.last_civilian_pre_service).toHaveLength(0);
  expect(vratimos.other_pre_oss_affiliations).toEqual([
    expect.objectContaining({ canonical_organization: null, relationship_type: "employment" }),
  ]);

  const vredenburg = await publicPerson(request, profiles[6][0], profiles[6][1]);
  expect(vredenburg).toMatchObject({ identity_status: "confirmed", research_status: "occupation_only_found" });
  expect(vredenburg.last_civilian_pre_service).toHaveLength(0);
  expect(vredenburg.other_pre_oss_affiliations).toEqual([
    expect.objectContaining({ canonical_organization: null, relationship_type: "employment" }),
  ]);

  const vuletic = await publicPerson(request, profiles[20][0], profiles[20][1]);
  expect(vuletic).toMatchObject({ identity_status: "confirmed", research_status: "requires_archival_review" });
  expect(vuletic.immediate_pre_oss_affiliations).toHaveLength(0);
  expect(vuletic.last_civilian_pre_service).toHaveLength(0);
  expect(vuletic.other_pre_oss_affiliations).toHaveLength(0);
});

test("duplicate-sensitive rows remain distinct and visibly grouped", async ({ request }) => {
  const vuchinichA = await publicPerson(request, profiles[11][0], profiles[11][1]);
  const vuchinichB = await publicPerson(request, profiles[12][0], profiles[12][1]);
  expect(vuchinichA).toMatchObject({ identity_status: "ambiguous", research_status: "conflicting_sources" });
  expect(vuchinichB).toMatchObject({ identity_status: "ambiguous", research_status: "conflicting_sources" });
  expect(vuchinichA.possible_duplicate_group).toMatch(/^duplicate-/);
  expect(vuchinichB.possible_duplicate_group).toBe(vuchinichA.possible_duplicate_group);

  const vujnovich = await publicPerson(request, profiles[15][0], profiles[15][1]);
  const vujovick = await publicPerson(request, profiles[17][0], profiles[17][1]);
  expect(vujnovich.person_id).not.toBe(vujovick.person_id);
  expect(vujnovich.possible_duplicate_group).toMatch(/^duplicate-/);
  expect(vujovick.possible_duplicate_group).toBe(vujnovich.possible_duplicate_group);
  expect(vujnovich.immediate_pre_oss_affiliations).toHaveLength(0);
  expect(vujovick.immediate_pre_oss_affiliations).toHaveLength(0);
});

test("unresolved Batch 991 people retain archival-review guidance", async ({ request }) => {
  for (const index of [1, 2, 3, 5, 7, 8, 9, 10, 14, 18, 19, 21, 22] as const) {
    const person = await publicPerson(request, profiles[index][0], profiles[index][1]);
    expect(person.research_status).toBe("requires_archival_review");
    expect(person.immediate_pre_oss_affiliations).toHaveLength(0);
    expect(person.last_civilian_pre_service).toHaveLength(0);
  }
});

test("Batch 991 evidence excludes secrets, full identifiers and raw bulk records", () => {
  expect(evidence).not.toMatch(/"serial_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toMatch(/"service_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toContain("NARA_API_KEY");
  expect(evidence).not.toContain("x-api-key");
  expect(evidence).not.toContain("candidate_identifier");
  expect(evidence).not.toContain("bulk_record_ordinal");
  expect(evidence).not.toMatch(/RA\d{8}/);
});

test("Batch 991 public claims retain inspectable source citations", async ({ request }) => {
  for (const index of [0, 4, 6, 13, 16, 20] as const) {
    const person = await publicPerson(request, profiles[index][0], profiles[index][1]);
    expect(person.claims.length).toBeGreaterThan(0);
    for (const claim of person.claims) {
      expect(claim.sources.length).toBeGreaterThan(0);
      for (const link of claim.sources) {
        expect(link.source.stable_url || link.source.archival_identifier).toBeTruthy();
        const excerpt = link.excerpt_override ?? claim.evidence_excerpt ?? "";
        expect(excerpt.trim() ? excerpt.trim().split(/\s+/).length : 0).toBeLessThanOrEqual(25);
      }
    }
  }
});

test("Batch 991 publishes exact coverage counters", async ({ request }) => {
  const response = await request.get("./data/stats.json");
  expect(response.ok()).toBeTruthy();
  expect(await response.json()).toMatchObject({
    source_rows: 23_978,
    person_entities: 23_936,
    possible_duplicate_groups: 679,
    research_attempted_people: 15_725,
    verified_affiliation_people: 1_138,
    verified_employer_people: 516,
    archival_review_assessed_people: 14_200,
    published_claims: 10_068,
    public_sources: 6_482,
  });
});
