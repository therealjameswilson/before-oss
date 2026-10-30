import fs from "node:fs";
import { expect, test } from "@playwright/test";
import type { APIRequestContext } from "@playwright/test";

const evidence = fs.readFileSync(
  new URL(
    "../../research/evidence-page484-domonic-virdo-to-floyd-tomas-vlasic-review_batch-987_2026-10-30.json",
    import.meta.url,
  ),
  "utf8",
);

const profiles = [
  ["c986edb4-91c5-53df-aa84-a04979f76455", "Domonic Virdo"],
  ["5a5ebcb8-87d3-5419-8da4-e205e973af8a", "Robert Viret"],
  ["832da0f2-62c5-52f4-ad61-2c2bf0e6f873", "Russell E Virgils"],
  ["fe075865-c28d-5ac1-bb0a-f940d75c5d3e", "Anthony Visini"],
  ["473f8b49-bf87-5cf5-b4ff-d92ff3fc6e4f", "Antonio Visini"],
  ["256326f1-90d9-578a-939a-a56eda91e1e0", "C R Vislocky"],
  ["f8cab5da-5946-5c38-9da1-1666fdd03e42", "Theodore Visser"],
  ["b4622aeb-4202-531e-8793-8dadd714cba3", "William G Visser"],
  ["a2cfec37-7bba-5459-ba97-0505bae9aa8d", "Steve Vitak Jr."],
  ["89a44246-6c0f-5d8f-9fc3-e28d254d4d1b", "Charles J Vitale"],
  ["9b76b69f-fc08-5c07-acea-22eb719b6b64", "Samuel Vitale"],
  ["f9a41038-73a4-58de-b790-244e10a28354", "Domenick P Viterisi"],
  ["abb41258-4f42-5160-bc07-58eda7573820", "Philip B Vito"],
  ["6e1925d1-7da1-5f7d-9fd8-3604d9577331", "Angelo Vitti"],
  ["b451a6c1-53c5-5e02-8f48-6ed0ca6f3803", "Aniceto Vitti"],
  ["bac268dd-0fce-5194-973b-0cf0b5909894", "Emile Vivequin"],
  ["ad5f4b1c-11ea-5da7-9665-c044e9fc75fa", "Neal B Vivian"],
  ["d083cf01-0633-5619-a6bc-13aa1c97805e", "Valentine P.T. Viviani"],
  ["7e952688-bb4b-514b-8718-5af15091729d", "William F Viviani"],
  ["6cef9a04-a514-502e-a9a2-c59defaa7c09", "Emile Viviquin"],
  ["effb65bc-b499-5652-8262-98f9eacce1cc", "Peter L Vlahakes"],
  ["9fa853a2-a40f-58ff-bed4-4576bd9dedb9", "Steve P Vlahovich"],
  ["e6d791d1-e3ef-5232-a6e9-9a96daa89bef", "Floyd Tomas Vlasic"],
] as const;

async function publicPerson(request: APIRequestContext, id: string, name: string) {
  const first = name[0].toLowerCase();
  const shard = /^[a-z]$/.test(first) ? first : "other";
  const response = await request.get(`./data/people/${shard}.json`);
  expect(response.ok()).toBeTruthy();
  return (await response.json()).find((item: { person_id: string }) => item.person_id === id);
}

test("Batch 987 publishes all 23 audited people with terminal outcomes", async ({ page }) => {
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

test("reviewed Army bridges publish broad categories, not named employers", async ({ request }) => {
  const expected = [
    ["c986edb4-91c5-53df-aa84-a04979f76455", "Domonic Virdo", "machine-shop or related occupation, not elsewhere classified", "employment"],
    ["473f8b49-bf87-5cf5-b4ff-d92ff3fc6e4f", "Antonio Visini", "electrician", "employment"],
    ["9b76b69f-fc08-5c07-acea-22eb719b6b64", "Samuel Vitale", "chauffeur or driver of a bus, taxi, truck, or tractor", "employment"],
    ["f9a41038-73a4-58de-b790-244e10a28354", "Domenick P Viterisi", "student", "student"],
    ["b451a6c1-53c5-5e02-8f48-6ed0ca6f3803", "Aniceto Vitti", "general farm hand", "employment"],
  ] as const;
  for (const [id, name, occupation, relationship] of expected) {
    const person = await publicPerson(request, id, name);
    expect(person).toMatchObject({ identity_status: "high_confidence", research_status: "occupation_only_found" });
    expect(person.last_civilian_pre_service).toHaveLength(0);
    expect(person.other_pre_oss_affiliations).toEqual(expect.arrayContaining([
      expect.objectContaining({
        canonical_organization: null,
        occupation,
        relationship_type: relationship,
        temporal_basis: "strongly_date_bounded",
        claim_confidence: "medium",
        publication_status: "publish_qualified",
      }),
    ]));
  }
});

test("Visini rows stay separate inside one visible duplicate-review group", async ({ request }) => {
  const anthony = await publicPerson(request, profiles[3][0], profiles[3][1]);
  const antonio = await publicPerson(request, profiles[4][0], profiles[4][1]);
  expect(anthony.person_id).not.toBe(antonio.person_id);
  expect(anthony.possible_duplicate_group).toBe(antonio.possible_duplicate_group);
  expect(anthony).toMatchObject({ identity_status: "probable", research_status: "requires_archival_review" });
  expect(antonio).toMatchObject({ identity_status: "high_confidence", research_status: "occupation_only_found" });
  expect(anthony.last_civilian_pre_service).toHaveLength(0);
  expect(antonio.last_civilian_pre_service).toHaveLength(0);
});

test("Vivequin and Viviquin remain separate ambiguous rows without affiliations", async ({ request }) => {
  const vivequin = await publicPerson(request, profiles[15][0], profiles[15][1]);
  const viviquin = await publicPerson(request, profiles[19][0], profiles[19][1]);
  expect(vivequin.person_id).not.toBe(viviquin.person_id);
  expect(vivequin.possible_duplicate_group).toBe(viviquin.possible_duplicate_group);
  for (const person of [vivequin, viviquin]) {
    expect(person).toMatchObject({ identity_status: "ambiguous", research_status: "requires_archival_review" });
    expect(person.immediate_pre_oss_affiliations).toHaveLength(0);
    expect(person.last_civilian_pre_service).toHaveLength(0);
    expect(person.other_pre_oss_affiliations).toHaveLength(0);
  }
});

test("Viviani to Vivian remains a qualified British military lead", async ({ request }) => {
  const person = await publicPerson(request, profiles[17][0], profiles[17][1]);
  expect(person).toMatchObject({
    identity_status: "probable",
    research_status: "requires_archival_review",
    personnel_category: "foreign_or_allied_military_personnel",
    commissioned_officer: true,
  });
  expect(person.last_civilian_pre_service).toHaveLength(0);
  expect(person.other_pre_oss_affiliations).toEqual(expect.arrayContaining([
    expect.objectContaining({
      canonical_organization: "British Army",
      relationship_type: "military_assignment",
      temporal_basis: "documented_prewar",
      identity_confidence: "probable",
      claim_confidence: "medium",
      publication_status: "publish_qualified",
    }),
  ]));
});

test("Batch 987 evidence excludes secrets, full identifiers and raw bulk records", () => {
  expect(evidence).not.toMatch(/"serial_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toMatch(/"service_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toContain("NARA_API_KEY");
  expect(evidence).not.toContain("x-api-key");
  expect(evidence).not.toContain("candidate_identifier");
  expect(evidence).not.toContain("bulk_record_ordinal");
  expect(evidence).not.toMatch(/RA\d{8}/);
});

test("Batch 987 publishes exact coverage counters", async ({ request }) => {
  const response = await request.get("./data/stats.json");
  expect(response.ok()).toBeTruthy();
  expect(await response.json()).toMatchObject({
    source_rows: 23_978,
    person_entities: 23_936,
    possible_duplicate_groups: 674,
    research_attempted_people: 15_633,
    verified_affiliation_people: 1_127,
    verified_employer_people: 508,
    archival_review_assessed_people: 14_109,
    published_claims: 9_983,
    public_sources: 6_436,
  });
});
