import fs from "node:fs";
import { expect, test } from "@playwright/test";
import type { APIRequestContext } from "@playwright/test";

const evidence = fs.readFileSync(
  new URL(
    "../../research/evidence-page487-waite-to-walk-review_batch-994_2026-11-03.json",
    import.meta.url,
  ),
  "utf8",
);

const profiles = [
  ["30250cf6-d13f-56cc-b743-c639b9120535", "Wilma Isabel Waite"],
  ["0556f56a-4bdf-5b63-af67-4f0629913e00", "Eugene Merse Waith"],
  ["564b2773-158c-57e3-8e81-5895472d7d6d", "Henry S Wakabayashi"],
  ["b0e63804-da34-5d6e-a559-54e8bc27a9d3", "Nancy Wake"],
  ["a45a141e-4073-5be4-a732-a9e38728c831", "Richard P Wakefield"],
  ["dbec9a7e-ed97-59bb-af82-7a3034cbe822", "Arthur Francis Walber"],
  ["a8860eb7-afc7-5794-a905-342135ea2d22", "Charles R Walbert"],
  ["cf66a9eb-8b52-5e53-99d6-83f98ef83371", "George O Walbridge"],
  ["48a25f31-02b3-5b89-bb49-45eb86e6fb6d", "Albert R Walcott"],
  ["626accf6-7831-58fd-8cb0-0f6698ecdee8", "Patrick K.C. Waldberg"],
  ["589acaac-0166-569b-a562-cdf5874509d9", "Carl O Walden"],
  ["3ca1371b-4df5-5f7a-97b6-f5799089d618", "James E Walden"],
  ["aca20a31-be9d-514c-8971-7b753de5cc51", "Herbert F Waldhorn"],
  ["87af7bcc-1d6f-5870-96fa-87a2ab2778e2", "Robert G Waldman"],
  ["aa96ec67-10e8-5dfc-89bb-e8433076bf1d", "Maturin F Waldo"],
  ["cc40a1b0-633e-5130-8d49-07e45610864a", "Phyllis H Waldo"],
  ["64650a84-e326-5e9d-b3f8-c63c1a95202f", "Henry H Waldon"],
  ["502814b4-df38-5b53-ab06-c9ba62dcbc5f", "Arthur Leonard Waldo-Stefans"],
  ["ae88568f-37ac-58d6-9ab8-6db3262e3d81", "Howard T Waldron"],
  ["adc91fda-fcf0-528e-b9e7-03951e0a24e0", "James Waldron"],
  ["3b16058e-9339-533b-a096-14304185c887", "John Waldron"],
  ["9debd6e3-7228-5e20-8735-277c7704a997", "Thomas H Waldron"],
  ["6602744c-b6d8-5828-8a48-e3b5d695f6f7", "Everett G Walk"],
] as const;

async function publicPerson(request: APIRequestContext, id: string, name: string) {
  const first = name[0].toLowerCase();
  const shard = /^[a-z]$/.test(first) ? first : "other";
  const response = await request.get(`./data/people/${shard}.json`);
  expect(response.ok()).toBeTruthy();
  return (await response.json()).find((item: { person_id: string }) => item.person_id === id);
}

test("Batch 994 publishes all 23 audited people with terminal outcomes", async ({ page }) => {
  for (const [id, name] of profiles) {
    await page.goto(`./people/${id}/`);
    await expect(page.getByRole("heading", { name, level: 1 })).toBeVisible();
    const main = page.locator("main");
    await expect(main).not.toContainText("not started");
    await expect(main).not.toContainText("in progress");
    await expect(main).not.toContainText(/\b[ORW]-?\d{5,9}\b/);
  }
});

test("Waith separates verified Yale employment from the Army pathway", async ({ request }) => {
  const person = await publicPerson(request, profiles[1][0], profiles[1][1]);
  expect(person).toMatchObject({
    identity_status: "high_confidence",
    research_status: "verified_employer_found",
    personnel_category: "commissioned_army_officer",
    commissioned_officer: true,
  });
  expect(person.last_civilian_pre_service).toEqual([
    expect.objectContaining({
      canonical_organization: "Yale University",
      role_title: "Instructor in English",
      claim_confidence: "high",
    }),
  ]);
  expect(person.immediate_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      canonical_organization: "United States Army",
      relationship_type: "military_assignment",
      claim_confidence: "high",
    }),
  ]);
});

test("Wake remains a probable identity and keeps Hearst, Resistance and SOE distinct", async ({ request }) => {
  const person = await publicPerson(request, profiles[3][0], profiles[3][1]);
  expect(person).toMatchObject({
    identity_status: "probable",
    research_status: "documented_prewar_employer_found",
    personnel_category: "foreign_or_allied_military_personnel",
  });
  expect(person.immediate_pre_oss_affiliations).toHaveLength(0);
  expect(person.last_civilian_pre_service).toEqual([
    expect.objectContaining({ canonical_organization: "Hearst newspapers" }),
  ]);
  expect(person.other_pre_oss_affiliations).toEqual(expect.arrayContaining([
    expect.objectContaining({ canonical_organization: "French Resistance", relationship_type: "volunteer" }),
    expect.objectContaining({ canonical_organization: "Special Operations Executive", relationship_type: "government_assignment" }),
  ]));
});

test("Walbridge and Waldhorn publish military pathways without civilian-employer inflation", async ({ request }) => {
  const walbridge = await publicPerson(request, profiles[7][0], profiles[7][1]);
  expect(walbridge.immediate_pre_oss_affiliations).toEqual([
    expect.objectContaining({ canonical_organization: "United States Navy", claim_confidence: "high" }),
  ]);
  expect(walbridge.last_civilian_pre_service).toHaveLength(0);

  const waldhorn = await publicPerson(request, profiles[12][0], profiles[12][1]);
  expect(waldhorn).toMatchObject({ identity_status: "confirmed", personnel_category: "commissioned_army_officer" });
  expect(waldhorn.immediate_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      canonical_organization: "74th General Hospital",
      temporal_basis: "explicit_immediate",
      claim_confidence: "confirmed",
    }),
  ]);
  expect(waldhorn.last_civilian_pre_service).toHaveLength(0);
});

test("the Walden shared identifier remains a visible conflict, not a merge", async ({ request }) => {
  const groups: string[] = [];
  for (const index of [10, 11] as const) {
    const person = await publicPerson(request, profiles[index][0], profiles[index][1]);
    expect(person).toMatchObject({
      identity_status: "conflicting",
      research_status: "conflicting_sources",
    });
    expect(person.possible_duplicate_group).toMatch(/^duplicate-[0-9a-f]{12}$/);
    groups.push(person.possible_duplicate_group);
    expect(person.claims).toEqual([
      expect.objectContaining({ claim_type: "identity", claim_confidence: "conflicting" }),
    ]);
  }
  expect(new Set(groups).size).toBe(1);
});

test("Army categories stay qualified and unnamed employers stay unnamed", async ({ request }) => {
  for (const index of [4, 14, 19] as const) {
    const person = await publicPerson(request, profiles[index][0], profiles[index][1]);
    expect(person.identity_status).toBe("confirmed");
    expect(person.last_civilian_pre_service).toHaveLength(0);
    const category = person.other_pre_oss_affiliations.find((item: { canonical_organization: string | null }) => item.canonical_organization === null);
    expect(category).toMatchObject({ claim_confidence: "medium", publication_status: "publish_qualified" });
  }
});

test("John Waldron remains unresolved despite an unbridged official OSS namesake", async ({ request }) => {
  const person = await publicPerson(request, profiles[20][0], profiles[20][1]);
  expect(person).toMatchObject({ identity_status: "unresolved", research_status: "requires_archival_review" });
  expect(person.claims).toHaveLength(0);
  expect(person.archival_file.review_priority).toBe("high");
});

test("Batch 994 evidence excludes secrets, full identifiers and raw bulk records", () => {
  expect(evidence).not.toMatch(/"serial_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toMatch(/"service_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toContain("NARA_API_KEY");
  expect(evidence).not.toContain("x-api-key");
  expect(evidence).not.toContain("candidate_identifier");
  expect(evidence).not.toContain("bulk_record_ordinal");
  expect(evidence).not.toMatch(/\b[ORW]-?\d{5,9}\b/);
});

test("Batch 994 public claims retain inspectable source citations", async ({ request }) => {
  for (const index of [1, 3, 4, 7, 9, 10, 11, 12, 14, 19] as const) {
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

test("Batch 994 publishes exact coverage counters", async ({ request }) => {
  const response = await request.get("./data/stats.json");
  expect(response.ok()).toBeTruthy();
  expect(await response.json()).toMatchObject({
    source_rows: 23_978,
    person_entities: 23_936,
    possible_duplicate_groups: 679,
    research_attempted_people: 15_794,
    verified_affiliation_people: 1_143,
    verified_employer_people: 517,
    archival_review_assessed_people: 14_269,
    published_claims: 10_122,
    public_sources: 6_506,
  });
});
