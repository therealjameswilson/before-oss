import fs from "node:fs";
import { expect, test } from "@playwright/test";
import type { APIRequestContext } from "@playwright/test";

const evidence = fs.readFileSync(
  new URL(
    "../../research/evidence-page469-george-s-tinlakos-to-bentley-tobin-review_batch-957_2026-10-29.json",
    import.meta.url,
  ),
  "utf8",
);

const profiles = [
  ["fb61ba6c-6059-550e-9839-82e058ce3783", "George S Tinlakos"],
  ["48d659c6-cab8-5a75-9e42-15f9c5efb2c9", "Vladimir Tinmoshenko"],
  ["2b9323d8-17cb-5503-b9ab-240238a9dad4", "Gerhard Tinner"],
  ["4977142b-28b4-5965-b7b5-7eb62d661f34", "Amedee Tinners"],
  ["3b2e307c-2e90-50fc-aa80-a0203028cef8", "Calvin L Tinney"],
  ["eb1fe0e8-97f5-5885-8d74-e9323154bd9b", "Paul Tinney"],
  ["f4b40566-0b08-527f-bf49-e7afc4b7650f", "Louise H Tipp"],
  ["d255da88-c17e-5014-bc51-06e5a972cc32", "Timonthy L Tippit"],
  ["818d4e1f-d461-5cde-b8d3-85c50d2ae0a3", "Lloyd R Tipton"],
  ["1c215017-0200-51c6-b49d-566f9a78cdcb", "Joseph Tirpik"],
  ["affc7800-9e2e-51f2-bc04-f5e4fdae4af4", "Laurence A Tisch"],
  ["b7a5fe6e-a8bc-5da9-a1e4-fb5d7e7e9566", "Chamroon Tishyarandara"],
  ["385e9df4-b96c-55fb-9879-2cec534c8cd3", "Paul Tison"],
  ["4f650f82-d872-5bab-a27f-c2937118926c", "Mischa Titiev"],
  ["0a50dadb-9ce7-5fcf-a35b-cee05810da13", "Austin E Titus"],
  ["5c7948a6-b3c3-5ae7-b64e-3c6f7bf1c6f9", "Gerald Titus"],
  ["c4470663-f746-5d1b-8be4-a8d01c796fc0", "Roy Titus"],
  ["2a6e984b-0962-5841-9d7c-c7ff1d07d76b", "Kenneth D Tivey"],
  ["6a5bf026-1024-547c-9b12-ee8055a12439", "Carl Tjerandsen"],
  ["fdbd568c-3c2f-59eb-a1c0-098d2e3fc429", "Carl Tjerandsen"],
  ["8b47480b-a586-540b-80c3-fdb94bdd067b", "Joseph M Tobari"],
  ["178ce891-c060-5d71-8c4c-20646d94107c", "Abraham J Tobias"],
  ["cd940470-af04-59be-b654-97e6ccaf928b", "Bentley Tobin"],
] as const;

const unresolvedIds = new Set([
  "2b9323d8-17cb-5503-b9ab-240238a9dad4",
  "4977142b-28b4-5965-b7b5-7eb62d661f34",
  "f4b40566-0b08-527f-bf49-e7afc4b7650f",
  "d255da88-c17e-5014-bc51-06e5a972cc32",
  "818d4e1f-d461-5cde-b8d3-85c50d2ae0a3",
  "1c215017-0200-51c6-b49d-566f9a78cdcb",
  "b7a5fe6e-a8bc-5da9-a1e4-fb5d7e7e9566",
  "385e9df4-b96c-55fb-9879-2cec534c8cd3",
  "0a50dadb-9ce7-5fcf-a35b-cee05810da13",
  "5c7948a6-b3c3-5ae7-b64e-3c6f7bf1c6f9",
  "2a6e984b-0962-5841-9d7c-c7ff1d07d76b",
  "fdbd568c-3c2f-59eb-a1c0-098d2e3fc429",
]);

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

test("Batch 957 publishes 23 audited people with terminal outcomes", async ({ page }) => {
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

test("four named employers preserve immediate and last-civilian distinctions", async ({ request, page }) => {
  const cases = [
    ["48d659c6-cab8-5a75-9e42-15f9c5efb2c9", "Vladimir Tinmoshenko", "Stanford University", "Food Research Institute, Stanford University"],
    ["3b2e307c-2e90-50fc-aa80-a0203028cef8", "Calvin L Tinney", "Mutual Broadcasting System", "Mutual Broadcasting System"],
    ["4f650f82-d872-5bab-a27f-c2937118926c", "Mischa Titiev", "University of Michigan", "University of Michigan"],
    ["c4470663-f746-5d1b-8be4-a8d01c796fc0", "Roy Titus", "Helena Rubinstein Inc.", "Helena Rubinstein Inc."],
  ] as const;

  for (const [id, name, canonical, historical] of cases) {
    const person = await publicPerson(request, id, name);
    expect(person).toMatchObject({ research_status: "verified_employer_found" });
    expect(person.immediate_pre_oss_affiliations).toEqual([
      expect.objectContaining({
        canonical_organization: canonical,
        historical_organization: historical,
        relationship_type: "employment",
        immediate_pre_oss: true,
        last_civilian_pre_service: true,
      }),
    ]);
    expect(person.last_civilian_pre_service).toEqual([
      expect.objectContaining({ canonical_organization: canonical }),
    ]);
    await page.goto(`./people/${id}/`);
    await expect(page.locator("main")).toContainText(historical);
  }
});

test("George Tinlakos keeps the printed spelling and qualified merchant-marine and Army pathways", async ({ request, page }) => {
  const person = await publicPerson(request, "fb61ba6c-6059-550e-9839-82e058ce3783", "George S Tinlakos");
  expect(person).toMatchObject({
    display_name: "George S Tinlakos",
    identity_status: "high_confidence",
    research_status: "completed",
    personnel_category: "enlisted_army_personnel",
  });
  expect(person.name_variants).toContain("George S. Tiniakos");
  expect(person.immediate_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      canonical_organization: "United States Army",
      relationship_type: "military_assignment",
      temporal_basis: "probable_immediate",
      claim_confidence: "medium",
    }),
  ]);
  expect(person.other_pre_oss_affiliations).toEqual(expect.arrayContaining([
    expect.objectContaining({
      canonical_organization: "Greek Merchant Marine",
      relationship_type: "professional_affiliation",
    }),
  ]));
  await page.goto("./people/fb61ba6c-6059-550e-9839-82e058ce3783/");
  const main = page.locator("main");
  await expect(main).toContainText("George S. Tiniakos");
  await expect(main).toContainText("ship, shipping line and employer remain unknown");
});

test("student and military pathways are not mislabeled as employers", async ({ request }) => {
  const laurence = await publicPerson(request, "affc7800-9e2e-51f2-bc04-f5e4fdae4af4", "Laurence A Tisch");
  expect(laurence.immediate_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      canonical_organization: "New York University",
      relationship_type: "student",
      immediate_pre_oss: true,
      last_civilian_pre_service: false,
    }),
  ]);
  expect(laurence.last_civilian_pre_service).toHaveLength(0);

  const joseph = await publicPerson(request, "8b47480b-a586-540b-80c3-fdb94bdd067b", "Joseph M Tobari");
  expect(joseph.immediate_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      canonical_organization: "University of Utah",
      relationship_type: "student",
      last_civilian_pre_service: false,
    }),
  ]);
  expect(joseph.last_civilian_pre_service).toHaveLength(0);

  const abraham = await publicPerson(request, "178ce891-c060-5d71-8c4c-20646d94107c", "Abraham J Tobias");
  expect(abraham.immediate_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      canonical_organization: "United States Army Air Forces",
      relationship_type: "military_assignment",
      last_civilian_pre_service: false,
    }),
  ]);
  expect(abraham.other_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      canonical_organization: "Federal Art Project",
      relationship_type: "government_assignment",
    }),
  ]);
});

test("the two Carl Tjerandsen rows remain separate and only row 19 receives biography claims", async ({ request, page }) => {
  const first = await publicPerson(request, "6a5bf026-1024-547c-9b12-ee8055a12439", "Carl Tjerandsen");
  const second = await publicPerson(request, "fdbd568c-3c2f-59eb-a1c0-098d2e3fc429", "Carl Tjerandsen");
  expect(first).toMatchObject({ identity_status: "high_confidence", research_status: "completed" });
  expect(second).toMatchObject({ identity_status: "ambiguous", research_status: "requires_archival_review" });
  expect(first.possible_duplicate_group).toBeTruthy();
  expect(first.possible_duplicate_group).toBe(second.possible_duplicate_group);
  expect(first.immediate_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      canonical_organization: null,
      occupation: "food and agriculture researcher",
      temporal_basis: "explicit_immediate",
    }),
  ]);
  expect(first.other_pre_oss_affiliations).toEqual(expect.arrayContaining([
    expect.objectContaining({ canonical_organization: "University of Idaho" }),
  ]));
  expect(second.immediate_pre_oss_affiliations).toHaveLength(0);
  expect(second.other_pre_oss_affiliations).toHaveLength(0);
  expect(second.claims).toHaveLength(0);
  await page.goto("./people/fdbd568c-3c2f-59eb-a1c0-098d2e3fc429/");
  await expect(page.locator("main")).toContainText("do not merge");
});

test("twelve unresolved or ambiguous people keep archival outcomes without transferred facts", async ({ request }) => {
  for (const [id, name] of profiles.filter(([id]) => unresolvedIds.has(id))) {
    const person = await publicPerson(request, id, name);
    expect(person.research_status).toBe("requires_archival_review");
    expect(["unresolved", "ambiguous"]).toContain(person.identity_status);
    expect(person.personnel_category).toBe("unknown_or_indeterminate");
    expect(person.immediate_pre_oss_affiliations).toHaveLength(0);
    expect(person.last_civilian_pre_service).toHaveLength(0);
    expect(person.other_pre_oss_affiliations).toHaveLength(0);
    expect(person.claims).toHaveLength(0);
  }
});

test("Batch 957 evidence excludes secrets and protected-identifier fields", () => {
  expect(evidence).not.toMatch(/"serial_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toMatch(/"service_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toContain("NARA_API_KEY");
  expect(evidence).not.toContain("x-api-key");
  expect(evidence).not.toContain("bulk_record_ordinal");
});

test("Batch 957 publishes exact coverage counters without changing the oil category", async ({ request, page }) => {
  const response = await request.get("./data/stats.json");
  expect(response.ok()).toBeTruthy();
  expect(await response.json()).toMatchObject({
    source_rows: 23_978,
    person_entities: 23_936,
    possible_duplicate_groups: 649,
    research_attempted_people: 14_949,
    verified_affiliation_people: 1_067,
    verified_employer_people: 478,
    archival_review_assessed_people: 13_425,
    published_claims: 9_320,
    public_sources: 6_088,
  });
  await page.goto("./oil-companies/");
  const main = page.locator("main");
  await expect(main).toContainText("14 people");
  await expect(main).toContainText("15 historically named");
  await expect(main).not.toContainText("Helena Rubinstein Inc.");
});
