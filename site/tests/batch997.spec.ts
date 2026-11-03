import fs from "node:fs";
import { expect, test } from "@playwright/test";
import type { APIRequestContext } from "@playwright/test";

const evidence = fs.readFileSync(
  new URL(
    "../../research/evidence-page489-wallace-to-walsh-review_batch-997_2026-11-03.json",
    import.meta.url,
  ),
  "utf8",
);

const profiles = [
  ["8bc4b395-0a4a-533d-a735-d52e8feed49e", "Inovar A Wallace"],
  ["f5761189-b996-54ad-a6de-dad011c891d2", "Jean Browne Wallace"],
  ["e8ffff68-cbe1-5f73-b56c-790384467c03", "John G Wallace"],
  ["495edc87-1bf8-5311-86e9-3908355b8a27", "Lynn de G Wallace"],
  ["edb65626-5c15-5103-9fea-0e6439eefff6", "Marcel H Wallace"],
  ["4dad3b4c-bd4c-5cf6-9c6b-ee05d6bcec26", "Neville M Wallace"],
  ["fbe9b621-0b06-5e77-9a74-25a7d6bd1462", "Owen M Wallace"],
  ["8347189c-b6e2-5bc4-bf45-479125cc7fa4", "Paul J Wallace"],
  ["37fbed5a-c775-5986-8537-5d3426ea809a", "Paul Kimball Wallace"],
  ["3ac25756-5223-543a-80f8-91c0dbe55656", "Robert E Wallace"],
  ["c5fd2f1d-f46c-5c5c-a684-66cfc89a8368", "Sherman L Wallace"],
  ["801f3a93-552c-5231-8fe6-68720b866029", "Warrack Wallace"],
  ["f9a11234-9f48-57d3-a7b2-620e8a6f3dd7", "Maurice Gene Wallen"],
  ["66448181-04d2-5eed-a887-261a5208c333", "Victor Wallen"],
  ["35e24273-0c50-5564-a61d-092f6cc2ff3e", "Clarence V Wallenberg"],
  ["c1248ae4-8088-5b8c-bbb4-a0dccc020cc9", "John Henry Waller"],
  ["4143ff42-e3f0-5646-a2fd-093f584ed0ef", "Mabel Aclydia Waller"],
  ["1142a070-a82f-5a46-8dde-491655534c2e", "Helen Wallin"],
  ["535c2746-7a1a-5209-83f2-8c950010965c", "Jack H Wallin"],
  ["7deac770-4360-589a-9cae-fbaafc42479d", "Sophia A Wallon"],
  ["cc075c6c-f5c1-570a-948a-b6d54e62621b", "Michel Walon"],
  ["a50ca661-582d-5197-a6c7-9720e25ab021", "Ingrid Walot"],
  ["0fd0b591-736e-5627-91d3-5ad3ea455852", "Emily A.T. Walsh"],
] as const;

async function publicPerson(request: APIRequestContext, id: string, name: string) {
  const first = name[0].toLowerCase();
  const shard = /^[a-z]$/.test(first) ? first : "other";
  const response = await request.get(`./data/people/${shard}.json`);
  expect(response.ok()).toBeTruthy();
  return (await response.json()).find((item: { person_id: string }) => item.person_id === id);
}

test("Batch 997 publishes all 23 audited people with terminal outcomes", async ({ page }) => {
  for (const [id, name] of profiles) {
    await page.goto(`./people/${id}/`);
    await expect(page.getByRole("heading", { name, level: 1 })).toBeVisible();
    const main = page.locator("main");
    await expect(main).not.toContainText("not started");
    await expect(main).not.toContainText("in progress");
    await expect(main).not.toContainText(/\b[ORW]-?\d{5,9}\b/);
  }
});

test("five Army bridges publish only qualified occupation categories", async ({ request }) => {
  const expected = new Map([
    [profiles[5][0], "sales clerk"],
    [profiles[6][0], "manufacturing foreman"],
    [profiles[7][0], "general office clerk"],
    [profiles[9][0], "railroad or carshop mechanic or repairman"],
    [profiles[18][0], "general industry clerk"],
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
        relationship_type: "employment",
        claim_confidence: "medium",
        publication_status: "publish_qualified",
      }),
    ]);
  }
});

test("Inovar Wallace retains the name and temporal uncertainty", async ({ request }) => {
  const person = await publicPerson(request, profiles[0][0], profiles[0][1]);
  expect(person).toMatchObject({
    identity_status: "high_confidence",
    research_status: "needs_temporal_review",
    personnel_category: "enlisted_army_personnel",
    commissioned_officer: false,
  });
  expect(person.name_variants).toContain("Ingvar A Wallace");
  expect(person.other_pre_oss_affiliations).toHaveLength(0);
  expect(person.claims).toEqual([
    expect.objectContaining({ claim_type: "identity", claim_confidence: "high" }),
  ]);
  expect(person.next_action).toContain("after OSS dissolution");
});

test("Warrack Wallace publishes distinct last-civilian and earlier oil work", async ({ request }) => {
  const person = await publicPerson(request, profiles[11][0], profiles[11][1]);
  expect(person).toMatchObject({
    identity_status: "high_confidence",
    research_status: "verified_employer_found",
    personnel_category: "commissioned_army_officer",
    commissioned_officer: true,
  });
  expect(person.last_civilian_pre_service).toEqual([
    expect.objectContaining({
      canonical_organization: "Baker & Daniels",
      role_title: "senior partner",
      occupation: "corporate lawyer",
      last_civilian_pre_service: true,
      claim_confidence: "high",
    }),
  ]);
  expect(person.other_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      canonical_organization: "Standard Oil Company (entity unspecified)",
      organization_name_as_found: "Standard Oil Company",
      relationship_type: "employment",
      claim_confidence: "high",
    }),
  ]);
});

test("John Waller publishes the explicit State Department to OSS transition", async ({ request }) => {
  const person = await publicPerson(request, profiles[15][0], profiles[15][1]);
  expect(person).toMatchObject({
    identity_status: "high_confidence",
    research_status: "verified_employer_found",
  });
  expect(person.immediate_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      canonical_organization: "United States Department of State",
      organization_name_as_found: "State Department",
      relationship_type: "government_assignment",
      immediate_pre_oss: true,
      temporal_basis: "explicit_immediate",
      claim_confidence: "high",
    }),
  ]);
  expect(person.last_civilian_pre_service).toHaveLength(0);
});

test("tempting namesakes remain unassigned without a direct bridge", async ({ request }) => {
  for (const index of [1, 8, 17] as const) {
    const person = await publicPerson(request, profiles[index][0], profiles[index][1]);
    expect(person).toMatchObject({
      identity_status: "unresolved",
      research_status: "requires_archival_review",
    });
    expect(person.claims).toHaveLength(0);
    expect(person.last_civilian_pre_service).toHaveLength(0);
    expect(person.immediate_pre_oss_affiliations).toHaveLength(0);
  }
});

test("Michel Walon retains the printed French officer classification", async ({ request }) => {
  const person = await publicPerson(request, profiles[20][0], profiles[20][1]);
  expect(person).toMatchObject({
    identity_status: "unresolved",
    research_status: "requires_archival_review",
    personnel_category: "foreign_or_allied_military_personnel",
    commissioned_officer: true,
    allied_or_foreign_personnel: true,
  });
  expect(person.source_records[0]).toMatchObject({
    rank_as_indexed: "S/Lt.",
    notes_as_indexed: "French",
  });
});

test("Batch 997 evidence excludes secrets, identifiers, and raw bulk records", () => {
  expect(evidence).not.toMatch(/"serial_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toMatch(/"service_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toContain("NARA_API_KEY");
  expect(evidence).not.toContain("x-api-key");
  expect(evidence).not.toContain("candidate_identifier");
  expect(evidence).not.toContain("bulk_record_ordinal");
  expect(evidence).not.toMatch(/\b[ORW]-?\d{5,9}\b/);
});

test("Batch 997 public claims retain inspectable source citations", async ({ request }) => {
  for (const index of [0, 5, 6, 7, 9, 11, 15, 18] as const) {
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

test("the oil-company category now includes Warrack Wallace", async ({ page }) => {
  await page.goto("./oil-companies/");
  await expect(page.getByRole("link", { name: "Warrack Wallace" })).toBeVisible();
  await expect(page.getByRole("link", { name: "Standard Oil Company (entity unspecified)" })).toBeVisible();
});

test("Batch 997 publishes exact coverage counters", async ({ request }) => {
  const response = await request.get("./data/stats.json");
  expect(response.ok()).toBeTruthy();
  expect(await response.json()).toMatchObject({
    source_rows: 23_978,
    person_entities: 23_936,
    possible_duplicate_groups: 679,
    research_attempted_people: 15_863,
    verified_affiliation_people: 1_145,
    verified_employer_people: 518,
    archival_review_assessed_people: 14_338,
    published_claims: 10_160,
    public_sources: 6_520,
  });
});
