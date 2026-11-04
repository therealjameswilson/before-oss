import fs from "node:fs";
import { expect, test } from "@playwright/test";
import type { APIRequestContext } from "@playwright/test";

const evidence = fs.readFileSync(
  new URL(
    "../../research/evidence-page499-westphal-to-wheeler-review_batch-1009_2026-11-03.json",
    import.meta.url,
  ),
  "utf8",
);

const profiles = [
  ["14c96599-61a4-5137-96be-af621d00ec6f", "Westphal Mau M Weston"],
  ["3cc43895-068a-5665-a183-c2ae2651556e", "Elkins Wetherill"],
  ["f6367530-b7ea-5ba1-bc83-b9e68bd1d211", "Curtis J Wethington"],
  ["0f936f33-9975-5d30-ae99-8464b7a769cf", "Melvin H Wetmore"],
  ["6e67ec35-b0ba-5f09-acfd-bd90fffa1163", "James E Wetrich"],
  ["531df8e6-9882-5569-8501-a2708c296072", "Gosta C.F. Wetterhall"],
  ["77aff1f6-37c6-5b0c-a1fc-6be4680cebd1", "Kenneth L Wettstein"],
  ["f4d61b8b-2635-5e36-9059-61e3b97bd937", "Albert L Wetzel"],
  ["66d247aa-65b1-5da8-992f-8dc025834910", "Richard C Wetzel"],
  ["6fde13fa-256f-531a-9c73-06aae304033d", "Victor A Wetzler"],
  ["7ded2005-246b-5e26-90a2-a22f78243da9", "Peter Weyer"],
  ["e8006d10-4bff-5709-8158-4b9d992f6f96", "Nathaniel Weyl"],
  ["de724ede-6859-5ab1-aeac-e8729c0c1d3c", "Walter Weyl"],
  ["ce02494a-9625-5fde-b55c-0292939fb143", "Stephen C Weyland"],
  ["ba23240d-7619-58a7-8292-50501df15f4a", "Thomas H Whalen"],
  ["abf01a50-b0cc-5f09-aac7-8807763c3cd0", "Faith S Whaley"],
  ["f263835a-3334-543f-9cf9-945c548e6b84", "Joseph S Whallen"],
  ["979b6fb6-3abc-5d93-a16d-312a37573a06", "Daniel O Whallon"],
  ["47a54693-66c5-5519-8f92-9f4d13ec6943", "Joseph F Whalon"],
  ["ca848a3a-f268-5bcd-90f6-8ddee866fd47", "Le Roy Whan"],
  ["bd8f2c86-c96d-5f3c-b68b-2e4635f86bd3", "Donald L Wharton"],
  ["3a8524a5-446e-5b0e-9e7a-6da9b2f76900", "Jack R Wheat"],
  ["e64b4ca2-13c8-5e73-ab08-158c09489117", "Jack R Wheat"],
  ["46b3553b-f74d-50b6-9cae-c63a19c0ecfa", "John P Wheat"],
  ["9cd78d4b-c2ed-5614-9741-e89a17057d95", "Robert I Wheat"],
  ["49bba267-8013-57b4-8322-248127a4cefa", "Alice G Wheaton"],
  ["0f883c74-4f9b-5212-b1cf-542ef0014b1b", "Jesse D Wheaton"],
  ["944823db-b607-50ca-b08c-b0aca466e5f4", "Barbara B Wheeler"],
  ["c5d47c44-9d28-5eb4-a610-e325f5858a0e", "Donald N Wheeler"],
  ["239f1ec5-0b8e-5167-9aa6-ecc18b00e185", "Donald Wheeler"],
  ["a3dfd306-c539-5efc-98aa-2eb50775da64", "Elmore Wheeler"],
  ["a73c97b1-3be6-5698-800a-5e838d7d1a1b", "George R Wheeler"],
  ["bb132943-7aad-5797-991f-d0cf970e2d03", "Howard D Wheeler"],
  ["090a518b-209c-57ab-9ef3-869914daa9c2", "Howard F Wheeler"],
  ["ce8b8cd9-89bb-5fc7-bb59-ec8344827598", "John L Wheeler"],
  ["817fb808-4d88-5fd2-800a-ba9078a7f1dd", "John W Wheeler"],
  ["afbd0519-adb4-5422-a950-6d77586a0bd6", "Leroy E Wheeler"],
  ["b8b1cbff-61cb-5d62-bfe3-283741bac968", "Lois E Wheeler"],
  ["b06a0a47-2a69-586e-9bca-5ecf768f3d59", "Margaret I Wheeler"],
  ["b0b4f3f5-18b8-5289-bbed-6d018545c699", "Nelson O Wheeler"],
  ["b53f79f1-f484-5bc9-9fb2-b393b4247ddb", "Raymond K Wheeler"],
  ["dc881c88-c124-5a5e-a6ff-a8c0c7e890cf", "Roderick D Wheeler"],
  ["b6a5be11-cf9a-5bd1-82be-6b1298efc275", "Sydney W Wheeler"],
  ["55924f02-fc8b-5d1d-83ae-f5f87160070b", "William C Wheeler"],
  ["fd44c322-a652-5965-a756-fd5eebaa6944", "William J Wheeler"],
  ["24b3b97a-eb41-5324-b1ca-57093922f0c3", "William M Wheeler Jr."],
] as const;

async function publicPerson(request: APIRequestContext, id: string, name: string) {
  const first = name[0].toLowerCase();
  const shard = /^[a-z]$/.test(first) ? first : "other";
  const response = await request.get(`./data/people/${shard}.json`);
  expect(response.ok()).toBeTruthy();
  return (await response.json()).find(
    (item: { person_id: string }) => item.person_id === id,
  );
}

test("Batch 1009 publishes all 46 reviewed people with terminal outcomes", async ({ page }) => {
  for (const [id, name] of profiles) {
    await page.goto(`./people/${id}/`);
    await expect(page.getByRole("heading", { name, level: 1 })).toBeVisible();
    const main = page.locator("main");
    await expect(main).not.toContainText("not started");
    await expect(main).not.toContainText("in progress");
    await expect(main).not.toContainText(/\b[ORW]-?\d{5,9}\b/);
  }
});

test("all 46 page 499 rows remain separately recoverable", async ({ request }) => {
  let sourceRows = 0;
  for (const [id, name] of profiles) {
    const person = await publicPerson(request, id, name);
    sourceRows += person.source_records.filter(
      (row: { pdf_page: number }) => row.pdf_page === 499,
    ).length;
  }
  expect(sourceRows).toBe(46);
});

test("five Army categories remain qualified and never invent employers", async ({ request }) => {
  const expected = new Map([
    [profiles[2][0], ["nursery and landscaping laborer", "unknown"]],
    [profiles[3][0], ["steam fitter, gas fitter, or plumber", "unknown"]],
    [profiles[4][0], ["mechanic or repairman, not elsewhere classified", "unknown"]],
    [profiles[13][0], ["industrial engineer", "unknown"]],
    [profiles[22][0], ["student", "student"]],
  ]);
  for (const [id, [occupation, relationship]] of expected) {
    const name = profiles.find(([personId]) => personId === id)![1];
    const person = await publicPerson(request, id, name);
    expect(person).toMatchObject({
      identity_status: "confirmed",
      personnel_category: "enlisted_army_personnel",
      commissioned_officer: false,
      research_status: "occupation_only_found",
    });
    expect(person.immediate_pre_oss_affiliations).toHaveLength(0);
    expect(person.last_civilian_pre_service).toHaveLength(0);
    expect(person.other_pre_oss_affiliations).toEqual([
      expect.objectContaining({
        canonical_organization: null,
        occupation,
        relationship_type: relationship,
        temporal_basis: "strongly_date_bounded",
        claim_confidence: "medium",
        publication_status: "publish_qualified",
      }),
    ]);
  }
});

test("Elkins Wetherill distinguishes student status from military assignments", async ({ request }) => {
  const person = await publicPerson(request, profiles[1][0], profiles[1][1]);
  expect(person).toMatchObject({
    identity_status: "high_confidence",
    personnel_category: "commissioned_army_officer",
    commissioned_officer: true,
    research_status: "completed",
  });
  expect(person.immediate_pre_oss_affiliations).toHaveLength(0);
  expect(person.last_civilian_pre_service).toHaveLength(0);
  expect(person.other_pre_oss_affiliations).toEqual(
    expect.arrayContaining([
      expect.objectContaining({
        canonical_organization: "University of Pennsylvania",
        relationship_type: "student",
        temporal_basis: "explicit_immediate",
      }),
      expect.objectContaining({
        canonical_organization: "First Troop Philadelphia City Cavalry",
        relationship_type: "military_assignment",
      }),
      expect.objectContaining({
        canonical_organization: "United States Army Signal Corps",
        temporal_basis: "temporal_relation_uncertain",
      }),
    ]),
  );
});

test("Gösta Wetterhall remains foreign military personnel with qualified assignments", async ({ request }) => {
  const person = await publicPerson(request, profiles[5][0], profiles[5][1]);
  expect(person).toMatchObject({
    identity_status: "high_confidence",
    personnel_category: "foreign_or_allied_military_personnel",
    commissioned_officer: true,
    allied_or_foreign_personnel: true,
  });
  expect(person.other_pre_oss_affiliations).toEqual(
    expect.arrayContaining([
      expect.objectContaining({
        canonical_organization: "Krigsskolan",
        role_title: "Teacher",
        temporal_basis: "documented_prewar",
      }),
      expect.objectContaining({
        canonical_organization: "Swedish Army Ranger School",
        role_title: "Commander",
        temporal_basis: "temporal_relation_uncertain",
      }),
    ]),
  );
});

test("Nathaniel Weyl keeps the last civilian assignment separate from earlier roles", async ({ request }) => {
  const person = await publicPerson(request, profiles[11][0], profiles[11][1]);
  expect(person).toMatchObject({ identity_status: "high_confidence", research_status: "completed" });
  expect(person.immediate_pre_oss_affiliations).toHaveLength(0);
  expect(person.last_civilian_pre_service).toEqual([
    expect.objectContaining({
      canonical_organization: "Board of Economic Warfare",
      role_title: "Economist",
      relationship_type: "government_assignment",
      temporal_basis: "strongly_date_bounded",
    }),
  ]);
  expect(person.other_pre_oss_affiliations).toEqual(
    expect.arrayContaining([
      expect.objectContaining({ canonical_organization: "Board of Governors of the Federal Reserve System" }),
      expect.objectContaining({ canonical_organization: "Agricultural Adjustment Administration" }),
    ]),
  );
});

test("Donald Niven Wheeler's Yale work remains earlier rather than immediate", async ({ request }) => {
  const person = await publicPerson(request, profiles[28][0], profiles[28][1]);
  expect(person).toMatchObject({
    identity_status: "high_confidence",
    personnel_category: "civilian_professional_or_administrative_grade",
    research_status: "completed",
  });
  expect(person.immediate_pre_oss_affiliations).toHaveLength(0);
  expect(person.last_civilian_pre_service).toHaveLength(0);
  expect(person.other_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      canonical_organization: "Yale University",
      relationship_type: "employment",
      temporal_basis: "documented_prewar",
      claim_confidence: "medium",
    }),
  ]);
});

test("John Wheat conflict and same-name Jack Wheat rows remain explicit", async ({ request }) => {
  const john = await publicPerson(request, profiles[23][0], profiles[23][1]);
  expect(john).toMatchObject({
    identity_status: "conflicting",
    research_status: "conflicting_sources",
  });
  expect(john.other_pre_oss_affiliations).toHaveLength(0);
  expect(john.claims.some((claim: { claim_confidence: string }) => claim.claim_confidence === "conflicting")).toBe(true);

  const unnumbered = await publicPerson(request, profiles[21][0], profiles[21][1]);
  const numbered = await publicPerson(request, profiles[22][0], profiles[22][1]);
  expect(unnumbered.person_id).not.toBe(numbered.person_id);
  expect(unnumbered.possible_duplicate_group).toBeTruthy();
  expect(numbered.possible_duplicate_group).toBe(unnumbered.possible_duplicate_group);
  expect(unnumbered.identity_status).toBe("unresolved");
  expect(numbered.identity_status).toBe("confirmed");
});

test("Batch 1009 evidence excludes secrets, identifiers, and raw bulk records", () => {
  expect(evidence).not.toMatch(/"serial_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toMatch(/"service_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toContain("NARA_API_KEY");
  expect(evidence).not.toContain("x-api-key");
  expect(evidence).not.toContain("candidate_identifier");
  expect(evidence).not.toContain("bulk_record_ordinal");
  expect(evidence).not.toMatch(/\b[ORW]-?\d{5,9}\b/);
});

test("Batch 1009 public claims retain inspectable short citations", async ({ request }) => {
  const claimIndexes = [1, 2, 3, 4, 5, 11, 13, 22, 23, 28] as const;
  for (const index of claimIndexes) {
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
