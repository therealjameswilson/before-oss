import fs from "node:fs";
import { expect, test } from "@playwright/test";
import type { APIRequestContext } from "@playwright/test";

const evidence = fs.readFileSync(
  new URL(
    "../../research/evidence-page472-oliver-trechter-to-walter-treumann-review_batch-964_2026-10-29.json",
    import.meta.url,
  ),
  "utf8",
);

const profiles = [
  ["6fe4eaa1-86c3-5d63-b223-68b2fda75b23", "Oliver E Trechter"],
  ["aa208071-c04b-5558-914a-ad29030b8351", "Barton G Treece"],
  ["e86d1332-e250-5dba-9617-39881a7b50b4", "Charles J Trees"],
  ["2154d06f-9bf5-540e-91cb-457981d016ee", "Jack R Trees"],
  ["0718d886-9fd4-5f31-898d-dbceafc4595d", "John R Tregenza"],
  ["feb195b8-d812-5ea4-a6fe-099fcf1f4fa8", "Benny J Treglia"],
  ["e01974ac-1197-5c29-bd10-f2d67bef32f1", "Nison A Tregor"],
  ["e3f8a928-a21e-5256-8a0d-afe6fd52e211", "Guillaume M Treguier"],
  ["d9e3e3c9-c5c5-5678-8c31-457ee5325861", "Richard W Treiber"],
  ["b5cd7e5e-3876-538e-9d87-314f6a070e11", "John Treisner"],
  ["5764ba1f-30c0-524e-b87d-30f17d35fa85", "Raymond A Tremblay"],
  ["2759e2e9-c59f-51e0-a2f6-30e5ba9706cf", "Liberty J Tremonte"],
  ["b9829380-0583-5381-9759-6afa04b0f1d9", "Walter N Trenerry"],
  ["a5500bfe-9a3b-5869-ba82-bb6bb0fedce1", "Louis P Trent"],
  ["14ff91bd-993e-5aa5-b86b-73be3482c144", "Clarence J Trentman"],
  ["d91b1a09-beb1-5319-8181-bbb322b31ac4", "Peter Trerotole"],
  ["21c7b171-aa76-57b1-bafe-6358af0661af", "Rudolph Tressel"],
  ["a9d1c646-205e-5415-9c0c-9b53ab370f1e", "Willis L Tressler"],
  ["994d4a09-36fc-5536-b6ca-5f7bf153131d", "Burton S Tretheway"],
  ["b62e39d5-4d63-5bec-8d26-41a28df5984e", "Vincent R Treul"],
  ["94c8d58c-9b7d-5f1c-b385-330e76891e1b", "Walter Treumann"],
] as const;

const unresolvedIds = new Set([
  "aa208071-c04b-5558-914a-ad29030b8351",
  "e86d1332-e250-5dba-9617-39881a7b50b4",
  "0718d886-9fd4-5f31-898d-dbceafc4595d",
  "d9e3e3c9-c5c5-5678-8c31-457ee5325861",
  "b5cd7e5e-3876-538e-9d87-314f6a070e11",
  "b9829380-0583-5381-9759-6afa04b0f1d9",
  "a5500bfe-9a3b-5869-ba82-bb6bb0fedce1",
  "14ff91bd-993e-5aa5-b86b-73be3482c144",
  "d91b1a09-beb1-5319-8181-bbb322b31ac4",
  "21c7b171-aa76-57b1-bafe-6358af0661af",
  "94c8d58c-9b7d-5f1c-b385-330e76891e1b",
]);

const armyProfiles = [
  ["6fe4eaa1-86c3-5d63-b223-68b2fda75b23", "Oliver E Trechter", "student", "student", "high_confidence"],
  ["2154d06f-9bf5-540e-91cb-457981d016ee", "Jack R Trees", "student", "student", "high_confidence"],
  ["feb195b8-d812-5ea4-a6fe-099fcf1f4fa8", "Benny J Treglia", "craneman, derrickman, hoistman, or shovelman", "employment", "high_confidence"],
  ["e3f8a928-a21e-5256-8a0d-afe6fd52e211", "Guillaume M Treguier", "cook, except private family", "employment", "high_confidence"],
  ["5764ba1f-30c0-524e-b87d-30f17d35fa85", "Raymond A Tremblay", "skilled boot or shoe manufacturing occupation", "employment", "high_confidence"],
  ["2759e2e9-c59f-51e0-a2f6-30e5ba9706cf", "Liberty J Tremonte", "semiskilled metal-products fabrication occupation, not elsewhere classified", "employment", "confirmed"],
  ["994d4a09-36fc-5536-b6ca-5f7bf153131d", "Burton S Tretheway", "student", "student", "high_confidence"],
  ["b62e39d5-4d63-5bec-8d26-41a28df5984e", "Vincent R Treul", "bookkeeper or cashier, except bank cashier", "employment", "high_confidence"],
] as const;

async function publicPerson(request: APIRequestContext, id: string, name: string) {
  const response = await request.get(`./data/people/${name[0].toLowerCase()}.json`);
  expect(response.ok()).toBeTruthy();
  return (await response.json()).find((item: { person_id: string }) => item.person_id === id);
}

test("Batch 964 publishes 21 audited people with terminal outcomes", async ({ page }) => {
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

test("eight Army bridges publish qualified occupations or student status only", async ({ request }) => {
  for (const [id, name, occupation, relationshipType, identityStatus] of armyProfiles) {
    const person = await publicPerson(request, id, name);
    expect(person).toMatchObject({
      identity_status: identityStatus,
      personnel_category: "enlisted_army_personnel",
      commissioned_officer: false,
      research_status: "occupation_only_found",
    });
    expect(person.immediate_pre_oss_affiliations).toHaveLength(0);
    expect(person.last_civilian_pre_service).toHaveLength(0);
    expect(person.other_pre_oss_affiliations).toEqual([
      expect.objectContaining({
        canonical_organization: null,
        occupation,
        relationship_type: relationshipType,
        temporal_basis: "strongly_date_bounded",
        claim_confidence: "medium",
      }),
    ]);
  }
});

test("Army student categories do not become employers or named schools", async ({ request }) => {
  for (const [id, name] of armyProfiles.filter((item) => item[3] === "student")) {
    const person = await publicPerson(request, id, name);
    expect(person.last_civilian_pre_service).toHaveLength(0);
    expect(person.other_pre_oss_affiliations[0]).toMatchObject({
      organization_id: null,
      canonical_organization: null,
      relationship_type: "student",
      occupation: "student",
    });
  }
});

test("Nison Tregor and Willis Tressler remain qualified prewar findings", async ({ request }) => {
  const tregor = await publicPerson(request, "e01974ac-1197-5c29-bd10-f2d67bef32f1", "Nison A Tregor");
  expect(tregor).toMatchObject({
    identity_status: "high_confidence",
    personnel_category: "commissioned_army_officer",
    commissioned_officer: true,
    research_status: "occupation_only_found",
  });
  expect(tregor.immediate_pre_oss_affiliations).toHaveLength(0);
  expect(tregor.last_civilian_pre_service).toHaveLength(0);
  expect(tregor.other_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      occupation: "sculptor",
      relationship_type: "self_employment",
      temporal_basis: "documented_prewar",
      claim_confidence: "medium",
    }),
  ]);

  const tressler = await publicPerson(request, "a9d1c646-205e-5415-9c0c-9b53ab370f1e", "Willis L Tressler");
  expect(tressler).toMatchObject({ identity_status: "probable", research_status: "occupation_only_found" });
  expect(tressler.immediate_pre_oss_affiliations).toHaveLength(0);
  expect(tressler.last_civilian_pre_service).toHaveLength(0);
  expect(tressler.other_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      canonical_organization: null,
      occupation: "scientific researcher and author on ostracods",
      relationship_type: "professional_affiliation",
      temporal_basis: "documented_prewar",
      claim_confidence: "medium",
    }),
  ]);
});

test("Liberty Tremonte has a confirmed original-record identity without an employer inference", async ({ request }) => {
  const person = await publicPerson(request, "2759e2e9-c59f-51e0-a2f6-30e5ba9706cf", "Liberty J Tremonte");
  expect(person.identity_status).toBe("confirmed");
  expect(person.immediate_pre_oss_affiliations).toHaveLength(0);
  expect(person.last_civilian_pre_service).toHaveLength(0);
  expect(person.claims).toEqual(expect.arrayContaining([
    expect.objectContaining({
      claim_type: "identity",
      claim_confidence: "confirmed",
      sources: expect.arrayContaining([
        expect.objectContaining({
          source: expect.objectContaining({
            document_number: "2610-PS",
            repository_publisher: expect.stringContaining("Library of Congress"),
          }),
        }),
      ]),
    }),
  ]));
});

test("eleven unresolved people retain archival outcomes without transferred namesake facts", async ({ request }) => {
  for (const [id, name] of profiles.filter(([id]) => unresolvedIds.has(id))) {
    const person = await publicPerson(request, id, name);
    expect(person).toMatchObject({ identity_status: "unresolved", research_status: "requires_archival_review" });
    expect(person.immediate_pre_oss_affiliations).toHaveLength(0);
    expect(person.last_civilian_pre_service).toHaveLength(0);
    expect(person.other_pre_oss_affiliations).toHaveLength(0);
    expect(person.claims).toHaveLength(0);
  }
});

test("Batch 964 evidence excludes secrets and protected identifiers", () => {
  expect(evidence).not.toMatch(/"serial_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toMatch(/"service_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toContain("NARA_API_KEY");
  expect(evidence).not.toContain("x-api-key");
  expect(evidence).not.toContain("bulk_record_ordinal");
});

test("Batch 964 publishes exact coverage counters without changing the oil category", async ({ request, page }) => {
  const response = await request.get("./data/stats.json");
  expect(response.ok()).toBeTruthy();
  expect(await response.json()).toMatchObject({
    source_rows: 23_978,
    person_entities: 23_936,
    possible_duplicate_groups: 663,
    research_attempted_people: 15_108,
    verified_affiliation_people: 1_084,
    verified_employer_people: 486,
    archival_review_assessed_people: 13_584,
    published_claims: 9_483,
    public_sources: 6_172,
  });
  await page.goto("./oil-companies/");
  const main = page.locator("main");
  await expect(main).toContainText("14 people");
  await expect(main).toContainText("15 historically named");
  await expect(main).not.toContainText("Students");
});
