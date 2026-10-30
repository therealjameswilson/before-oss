import fs from "node:fs";
import { expect, test } from "@playwright/test";
import type { APIRequestContext } from "@playwright/test";

const evidence = fs.readFileSync(
  new URL(
    "../../research/evidence-page477-joe-ulmer-to-morris-unterberger-review_batch-974_2026-10-30.json",
    import.meta.url,
  ),
  "utf8",
);

const profiles = [
  ["c2108c77-94f6-5ba8-84e9-f531f877b938", "Joe W Ulmer"],
  ["34363099-20a9-5b4b-8a83-685bf9d192d1", "Kent D Ulrich"],
  ["69b2549a-bd6a-550e-8fd7-f425eb57491b", "Nels Ulvesaker"],
  ["a776790f-bf8a-5001-973b-6b39190ef45a", "Robert A Ulving"],
  ["a382a962-571b-561f-8516-02c7fa2c1064", "George A Uman"],
  ["e1c04578-f0d6-50b2-b0a2-6d95c4c8fe50", "Karl S Umberger"],
  ["2d98d4a5-9a9c-5a05-b25e-a2a75dc34c26", "Marcia Umbsen"],
  ["0deabb2f-7b88-5a56-be9c-b618edbfdabd", "Max E Umpleby"],
  ["f2db89b9-b496-5f4d-afbd-1f110e601ad5", "Irvin W Underhill"],
  ["9291090f-d334-5c13-810a-7b918a350b3e", "Claire Leon Underwood"],
  ["e4ca0559-3f57-518f-bc12-d94fbba57a43", "Gailey B Underwood"],
  ["7883ec1d-e618-57e5-a553-4a80d47d04ea", "George W Underwood"],
  ["536de873-11c1-5341-988c-7f520d5a26b9", "Horace H Underwood"],
  ["89066262-89dc-577e-9b54-b46aad1f4cfb", "Horace G Underwood"],
  ["3fa535e8-ad0d-56b7-8685-66c144a2890b", "Irene J Underwood"],
  ["153d29a7-046b-536b-82b9-e25df61ee401", "James B Underwood"],
  ["c3136cd5-cbac-5260-b604-0a32476975eb", "Orval Underwood"],
  ["d6e53de7-07ac-5a66-8bff-f679ce8273bb", "Richard F Underwood"],
  ["465d1553-ecba-5ac8-9585-df2a4f744703", "William A Underwood"],
  ["93cafd62-5e8c-5d6d-b5dd-c4dbb9a7bbcd", "Matthew J Ungerleider"],
  ["a09cf2e4-ef7f-5d2d-be17-227cdd2ef24e", "Warren W Unna"],
  ["261b84f9-c78f-5894-80e6-f05f0e2a6c1c", "Kazuo Unoki"],
  ["fafe63fd-3da6-5268-a85f-7deef1c12d88", "Morris Unterberger"],
] as const;

const unresolvedProfiles = [
  ["c2108c77-94f6-5ba8-84e9-f531f877b938", "Joe W Ulmer"],
  ["69b2549a-bd6a-550e-8fd7-f425eb57491b", "Nels Ulvesaker"],
  ["a776790f-bf8a-5001-973b-6b39190ef45a", "Robert A Ulving"],
  ["a382a962-571b-561f-8516-02c7fa2c1064", "George A Uman"],
  ["e1c04578-f0d6-50b2-b0a2-6d95c4c8fe50", "Karl S Umberger"],
  ["2d98d4a5-9a9c-5a05-b25e-a2a75dc34c26", "Marcia Umbsen"],
  ["9291090f-d334-5c13-810a-7b918a350b3e", "Claire Leon Underwood"],
  ["e4ca0559-3f57-518f-bc12-d94fbba57a43", "Gailey B Underwood"],
  ["7883ec1d-e618-57e5-a553-4a80d47d04ea", "George W Underwood"],
  ["3fa535e8-ad0d-56b7-8685-66c144a2890b", "Irene J Underwood"],
  ["153d29a7-046b-536b-82b9-e25df61ee401", "James B Underwood"],
  ["c3136cd5-cbac-5260-b604-0a32476975eb", "Orval Underwood"],
  ["465d1553-ecba-5ac8-9585-df2a4f744703", "William A Underwood"],
  ["fafe63fd-3da6-5268-a85f-7deef1c12d88", "Morris Unterberger"],
] as const;

async function publicPerson(request: APIRequestContext, id: string, name: string) {
  const response = await request.get(`./data/people/${name[0].toLowerCase()}.json`);
  expect(response.ok()).toBeTruthy();
  return (await response.json()).find((item: { person_id: string }) => item.person_id === id);
}

test("Batch 974 publishes all 23 audited people with terminal outcomes", async ({ page }) => {
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

test("four protected Army matches publish occupations, never employers", async ({ request }) => {
  const expected = [
    ["34363099-20a9-5b4b-8a83-685bf9d192d1", "Kent D Ulrich", "mechanic or repairman, not elsewhere classified", "documented_prewar"],
    ["0deabb2f-7b88-5a56-be9c-b618edbfdabd", "Max E Umpleby", "student", "documented_prewar"],
    ["d6e53de7-07ac-5a66-8bff-f679ce8273bb", "Richard F Underwood", "student", "temporal_relation_uncertain"],
    ["93cafd62-5e8c-5d6d-b5dd-c4dbb9a7bbcd", "Matthew J Ungerleider", "stock clerk", "documented_prewar"],
  ] as const;
  for (const [id, name, occupation, temporalBasis] of expected) {
    const person = await publicPerson(request, id, name);
    expect(person).toMatchObject({
      identity_status: "high_confidence",
      research_status: "occupation_only_found",
      personnel_category: "enlisted_army_personnel",
      commissioned_officer: false,
    });
    expect(person.immediate_pre_oss_affiliations).toHaveLength(0);
    expect(person.last_civilian_pre_service).toHaveLength(0);
    expect(person.other_pre_oss_affiliations).toEqual(expect.arrayContaining([
      expect.objectContaining({
        canonical_organization: null,
        occupation,
        temporal_basis: temporalBasis,
        claim_confidence: "medium",
        publication_status: "publish_qualified",
      }),
    ]));
  }
});

test("Irvin Underhill separates concurrent housing employment from earlier mission service", async ({ request }) => {
  const person = await publicPerson(request, "f2db89b9-b496-5f4d-afbd-1f110e601ad5", "Irvin W Underhill");
  expect(person).toMatchObject({ identity_status: "high_confidence", research_status: "verified_employer_found" });
  expect(person.immediate_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      canonical_organization: "Philadelphia Housing Authority",
      role_title: "manager of Richard Allen Homes",
      relationship_type: "employment",
      temporal_basis: "strongly_date_bounded",
      claim_confidence: "high",
    }),
  ]);
  expect(person.last_civilian_pre_service).toEqual([
    expect.objectContaining({ canonical_organization: "Philadelphia Housing Authority" }),
  ]);
  expect(person.other_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      canonical_organization: "Presbyterian Church in the U.S.A. West Africa Mission",
      relationship_type: "professional_affiliation",
      temporal_basis: "documented_prewar",
    }),
  ]);
});

test("Horace Horton and Horace Grant Underwood remain separate people", async ({ request }) => {
  const father = await publicPerson(request, "536de873-11c1-5341-988c-7f520d5a26b9", "Horace H Underwood");
  const son = await publicPerson(request, "89066262-89dc-577e-9b54-b46aad1f4cfb", "Horace G Underwood");
  expect(father).toMatchObject({
    identity_status: "high_confidence",
    research_status: "documented_prewar_employer_found",
    display_name: "Horace H Underwood",
  });
  expect(father.last_civilian_pre_service).toEqual([
    expect.objectContaining({
      canonical_organization: "Yonhi College",
      role_title: "third president",
      claim_confidence: "medium",
      publication_status: "publish_qualified",
    }),
  ]);
  expect(son).toMatchObject({
    identity_status: "high_confidence",
    research_status: "documented_prewar_employer_found",
    personnel_category: "commissioned_naval_officer",
    commissioned_officer: true,
    display_name: "Horace G Underwood",
  });
  expect(son.last_civilian_pre_service).toEqual([
    expect.objectContaining({
      canonical_organization: "Yonhi College",
      organization_name_as_found: "Chosen Christian College",
      role_title: "English instructor",
      claim_confidence: "high",
    }),
  ]);
  expect(son.other_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      canonical_organization: "United States Navy",
      relationship_type: "military_assignment",
      temporal_basis: "temporal_relation_uncertain",
    }),
  ]);
});

test("Warren Unna stays a qualified student candidate and Kazuo Unoki identity evidence stays non-temporal", async ({ request }) => {
  const unna = await publicPerson(request, "a09cf2e4-ef7f-5d2d-be17-227cdd2ef24e", "Warren W Unna");
  expect(unna).toMatchObject({ identity_status: "probable", research_status: "occupation_only_found" });
  expect(unna.last_civilian_pre_service).toHaveLength(0);
  expect(unna.other_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      canonical_organization: "University of California, Berkeley",
      relationship_type: "student",
      claim_confidence: "medium",
      publication_status: "publish_qualified",
    }),
  ]);

  const unoki = await publicPerson(request, "261b84f9-c78f-5894-80e6-f05f0e2a6c1c", "Kazuo Unoki");
  expect(unoki).toMatchObject({ identity_status: "high_confidence", research_status: "requires_archival_review" });
  expect(unoki.immediate_pre_oss_affiliations).toHaveLength(0);
  expect(unoki.last_civilian_pre_service).toHaveLength(0);
  expect(unoki.other_pre_oss_affiliations).toHaveLength(0);
  expect(unoki.claims).toEqual([
    expect.objectContaining({ claim_type: "identity", claim_confidence: "high", publication_status: "published" }),
  ]);
});

test("fourteen unresolved profiles remain dignified archival-review cases", async ({ request }) => {
  for (const [id, name] of unresolvedProfiles) {
    const person = await publicPerson(request, id, name);
    expect(person).toMatchObject({
      identity_status: "unresolved",
      research_status: "requires_archival_review",
      manual_review_required: true,
    });
    expect(person.immediate_pre_oss_affiliations).toHaveLength(0);
    expect(person.last_civilian_pre_service).toHaveLength(0);
    expect(person.other_pre_oss_affiliations).toHaveLength(0);
    expect(person.claims).toHaveLength(0);
  }
});

test("Batch 974 evidence excludes secrets, full identifiers and raw bulk records", () => {
  expect(evidence).not.toMatch(/"serial_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toMatch(/"service_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toContain("NARA_API_KEY");
  expect(evidence).not.toContain("x-api-key");
  expect(evidence).not.toContain("candidate_identifier");
  expect(evidence).not.toContain("bulk_record_ordinal");
  expect(evidence).not.toMatch(/RA\d{8}/);
});

test("Batch 974 publishes exact coverage counters and preserves oil counts", async ({ request, page }) => {
  const response = await request.get("./data/stats.json");
  expect(response.ok()).toBeTruthy();
  expect(await response.json()).toMatchObject({
    source_rows: 23_978,
    person_entities: 23_936,
    possible_duplicate_groups: 664,
    research_attempted_people: 15_338,
    verified_affiliation_people: 1_102,
    verified_employer_people: 493,
    archival_review_assessed_people: 13_814,
    published_claims: 9_727,
    public_sources: 6_294,
  });
  await page.goto("./oil-companies/");
  const main = page.locator("main");
  await expect(main).toContainText("14 people");
  await expect(main).toContainText("15 historically named");
});
