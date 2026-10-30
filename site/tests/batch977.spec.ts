import fs from "node:fs";
import { expect, test } from "@playwright/test";
import type { APIRequestContext } from "@playwright/test";

const evidence = fs.readFileSync(
  new URL(
    "../../research/evidence-page479-melchiore-valeriano-to-william-van-cleef-review_batch-977_2026-10-30.json",
    import.meta.url,
  ),
  "utf8",
);

const profiles = [
  ["95a691b7-d95f-5e6f-a737-2aa82f15476e", "Melchiore Valeriano"],
  ["f96fa4a8-3df9-533f-a15f-f2cc2ed13a42", "Helen Valerius"],
  ["ac44646e-5c94-5090-92b3-8da69e883761", "Neal A Valiant"],
  ["b6ac172d-0919-5286-9637-2d6510182f02", "Edgar M Valk"],
  ["ba07fe40-ff1e-5c41-9a6f-a2657abc04c6", "Dale E Vallance"],
  ["03474dc7-0d37-5866-8c6d-a09f7134b64b", "Jean Vallery"],
  ["d469ff8c-4692-5809-befe-c96f9057693b", "Armand I Vallieres"],
  ["cc2ab2ea-3666-5a30-bd9d-6ed30780161e", "Serban Vallimarescu"],
  ["e8c77f21-eceb-562a-872b-06fa0bc02bca", "A Valusis"],
  ["9f2f9334-22dd-54e6-bb2b-402a9369480f", "Marcos Valvis"],
  ["88b9fdac-9570-56a0-887e-693dfc275d6f", "William L Van Alen"],
  ["0598817d-ded2-53ba-a6d1-c70edba42a6c", "Greta Van Antwerp"],
  ["3e9f09d0-2a84-505f-ae59-60b1ae8dd865", "Gerhard P Van Arkel"],
  ["0ecf5a46-6eab-5031-9a99-91762e876b8e", "Ruth B Van Arkel"],
  ["160528a9-bcfb-5d1c-9245-f13b211a484b", "Albert H Van Arsdale"],
  ["d63972d5-780e-5713-acb9-ba6f80f56d1f", "Douglas W Van Arsdale"],
  ["56e73541-eae0-539c-8d04-9d72435da777", "Charles J Van Bergen"],
  ["70551449-2677-5354-a80d-54f9453361f9", "Archbold Van Beuren"],
  ["1bf6cea5-af41-5643-99f0-b10932a33e0e", "Micheline Van Biesbroec"],
  ["4b330868-c4c6-5535-904a-1ba64479343a", "Cornelius C Van Boecop"],
  ["d09fe90c-ed61-5f4f-b0ca-6c41689f5b63", "Frank Van Brunt"],
  ["baad67f6-7232-5fcd-8074-dd069c5119e5", "Delbert E Van Camplear"],
  ["a1f63a96-6d2f-53c0-8a5e-ded8307cd190", "William R Van Cleef"],
] as const;

async function publicPerson(request: APIRequestContext, id: string, name: string) {
  const response = await request.get(`./data/people/${name[0].toLowerCase()}.json`);
  expect(response.ok()).toBeTruthy();
  return (await response.json()).find((item: { person_id: string }) => item.person_id === id);
}

test("Batch 977 publishes all 23 audited people with terminal outcomes", async ({ page }) => {
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

test("four protected Army matches publish dated categories, never employers", async ({ request }) => {
  const expected = [
    ["ac44646e-5c94-5090-92b3-8da69e883761", "Neal A Valiant", "transportation worker, not elsewhere classified", "unknown"],
    ["d469ff8c-4692-5809-befe-c96f9057693b", "Armand I Vallieres", "student", "student"],
    ["9f2f9334-22dd-54e6-bb2b-402a9369480f", "Marcos Valvis", "chauffeur or driver", "unknown"],
    ["d09fe90c-ed61-5f4f-b0ca-6c41689f5b63", "Frank Van Brunt", "technician, except laboratory", "unknown"],
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

test("Vallimarescu keeps Harvard student status and Army service separate from employment", async ({ request }) => {
  const person = await publicPerson(request, "cc2ab2ea-3666-5a30-bd9d-6ed30780161e", "Serban Vallimarescu");
  expect(person).toMatchObject({
    identity_status: "high_confidence",
    research_status: "occupation_only_found",
    personnel_category: "commissioned_army_officer",
    commissioned_officer: true,
  });
  expect(person.immediate_pre_oss_affiliations).toHaveLength(0);
  expect(person.last_civilian_pre_service).toHaveLength(0);
  expect(person.other_pre_oss_affiliations).toEqual(expect.arrayContaining([
    expect.objectContaining({
      canonical_organization: "Harvard University",
      relationship_type: "student",
      temporal_basis: "strongly_date_bounded",
      claim_confidence: "high",
    }),
    expect.objectContaining({
      canonical_organization: "United States Army",
      relationship_type: "military_assignment",
      temporal_basis: "temporal_relation_uncertain",
      claim_confidence: "high",
    }),
  ]));
});

test("Van Beuren publishes Cue as professional affiliation, not an employer", async ({ request }) => {
  const person = await publicPerson(request, "70551449-2677-5354-a80d-54f9453361f9", "Archbold Van Beuren");
  expect(person).toMatchObject({
    identity_status: "high_confidence",
    research_status: "completed",
    personnel_category: "civilian_professional_or_administrative_grade",
    commissioned_officer: false,
  });
  expect(person.immediate_pre_oss_affiliations).toHaveLength(0);
  expect(person.last_civilian_pre_service).toHaveLength(0);
  expect(person.other_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      canonical_organization: "Cue magazine",
      relationship_type: "professional_affiliation",
      temporal_basis: "documented_prewar",
      claim_confidence: "high",
    }),
  ]);
});

test("Van Biesbroec remains probable with qualified student evidence", async ({ request }) => {
  const person = await publicPerson(request, "1bf6cea5-af41-5643-99f0-b10932a33e0e", "Micheline Van Biesbroec");
  expect(person).toMatchObject({
    identity_status: "probable",
    research_status: "requires_archival_review",
    personnel_category: "unknown_or_indeterminate",
  });
  expect(person.name_variants).toContain("Micheline Van Biesbroeck");
  expect(person.last_civilian_pre_service).toHaveLength(0);
  expect(person.other_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      organization_name_as_found: "Williams Bay High School",
      relationship_type: "student",
      temporal_basis: "documented_prewar",
      claim_confidence: "medium",
      publication_status: "publish_qualified",
    }),
  ]);
});

test("same-name William R Van Cleef rows stay separate and visibly grouped", async ({ request }) => {
  const first = await publicPerson(request, "a1f63a96-6d2f-53c0-8a5e-ded8307cd190", "William R Van Cleef");
  const second = await publicPerson(request, "9db44dbe-b1b5-5303-8d36-819031afc12c", "William R Van Cleef");
  expect(first.person_id).not.toBe(second.person_id);
  expect(first.possible_duplicate_group).toBeTruthy();
  expect(first.possible_duplicate_group).toBe(second.possible_duplicate_group);
  expect(first.research_status).toBe("requires_archival_review");
  expect(second.research_status).toBe("not_started");
});

test("unbridged prominent namesakes publish no affiliation", async ({ request }) => {
  for (const [id, name] of [
    ["88b9fdac-9570-56a0-887e-693dfc275d6f", "William L Van Alen"],
    ["4b330868-c4c6-5535-904a-1ba64479343a", "Cornelius C Van Boecop"],
  ] as const) {
    const person = await publicPerson(request, id, name);
    expect(person.identity_status).toBe("ambiguous");
    expect(person.immediate_pre_oss_affiliations).toHaveLength(0);
    expect(person.last_civilian_pre_service).toHaveLength(0);
    expect(person.other_pre_oss_affiliations).toHaveLength(0);
  }
});

test("Batch 977 evidence excludes secrets, full identifiers and raw bulk records", () => {
  expect(evidence).not.toMatch(/"serial_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toMatch(/"service_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toContain("NARA_API_KEY");
  expect(evidence).not.toContain("x-api-key");
  expect(evidence).not.toContain("candidate_identifier");
  expect(evidence).not.toContain("bulk_record_ordinal");
  expect(evidence).not.toMatch(/RA\d{8}/);
});

test("Batch 977 publishes exact coverage counters and preserves oil counts", async ({ request, page }) => {
  const response = await request.get("./data/stats.json");
  expect(response.ok()).toBeTruthy();
  expect(await response.json()).toMatchObject({
    source_rows: 23_978,
    person_entities: 23_936,
    possible_duplicate_groups: 666,
    research_attempted_people: 15_406,
    verified_affiliation_people: 1_110,
    verified_employer_people: 497,
    archival_review_assessed_people: 13_882,
    published_claims: 9_787,
    public_sources: 6_328,
  });
  await page.goto("./oil-companies/");
  const main = page.locator("main");
  await expect(main).toContainText("14 people");
  await expect(main).toContainText("15 historically named");
});
