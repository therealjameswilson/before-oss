import fs from "node:fs";
import { expect, test } from "@playwright/test";
import type { APIRequestContext } from "@playwright/test";

const evidence = fs.readFileSync(
  new URL(
    "../../research/evidence-page495-weichbrodt-to-weisberg-review_batch-1005_2026-11-03.json",
    import.meta.url,
  ),
  "utf8",
);

const profiles = [
  ["96380515-34a4-54d4-af42-67d1c36f8f95", "Ray J Weichbrodt"],
  ["9a974e19-d4d8-5c62-9ffd-eef3784e8378", "William H Weick"],
  ["ee26e0c9-77a6-57d0-8e1c-6b5fa6f2010c", "Edward R Weickel Jr."],
  ["dc0d35bf-f811-5d25-8494-35d79874ae66", "Frederick P Weidner"],
  ["7a47aa95-93d7-5d35-adfc-e8027664a58d", "Ernest G Weidul"],
  ["99a8c9da-698d-5daa-a64b-3b780fd8a59b", "Guido G Weigend"],
  ["adcb2aa1-2d70-5fae-9f1b-aa49b37f4567", "Mary E Weikel"],
  ["bfbba608-2723-546a-9bf6-fbd7e4f64c12", "Billie A Weil"],
  ["d456d2fa-5d89-56a8-9aa0-ef15876c2ea0", "Morris Weil"],
  ["cf879662-102b-560d-8c1c-d106412d43ec", "Morris Weil"],
  ["a627a7ef-519a-5052-bc41-e799915a1463", "Richard Weil Jr."],
  ["d8ad01d0-cf9e-50c5-9184-db58ae03d50d", "Charles H Weilamann Jr."],
  ["dc480af6-f4b6-5bf7-b0c8-d132d047d293", "Robert J Weiler"],
  ["27184007-d820-53a0-a4c4-1773857b839f", "Otto Weill"],
  ["e56df687-2d94-56c2-a934-7e448d5b7637", "Ruth Weiller"],
  ["0c21257e-626d-5259-b0bc-e2f0771e49da", "Robert P Weimann"],
  ["215294cb-acef-55a3-8c29-8bcf65344475", "Marian E Weimer"],
  ["38069ad6-69b5-55af-9be5-751947e67f45", "Albert K Weinberg"],
  ["bcbb680f-0b79-5d7f-b1c1-d64110b2fe7b", "Edgar Weinberg"],
  ["990bfb96-b0cd-5897-acd9-f4b799b6604b", "Irving Weinberg"],
  ["95ea5da4-9589-5f3e-bfd8-add668877113", "Abraham Weiner"],
  ["3e4d54bc-f5e0-5681-9494-bb05129eceb6", "Daniel J Weiner"],
  ["47cb41f9-98c7-5168-b8a7-fa3978bbd857", "Daniel J Weiner"],
  ["1ef133ec-c826-5a17-b9c1-b7b17e5de822", "George Weiner"],
  ["200f7993-0eb6-50d9-8bcf-6645ec74fadc", "George Weiner"],
  ["82e0b6ac-d40d-5815-8fe3-e4046e26d65a", "Gerald I Weiner"],
  ["757ea55f-be27-5da0-b167-ebb5638ae950", "Irving R Weiner"],
  ["6a500891-e969-5f82-8795-d873bbcb657b", "Louis L Weiner"],
  ["9527f68e-1811-5aa6-bace-aca9f0a83183", "Martin J Weiner"],
  ["8eefdaba-3e61-5954-b660-81f3a8645fd5", "Samuel S Weinfeld"],
  ["1a500550-8c9f-5a45-9d21-e22a2387ded9", "Robert F Weingartner"],
  ["f76ffe3b-f960-583e-872a-2ae345aa0f0b", "Louis Weinman"],
  ["b22480d2-e3e4-5b91-94a1-31f9cb0db9b4", "Walter E Weinmann"],
  ["90eb1d9b-d9f1-5f23-a785-278f645eacd6", "Marcel I Weinrich"],
  ["2216ca28-872d-5b1e-92b0-7f5a623825e7", "Leo Weinstein"],
  ["7c899093-f52d-5a67-b610-462e891d463d", "Lionel I Weinstock"],
  ["a62731cd-5f4b-5aa1-b67c-16412413ee2e", "Monroe Weinstock"],
  ["ad99cb59-4129-596d-b7d2-0f8eb860030b", "Lewis R Weintraub"],
  ["73f3649a-d598-5791-bac4-e72405339859", "R E Weinzettel"],
  ["a402fdf7-1059-5522-aeb8-4cdde5ec31b7", "Donald E Weir"],
  ["cb767798-9c5d-580c-a957-a421c97b3030", "Marjorie Q Weir"],
  ["99a0375c-4912-5478-bf66-8bd3e433fa23", "Siegfried H Weir"],
  ["4dad4fa3-09da-5d34-bc46-f7e1027d8caf", "Thomas A Weir"],
  ["a7105a68-9492-5d7f-89aa-030a3ecdfab7", "George B Weisback"],
  ["e57be43b-4812-5e91-8a90-9c73c62b7484", "Walter G Weisbecker"],
  ["d0bdcbdd-a1da-5f4c-adea-c5dfde35ed77", "Harold Weisberg"],
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

test("Batch 1005 publishes all 46 audited people with terminal outcomes", async ({ page }) => {
  for (const [id, name] of profiles) {
    await page.goto(`./people/${id}/`);
    await expect(page.getByRole("heading", { name, level: 1 })).toBeVisible();
    const main = page.locator("main");
    await expect(main).not.toContainText("not started");
    await expect(main).not.toContainText("in progress");
    await expect(main).not.toContainText(/\b[ORW]-?\d{5,9}\b/);
  }
});

test("fifteen Army categories remain bounded and never invent employers", async ({ request }) => {
  const expected = new Map([
    [profiles[2][0], ["student", "student"]],
    [profiles[11][0], ["toolmaker or die sinker and setter", "unknown"]],
    [profiles[20][0], ["manufacturing foreman", "unknown"]],
    [profiles[21][0], ["student", "student"]],
    [profiles[23][0], ["accountant or auditor", "unknown"]],
    [profiles[28][0], ["student", "student"]],
    [profiles[29][0], ["shipping and receiving clerk", "unknown"]],
    [profiles[30][0], ["lawyer or judge", "unknown"]],
    [profiles[31][0], ["carpenter", "unknown"]],
    [profiles[34][0], ["student", "student"]],
    [profiles[35][0], ["student", "student"]],
    [profiles[36][0], ["student", "student"]],
    [profiles[37][0], ["actor", "unknown"]],
    [profiles[39][0], ["draftsman", "unknown"]],
    [profiles[44][0], ["author, editor, or reporter", "unknown"]],
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

test("Richard Weil separates the immediate Bamberger employer from earlier Macy work", async ({ request }) => {
  const person = await publicPerson(request, profiles[10][0], profiles[10][1]);
  expect(person).toMatchObject({
    identity_status: "confirmed",
    personnel_category: "commissioned_army_officer",
    commissioned_officer: true,
    research_status: "verified_employer_found",
  });
  expect(person.immediate_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      canonical_organization: "L. Bamberger & Company",
      role_title: "President",
      relationship_type: "employment",
      temporal_basis: "explicit_immediate",
      claim_confidence: "confirmed",
    }),
  ]);
  expect(person.last_civilian_pre_service).toEqual([
    expect.objectContaining({ canonical_organization: "L. Bamberger & Company" }),
  ]);
  expect(person.other_pre_oss_affiliations).toEqual(
    expect.arrayContaining([
      expect.objectContaining({ canonical_organization: "R. H. Macy & Company" }),
    ]),
  );
});

test("Harold Weisberg separates Army, freelance, magazine, and Senate evidence", async ({ request }) => {
  const person = await publicPerson(request, profiles[45][0], profiles[45][1]);
  expect(person).toMatchObject({
    identity_status: "confirmed",
    personnel_category: "enlisted_army_personnel",
    commissioned_officer: false,
    research_status: "verified_employer_found",
  });
  expect(person.immediate_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      canonical_organization: "United States Army",
      relationship_type: "military_assignment",
    }),
  ]);
  expect(person.last_civilian_pre_service).toEqual([
    expect.objectContaining({
      canonical_organization: "Self-employed",
      relationship_type: "self_employment",
      occupation: "journalist and writer",
    }),
  ]);
  expect(person.other_pre_oss_affiliations).toEqual(
    expect.arrayContaining([
      expect.objectContaining({ canonical_organization: "Click magazine", relationship_type: "professional_affiliation" }),
      expect.objectContaining({ canonical_organization: "U.S. Senate Civil Liberties Committee", relationship_type: "employment" }),
    ]),
  );
  expect(JSON.stringify(person)).not.toContain("Code 940");
});

test("Guido Weigend publishes student status without converting Chicago into an employer", async ({ request }) => {
  const person = await publicPerson(request, profiles[5][0], profiles[5][1]);
  expect(person).toMatchObject({
    identity_status: "high_confidence",
    research_status: "completed",
  });
  expect(person.immediate_pre_oss_affiliations).toHaveLength(0);
  expect(person.last_civilian_pre_service).toHaveLength(0);
  expect(person.other_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      canonical_organization: "University of Chicago",
      relationship_type: "student",
      role_title: "Student",
    }),
  ]);
});

test("the two George Weiner rows remain separate and the conflicting row gets no Army occupation", async ({ request }) => {
  const supported = await publicPerson(request, profiles[23][0], profiles[23][1]);
  const conflicting = await publicPerson(request, profiles[24][0], profiles[24][1]);
  expect(supported).toMatchObject({
    identity_status: "confirmed",
    research_status: "occupation_only_found",
  });
  expect(conflicting).toMatchObject({
    identity_status: "conflicting",
    research_status: "conflicting_sources",
  });
  expect(supported.person_id).not.toBe(conflicting.person_id);
  expect(supported.possible_duplicate_group).toBeTruthy();
  expect(conflicting.possible_duplicate_group).toBe(
    supported.possible_duplicate_group,
  );
  expect(conflicting.other_pre_oss_affiliations).toHaveLength(0);
  expect(conflicting.claims).toEqual([
    expect.objectContaining({ claim_confidence: "conflicting", publication_status: "conflicting" }),
  ]);
});

test("post-OSS Army-entry records are not published as pre-OSS occupations", async ({ request }) => {
  for (const index of [15, 43] as const) {
    const person = await publicPerson(request, profiles[index][0], profiles[index][1]);
    expect(person).toMatchObject({
      identity_status: "high_confidence",
      research_status: "requires_archival_review",
    });
    expect(person.immediate_pre_oss_affiliations).toHaveLength(0);
    expect(person.last_civilian_pre_service).toHaveLength(0);
    expect(person.other_pre_oss_affiliations).toHaveLength(0);
  }
});

test("printed officer, enlisted, and civilian categories remain distinct", async ({ request }) => {
  const richard = await publicPerson(request, profiles[10][0], profiles[10][1]);
  const louis = await publicPerson(request, profiles[27][0], profiles[27][1]);
  const lionel = await publicPerson(request, profiles[35][0], profiles[35][1]);
  const weinzettel = await publicPerson(request, profiles[38][0], profiles[38][1]);
  const thomas = await publicPerson(request, profiles[42][0], profiles[42][1]);
  expect(richard).toMatchObject({ personnel_category: "commissioned_army_officer", commissioned_officer: true });
  expect(louis).toMatchObject({ personnel_category: "commissioned_army_officer", commissioned_officer: true });
  expect(lionel).toMatchObject({ personnel_category: "enlisted_army_personnel", commissioned_officer: false });
  expect(weinzettel).toMatchObject({ personnel_category: "civilian_professional_or_administrative_grade", commissioned_officer: false });
  expect(thomas).toMatchObject({ personnel_category: "civilian_professional_or_administrative_grade", commissioned_officer: false });
});

test("Batch 1005 evidence excludes secrets, identifiers, and raw bulk records", () => {
  expect(evidence).not.toMatch(/"serial_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toMatch(/"service_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toContain("NARA_API_KEY");
  expect(evidence).not.toContain("x-api-key");
  expect(evidence).not.toContain("candidate_identifier");
  expect(evidence).not.toContain("bulk_record_ordinal");
  expect(evidence).not.toMatch(/\b[ORW]-?\d{5,9}\b/);
});

test("Batch 1005 public claims retain inspectable short citations", async ({ request }) => {
  for (const index of [2, 5, 10, 11, 15, 20, 21, 23, 24, 28, 29, 30, 31, 34, 35, 36, 37, 39, 43, 44, 45] as const) {
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
