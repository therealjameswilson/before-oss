import fs from "node:fs";
import { expect, test } from "@playwright/test";
import type { APIRequestContext } from "@playwright/test";

const evidence = fs.readFileSync(
  new URL(
    "../../research/evidence-page464-marcelen-j-tezak-to-milton-theaman-review_batch-947_2026-10-28.json",
    import.meta.url,
  ),
  "utf8",
);

const profiles = [
  ["f9f222b7-721e-54fc-9bcd-e22ad431a59f", "Marcelen J Tezak"],
  ["d2783d4b-fe3b-560d-b190-f6f84e6de449", "William M Thabit"],
  ["4c53ed20-1ce2-507d-a269-34b4bd9eb7ca", "Vera L Thacher"],
  ["a29532d6-9a7c-5f1e-b629-13b2e5b7b5ab", "Henry H Thackthwaite"],
  ["403f4110-6b65-5ad9-9953-88cc025cc06e", "Shelby Thames"],
  ["99367b41-0a3e-5c62-aef5-3104871326bd", "Travis H Thames"],
  ["0cd1511a-436c-5194-8cb8-8fc06f3704f2", "Spiro Thanas"],
  ["1c92d07c-cd55-5e30-b2a4-e08d875b4053", "William J Thanos"],
  ["d8530779-7a9c-5320-b4f7-3da486e87dc4", "William Thanos"],
  ["192eba0d-f4e2-5312-94bf-0296d77898ef", "Melvin E Tharp"],
  ["7d9b1c4a-da89-520e-8cbf-5f710df54b6a", "Melvin E Tharp"],
  ["b07b5eb3-e214-51be-bf1f-74bab9fcec48", "Robert E Tharp"],
  ["bb719215-673f-594d-a912-d2b97c02d1b0", "William G Tharp"],
  ["a6b1e854-e46e-504a-8d46-fca99c2da9fc", "Kathryn L Tharpe"],
  ["642defc6-04d1-5ac0-9662-e4a5c22454ff", "Herbert S Thatcher"],
  ["289cb16a-9b6f-5f3b-a998-3d93b87d9cd2", "Charles W Thayer"],
  ["41a0b4c5-ff81-52f7-ae21-5bbaf74742ab", "Frank A Thayer"],
  ["b925f995-0e43-5318-b36c-83627a67fe75", "Guy V Thayer"],
  ["11cb30b6-b205-5398-951d-25b488c3ca42", "John O Thayer"],
  ["c802b855-fe16-54cc-b66b-ddc1df2d6aaa", "William F Thayer"],
  ["2865eae8-783c-5524-849e-5c4f981cf01f", "William A Thayer"],
  ["85cf7aaf-41bb-520b-9b90-3eb782d0c1df", "William A Thayer"],
  ["748e62ad-1fcb-57da-9267-515ca36220c8", "Milton Theaman"],
] as const;

async function peopleShard(request: APIRequestContext, letter: string) {
  const response = await request.get(`./data/people/${letter}.json`);
  expect(response.ok()).toBeTruthy();
  return response.json();
}

test("Batch 947 publishes all 23 indexed-row entities with terminal outcomes", async ({ page }) => {
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

test("the Thanos, Melvin Tharp and William Thayer duplicate rows remain separate", async ({ request }) => {
  const pairs = [
    ["w", "1c92d07c-cd55-5e30-b2a4-e08d875b4053", "d8530779-7a9c-5320-b4f7-3da486e87dc4"],
    ["m", "7d9b1c4a-da89-520e-8cbf-5f710df54b6a", "192eba0d-f4e2-5312-94bf-0296d77898ef"],
    ["w", "85cf7aaf-41bb-520b-9b90-3eb782d0c1df", "2865eae8-783c-5524-849e-5c4f981cf01f"],
  ] as const;
  for (const [letter, bridgedId, unbridgedId] of pairs) {
    const people = await peopleShard(request, letter);
    const bridged = people.find((item: { person_id: string }) => item.person_id === bridgedId);
    const unbridged = people.find((item: { person_id: string }) => item.person_id === unbridgedId);
    expect(bridged.person_id).not.toBe(unbridged.person_id);
    expect(bridged.possible_duplicate_group).toBe(unbridged.possible_duplicate_group);
    expect(bridged.identity_status).toBe("high_confidence");
    expect(unbridged.identity_status).toBe("ambiguous");
    expect(unbridged.claims).toHaveLength(0);
    expect(unbridged.other_pre_oss_affiliations).toHaveLength(0);
  }
});

test("Henry Thackthwaite remains a British SOE officer with separate Army and civilian history", async ({ request, page }) => {
  const person = (await peopleShard(request, "h")).find(
    (item: { person_id: string }) => item.person_id === "a29532d6-9a7c-5f1e-b629-13b2e5b7b5ab",
  );
  expect(person).toMatchObject({
    identity_status: "high_confidence",
    research_status: "needs_temporal_review",
    personnel_category: "foreign_or_allied_military_personnel",
    commissioned_officer: true,
    allied_or_foreign_personnel: true,
  });
  expect(person.immediate_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      canonical_organization: "Special Operations Executive",
      relationship_type: "government_assignment",
      claim_confidence: "high",
      temporal_basis: "explicit_immediate",
    }),
  ]);
  expect(person.other_pre_oss_affiliations).toEqual(expect.arrayContaining([
    expect.objectContaining({ canonical_organization: "Royal Army Service Corps", relationship_type: "military_assignment" }),
    expect.objectContaining({ canonical_organization: null, occupation: "translator and teacher", claim_confidence: "medium" }),
  ]));
  await page.goto("./people/a29532d6-9a7c-5f1e-b629-13b2e5b7b5ab/");
  const main = page.locator("main");
  await expect(main).toContainText("British");
  await expect(main).toContainText("Special Operations Executive");
  await expect(main).toContainText("Royal Army Service Corps");
});

test("Charles Thayer publishes State as a qualified government predecessor, not a civilian employer", async ({ request, page }) => {
  const person = (await peopleShard(request, "c")).find(
    (item: { person_id: string }) => item.person_id === "289cb16a-9b6f-5f3b-a998-3d93b87d9cd2",
  );
  expect(person).toMatchObject({
    identity_status: "high_confidence",
    research_status: "needs_temporal_review",
    personnel_category: "commissioned_army_officer",
    commissioned_officer: true,
  });
  expect(person.immediate_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      canonical_organization: "United States Department of State",
      relationship_type: "government_assignment",
      temporal_basis: "probable_immediate",
      claim_confidence: "high",
      publication_status: "publish_qualified",
    }),
  ]);
  expect(person.last_civilian_pre_service).toHaveLength(0);
  await page.goto("./people/289cb16a-9b6f-5f3b-a998-3d93b87d9cd2/");
  const main = page.locator("main");
  await expect(main).toContainText("United States Department of State");
  await expect(main).toContainText("Probable immediate");
});

test("Milton Theaman publishes direct OSS staff identity but no invented pre-OSS employer", async ({ request, page }) => {
  const person = (await peopleShard(request, "m")).find(
    (item: { person_id: string }) => item.person_id === "748e62ad-1fcb-57da-9267-515ca36220c8",
  );
  expect(person).toMatchObject({
    identity_status: "high_confidence",
    research_status: "requires_archival_review",
    personnel_category: "commissioned_army_officer",
    commissioned_officer: true,
  });
  expect(person.immediate_pre_oss_affiliations).toHaveLength(0);
  expect(person.last_civilian_pre_service).toHaveLength(0);
  expect(person.other_pre_oss_affiliations).toHaveLength(0);
  expect(person.claims).toEqual([
    expect.objectContaining({ claim_type: "identity", claim_confidence: "high" }),
  ]);
  await page.goto("./people/748e62ad-1fcb-57da-9267-515ca36220c8/");
  const main = page.locator("main");
  await expect(main).toContainText("OSS Assessment Staff");
  await expect(main).toContainText("Fairfax");
});

test("reviewed Army categories stay unnamed and Student is status, not employment", async ({ request }) => {
  const cases = [
    ["t", "99367b41-0a3e-5c62-aef5-3104871326bd", "general farmer", "employment"],
    ["s", "0cd1511a-436c-5194-8cb8-8fc06f3704f2", "skilled occupation in manufacture of miscellaneous products", "employment"],
    ["w", "1c92d07c-cd55-5e30-b2a4-e08d875b4053", "student", "student"],
    ["m", "7d9b1c4a-da89-520e-8cbf-5f710df54b6a", "manager or official, not elsewhere classified", "employment"],
    ["f", "41a0b4c5-ff81-52f7-ae21-5bbaf74742ab", "skilled general woodworking occupation, not elsewhere classified", "employment"],
    ["w", "c802b855-fe16-54cc-b66b-ddc1df2d6aaa", "skilled bakery-production occupation, not elsewhere classified", "employment"],
    ["w", "85cf7aaf-41bb-520b-9b90-3eb782d0c1df", "semiskilled mechanical metal-treatment occupation, not elsewhere classified", "employment"],
  ] as const;
  for (const [letter, id, occupation, relationshipType] of cases) {
    const person = (await peopleShard(request, letter)).find(
      (item: { person_id: string }) => item.person_id === id,
    );
    expect(person.personnel_category).toBe("enlisted_army_personnel");
    expect(person.commissioned_officer).toBe(false);
    expect(person.immediate_pre_oss_affiliations).toHaveLength(0);
    expect(person.last_civilian_pre_service).toHaveLength(0);
    expect(person.other_pre_oss_affiliations[0]).toMatchObject({
      canonical_organization: null,
      organization_name_as_found: null,
      occupation,
      relationship_type: relationshipType,
      claim_confidence: "medium",
    });
  }
  const marcelen = (await peopleShard(request, "m")).find(
    (item: { person_id: string }) => item.person_id === "f9f222b7-721e-54fc-9bcd-e22ad431a59f",
  );
  expect(marcelen.other_pre_oss_affiliations).toHaveLength(0);
  expect(marcelen.claims).toHaveLength(1);
});

test("William Thayer collision is explicit and protected identifiers stay excluded", () => {
  expect(evidence).toContain("Hucal Julian S");
  expect(evidence).toContain("explicitly rejected as a name conflict");
  expect(evidence).not.toMatch(/"serial_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toMatch(/"service_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toContain("NARA_API_KEY");
  expect(evidence).not.toContain("x-api-key");
});

test("Batch 947 does not change the evidence-defined oil-company category", async ({ page }) => {
  await page.goto("./oil-companies/");
  const main = page.locator("main");
  await expect(main).toContainText("14 people");
  await expect(main).toContainText("15 historically named");
  await expect(main).not.toContainText("Special Operations Executive");
});

test("Batch 947 publishes its exact coverage counters", async ({ request }) => {
  const response = await request.get("./data/stats.json");
  expect(response.ok()).toBeTruthy();
  const stats = await response.json();
  expect(stats).toMatchObject({
    source_rows: 23_978,
    person_entities: 23_936,
    possible_duplicate_groups: 648,
    research_attempted_people: 14_722,
    verified_affiliation_people: 1_046,
    verified_employer_people: 470,
    archival_review_assessed_people: 13_196,
    published_claims: 9_143,
    public_sources: 6_009,
  });
});
