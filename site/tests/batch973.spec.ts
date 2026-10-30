import fs from "node:fs";
import { expect, test } from "@playwright/test";
import type { APIRequestContext } from "@playwright/test";

const evidence = fs.readFileSync(
  new URL(
    "../../research/evidence-page477-robert-tyson-to-doris-ulmer-review_batch-973_2026-10-30.json",
    import.meta.url,
  ),
  "utf8",
);

const profiles = [
  ["ee68d2b2-2b29-57ae-b381-2afa4762953f", "Robert M Tyson"],
  ["bb632a58-a6c6-517a-8fa5-84e250185644", "John D Tyus"],
  ["e4a178e3-5b78-53a9-b5d6-384661eec6e5", "Basil Tzitzis"],
  ["085ff861-6de1-5f7e-817e-8b7f0edf1734", "Bruno Uberti"],
  ["e57fb641-762d-5337-973a-e483baec31dd", "John N Uccellini"],
  ["cd11446a-8c89-5d7a-9df0-1aab4f038ea3", "Edward J Uchno"],
  ["609741dd-dcbd-52f6-a07c-7e787ea110ff", "Louis D Udvari"],
  ["3fcd03ff-e331-5ef4-9204-1398a6af1584", "Charles Uehara"],
  ["29f4b909-e41b-526c-8445-a39db466fad9", "Philip P Ugiss"],
  ["50a6b801-5bcc-502f-9446-b52a9d70b963", "Joseph E Uher"],
  ["c89e5ba9-8b2e-5002-aecf-0f932f13f8da", "Katherine L Uhler"],
  ["740604f3-1388-57f3-803f-96cf7120b0c5", "Lottie Uhlfelder"],
  ["48260e6b-f244-57b6-be8f-5c2d8ee2c74d", "John D Ukrop"],
  ["51db351b-7ebb-5bb8-baef-1dbcf923876c", "Robert Ulich"],
  ["f82fa3bc-3391-50ca-ba0e-c1c52b1e73f0", "John Ulivelli"],
  ["674731e3-d0e1-5de5-bf5d-a53ed586b806", "Edward L Ullman"],
  ["c869743e-850c-5045-bbef-5ca46c834aa8", "Maurice S Ullman"],
  ["5eda059a-79a4-53cf-88a7-af55d8361f31", "Paul Ullman"],
  ["35fcd984-3c1b-5d81-9860-e78ae844988d", "Robert Ullman"],
  ["9ccd8f48-5c5e-5ca1-95d2-477a6e5e473a", "Elinor Ulman"],
  ["db799a3d-911d-5efb-885b-e26e9597189a", "Louis M Ulmann"],
  ["f097cf61-b748-5a27-af34-8021a6b6e43d", "Alfred C Ulmer"],
  ["f9fdff5e-bd5e-5a02-81c7-b5da3fb2f350", "Doris B Ulmer"],
] as const;

const armyOccupationProfiles = [
  ["ee68d2b2-2b29-57ae-b381-2afa4762953f", "Robert M Tyson", "manager or official, not elsewhere classified", "unknown"],
  ["bb632a58-a6c6-517a-8fa5-84e250185644", "John D Tyus", "barber, beautician or manicurist", "unknown"],
  ["e4a178e3-5b78-53a9-b5d6-384661eec6e5", "Basil Tzitzis", "construction or maintenance painter", "unknown"],
  ["e57fb641-762d-5337-973a-e483baec31dd", "John N Uccellini", "machinist", "unknown"],
  ["48260e6b-f244-57b6-be8f-5c2d8ee2c74d", "John D Ukrop", "student", "student"],
] as const;

const unresolvedProfiles = [
  ["609741dd-dcbd-52f6-a07c-7e787ea110ff", "Louis D Udvari"],
  ["3fcd03ff-e331-5ef4-9204-1398a6af1584", "Charles Uehara"],
  ["29f4b909-e41b-526c-8445-a39db466fad9", "Philip P Ugiss"],
  ["50a6b801-5bcc-502f-9446-b52a9d70b963", "Joseph E Uher"],
  ["c89e5ba9-8b2e-5002-aecf-0f932f13f8da", "Katherine L Uhler"],
  ["740604f3-1388-57f3-803f-96cf7120b0c5", "Lottie Uhlfelder"],
  ["f82fa3bc-3391-50ca-ba0e-c1c52b1e73f0", "John Ulivelli"],
  ["c869743e-850c-5045-bbef-5ca46c834aa8", "Maurice S Ullman"],
  ["9ccd8f48-5c5e-5ca1-95d2-477a6e5e473a", "Elinor Ulman"],
  ["db799a3d-911d-5efb-885b-e26e9597189a", "Louis M Ulmann"],
  ["f9fdff5e-bd5e-5a02-81c7-b5da3fb2f350", "Doris B Ulmer"],
] as const;

async function publicPerson(request: APIRequestContext, id: string, name: string) {
  const response = await request.get(`./data/people/${name[0].toLowerCase()}.json`);
  expect(response.ok()).toBeTruthy();
  return (await response.json()).find((item: { person_id: string }) => item.person_id === id);
}

test("Batch 973 publishes all 23 audited people with terminal outcomes", async ({ page }) => {
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

test("five Army categories remain qualified occupation or student findings without employers", async ({ request }) => {
  for (const [id, name, occupation, relationshipType] of armyOccupationProfiles) {
    const person = await publicPerson(request, id, name);
    expect(person).toMatchObject({
      identity_status: "high_confidence",
      research_status: "occupation_only_found",
      personnel_category: "enlisted_army_personnel",
      commissioned_officer: false,
    });
    expect(person.immediate_pre_oss_affiliations).toHaveLength(0);
    expect(person.last_civilian_pre_service).toHaveLength(0);
    expect(person.other_pre_oss_affiliations).toEqual(expect.arrayContaining([
      expect.objectContaining({
        canonical_organization: null,
        occupation,
        relationship_type: relationshipType,
        temporal_basis: "documented_prewar",
        claim_confidence: "medium",
        publication_status: "publish_qualified",
      }),
    ]));
  }
});

test("Bruno Uberti publishes an immediate Army Medical Corps assignment, not a civilian employer", async ({ request, page }) => {
  const person = await publicPerson(request, "085ff861-6de1-5f7e-817e-8b7f0edf1734", "Bruno Uberti");
  expect(person).toMatchObject({
    identity_status: "high_confidence",
    personnel_category: "commissioned_army_officer",
    commissioned_officer: true,
  });
  expect(person.immediate_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      canonical_organization: "United States Army Medical Corps",
      relationship_type: "military_assignment",
      temporal_basis: "explicit_immediate",
      claim_confidence: "high",
    }),
  ]);
  expect(person.last_civilian_pre_service).toHaveLength(0);
  await page.goto("./organizations/684d8dc3-57fe-51f0-88a2-084514015c8f/");
  await expect(page.locator("main")).toContainText("Bruno Uberti");
});

test("Robert Ulich publishes Harvard as immediate and last civilian employer", async ({ request, page }) => {
  const person = await publicPerson(request, "51db351b-7ebb-5bb8-baef-1dbcf923876c", "Robert Ulich");
  expect(person).toMatchObject({ identity_status: "high_confidence", research_status: "verified_employer_found" });
  for (const affiliation of [person.immediate_pre_oss_affiliations[0], person.last_civilian_pre_service[0]]) {
    expect(affiliation).toMatchObject({
      canonical_organization: "Harvard Graduate School of Education",
      role_title: "Professor of the History and Philosophy of Education",
      relationship_type: "employment",
      temporal_basis: "strongly_date_bounded",
      claim_confidence: "high",
    });
  }
  await page.goto("./organizations/6835d848-b0b6-517e-b63b-6b7c24f3e659/");
  await expect(page.locator("main")).toContainText("Robert Ulich");
});

test("Edward Ullman is a probable University of Chicago student, not an employee", async ({ request }) => {
  const person = await publicPerson(request, "674731e3-d0e1-5de5-bf5d-a53ed586b806", "Edward L Ullman");
  expect(person.immediate_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      canonical_organization: "University of Chicago",
      role_title: "doctoral student in geography",
      relationship_type: "student",
      temporal_basis: "probable_immediate",
      claim_confidence: "medium",
      publication_status: "publish_qualified",
    }),
  ]);
  expect(person.last_civilian_pre_service).toHaveLength(0);
});

test("Paul Ullman keeps stockbroker, AFS volunteer and artist evidence distinct", async ({ request }) => {
  const person = await publicPerson(request, "5eda059a-79a4-53cf-88a7-af55d8361f31", "Paul Ullman");
  expect(person.immediate_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      canonical_organization: null,
      occupation: "stockbroker",
      relationship_type: "unknown",
      temporal_basis: "explicit_immediate",
      claim_confidence: "medium",
    }),
  ]);
  expect(person.last_civilian_pre_service).toHaveLength(0);
  expect(person.other_pre_oss_affiliations).toEqual(expect.arrayContaining([
    expect.objectContaining({ canonical_organization: "American Field Service", relationship_type: "volunteer" }),
    expect.objectContaining({ canonical_organization: null, occupation: "painter and illustrator", relationship_type: "unknown" }),
  ]));
});

test("Robert Ullman remains a probable Pathé candidate outside default analytics", async ({ request }) => {
  const person = await publicPerson(request, "35fcd984-3c1b-5d81-9860-e78ae844988d", "Robert Ullman");
  expect(person).toMatchObject({ identity_status: "probable", research_status: "requires_archival_review" });
  expect(person.immediate_pre_oss_affiliations).toHaveLength(0);
  expect(person.last_civilian_pre_service).toHaveLength(0);
  expect(person.other_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      canonical_organization: "Pathé News",
      relationship_type: "employment",
      temporal_basis: "temporal_relation_uncertain",
      claim_confidence: "medium",
      publication_status: "publish_qualified",
    }),
  ]);
});

test("Alfred Ulmer separates Navy, advertising and newspaper chronology", async ({ request, page }) => {
  const person = await publicPerson(request, "f097cf61-b748-5a27-af34-8021a6b6e43d", "Alfred C Ulmer");
  expect(person).toMatchObject({
    identity_status: "high_confidence",
    research_status: "documented_prewar_employer_found",
    personnel_category: "commissioned_naval_officer",
    commissioned_officer: true,
  });
  expect(person.immediate_pre_oss_affiliations).toEqual([
    expect.objectContaining({ canonical_organization: "Office of Naval Intelligence", relationship_type: "military_assignment", temporal_basis: "explicit_immediate", claim_confidence: "high" }),
  ]);
  expect(person.last_civilian_pre_service).toEqual([
    expect.objectContaining({ canonical_organization: "Benton & Bowles", relationship_type: "employment", claim_confidence: "medium" }),
  ]);
  expect(person.other_pre_oss_affiliations).toEqual([
    expect.objectContaining({ canonical_organization: "Jacksonville Journal", role_title: "newspaper reporter", temporal_basis: "documented_prewar" }),
  ]);
  for (const [id, name] of [
    ["f45dd890-7883-5272-9f32-4eb34218760f", "Office of Naval Intelligence"],
    ["fd1f6ea8-99fa-58a9-b81f-b9f9f2f47a08", "Benton & Bowles"],
    ["018ca21e-d906-5f9f-afed-99b5bacd9af4", "Jacksonville Journal"],
  ]) {
    await page.goto(`./organizations/${id}/`);
    await expect(page.getByRole("heading", { name, level: 1 })).toBeVisible();
    await expect(page.locator("main")).toContainText("Alfred C Ulmer");
  }
});

test("undefined Army code supports Edward Uchno's identity only", async ({ request }) => {
  const person = await publicPerson(request, "cd11446a-8c89-5d7a-9df0-1aab4f038ea3", "Edward J Uchno");
  expect(person).toMatchObject({
    identity_status: "high_confidence",
    research_status: "requires_archival_review",
    personnel_category: "enlisted_army_personnel",
    commissioned_officer: false,
  });
  expect(person.immediate_pre_oss_affiliations).toHaveLength(0);
  expect(person.last_civilian_pre_service).toHaveLength(0);
  expect(person.other_pre_oss_affiliations).toHaveLength(0);
  expect(person.claims).toEqual([
    expect.objectContaining({ claim_type: "identity", claim_confidence: "high", publication_status: "published" }),
  ]);
});

test("eleven unresolved profiles remain dignified archival-review cases", async ({ request }) => {
  for (const [id, name] of unresolvedProfiles) {
    const person = await publicPerson(request, id, name);
    expect(person).toMatchObject({
      identity_status: "unresolved",
      research_status: "requires_archival_review",
      manual_review_required: true,
    });
    expect(person.immediate_pre_oss_affiliations).toHaveLength(0);
    expect(person.last_civilian_pre_service).toHaveLength(0);
    expect(person.other_pre_oss_affiliations).toHaveLength(0);
    expect(person.claims).toHaveLength(0);
  }
});

test("Batch 973 evidence excludes secrets, full identifiers and raw bulk records", () => {
  expect(evidence).not.toMatch(/"serial_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toMatch(/"service_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toContain("NARA_API_KEY");
  expect(evidence).not.toContain("x-api-key");
  expect(evidence).not.toContain("candidate_identifier");
  expect(evidence).not.toContain("bulk_record_ordinal");
});

test("Batch 973 publishes exact coverage counters and preserves oil counts", async ({ request, page }) => {
  const response = await request.get("./data/stats.json");
  expect(response.ok()).toBeTruthy();
  expect(await response.json()).toMatchObject({
    source_rows: 23_978,
    person_entities: 23_936,
    possible_duplicate_groups: 664,
    research_attempted_people: 15_315,
    verified_affiliation_people: 1_100,
    verified_employer_people: 491,
    archival_review_assessed_people: 13_791,
    published_claims: 9_706,
    public_sources: 6_280,
  });
  await page.goto("./oil-companies/");
  const main = page.locator("main");
  await expect(main).toContainText("14 people");
  await expect(main).toContainText("15 historically named");
});
