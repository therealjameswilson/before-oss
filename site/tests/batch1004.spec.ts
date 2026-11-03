import fs from "node:fs";
import { expect, test } from "@playwright/test";
import type { APIRequestContext } from "@playwright/test";

const evidence = fs.readFileSync(
  new URL(
    "../../research/evidence-page494-weber-to-weible-review_batch-1004_2026-11-03.json",
    import.meta.url,
  ),
  "utf8",
);

const profiles = [
  ["fa864ef2-ce19-5dab-aa46-decabe576042", "Jeanette Weber"],
  ["b03e84c4-26e3-513b-9482-d33afba6d1c1", "Richard H Weber"],
  ["fea827ca-2745-5b7c-8745-e610e07e474f", "Hartwick E Weberg"],
  ["94bbea5f-4c8c-5bc8-9603-d6ed5146a09a", "Kenneth H Weberg"],
  ["1a3992ae-fdbe-5404-a21f-21832b7a8a02", "Charles A Webster"],
  ["bb981f1f-01ad-5658-bbfe-f3d41a626a1d", "David Webster Jr."],
  ["4c71e524-afc7-5ee5-912c-416088b94958", "Donald E Webster"],
  ["aaae78a1-5dc1-59e1-b287-e2669cffaf8a", "Douglas Webster"],
  ["5aec9009-6a31-551d-bb91-0bd6fda7f18c", "George F Webster"],
  ["cfe280b2-ad24-546f-90dc-384561bb93e7", "James H Webster"],
  ["dce8e648-8a95-57c1-8288-6fff7c40e98d", "John D Webster"],
  ["ae7fb230-7c76-523c-8497-696f2e4c8cba", "Pauline E Webster"],
  ["5aeca52f-7fcf-5049-92c9-707ab1929e28", "Vera M Webster"],
  ["54415368-3c67-5c39-9807-c8965eef8cd9", "Joseph Wechsberg"],
  ["f50fca9a-eeec-5f59-afcf-f2b2970a04b2", "Roland E Wechsberg"],
  ["bc3f2fee-eca3-5754-bfd4-067954af174a", "Ronald E Wechsler"],
  ["23eb2a08-3751-5eab-abb9-7e28cc226d7e", "Richard J Weckesser"],
  ["942b6d72-2420-5299-8623-bfbadf35c3e4", "Joseph E Weckler"],
  ["ae3d67ad-9869-5fe4-bd4c-7c2b581f39f6", "Margaret E Weddell"],
  ["c09a30c6-c0b1-5fb4-9ca0-8ea3730fd2be", "Arthur J Wedler"],
  ["7541818d-3e99-560c-bc6a-859069dfad54", "Edna Weed"],
  ["30916b94-186b-5a9f-a1e3-aef3ec5d4356", "Elizabeth J Weed"],
  ["d198f838-d0b6-5048-812f-034a37a8d367", "Elizabeth R Weed"],
  ["45d00a91-8bc8-5c3b-82cc-bf366837ef0b", "J M Weed"],
  ["36919928-0134-5ff4-9c8d-7285ef658362", "Ruth E Weed"],
  ["b14f8be8-0517-5ace-89c0-bd3b3677f16e", "John W Weeden"],
  ["6fcd0a5c-a4a4-55d6-b9b7-985973ab7330", "George W Weege"],
  ["cc2647f8-fad1-548e-b7b3-5b2e0071f3fb", "Clair H Weeks"],
  ["f41aff07-2672-5830-ba7f-1e57284df2cd", "Clair H Weeks"],
  ["3b2e4873-a760-55d0-ae98-8237bce27597", "Grohl H Weeks"],
  ["375d8c34-60ce-5426-ab58-50731599e624", "Robert O Weeks"],
  ["57a005d7-8004-5584-b7eb-79a4a51f875e", "Clarence Weems Jr."],
  ["c60326d2-d745-5833-ac58-28d7f00b5e37", "Michael K Weese"],
  ["f1ee23d2-3615-54bd-b86e-d5c8d2912fe1", "Walter E Weese"],
  ["f02ed8a5-87df-5780-b957-e61e22f9a8ab", "Betty E Weethee"],
  ["e6c61749-0296-5715-b1d2-0e30c6f8edbd", "Theodore G Wege"],
  ["72189316-9715-5f71-9013-8f3c161bd142", "Herbert A Weger"],
  ["1e2571b2-5f98-514d-b787-4362cbdb246f", "Alice E Wegner"],
  ["02cbd337-3848-538d-bb46-59534d055fd6", "Alfred P Wehren"],
  ["11c0d5e1-4686-52f1-90f0-8091fa866a0d", "Numa A Wehrle"],
  ["b325a60f-7ca1-5029-b5f3-e9ebc5b88f3a", "John E Wehrum"],
  ["0e9c2d1f-96d7-5023-8a93-ab3c07d5082b", "Arthur H Wehry"],
  ["a65e9e53-36b2-552e-9c8f-e49429759dc5", "Cheng S Wei"],
  ["92ef8efc-4bdf-5969-bf91-f734e0553cf6", "Wen Yuan Wei"],
  ["388d1b8a-73bf-5094-ac8b-c80844a27724", "Charles F Weible"],
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

test("Batch 1004 publishes all 45 audited people with terminal outcomes", async ({ page }) => {
  for (const [id, name] of profiles) {
    await page.goto(`./people/${id}/`);
    await expect(page.getByRole("heading", { name, level: 1 })).toBeVisible();
    const main = page.locator("main");
    await expect(main).not.toContainText("not started");
    await expect(main).not.toContainText("in progress");
    await expect(main).not.toContainText(/\b[ORW]-?\d{5,9}\b/);
  }
});

test("eight Army occupations remain bounded categories without invented employers", async ({ request }) => {
  const expected = new Map([
    [profiles[3][0], "general office clerk"],
    [profiles[16][0], "chauffeur or driver"],
    [profiles[19][0], "machinist apprentice"],
    [profiles[25][0], "pattern or model maker, except paper"],
    [profiles[32][0], "unskilled printing or publishing worker"],
    [profiles[33][0], "college president, professor, or instructor"],
    [profiles[40][0], "checker"],
    [profiles[41][0], "photographer"],
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
    expect(person.immediate_pre_oss_affiliations).toHaveLength(0);
    expect(person.last_civilian_pre_service).toHaveLength(0);
    expect(person.other_pre_oss_affiliations).toEqual([
      expect.objectContaining({
        canonical_organization: null,
        occupation,
        relationship_type: "unknown",
        temporal_basis: "strongly_date_bounded",
        claim_confidence: "medium",
        publication_status: "publish_qualified",
      }),
    ]);
  }
});

test("Kenneth Weberg identity includes the official OSS theater roster", async ({ request }) => {
  const person = await publicPerson(request, profiles[3][0], profiles[3][1]);
  const identity = person.claims.find(
    (claim: { claim_type: string }) => claim.claim_type === "identity",
  );
  expect(identity.sources.map((link: { source: { title: string } }) => link.source.title)).toContain(
    "Battle Participation Awards",
  );
});

test("Joseph Wechsberg separates freelance work from New Yorker contributor status", async ({ request }) => {
  const person = await publicPerson(request, profiles[13][0], profiles[13][1]);
  expect(person).toMatchObject({
    identity_status: "confirmed",
    research_status: "verified_employer_found",
    name_variants: expect.arrayContaining(["Joseph Wachsberg"]),
  });
  expect(person.last_civilian_pre_service).toEqual([
    expect.objectContaining({
      canonical_organization: "Self-employed",
      relationship_type: "self_employment",
      occupation: "journalist and writer",
      temporal_basis: "strongly_date_bounded",
      claim_confidence: "high",
    }),
  ]);
  expect(person.other_pre_oss_affiliations).toEqual(
    expect.arrayContaining([
      expect.objectContaining({
        canonical_organization: "The New Yorker",
        relationship_type: "professional_affiliation",
        role_title: "Contributor",
      }),
    ]),
  );
});

test("Clarence Weems has a qualified MIS predecessor and is not added to the oil category", async ({ request, page }) => {
  const person = await publicPerson(request, profiles[31][0], profiles[31][1]);
  expect(person).toMatchObject({
    identity_status: "high_confidence",
    personnel_category: "commissioned_army_officer",
    commissioned_officer: true,
    research_status: "completed",
  });
  expect(person.immediate_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      canonical_organization: "Military Intelligence Service (U.S. Army)",
      organization_name_as_found: "M.I.S. Far East Branch",
      relationship_type: "government_assignment",
      temporal_basis: "probable_immediate",
      claim_confidence: "medium",
      publication_status: "publish_qualified",
    }),
  ]);
  expect(person.last_civilian_pre_service).toHaveLength(0);
  await page.goto("./oil-companies/");
  await expect(page.locator("main")).not.toContainText("Clarence Weems");
});

test("Roland Wechsberg conflict remains visible without merging the page 498 row", async ({ request }) => {
  const person = await publicPerson(request, profiles[14][0], profiles[14][1]);
  expect(person).toMatchObject({
    identity_status: "conflicting",
    research_status: "conflicting_sources",
  });
  expect(person.source_records).toHaveLength(1);
  expect(person.immediate_pre_oss_affiliations).toHaveLength(0);
  expect(person.last_civilian_pre_service).toHaveLength(0);
  expect(person.claims).toEqual([
    expect.objectContaining({
      claim_type: "identity",
      claim_confidence: "conflicting",
      publication_status: "conflicting",
    }),
  ]);
});

test("John Webster retains two immutable source rows under one confirmed entity", async ({ request }) => {
  const person = await publicPerson(request, profiles[10][0], profiles[10][1]);
  expect(person).toMatchObject({
    identity_status: "confirmed",
    personnel_category: "commissioned_army_officer",
    commissioned_officer: true,
    research_status: "requires_archival_review",
  });
  expect(person.source_records).toHaveLength(2);
  expect(person.source_records.map((record: { box: string }) => record.box).sort()).toEqual([
    "821",
    "828",
  ]);
});

test("printed civilian and foreign-personnel categories remain conservative", async ({ request }) => {
  const jeanette = await publicPerson(request, profiles[0][0], profiles[0][1]);
  expect(jeanette).toMatchObject({
    personnel_category: "civilian_professional_or_administrative_grade",
    commissioned_officer: false,
    research_status: "requires_archival_review",
  });
  const cheng = await publicPerson(request, profiles[42][0], profiles[42][1]);
  expect(cheng).toMatchObject({
    personnel_category: "foreign_or_allied_military_personnel",
    commissioned_officer: null,
    allied_or_foreign_personnel: true,
    research_status: "requires_archival_review",
  });
});

test("Batch 1004 evidence excludes secrets, identifiers, and raw bulk records", () => {
  expect(evidence).not.toMatch(/"serial_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toMatch(/"service_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toContain("NARA_API_KEY");
  expect(evidence).not.toContain("x-api-key");
  expect(evidence).not.toContain("candidate_identifier");
  expect(evidence).not.toContain("bulk_record_ordinal");
  expect(evidence).not.toMatch(/\b[ORW]-?\d{5,9}\b/);
});

test("Batch 1004 public claims retain inspectable short citations", async ({ request }) => {
  for (const index of [3, 10, 13, 14, 16, 19, 25, 31, 32, 33, 40, 41] as const) {
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
