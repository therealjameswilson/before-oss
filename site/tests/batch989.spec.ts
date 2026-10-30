import fs from "node:fs";
import { expect, test } from "@playwright/test";
import type { APIRequestContext } from "@playwright/test";

const evidence = fs.readFileSync(
  new URL(
    "../../research/evidence-page485-voiles-to-von-meyerfeld-review_batch-989_2026-10-30.json",
    import.meta.url,
  ),
  "utf8",
);

const profiles = [
  ["2f4efe76-ace1-5e51-b6c1-37bea40965ac", "Alice Voiles"],
  ["1544624a-b9ba-549b-968a-433233d49a7c", "John F Vokestaitis"],
  ["aa1ebeca-8f75-538f-8771-d00f31025d41", "Joseph C Vokoun Jr."],
  ["2cef112d-9b1c-59ae-af29-c585cc49a415", "Arthur W Volck"],
  ["0ee623a9-7af4-5d84-89f0-6dce00e8a775", "Harold F Volk"],
  ["2cde1c52-ca14-52a3-b9b8-bc3a61fdbe18", "William J Volk"],
  ["168bb5fb-3e0e-543b-92a4-b80c8ada3acd", "Ernest W Volkmar"],
  ["9086c36c-96b5-5a72-a132-d139935f13d3", "Daniel E Volm"],
  ["1895dfcb-a588-5581-a5dc-6b56b86546a7", "Gerald Volm"],
  ["752029e7-cc27-5f1c-b486-30108e4126ee", "James Volosen"],
  ["b5fe08c4-ccf3-55e9-875c-13318f603d38", "Mario H Volpe"],
  ["b0b9a0cb-dc8e-59b8-bf41-49cf90f41b8f", "William Volpe"],
  ["113ffbf7-df79-5f44-a033-9f4e9560b928", "Elmer Volton"],
  ["2b7a4536-0cc9-54ad-b7d2-8447faa16939", "Frederick G Voltz"],
  ["2afa5f16-eb5c-539b-947e-0db82255d630", "Joseph Voltz"],
  ["43ea8eb6-e45b-554e-96da-f05b7bcb038f", "Nathalie A Von Bretzel"],
  ["42bb66fb-49e7-5501-a166-4451abefae0d", "Maxim C Von Brevern"],
  ["e6eb81b4-b503-5a3e-a5cd-c32139ddcb27", "John Von Der Lieth"],
  ["b365dd9c-3759-5b54-8365-b0662c9c7aa4", "Gunther Von Fritsch"],
  ["2216a8ab-92ec-5871-a82a-2e80d7ce470d", "Gerhard E Von Glahn"],
  ["bbc9de8f-66d7-52ef-a825-cd04a55cfba4", "Gert Hans Von Gontard"],
  ["52b56726-abdc-51af-aefe-6557f1c579ee", "Wilhelm-Viggo E.F. Von Hoffmanst"],
  ["7dfe6372-13f7-5ee8-8fb2-4dab6bdf03df", "Herman W Von Meyerfeld"],
] as const;

async function publicPerson(request: APIRequestContext, id: string, name: string) {
  const first = name[0].toLowerCase();
  const shard = /^[a-z]$/.test(first) ? first : "other";
  const response = await request.get(`./data/people/${shard}.json`);
  expect(response.ok()).toBeTruthy();
  return (await response.json()).find((item: { person_id: string }) => item.person_id === id);
}

test("Batch 989 publishes all 23 audited people with terminal outcomes", async ({ page }) => {
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
    [profiles[2][0], profiles[2][1], "general office clerk"],
    [profiles[10][0], profiles[10][1], "lawyer or judge"],
  ] as const;
  for (const [id, name, occupation] of expected) {
    const person = await publicPerson(request, id, name);
    expect(person).toMatchObject({ identity_status: "high_confidence", research_status: "occupation_only_found" });
    expect(person.immediate_pre_oss_affiliations).toHaveLength(0);
    expect(person.last_civilian_pre_service).toHaveLength(0);
    expect(person.other_pre_oss_affiliations).toEqual(expect.arrayContaining([
      expect.objectContaining({
        canonical_organization: null,
        occupation,
        relationship_type: "employment",
        temporal_basis: "strongly_date_bounded",
        claim_confidence: "medium",
        publication_status: "publish_qualified",
      }),
    ]));
  }
});

test("William Volk and William Volpe keep identity bridges without unsafe occupation transfer", async ({ request }) => {
  for (const index of [5, 11] as const) {
    const person = await publicPerson(request, profiles[index][0], profiles[index][1]);
    expect(person).toMatchObject({ identity_status: "high_confidence", research_status: "requires_archival_review" });
    expect(person.immediate_pre_oss_affiliations).toHaveLength(0);
    expect(person.last_civilian_pre_service).toHaveLength(0);
    expect(person.other_pre_oss_affiliations).toHaveLength(0);
  }
  const volk = await publicPerson(request, profiles[5][0], profiles[5][1]);
  const volpe = await publicPerson(request, profiles[11][0], profiles[11][1]);
  expect(JSON.stringify(volk)).not.toContain("sheet metal");
  expect(JSON.stringify(volpe)).not.toContain('"occupation":"999"');
});

test("Nathalie von Bretzel publishes earlier teaching without claiming immediacy", async ({ request }) => {
  const person = await publicPerson(request, profiles[15][0], profiles[15][1]);
  expect(person).toMatchObject({
    identity_status: "high_confidence",
    research_status: "documented_prewar_employer_found",
    personnel_category: "civilian_professional_or_administrative_grade",
  });
  expect(person.immediate_pre_oss_affiliations).toHaveLength(0);
  expect(person.last_civilian_pre_service).toHaveLength(0);
  expect(person.other_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      canonical_organization: "National Park Junior College",
      role_title: "teacher",
      relationship_type: "employment",
      temporal_basis: "documented_prewar",
      claim_confidence: "high",
      publication_status: "published",
    }),
  ]);
});

test("probable identities keep qualified context separate from employer analytics", async ({ request }) => {
  const maxim = await publicPerson(request, profiles[16][0], profiles[16][1]);
  expect(maxim).toMatchObject({ identity_status: "probable", research_status: "requires_archival_review" });
  expect(maxim.other_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      canonical_organization: "Institute for Advanced Study",
      relationship_type: "professional_affiliation",
      temporal_basis: "documented_prewar",
      claim_confidence: "medium",
      publication_status: "publish_qualified",
    }),
  ]);

  const fritsch = await publicPerson(request, profiles[18][0], profiles[18][1]);
  expect(fritsch).toMatchObject({ identity_status: "probable", research_status: "requires_archival_review" });
  expect(fritsch.other_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      canonical_organization: "United States Department of the Interior",
      relationship_type: "government_assignment",
      temporal_basis: "documented_prewar",
      claim_confidence: "medium",
      publication_status: "publish_qualified",
    }),
  ]);

  const lieth = await publicPerson(request, profiles[17][0], profiles[17][1]);
  expect(lieth).toMatchObject({ identity_status: "probable", research_status: "requires_archival_review" });
  expect(lieth.immediate_pre_oss_affiliations).toHaveLength(0);
  expect(lieth.last_civilian_pre_service).toHaveLength(0);
  expect(lieth.other_pre_oss_affiliations).toHaveLength(0);
});

test("identifier conflicts remain separate and transfer no employment", async ({ request }) => {
  const volosen = await publicPerson(request, profiles[9][0], profiles[9][1]);
  expect(volosen).toMatchObject({ identity_status: "conflicting", research_status: "conflicting_sources" });
  expect(volosen.possible_duplicate_group).toMatch(/^duplicate-/);

  const hoffmanst = await publicPerson(request, profiles[21][0], profiles[21][1]);
  expect(hoffmanst).toMatchObject({ identity_status: "conflicting", research_status: "conflicting_sources" });

  for (const person of [volosen, hoffmanst]) {
    expect(person.immediate_pre_oss_affiliations).toHaveLength(0);
    expect(person.last_civilian_pre_service).toHaveLength(0);
    expect(person.other_pre_oss_affiliations).toHaveLength(0);
    expect(person.claims).toEqual(expect.arrayContaining([
      expect.objectContaining({ claim_type: "identity", claim_confidence: "conflicting", publication_status: "conflicting" }),
    ]));
  }
});

test("Batch 989 evidence excludes secrets, full identifiers and raw bulk records", () => {
  expect(evidence).not.toMatch(/"serial_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toMatch(/"service_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toContain("NARA_API_KEY");
  expect(evidence).not.toContain("x-api-key");
  expect(evidence).not.toContain("candidate_identifier");
  expect(evidence).not.toContain("bulk_record_ordinal");
  expect(evidence).not.toMatch(/RA\d{8}/);
});

test("Batch 989 public claims retain inspectable source citations", async ({ request }) => {
  for (const index of [2, 5, 9, 10, 11, 15, 16, 17, 18, 21] as const) {
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

test("Batch 989 publishes exact coverage counters", async ({ request }) => {
  const response = await request.get("./data/stats.json");
  expect(response.ok()).toBeTruthy();
  expect(await response.json()).toMatchObject({
    source_rows: 23_978,
    person_entities: 23_936,
    possible_duplicate_groups: 676,
    research_attempted_people: 15_679,
    verified_affiliation_people: 1_129,
    verified_employer_people: 510,
    archival_review_assessed_people: 14_154,
    published_claims: 10_021,
    public_sources: 6_451,
  });
});
