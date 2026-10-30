import fs from "node:fs";
import { expect, test } from "@playwright/test";
import type { APIRequestContext } from "@playwright/test";

const evidence = fs.readFileSync(
  new URL(
    "../../research/evidence-page485-von-moltke-to-vournas-review_batch-990_2026-10-30.json",
    import.meta.url,
  ),
  "utf8",
);

const profiles = [
  ["b8227a87-17a5-52a4-80d7-d31ff6dee558", "Wilhelm-Viggo E.F. Von Moltke"],
  ["aa89d58a-8da6-593e-8326-0cc9fd347daa", "Robert A Von Neuman"],
  ["afe08b69-e1ee-5700-b66f-373c322ebc88", "Rudolph C Von Ripper"],
  ["a4669b2c-e62f-5f67-8788-467466c49f16", "Walter Von Schuschn"],
  ["ff7f569a-385a-5a25-bcb8-4c3ad1482600", "Franz Von Seidler"],
  ["8a43d6b7-7310-5ded-b614-163865da9fe4", "Joseph Vona"],
  ["fe5b6b14-d45d-5d5f-97fe-d43b8dfbaa97", "Roy P Vonel"],
  ["54c6913a-3cf1-57fa-a0d1-c9fff105ba31", "John G Vonetes"],
  ["e0bfc44d-4a4f-5019-bdee-c27bf69ed7a7", "Nicholas A Vonneuman"],
  ["aa840791-02df-5e25-82f1-0bd391955bb5", "Francis S Vonstade"],
  ["03ce197a-fcd3-5ea8-b9a4-cc3c83b02da0", "James A Voorhees"],
  ["d9f08064-0aa3-5dc0-aa1b-cc99525c59fe", "John S Voorhees"],
  ["335da26b-23b5-532f-b451-bbc3030ab3a4", "Bert D Voot"],
  ["6726c8ad-2148-572f-b157-acaa6620b369", "Henri G.W. Vorbroker"],
  ["09daafe4-c14a-5f0b-827a-5ce19ecfb3b4", "Donald W Vose"],
  ["7ed7291c-2f3a-5fc5-9ae7-8c34a10cd660", "Robert J Voskuil"],
  ["00cfd64f-fb8a-5b33-b745-65d7e28fd264", "Raymond G Vosper"],
  ["8d107515-262c-5fb5-8a0a-4e9f3f782c12", "T.Alexander Votichenko"],
  ["f7484bdc-8aa4-52bf-a82f-8d9971ef4998", "Mario J Votinelli"],
  ["09554b6e-359e-5d5c-9d23-c4083c684e43", "Claude Vougnon"],
  ["a64bc4dd-29e4-5aff-a951-d48b1d668310", "Steve Voulgarakis"],
  ["6a2fc444-1dc1-5918-a72c-3ce9f111875b", "Adam Voulgaris"],
  ["2ca75e2b-edd4-5471-a531-c74859a0b266", "George C Vournas"],
] as const;

async function publicPerson(request: APIRequestContext, id: string, name: string) {
  const first = name[0].toLowerCase();
  const shard = /^[a-z]$/.test(first) ? first : "other";
  const response = await request.get(`./data/people/${shard}.json`);
  expect(response.ok()).toBeTruthy();
  return (await response.json()).find((item: { person_id: string }) => item.person_id === id);
}

test("Batch 990 publishes all 23 audited people with terminal outcomes", async ({ page }) => {
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

test("Nicholas Vonneuman publishes the bank, Army and OSS sequence", async ({ request }) => {
  const person = await publicPerson(request, profiles[8][0], profiles[8][1]);
  expect(person).toMatchObject({ identity_status: "confirmed", research_status: "verified_employer_found" });
  expect(person.immediate_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      canonical_organization: "United States Army",
      relationship_type: "military_assignment",
      temporal_basis: "explicit_immediate",
      claim_confidence: "confirmed",
    }),
  ]);
  expect(person.last_civilian_pre_service).toEqual([
    expect.objectContaining({
      canonical_organization: "National City Bank of New York",
      role_title: "auditor, Comptrollers Department",
      relationship_type: "employment",
      claim_confidence: "high",
    }),
  ]);
});

test("Francis von Stade keeps Harvard separate from Naval Intelligence", async ({ request }) => {
  const person = await publicPerson(request, profiles[9][0], profiles[9][1]);
  expect(person).toMatchObject({ identity_status: "high_confidence", research_status: "verified_employer_found" });
  expect(person.name_variants).toContain("Francis Skiddy von Stade Jr.");
  expect(person.immediate_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      canonical_organization: "Office of Naval Intelligence",
      relationship_type: "military_assignment",
      temporal_basis: "probable_immediate",
      publication_status: "publish_qualified",
    }),
  ]);
  expect(person.last_civilian_pre_service).toEqual([
    expect.objectContaining({ canonical_organization: "Harvard College", role_title: "Assistant Dean" }),
  ]);
});

test("Robert Voskuil publishes the COI predecessor and university employer", async ({ request }) => {
  const person = await publicPerson(request, profiles[15][0], profiles[15][1]);
  expect(person).toMatchObject({
    identity_status: "confirmed",
    personnel_category: "commissioned_naval_officer",
    research_status: "verified_employer_found",
  });
  expect(person.immediate_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      canonical_organization: "Coordinator of Information Cartography Section",
      relationship_type: "government_assignment",
      temporal_basis: "explicit_immediate",
    }),
  ]);
  expect(person.last_civilian_pre_service).toEqual([
    expect.objectContaining({ canonical_organization: "University of Illinois", role_title: "Assistant in Geography" }),
  ]);
});

test("qualified military pathways stay qualified and student status is not employment", async ({ request }) => {
  const votichenko = await publicPerson(request, profiles[17][0], profiles[17][1]);
  expect(votichenko).toMatchObject({ identity_status: "high_confidence", research_status: "requires_archival_review" });
  expect(votichenko.name_variants).toContain("Taras A. Votichenko");
  expect(votichenko.immediate_pre_oss_affiliations).toEqual([
    expect.objectContaining({ canonical_organization: "United States Navy", publication_status: "publish_qualified" }),
  ]);
  expect(votichenko.other_pre_oss_affiliations).toEqual([
    expect.objectContaining({ canonical_organization: "Princeton University", relationship_type: "student" }),
  ]);
  expect(votichenko.last_civilian_pre_service).toHaveLength(0);

  const vougnon = await publicPerson(request, profiles[19][0], profiles[19][1]);
  expect(vougnon).toMatchObject({
    identity_status: "probable",
    personnel_category: "foreign_or_allied_military_personnel",
  });
  expect(vougnon.immediate_pre_oss_affiliations).toEqual([
    expect.objectContaining({ canonical_organization: "Maquis C-134", publication_status: "publish_qualified" }),
  ]);
});

test("George Vournas keeps Army assignment and private law practice distinct", async ({ request }) => {
  const person = await publicPerson(request, profiles[22][0], profiles[22][1]);
  expect(person).toMatchObject({
    identity_status: "high_confidence",
    personnel_category: "commissioned_army_officer",
    research_status: "verified_employer_found",
  });
  expect(person.immediate_pre_oss_affiliations).toEqual([
    expect.objectContaining({ canonical_organization: "United States Army", relationship_type: "military_assignment" }),
  ]);
  expect(person.last_civilian_pre_service).toEqual([
    expect.objectContaining({ canonical_organization: null, relationship_type: "self_employment", occupation: "lawyer" }),
  ]);
});

test("unresolved and conflict cases retain archival-review guidance", async ({ request }) => {
  for (const index of [1, 3, 4, 5, 7, 11, 13, 21] as const) {
    const person = await publicPerson(request, profiles[index][0], profiles[index][1]);
    expect(["requires_archival_review", "conflicting_sources"]).toContain(person.research_status);
    expect(person.immediate_pre_oss_affiliations).toHaveLength(0);
    expect(person.last_civilian_pre_service).toHaveLength(0);
  }
  const voot = await publicPerson(request, profiles[12][0], profiles[12][1]);
  expect(voot).toMatchObject({ identity_status: "conflicting", research_status: "conflicting_sources" });
  expect(voot.possible_duplicate_group).toMatch(/^duplicate-/);
  const schuschn = await publicPerson(request, profiles[3][0], profiles[3][1]);
  expect(schuschn).toMatchObject({ identity_status: "ambiguous", research_status: "requires_archival_review" });
  expect(schuschn.possible_duplicate_group).toMatch(/^duplicate-/);
});

test("Batch 990 evidence excludes secrets, full identifiers and raw bulk records", () => {
  expect(evidence).not.toMatch(/"serial_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toMatch(/"service_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toContain("NARA_API_KEY");
  expect(evidence).not.toContain("x-api-key");
  expect(evidence).not.toContain("candidate_identifier");
  expect(evidence).not.toContain("bulk_record_ordinal");
  expect(evidence).not.toMatch(/RA\d{8}/);
});

test("Batch 990 public claims retain inspectable source citations", async ({ request }) => {
  for (const index of [0, 2, 6, 8, 9, 10, 12, 14, 15, 16, 17, 18, 19, 20, 22] as const) {
    const person = await publicPerson(request, profiles[index][0], profiles[index][1]);
    expect(person.claims.length).toBeGreaterThan(0);
    for (const claim of person.claims) {
      expect(claim.sources.length).toBeGreaterThan(0);
      for (const link of claim.sources) {
        expect(link.source.stable_url || link.source.archival_identifier).toBeTruthy();
        const excerpt = link.excerpt_override ?? claim.evidence_excerpt ?? "";
        expect(excerpt.trim() ? excerpt.trim().split(/\s+/).length : 0).toBeLessThanOrEqual(25);
      }
    }
  }
});

test("Batch 990 publishes exact coverage counters", async ({ request }) => {
  const response = await request.get("./data/stats.json");
  expect(response.ok()).toBeTruthy();
  expect(await response.json()).toMatchObject({
    source_rows: 23_978,
    person_entities: 23_936,
    possible_duplicate_groups: 677,
    research_attempted_people: 15_702,
    verified_affiliation_people: 1_135,
    verified_employer_people: 514,
    archival_review_assessed_people: 14_177,
    published_claims: 10_053,
    public_sources: 6_470,
  });
});
