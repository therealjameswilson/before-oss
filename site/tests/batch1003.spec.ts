import fs from "node:fs";
import { expect, test } from "@playwright/test";
import type { APIRequestContext } from "@playwright/test";

const evidence = fs.readFileSync(
  new URL(
    "../../research/evidence-page493-watterson-to-weber-review_batch-1003_2026-11-03.json",
    import.meta.url,
  ),
  "utf8",
);

const profiles = [
  ["e1b78199-e6d3-533b-8552-2255721a5953", "Arthur W Watterson"],
  ["f3555281-6063-59bf-a7d3-c8d71fa1603d", "Robert Silas Wattles"],
  ["cbbfe8eb-44c8-5e2f-b7b3-c193a4d876e7", "Arthur P Watts"],
  ["01cbb21a-3e2b-51be-a075-ff2657d3000b", "Dallas H Watts"],
  ["573e5b0b-4dc2-553f-9011-3df911f332d0", "Erwin H Watts"],
  ["8d384416-1380-5563-b7ae-344fec95e4d5", "Eve Watts"],
  ["092eaffe-127e-593c-a910-b1ea9131f365", "James P Watts Jr."],
  ["143b8109-28ac-5e56-bcf3-2bba6d0440cc", "Richard Watts Jr."],
  ["c02e9cd9-56fe-588c-a152-a1df5e4dbf7a", "Robert T Watts"],
  ["eb3bc431-05f0-56b9-8bb4-4a90a383937a", "Shirley L Watts"],
  ["8ee1dda8-b9c6-5b2f-a0a8-52cdcea29e13", "Robert Wauchope"],
  ["6ca54963-6dcb-587a-8b68-e9e0cfa85548", "Frederick J Waugh Jr."],
  ["d4111205-bd60-505c-a3fe-2dee3a692fce", "Jeanne Wax"],
  ["43dc6fea-d61b-53c3-ac8a-adbea7cb479e", "Edrie C Way"],
  ["dbbb76cf-ebfc-5b76-ac55-42d83baf8e16", "Helen P Weary"],
  ["7ece89f4-dadb-5891-acb7-d9d20b5b5291", "Meredith Weatherby"],
  ["5473d13c-e63d-52f4-8942-6e8a249c1842", "Paul Weatherill"],
  ["605f5941-8b11-55ab-8af7-ef6ee46da3c1", "Gerald Weathers"],
  ["6c363f8a-ce24-527e-843c-44e417d00d81", "Anthony J Weaver Jr."],
  ["eafde514-22ea-5b57-a140-2f4aa0892cb6", "Charlotte E Weaver"],
  ["1b72519d-6f46-54c5-bd6a-e134d752277a", "Charlton A Weaver"],
  ["7205097b-3f94-513e-a4d9-2ac9f9d57707", "Edward L Weaver"],
  ["2a7d64b6-a329-530c-a595-78be22aff0a0", "Helen K Weaver"],
  ["0c9af132-45fd-5c87-b6a0-a73b19d8b014", "Jim R Weaver"],
  ["aecbaf59-4b19-5bb6-8d94-5b5ddc978f0b", "John F Weaver"],
  ["94053f47-2df3-5250-b5d7-8fcfeba9208b", "John O Weaver"],
  ["bacca2df-f44b-5179-92af-48e4a0180c39", "John C Weaver"],
  ["00ee89a6-edf2-59fd-89d3-90b6eb612292", "Leon H Weaver"],
  ["277dbab4-641c-584c-946f-772732a329ef", "Margaret L Weaver"],
  ["f1441a91-0830-510c-9df8-5ce7a2e14da0", "Robert G Weaver"],
  ["299ebc54-2409-518e-9dd5-1c88ac3385a8", "William Weaver"],
  ["496804e3-6a41-539e-a265-dd50394f28c6", "* Weaver and C"],
  ["fd6448d5-ff98-510f-82b2-2547470b8a77", "Clinton Webb"],
  ["1199e6b9-f016-516e-be71-fb979b8b3d82", "Dorothy J Webb"],
  ["b70198e8-4541-59be-bccb-89ad23ba7be0", "Frances Webb"],
  ["d4b9090a-7ac4-5640-8035-4798f553d40a", "Guy E Webb"],
  ["4db5be91-fcef-5ca1-88cd-a3784c3bef0b", "James H Webb Jr."],
  ["071a99c2-27f8-53de-97eb-5d1a9ff9ab7f", "John A Webb"],
  ["fbd6811e-0c76-551f-8050-5112f4815e4c", "Kenneth W Webb"],
  ["317c293c-265a-5818-b150-939d35022f8c", "Thomas B Webb Jr."],
  ["2ee5f8b5-7394-5254-9798-896d7b600678", "Wesley D Webb"],
  ["1d96e15f-6b50-51ec-8c29-6c7a0acc31fe", "M. V Webbert"],
  ["10f7202d-9ee4-5a88-bf10-988b60dd88ec", "Dean Weber"],
  ["0ec2d8ef-d908-5564-b4be-53bd47fa07b7", "Frank R Weber"],
  ["c64303f5-5b04-5d67-b46f-8eefa17e9908", "Harry Weber"],
  ["4a8ea418-6dd5-5412-9eeb-8ec49190142b", "Jacob H Weber"],
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

test("Batch 1003 publishes all 46 audited people with terminal outcomes", async ({ page }) => {
  for (const [id, name] of profiles) {
    await page.goto(`./people/${id}/`);
    await expect(page.getByRole("heading", { name, level: 1 })).toBeVisible();
    const main = page.locator("main");
    await expect(main).not.toContainText("not started");
    await expect(main).not.toContainText("in progress");
    await expect(main).not.toContainText(/\b[ORW]-?\d{5,9}\b/);
  }
});

test("ten Army occupations remain bounded categories without invented employers", async ({ request }) => {
  const expected = new Map([
    [profiles[0][0], ["secondary-school teacher or principal", "unknown"]],
    [profiles[3][0], ["student", "student"]],
    [profiles[6][0], ["unskilled leather-products manufacturing worker", "unknown"]],
    [profiles[9][0], ["file clerk", "unknown"]],
    [profiles[17][0], ["actor", "unknown"]],
    [profiles[29][0], ["actor", "unknown"]],
    [profiles[35][0], ["student", "student"]],
    [profiles[38][0], ["lithographer", "unknown"]],
    [profiles[43][0], ["laboratory technician or assistant", "unknown"]],
    [profiles[44][0], ["lawyer or judge", "unknown"]],
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

test("Charlton Weaver identity does not turn a post-OSS Army code into prehistory", async ({ request }) => {
  const person = await publicPerson(request, profiles[20][0], profiles[20][1]);
  expect(person).toMatchObject({
    identity_status: "confirmed",
    personnel_category: "enlisted_army_personnel",
    research_status: "requires_archival_review",
  });
  expect(person.immediate_pre_oss_affiliations).toHaveLength(0);
  expect(person.last_civilian_pre_service).toHaveLength(0);
  expect(person.other_pre_oss_affiliations).toHaveLength(0);
  expect(person.claims).toEqual([
    expect.objectContaining({ claim_type: "identity", claim_confidence: "confirmed" }),
  ]);
});

test("Robert Wauchope has an explicit Tulane immediate and last-civilian chronology", async ({ request }) => {
  const person = await publicPerson(request, profiles[10][0], profiles[10][1]);
  expect(person).toMatchObject({
    identity_status: "high_confidence",
    personnel_category: "commissioned_naval_officer",
    commissioned_officer: true,
    research_status: "verified_employer_found",
  });
  const expected = expect.objectContaining({
    canonical_organization: "Tulane University",
    role_title: "Director, Middle American Research Institute, and associate professor of anthropology",
    relationship_type: "employment",
    immediate_pre_oss: true,
    last_civilian_pre_service: true,
    temporal_basis: "explicit_immediate",
    claim_confidence: "high",
  });
  expect(person.immediate_pre_oss_affiliations).toEqual([expected]);
  expect(person.last_civilian_pre_service).toEqual([expected]);
});

test("Meredith Weatherby keeps Foreign Service separate from immediate pre-OSS affiliation", async ({ request }) => {
  const person = await publicPerson(request, profiles[15][0], profiles[15][1]);
  expect(person).toMatchObject({
    identity_status: "high_confidence",
    research_status: "verified_employer_found",
  });
  expect(person.immediate_pre_oss_affiliations).toHaveLength(0);
  expect(person.last_civilian_pre_service).toEqual([
    expect.objectContaining({
      canonical_organization: "United States Department of State",
      organization_name_as_found: "Foreign Service",
      relationship_type: "government_assignment",
      immediate_pre_oss: false,
      last_civilian_pre_service: true,
      temporal_basis: "strongly_date_bounded",
      claim_confidence: "high",
    }),
  ]);
});

test("Frank Weber combines the private Army bridge with a public OSS order", async ({ request }) => {
  const person = await publicPerson(request, profiles[43][0], profiles[43][1]);
  expect(person).toMatchObject({
    identity_status: "confirmed",
    personnel_category: "enlisted_army_personnel",
    research_status: "occupation_only_found",
  });
  const identity = person.claims.find(
    (claim: { claim_type: string }) => claim.claim_type === "identity",
  );
  expect(identity.sources.map((link: { source: { title: string } }) => link.source.title)).toContain(
    "Assignment of Qualified Personnel to OSS-ME Parachute Unit",
  );
});

test("plausible namesakes remain withheld pending archival corroboration", async ({ request }) => {
  for (const index of [4, 32, 34] as const) {
    const person = await publicPerson(request, profiles[index][0], profiles[index][1]);
    expect(person).toMatchObject({
      identity_status: "probable",
      research_status: "requires_archival_review",
    });
    expect(person.immediate_pre_oss_affiliations).toHaveLength(0);
    expect(person.last_civilian_pre_service).toHaveLength(0);
    expect(person.other_pre_oss_affiliations).toHaveLength(0);
    expect(person.claims).toHaveLength(0);
  }
});

test("unusual printed form and officer categories remain recoverable", async ({ request }) => {
  const fragment = await publicPerson(request, profiles[31][0], profiles[31][1]);
  expect(fragment).toMatchObject({
    display_name: "* Weaver and C",
    identity_status: "unresolved",
    research_status: "requires_archival_review",
  });
  expect(fragment.source_records).toEqual([
    expect.objectContaining({
      indexed_last_name: "Weaver and C",
      indexed_first_name: "*",
      notes_as_indexed: "review",
      pdf_page: 493,
      box: "820",
    }),
  ]);
  expect(fragment.other_pre_oss_affiliations).toHaveLength(0);

  for (const [index, category, officer] of [
    [11, "commissioned_army_officer", true],
    [25, "commissioned_army_officer", true],
    [26, "enlisted_naval_personnel", false],
    [36, "commissioned_army_officer", true],
  ] as const) {
    const person = await publicPerson(request, profiles[index][0], profiles[index][1]);
    expect(person).toMatchObject({
      personnel_category: category,
      commissioned_officer: officer,
      research_status: "requires_archival_review",
    });
  }
});

test("Batch 1003 evidence excludes secrets, identifiers, and raw bulk records", () => {
  expect(evidence).not.toMatch(/"serial_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toMatch(/"service_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toContain("NARA_API_KEY");
  expect(evidence).not.toContain("x-api-key");
  expect(evidence).not.toContain("candidate_identifier");
  expect(evidence).not.toContain("bulk_record_ordinal");
  expect(evidence).not.toMatch(/\b[ORW]-?\d{5,9}\b/);
});

test("Batch 1003 public claims retain inspectable short citations", async ({ request }) => {
  for (const index of [0, 3, 6, 9, 10, 15, 17, 20, 29, 35, 38, 43, 44] as const) {
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
