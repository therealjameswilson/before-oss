import fs from "node:fs";
import { expect, test } from "@playwright/test";
import type { APIRequestContext } from "@playwright/test";

const evidence = fs.readFileSync(
  new URL(
    "../../research/evidence-page481-spyridon-s-varthis-to-lena-b-veazey-review_batch-982_2026-10-30.json",
    import.meta.url,
  ),
  "utf8",
);

const profiles = [
  ["36517755-54ec-50f6-afae-502c414c2754", "Spyridon S Varthis"],
  ["37d602c5-4b19-5eb8-94fd-106d6e6dd4c7", "John A Vasdekis"],
  ["2885f9a0-0523-5b02-b09d-5b509ea2fbe8", "John M Vasicak"],
  ["7783cf92-1a1e-5a60-a18d-e2d540e7c82a", "Helen Vasiliou"],
  ["e8daa0a0-a427-5118-87da-9c7220cdf61b", "Joseph F Vasko"],
  ["4c33016a-9513-5a16-9055-68fea1dd99a3", "Philip N Vassil"],
  ["78d5a8f0-936f-54d0-87c1-a0491d72eb76", "Steve Vassiliades"],
  ["bd395aaa-5af1-51d0-aaa6-14cb8e528862", "John Vassos"],
  ["3c644922-ab30-5b95-ad91-b7707aa47937", "James H Vater"],
  ["e84e9bd0-adcd-5f91-9818-1fb3ef3c5a97", "Anastassios T Vatis"],
  ["abc57901-1182-5327-8f14-1b344d4178e3", "Joan M Vatsek"],
  ["a9f02ad8-652e-5fae-941e-9d644d20a575", "Philip Vaudrin"],
  ["93ede38e-9f89-500e-9106-defc6c205efa", "James Vaughan Jr."],
  ["2ba6c6c1-029f-57b6-aaeb-83e35e4b252d", "Grady W Vaughn"],
  ["42952bdd-a460-590f-8d0d-7250f9adbf5c", "James K Vaughn"],
  ["babd50c3-6b7d-5404-bbff-837ea829f1a0", "James B Vaughn"],
  ["4649c0a2-1f81-584d-ba7b-8f2d5ea92bc3", "John J Vaughn"],
  ["e7bba9bc-f72e-55ff-9d5b-f7f362845544", "Richard B Vaughn"],
  ["7a43241e-66da-55e3-8f1a-99549733b28d", "William L Vaughn"],
  ["16c1a5d0-6a50-5979-a48a-ea254489b749", "Jean Vauzelle"],
  ["a61d9e12-ec43-595f-8ef6-b1191764f80d", "Salvatore Vavala"],
  ["9df06569-d14b-5318-bcec-b9f35893a9d0", "Alberto Vazquez"],
  ["f95e3869-4cb3-5121-8977-b8b915deff46", "Lena B Veazey"],
] as const;

async function publicPerson(request: APIRequestContext, id: string, name: string) {
  const first = name[0].toLowerCase();
  const shard = /^[a-z]$/.test(first) ? first : "other";
  const response = await request.get(`./data/people/${shard}.json`);
  expect(response.ok()).toBeTruthy();
  return (await response.json()).find((item: { person_id: string }) => item.person_id === id);
}

test("Batch 982 publishes all 23 audited people with terminal outcomes", async ({ page }) => {
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

test("five Army bridges publish qualified occupation categories, never employers", async ({ request }) => {
  const expected = [
    ["36517755-54ec-50f6-afae-502c414c2754", "Spyridon S Varthis", "ship captain, mate, pilot, or engineer"],
    ["e8daa0a0-a427-5118-87da-9c7220cdf61b", "Joseph F Vasko", "semiskilled automobile-manufacturing occupation, not elsewhere classified"],
    ["3c644922-ab30-5b95-ad91-b7707aa47937", "James H Vater", "stenographer or typist"],
    ["e84e9bd0-adcd-5f91-9818-1fb3ef3c5a97", "Anastassios T Vatis", "semiprofessional occupation, not elsewhere classified"],
    ["a61d9e12-ec43-595f-8ef6-b1191764f80d", "Salvatore Vavala", "unskilled machine-shop or related occupation, not elsewhere classified"],
  ] as const;
  for (const [id, name, occupation] of expected) {
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
        relationship_type: "unknown",
        temporal_basis: "strongly_date_bounded",
        claim_confidence: "medium",
        publication_status: "publish_qualified",
      }),
    ]);
  }
});

test("Vassos separates RCA employment from wartime Army service", async ({ request }) => {
  const person = await publicPerson(request, "bd395aaa-5af1-51d0-aaa6-14cb8e528862", "John Vassos");
  expect(person).toMatchObject({
    identity_status: "high_confidence",
    research_status: "verified_employer_found",
    personnel_category: "commissioned_army_officer",
    commissioned_officer: true,
  });
  expect(person.immediate_pre_oss_affiliations).toHaveLength(0);
  expect(person.last_civilian_pre_service).toEqual([
    expect.objectContaining({
      canonical_organization: "Radio Corporation of America",
      organization_name_as_found: "RCA Victor Division",
      role_title: "consultant designer",
      occupation: "industrial designer",
      relationship_type: "employment",
      start_date: "1934",
      end_date: "1942",
      claim_confidence: "high",
    }),
  ]);
  expect(person.other_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      canonical_organization: "United States Army Corps of Engineers",
      organization_name_as_found: "Army Engineering Corps",
      relationship_type: "military_assignment",
      temporal_basis: "temporal_relation_uncertain",
    }),
  ]);
});

test("Vassil publishes Signal Corps service without inventing a civilian employer", async ({ request }) => {
  const person = await publicPerson(request, "4c33016a-9513-5a16-9055-68fea1dd99a3", "Philip N Vassil");
  expect(person).toMatchObject({
    identity_status: "high_confidence",
    research_status: "requires_archival_review",
    personnel_category: "commissioned_army_officer",
    commissioned_officer: true,
  });
  expect(person.immediate_pre_oss_affiliations).toHaveLength(0);
  expect(person.last_civilian_pre_service).toHaveLength(0);
  expect(person.other_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      canonical_organization: "United States Army Signal Corps",
      organization_name_as_found: "Army Signal Corps",
      role_title: "captain",
      relationship_type: "military_assignment",
      temporal_basis: "temporal_relation_uncertain",
      claim_confidence: "high",
    }),
  ]);
});

test("Vaudrin remains a qualified probable prewar employment finding", async ({ request }) => {
  const person = await publicPerson(request, "a9f02ad8-652e-5fae-941e-9d644d20a575", "Philip Vaudrin");
  expect(person).toMatchObject({
    identity_status: "probable",
    research_status: "documented_prewar_employer_found",
    personnel_category: "unknown_or_indeterminate",
  });
  expect(person.immediate_pre_oss_affiliations).toHaveLength(0);
  expect(person.last_civilian_pre_service).toHaveLength(0);
  expect(person.other_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      canonical_organization: "Oxford University Press",
      role_title: "editor",
      relationship_type: "employment",
      temporal_basis: "documented_prewar",
      identity_confidence: "probable",
      claim_confidence: "medium",
      publication_status: "publish_qualified",
    }),
  ]);
});

test("the 15 unbridged people remain affiliation-free archival-review cases", async ({ request }) => {
  for (const [id, name] of profiles.filter(([, name]) => ![
    "Spyridon S Varthis", "Joseph F Vasko", "Philip N Vassil", "John Vassos",
    "James H Vater", "Anastassios T Vatis", "Philip Vaudrin", "Salvatore Vavala",
  ].includes(name))) {
    const person = await publicPerson(request, id, name);
    expect(person).toMatchObject({
      identity_status: "unresolved",
      research_status: "requires_archival_review",
    });
    expect(person.immediate_pre_oss_affiliations).toHaveLength(0);
    expect(person.last_civilian_pre_service).toHaveLength(0);
    expect(person.other_pre_oss_affiliations).toHaveLength(0);
  }
});

test("Batch 982 evidence excludes secrets, full identifiers and raw bulk records", () => {
  expect(evidence).not.toMatch(/"serial_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toMatch(/"service_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toContain("NARA_API_KEY");
  expect(evidence).not.toContain("x-api-key");
  expect(evidence).not.toContain("candidate_identifier");
  expect(evidence).not.toContain("bulk_record_ordinal");
  expect(evidence).not.toMatch(/RA\d{8}/);
});

test("Batch 982 publishes exact coverage counters and preserves oil counts", async ({ request, page }) => {
  const response = await request.get("./data/stats.json");
  expect(response.ok()).toBeTruthy();
  expect(await response.json()).toMatchObject({
    source_rows: 23_978,
    person_entities: 23_936,
    possible_duplicate_groups: 668,
    research_attempted_people: 15_521,
    verified_affiliation_people: 1_119,
    verified_employer_people: 504,
    archival_review_assessed_people: 13_997,
    published_claims: 9_874,
    public_sources: 6_385,
  });
  await page.goto("./oil-companies/");
  const main = page.locator("main");
  await expect(main).toContainText("14 people");
  await expect(main).toContainText("15 historically named");
});
