import fs from "node:fs";
import { expect, test } from "@playwright/test";
import type { APIRequestContext } from "@playwright/test";

const evidence = fs.readFileSync(
  new URL(
    "../../research/evidence-page468-arthur-m-thurston-to-aaron-l-tietelbaum-review_batch-955_2026-10-29.json",
    import.meta.url,
  ),
  "utf8",
);

const profiles = [
  ["db997c8d-1ca3-5c5d-9485-3df1941a3be8", "Arthur M Thurston"],
  ["dc28e0fc-012a-52a2-a3ea-321137395080", "Charles A Thurston"],
  ["bac0f088-6372-5119-9a5d-dc481b57e921", "Lois L Tibben"],
  ["134dccdb-07cf-53ba-8a6a-5cedb980acee", "Margaret J Tibbetts"],
  ["5d5d1a61-c567-5008-b42b-1ed44a218043", "Ralph F Tibbetts"],
  ["78238042-cac6-5e6a-8949-e4b89019e48c", "Robert W Tibbetts"],
  ["24d45a3d-d48e-55ee-bdab-8e4e7ff516ae", "Richard H Tibbs"],
  ["63cf9ad7-a959-57d3-a916-1979f689fb0c", "Stafford Tibbs"],
  ["baa17585-db77-5852-a52e-64a0368bddcb", "Edward T Tiche"],
  ["01bc7836-0bd1-5168-835a-401413775729", "Kenneth H Tichnell"],
  ["e0365f40-d2e7-5b3d-8852-b1b7e56f1831", "William D Ticknor"],
  ["07920f04-56ab-5277-9a33-9c27d3edc616", "James M Tidwell"],
  ["dc9b365c-a6fb-58dc-9b91-570b391e9e71", "Jane V Tidwell"],
  ["6382cde3-d93d-5fee-a566-98fb1e218cfe", "Jane W Tidwell"],
  ["21fe8de2-5aab-578c-b21a-2fcdf5f76d02", "William A Tidwell"],
  ["70acabb2-5e46-5e5f-8411-0b079ec974e2", "Loren A Tiegland"],
  ["5ea910b5-24b0-5df0-b538-d7e10cff8fe7", "Herman F Tierney"],
  ["1b15da94-c712-5b6a-ba31-1eb8546aa499", "Joseph E Tierney"],
  ["a054c154-cd1d-5aa1-97c3-1ead473286d6", "Philip D Tierney"],
  ["2c4e7a1c-f734-5b75-8bd0-8aeb2ec0bf4a", "Francis R Tierno"],
  ["5aa4fd50-2bbe-5b56-95fc-461ab9766544", "Cornelius Tiers"],
  ["c6de9c88-1717-5bcb-891f-8e1706713f00", "Aaron L Tietelbaum"],
] as const;

const armyCategories = [
  ["dc28e0fc-012a-52a2-a3ea-321137395080", "Charles A Thurston", "architects", "1941-05-02"],
  ["5d5d1a61-c567-5008-b42b-1ed44a218043", "Ralph F Tibbetts", "radio operators", "1944-03-31"],
  ["24d45a3d-d48e-55ee-bdab-8e4e7ff516ae", "Richard H Tibbs", "lithographers", "1943-05-04"],
  ["07920f04-56ab-5277-9a33-9c27d3edc616", "James M Tidwell", "managers and officials, n. e. c.", "1943-05-29"],
  ["1b15da94-c712-5b6a-ba31-1eb8546aa499", "Joseph E Tierney", "elevator operators", "1942-10-16"],
  ["a054c154-cd1d-5aa1-97c3-1ead473286d6", "Philip D Tierney", "salesmen, insurance", "1942-09-08"],
  ["2c4e7a1c-f734-5b75-8bd0-8aeb2ec0bf4a", "Francis R Tierno", "clerks, general", "1940-09-16"],
  ["5aa4fd50-2bbe-5b56-95fc-461ab9766544", "Cornelius Tiers", "aviators", "1942-04-13"],
  ["c6de9c88-1717-5bcb-891f-8e1706713f00", "Aaron L Tietelbaum", "lawyers and judges", "1942-08-10"],
] as const;

const unresolvedIds = [
  "bac0f088-6372-5119-9a5d-dc481b57e921",
  "134dccdb-07cf-53ba-8a6a-5cedb980acee",
  "78238042-cac6-5e6a-8949-e4b89019e48c",
  "63cf9ad7-a959-57d3-a916-1979f689fb0c",
  "baa17585-db77-5852-a52e-64a0368bddcb",
  "01bc7836-0bd1-5168-835a-401413775729",
  "e0365f40-d2e7-5b3d-8852-b1b7e56f1831",
  "dc9b365c-a6fb-58dc-9b91-570b391e9e71",
  "6382cde3-d93d-5fee-a566-98fb1e218cfe",
  "21fe8de2-5aab-578c-b21a-2fcdf5f76d02",
  "70acabb2-5e46-5e5f-8411-0b079ec974e2",
  "5ea910b5-24b0-5df0-b538-d7e10cff8fe7",
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

test("Batch 955 publishes 23 source rows as 22 audited people with terminal outcomes", async ({ page, request }) => {
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
  const philip = await publicPerson(
    request,
    "a054c154-cd1d-5aa1-97c3-1ead473286d6",
    "Philip D Tierney",
  );
  expect(philip.source_records).toHaveLength(2);
  expect(
    philip.source_records.map((item: { source_record_id: string }) => item.source_record_id).sort(),
  ).toEqual([
    "2359ca76-eba4-53b2-be7f-bae4abb2c73d",
    "7422bd53-4006-55e0-b032-e69756b5f1ba",
  ]);
});

test("Arthur M Thurston publishes a documented FBI assignment without claiming immediacy", async ({ request, page }) => {
  const person = await publicPerson(
    request,
    "db997c8d-1ca3-5c5d-9485-3df1941a3be8",
    "Arthur M Thurston",
  );
  expect(person).toMatchObject({
    identity_status: "high_confidence",
    research_status: "completed",
    personnel_category: "commissioned_army_officer",
    commissioned_officer: true,
  });
  expect(person.immediate_pre_oss_affiliations).toHaveLength(0);
  expect(person.last_civilian_pre_service).toHaveLength(0);
  expect(person.other_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      canonical_organization: "Federal Bureau of Investigation",
      historical_organization: "Federal Bureau of Investigation",
      role_title: "Legal Attaché, American Embassy, London",
      relationship_type: "government_assignment",
      end_date: "1943-08-18",
      temporal_basis: "strongly_date_bounded",
      claim_confidence: "high",
    }),
  ]);
  await page.goto("./people/db997c8d-1ca3-5c5d-9485-3df1941a3be8/");
  const main = page.locator("main");
  await expect(main).toContainText("Federal Bureau of Investigation");
  await expect(main).toContainText("Legal Attaché, American Embassy, London");
  await expect(main).toContainText("beginning and end dates are not established");
  await expect(main).toContainText("immediacy before OSS is not established");
});

test("nine Army matches publish only qualified dated historical categories", async ({ request }) => {
  for (const [id, name, occupation, endDate] of armyCategories) {
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
        relationship_type: "employment",
        end_date: endDate,
        temporal_basis: "strongly_date_bounded",
        claim_confidence: "medium",
      }),
    ]);
  }
});

test("Joseph Tierney keeps the sourced suffix and Cornelius Tiers keeps source damage transparent", async ({ request, page }) => {
  const joseph = await publicPerson(
    request,
    "1b15da94-c712-5b6a-ba31-1eb8546aa499",
    "Joseph E Tierney",
  );
  expect(joseph.name_variants).toContain("Joseph E Tierney Jr");

  await page.goto("./people/5aa4fd50-2bbe-5b56-95fc-461ab9766544/");
  const main = page.locator("main");
  await expect(main).toContainText("fixed-width Army form CORNELI S");
  await expect(main).toContainText("aviators");
  await expect(main).not.toContainText("employer: Aviators");
});

test("twelve unresolved people keep archival-review outcomes without transferred facts", async ({ request }) => {
  for (const id of unresolvedIds) {
    const profile = profiles.find(([profileId]) => profileId === id);
    expect(profile).toBeTruthy();
    const person = await publicPerson(request, id, profile![1]);
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

test("Batch 955 evidence excludes secrets and protected-identifier fields", () => {
  expect(evidence).not.toMatch(/"serial_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toMatch(/"service_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toContain("NARA_API_KEY");
  expect(evidence).not.toContain("x-api-key");
  expect(evidence).not.toContain("bulk_record_ordinal");
});

test("Batch 955 publishes exact coverage counters without changing the oil category", async ({ request, page }) => {
  const response = await request.get("./data/stats.json");
  expect(response.ok()).toBeTruthy();
  expect(await response.json()).toMatchObject({
    source_rows: 23_978,
    person_entities: 23_936,
    possible_duplicate_groups: 648,
    research_attempted_people: 14_903,
    verified_affiliation_people: 1_054,
    verified_employer_people: 472,
    archival_review_assessed_people: 13_379,
    published_claims: 9_263,
    public_sources: 6_058,
  });
  await page.goto("./oil-companies/");
  const main = page.locator("main");
  await expect(main).toContainText("14 people");
  await expect(main).toContainText("15 historically named");
  await expect(main).not.toContainText("Federal Bureau of Investigation");
});
