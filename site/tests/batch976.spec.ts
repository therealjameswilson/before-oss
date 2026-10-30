import fs from "node:fs";
import { expect, test } from "@playwright/test";
import type { APIRequestContext } from "@playwright/test";

const evidence = fs.readFileSync(
  new URL(
    "../../research/evidence-page478-sylvester-vacek-to-florencio-valenzuela-review_batch-976_2026-10-30.json",
    import.meta.url,
  ),
  "utf8",
);

const profiles = [
  ["63edeaf2-394b-599c-a9f3-48def87e523c", "Sylvester Vacek"],
  ["04165636-ad69-57ff-a11d-0fea61f27292", "Vincenzon Vacirca"],
  ["299230c6-8400-5b77-8eaf-8a4def43e1de", "Charoen Vadhanapanic"],
  ["2edfdc1d-702d-5dc1-9752-b6ca8139c458", "Anthony Vaiksnoras"],
  ["0bdab0b0-0954-584c-8639-a5d283b2d1a3", "Margaret B Vaill"],
  ["bfc6beb7-301b-5682-987f-da0eac235d2c", "Anthony S Vaivada"],
  ["fdcccd3f-98b3-565d-a3ba-eaad1b1dc784", "Vichien Vaivananda"],
  ["5f7f6bb9-09ce-5fc0-9163-be180cb21bb8", "Sotirios G Vakakas"],
  ["57ef22b9-66d9-56c7-99f8-133c3ce7d06a", "Apollon P Valakis"],
  ["cd78f351-8de8-5fc0-84c0-15a00c2b77aa", "Filippo A Valastro"],
  ["3904fff6-2313-58e0-9b07-fcd7f493694d", "Stanley Valcik"],
  ["89c7af4d-a67d-5c86-9680-707b8a5e8a58", "Jean P Valdene"],
  ["0a371ef8-9386-5927-a802-d2a6963916f2", "Carlos Valensuela"],
  ["b570bd27-976a-504b-bb5f-9b64682e9997", "Louis Valenti"],
  ["d36b2f94-17a6-5066-98af-01bc22048595", "Pasquale T Valenti"],
  ["30c32dd3-ecef-5fab-99dd-392c1b96c037", "RJM V Valentin"],
  ["dba02895-ce3a-52fb-9224-d8be5b4642b2", "Bruce M Valentine"],
  ["15c5233f-1550-566d-ba2f-b64a72e87a5e", "John Valentine"],
  ["8c283028-2b56-5fc8-a781-e0dc1764a80d", "Samuel B Valentine"],
  ["3eb23c79-6499-5e37-8c14-fde6d6689e74", "Bruno J Valentini"],
  ["68dc73e2-108a-5d19-96d9-651a51fd5f13", "Charles B Valentino"],
  ["096babf3-1468-5d0e-a850-446373260405", "Matthew A Valenza"],
  ["641721b1-af7b-5027-87b1-701f31ef03c1", "Florencio A Valenzuela"],
] as const;

async function publicPerson(request: APIRequestContext, id: string, name: string) {
  const response = await request.get(`./data/people/${name[0].toLowerCase()}.json`);
  expect(response.ok()).toBeTruthy();
  return (await response.json()).find((item: { person_id: string }) => item.person_id === id);
}

test("Batch 976 publishes all 23 audited people with terminal outcomes", async ({ page }) => {
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

test("five protected Army matches publish occupation or student evidence, never employers", async ({ request }) => {
  const expected = [
    ["2edfdc1d-702d-5dc1-9752-b6ca8139c458", "Anthony Vaiksnoras", "artist, sculptor or teacher of art", "unknown"],
    ["cd78f351-8de8-5fc0-84c0-15a00c2b77aa", "Filippo A Valastro", "actor", "unknown"],
    ["68dc73e2-108a-5d19-96d9-651a51fd5f13", "Charles B Valentino", "construction worker, not elsewhere classified", "unknown"],
    ["096babf3-1468-5d0e-a850-446373260405", "Matthew A Valenza", "construction worker, not elsewhere classified", "unknown"],
    ["641721b1-af7b-5027-87b1-701f31ef03c1", "Florencio A Valenzuela", "student", "student"],
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
    expect(person.other_pre_oss_affiliations).toEqual(expect.arrayContaining([
      expect.objectContaining({
        canonical_organization: null,
        occupation,
        relationship_type: relationshipType,
        claim_confidence: "medium",
        publication_status: "publish_qualified",
      }),
    ]));
  }
});

test("Vaiksnoras keeps art-school student status separate from Army occupation evidence", async ({ request }) => {
  const person = await publicPerson(request, "2edfdc1d-702d-5dc1-9752-b6ca8139c458", "Anthony Vaiksnoras");
  expect(person.name_variants).toEqual(expect.arrayContaining(["Anthony J. Vaiksnoras", "V IKSNORAS ANTHONY JR"]));
  expect(person.other_pre_oss_affiliations).toEqual(expect.arrayContaining([
    expect.objectContaining({
      canonical_organization: "Cleveland School of Art",
      relationship_type: "student",
      temporal_basis: "strongly_date_bounded",
      claim_confidence: "high",
    }),
    expect.objectContaining({
      canonical_organization: null,
      relationship_type: "unknown",
      claim_confidence: "medium",
    }),
  ]));
});

test("Vacirca separates qualified 1942 VOA context from earlier La Strada employment", async ({ request }) => {
  const person = await publicPerson(request, "04165636-ad69-57ff-a11d-0fea61f27292", "Vincenzon Vacirca");
  expect(person).toMatchObject({
    identity_status: "high_confidence",
    research_status: "verified_employer_found",
    personnel_category: "civilian_professional_or_administrative_grade",
    commissioned_officer: false,
  });
  expect(person.name_variants).toContain("Vincenzo Vacirca");
  expect(person.immediate_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      canonical_organization: "Voice of America",
      relationship_type: "government_assignment",
      temporal_basis: "probable_immediate",
      claim_confidence: "medium",
      publication_status: "publish_qualified",
    }),
  ]);
  expect(person.last_civilian_pre_service).toHaveLength(0);
  expect(person.other_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      canonical_organization: "La Strada",
      relationship_type: "employment",
      temporal_basis: "documented_prewar",
      claim_confidence: "high",
    }),
  ]);
});

test("Vaivada publishes Naujienos as last documented civilian employer and keeps CIC separate", async ({ request }) => {
  const person = await publicPerson(request, "bfc6beb7-301b-5682-987f-da0eac235d2c", "Anthony S Vaivada");
  expect(person).toMatchObject({
    identity_status: "high_confidence",
    research_status: "verified_employer_found",
    personnel_category: "commissioned_army_officer",
    commissioned_officer: true,
  });
  expect(person.last_civilian_pre_service).toEqual([
    expect.objectContaining({
      canonical_organization: "Naujienos (The Lithuanian Daily News)",
      role_title: "city editor",
      relationship_type: "employment",
      temporal_basis: "probable_immediate",
      claim_confidence: "high",
    }),
  ]);
  expect(person.other_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      canonical_organization: "United States Army Counter Intelligence Corps",
      relationship_type: "military_assignment",
      temporal_basis: "temporal_relation_uncertain",
    }),
  ]);
});

test("Vaivananda, Vakakas and Valakis publish wartime identity evidence without invented employers", async ({ request }) => {
  const vaivananda = await publicPerson(request, "fdcccd3f-98b3-565d-a3ba-eaad1b1dc784", "Vichien Vaivananda");
  expect(vaivananda.name_variants).toContain("Wichian Waiwanon");
  expect(vaivananda.last_civilian_pre_service).toHaveLength(0);
  expect(vaivananda.other_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      canonical_organization: "Free Thai Society",
      relationship_type: "military_assignment",
      temporal_basis: "temporal_relation_uncertain",
    }),
  ]);

  const vakakas = await publicPerson(request, "5f7f6bb9-09ce-5fc0-9163-be180cb21bb8", "Sotirios G Vakakas");
  expect(vakakas).toMatchObject({
    identity_status: "confirmed",
    research_status: "requires_archival_review",
    personnel_category: "enlisted_army_personnel",
    commissioned_officer: false,
  });
  expect(vakakas.last_civilian_pre_service).toHaveLength(0);
  expect(vakakas.other_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      canonical_organization: "OSS Greek Operational Group",
      relationship_type: "military_assignment",
      claim_confidence: "confirmed",
    }),
  ]);

  const valakis = await publicPerson(request, "57ef22b9-66d9-56c7-99f8-133c3ce7d06a", "Apollon P Valakis");
  expect(valakis.last_civilian_pre_service).toHaveLength(0);
  expect(valakis.other_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      canonical_organization: "Office of Strategic Services",
      relationship_type: "government_assignment",
      temporal_basis: "temporal_relation_uncertain",
    }),
  ]);
  expect(JSON.stringify(valakis.other_pre_oss_affiliations)).not.toContain("Northeastern");
  expect(JSON.stringify(valakis.other_pre_oss_affiliations)).not.toContain("Boston University");
});

test("Batch 976 evidence excludes secrets, full identifiers and raw bulk records", () => {
  expect(evidence).not.toMatch(/"serial_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toMatch(/"service_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toContain("NARA_API_KEY");
  expect(evidence).not.toContain("x-api-key");
  expect(evidence).not.toContain("candidate_identifier");
  expect(evidence).not.toContain("bulk_record_ordinal");
  expect(evidence).not.toMatch(/RA\d{8}/);
});

test("Batch 976 publishes exact coverage counters and preserves oil counts", async ({ request, page }) => {
  const response = await request.get("./data/stats.json");
  expect(response.ok()).toBeTruthy();
  expect(await response.json()).toMatchObject({
    source_rows: 23_978,
    person_entities: 23_936,
    possible_duplicate_groups: 665,
    research_attempted_people: 15_383,
    verified_affiliation_people: 1_108,
    verified_employer_people: 497,
    archival_review_assessed_people: 13_859,
    published_claims: 9_772,
    public_sources: 6_318,
  });
  await page.goto("./oil-companies/");
  const main = page.locator("main");
  await expect(main).toContainText("14 people");
  await expect(main).toContainText("15 historically named");
});
