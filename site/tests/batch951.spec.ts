import fs from "node:fs";
import { expect, test } from "@playwright/test";
import type { APIRequestContext } from "@playwright/test";

const evidence = fs.readFileSync(
  new URL(
    "../../research/evidence-page466-austin-h-thompson-to-james-l-thompson-review_batch-951_2026-10-28.json",
    import.meta.url,
  ),
  "utf8",
);

const profiles = [
  ["f55c9fe2-2777-5fc4-be9e-66b2879bb6fb", "Austin H Thompson"],
  ["6afbec90-7296-5481-87e1-da8b070b1b0a", "Benjamin C Thompson"],
  ["a0e9c855-9fee-5c71-a947-e1d0695fb408", "Charles D Thompson"],
  ["e03b71e1-6c88-59a1-9c07-b256281029e4", "Charles F Thompson"],
  ["81c0c7d6-e51d-562c-8c38-9972623903d4", "Charles L Thompson"],
  ["db6bea42-64d8-585e-8a86-f8903b4e82b4", "Charles W Thompson"],
  ["ccf7ae6b-eb61-513b-9de4-ca9277c7d0de", "Cynthia N Thompson"],
  ["7a4b4ec6-23bc-5b2a-8e51-5d65b4d1acc6", "Cyril S Thompson"],
  ["fded3f72-83b3-5b17-ab28-8a73540cf94b", "Delwyn D Thompson"],
  ["14bfb168-2e53-533d-8a22-a8175b17242a", "Edward A Thompson"],
  ["0cdac249-9664-588b-813d-68ea1649b099", "Edwin E Thompson"],
  ["9608cf06-262b-5edf-aea2-89da1577571c", "Elise E Thompson"],
  ["4d8a352b-6619-5971-98c1-f6b1c07e01e7", "Esther V Thompson"],
  ["4a3cde62-0215-518b-80e2-9420cf1389c4", "Eugene K Thompson"],
  ["fce5601f-6e15-5c10-b409-54e8cc056310", "Frances K Thompson"],
  ["c5512256-75fe-57f8-9813-8ef2c96962f2", "Frances M Thompson"],
  ["da533eb3-42a9-5d6a-b1ba-d3d357b795f0", "Genevieve Thompson"],
  ["e6a733b8-2d8b-5c24-8633-ec3eb1f0e966", "Granville K Thompson"],
  ["d5a4614e-85b1-5e40-8585-00ab8fefbb92", "Harry N Thompson"],
  ["901fbd46-4d5b-5a72-92c8-3a10d537d05e", "James W Thompson"],
  ["f0db9336-3497-5723-94f6-92133e1dc79d", "James C Thompson"],
  ["90ee0049-4953-5278-b942-fc960e8cf0c0", "James H Thompson"],
  ["f0cccd89-8310-5e42-82ba-e2427ca4433a", "James L Thompson"],
] as const;

async function peopleShard(request: APIRequestContext, letter: string) {
  const response = await request.get(`./data/people/${letter}.json`);
  expect(response.ok()).toBeTruthy();
  return response.json();
}

test("Batch 951 publishes all 23 audited rows with terminal outcomes and masked identifiers", async ({ page }) => {
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

test("five Army occupation categories remain qualified and unnamed", async ({ request }) => {
  const cases = [
    ["a", "f55c9fe2-2777-5fc4-be9e-66b2879bb6fb", "radio or phonograph manufacturing occupation"],
    ["e", "0cdac249-9664-588b-813d-68ea1649b099", "nonprocess manufacturing occupation, not elsewhere classified"],
    ["g", "e6a733b8-2d8b-5c24-8633-ec3eb1f0e966", "accountant or auditor"],
    ["h", "d5a4614e-85b1-5e40-8585-00ab8fefbb92", "general office clerk"],
    ["j", "f0db9336-3497-5723-94f6-92133e1dc79d", "miner or mining-machine operator"],
  ] as const;
  for (const [letter, id, occupation] of cases) {
    const person = (await peopleShard(request, letter)).find(
      (item: { person_id: string }) => item.person_id === id,
    );
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
        temporal_basis: "strongly_date_bounded",
        claim_confidence: "medium",
      }),
    ]);
  }
});

test("James L Thompson is student status without an inferred school or employer", async ({ request, page }) => {
  const person = (await peopleShard(request, "j")).find(
    (item: { person_id: string }) => item.person_id === "f0cccd89-8310-5e42-82ba-e2427ca4433a",
  );
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
      occupation: "student",
      relationship_type: "student",
      temporal_basis: "strongly_date_bounded",
    }),
  ]);
  await page.goto("./people/f0cccd89-8310-5e42-82ba-e2427ca4433a/");
  await expect(page.locator("main")).toContainText("Students category");
  await expect(page.locator("main")).toContainText("no school or employer");
});

test("Frances K Thompson exposes the name conflict and transfers no Army affiliation", async ({ request, page }) => {
  const person = (await peopleShard(request, "f")).find(
    (item: { person_id: string }) => item.person_id === "fce5601f-6e15-5c10-b409-54e8cc056310",
  );
  expect(person).toMatchObject({
    identity_status: "conflicting",
    research_status: "conflicting_sources",
    personnel_category: "unknown_or_indeterminate",
  });
  expect(person.other_pre_oss_affiliations).toHaveLength(0);
  expect(person.claims).toEqual([
    expect.objectContaining({
      claim_confidence: "conflicting",
      publication_status: "conflicting",
    }),
  ]);
  await page.goto("./people/fce5601f-6e15-5c10-b409-54e8cc056310/");
  const main = page.locator("main");
  await expect(main).toContainText("Frank K. Thompson");
  await expect(main).toContainText("no Army field is transferred");
});

test("Benjamin C Thompson retains a qualified identity lead without public facts", async ({ request, page }) => {
  const person = (await peopleShard(request, "b")).find(
    (item: { person_id: string }) => item.person_id === "6afbec90-7296-5481-87e1-da8b070b1b0a",
  );
  expect(person).toMatchObject({
    identity_status: "ambiguous",
    research_status: "needs_identity_review",
    personnel_category: "unknown_or_indeterminate",
  });
  expect(person.immediate_pre_oss_affiliations).toHaveLength(0);
  expect(person.last_civilian_pre_service).toHaveLength(0);
  expect(person.other_pre_oss_affiliations).toHaveLength(0);
  expect(person.claims).toHaveLength(0);
  await page.goto("./people/6afbec90-7296-5481-87e1-da8b070b1b0a/");
  const main = page.locator("main");
  await expect(main).toContainText("plausible exact-name OSS candidate");
  await expect(main).toContainText("Review Box 774");
});

test("Batch 951 evidence excludes secrets and protected-identifier fields", () => {
  expect(evidence).not.toMatch(/"serial_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toMatch(/"service_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toContain("NARA_API_KEY");
  expect(evidence).not.toContain("x-api-key");
  expect(evidence).not.toContain("bulk_record_ordinal");
});

test("Batch 951 publishes exact coverage counters without changing the oil category", async ({ request, page }) => {
  const response = await request.get("./data/stats.json");
  expect(response.ok()).toBeTruthy();
  expect(await response.json()).toMatchObject({
    source_rows: 23_978,
    person_entities: 23_936,
    possible_duplicate_groups: 648,
    research_attempted_people: 14_813,
    verified_affiliation_people: 1_050,
    verified_employer_people: 471,
    archival_review_assessed_people: 13_288,
    published_claims: 9_203,
    public_sources: 6_032,
  });
  await page.goto("./oil-companies/");
  const main = page.locator("main");
  await expect(main).toContainText("14 people");
  await expect(main).toContainText("15 historically named");
  await expect(main).not.toContainText("United States Army");
});
