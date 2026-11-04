import fs from "node:fs";
import { expect, test } from "@playwright/test";
import type { APIRequestContext } from "@playwright/test";

const evidence = fs.readFileSync(
  new URL(
    "../../research/evidence-page496-weisch-to-wellman-review_batch-1006_2026-11-03.json",
    import.meta.url,
  ),
  "utf8",
);

const profiles = [
  ["9637eb7f-fd8b-591d-961c-07b57e8d9096", "William S Weisch"],
  ["a3862cc4-56d0-509d-af6e-6cbb352f2da0", "Willis Weisenborn"],
  ["e14df31e-236d-53f3-a4e3-626965df7a95", "Paul R Weisenford"],
  ["1e7f7717-f628-5999-bded-cbf57a761ec1", "Emanuel Weisgal"],
  ["a93ce7da-b421-5fcf-bfee-efafad927472", "Jacob Weisman"],
  ["c77ecc8d-345c-5189-9ed8-a8027272b351", "Edwin Weismantel"],
  ["22fa4603-6ad9-5a98-be2b-c2f3a3a88a14", "Edward Ronald Weismiller"],
  ["ca18d8c7-089b-5ff5-91b5-7f63233923ed", "Edward E Weiss"],
  ["a7945de2-80cd-5d70-aae0-9eaf866bd91d", "Harry Weiss"],
  ["eeb310fa-1944-5a96-9212-027020f49ad7", "Karl Weiss"],
  ["7c1acf69-cc93-521c-93b3-e43a4aa6232e", "Rudi Weiss"],
  ["2ee57559-2ce6-5e46-8848-c2a67d85a93d", "Sendor Weiss"],
  ["1d342508-e680-5225-8071-2c75faa82694", "William P Weiss"],
  ["246f2907-7acd-5948-a63e-9e4e99c5b0cc", "Russell G Weissinger"],
  ["c6f635c3-896e-5df3-b150-1e24386ffdfd", "Russell G Weissinger"],
  ["93a1ba96-127b-54e6-a363-ef67b0ae534a", "Aaron Weissman"],
  ["a300df26-e40b-5e5e-b31b-ac36c2be6432", "Bessie Weissman"],
  ["4f4025b2-b66b-57aa-94b6-93fbea65a5c2", "Ferdinand Weiszmann"],
  ["3797df38-fe99-52d2-9e81-f59e67d3f3d0", "Helen C Weitzel"],
  ["9f0fbc25-551e-58f5-ac40-e90147bd5176", "Benjamin Weitzner"],
  ["ffb9bbf5-6ce0-5baf-ab96-104e73a398fc", "Richard A Wejmar"],
  ["80ca1776-8667-5939-8f3a-5712c5126776", "Charles P Welbon"],
  ["10e1db43-0ff5-5dd5-8220-a3059c6d6d68", "Emily Welborn"],
  ["7a004eec-ed3f-553d-a6e4-45780ae6e50d", "Caroline H Welch"],
  ["808a46e0-d844-5437-89a3-6449c92cd14a", "Edward J Welch"],
  ["7d07895d-cd12-54db-83f7-65f4c22824b7", "James S Welch"],
  ["01467b07-f41e-5452-863d-8114b52a1184", "John F Welch"],
  ["3ceb7696-7c1a-5f4c-8ad2-7f7d2f5ee07b", "John F Welch"],
  ["7a2a94d6-06f0-555b-81b6-efaf7b6a00f1", "Joseph H Welch"],
  ["08383c20-3c71-5753-b56a-0679d25be7b6", "Richard E Welch"],
  ["c1e94569-7096-530f-b753-811f6d009022", "Wallace C Welch"],
  ["8eed9943-03da-5666-a317-f9daf372b463", "John D Welchel"],
  ["f81ffd12-2b4e-5bfc-b7ca-97b74f583dcf", "Marie F Welcome"],
  ["933646ec-234f-5c2e-ac61-7abc2f7657c1", "Jerome H Weld"],
  ["3c8d0cb6-6673-54f8-bdf9-4f4b4b6438c9", "Philip S Weld"],
  ["c522721c-6d0c-51d8-b0d4-72eb9101bb01", "Henry H Weldon"],
  ["dbb89959-c2c2-5271-bb69-cf37c1670a93", "Ella Welker"],
  ["d4cd2777-53b5-5d78-be57-a445464317a3", "David M Well"],
  ["423b1e4a-f36c-5191-a377-f99b529f5979", "Clement F Wellein"],
  ["1b059e1e-f463-5175-90a2-efa55e940ffc", "Marilyn R Wellemeyer"],
  ["fe98259e-0671-5ebb-a1a1-e3b6f7c06e47", "Benjamin Welles"],
  ["3441c9db-b396-5d18-a62a-2f9b27c10975", "Charles B Welles"],
  ["6ec0023a-4cae-53a3-bc69-7a3b3891f415", "Edward O Welles"],
  ["64a3024e-c2cd-5209-8af7-8b968218d485", "Walter C Wellman"],
  ["13d07abd-6746-5708-923d-b56d63621f34", "Walter J Wellman"],
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

test("Batch 1006 publishes all 45 reviewed people with terminal outcomes", async ({ page }) => {
  for (const [id, name] of profiles) {
    await page.goto(`./people/${id}/`);
    await expect(page.getByRole("heading", { name, level: 1 })).toBeVisible();
    const main = page.locator("main");
    await expect(main).not.toContainText("not started");
    await expect(main).not.toContainText("in progress");
    await expect(main).not.toContainText(/\b[ORW]-?\d{5,9}\b/);
  }
});

test("all 46 source rows remain recoverable after the reviewed Weismiller merge", async ({ request }) => {
  let sourceRows = 0;
  for (const [id, name] of profiles) {
    const person = await publicPerson(request, id, name);
    sourceRows += person.source_records.length;
  }
  expect(sourceRows).toBe(46);

  const weismiller = await publicPerson(request, profiles[6][0], profiles[6][1]);
  expect(weismiller.source_records).toHaveLength(2);
  expect(weismiller.source_records).toEqual(
    expect.arrayContaining([
      expect.objectContaining({ indexed_first_name: "Edward", indexed_middle: "R", rank_as_indexed: "1st Lt.", pdf_page: 496 }),
      expect.objectContaining({ indexed_first_name: "Edward Ronal", indexed_middle: null, pdf_page: 496 }),
    ]),
  );
});

test("twelve Army occupation categories remain qualified and never invent employers", async ({ request }) => {
  const expected = new Map([
    [profiles[2][0], ["chauffeur or driver", "unknown"]],
    [profiles[8][0], ["sales clerk", "unknown"]],
    [profiles[10][0], ["leather-manufacturing occupation", "unknown"]],
    [profiles[11][0], ["retail manager", "unknown"]],
    [profiles[14][0], ["photographic-process occupation", "unknown"]],
    [profiles[15][0], ["photographer", "unknown"]],
    [profiles[21][0], ["secretary", "unknown"]],
    [profiles[25][0], ["student", "student"]],
    [profiles[27][0], ["bartender", "unknown"]],
    [profiles[29][0], ["student", "student"]],
    [profiles[31][0], ["motor-vehicle mechanic", "unknown"]],
    [profiles[38][0], ["sales clerk", "unknown"]],
  ]);
  for (const [id, [occupation, relationship]] of expected) {
    const name = profiles.find(([personId]) => personId === id)![1];
    const person = await publicPerson(request, id, name);
    expect(person).toMatchObject({
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

test("Joseph Welch's late Army record remains identity evidence only", async ({ request }) => {
  const person = await publicPerson(request, profiles[28][0], profiles[28][1]);
  expect(person).toMatchObject({
    identity_status: "high_confidence",
    personnel_category: "enlisted_army_personnel",
    research_status: "requires_archival_review",
  });
  expect(person.immediate_pre_oss_affiliations).toHaveLength(0);
  expect(person.last_civilian_pre_service).toHaveLength(0);
  expect(person.other_pre_oss_affiliations).toHaveLength(0);
  expect(JSON.stringify(person)).not.toContain("manager");
});

test("Edward Weismiller keeps immediate, civilian, and earlier affiliations distinct", async ({ request }) => {
  const person = await publicPerson(request, profiles[6][0], profiles[6][1]);
  expect(person).toMatchObject({
    display_name: "Edward Ronald Weismiller",
    identity_status: "confirmed",
    personnel_category: "commissioned_marine_corps_officer",
    commissioned_officer: true,
    research_status: "documented_prewar_employer_found",
  });
  expect(person.immediate_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      canonical_organization: "Harvard University",
      role_title: "Teacher",
      relationship_type: "employment",
      temporal_basis: "probable_immediate",
      claim_confidence: "medium",
      publication_status: "publish_qualified",
    }),
  ]);
  expect(person.last_civilian_pre_service).toEqual([
    expect.objectContaining({ canonical_organization: "Harvard University", relationship_type: "employment" }),
  ]);
  expect(person.other_pre_oss_affiliations).toEqual(
    expect.arrayContaining([
      expect.objectContaining({ canonical_organization: "Cornell College", relationship_type: "student" }),
      expect.objectContaining({ canonical_organization: "University of Oxford", relationship_type: "student" }),
      expect.objectContaining({ canonical_organization: "Random House", relationship_type: "employment" }),
    ]),
  );
});

test("Benjamin Welles separates the Army pathway from his Times employer", async ({ request }) => {
  const person = await publicPerson(request, profiles[40][0], profiles[40][1]);
  expect(person).toMatchObject({
    identity_status: "confirmed",
    personnel_category: "commissioned_army_officer",
    commissioned_officer: true,
    research_status: "verified_employer_found",
  });
  expect(person.immediate_pre_oss_affiliations).toEqual([
    expect.objectContaining({ canonical_organization: "United States Army", relationship_type: "military_assignment" }),
  ]);
  expect(person.last_civilian_pre_service).toEqual([
    expect.objectContaining({
      canonical_organization: "The New York Times",
      role_title: "News clerk",
      relationship_type: "employment",
      temporal_basis: "strongly_date_bounded",
      claim_confidence: "high",
    }),
  ]);
  expect(person.other_pre_oss_affiliations).toEqual([
    expect.objectContaining({ canonical_organization: "Harvard University", relationship_type: "student" }),
  ]);
});

test("Edward Welles publishes a bounded British-intelligence pathway, not an employer", async ({ request }) => {
  const person = await publicPerson(request, profiles[42][0], profiles[42][1]);
  expect(person).toMatchObject({ identity_status: "high_confidence", research_status: "completed" });
  expect(person.immediate_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      canonical_organization: "British intelligence service (unspecified)",
      relationship_type: "government_assignment",
      temporal_basis: "explicit_immediate",
      claim_confidence: "high",
    }),
  ]);
  expect(person.last_civilian_pre_service).toHaveLength(0);
  expect(person.other_pre_oss_affiliations).toEqual([
    expect.objectContaining({ canonical_organization: "Yale University", relationship_type: "student" }),
  ]);
});

test("qualified student leads stay visible without becoming employers", async ({ request }) => {
  const expected = [
    [profiles[3], "Harvard University", "temporal_relation_uncertain"],
    [profiles[34], "Harvard University", "documented_prewar"],
    [profiles[39], "Bryn Mawr College", "temporal_relation_uncertain"],
  ] as const;
  for (const [[id, name], organization, temporalBasis] of expected) {
    const person = await publicPerson(request, id, name);
    expect(person.research_status).toBe("requires_archival_review");
    expect(person.immediate_pre_oss_affiliations).toHaveLength(0);
    expect(person.last_civilian_pre_service).toHaveLength(0);
    expect(person.other_pre_oss_affiliations).toEqual([
      expect.objectContaining({
        canonical_organization: organization,
        relationship_type: "student",
        temporal_basis: temporalBasis,
        claim_confidence: "medium",
        publication_status: "publish_qualified",
      }),
    ]);
  }
});

test("same-name Weissinger and Welch rows remain separate cautious entities", async ({ request }) => {
  for (const [leftIndex, rightIndex] of [[13, 14], [26, 27]] as const) {
    const left = await publicPerson(request, profiles[leftIndex][0], profiles[leftIndex][1]);
    const right = await publicPerson(request, profiles[rightIndex][0], profiles[rightIndex][1]);
    expect(left.person_id).not.toBe(right.person_id);
    expect(left.possible_duplicate_group).toBeTruthy();
    expect(right.possible_duplicate_group).toBe(left.possible_duplicate_group);
    expect(left.identity_status).toBe("unresolved");
    expect(left.other_pre_oss_affiliations).toHaveLength(0);
    expect(right.identity_status).toBe("confirmed");
    expect(right.other_pre_oss_affiliations).toHaveLength(1);
  }
});

test("Batch 1006 evidence excludes secrets, identifiers, and raw bulk records", () => {
  expect(evidence).not.toMatch(/"serial_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toMatch(/"service_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toContain("NARA_API_KEY");
  expect(evidence).not.toContain("x-api-key");
  expect(evidence).not.toContain("candidate_identifier");
  expect(evidence).not.toContain("bulk_record_ordinal");
  expect(evidence).not.toMatch(/\b[ORW]-?\d{5,9}\b/);
});

test("Batch 1006 public claims retain inspectable short citations", async ({ request }) => {
  const claimProfiles = [2, 3, 6, 8, 10, 11, 14, 15, 21, 25, 27, 28, 29, 31, 34, 38, 39, 40, 42] as const;
  for (const index of claimProfiles) {
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
