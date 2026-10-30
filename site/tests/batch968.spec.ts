import fs from "node:fs";
import { expect, test } from "@playwright/test";
import type { APIRequestContext } from "@playwright/test";

const evidence = fs.readFileSync(
  new URL(
    "../../research/evidence-page474-michalis-tsirmulas-to-margaret-tugas-review_batch-968_2026-10-30.json",
    import.meta.url,
  ),
  "utf8",
);

const profiles = [
  ["2a3e1fd8-a46d-553e-aa39-0ae740bdf7b6", "Michalis Tsirmulas"],
  ["e6c5814a-672a-5bac-ae39-2a26838efc57", "Tsun O Tso"],
  ["b292cf8c-e222-5691-af95-d8b9611a1804", "George T Tsohonis"],
  ["b26df1e4-6235-529e-a944-eb433fac14da", "James Tsolas"],
  ["1a007dc6-b269-5628-b725-877372b6a93d", "John E Tsouderos"],
  ["c1d3dce5-ca55-5fab-b00b-48b340b5691e", "Henry J Tsurutani"],
  ["7a7cc39d-f5f6-5acd-bac5-0a09bacd19e1", "Frances M Tuchscher"],
  ["7b279230-6292-529c-9480-87e12a7c69a1", "Emily Tuck"],
  ["5fe05290-6b8b-5b6a-84f7-049e0b5c627a", "G L Tucker"],
  ["bcb3f46a-5f2f-5770-9a73-250b2c1a855f", "Gertrude G Tucker"],
  ["f494ab67-5719-579c-8e05-3127319d62f9", "Isota A Tucker"],
  ["c1f47b06-84b9-5924-9e22-6b55c72bd8b0", "James R Tucker"],
  ["1783f52f-a39e-5f77-b1e5-7f0b882b5bb8", "Lula E Tucker"],
  ["d3a34ac7-43ac-5275-ae27-cb95fc84324d", "Robert C Tucker"],
  ["96fb3fa0-c6cf-5e8b-b7fb-84ae878c8326", "Robert W Tucker"],
  ["7d27b4fb-6450-5bc4-a3e5-81821aacccf2", "Roger S Tucker"],
  ["5de20758-c6bd-5ac2-9599-9ad015af799f", "William R Tucker"],
  ["a9947f65-e455-5916-b23c-22b3d93f9c1f", "Laura W Tuckerman"],
  ["4139f4b9-2858-53d7-8ec5-de13855ba5ae", "Margaret C Tuckerman"],
  ["f9bd1785-ba59-57e9-b1c0-30854e721f7b", "Bert A Tueling"],
  ["23f36d5e-436d-59f4-80d7-c784630bad71", "Lois R Tufts"],
  ["13d4e94d-069e-59ae-9c82-148c1d872244", "Robert W Tufts"],
  ["fe30d53d-9014-56f2-8470-bf66465c91d4", "Margaret E Tugas"],
] as const;

const occupationProfiles = [
  ["2a3e1fd8-a46d-553e-aa39-0ae740bdf7b6", "Michalis Tsirmulas", "confirmed", "waiter", "unknown"],
  ["b292cf8c-e222-5691-af95-d8b9611a1804", "George T Tsohonis", "high_confidence", "salesman or sales agent", "unknown"],
  ["b26df1e4-6235-529e-a944-eb433fac14da", "James Tsolas", "high_confidence", "waiter", "unknown"],
  ["c1f47b06-84b9-5924-9e22-6b55c72bd8b0", "James R Tucker", "high_confidence", "fireman other than a process fireman", "unknown"],
  ["7d27b4fb-6450-5bc4-a3e5-81821aacccf2", "Roger S Tucker", "high_confidence", "stenographer or typist", "unknown"],
  ["5de20758-c6bd-5ac2-9599-9ad015af799f", "William R Tucker", "high_confidence", "student", "student"],
  ["13d4e94d-069e-59ae-9c82-148c1d872244", "Robert W Tufts", "high_confidence", "professional occupation, not elsewhere classified", "unknown"],
] as const;

const unresolvedProfiles = [
  ["e6c5814a-672a-5bac-ae39-2a26838efc57", "Tsun O Tso"],
  ["7a7cc39d-f5f6-5acd-bac5-0a09bacd19e1", "Frances M Tuchscher"],
  ["7b279230-6292-529c-9480-87e12a7c69a1", "Emily Tuck"],
  ["5fe05290-6b8b-5b6a-84f7-049e0b5c627a", "G L Tucker"],
  ["bcb3f46a-5f2f-5770-9a73-250b2c1a855f", "Gertrude G Tucker"],
  ["f494ab67-5719-579c-8e05-3127319d62f9", "Isota A Tucker"],
  ["1783f52f-a39e-5f77-b1e5-7f0b882b5bb8", "Lula E Tucker"],
  ["96fb3fa0-c6cf-5e8b-b7fb-84ae878c8326", "Robert W Tucker"],
  ["4139f4b9-2858-53d7-8ec5-de13855ba5ae", "Margaret C Tuckerman"],
  ["f9bd1785-ba59-57e9-b1c0-30854e721f7b", "Bert A Tueling"],
  ["23f36d5e-436d-59f4-80d7-c784630bad71", "Lois R Tufts"],
  ["fe30d53d-9014-56f2-8470-bf66465c91d4", "Margaret E Tugas"],
] as const;

async function publicPerson(request: APIRequestContext, id: string, name: string) {
  const response = await request.get(`./data/people/${name[0].toLowerCase()}.json`);
  expect(response.ok()).toBeTruthy();
  return (await response.json()).find((item: { person_id: string }) => item.person_id === id);
}

test("Batch 968 publishes all 23 audited people with terminal outcomes", async ({ page }) => {
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

test("seven Army categories remain qualified statuses without fabricated employers", async ({ request }) => {
  for (const [id, name, identity, occupation, relationship] of occupationProfiles) {
    const person = await publicPerson(request, id, name);
    expect(person).toMatchObject({
      identity_status: identity,
      personnel_category: "enlisted_army_personnel",
      commissioned_officer: false,
      research_status: "occupation_only_found",
    });
    expect(person.immediate_pre_oss_affiliations).toHaveLength(0);
    expect(person.last_civilian_pre_service).toHaveLength(0);
    expect(person.other_pre_oss_affiliations).toEqual(expect.arrayContaining([
      expect.objectContaining({
        canonical_organization: null,
        occupation,
        relationship_type: relationship,
        temporal_basis: "strongly_date_bounded",
        claim_confidence: "medium",
      }),
    ]));
  }
});

test("Michalis Tsirmulas and James Tsolas retain identity variants and OSS context", async ({ request }) => {
  const tsirmulas = await publicPerson(request, "2a3e1fd8-a46d-553e-aa39-0ae740bdf7b6", "Michalis Tsirmulas");
  expect(tsirmulas.name_variants).toEqual(expect.arrayContaining(["Teirmulas Michalis"]));
  expect(tsirmulas.claims).toEqual(expect.arrayContaining([
    expect.objectContaining({ claim_type: "identity", claim_confidence: "confirmed" }),
  ]));

  const tsolas = await publicPerson(request, "b26df1e4-6235-529e-a944-eb433fac14da", "James Tsolas");
  expect(tsolas.name_variants).toEqual(expect.arrayContaining(["James A Tsolas", "Tbola James"]));
  expect(tsolas).toMatchObject({ identity_status: "high_confidence", commissioned_officer: false });
});

test("John E Tsouderos separates military pathway from last civilian occupation", async ({ request }) => {
  const person = await publicPerson(request, "1a007dc6-b269-5628-b725-877372b6a93d", "John E Tsouderos");
  expect(person.immediate_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      canonical_organization: "United States Army Field Artillery",
      relationship_type: "military_assignment",
      temporal_basis: "explicit_immediate",
      claim_confidence: "high",
    }),
  ]);
  expect(person.last_civilian_pre_service).toEqual([
    expect.objectContaining({
      canonical_organization: null,
      occupation: "busboy or waiter",
      relationship_type: "employment",
      claim_confidence: "high",
    }),
  ]);
});

test("Henry J Tsurutani keeps legal-aid assignment and attorney occupation separate", async ({ request }) => {
  const person = await publicPerson(request, "c1d3dce5-ca55-5fab-b00b-48b340b5691e", "Henry J Tsurutani");
  expect(person.immediate_pre_oss_affiliations).toHaveLength(0);
  expect(person.last_civilian_pre_service).toHaveLength(0);
  expect(person.other_pre_oss_affiliations).toEqual(expect.arrayContaining([
    expect.objectContaining({
      canonical_organization: "Manzanar Relocation Center Legal Aid Section",
      relationship_type: "government_assignment",
      occupation: "attorney",
    }),
    expect.objectContaining({
      canonical_organization: null,
      relationship_type: "unknown",
      occupation: "attorney",
    }),
  ]));
});

test("Robert C Tucker is a student, not a Harvard employee", async ({ request }) => {
  const person = await publicPerson(request, "d3a34ac7-43ac-5275-ae27-cb95fc84324d", "Robert C Tucker");
  expect(person.immediate_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      canonical_organization: null,
      occupation: "student",
      relationship_type: "student",
    }),
  ]);
  expect(person.other_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      canonical_organization: "Harvard University",
      occupation: "student",
      relationship_type: "student",
    }),
  ]);
  expect(person.last_civilian_pre_service).toHaveLength(0);
});

test("Laura W Tuckerman keeps the unnamed dress-shop job qualified", async ({ request }) => {
  const person = await publicPerson(request, "a9947f65-e455-5916-b23c-22b3d93f9c1f", "Laura W Tuckerman");
  expect(person.name_variants).toEqual(expect.arrayContaining(["Laura Wolcott Tuckerman", "Laura Tuckerman Triest"]));
  expect(person.other_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      canonical_organization: null,
      occupation: "dress-shop worker",
      relationship_type: "employment",
      temporal_basis: "documented_prewar",
      claim_confidence: "medium",
    }),
  ]);
});

test("twelve unresolved profiles remain dignified archival-review cases", async ({ request }) => {
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
    expect(person.next_action).toContain("No reliable pre-OSS employer has yet been identified");
  }
});

test("Batch 968 evidence excludes secrets, full identifiers and raw bulk records", () => {
  expect(evidence).not.toMatch(/"serial_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toMatch(/"service_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toContain("NARA_API_KEY");
  expect(evidence).not.toContain("x-api-key");
  expect(evidence).not.toContain("candidate_identifier");
  expect(evidence).not.toContain("bulk_record_ordinal");
});

test("Batch 968 publishes exact coverage counters without changing the oil category", async ({ request, page }) => {
  const response = await request.get("./data/stats.json");
  expect(response.ok()).toBeTruthy();
  expect(await response.json()).toMatchObject({
    source_rows: 23_978,
    person_entities: 23_936,
    possible_duplicate_groups: 664,
    research_attempted_people: 15_200,
    verified_affiliation_people: 1_094,
    verified_employer_people: 488,
    archival_review_assessed_people: 13_676,
    published_claims: 9_598,
    public_sources: 6_230,
  });
  await page.goto("./oil-companies/");
  const main = page.locator("main");
  await expect(main).toContainText("14 people");
  await expect(main).toContainText("15 historically named");
  await expect(main).not.toContainText("Students");
});
