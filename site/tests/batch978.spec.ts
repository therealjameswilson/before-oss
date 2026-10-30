import fs from "node:fs";
import { expect, test } from "@playwright/test";
import type { APIRequestContext } from "@playwright/test";

const evidence = fs.readFileSync(
  new URL(
    "../../research/evidence-page479-william-van-cleef-to-samuel-van-hyning-review_batch-978_2026-10-30.json",
    import.meta.url,
  ),
  "utf8",
);

const profiles = [
  ["9db44dbe-b1b5-5303-8d36-819031afc12c", "William R Van Cleef"],
  ["5a9235b3-8018-5c0a-8c72-52b790897b30", "Richard L Van Cleve"],
  ["82f89e15-2a94-5280-950e-0d0cc1bba43b", "Thomas C Van Cleve"],
  ["c445350f-04b1-50b8-b933-061d5b0e9807", "John Van Costen"],
  ["2cf892b1-527f-5d01-bcf2-7dc1931e0668", "Albert Van Dam"],
  ["98b21a2b-b6c9-5690-8c1c-250795ae0239", "Cecil Van Den Beldt"],
  ["b71ef978-46c4-5d13-b5e7-f9f91cec2e80", "Ides Van Der Grac"],
  ["888a34d4-9b1b-5ae1-bbe2-a56fb00b2582", "George T Van Der Hoef"],
  ["263ae5be-4956-56c8-aa00-8e8e1d57d7af", "Paul R Van DerStricht"],
  ["2fa57046-ac09-5f66-b172-bd1fe428859f", "Jan W Van Driel"],
  ["d31820a7-1c8f-5514-9f78-b58cdb7481f9", "John Van Duyne"],
  ["08691531-2228-529b-84e3-28415a47daf7", "Emile J Van Dyck"],
  ["97efd8f9-be4d-5614-b6c0-e0e68fed0bca", "Margi Van Ende"],
  ["7c9f011a-69e4-58de-8abd-c6f49c9a350a", "Marcel Van Essen"],
  ["d59ad61c-a247-53c3-9863-40253350adeb", "Andrew E Van Esso"],
  ["f194594e-ee92-591a-a669-cb4771566bdf", "William Van Ewijk"],
  ["7d6043d3-e6f6-511b-ba65-42b2dfc26ca2", "Stephen C Van Fleet"],
  ["933aa9c0-d0c1-550d-8a5f-190564980b7d", "Edwin H Van Gessel"],
  ["6d1db677-9282-5e5a-b534-59c5ac87c3f5", "John T Van Hart"],
  ["c242b464-4491-5e4e-b271-fe81aeab10e5", "Alice Van Hoesen"],
  ["b96f8c23-e90e-5258-b800-893834cc9c23", "Florence Van Horn"],
  ["cd36567d-8292-5dc0-b15f-4d989bcc5028", "Charles H Van Houten"],
  ["3c7e94ee-2f09-553f-a9c6-05b77733a781", "Samuel Van Hyning"],
] as const;

async function publicPerson(request: APIRequestContext, id: string, name: string) {
  const response = await request.get(`./data/people/${name[0].toLowerCase()}.json`);
  expect(response.ok()).toBeTruthy();
  return (await response.json()).find((item: { person_id: string }) => item.person_id === id);
}

test("Batch 978 publishes all 23 audited people with terminal outcomes", async ({ page }) => {
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

test("Van Cleve publishes Bowdoin as last civilian employer, not an explicit OSS predecessor", async ({ request }) => {
  const person = await publicPerson(request, "82f89e15-2a94-5280-950e-0d0cc1bba43b", "Thomas C Van Cleve");
  expect(person).toMatchObject({
    identity_status: "high_confidence",
    research_status: "verified_employer_found",
    personnel_category: "commissioned_army_officer",
    commissioned_officer: true,
  });
  expect(person.immediate_pre_oss_affiliations).toHaveLength(0);
  expect(person.last_civilian_pre_service).toEqual([
    expect.objectContaining({
      canonical_organization: "Bowdoin College",
      role_title: "professor of history and political science",
      relationship_type: "employment",
      temporal_basis: "probable_immediate",
      claim_confidence: "high",
    }),
  ]);
});

test("Van Der Grac keeps military pathway, last civilian practice and earlier employment separate", async ({ request }) => {
  const person = await publicPerson(request, "b71ef978-46c4-5d13-b5e7-f9f91cec2e80", "Ides Van Der Grac");
  expect(person).toMatchObject({
    identity_status: "high_confidence",
    research_status: "verified_employer_found",
    personnel_category: "commissioned_army_officer",
    commissioned_officer: true,
  });
  expect(person.immediate_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      canonical_organization: "345th Bombardment Squadron, United States Army Air Forces",
      role_title: "intelligence officer",
      relationship_type: "military_assignment",
      temporal_basis: "probable_immediate",
      claim_confidence: "high",
    }),
  ]);
  expect(person.last_civilian_pre_service).toEqual([
    expect.objectContaining({
      canonical_organization: "Ides van der Gracht and Walter H. Kilham Jr., Architects",
      role_title: "architect and partner",
      relationship_type: "self_employment",
      temporal_basis: "strongly_date_bounded",
      claim_confidence: "high",
    }),
  ]);
  expect(person.other_pre_oss_affiliations).toEqual(expect.arrayContaining([
    expect.objectContaining({
      canonical_organization: "Delano & Aldrich",
      relationship_type: "employment",
      temporal_basis: "documented_prewar",
      claim_confidence: "high",
    }),
  ]));
});

test("Van DerStricht publishes a confirmed attorney occupation without inventing a firm", async ({ request }) => {
  const person = await publicPerson(request, "263ae5be-4956-56c8-aa00-8e8e1d57d7af", "Paul R Van DerStricht");
  expect(person).toMatchObject({
    identity_status: "confirmed",
    research_status: "occupation_only_found",
    personnel_category: "commissioned_army_officer",
    commissioned_officer: true,
  });
  expect(person.immediate_pre_oss_affiliations).toHaveLength(0);
  expect(person.last_civilian_pre_service).toHaveLength(0);
  expect(person.other_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      canonical_organization: null,
      occupation: "attorney",
      relationship_type: "unknown",
      temporal_basis: "probable_immediate",
      claim_confidence: "medium",
      publication_status: "publish_qualified",
    }),
  ]);
});

test("Van DerStricht spelling variants stay separate and visibly grouped", async ({ request }) => {
  const first = await publicPerson(request, "263ae5be-4956-56c8-aa00-8e8e1d57d7af", "Paul R Van DerStricht");
  const second = await publicPerson(request, "a1146a1f-3102-5b31-8565-c93ccc980831", "Paul VanDenstricht");
  expect(first.person_id).not.toBe(second.person_id);
  expect(first.possible_duplicate_group).toBeTruthy();
  expect(first.possible_duplicate_group).toBe(second.possible_duplicate_group);
  expect(first.research_status).toBe("occupation_only_found");
  expect(second.research_status).toBe("not_started");
});

test("official Army identity bridges publish occupations, never employers", async ({ request }) => {
  const expected = [
    ["2cf892b1-527f-5d01-bcf2-7dc1931e0668", "Albert Van Dam", "jeweler, watchmaker, goldsmith, or silversmith"],
    ["6d1db677-9282-5e5a-b534-59c5ac87c3f5", "John T Van Hart", "shipping or receiving clerk"],
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
    expect(person.other_pre_oss_affiliations).toEqual(expect.arrayContaining([
      expect.objectContaining({
        canonical_organization: null,
        occupation,
        relationship_type: "unknown",
        temporal_basis: "strongly_date_bounded",
        claim_confidence: "medium",
      }),
    ]));
  }
});

test("SOE file identities do not create unsupported employers", async ({ request }) => {
  for (const [id, name] of [
    ["2fa57046-ac09-5f66-b172-bd1fe428859f", "Jan W Van Driel"],
    ["08691531-2228-529b-84e3-28415a47daf7", "Emile J Van Dyck"],
    ["7c9f011a-69e4-58de-8abd-c6f49c9a350a", "Marcel Van Essen"],
  ] as const) {
    const person = await publicPerson(request, id, name);
    expect(person.identity_status).toBe("high_confidence");
    expect(person.research_status).toBe("requires_archival_review");
    expect(person.immediate_pre_oss_affiliations).toHaveLength(0);
    expect(person.last_civilian_pre_service).toHaveLength(0);
    expect(person.other_pre_oss_affiliations).toHaveLength(0);
  }
});

test("qualified and rejected namesake leads remain visibly uncertain", async ({ request }) => {
  const vanEsso = await publicPerson(request, "d59ad61c-a247-53c3-9863-40253350adeb", "Andrew E Van Esso");
  expect(vanEsso.identity_status).toBe("probable");
  expect(vanEsso.research_status).toBe("requires_archival_review");
  expect(vanEsso.other_pre_oss_affiliations).toHaveLength(0);

  const vanDenBeldt = await publicPerson(request, "98b21a2b-b6c9-5690-8c1c-250795ae0239", "Cecil Van Den Beldt");
  expect(vanDenBeldt.identity_status).toBe("ambiguous");
  expect(vanDenBeldt.immediate_pre_oss_affiliations).toHaveLength(0);
  expect(vanDenBeldt.last_civilian_pre_service).toHaveLength(0);
  expect(vanDenBeldt.other_pre_oss_affiliations).toHaveLength(0);
});

test("Van Hyning publishes COI as professional affiliation, not employment", async ({ request }) => {
  const person = await publicPerson(request, "3c7e94ee-2f09-553f-a9c6-05b77733a781", "Samuel Van Hyning");
  expect(person).toMatchObject({
    identity_status: "high_confidence",
    research_status: "requires_archival_review",
    personnel_category: "civilian_professional_or_administrative_grade",
    commissioned_officer: false,
  });
  expect(person.immediate_pre_oss_affiliations).toHaveLength(0);
  expect(person.last_civilian_pre_service).toHaveLength(0);
  expect(person.other_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      canonical_organization: "Coordinator of Information",
      relationship_type: "professional_affiliation",
      temporal_basis: "documented_prewar",
      claim_confidence: "high",
    }),
  ]);
});

test("Batch 978 evidence excludes secrets, full identifiers and raw bulk records", () => {
  expect(evidence).not.toMatch(/"serial_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toMatch(/"service_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toContain("NARA_API_KEY");
  expect(evidence).not.toContain("x-api-key");
  expect(evidence).not.toContain("candidate_identifier");
  expect(evidence).not.toContain("bulk_record_ordinal");
  expect(evidence).not.toMatch(/RA\d{8}/);
});

test("Batch 978 publishes exact coverage counters and preserves oil counts", async ({ request, page }) => {
  const response = await request.get("./data/stats.json");
  expect(response.ok()).toBeTruthy();
  expect(await response.json()).toMatchObject({
    source_rows: 23_978,
    person_entities: 23_936,
    possible_duplicate_groups: 667,
    research_attempted_people: 15_429,
    verified_affiliation_people: 1_113,
    verified_employer_people: 499,
    archival_review_assessed_people: 13_905,
    published_claims: 9_805,
    public_sources: 6_345,
  });
  await page.goto("./oil-companies/");
  const main = page.locator("main");
  await expect(main).toContainText("14 people");
  await expect(main).toContainText("15 historically named");
});
