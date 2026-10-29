import fs from "node:fs";
import { expect, test } from "@playwright/test";
import type { APIRequestContext } from "@playwright/test";

const evidence = fs.readFileSync(
  new URL(
    "../../research/evidence-page468-francis-e-tifft-to-paul-tinken-review_batch-956_2026-10-29.json",
    import.meta.url,
  ),
  "utf8",
);

const profiles = [
  ["a0bd0a5a-c84a-583d-8c32-70f0d70ff0f5", "Francis E Tifft"],
  ["41e97d7c-2565-5045-a44e-106b7a50adf3", "Howard Tige"],
  ["0f8a3234-6350-5a2e-9267-5c694628432d", "Leslie C Tihany"],
  ["7d0c43ba-dbfa-58d2-ad26-3ff193f4713a", "Wilho Tikander"],
  ["1a7e8ce1-0cf5-5ebc-bf40-6ba680014bff", "Ellen Tilden"],
  ["d0598d0d-cd23-5ded-a0a2-1743c0c40086", "Fred F Tilden"],
  ["874180b1-ff6b-5554-9504-7d2fc87af7de", "Maurice Tillier"],
  ["8ce0b528-2f00-58cd-bf2e-6060a4c9c7fe", "Fritz G Tillisch"],
  ["31cbce2f-6538-5d21-9cb4-e3f891f11fc3", "David E Tillquist"],
  ["558046a4-244c-5692-b0ab-c50b1ebb18b9", "James L Tilly"],
  ["f450b8cf-d969-5276-99a1-fb75826843bc", "John T Timlin"],
  ["f2bd8f15-de2a-5220-9d22-866dfee20e50", "Eric W Timm"],
  ["3297f5e3-76fc-5d8d-81a0-ede4cbfbc1ed", "Otwell D Timmons"],
  ["188c1274-dce6-566a-90f4-59e272ed5cee", "Robert H Timmons"],
  ["d36d2d6f-02da-54e3-a648-bf17fd4d8d63", "Robert N Timmons"],
  ["d35174b0-5825-50f9-9d72-69270948de36", "Louis Timpanaro"],
  ["b2662fec-7f07-5a20-bb29-f1fdfc623a83", "Richard W Tims"],
  ["7251b2e3-58ce-548f-ac74-bccbc72fa0b2", "Richard Tims"],
  ["c2e53f26-0638-5ec9-80ee-af9d295e7505", "Charles P Tindall"],
  ["6eccefb8-1664-5c28-b4ab-c522e10e6e70", "Francis S Tindall"],
  ["f34c8b9d-f960-58a8-8c01-9db8c47a65c9", "Edgar J Tingle"],
  ["a8818ca9-a414-56d9-a1c0-e73e5dbca13b", "Joseph Tinkelman"],
  ["f6677edd-4954-5f08-8ebf-f07a88165a1d", "Paul Tinken"],
] as const;

const unresolvedIds = new Set([
  "41e97d7c-2565-5045-a44e-106b7a50adf3",
  "1a7e8ce1-0cf5-5ebc-bf40-6ba680014bff",
  "d0598d0d-cd23-5ded-a0a2-1743c0c40086",
  "874180b1-ff6b-5554-9504-7d2fc87af7de",
  "31cbce2f-6538-5d21-9cb4-e3f891f11fc3",
  "f450b8cf-d969-5276-99a1-fb75826843bc",
  "f2bd8f15-de2a-5220-9d22-866dfee20e50",
  "188c1274-dce6-566a-90f4-59e272ed5cee",
  "d36d2d6f-02da-54e3-a648-bf17fd4d8d63",
  "7251b2e3-58ce-548f-ac74-bccbc72fa0b2",
  "6eccefb8-1664-5c28-b4ab-c522e10e6e70",
  "f34c8b9d-f960-58a8-8c01-9db8c47a65c9",
  "f6677edd-4954-5f08-8ebf-f07a88165a1d",
]);

const armyCategories = [
  ["a0bd0a5a-c84a-583d-8c32-70f0d70ff0f5", "Francis E Tifft", "chauffeurs and drivers, bus, taxi, truck, and tractor", "employment", "1944-11-10"],
  ["b2662fec-7f07-5a20-bb29-f1fdfc623a83", "Richard W Tims", "semiprofessional occupations, n.e.c.", "employment", "1943-03-20"],
  ["c2e53f26-0638-5ec9-80ee-af9d295e7505", "Charles P Tindall", "students", "student", "1942-11-16"],
  ["a8818ca9-a414-56d9-a1c0-e73e5dbca13b", "Joseph Tinkelman", "students", "student", "1943-03-16"],
] as const;

async function peopleShard(request: APIRequestContext, letter: string) {
  const response = await request.get(`./data/people/${letter}.json`);
  expect(response.ok()).toBeTruthy();
  return response.json();
}

async function publicPerson(
  request: APIRequestContext,
  id: string,
  displayName: string,
) {
  const shard = await peopleShard(request, displayName[0].toLowerCase());
  return shard.find((item: { person_id: string }) => item.person_id === id);
}

test("Batch 956 publishes 23 audited people with terminal outcomes", async ({ page }) => {
  for (const [id, name] of profiles) {
    await page.goto(`./people/${id}/`);
    await expect(page.getByRole("heading", { name, level: 1 })).toBeVisible();
    const main = page.locator("main");
    await expect(main).not.toContainText("not started");
    await expect(main).not.toContainText("in progress");
    const serials = await main.locator("dt").filter({ hasText: /^Serial$/ })
      .locator("xpath=following-sibling::dd[1]").allTextContents();
    for (const value of serials) {
      expect(value).not.toMatch(/^[A-Z]?\s?\d{4,9}(?:RA)?$/);
    }
  }
});

test("Louis Timpanaro publishes a confirmed immediate employer and last civilian employer", async ({ request, page }) => {
  const person = await publicPerson(
    request,
    "d35174b0-5825-50f9-9d72-69270948de36",
    "Louis Timpanaro",
  );
  expect(person).toMatchObject({
    identity_status: "confirmed",
    research_status: "verified_employer_found",
    personnel_category: "enlisted_army_personnel",
    commissioned_officer: false,
  });
  const expectedEmployer = expect.objectContaining({
    canonical_organization: "Artex Spraying Company",
    historical_organization: "Artex Spraying Company",
    role_title: "auto and wood sprayer",
    occupation: "spray painter",
    relationship_type: "employment",
    end_date: "1942-11-19",
    immediate_pre_oss: true,
    last_civilian_pre_service: true,
    temporal_basis: "explicit_immediate",
    identity_confidence: "confirmed",
    claim_confidence: "confirmed",
  });
  expect(person.immediate_pre_oss_affiliations).toEqual([expectedEmployer]);
  expect(person.last_civilian_pre_service).toEqual([expectedEmployer]);
  await page.goto("./people/d35174b0-5825-50f9-9d72-69270948de36/");
  const main = page.locator("main");
  await expect(main).toContainText("Artex Spraying Company");
  await expect(main).toContainText("auto and wood sprayer");
  await expect(main).toContainText("explicit immediate");
});

test("Wilho Tikander publishes confirmed identity and dated Justice Department work without claiming immediacy", async ({ request, page }) => {
  const person = await publicPerson(
    request,
    "7d0c43ba-dbfa-58d2-ad26-3ff193f4713a",
    "Wilho Tikander",
  );
  expect(person).toMatchObject({
    identity_status: "confirmed",
    research_status: "completed",
    personnel_category: "civilian_professional_or_administrative_grade",
  });
  expect(person.immediate_pre_oss_affiliations).toHaveLength(0);
  expect(person.last_civilian_pre_service).toHaveLength(0);
  expect(person.other_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      canonical_organization: "U.S. Department of Justice",
      role_title: "Special Attorney",
      relationship_type: "government_assignment",
      end_date: "1940-07-24",
      temporal_basis: "documented_prewar",
      claim_confidence: "high",
    }),
  ]);
  await page.goto("./people/7d0c43ba-dbfa-58d2-ad26-3ff193f4713a/");
  const main = page.locator("main");
  await expect(main).toContainText("OSS Chief in Stockholm");
  await expect(main).toContainText("Special Attorney");
  await expect(main).toContainText("does not establish the exact OSS recruitment date");
});

test("Fritz Tillisch keeps the indexed spelling and qualified Danish chronology", async ({ request, page }) => {
  const person = await publicPerson(
    request,
    "8ce0b528-2f00-58cd-bf2e-6060a4c9c7fe",
    "Fritz G Tillisch",
  );
  expect(person.name_variants).toContain("Frits Gustav Tillisch");
  expect(person).toMatchObject({
    identity_status: "high_confidence",
    research_status: "completed",
    personnel_category: "foreign_or_allied_military_personnel",
    commissioned_officer: true,
  });
  expect(person.immediate_pre_oss_affiliations).toHaveLength(0);
  expect(person.last_civilian_pre_service).toHaveLength(0);
  expect(person.other_pre_oss_affiliations).toEqual(expect.arrayContaining([
    expect.objectContaining({
      canonical_organization: "Royal Danish Army",
      temporal_basis: "documented_prewar",
    }),
    expect.objectContaining({
      canonical_organization: "Danish Military Intelligence Service (wartime illegal service)",
      temporal_basis: "temporal_relation_uncertain",
      publication_status: "publish_qualified",
    }),
  ]));
  await page.goto("./people/8ce0b528-2f00-58cd-bf2e-6060a4c9c7fe/");
  await expect(page.locator("main")).toContainText("not labeled immediate pre-OSS");
});

test("Army bulk matches publish only qualified categories and never invented employers", async ({ request }) => {
  for (const [id, name, occupation, relationshipType, endDate] of armyCategories) {
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
        end_date: endDate,
        temporal_basis: "strongly_date_bounded",
        claim_confidence: "medium",
      }),
    ]);
  }
});

test("Leslie Tihany and Otwell Timmons remain qualified and James Tilly stays archival", async ({ request }) => {
  const leslie = await publicPerson(request, "0f8a3234-6350-5a2e-9267-5c694628432d", "Leslie C Tihany");
  expect(leslie.other_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      canonical_organization: null,
      occupation: "linguist and scholar",
      relationship_type: "professional_affiliation",
      end_date: "1940-06",
    }),
  ]);
  expect(leslie.last_civilian_pre_service).toHaveLength(0);

  const otwell = await publicPerson(request, "3297f5e3-76fc-5d8d-81a0-ede4cbfbc1ed", "Otwell D Timmons");
  expect(otwell.immediate_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      canonical_organization: "United States Army",
      relationship_type: "military_assignment",
      temporal_basis: "probable_immediate",
      claim_confidence: "medium",
    }),
  ]);
  expect(otwell.last_civilian_pre_service).toHaveLength(0);

  const james = await publicPerson(request, "558046a4-244c-5692-b0ab-c50b1ebb18b9", "James L Tilly");
  expect(james).toMatchObject({
    identity_status: "high_confidence",
    research_status: "requires_archival_review",
    personnel_category: "commissioned_army_officer",
    commissioned_officer: true,
  });
  expect(james.immediate_pre_oss_affiliations).toHaveLength(0);
  expect(james.last_civilian_pre_service).toHaveLength(0);
});

test("thirteen unresolved people keep archival outcomes without transferred facts", async ({ request }) => {
  for (const [id, name] of profiles.filter(([id]) => unresolvedIds.has(id))) {
    const person = await publicPerson(request, id, name);
    expect(person).toMatchObject({
      identity_status: "unresolved",
      research_status: "requires_archival_review",
      personnel_category: "unknown_or_indeterminate",
    });
    expect(person.immediate_pre_oss_affiliations).toHaveLength(0);
    expect(person.last_civilian_pre_service).toHaveLength(0);
    expect(person.other_pre_oss_affiliations).toHaveLength(0);
    expect(person.claims).toHaveLength(0);
  }
});

test("Batch 956 evidence excludes secrets and protected-identifier fields", () => {
  expect(evidence).not.toMatch(/"serial_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toMatch(/"service_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toContain("NARA_API_KEY");
  expect(evidence).not.toContain("x-api-key");
  expect(evidence).not.toContain("bulk_record_ordinal");
});

test("Batch 956 publishes exact coverage counters without changing the oil category", async ({ request, page }) => {
  const response = await request.get("./data/stats.json");
  expect(response.ok()).toBeTruthy();
  expect(await response.json()).toMatchObject({
    source_rows: 23_978,
    person_entities: 23_936,
    possible_duplicate_groups: 648,
    research_attempted_people: 14_926,
    verified_affiliation_people: 1_058,
    verified_employer_people: 473,
    archival_review_assessed_people: 13_402,
    published_claims: 9_284,
    public_sources: 6_071,
  });
  await page.goto("./oil-companies/");
  const main = page.locator("main");
  await expect(main).toContainText("14 people");
  await expect(main).toContainText("15 historically named");
  await expect(main).not.toContainText("Artex Spraying Company");
});
