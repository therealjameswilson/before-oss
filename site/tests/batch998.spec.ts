import fs from "node:fs";
import { expect, test } from "@playwright/test";
import type { APIRequestContext } from "@playwright/test";

const evidence = fs.readFileSync(
  new URL(
    "../../research/evidence-page489-walsh-to-walters-review_batch-998_2026-11-03.json",
    import.meta.url,
  ),
  "utf8",
);

const profiles = [
  ["7cd40e3d-ac07-53f3-8b80-fdb080abceaa", "James B Walsh"],
  ["772b3d25-d931-5153-98fe-a1ee4520f0ab", "James D Walsh"],
  ["f638258e-9f5c-5f06-99b3-74ef48e97b12", "John P Walsh"],
  ["6b456d9c-a880-5fd9-9e5d-da6b29010d3a", "Louis A Walsh Jr."],
  ["d15a6330-2faf-5646-89b2-5d920fbca282", "Lucille B Walsh"],
  ["64fe3e00-3f9e-5099-bbd1-9dabcbf2927f", "Margaret E Walsh"],
  ["e797ac78-524c-56b1-b3b6-112cdc16ec6e", "Matilda R Walsh"],
  ["14cc594d-8688-582b-a27c-15abc92eb2e4", "Richard L Walsh"],
  ["43acb70c-ea97-50c1-99c2-a601293edf7f", "Richard T Walsh"],
  ["dd9f8589-bfab-5ccf-b508-b50229125541", "Rutherford T Walsh"],
  ["2e043a99-db2d-5b34-83f7-37b9ae5caef8", "Thomas J Walsh Jr."],
  ["642c272e-ce42-5107-af8b-10083c4c9895", "William B Walsh"],
  ["669746fa-822a-5727-8db0-712f2e89e03e", "William F Walsh"],
  ["5fc300b8-b79a-51a9-847e-374fb4c46b27", "Edmond S Walstrum"],
  ["79f14b4c-3d29-58a8-b3eb-2359bc3ce576", "Austin Walter"],
  ["36cb5e40-f961-5f47-88fe-d15c8415e92a", "Billy H Walter"],
  ["8dc18e64-594e-5505-9aef-86095e0fb0e1", "Hugh T Walter"],
  ["bf349e30-514b-547c-96fd-1a4d749e796f", "Martin J Walter"],
  ["a8aa7172-f03d-5a7b-94a3-8a220bbcf319", "Robert B Walter"],
  ["c0daf938-ecef-569c-88d2-562f9ac19b7d", "Carroll R Walters"],
  ["31ef38be-bae9-5e4b-a588-efe6b04a895e", "George T Walters"],
  ["4ab6b5e5-c100-5b80-b0fa-6ed51d0f6b96", "Lawrence T Walters"],
  ["441b8ec5-2fc8-537d-aa45-072503acc264", "Lenore B Walters"],
] as const;

async function publicPerson(request: APIRequestContext, id: string, name: string) {
  const first = name[0].toLowerCase();
  const shard = /^[a-z]$/.test(first) ? first : "other";
  const response = await request.get(`./data/people/${shard}.json`);
  expect(response.ok()).toBeTruthy();
  return (await response.json()).find((item: { person_id: string }) => item.person_id === id);
}

test("Batch 998 publishes all 23 audited people with terminal outcomes", async ({ page }) => {
  for (const [id, name] of profiles) {
    await page.goto(`./people/${id}/`);
    await expect(page.getByRole("heading", { name, level: 1 })).toBeVisible();
    const main = page.locator("main");
    await expect(main).not.toContainText("not started");
    await expect(main).not.toContainText("in progress");
    await expect(main).not.toContainText(/\b[ORW]-?\d{5,9}\b/);
  }
});

test("three Army bridges publish only qualified occupations", async ({ request }) => {
  const expected = new Map([
    [profiles[2][0], "machinist"],
    [profiles[15][0], "chauffeur or driver of a bus, taxi, truck, or tractor"],
    [profiles[19][0], "farm hand on a general farm"],
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

test("officer and Pharmacist's Mate classifications remain distinct", async ({ request }) => {
  for (const index of [3, 9] as const) {
    const person = await publicPerson(request, profiles[index][0], profiles[index][1]);
    expect(person).toMatchObject({
      identity_status: "unresolved",
      personnel_category: "commissioned_army_officer",
      commissioned_officer: true,
      research_status: "requires_archival_review",
    });
  }

  const robert = await publicPerson(request, profiles[18][0], profiles[18][1]);
  expect(robert).toMatchObject({
    identity_status: "unresolved",
    personnel_category: "enlisted_naval_personnel",
    commissioned_officer: false,
    research_status: "requires_archival_review",
  });
  expect(robert.source_records[0]).toMatchObject({
    rank_as_indexed: "PhM 1/c",
    notes_as_indexed: "USNR",
  });
});

test("tempting namesakes remain unassigned without a direct bridge", async ({ request }) => {
  for (const index of [3, 7, 11, 12, 17, 20, 21] as const) {
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

test("Batch 998 evidence excludes secrets, identifiers, and raw bulk records", () => {
  expect(evidence).not.toMatch(/"serial_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toMatch(/"service_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toContain("NARA_API_KEY");
  expect(evidence).not.toContain("x-api-key");
  expect(evidence).not.toContain("candidate_identifier");
  expect(evidence).not.toContain("bulk_record_ordinal");
  expect(evidence).not.toMatch(/\b[ORW]-?\d{5,9}\b/);
});

test("Batch 998 public claims retain inspectable source citations", async ({ request }) => {
  for (const index of [2, 15, 19] as const) {
    const person = await publicPerson(request, profiles[index][0], profiles[index][1]);
    expect(person.claims).toHaveLength(2);
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

test("Batch 998 publishes exact coverage counters", async ({ request }) => {
  const response = await request.get("./data/stats.json");
  expect(response.ok()).toBeTruthy();
  expect(await response.json()).toMatchObject({
    source_rows: 23_978,
    person_entities: 23_936,
    possible_duplicate_groups: 679,
    research_attempted_people: 15_886,
    verified_affiliation_people: 1_145,
    verified_employer_people: 518,
    archival_review_assessed_people: 14_361,
    published_claims: 10_166,
    public_sources: 6_524,
  });
});
