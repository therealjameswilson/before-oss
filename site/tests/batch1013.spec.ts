import fs from "node:fs";
import { expect, test } from "@playwright/test";
import type { APIRequestContext } from "@playwright/test";

const evidence = fs.readFileSync(
  new URL(
    "../../research/evidence-page503-wiener-to-wiley-review_batch-1013_2026-11-04.json",
    import.meta.url,
  ),
  "utf8",
);

const profiles = [
  ["1a09c318-edad-5b53-b5a6-e752c38e2891", "Thomas Wiener"],
  ["42b65160-afad-5cdd-84f2-b59d748ea19e", "Walter F Wiener"],
  ["1bd72a34-651e-5fad-ad01-ca4386dde398", "August I Wieners"],
  ["09b95d6e-af48-51ae-875a-56dd51e66193", "Harold J Wiens"],
  ["dcd81c36-9104-5983-89da-2e692bf44d6e", "Henry W Wieringa"],
  ["7c7a5efb-1a6f-5647-b23e-484c136a8b49", "Leona E.D. Wierum"],
  ["5237f1ae-be94-5279-a828-2ae3fe9cd318", "Walter Wierzbicki"],
  ["37d1722d-9e45-5228-94c9-daa472b73c3c", "Heinrich A Wieschhoff"],
  ["1c37314d-af73-5479-9c7a-c98b444755af", "Melvin C Wiese"],
  ["44b988a2-d0f0-5852-afd2-769b954552b7", "Clifford C Wiesen"],
  ["286b1d59-b9db-5a12-bdf1-b48165c2a72e", "Louis A Wiesner"],
  ["31b9257c-f13a-50b9-ade0-ad0b1fb9e1c7", "Donald F Wiggin"],
  ["1e334e6c-7cbe-5080-b0df-bdb164600264", "Charles W Wiggins"],
  ["08407581-67ef-52e0-ac7e-ae51d0d5a413", "Robert S Wiggins"],
  ["cb1a78c4-c52e-58b6-a68b-5f408babb4a7", "Frederick Wight"],
  ["8c0cad5e-0fa5-520b-bcb1-4e7d01bb12c5", "Louis D Wight"],
  ["70d09633-c395-59db-b065-1d4f0f851ceb", "Russell B Wight"],
  ["de221dc5-a780-5b56-8085-99abedcaca82", "Royce Wightman"],
  ["171a26db-42c9-565e-819d-94fba7d81005", "John C Wigington"],
  ["1394fbf4-a578-5c51-89d9-e3474d330405", "Robert J Wigner"],
  ["9e78c8e0-04a5-5ba0-a839-9c8c08de5f11", "Constantine A Wihtol"],
  ["544bb2dd-2960-5f20-9e14-455e9713bd4c", "Orvin I Wikoff"],
  ["046d53ed-9633-58a8-8339-1ef920bd1cbb", "John W Wikstrand"],
  ["b858c2fe-60c2-5143-bdc1-39ff82d92713", "John A Wilbert"],
  ["988b1615-a74b-5020-a82d-cbd8831f21c9", "C. Martin Wilbur"],
  ["6626039a-00cd-5019-83cf-ba7c2ee78786", "Lawrence L Wilbur Jr."],
  ["d0880868-5f3e-5e66-a151-2fef9dca3593", "Richard H Wilbur"],
  ["d2a8e5cd-25e8-5f56-bc24-c332632a27b8", "George E Wilcox"],
  ["906dfc12-2033-5a55-b215-e918d4cb0e78", "James A Wilcox"],
  ["d9373462-a1d3-5787-be85-0fd7a890afbd", "James W Wilcox"],
  ["f3e1ac0e-38c2-5f41-a736-7996f9422758", "Oliver W Wilcox"],
  ["b8b02544-5345-50b5-92d6-bce85aab0f07", "Ray Wilcox"],
  ["37950eb8-f987-562e-a9d1-672fdeb154f4", "Stanley Wilcox"],
  ["70b7d720-3821-57d3-9d87-f778baf05acf", "Isabelle S Wild"],
  ["8c157b72-9357-54b7-869b-aa3f78b904ea", "Mount G Wild"],
  ["c6f89842-e6f6-5b1e-9a41-f59914ea2365", "Norman Wild"],
  ["706f91cf-7f26-5755-b2f1-19699edc7731", "Payson S Wild"],
  ["a5d67311-8176-505a-808c-c425cddb5f2b", "John H Wilde"],
  ["926d4a3d-7c3a-5eb7-a2dc-5d383388e2c9", "Charles Wilder"],
  ["c516cb4c-9706-55a7-b726-784cde9e56f0", "Forrest G Wilder Jr."],
  ["339e3d2e-1514-555e-9f3b-f937783aafa0", "Gordon J Wilder"],
  ["8bcc4be4-f8a8-5ff9-a612-bf0e5d1b78a8", "Edith M Wildrick"],
  ["25d8d021-07c1-5a1c-b394-d9aa5a953c7d", "Charles R Wilds"],
  ["cfee7651-162f-5c02-9354-88a8166a24d2", "Arthur J Wildt"],
  ["df4f63f5-d123-543f-9741-d0de4e97b9a9", "E. David Wiley"],
  ["e787fa88-e6c7-53f2-83db-2d509a343a58", "John C Wiley"],
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

test("Batch 1013 publishes all 46 reviewed people with terminal or review outcomes", async ({ request }) => {
  for (const [id, name] of profiles) {
    const person = await publicPerson(request, id, name);
    expect(person, name).toBeTruthy();
    expect(person.research_status).not.toBe("not_started");
    expect(person.research_status).not.toBe("in_progress");
    expect(JSON.stringify(person)).not.toMatch(/\b[ORW]-?\d{5,9}\b/);
  }
});

test("all 46 page 503 rows remain separately recoverable", async ({ request }) => {
  let sourceRows = 0;
  for (const [id, name] of profiles) {
    const person = await publicPerson(request, id, name);
    sourceRows += person.source_records.filter(
      (row: { pdf_page: number }) => row.pdf_page === 503,
    ).length;
  }
  expect(sourceRows).toBe(46);
});

test("ten Army categories remain qualified and never invent employers", async ({ request }) => {
  const expected = new Map([
    [profiles[9][0], "checker"],
    [profiles[16][0], "secondary-school teacher or principal"],
    [profiles[19][0], "stenographer or typist"],
    [profiles[21][0], "motor-vehicle mechanic or repairman"],
    [profiles[25][0], "actor or actress"],
    [profiles[30][0], "machine-shop or related occupation, not elsewhere classified"],
    [profiles[32][0], "secondary-school teacher or principal"],
    [profiles[37][0], "student"],
    [profiles[39][0], "skilled worker in production of bakery products, not elsewhere classified"],
    [profiles[42][0], "student"],
  ]);
  for (const [id, occupation] of expected) {
    const name = profiles.find(([personId]) => personId === id)![1];
    const person = await publicPerson(request, id, name);
    expect(person).toMatchObject({
      personnel_category: "enlisted_army_personnel",
      commissioned_officer: false,
      research_status: "occupation_only_found",
    });
    expect(person.identity_status).toMatch(/^(confirmed|high_confidence)$/);
    expect(person.immediate_pre_oss_affiliations).toHaveLength(0);
    expect(person.last_civilian_pre_service).toHaveLength(0);
    expect(person.other_pre_oss_affiliations).toEqual([
      expect.objectContaining({
        canonical_organization: null,
        occupation,
        claim_confidence: "medium",
        publication_status: "publish_qualified",
      }),
    ]);
  }
});

test("Wieringa and Wilbert identifier conflicts remain visible and transfer no Army data", async ({ request }) => {
  for (const index of [4, 23] as const) {
    const person = await publicPerson(request, profiles[index][0], profiles[index][1]);
    expect(person).toMatchObject({
      identity_status: "conflicting",
      research_status: "conflicting_sources",
    });
    expect(person.immediate_pre_oss_affiliations).toHaveLength(0);
    expect(person.last_civilian_pre_service).toHaveLength(0);
    expect(person.other_pre_oss_affiliations).toHaveLength(0);
    expect(person.claims).toEqual([
      expect.objectContaining({
        claim_type: "identity",
        claim_confidence: "conflicting",
        publication_status: "conflicting",
      }),
    ]);
  }
});

test("Wieschhoff publishes a strongly date-bounded Penn Museum employer", async ({ request, page }) => {
  const person = await publicPerson(request, profiles[7][0], profiles[7][1]);
  expect(person).toMatchObject({
    identity_status: "high_confidence",
    personnel_category: "civilian_professional_or_administrative_grade",
    commissioned_officer: false,
    research_status: "verified_employer_found",
  });
  expect(person.immediate_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      canonical_organization: "University of Pennsylvania Museum",
      role_title: "Curator of the African Section",
      relationship_type: "employment",
      temporal_basis: "strongly_date_bounded",
      claim_confidence: "high",
    }),
  ]);
  expect(person.last_civilian_pre_service).toHaveLength(1);
  await page.goto(`./people/${profiles[7][0]}/`);
  await expect(page.getByRole("heading", { name: profiles[7][1], level: 1 })).toBeVisible();
  await expect(page.locator("main")).toContainText("University of Pennsylvania Museum");
});

test("Frederick Wight separates Naval Reserve assignment from civilian self-employment", async ({ request }) => {
  const person = await publicPerson(request, profiles[14][0], profiles[14][1]);
  expect(person).toMatchObject({
    identity_status: "confirmed",
    personnel_category: "commissioned_naval_officer",
    commissioned_officer: true,
    research_status: "verified_employer_found",
  });
  expect(person.immediate_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      canonical_organization: "United States Naval Reserve",
      relationship_type: "military_assignment",
      temporal_basis: "explicit_immediate",
    }),
  ]);
  expect(person.last_civilian_pre_service).toEqual([
    expect.objectContaining({
      canonical_organization: "Self-employed",
      role_title: "Portrait painter and writer",
      relationship_type: "self_employment",
    }),
  ]);
});

test("Louis Wiesner separates CFR immediate employment from earlier Harvard employment", async ({ request }) => {
  const person = await publicPerson(request, profiles[10][0], profiles[10][1]);
  expect(person.immediate_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      canonical_organization: "Council on Foreign Relations",
      role_title: "Research Secretary",
      temporal_basis: "explicit_immediate",
      claim_confidence: "confirmed",
    }),
  ]);
  expect(person.last_civilian_pre_service).toHaveLength(1);
  expect(person.other_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      canonical_organization: "Harvard University",
      role_title: "Graduate Assistant and Teaching Fellow",
      temporal_basis: "documented_prewar",
    }),
  ]);
});

test("Payson Wild remains temporally qualified and John Wiley remains nonpublic", async ({ request }) => {
  const payson = await publicPerson(request, profiles[36][0], profiles[36][1]);
  expect(payson).toMatchObject({
    identity_status: "high_confidence",
    research_status: "needs_temporal_review",
  });
  expect(payson.immediate_pre_oss_affiliations).toHaveLength(0);
  expect(payson.last_civilian_pre_service).toHaveLength(0);
  expect(payson.other_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      canonical_organization: "Harvard University",
      temporal_basis: "temporal_relation_uncertain",
      claim_confidence: "medium",
      publication_status: "publish_qualified",
    }),
  ]);

  const wiley = await publicPerson(request, profiles[45][0], profiles[45][1]);
  expect(wiley).toMatchObject({
    identity_status: "probable",
    research_status: "needs_identity_review",
  });
  expect(wiley.immediate_pre_oss_affiliations).toHaveLength(0);
  expect(wiley.last_civilian_pre_service).toHaveLength(0);
  expect(wiley.other_pre_oss_affiliations).toHaveLength(0);
  expect(wiley.claims).toHaveLength(0);
  expect(JSON.stringify(wiley)).not.toContain("United States Department of State");
});

test("C. Martin Wilbur retains exactly one Field Museum affiliation", async ({ request }) => {
  const person = await publicPerson(request, profiles[24][0], profiles[24][1]);
  expect(person.immediate_pre_oss_affiliations).toHaveLength(1);
  expect(person.last_civilian_pre_service).toHaveLength(1);
  expect(person.immediate_pre_oss_affiliations[0]).toMatchObject({
    canonical_organization: "Field Museum of Natural History",
    role_title: "Curator of Chinese Archaeology and Ethnology",
    temporal_basis: "explicit_immediate",
  });
  expect(person.last_civilian_pre_service[0].affiliation_id).toBe(
    person.immediate_pre_oss_affiliations[0].affiliation_id,
  );
});

test("Batch 1013 evidence excludes secrets, identifiers, and raw bulk records", () => {
  expect(evidence).not.toMatch(/"serial_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toMatch(/"service_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toContain("NARA_API_KEY");
  expect(evidence).not.toContain("x-api-key");
  expect(evidence).not.toContain("candidate_identifier");
  expect(evidence).not.toContain("bulk_record_ordinal");
  expect(evidence).not.toMatch(/\b[ORW]-?\d{5,9}\b/);
});

test("Batch 1013 public claims retain inspectable short citations", async ({ request }) => {
  const claimIndexes = [4, 7, 9, 10, 14, 16, 19, 21, 23, 24, 25, 30, 32, 36, 37, 39, 42] as const;
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
