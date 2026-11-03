import fs from "node:fs";
import { expect, test } from "@playwright/test";
import type { APIRequestContext } from "@playwright/test";

const evidence = fs.readFileSync(
  new URL(
    "../../research/evidence-page492-waters-to-watters-review_batch-1002_2026-11-03.json",
    import.meta.url,
  ),
  "utf8",
);

const profiles = [
  ["f8df6b7e-af94-5c45-978f-ada828df39e5", "Donald O Waters"],
  ["9a74397d-2341-5bcf-91d2-201d42927823", "Freeman Waters"],
  ["97d07707-aee0-522e-8033-6bd6d46fe267", "John R Waters"],
  ["666bafff-6b58-5301-b0a9-21b399578c13", "Lee W Waters"],
  ["9c35ecd1-a1b0-5ea8-aec2-a80d48214d1b", "Louise V Waters"],
  ["38ae5342-7ef4-57d7-b904-1f143d37c273", "Martin J Waters Jr."],
  ["8d427d07-8902-57dd-bbd0-632afc4e9dcb", "William J Waters"],
  ["60b2620c-5001-55af-8dbc-005ad86bdce1", "John J Wathey"],
  ["dfd06350-8ca2-5188-909d-6913e7c43ea1", "Agnes M Wathley"],
  ["d433152f-6f0b-50af-a9da-f0032526ec4b", "Ann Watkins"],
  ["c8800e05-3bf6-561d-ba74-377a56e4b00e", "Armitage Watkins"],
  ["fe8d97f1-79ec-5c69-93eb-1dd8faeb673b", "Arthur W Watkins"],
  ["0eed28b7-cb28-5aa8-8a91-f8f644689e5e", "Caryl J Watkins"],
  ["6b615233-75aa-5b02-8c54-b98e6530ef7b", "Charles R Watkins"],
  ["2811a6e9-abc3-58fb-ae3c-9719b4ab3b92", "Elizabeth L Watkins"],
  ["fcbc3bb1-285e-5b1a-bafa-ec8d035ba34d", "Ervine C Watkins"],
  ["2f061908-5ea8-5ef8-8088-18d9e93ffecd", "Fitch Watkins"],
  ["3d4c6a52-a771-5ecb-a408-fc20a473d7fc", "Frederick M Watkins"],
  ["01aa76df-a5f9-538c-b6fa-5a18aaecb692", "George E Watkins"],
  ["10238e5a-1e22-5c9d-b686-41f1c535b1d7", "George L Watkins"],
  ["765c1a83-c5e6-5f3c-b441-367f5fe7f6fc", "Gladys M Watkins"],
  ["615ed00a-a4af-501c-812f-e45747d99033", "Thomas H Watkins"],
  ["1d9badfa-9791-57de-a7f1-769b472a57d3", "William H Watkins"],
  ["1b35027b-8402-5142-941e-0c10d412c680", "Allyn R Watson"],
  ["bddef72e-36a0-53e1-aa57-4c4df4542871", "Eldon D Watson"],
  ["eb26f905-3ac1-562f-b6df-d3b617b95212", "Fred S Watson Jr."],
  ["78717d07-eb68-59e7-97cc-77212c315841", "George W Watson"],
  ["fe23b5c2-4712-5698-902f-29e24c1d2779", "George L Watson"],
  ["3af47aef-c75e-5715-96d3-4dea77fc01da", "George H Watson"],
  ["343fe3d3-84f2-5fbf-8bfe-12f83b795d2a", "Henry P Watson"],
  ["28b7e7bc-199d-5e84-bbe9-279640218279", "Hermine G Watson"],
  ["9483b242-0e98-58dc-9c80-b5fbbea61e03", "John T Watson"],
  ["38165f9e-2618-5a47-9210-72e51e484ebb", "Lee V Watson"],
  ["dd31dd6e-f2bb-553d-9bdb-d25b870b791f", "Mary A Watson"],
  ["696bde5d-8ca8-5d32-93f4-37a8fac0275d", "Mary S Watson"],
  ["f289cd20-68bf-51b2-98d0-ed9d86b5573c", "Minerva Louis Watson"],
  ["1f801a64-198c-5626-a9a1-11232a926f1c", "Minnie L Watson"],
  ["4dda1e45-8d25-52b1-b1f6-170809e98986", "Oscar L Watson"],
  ["01b2c3e2-a0f3-569f-951b-87c0f773c550", "Tom J Watson"],
  ["a8951ad7-b713-530a-addd-982a01302364", "William K Watson"],
  ["c193282a-c021-59d2-a48b-e6f14e484b9c", "Richard F Watt"],
  ["37bf5363-2d97-5d28-b725-e64aa3015e0e", "Edwin E Watte"],
  ["7f5ae83b-05f3-5636-810a-d3ee71103f6c", "Frederick Watteins"],
  ["3f2b3006-da89-526d-86c7-ca41b1b6c36b", "Joseph A Wattenhofer"],
  ["c8e51e6a-ee01-5f04-afd7-37705450a087", "Katharine Watters"],
  ["8a956e47-3a04-5155-9267-9ba42647c5c3", "Lee J Watters"],
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

test("Batch 1002 publishes all 46 audited people with terminal outcomes", async ({ page }) => {
  for (const [id, name] of profiles) {
    await page.goto(`./people/${id}/`);
    await expect(page.getByRole("heading", { name, level: 1 })).toBeVisible();
    const main = page.locator("main");
    await expect(main).not.toContainText("not started");
    await expect(main).not.toContainText("in progress");
    await expect(main).not.toContainText(/\b[ORW]-?\d{5,9}\b/);
  }
});

test("nine Army occupations remain bounded categories without invented employers", async ({ request }) => {
  const expected = new Map([
    [profiles[0][0], ["elevator operator", "unknown"]],
    [profiles[2][0], ["student", "student"]],
    [profiles[7][0], ["paymaster, payroll clerk, or timekeeper", "unknown"]],
    [profiles[11][0], ["semiskilled bakery-products production worker", "unknown"]],
    [profiles[12][0], ["wholesale manager", "unknown"]],
    [profiles[16][0], ["chauffeur or driver", "unknown"]],
    [profiles[23][0], ["student", "student"]],
    [profiles[24][0], ["carpenter", "unknown"]],
    [profiles[45][0], ["apprentice to another trade", "unknown"]],
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

test("Oscar Watson keeps identity confirmation without inventing an occupation", async ({ request }) => {
  const person = await publicPerson(request, profiles[37][0], profiles[37][1]);
  expect(person).toMatchObject({
    identity_status: "confirmed",
    personnel_category: "enlisted_army_personnel",
    research_status: "requires_archival_review",
  });
  expect(person.immediate_pre_oss_affiliations).toHaveLength(0);
  expect(person.last_civilian_pre_service).toHaveLength(0);
  expect(person.other_pre_oss_affiliations).toHaveLength(0);
});

test("Fred Watson conflict transfers no identity or occupation", async ({ request }) => {
  const person = await publicPerson(request, profiles[25][0], profiles[25][1]);
  expect(person).toMatchObject({
    identity_status: "conflicting",
    research_status: "conflicting_sources",
  });
  expect(person.immediate_pre_oss_affiliations).toHaveLength(0);
  expect(person.last_civilian_pre_service).toHaveLength(0);
  expect(person.other_pre_oss_affiliations).toHaveLength(0);
  expect(person.claims).toEqual([
    expect.objectContaining({ claim_type: "identity", claim_confidence: "conflicting" }),
  ]);
});

test("Armitage Watkins publishes OWI evidence with unresolved OSS sequence", async ({ request }) => {
  const person = await publicPerson(request, profiles[10][0], profiles[10][1]);
  expect(person).toMatchObject({
    identity_status: "high_confidence",
    research_status: "requires_archival_review",
  });
  expect(person.immediate_pre_oss_affiliations).toHaveLength(0);
  expect(person.last_civilian_pre_service).toHaveLength(0);
  expect(person.other_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      canonical_organization: "United States Office of War Information",
      role_title: "Overseas Publications",
      relationship_type: "government_assignment",
      temporal_basis: "temporal_relation_uncertain",
      claim_confidence: "medium",
    }),
  ]);
});

test("printed officers remain officers without fabricated biographies", async ({ request }) => {
  for (const index of [5, 29, 40, 41] as const) {
    const person = await publicPerson(request, profiles[index][0], profiles[index][1]);
    expect(person).toMatchObject({
      identity_status: "unresolved",
      personnel_category: "commissioned_army_officer",
      commissioned_officer: true,
      research_status: "requires_archival_review",
    });
    expect(person.other_pre_oss_affiliations).toHaveLength(0);
  }
});

test("unbridged names and printed variants retain archival outcomes", async ({ request }) => {
  for (const index of [1, 3, 4, 8, 14, 30, 35, 42, 44] as const) {
    const person = await publicPerson(request, profiles[index][0], profiles[index][1]);
    expect(person).toMatchObject({
      identity_status: "unresolved",
      research_status: "requires_archival_review",
    });
    expect(person.immediate_pre_oss_affiliations).toHaveLength(0);
    expect(person.last_civilian_pre_service).toHaveLength(0);
    expect(person.other_pre_oss_affiliations).toHaveLength(0);
  }
});

test("Batch 1002 evidence excludes secrets, identifiers, and raw bulk records", () => {
  expect(evidence).not.toMatch(/"serial_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toMatch(/"service_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toContain("NARA_API_KEY");
  expect(evidence).not.toContain("x-api-key");
  expect(evidence).not.toContain("candidate_identifier");
  expect(evidence).not.toContain("bulk_record_ordinal");
  expect(evidence).not.toMatch(/\b[ORW]-?\d{5,9}\b/);
});

test("Batch 1002 public claims retain inspectable citations", async ({ request }) => {
  for (const index of [0, 2, 7, 10, 11, 12, 16, 23, 24, 25, 37, 45] as const) {
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
