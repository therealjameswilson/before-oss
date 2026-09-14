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
  ["1653a811-dc15-502e-bcbb-935f214ea7a3", "William C Dabney", "a447cc1b-b0fb-5b16-8c95-86f99dc3e249", null, false],
  ["dfa67e64-7f53-5029-a952-1bb5fde9de8d", "Marcelino H DaCosta", "e0fcad4f-b8f1-5468-9e27-66e83ab4e0b8", null, false],
  ["ba998c3d-6ef9-518e-a828-f9e9fb6dd846", "Theodore A Dada", "8bce0afd-e8fe-520d-8ef3-98959b08ab34", null, true],
  ["adc1d354-7127-5c70-aaa1-fc7e13ec5c15", "Emilio Q Daddario", "6ac8e2d7-cde5-5658-9b6a-a0d2927e896f", "Capt", true],
  ["c90ccd7d-3d5f-5aa3-bef4-789221eb00d5", "Joseph Dagan", "123cfa37-97b5-5122-a277-1290472a6b0b", null, true],
  ["74306f72-8e5d-5718-8aa3-c78d823c7104", "Malcolm D Daggett", "dbad9f2f-9988-5c5c-ad58-e2960ab787ea", null, false],
  ["6c3a7793-5068-5367-bef1-ed38f12b7d0f", "Stuart Daggett", "aa5a83ed-3c94-5d86-943f-c25cdb0aeddd", null, false],
  ["6f57027e-810d-5dc4-937b-0c2cfece1351", "Arthur T D'Agostino", "c545c96e-4e0f-54f0-8252-54964aef4a4d", null, true],
  ["96d3a958-c2c1-5472-898a-fac14740d477", "Ralph C Dahdah", "315cc811-723c-5882-9c1a-78367f206dda", null, true],
  ["5efaa079-0ce5-5114-91eb-dab527cef37c", "Clarence Dahl", "85527473-528f-58fe-9f92-cc70f7f6a048", null, false],
] as const;

test("Batch 517 preserves page 103 rows 12-21 and masks five private fields", () => {
  for (const [id, name, sourceRecordId, rank, hasPrivateIdentifier] of cohort) {
    const person = profile(id);
    expect(person).toMatchObject({ display_name: name });
    const sourceRecord = person.source_records.find(
      (record: { source_record_id: string }) => record.source_record_id === sourceRecordId,
    );
    expect(sourceRecord).toMatchObject({
      box: "163",
      archive_location: "230/86/29/05",
      pdf_page: 103,
      rank_as_indexed: rank,
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

test("Batch 517 publishes William Dabney's qualified identity and education without inventing an employer", () => {
  const william = profile("1653a811-dc15-502e-bcbb-935f214ea7a3");
  expect(william).toMatchObject({
    identity_status: "high_confidence",
    personnel_category: "commissioned_army_officer",
    commissioned_officer: true,
    research_status: "completed",
    immediate_pre_oss_affiliations: [],
    last_civilian_pre_service: [],
  });
  expect(william.other_pre_oss_affiliations).toHaveLength(1);
  expect(william.other_pre_oss_affiliations[0]).toMatchObject({
    canonical_organization: "Colorado College",
    relationship_type: "student",
    temporal_basis: "documented_prewar",
    identity_confidence: "high_confidence",
    claim_confidence: "high",
    publication_status: "published",
  });
  expect(william.claims.some((claim: { match_notes?: string }) =>
    claim.match_notes?.includes("Two exact-name Army rows remain unlinked"),
  )).toBe(true);
});

test("Batch 517 separates Emilio Daddario's last civilian practice from the disputed Army pathway", () => {
  const emilio = profile("adc1d354-7127-5c70-aaa1-fc7e13ec5c15");
  expect(emilio).toMatchObject({
    identity_status: "confirmed",
    personnel_category: "commissioned_army_officer",
    commissioned_officer: true,
    research_status: "verified_employer_found",
  });
  expect(emilio.last_civilian_pre_service).toHaveLength(1);
  expect(emilio.last_civilian_pre_service[0]).toMatchObject({
    canonical_organization: "Self-employed legal practice",
    role_title: "Attorney in individual private practice",
    relationship_type: "self_employment",
    temporal_basis: "strongly_date_bounded",
    claim_confidence: "confirmed",
    publication_status: "published",
  });
  expect(emilio.immediate_pre_oss_affiliations).toHaveLength(1);
  expect(emilio.immediate_pre_oss_affiliations[0]).toMatchObject({
    canonical_organization: "United States Army",
    relationship_type: "military_assignment",
    claim_confidence: "conflicting",
    publication_status: "conflicting",
  });
  expect(emilio.claims).toEqual(expect.arrayContaining([
    expect.objectContaining({
      claim_type: "immediate_pre_oss_affiliation",
      claim_confidence: "conflicting",
      publication_status: "conflicting",
    }),
  ]));
});

test("Batch 517 publishes three bounded occupations but no employer", () => {
  const cases = [
    ["c90ccd7d-3d5f-5aa3-bef4-789221eb00d5", "salesman to consumers"],
    ["6f57027e-810d-5dc4-937b-0c2cfece1351", "cook, except private family"],
    ["96d3a958-c2c1-5472-898a-fac14740d477", "stenographer or typist"],
  ] as const;

  for (const [id, occupation] of cases) {
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
      relationship_type: "unknown",
      temporal_basis: "strongly_date_bounded",
      claim_confidence: "medium",
      publication_status: "publish_qualified",
    });
  }
});

test("Batch 517 leaves five unsupported name cases unresolved and directs them to Box 163", () => {
  for (const id of [
    "dfa67e64-7f53-5029-a952-1bb5fde9de8d",
    "ba998c3d-6ef9-518e-a828-f9e9fb6dd846",
    "74306f72-8e5d-5718-8aa3-c78d823c7104",
    "6c3a7793-5068-5367-bef1-ed38f12b7d0f",
    "5efaa079-0ce5-5114-91eb-dab527cef37c",
  ]) {
    expect(profile(id)).toMatchObject({
      identity_status: "unresolved",
      personnel_category: "unknown_or_indeterminate",
      commissioned_officer: null,
      research_status: "requires_archival_review",
      immediate_pre_oss_affiliations: [],
      last_civilian_pre_service: [],
      other_pre_oss_affiliations: [],
      claims: [],
      archival_file: { box: "163", indexed: true, digitized: false, reviewed: false },
    });
  }
  expect(profile("6c3a7793-5068-5367-bef1-ed38f12b7d0f").identity_evidence).toContain(
    "University of California economist",
  );
  expect(profile("5efaa079-0ce5-5114-91eb-dab527cef37c").identity_evidence).toContain(
    "rejected namesakes",
  );
});

test("Batch 517 advances exact aggregate coverage without changing the index denominator", () => {
  expect(stats).toMatchObject({
    source_rows: 23978,
    person_entities: 23940,
    research_attempted_people: 4937,
    research_attempt_percent: 20.6224,
    verified_affiliation_people: 564,
    verified_affiliation_percent: 2.3559,
    verified_employer_people: 251,
    verified_employer_percent: 1.0485,
    archival_review_assessed_people: 4892,
    archival_review_percent: 20.4344,
    published_claims: 3898,
    public_sources: 3341,
  });
  expect(stats.research_status_counts).toMatchObject({
    completed: 142,
    not_started: 19003,
    occupation_only_found: 896,
    requires_archival_review: 3049,
    verified_employer_found: 236,
  });
});

test.describe("Batch 517 direct profile routes", () => {
  for (const [id, name] of cohort) {
    test(`${name} renders from a direct route`, async ({ page }) => {
      await page.goto(`./people/${id}/`);
      await expect(page.locator("h1")).toContainText(name);
      await expect(page.locator("body")).toContainText("Box 163");
    });
  }
});
