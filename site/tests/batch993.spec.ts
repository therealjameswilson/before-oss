import fs from "node:fs";
import { expect, test } from "@playwright/test";
import type { APIRequestContext } from "@playwright/test";

const evidence = fs.readFileSync(
  new URL(
    "../../research/evidence-page487-waffle-to-waite-review_batch-993_2026-11-03.json",
    import.meta.url,
  ),
  "utf8",
);

const profiles = [
  ["c9d24217-4daf-54c1-a360-7bbf1130d951", "Albert H Waffle"],
  ["aaf02551-6b0f-5358-ac5b-09d04eb45d59", "Siegfried Wagener"],
  ["f823b41c-13ff-5735-8b5c-21117a39475e", "Stanley S Wager"],
  ["74f95699-9431-5381-bd4f-f58c95d8e856", "David E Waggoner"],
  ["1ff34c99-84d5-539b-a946-635ee8d7b323", "Albert Wagner"],
  ["a83ac3b9-2f7f-59b1-a87b-9800dc64f475", "Allan Wagner"],
  ["c902112c-4321-5c6d-bfc8-e1d5f69fd0db", "Allen Oscar Wagner"],
  ["4c8b55c7-eb17-5490-893c-32f05e62e8de", "Bernard G Wagner"],
  ["e05bbae5-7976-5f5e-90df-21c66096b8da", "Charles B Wagner"],
  ["614f3952-4274-5c62-8bc4-a44b1b82abe3", "Harry Eugene Wagner"],
  ["f38438b9-058a-5208-95c5-616f37265236", "Herta Gloria Wagner"],
  ["8663f075-bcc3-50b2-9de0-e9fdfac8a682", "Lloyd A Wagner"],
  ["8e2548e9-16a4-5e4d-ac17-2d14a40834ae", "Ludwig Anton Wagner"],
  ["02ed2ba0-c9e3-56cf-81c7-8142e8da4f2a", "Paul A Wagner"],
  ["66344d4e-7120-5bca-9cdb-259bab783be8", "Richard D Wagner"],
  ["917d8c7a-0983-5730-934e-314ff181e146", "Shirley Carol Wagner"],
  ["44f08118-cc69-5e8c-85b5-d0555cd2ae14", "William E Wagner"],
  ["146c48fa-7fb8-5a02-adfe-4938e195d561", "Joseph Wago Jr."],
  ["80c9aa4f-6fe5-5fe4-b790-12ed4fb6f446", "Florence E Wagoner"],
  ["1485beb4-f02c-5159-9abe-7b10a9fdae8c", "David R Wahl"],
  ["7717ded8-388f-5cf9-8dea-cbc41c69f1c7", "Harvey W Wainwright"],
  ["55ab49e4-7b19-5746-9576-de7f1c8cc8d4", "Stuyvesant Wainwright"],
  ["f26f02bd-08ba-58d2-b7a7-13c6b1f7f485", "James P Waite"],
] as const;

async function publicPerson(request: APIRequestContext, id: string, name: string) {
  const first = name[0].toLowerCase();
  const shard = /^[a-z]$/.test(first) ? first : "other";
  const response = await request.get(`./data/people/${shard}.json`);
  expect(response.ok()).toBeTruthy();
  return (await response.json()).find((item: { person_id: string }) => item.person_id === id);
}

test("Batch 993 publishes all 23 audited people with terminal outcomes", async ({ page }) => {
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

test("Wagener publishes a qualified Chicago Times pathway and separate KFEL work", async ({ request }) => {
  const person = await publicPerson(request, profiles[1][0], profiles[1][1]);
  expect(person).toMatchObject({
    identity_status: "high_confidence",
    research_status: "documented_prewar_employer_found",
    personnel_category: "civilian_professional_or_administrative_grade",
  });
  expect(person.immediate_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      canonical_organization: "Chicago Daily Times",
      historical_organization: "Chicago Times",
      relationship_type: "employment",
      temporal_basis: "probable_immediate",
      claim_confidence: "medium",
      publication_status: "publish_qualified",
    }),
  ]);
  expect(person.last_civilian_pre_service).toHaveLength(1);
  expect(person.other_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      canonical_organization: "KFEL",
      relationship_type: "professional_affiliation",
      temporal_basis: "documented_prewar",
    }),
  ]);
});

test("Stuyvesant Wainwright separates Yale student status from the Army pathway", async ({ request }) => {
  const person = await publicPerson(request, profiles[21][0], profiles[21][1]);
  expect(person).toMatchObject({
    identity_status: "high_confidence",
    research_status: "completed",
    personnel_category: "commissioned_army_officer",
    commissioned_officer: true,
  });
  expect(person.immediate_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      canonical_organization: "United States Army",
      relationship_type: "military_assignment",
      claim_confidence: "high",
      publication_status: "published",
    }),
  ]);
  expect(person.last_civilian_pre_service).toHaveLength(0);
  expect(person.other_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      canonical_organization: "Yale Law School",
      relationship_type: "student",
      claim_confidence: "high",
    }),
  ]);
});

test("Harvey Wainright keeps the documented spelling and generic student status", async ({ request }) => {
  const person = await publicPerson(request, profiles[20][0], profiles[20][1]);
  expect(person).toMatchObject({
    identity_status: "confirmed",
    research_status: "occupation_only_found",
    personnel_category: "enlisted_army_personnel",
    commissioned_officer: false,
  });
  expect(person.name_variants).toContain("Harvey W Wainright");
  expect(person.other_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      canonical_organization: null,
      occupation: "student",
      relationship_type: "student",
      claim_confidence: "medium",
    }),
  ]);
});

test("Army categories stay qualified and post-OSS entries remain identity-only", async ({ request }) => {
  const albert = await publicPerson(request, profiles[4][0], profiles[4][1]);
  expect(albert.other_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      canonical_organization: null,
      occupation: "farm hands, general farms",
      relationship_type: "employment",
      claim_confidence: "medium",
      publication_status: "publish_qualified",
    }),
  ]);
  expect(albert.last_civilian_pre_service).toHaveLength(0);

  for (const index of [14, 16] as const) {
    const person = await publicPerson(request, profiles[index][0], profiles[index][1]);
    expect(person).toMatchObject({
      identity_status: "confirmed",
      research_status: "requires_archival_review",
      personnel_category: "enlisted_army_personnel",
    });
    expect(person.immediate_pre_oss_affiliations).toHaveLength(0);
    expect(person.last_civilian_pre_service).toHaveLength(0);
    expect(person.other_pre_oss_affiliations).toHaveLength(0);
    expect(person.claims).toEqual([
      expect.objectContaining({ claim_type: "identity", claim_confidence: "confirmed" }),
    ]);
  }
});

test("Ludwig Wagner remains a probable identity with qualified earlier roles", async ({ request }) => {
  const person = await publicPerson(request, profiles[12][0], profiles[12][1]);
  expect(person).toMatchObject({
    identity_status: "probable",
    research_status: "documented_prewar_employer_found",
  });
  expect(person.immediate_pre_oss_affiliations).toHaveLength(0);
  expect(person.last_civilian_pre_service).toHaveLength(0);
  expect(person.other_pre_oss_affiliations).toEqual(expect.arrayContaining([
    expect.objectContaining({
      canonical_organization: "Das Kleine Blatt",
      relationship_type: "employment",
      temporal_basis: "documented_prewar",
      claim_confidence: "medium",
    }),
    expect.objectContaining({
      canonical_organization: "Assembly for a Democratic Austrian Republic",
      relationship_type: "professional_affiliation",
      temporal_basis: "temporal_relation_uncertain",
    }),
  ]));
});

test("unresolved Batch 993 people retain empty claims and archival guidance", async ({ request }) => {
  for (const index of [0, 3, 5, 6, 7, 8, 9, 10, 15, 17, 18, 19, 22] as const) {
    const person = await publicPerson(request, profiles[index][0], profiles[index][1]);
    expect(person).toMatchObject({
      identity_status: "unresolved",
      research_status: "requires_archival_review",
    });
    expect(person.immediate_pre_oss_affiliations).toHaveLength(0);
    expect(person.last_civilian_pre_service).toHaveLength(0);
    expect(person.other_pre_oss_affiliations).toHaveLength(0);
    expect(person.claims).toHaveLength(0);
    expect(person.archival_file.review_priority).toBe("high");
  }
});

test("Batch 993 evidence excludes secrets, full identifiers and raw bulk records", () => {
  expect(evidence).not.toMatch(/"serial_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toMatch(/"service_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toContain("NARA_API_KEY");
  expect(evidence).not.toContain("x-api-key");
  expect(evidence).not.toContain("candidate_identifier");
  expect(evidence).not.toContain("bulk_record_ordinal");
  expect(evidence).not.toMatch(/RA\d{8}/);
});

test("Batch 993 public claims retain inspectable source citations", async ({ request }) => {
  for (const index of [1, 2, 4, 11, 12, 13, 14, 16, 20, 21] as const) {
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

test("Batch 993 publishes exact coverage counters", async ({ request }) => {
  const response = await request.get("./data/stats.json");
  expect(response.ok()).toBeTruthy();
  expect(await response.json()).toMatchObject({
    source_rows: 23_978,
    person_entities: 23_936,
    possible_duplicate_groups: 679,
    research_attempted_people: 15_771,
    verified_affiliation_people: 1_139,
    verified_employer_people: 516,
    archival_review_assessed_people: 14_246,
    published_claims: 10_097,
    public_sources: 6_496,
  });
});
