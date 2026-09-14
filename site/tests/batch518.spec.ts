import { expect, test } from "@playwright/test";
import fs from "node:fs";

const people = JSON.parse(
  fs.readFileSync(new URL("../src/data/generated/people.json", import.meta.url), "utf8"),
);
const stats = JSON.parse(
  fs.readFileSync(new URL("../src/data/generated/stats.json", import.meta.url), "utf8"),
);
const profile = (id: string) =>
  people.find((person: { person_id: string }) => person.person_id === id);

const cohort = [
  ["e6d294a3-8abe-50ca-be75-c113317d4ef0", "Dorothy J Dahl", "89736d3c-e897-58c4-be1b-9bcaf3a8ea65", "163", false],
  ["11d04934-ef5c-57f3-8a24-3259956301f5", "George N Dahl", "abbd6e50-546b-5c80-a3a8-e1caa38d1fb8", "163", true],
  ["8601b32f-db64-5538-b76e-2fe778a7af9e", "Nils Dahl", "da8a8448-6768-51e9-aab5-826a35f4172f", "163", true],
  ["d4943ed2-7205-5eb4-afed-cef6e5a33e45", "Bruce T Dahlberg", "8cb8e9f3-bc97-54d3-a5e2-363d66911261", "163", true],
  ["7d186de7-10a5-5630-b14f-86d1b63f1f2a", "Alma A Dahlgren", "689d3c68-2b25-5f40-bf68-4e58c72d6b64", "163", false],
  ["86dcac95-6a09-5cf8-8bea-e6454874e855", "Robert N Dahlgren", "e1284479-073d-5811-8d68-b9b16dc6a4e3", "163", false],
  ["a3e32aa6-edaa-5084-90b3-c958756d0d73", "Larry A Dahlquist", "a3e1e62c-588b-5830-9d24-6870e41e2dd5", "163", true],
  ["e7238eb3-c621-5619-9f90-cf1f0b2d80b5", "Bingham Dai", "d3737768-246b-5b5b-bb06-b5123032da9f", "163", false],
  ["3fbe064b-08bb-54c1-a97f-cc865c222083", "Marion H Daigle", "3f4e43af-f041-50fa-aaa4-96f9837d9953", "164", false],
  ["1a8e0ac8-6643-5033-86ba-a46c568b8d88", "Richard J Daigle Jr.", "9b08cad7-6253-5ef3-882a-4bf9ab092fa3", "164", true],
] as const;

test("Batch 518 preserves page 103 rows 22-31 and masks five private fields", () => {
  for (const [id, name, sourceRecordId, box, hasPrivateIdentifier] of cohort) {
    const person = profile(id);
    expect(person).toMatchObject({ display_name: name });
    const sourceRecord = person.source_records.find(
      (record: { source_record_id: string }) => record.source_record_id === sourceRecordId,
    );
    expect(sourceRecord).toMatchObject({
      box,
      archive_location: "230/86/29/05",
      pdf_page: 103,
      rank_as_indexed: null,
    });
    if (hasPrivateIdentifier) {
      expect(sourceRecord.serial_masked).toMatch(/^••••\d{4}$/);
    } else {
      expect(sourceRecord.serial_masked).toBeNull();
    }
    expect(JSON.stringify(person)).not.toMatch(
      /"serial_number"|"serial_number_raw"|"serial_number_normalized"/,
    );
  }
});

test("Batch 518 publishes Bingham Dai's Duke predecessor employment separately from earlier Peking work", () => {
  const bingham = profile("e7238eb3-c621-5619-9f90-cf1f0b2d80b5");
  expect(bingham).toMatchObject({
    identity_status: "confirmed",
    personnel_category: "civilian_professional_or_administrative_grade",
    commissioned_officer: false,
    research_status: "verified_employer_found",
  });
  expect(bingham.immediate_pre_oss_affiliations).toHaveLength(1);
  expect(bingham.immediate_pre_oss_affiliations[0]).toMatchObject({
    canonical_organization: "Duke University",
    relationship_type: "employment",
    temporal_basis: "explicit_immediate",
    claim_confidence: "confirmed",
    publication_status: "published",
  });
  expect(bingham.last_civilian_pre_service).toHaveLength(1);
  expect(bingham.last_civilian_pre_service[0].canonical_organization).toBe("Duke University");
  expect(bingham.other_pre_oss_affiliations).toHaveLength(1);
  expect(bingham.other_pre_oss_affiliations[0]).toMatchObject({
    canonical_organization: "Peking Union Medical College",
    relationship_type: "employment",
    temporal_basis: "documented_prewar",
    claim_confidence: "high",
    publication_status: "published",
  });
});

test("Batch 518 publishes two identifier-linked pre-service statuses without inventing employers", () => {
  const cases = [
    ["d4943ed2-7205-5eb4-afed-cef6e5a33e45", "student", "Students"],
    ["a3e32aa6-edaa-5084-90b3-c958756d0d73", "unknown", "Construction occupations, n.e.c."],
  ] as const;

  for (const [id, relationshipType, occupation] of cases) {
    const person = profile(id);
    expect(person).toMatchObject({
      identity_status: "confirmed",
      personnel_category: "enlisted_army_personnel",
      commissioned_officer: false,
      research_status: "occupation_only_found",
      immediate_pre_oss_affiliations: [],
      last_civilian_pre_service: [],
    });
    expect(person.other_pre_oss_affiliations).toHaveLength(1);
    expect(person.other_pre_oss_affiliations[0]).toMatchObject({
      organization_id: null,
      occupation,
      relationship_type: relationshipType,
      temporal_basis: "strongly_date_bounded",
      claim_confidence: "medium",
      publication_status: "publish_qualified",
    });
  }
});

test("Batch 518 confirms Richard Daigle's identity but withholds a post-OSS occupation", () => {
  const richard = profile("1a8e0ac8-6643-5033-86ba-a46c568b8d88");
  expect(richard).toMatchObject({
    identity_status: "confirmed",
    personnel_category: "enlisted_army_personnel",
    commissioned_officer: false,
    research_status: "requires_archival_review",
    immediate_pre_oss_affiliations: [],
    last_civilian_pre_service: [],
    other_pre_oss_affiliations: [],
  });
  expect(richard.identity_evidence).toContain("Greek Group VI");
  expect(richard.claims).toHaveLength(1);
  expect(richard.claims[0]).toMatchObject({
    claim_type: "identity",
    claim_confidence: "confirmed",
    publication_status: "published",
  });
  expect(JSON.stringify(richard)).not.toContain("occupation value 480");
});

test("Batch 518 leaves six unsupported name cases unresolved and directs them to the indexed box", () => {
  const cases = [
    ["e6d294a3-8abe-50ca-be75-c113317d4ef0", "163"],
    ["11d04934-ef5c-57f3-8a24-3259956301f5", "163"],
    ["8601b32f-db64-5538-b76e-2fe778a7af9e", "163"],
    ["7d186de7-10a5-5630-b14f-86d1b63f1f2a", "163"],
    ["86dcac95-6a09-5cf8-8bea-e6454874e855", "163"],
    ["3fbe064b-08bb-54c1-a97f-cc865c222083", "164"],
  ] as const;
  for (const [id, box] of cases) {
    expect(profile(id)).toMatchObject({
      identity_status: "unresolved",
      personnel_category: "unknown_or_indeterminate",
      commissioned_officer: null,
      research_status: "requires_archival_review",
      immediate_pre_oss_affiliations: [],
      last_civilian_pre_service: [],
      other_pre_oss_affiliations: [],
      claims: [],
      archival_file: { box, indexed: true, digitized: false, reviewed: false },
    });
  }
});

test("Batch 518 advances exact aggregate coverage without changing the index denominator", () => {
  expect(stats).toMatchObject({
    source_rows: 23978,
    person_entities: 23940,
    research_attempted_people: 4947,
    research_attempt_percent: 20.6642,
    verified_affiliation_people: 565,
    verified_affiliation_percent: 2.3601,
    verified_employer_people: 252,
    verified_employer_percent: 1.0526,
    archival_review_assessed_people: 4902,
    archival_review_percent: 20.4762,
    published_claims: 3907,
    public_sources: 3349,
  });
  expect(stats.research_status_counts).toMatchObject({
    completed: 142,
    not_started: 18993,
    occupation_only_found: 898,
    requires_archival_review: 3056,
    verified_employer_found: 237,
  });
});

test.describe("Batch 518 direct profile routes", () => {
  for (const [id, name, , box] of cohort) {
    test(`${name} renders from a direct route`, async ({ page }) => {
      await page.goto(`./people/${id}/`);
      await expect(page.locator("h1")).toContainText(name);
      await expect(page.locator("body")).toContainText(`Box ${box}`);
    });
  }
});
