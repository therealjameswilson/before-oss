import fs from "node:fs";
import { expect, test } from "@playwright/test";
import type { APIRequestContext } from "@playwright/test";

const evidence = fs.readFileSync(
  new URL(
    "../../research/evidence-page507-arthur-j-willis-to-georgia-wilson-review_batch-1017_2026-11-04.json",
    import.meta.url,
  ),
  "utf8",
);

const profiles = [
  ["43a26b83-8ed9-54f5-bc9b-5929279b2a85", "Nicholas W Willis"],
  ["35467c71-f728-5d3c-b3ba-e6aecc925d7a", "Allan A Willman"],
  ["321d3f5b-f7b5-5df8-a2c6-b2f692c4d0f9", "Donald R Willmott"],
  ["667b8a49-0a5e-5609-8eff-1bd23468a97a", "Paul R Wilner"],
  ["854bfd25-7269-590f-bcea-1479f933bfb2", "Donald C Wilson"],
  ["9de40ef5-ec1d-5a31-9f62-a89a7879ce66", "E Bright Wilson"],
  ["7f0453df-657a-5050-b409-061785a1ed0b", "Joe W Willis"],
  ["1a46608b-cf51-5566-86c6-b7a49e9562b4", "John B Willis"],
] as const;

async function publicPerson(request: APIRequestContext, id: string, name: string) {
  const response = await request.get(`./data/people/${name[0].toLowerCase()}.json`);
  expect(response.ok()).toBeTruthy();
  return (await response.json()).find(
    (item: { person_id: string }) => item.person_id === id,
  );
}

test("Batch 1017 publishes every page 507 row with a completed outcome", async ({ request }) => {
  let sourceRows = 0;
  let people = 0;
  for (const letter of [
    ..."abcdefghijklmnopqrstuvw",
    "y",
    "z",
    "other",
  ]) {
    const response = await request.get(`./data/people/${letter}.json`);
    expect(response.ok()).toBeTruthy();
    for (const person of await response.json()) {
      const rows = person.source_records.filter(
        (row: { pdf_page: number }) => row.pdf_page === 507,
      );
      if (rows.length) {
        people += 1;
        sourceRows += rows.length;
        expect(person.research_status).not.toBe("not_started");
        expect(person.research_status).not.toBe("in_progress");
        expect(JSON.stringify(person)).not.toMatch(/\b[ORW]-?\d{5,9}\b/);
      }
    }
  }
  expect(people).toBe(46);
  expect(sourceRows).toBe(46);
});

test("Allan Willman keeps Wyoming as last civilian employer, not immediate OSS", async ({ request }) => {
  const person = await publicPerson(request, profiles[1][0], profiles[1][1]);
  expect(person).toMatchObject({
    identity_status: "high_confidence",
    research_status: "verified_employer_found",
  });
  expect(person.immediate_pre_oss_affiliations).toHaveLength(0);
  expect(person.last_civilian_pre_service).toEqual([
    expect.objectContaining({
      canonical_organization: "University of Wyoming",
      relationship_type: "employment",
      temporal_basis: "strongly_date_bounded",
      claim_confidence: "high",
    }),
  ]);
});

test("Donald Willmott has a qualified exact immediate teaching pathway", async ({ request, page }) => {
  const person = await publicPerson(request, profiles[2][0], profiles[2][1]);
  expect(person).toMatchObject({
    identity_status: "high_confidence",
    research_status: "verified_employer_found",
  });
  expect(person.immediate_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      canonical_organization: "Unidentified Chinese middle school near Chengdu",
      role_title: "teacher",
      relationship_type: "employment",
      temporal_basis: "explicit_immediate",
      claim_confidence: "high",
    }),
  ]);
  await page.goto(`./people/${profiles[2][0]}/`);
  await expect(page.getByRole("heading", { name: profiles[2][1], level: 1 })).toBeVisible();
  await expect(page.locator("main")).toContainText("Unidentified Chinese middle school near Chengdu");
});

test("Donald C Wilson separates immediate Army service from civilian utility employment", async ({ request }) => {
  const person = await publicPerson(request, profiles[4][0], profiles[4][1]);
  expect(person).toMatchObject({
    identity_status: "confirmed",
    research_status: "verified_employer_found",
    personnel_category: "warrant_officer",
    commissioned_officer: false,
  });
  expect(person.immediate_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      canonical_organization: "United States Army",
      relationship_type: "military_assignment",
      temporal_basis: "explicit_immediate",
      claim_confidence: "confirmed",
    }),
  ]);
  expect(person.last_civilian_pre_service).toEqual([
    expect.objectContaining({
      canonical_organization: "Unidentified public utility company in Salem, Ohio",
      relationship_type: "employment",
      claim_confidence: "confirmed",
    }),
  ]);
});

test("Paul Wilner preserves the branch conflict and qualified civilian roles", async ({ request, page }) => {
  const person = await publicPerson(request, profiles[3][0], profiles[3][1]);
  expect(person).toMatchObject({
    identity_status: "high_confidence",
    research_status: "conflicting_sources",
    commissioned_officer: true,
  });
  expect(person.immediate_pre_oss_affiliations).toHaveLength(0);
  expect(person.last_civilian_pre_service).toEqual(
    expect.arrayContaining([
      expect.objectContaining({ canonical_organization: "Self-employed", claim_confidence: "medium" }),
      expect.objectContaining({ canonical_organization: "Georgetown University", claim_confidence: "medium" }),
    ]),
  );
  expect(person.claims).toEqual(
    expect.arrayContaining([
      expect.objectContaining({ claim_confidence: "conflicting", publication_status: "conflicting" }),
    ]),
  );
  await page.goto(`./people/${profiles[3][0]}/`);
  await expect(page.locator("main")).toContainText("conflict");
});

test("Army occupation evidence stays qualified and unnamed", async ({ request }) => {
  const person = await publicPerson(request, profiles[7][0], profiles[7][1]);
  expect(person).toMatchObject({
    identity_status: "confirmed",
    research_status: "occupation_only_found",
    personnel_category: "enlisted_army_personnel",
    commissioned_officer: false,
  });
  expect(person.immediate_pre_oss_affiliations).toHaveLength(0);
  expect(person.last_civilian_pre_service).toHaveLength(0);
  expect(person.other_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      canonical_organization: null,
      occupation: "secondary-school teacher or principal",
      claim_confidence: "medium",
      publication_status: "publish_qualified",
    }),
  ]);
});

test("identity-only and documented-prewar cases do not overclaim immediacy", async ({ request }) => {
  const nicholas = await publicPerson(request, profiles[0][0], profiles[0][1]);
  expect(nicholas).toMatchObject({
    identity_status: "high_confidence",
    research_status: "requires_archival_review",
    commissioned_officer: true,
  });
  expect(nicholas.immediate_pre_oss_affiliations).toHaveLength(0);
  expect(nicholas.last_civilian_pre_service).toHaveLength(0);

  const bright = await publicPerson(request, profiles[5][0], profiles[5][1]);
  expect(bright).toMatchObject({
    identity_status: "high_confidence",
    research_status: "documented_prewar_employer_found",
  });
  expect(bright.immediate_pre_oss_affiliations).toHaveLength(0);
  expect(bright.last_civilian_pre_service).toHaveLength(0);
  expect(bright.other_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      canonical_organization: "Harvard University",
      temporal_basis: "documented_prewar",
      claim_confidence: "high",
    }),
  ]);
});

test("Joe Willis conflicting protected-identifier candidate transfers no data", async ({ request }) => {
  const person = await publicPerson(request, profiles[6][0], profiles[6][1]);
  expect(person).toMatchObject({
    identity_status: "conflicting",
    research_status: "conflicting_sources",
  });
  expect(person.immediate_pre_oss_affiliations).toHaveLength(0);
  expect(person.last_civilian_pre_service).toHaveLength(0);
  expect(person.other_pre_oss_affiliations).toHaveLength(0);
});

test("Batch 1017 evidence excludes secrets, identifiers, and raw bulk records", () => {
  expect(evidence).not.toMatch(/"serial_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toMatch(/"service_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toContain("NARA_API_KEY");
  expect(evidence).not.toContain("x-api-key");
  expect(evidence).not.toContain("candidate_identifier");
  expect(evidence).not.toContain("bulk_record_ordinal");
  expect(evidence).not.toMatch(/\b[ORW]-?\d{5,9}\b/);
});

test("Batch 1017 coverage totals are public", async ({ request }) => {
  const response = await request.get("./data/stats.json");
  expect(response.ok()).toBeTruthy();
  const stats = await response.json();
  expect(stats).toMatchObject({
    source_rows: 23978,
    person_entities: 23935,
    research_attempted_people: 16706,
    verified_affiliation_people: 1180,
    verified_employer_people: 542,
    archival_review_assessed_people: 15186,
  });
});
