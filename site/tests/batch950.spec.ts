import fs from "node:fs";
import { expect, test } from "@playwright/test";
import type { APIRequestContext } from "@playwright/test";

const evidence = fs.readFileSync(
  new URL(
    "../../research/evidence-page465-lewis-v-thomas-to-allen-j-thompson-review_batch-950_2026-10-28.json",
    import.meta.url,
  ),
  "utf8",
);

const profiles = [
  ["e44e7ee4-3e3c-56c0-b0e2-9f4f360fa3d7", "Lewis V Thomas"],
  ["f1bcfc60-59c3-5091-99ca-a5c81b13f6b6", "Lloyd T Thomas"],
  ["101cde46-ba70-5bb4-9dbb-04dd02c75096", "Lorres C Thomas"],
  ["2cc7cf60-0256-5442-9eb9-4b452b20f8a6", "Margaret Thomas"],
  ["54c9e6d9-fac7-559b-a6b4-6a1d1970383b", "Martha E Thomas"],
  ["e2dd9b24-eeaf-5765-83cc-afd7f2938449", "Mary C Thomas"],
  ["b9b8b015-4796-5137-b9bd-8bcc7228e6c3", "Melen E Thomas"],
  ["0763cce9-6235-5eff-8672-c82aa0ee7bc9", "Otaway M Thomas"],
  ["ca4335f3-d926-5d2d-8129-a26267b033c8", "Richard A Thomas"],
  ["0c6563ee-519e-5ee1-a7cf-949ac6ef1d01", "Richard B Thomas"],
  ["3cc76513-1dd0-5b56-bb1c-38f7bac4503d", "Roosevelt Thomas"],
  ["75d7d142-63ec-5319-ab54-44b9a9bc3ff9", "Rudolph Thomas"],
  ["72f771c2-2f4f-5853-811e-9b4c6fb439c0", "Ruth E Thomas"],
  ["560a03c8-5f9a-54f9-bcce-1637871a09f8", "Sidney S Thomas"],
  ["ee1f713c-aaf1-5b26-82c2-57718bd18007", "Thomas H Thomas"],
  ["f33765df-f93d-5ca9-8630-6d0cc2f32d71", "Wilfred Thomas"],
  ["c7fca1a6-69e9-5194-b841-f58a7ab6b688", "William H Thomas"],
  ["370c487f-8c13-5bf4-ad54-04b2a4a2996a", "William J Thomason"],
  ["d37e4799-3e65-5298-8a88-305db958013c", "Harvey W Thomasson"],
  ["7b9a42c7-87aa-5133-a3ab-60dd72458c8d", "Stefan A Thomasson"],
  ["544f416b-ca58-5f26-b2d2-f68cd03c7bdd", "Paul P Thomle"],
  ["c90e461d-215c-5e44-aa88-77a5cc478f58", "Allen R Thompson"],
  ["756e5e56-0715-500f-98fd-aa07095efe1f", "Allen J Thompson"],
] as const;

async function peopleShard(request: APIRequestContext, letter: string) {
  const response = await request.get(`./data/people/${letter}.json`);
  expect(response.ok()).toBeTruthy();
  return response.json();
}

test("Batch 950 publishes all 23 audited rows with terminal outcomes and masked identifiers", async ({ page }) => {
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

test("three Army occupation categories remain qualified and unnamed", async ({ request }) => {
  const cases = [
    ["r", "75d7d142-63ec-5319-ab54-44b9a9bc3ff9", "farm hand on a general farm"],
    ["w", "f33765df-f93d-5ca9-8630-6d0cc2f32d71", "packing, filling, labeling, marking, bottling, or related work, not elsewhere classified"],
    ["h", "d37e4799-3e65-5298-8a88-305db958013c", "insurance salesman"],
  ] as const;
  for (const [letter, id, occupation] of cases) {
    const person = (await peopleShard(request, letter)).find(
      (item: { person_id: string }) => item.person_id === id,
    );
    expect(person).toMatchObject({
      identity_status: "high_confidence",
      research_status: "occupation_only_found",
      personnel_category: "enlisted_army_personnel",
    });
    expect(person.other_pre_oss_affiliations).toEqual([
      expect.objectContaining({
        canonical_organization: null,
        occupation,
        temporal_basis: "strongly_date_bounded",
        claim_confidence: "medium",
      }),
    ]);
  }
});

test("Lorres Thomas separates student and military chronology from employer claims", async ({ request, page }) => {
  const person = (await peopleShard(request, "l")).find(
    (item: { person_id: string }) => item.person_id === "101cde46-ba70-5bb4-9dbb-04dd02c75096",
  );
  expect(person).toMatchObject({
    identity_status: "confirmed",
    research_status: "requires_archival_review",
    personnel_category: "commissioned_army_officer",
    commissioned_officer: true,
  });
  expect(person.immediate_pre_oss_affiliations).toHaveLength(0);
  expect(person.last_civilian_pre_service).toHaveLength(0);
  expect(person.other_pre_oss_affiliations).toEqual(expect.arrayContaining([
    expect.objectContaining({
      canonical_organization: "United States Military Academy",
      relationship_type: "student",
      temporal_basis: "temporal_relation_uncertain",
    }),
    expect.objectContaining({
      canonical_organization: "United States Army",
      relationship_type: "military_assignment",
      temporal_basis: "temporal_relation_uncertain",
    }),
  ]));
  await page.goto("./people/101cde46-ba70-5bb4-9dbb-04dd02c75096/");
  const main = page.locator("main");
  await expect(main).toContainText("United States Military Academy");
  await expect(main).toContainText("Corps of Engineers");
  await expect(main).toContainText("student");
});

test("Paul Thomle publishes the official identity result without inventing an affiliation", async ({ request, page }) => {
  const person = (await peopleShard(request, "p")).find(
    (item: { person_id: string }) => item.person_id === "544f416b-ca58-5f26-b2d2-f68cd03c7bdd",
  );
  expect(person).toMatchObject({
    identity_status: "confirmed",
    research_status: "requires_archival_review",
    personnel_category: "enlisted_army_personnel",
    commissioned_officer: false,
  });
  expect(person.immediate_pre_oss_affiliations).toHaveLength(0);
  expect(person.last_civilian_pre_service).toHaveLength(0);
  expect(person.other_pre_oss_affiliations).toHaveLength(0);
  expect(person.claims).toHaveLength(1);
  await page.goto("./people/544f416b-ca58-5f26-b2d2-f68cd03c7bdd/");
  await expect(page.locator("main")).toContainText("died of wounds");
});

test("Batch 950 evidence excludes secrets and protected-identifier fields", () => {
  expect(evidence).not.toMatch(/"serial_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toMatch(/"service_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toContain("NARA_API_KEY");
  expect(evidence).not.toContain("x-api-key");
});

test("Batch 950 publishes exact coverage counters without changing the oil category", async ({ request, page }) => {
  const response = await request.get("./data/stats.json");
  expect(response.ok()).toBeTruthy();
  expect(await response.json()).toMatchObject({
    source_rows: 23_978,
    person_entities: 23_936,
    possible_duplicate_groups: 648,
    research_attempted_people: 14_790,
    verified_affiliation_people: 1_050,
    verified_employer_people: 471,
    archival_review_assessed_people: 13_265,
    published_claims: 9_190,
    public_sources: 6_028,
  });
  await page.goto("./oil-companies/");
  const main = page.locator("main");
  await expect(main).toContainText("14 people");
  await expect(main).toContainText("15 historically named");
  await expect(main).not.toContainText("United States Army");
});
