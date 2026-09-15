import { expect, test } from "@playwright/test";
import fs from "node:fs";

const people = JSON.parse(
  fs.readFileSync(new URL("../src/data/generated/people.json", import.meta.url), "utf8"),
);
const stats = JSON.parse(
  fs.readFileSync(new URL("../src/data/generated/stats.json", import.meta.url), "utf8"),
);
const evidence = fs.readFileSync(
  new URL(
    "../../research/evidence-page-one-hundred-and-six-john-j-davidson-through-f-t-davies-pathways_batch-533_2026-09-14.json",
    import.meta.url,
  ),
  "utf8",
);
const profile = (id: string) =>
  people.find((person: { person_id: string }) => person.person_id === id);

const cohort = [
  ["cdda339e-ab68-596d-96cd-7a0b8ce05e6d", "John J Davidson", "46a861b5-2876-5cd1-8f10-df5884302e1b", true],
  ["2b3786dd-e97b-5cbc-830d-40ee51ad3952", "John T Davidson Jr.", "2d36c293-f571-5f9d-8f4b-76f827a74f28", true],
  ["44e80b12-0d77-5556-83fa-8623dbc8932e", "Kenneth E Davidson", "80a55bc3-8d60-5988-87a0-17fd416c8512", true],
  ["734db315-13e2-513a-a730-fa0f45080ddc", "Milton Davidson", "11216c4d-4c0d-5f87-a343-03d5f3f8e16d", false],
  ["fc3ff118-01f7-56ca-83c8-30a0bca61810", "Rebecca D Davidson", "91c7bdde-a473-5cbd-b51d-d8ea530eec2b", false],
  ["ed9a0f14-c3b5-5b7e-a72a-58f2aad9afac", "Thomas Davidson", "8024ebd5-a5ca-5658-9eac-f0359dea294d", false],
  ["4a1c57e1-7052-5f8c-92b1-428fc2a1ccae", "Alfred Davies", "f8fb50c2-aa1e-5ac5-a169-56f46d8e1026", false],
  ["49696b15-fe98-5137-a67f-fd4d6fd7bfc7", "David M Davies", "70266235-7a83-5daf-97d3-18f25ed28fe8", false],
  ["c0e63e3a-b4a1-516f-85f1-ef82211524f7", "Elspeth V Davies", "aad3a81a-d041-5d2c-b9b0-b3ff875dd4df", false],
  ["991d1a51-9960-52bb-ba4b-a0ff4b44b7a6", "F T Davies", "4fa1cf61-e4ff-5e9d-95e7-826fb058d1da", false],
] as const;

test("Batch 533 preserves page 106 rows 36-45 and masks every private field", () => {
  for (const [id, name, sourceRecordId, hasPrivateIdentifier] of cohort) {
    const person = profile(id);
    expect(person).toMatchObject({ display_name: name });
    const sourceRecord = person.source_records.find(
      (record: { source_record_id: string }) => record.source_record_id === sourceRecordId,
    );
    expect(sourceRecord).toMatchObject({ archive_location: "230/86/29/06", box: "169", pdf_page: 106 });
    if (hasPrivateIdentifier) {
      expect(sourceRecord.serial_masked).toMatch(/^••••\d{2,4}$/);
    } else {
      expect(sourceRecord.serial_masked).toBeNull();
    }
    expect(JSON.stringify(person)).not.toMatch(
      /"serial_number"|"serial_number_raw"|"serial_number_normalized"/,
    );
  }
});

test("Batch 533 publishes three confirmed Army-entry occupations without employers", () => {
  const expected = [
    ["cdda339e-ab68-596d-96cd-7a0b8ce05e6d", "Managers and officials, n.e.c.", "1943-05-26"],
    ["2b3786dd-e97b-5cbc-830d-40ee51ad3952", "Stenographers and typists", "1942-08-22"],
    ["44e80b12-0d77-5556-83fa-8623dbc8932e", "Farm hands, general farms", "1943-03-11"],
  ] as const;
  for (const [id, occupation, endDate] of expected) {
    const person = profile(id);
    expect(person).toMatchObject({
      identity_status: "confirmed",
      personnel_category: "enlisted_army_personnel",
      commissioned_officer: false,
      research_status: "occupation_only_found",
      research_attempt_count: 3,
    });
    expect(person.immediate_pre_oss_affiliations).toEqual([]);
    expect(person.last_civilian_pre_service).toEqual([]);
    expect(person.other_pre_oss_affiliations).toHaveLength(1);
    expect(person.other_pre_oss_affiliations[0]).toMatchObject({
      canonical_organization: null,
      occupation,
      end_date: endDate,
      relationship_type: "unknown",
      temporal_basis: "strongly_date_bounded",
      identity_confidence: "confirmed",
      claim_confidence: "medium",
      publication_status: "publish_qualified",
    });
    expect(person.claims).toHaveLength(2);
  }
});

test("Batch 533 documents John T Davidson Jr. suffix normalization explicitly", () => {
  const john = profile("2b3786dd-e97b-5cbc-830d-40ee51ad3952");
  expect(john.identity_evidence).toContain("conventional suffix order");
  expect(john.claims.find((claim: { claim_type: string }) => claim.claim_type === "identity"))
    .toMatchObject({
      evidence_excerpt: "DAVIDSON JOHN T JR",
      claim_confidence: "confirmed",
      publication_status: "published",
    });
});

test("Batch 533 leaves seven identities unresolved without publishing candidates", () => {
  for (const id of [
    "734db315-13e2-513a-a730-fa0f45080ddc",
    "fc3ff118-01f7-56ca-83c8-30a0bca61810",
    "ed9a0f14-c3b5-5b7e-a72a-58f2aad9afac",
    "4a1c57e1-7052-5f8c-92b1-428fc2a1ccae",
    "49696b15-fe98-5137-a67f-fd4d6fd7bfc7",
    "c0e63e3a-b4a1-516f-85f1-ef82211524f7",
    "991d1a51-9960-52bb-ba4b-a0ff4b44b7a6",
  ]) {
    const person = profile(id);
    expect(person).toMatchObject({
      identity_status: "unresolved",
      research_status: "no_reliable_result_after_protocol",
      research_attempt_count: 3,
    });
    expect(person.archival_file).toMatchObject({ review_priority: "critical" });
    expect(person.immediate_pre_oss_affiliations).toEqual([]);
    expect(person.last_civilian_pre_service).toEqual([]);
    expect(person.other_pre_oss_affiliations).toEqual([]);
    expect(person.claims).toEqual([]);
    expect(person.next_action).toContain("No reliable pre-OSS employer has yet been identified");
  }
});

test("Batch 533 preserves indexed rank classifications without over-resolving identity", () => {
  expect(profile("49696b15-fe98-5137-a67f-fd4d6fd7bfc7")).toMatchObject({
    personnel_category: "enlisted_army_personnel",
    commissioned_officer: false,
  });
  expect(profile("991d1a51-9960-52bb-ba4b-a0ff4b44b7a6")).toMatchObject({
    personnel_category: "foreign_or_allied_military_personnel",
    commissioned_officer: null,
    allied_or_foreign_personnel: true,
  });
});

test("Batch 533 advances attempted and archival coverage with reproducible totals", () => {
  expect(stats).toMatchObject({
    source_rows: 23978,
    person_entities: 23940,
    research_attempted_people: 5098,
    research_attempt_percent: 21.2949,
    verified_affiliation_people: 569,
    verified_affiliation_percent: 2.3768,
    verified_employer_people: 253,
    verified_employer_percent: 1.0568,
    archival_review_assessed_people: 5053,
    archival_review_percent: 21.1069,
    published_claims: 4019,
    public_sources: 3424,
  });
  expect(stats.research_status_counts).toMatchObject({
    not_started: 18842,
    conflicting_sources: 97,
    no_reliable_result_after_protocol: 114,
    occupation_only_found: 939,
    documented_prewar_employer_found: 101,
    requires_archival_review: 3111,
  });
});

test("Batch 533 evidence is complete, citation-linked, and private-value free", () => {
  const bundle = JSON.parse(evidence);
  expect(bundle).toMatchObject({ bundle_version: "1.0" });
  expect(bundle.sources).toHaveLength(3);
  expect(bundle.organizations).toHaveLength(0);
  expect(bundle.affiliations).toHaveLength(3);
  expect(bundle.claims).toHaveLength(6);
  expect(bundle.claims.reduce(
    (sum: number, claim: { sources: unknown[] }) => sum + claim.sources.length,
    0,
  )).toBe(12);
  expect(bundle.person_updates).toHaveLength(10);
  expect(bundle.research_attempts).toHaveLength(10);
  expect(bundle.claims.filter(
    (claim: { claim_type: string }) => claim.claim_type === "occupation",
  )).toHaveLength(3);
  expect(bundle.claims.every(
    (claim: { publication_status: string }) => ["published", "publish_qualified"].includes(claim.publication_status),
  )).toBe(true);
  expect(evidence).not.toMatch(/serial_number|service_number/);
});

test.describe("Batch 533 direct profile routes", () => {
  for (const [id, name] of cohort) {
    test(`${name} ${id.slice(0, 8)} renders from a direct route`, async ({ page }) => {
      await page.goto(`./people/${id}/`);
      await expect(page.locator("h1")).toContainText(name);
      await expect(page.locator("body")).toContainText("Box169");
      await expect(page.locator("body")).toContainText("Archival-review priority");
    });
  }
});
