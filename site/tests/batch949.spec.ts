import fs from "node:fs";
import { expect, test } from "@playwright/test";
import type { APIRequestContext } from "@playwright/test";

const evidence = fs.readFileSync(
  new URL(
    "../../research/evidence-page465-robert-thomale-to-josephine-thomas-review_batch-949_2026-10-28.json",
    import.meta.url,
  ),
  "utf8",
);

const profiles = [
  ["a2237c45-cf09-5527-93f5-e8a28fa480b1", "Robert Thomale"],
  ["eb722592-1737-570a-8c5d-d53d223cc31d", "Anthony Thomann"],
  ["9ec3b452-168a-58d2-bf07-717405f8432f", "Anton C Thomann"],
  ["848cbc0c-de59-53c2-971f-59d1550b4bf0", "Albert Thomas"],
  ["b7f0c3a4-816e-5d51-9ae4-ca5de1cea3a7", "Alfred B Thomas"],
  ["4b6ce778-ca66-5bab-bead-6092f597e135", "Allison K Thomas"],
  ["327b7145-da3a-5e1c-8f03-97cfb7d52c43", "Annie B Thomas"],
  ["1f065e09-e3b8-5832-8b92-150d3fa2ecb6", "Christopher G Thomas"],
  ["fea54bf1-c0f0-5a5c-8efb-d804746fedbd", "Clinton F Thomas"],
  ["8012bd97-b9ab-5104-b534-426bc75adab4", "Cynthia M Thomas"],
  ["21853702-bc6d-500c-a4ae-739c01fc2c85", "Edward G Thomas"],
  ["e398bf65-febf-5a08-95a2-03748594a270", "Francis L Thomas"],
  ["3da7dfb8-29bf-5862-8f30-8a94ebf2a33a", "G W Thomas"],
  ["53563a1b-63ec-514a-812d-8772c3303a50", "George W Thomas"],
  ["19247a68-3dd0-5808-b4de-18a98415f82a", "Gertrude M Thomas"],
  ["71805a05-515c-50ed-88e8-96d6c8bc7b2b", "Gregory Thomas"],
  ["abd10a7f-9aa1-5912-8227-287c708d7e6a", "Helen E Thomas"],
  ["82a29dd8-abaf-597a-95ca-a3ebcf4bd01e", "Hugh R Thomas"],
  ["6351a088-3a21-5bd4-9386-c23593aef8fb", "James A Thomas"],
  ["f1d18087-0244-5533-af39-2747203f7117", "Jean Thomas"],
  ["77cd18a4-d48a-5460-bc8b-ee359f58b1fc", "John L Thomas"],
  ["80feec29-4005-5aea-af35-fef831dbc9cc", "Joseph E Thomas"],
  ["2111bd68-1f04-59f8-9753-708774f5be42", "Josephine Thomas"],
] as const;

async function peopleShard(request: APIRequestContext, letter: string) {
  const response = await request.get(`./data/people/${letter}.json`);
  expect(response.ok()).toBeTruthy();
  return response.json();
}

test("Batch 949 publishes all 23 audited rows with terminal outcomes and masked identifiers", async ({ page }) => {
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

test("Allison Thomas separates the Army pathway from unnamed Michigan legal work", async ({ request, page }) => {
  const person = (await peopleShard(request, "a")).find(
    (item: { person_id: string }) => item.person_id === "4b6ce778-ca66-5bab-bead-6092f597e135",
  );
  expect(person).toMatchObject({
    identity_status: "high_confidence",
    research_status: "occupation_only_found",
    personnel_category: "commissioned_army_officer",
    commissioned_officer: true,
  });
  expect(person.immediate_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      canonical_organization: "United States Army",
      relationship_type: "military_assignment",
      temporal_basis: "explicit_immediate",
      claim_confidence: "high",
    }),
  ]);
  expect(person.last_civilian_pre_service).toEqual([
    expect.objectContaining({
      canonical_organization: null,
      occupation: "lawyer",
      claim_confidence: "medium",
    }),
  ]);
  await page.goto("./people/4b6ce778-ca66-5bab-bead-6092f597e135/");
  const main = page.locator("main");
  await expect(main).toContainText("United States Army");
  await expect(main).toContainText("lawyer");
  await expect(main).toContainText("no employer or firm");
});

test("five Army categories remain qualified and post-OSS unassigned codes remain unpublished", async ({ request }) => {
  const cases = [
    ["a", "eb722592-1737-570a-8c5d-d53d223cc31d", "bookkeepers and cashiers, except bank cashiers"],
    ["a", "9ec3b452-168a-58d2-bf07-717405f8432f", "motor-vehicle mechanic or repairman"],
    ["c", "1f065e09-e3b8-5832-8b92-150d3fa2ecb6", "retail manager"],
    ["e", "21853702-bc6d-500c-a4ae-739c01fc2c85", "carpenter"],
    ["j", "6351a088-3a21-5bd4-9386-c23593aef8fb", "cook, except private family"],
  ] as const;
  for (const [letter, id, occupation] of cases) {
    const person = (await peopleShard(request, letter)).find((item: { person_id: string }) => item.person_id === id);
    expect(person.other_pre_oss_affiliations[0]).toMatchObject({
      canonical_organization: null,
      occupation,
      claim_confidence: "medium",
    });
  }

  for (const id of ["848cbc0c-de59-53c2-971f-59d1550b4bf0", "e398bf65-febf-5a08-95a2-03748594a270"]) {
    const letter = id.startsWith("848") ? "a" : "f";
    const person = (await peopleShard(request, letter)).find((item: { person_id: string }) => item.person_id === id);
    expect(person.other_pre_oss_affiliations).toHaveLength(0);
    expect(person.claims).toHaveLength(1);
  }
});

test("Batch 949 evidence excludes secrets and full protected identifiers", () => {
  expect(evidence).not.toMatch(/"serial_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toMatch(/"service_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toContain("NARA_API_KEY");
  expect(evidence).not.toContain("x-api-key");
  expect(evidence).not.toContain("32075888");
  expect(evidence).not.toContain("1284241");
});

test("Batch 949 publishes exact coverage counters without changing the oil category", async ({ request, page }) => {
  const response = await request.get("./data/stats.json");
  expect(response.ok()).toBeTruthy();
  expect(await response.json()).toMatchObject({
    source_rows: 23_978,
    person_entities: 23_936,
    possible_duplicate_groups: 648,
    research_attempted_people: 14_767,
    verified_affiliation_people: 1_050,
    verified_employer_people: 471,
    archival_review_assessed_people: 13_242,
    published_claims: 9_180,
    public_sources: 6_022,
  });
  await page.goto("./oil-companies/");
  const main = page.locator("main");
  await expect(main).toContainText("14 people");
  await expect(main).toContainText("15 historically named");
  await expect(main).not.toContainText("United States Army");
});
