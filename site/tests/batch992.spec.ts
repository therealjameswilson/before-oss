import fs from "node:fs";
import { expect, test } from "@playwright/test";
import type { APIRequestContext } from "@playwright/test";

const evidence = fs.readFileSync(
  new URL(
    "../../research/evidence-page486-vyhnal-to-wadsworth-review_batch-992_2026-11-03.json",
    import.meta.url,
  ),
  "utf8",
);

const profiles = [
  ["6c54d837-08b0-5ea8-ac67-20a5a9dac9ed", "William Vyhnal"],
  ["ec9478ce-7f0d-5119-a623-35b1d85606f1", "Henry Waas"],
  ["104c6d8f-56ef-574c-83c9-a77be88717b0", "Bertus Harry Wabeke"],
  ["43702028-77fa-508f-87ba-611149fc00b3", "Daniel L Wachner"],
  ["7dfbbef1-b7c6-5180-9b1c-39c3e3f5ad71", "Ruth M Wachs"],
  ["ff3e3bf6-50ff-584e-b4bd-93f375eb53ae", "John E Wachsmuth"],
  ["7dfb0209-7e0e-5d19-8124-3b873e0f3264", "Robert A Wacht"],
  ["513fca2b-f391-5b4c-829d-45742f5d887f", "Ruth E Waddell"],
  ["483e3bc7-e5d7-5242-8201-7d9906eb0b6f", "William E Waddell"],
  ["a71edd00-2296-51ea-8c61-bb85eee7aa0c", "Catherine Wade"],
  ["e32621a4-ab2c-585b-8e57-0b8d866e8dfc", "Charles S Wade"],
  ["6c4fc1e4-c315-5a60-93b4-177def3c7506", "Emmitt M Wade"],
  ["ff583686-338b-5109-b433-5843d0e20780", "Grant H Wade"],
  ["dadf7da5-596b-5b2a-9c79-042bb37f0476", "Nena Violet Wade"],
  ["ba820870-b924-56f4-8a09-8d231f4550c2", "Stanley F Wade"],
  ["5035b1e1-ea6f-5fe2-a516-3087c26dd204", "Alfred Inge Wadell"],
  ["9aab06e7-109d-5b25-88fa-8cd1bf095ece", "Frank Wadena"],
  ["956c1940-c4ea-585d-a9d9-fa55bafb651b", "Mildred B Wadkins"],
  ["454be13a-b545-548c-8b6e-2d4d7e19e483", "Julia F Wadleigh"],
  ["88ce0a53-fea0-5b8e-8e06-81f2b9f91bdf", "Frederick J Wadley III"],
  ["c5c9705a-3a43-552c-bb27-bb097a531f17", "Milton J Wadlow"],
  ["818022e6-813b-5f18-84b3-bae818d7ee84", "Harold E Wadman"],
  ["82f8e2aa-c474-5b1a-90d9-190b1e567b5c", "Claude V Wadsworth"],
] as const;

async function publicPerson(request: APIRequestContext, id: string, name: string) {
  const first = name[0].toLowerCase();
  const shard = /^[a-z]$/.test(first) ? first : "other";
  const response = await request.get(`./data/people/${shard}.json`);
  expect(response.ok()).toBeTruthy();
  return (await response.json()).find((item: { person_id: string }) => item.person_id === id);
}

test("Batch 992 publishes all 23 audited people with terminal outcomes", async ({ page }) => {
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

test("Wabeke remains a qualified identity lead without a pre-OSS employer", async ({ request }) => {
  const person = await publicPerson(request, profiles[2][0], profiles[2][1]);
  expect(person).toMatchObject({
    identity_status: "probable",
    research_status: "requires_archival_review",
  });
  expect(person.immediate_pre_oss_affiliations).toHaveLength(0);
  expect(person.last_civilian_pre_service).toHaveLength(0);
  expect(person.other_pre_oss_affiliations).toHaveLength(0);
  expect(person.claims).toEqual([
    expect.objectContaining({
      claim_type: "identity",
      claim_confidence: "medium",
      publication_status: "publish_qualified",
    }),
  ]);
});

test("Wachsmuth's Minnesota ROTC evidence is student status, not employment", async ({ request }) => {
  const person = await publicPerson(request, profiles[5][0], profiles[5][1]);
  expect(person).toMatchObject({
    identity_status: "probable",
    research_status: "requires_archival_review",
  });
  expect(person.immediate_pre_oss_affiliations).toHaveLength(0);
  expect(person.last_civilian_pre_service).toHaveLength(0);
  expect(person.other_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      canonical_organization: "University of Minnesota",
      relationship_type: "student",
      temporal_basis: "temporal_relation_uncertain",
      claim_confidence: "medium",
      publication_status: "publish_qualified",
    }),
  ]);
  expect(person.commissioned_officer).toBeNull();
});

test("Army occupation categories remain qualified and never become employers", async ({ request }) => {
  const wade = await publicPerson(request, profiles[10][0], profiles[10][1]);
  expect(wade).toMatchObject({
    identity_status: "confirmed",
    personnel_category: "enlisted_army_personnel",
    commissioned_officer: false,
    research_status: "occupation_only_found",
  });
  expect(wade.last_civilian_pre_service).toHaveLength(0);
  expect(wade.other_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      canonical_organization: null,
      occupation: "repairmen and mechanics, n.e.c.",
      relationship_type: "employment",
      claim_confidence: "medium",
      publication_status: "publish_qualified",
    }),
  ]);

  const wadley = await publicPerson(request, profiles[19][0], profiles[19][1]);
  expect(wadley).toMatchObject({
    identity_status: "confirmed",
    personnel_category: "enlisted_army_personnel",
    commissioned_officer: false,
    research_status: "occupation_only_found",
  });
  expect(wadley.last_civilian_pre_service).toHaveLength(0);
  expect(wadley.other_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      canonical_organization: null,
      occupation: "policemen and detectives, public service",
      relationship_type: "employment",
      claim_confidence: "medium",
      publication_status: "publish_qualified",
    }),
  ]);
});

test("unresolved Batch 992 people retain empty claims and archival guidance", async ({ request }) => {
  for (const index of [0, 1, 3, 4, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 20, 21, 22] as const) {
    const person = await publicPerson(request, profiles[index][0], profiles[index][1]);
    expect(person).toMatchObject({
      identity_status: "unresolved",
      research_status: "requires_archival_review",
    });
    expect(person.immediate_pre_oss_affiliations).toHaveLength(0);
    expect(person.last_civilian_pre_service).toHaveLength(0);
    expect(person.other_pre_oss_affiliations).toHaveLength(0);
    expect(person.claims).toHaveLength(0);
    expect(person.archival_file.review_priority).toBe("high");
  }
});

test("Batch 992 evidence excludes secrets, full identifiers and raw bulk records", () => {
  expect(evidence).not.toMatch(/"serial_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toMatch(/"service_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toContain("NARA_API_KEY");
  expect(evidence).not.toContain("x-api-key");
  expect(evidence).not.toContain("candidate_identifier");
  expect(evidence).not.toContain("bulk_record_ordinal");
  expect(evidence).not.toMatch(/RA\d{8}/);
});

test("Batch 992 public claims retain inspectable source citations", async ({ request }) => {
  for (const index of [2, 5, 10, 19] as const) {
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

test("Batch 992 publishes exact coverage counters", async ({ request }) => {
  const response = await request.get("./data/stats.json");
  expect(response.ok()).toBeTruthy();
  expect(await response.json()).toMatchObject({
    source_rows: 23_978,
    person_entities: 23_936,
    possible_duplicate_groups: 679,
    research_attempted_people: 15_748,
    verified_affiliation_people: 1_138,
    verified_employer_people: 516,
    archival_review_assessed_people: 14_223,
    published_claims: 10_075,
    public_sources: 6_488,
  });
});
