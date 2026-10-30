import fs from "node:fs";
import { expect, test } from "@playwright/test";
import type { APIRequestContext } from "@playwright/test";

const evidence = fs.readFileSync(
  new URL(
    "../../research/evidence-page484-ovito-vlasic-to-lou-bernard-voigt-review_batch-988_2026-10-30.json",
    import.meta.url,
  ),
  "utf8",
);

const profiles = [
  ["b75eda33-b0e4-563e-abf0-a49867f93cf0", "Ovito T Vlasic"],
  ["faa6c43f-2007-5a7d-a45b-a47eb5e47d23", "Charlie Vlkojan Jr."],
  ["5e7446c1-b779-56bd-aba6-52dab666613a", "Stephen F Vlodek"],
  ["84e8bec8-11d8-5218-88e1-5137c23f35db", "John C Vlossak"],
  ["449eed30-cb35-5c10-ba63-0768a85eaa71", "Sylvester J Vodde"],
  ["3dec0c62-6dbb-58b3-ac01-7efa2beb3ee2", "Josephine G Vodika"],
  ["78470cf4-0695-53b5-ac63-0c09fa824a38", "Oliver B Vodrey"],
  ["ebae0b04-b7a7-5139-887e-b226723176ec", "Vance V Vogal"],
  ["0f604abf-fcad-532b-ac0e-716cadbca4c8", "Emmett Vogan Jr."],
  ["e9ff643a-98e9-5c57-a6f2-98cfbbaf4ed3", "Noel A Voge"],
  ["09afd35f-18d3-5e71-a594-635bc5f9bd43", "Edward F Vogel"],
  ["2930308b-327f-59b2-9a3a-3f93ec9d3623", "Frank S Vogel"],
  ["b27073b5-6d3a-5e5f-ae33-76aa7bd959d4", "Robert F Vogel"],
  ["aa961d2a-055b-546e-9ec4-e49f5a22ab40", "Vance V Vogel"],
  ["d3ad13a4-8e99-51d0-9333-d7b67dd0d847", "Edgar Voges"],
  ["a6682a72-96bc-5cae-927f-2f1f8c742c36", "Edgar Voges"],
  ["4560d7c3-f72b-5ffd-be8c-e00d2ab655b8", "Bert D Vogt"],
  ["56518591-c05b-5bd1-8d71-00382943dda8", "George R Vogt"],
  ["60985369-08f8-58e4-9568-20d77cfb57b1", "Lawrence R Vogt"],
  ["0c543385-954c-5510-8e6c-b73d0f990c1b", "Robert J Vogt"],
  ["d9d8ebc6-c7f6-57ea-b344-5a47578fc492", "Edgar H Voight"],
  ["1186b7ea-8636-5337-8d06-89c74a5ae929", "John P Voight"],
  ["01f9144e-eb54-5b9e-877e-5b452a804ee7", "Lou Bernard Voigt"],
] as const;

async function publicPerson(request: APIRequestContext, id: string, name: string) {
  const first = name[0].toLowerCase();
  const shard = /^[a-z]$/.test(first) ? first : "other";
  const response = await request.get(`./data/people/${shard}.json`);
  expect(response.ok()).toBeTruthy();
  return (await response.json()).find((item: { person_id: string }) => item.person_id === id);
}

test("Batch 988 publishes all 23 audited people with terminal outcomes", async ({ page }) => {
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
    ["84e8bec8-11d8-5218-88e1-5137c23f35db", "John C Vlossak", "actor or actress", "employment"],
    ["449eed30-cb35-5c10-ba63-0768a85eaa71", "Sylvester J Vodde", "lineman or serviceman in telegraph, telephone, or power work", "employment"],
    ["e9ff643a-98e9-5c57-a6f2-98cfbbaf4ed3", "Noel A Voge", "warehousing, storekeeping, handling, loading, unloading, or related occupation", "employment"],
    ["09afd35f-18d3-5e71-a594-635bc5f9bd43", "Edward F Vogel", "student", "student"],
    ["2930308b-327f-59b2-9a3a-3f93ec9d3623", "Frank S Vogel", "retail manager", "employment"],
    ["b27073b5-6d3a-5e5f-ae33-76aa7bd959d4", "Robert F Vogel", "cook, except for a private family", "employment"],
    ["d3ad13a4-8e99-51d0-9333-d7b67dd0d847", "Edgar Voges", "chauffeur or driver of a bus, taxi, truck, or tractor", "employment"],
    ["60985369-08f8-58e4-9568-20d77cfb57b1", "Lawrence R Vogt", "decorator or window dresser", "employment"],
    ["0c543385-954c-5510-8e6c-b73d0f990c1b", "Robert J Vogt", "elevator operator", "employment"],
  ] as const;
  for (const [id, name, occupation, relationship] of expected) {
    const person = await publicPerson(request, id, name);
    expect(person).toMatchObject({ identity_status: "high_confidence", research_status: "occupation_only_found" });
    expect(person.immediate_pre_oss_affiliations).toHaveLength(0);
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

test("Charlie Vlkojan keeps the identity bridge but does not expose undefined code 590", async ({ request }) => {
  const person = await publicPerson(request, profiles[1][0], profiles[1][1]);
  expect(person).toMatchObject({ identity_status: "high_confidence", research_status: "requires_archival_review" });
  expect(person.immediate_pre_oss_affiliations).toHaveLength(0);
  expect(person.last_civilian_pre_service).toHaveLength(0);
  expect(person.other_pre_oss_affiliations).toHaveLength(0);
  expect(JSON.stringify(person)).not.toContain('"occupation":"590"');
});

test("two Edgar Voges rows stay separate inside one review group", async ({ request }) => {
  const numbered = await publicPerson(request, profiles[14][0], profiles[14][1]);
  const unnumbered = await publicPerson(request, profiles[15][0], profiles[15][1]);
  expect(numbered.person_id).not.toBe(unnumbered.person_id);
  expect(numbered.possible_duplicate_group).toBe(unnumbered.possible_duplicate_group);
  expect(numbered).toMatchObject({ identity_status: "high_confidence", research_status: "occupation_only_found" });
  expect(unnumbered).toMatchObject({ identity_status: "ambiguous", research_status: "requires_archival_review" });
  expect(unnumbered.immediate_pre_oss_affiliations).toHaveLength(0);
  expect(unnumbered.last_civilian_pre_service).toHaveLength(0);
  expect(unnumbered.other_pre_oss_affiliations).toHaveLength(0);
});

test("Vance Vogal and Vogel rows remain separate ambiguous candidates", async ({ request }) => {
  const vogal = await publicPerson(request, profiles[7][0], profiles[7][1]);
  const vogel = await publicPerson(request, profiles[13][0], profiles[13][1]);
  expect(vogal.person_id).not.toBe(vogel.person_id);
  expect(vogal.possible_duplicate_group).toBe(vogel.possible_duplicate_group);
  for (const person of [vogal, vogel]) {
    expect(person).toMatchObject({ identity_status: "ambiguous", research_status: "requires_archival_review" });
    expect(person.immediate_pre_oss_affiliations).toHaveLength(0);
    expect(person.last_civilian_pre_service).toHaveLength(0);
    expect(person.other_pre_oss_affiliations).toHaveLength(0);
  }
});

test("Bert Vogt preserves the shared-identifier conflict without an occupation claim", async ({ request }) => {
  const person = await publicPerson(request, profiles[16][0], profiles[16][1]);
  expect(person).toMatchObject({ identity_status: "conflicting", research_status: "conflicting_sources" });
  expect(person.possible_duplicate_group).toMatch(/^duplicate-/);
  expect(person.immediate_pre_oss_affiliations).toHaveLength(0);
  expect(person.last_civilian_pre_service).toHaveLength(0);
  expect(person.other_pre_oss_affiliations).toHaveLength(0);
});

test("Lou Voigt separates immediate, last-civilian and earlier employment", async ({ request }) => {
  const person = await publicPerson(request, profiles[22][0], profiles[22][1]);
  expect(person).toMatchObject({
    identity_status: "high_confidence",
    research_status: "verified_employer_found",
    personnel_category: "civilian_professional_or_administrative_grade",
  });
  expect(person.immediate_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      canonical_organization: "Skidmore, Owings & Merrill",
      role_title: "site-planning designer for atomic plant installations at Oak Ridge",
      temporal_basis: "strongly_date_bounded",
      claim_confidence: "high",
      publication_status: "published",
    }),
  ]);
  expect(person.last_civilian_pre_service).toEqual([
    expect.objectContaining({ canonical_organization: "Skidmore, Owings & Merrill" }),
  ]);
  expect(person.other_pre_oss_affiliations).toEqual(expect.arrayContaining([
    expect.objectContaining({
      canonical_organization: "Black Mountain College",
      role_title: "instructor in botany and landscape architecture",
      temporal_basis: "documented_prewar",
      claim_confidence: "high",
    }),
  ]));
  expect(person.claims).toEqual(expect.arrayContaining([
    expect.objectContaining({ claim_type: "immediate_pre_oss_affiliation", claim_confidence: "high" }),
    expect.objectContaining({ claim_type: "last_civilian_pre_service", claim_confidence: "high" }),
    expect.objectContaining({ claim_type: "other_pre_oss_affiliation", claim_confidence: "high" }),
  ]));
});

test("Batch 988 evidence excludes secrets, full identifiers and raw bulk records", () => {
  expect(evidence).not.toMatch(/"serial_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toMatch(/"service_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toContain("NARA_API_KEY");
  expect(evidence).not.toContain("x-api-key");
  expect(evidence).not.toContain("candidate_identifier");
  expect(evidence).not.toContain("bulk_record_ordinal");
  expect(evidence).not.toMatch(/RA\d{8}/);
});

test("Batch 988 publishes exact coverage counters", async ({ request }) => {
  const response = await request.get("./data/stats.json");
  expect(response.ok()).toBeTruthy();
  expect(await response.json()).toMatchObject({
    source_rows: 23_978,
    person_entities: 23_936,
    possible_duplicate_groups: 676,
    research_attempted_people: 15_656,
    verified_affiliation_people: 1_128,
    verified_employer_people: 509,
    archival_review_assessed_people: 14_132,
    published_claims: 10_006,
    public_sources: 6_442,
  });
});
