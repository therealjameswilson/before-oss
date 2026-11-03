import fs from "node:fs";
import { expect, test } from "@playwright/test";
import type { APIRequestContext } from "@playwright/test";

const evidence = fs.readFileSync(
  new URL(
    "../../research/evidence-page490-walters-to-warburton-review_batch-999_2026-11-03.json",
    import.meta.url,
  ),
  "utf8",
);

const profiles = [
  ["11146615-3f52-5ae6-9119-ecc165802b78", "Robert E Walters"],
  ["74ab917d-f2ab-5d2f-bf4f-59055a55da57", "Thelma Walters"],
  ["1141d8de-a8d3-5aaf-b779-8b84ec4cf1b0", "Curt Waltheim"],
  ["9f35a8cd-f1b4-52c6-86b4-714c202bf405", "Alan T Walther"],
  ["996f75ec-4fac-55f6-b7bf-fa4f0ddb43a7", "John J Walthers"],
  ["35002c15-38b4-5f5e-8713-b0b226926dd0", "Daniel W Walton"],
  ["403d1c63-8193-5f2f-a549-5f71c37c1f71", "Gladys E Walton"],
  ["b23d9b76-1987-537d-b0bf-89c43d458860", "Lewis B Walton"],
  ["2bfe7baf-a5df-5c11-8fcd-d8f5a4146430", "Marion C Walton"],
  ["a74ca522-ca4d-5924-a8dc-ed3382ee190f", "Wilson W Waltz"],
  ["491e9892-9c66-5c7b-85a8-276ff02d464d", "Joseph A Walukinas"],
  ["e11cbc37-42b3-5a65-8657-cdf1ac337f83", "Leonard Walz"],
  ["fae415ae-efc6-5102-bd9c-b6abba49fa52", "Robert E Wampler"],
  ["38cb516e-118d-5644-b837-9d45de5ea917", "Kenneth Wanamaker"],
  ["9ab444b5-ff20-5e15-9848-43ddb04202cd", "Rafael Wand"],
  ["13428c39-15ea-5c58-bdb9-dfa9089a968e", "Edward W Wank"],
  ["53ff2ff5-0e2d-5e07-b144-6fa3393829ca", "Lucien H Wante"],
  ["140ae430-6d2f-51ee-9f80-9f223b4e6aa2", "John C Wantland"],
  ["da9f2b1c-e14b-507e-8a85-79946acc3477", "Newton R Wantland"],
  ["3dd93a91-632c-54b9-9dee-7171a731a6c7", "James Wanveer"],
  ["83703277-d84d-5429-88c6-e13b0ef7fdbd", "Harry F Wanvig"],
  ["5e7d4837-9102-5424-bdf0-90556c450648", "Douglas Waples"],
  ["c4243e64-49ca-5166-8354-37b415fea9cf", "John H Warburton"],
] as const;

async function publicPerson(request: APIRequestContext, id: string, name: string) {
  const first = name[0].toLowerCase();
  const shard = /^[a-z]$/.test(first) ? first : "other";
  const response = await request.get(`./data/people/${shard}.json`);
  expect(response.ok()).toBeTruthy();
  return (await response.json()).find((item: { person_id: string }) => item.person_id === id);
}

test("Batch 999 publishes all 23 audited people with terminal outcomes", async ({ page }) => {
  for (const [id, name] of profiles) {
    await page.goto(`./people/${id}/`);
    await expect(page.getByRole("heading", { name, level: 1 })).toBeVisible();
    const main = page.locator("main");
    await expect(main).not.toContainText("not started");
    await expect(main).not.toContainText("in progress");
    await expect(main).not.toContainText(/\b[ORW]-?\d{5,9}\b/);
  }
});

test("five Army bridges publish only qualified broad occupations", async ({ request }) => {
  const expected = new Map([
    [profiles[3][0], "draftsman"],
    [profiles[5][0], "general farmer"],
    [profiles[14][0], "textile-products-fabrication occupation, not elsewhere classified"],
    [profiles[18][0], "mechanic or repairman, not elsewhere classified"],
    [profiles[22][0], "filling-station or parking-lot attendant"],
  ]);
  for (const [id, occupation] of expected) {
    const name = profiles.find(([personId]) => personId === id)![1];
    const person = await publicPerson(request, id, name);
    expect(person).toMatchObject({
      identity_status: "confirmed",
      personnel_category: "enlisted_army_personnel",
      commissioned_officer: false,
      research_status: "occupation_only_found",
    });
    expect(person.last_civilian_pre_service).toHaveLength(0);
    expect(person.immediate_pre_oss_affiliations).toHaveLength(0);
    expect(person.other_pre_oss_affiliations).toEqual([
      expect.objectContaining({
        canonical_organization: null,
        occupation,
        relationship_type: "unknown",
        claim_confidence: "medium",
        publication_status: "publish_qualified",
      }),
    ]);
  }
});

test("residual code 999 supports identity only", async ({ request }) => {
  for (const index of [9, 13] as const) {
    const person = await publicPerson(request, profiles[index][0], profiles[index][1]);
    expect(person).toMatchObject({
      identity_status: "confirmed",
      personnel_category: "enlisted_army_personnel",
      commissioned_officer: false,
      research_status: "requires_archival_review",
    });
    expect(person.immediate_pre_oss_affiliations).toHaveLength(0);
    expect(person.last_civilian_pre_service).toHaveLength(0);
    expect(person.other_pre_oss_affiliations).toHaveLength(0);
    expect(person.claims).toHaveLength(1);
    expect(person.claims[0]).toMatchObject({ claim_type: "identity", claim_confidence: "confirmed" });
  }
});

test("Robert Wampler is an officer identity match without an invented pre-OSS employer", async ({ request }) => {
  const person = await publicPerson(request, profiles[12][0], profiles[12][1]);
  expect(person).toMatchObject({
    identity_status: "high_confidence",
    personnel_category: "commissioned_army_officer",
    commissioned_officer: true,
    research_status: "requires_archival_review",
  });
  expect(person.immediate_pre_oss_affiliations).toHaveLength(0);
  expect(person.last_civilian_pre_service).toHaveLength(0);
  expect(person.other_pre_oss_affiliations).toHaveLength(0);
  expect(person.claims).toEqual([
    expect.objectContaining({ claim_type: "identity", claim_confidence: "high" }),
  ]);
});

test("Douglas Waples publishes bounded University of Chicago employment", async ({ request }) => {
  const person = await publicPerson(request, profiles[21][0], profiles[21][1]);
  expect(person).toMatchObject({
    identity_status: "high_confidence",
    research_status: "documented_prewar_employer_found",
  });
  expect(person.immediate_pre_oss_affiliations).toHaveLength(0);
  expect(person.last_civilian_pre_service).toHaveLength(0);
  expect(person.other_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      canonical_organization: "University of Chicago",
      role_title: "professor",
      relationship_type: "employment",
      temporal_basis: "documented_prewar",
      claim_confidence: "high",
      publication_status: "published",
    }),
  ]);
  expect(person.claims).toHaveLength(2);
});

test("Harry Wanvig remains probable and Joseph Walukinas remains conflicting", async ({ request }) => {
  const wanvig = await publicPerson(request, profiles[20][0], profiles[20][1]);
  expect(wanvig).toMatchObject({
    identity_status: "probable",
    personnel_category: "commissioned_army_officer",
    commissioned_officer: true,
    research_status: "requires_archival_review",
  });
  expect(wanvig.other_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      canonical_organization: "309th Field Artillery Regiment",
      relationship_type: "military_assignment",
      identity_confidence: "probable",
      claim_confidence: "medium",
      publication_status: "publish_qualified",
    }),
  ]);

  const walukinas = await publicPerson(request, profiles[10][0], profiles[10][1]);
  expect(walukinas).toMatchObject({
    identity_status: "conflicting",
    research_status: "conflicting_sources",
  });
  expect(walukinas.other_pre_oss_affiliations).toHaveLength(0);
  expect(walukinas.claims).toEqual([
    expect.objectContaining({ claim_type: "identity", claim_confidence: "conflicting" }),
  ]);
});

test("the original Curt Waltheim note remains recoverable", async ({ request }) => {
  const person = await publicPerson(request, profiles[2][0], profiles[2][1]);
  expect(person).toMatchObject({
    identity_status: "unresolved",
    research_status: "requires_archival_review",
  });
  expect(person.source_records[0]).toMatchObject({
    indexed_last_name: "Waltheim",
    indexed_first_name: "Curt",
    notes_as_indexed: "? Move t",
    box: "814",
  });
});

test("Batch 999 evidence excludes secrets, identifiers, and raw bulk records", () => {
  expect(evidence).not.toMatch(/"serial_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toMatch(/"service_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toContain("NARA_API_KEY");
  expect(evidence).not.toContain("x-api-key");
  expect(evidence).not.toContain("candidate_identifier");
  expect(evidence).not.toContain("bulk_record_ordinal");
  expect(evidence).not.toMatch(/\b[ORW]-?\d{5,9}\b/);
});

test("Batch 999 public claims retain inspectable source citations", async ({ request }) => {
  for (const index of [3, 5, 10, 12, 14, 18, 20, 21, 22] as const) {
    const person = await publicPerson(request, profiles[index][0], profiles[index][1]);
    expect(person.claims.length).toBeGreaterThan(0);
    for (const item of person.claims) {
      expect(item.sources.length).toBeGreaterThan(0);
      for (const link of item.sources) {
        expect(link.source.stable_url || link.source.archival_identifier).toBeTruthy();
        const excerpt = link.excerpt_override ?? item.evidence_excerpt ?? "";
        expect(excerpt.trim() ? excerpt.trim().split(/\s+/).length : 0).toBeLessThanOrEqual(25);
      }
    }
  }
});

test("Batch 999 publishes exact coverage counters", async ({ request }) => {
  const response = await request.get("./data/stats.json");
  expect(response.ok()).toBeTruthy();
  expect(await response.json()).toMatchObject({
    source_rows: 23_978,
    person_entities: 23_936,
    possible_duplicate_groups: 679,
    research_attempted_people: 15_909,
    verified_affiliation_people: 1_146,
    verified_employer_people: 519,
    archival_review_assessed_people: 14_384,
    published_claims: 10_184,
    public_sources: 6_533,
  });
});
