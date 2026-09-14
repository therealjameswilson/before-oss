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
  ["fbd61f6c-2597-5d29-b8ae-7c0629344a13", "Rose Daigle", "7f2112a6-0ce9-51cc-82cc-f12d47dea4d3", null, false],
  ["3711608f-c2e2-59a1-8733-7ce4daf72d11", "Alfred P Daignault", "48f34b86-3d1f-560a-a659-d92abb9e7517", null, true],
  ["a5de09e6-8b19-555e-ba4e-316a4c40e580", "George E Dail Jr.", "76a6c283-f727-5430-b9ed-e9720bf7ba52", "2nd Lt", false],
  ["8c34f4dc-c4a1-5b37-99f7-a050cf5736ec", "Lowell R Dailey", "f4cb3491-15d9-51e6-9eb8-ac5c7c511017", null, false],
  ["434aaeff-7489-57f5-9313-de08e317fbc2", "Pat H Dailey", "434818cf-dfdd-514a-8576-3d3094914ce9", null, true],
  ["c92c4d78-2b39-5982-8e05-6a0ba276ac3e", "James Daily", "6495ec55-f4c6-5eac-8652-618be897077a", null, false],
  ["60da51f6-afb3-5eeb-b3ef-9486961a9fae", "Harvey J Dain", "83347755-c89f-54c9-9296-bf5a0ff22074", "Capt", true],
  ["45b86bd5-f46a-56fc-8ce5-665fe407cfb7", "John W Dain", "ed9698b8-b15a-55d4-97a6-835e666954c3", null, false],
  ["ed64b606-9b10-5984-b864-17edb72d97b8", "Charles Daish", "d19d2e7e-d6ff-5697-8332-7f82a674231c", null, false],
  ["e7978ab6-aac5-5e97-9dd7-2bd37f556ccb", "Edward J Dajewski", "3f57d19b-5403-5475-b0fd-646623e1e50c", null, true],
] as const;

test("Batch 519 preserves page 103 rows 32-41 and masks four private fields", () => {
  for (const [id, name, sourceRecordId, rank, hasPrivateIdentifier] of cohort) {
    const person = profile(id);
    expect(person).toMatchObject({ display_name: name });
    const sourceRecord = person.source_records.find(
      (record: { source_record_id: string }) => record.source_record_id === sourceRecordId,
    );
    expect(sourceRecord).toMatchObject({
      box: "164",
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

test("Batch 519 confirms Alfred Daignault with independent OSS staff evidence but invents no employer", () => {
  const alfred = profile("3711608f-c2e2-59a1-8733-7ce4daf72d11");
  expect(alfred).toMatchObject({
    identity_status: "confirmed",
    personnel_category: "enlisted_army_personnel",
    commissioned_officer: false,
    research_status: "occupation_only_found",
    immediate_pre_oss_affiliations: [],
    last_civilian_pre_service: [],
  });
  expect(alfred.identity_evidence).toContain("Assessment Staff");
  expect(alfred.other_pre_oss_affiliations).toHaveLength(1);
  expect(alfred.other_pre_oss_affiliations[0]).toMatchObject({
    organization_id: null,
    occupation: "Occupations in manufacture of automobiles, n.e.c.",
    relationship_type: "unknown",
    temporal_basis: "strongly_date_bounded",
    claim_confidence: "medium",
    publication_status: "publish_qualified",
  });
  expect(alfred.claims).toHaveLength(2);
});

test("Batch 519 confirms Pat Dailey's machinist status without inventing an employer", () => {
  const pat = profile("434aaeff-7489-57f5-9313-de08e317fbc2");
  expect(pat).toMatchObject({
    identity_status: "confirmed",
    personnel_category: "enlisted_army_personnel",
    commissioned_officer: false,
    research_status: "occupation_only_found",
    immediate_pre_oss_affiliations: [],
    last_civilian_pre_service: [],
  });
  expect(pat.other_pre_oss_affiliations).toHaveLength(1);
  expect(pat.other_pre_oss_affiliations[0]).toMatchObject({
    organization_id: null,
    occupation: "Machinists",
    relationship_type: "unknown",
    temporal_basis: "strongly_date_bounded",
    claim_confidence: "medium",
    publication_status: "publish_qualified",
  });
  expect(pat.claims).toHaveLength(2);
});

test("Batch 519 qualifies George Dail's OSS identity and keeps later OSS duty out of pre-OSS fields", () => {
  const george = profile("a5de09e6-8b19-555e-ba4e-316a4c40e580");
  expect(george).toMatchObject({
    identity_status: "high_confidence",
    personnel_category: "commissioned_army_officer",
    commissioned_officer: true,
    research_status: "requires_archival_review",
    immediate_pre_oss_affiliations: [],
    last_civilian_pre_service: [],
    other_pre_oss_affiliations: [],
  });
  expect(george.identity_evidence).toContain("Morale Operations");
  expect(george.claims).toHaveLength(1);
  expect(george.claims[0]).toMatchObject({
    claim_type: "identity",
    claim_confidence: "high",
    publication_status: "published",
  });
});

test("Batch 519 retains Harvey Dain's indexed commissioned classification without assigning the psychiatrist namesake", () => {
  const harvey = profile("60da51f6-afb3-5eeb-b3ef-9486961a9fae");
  expect(harvey).toMatchObject({
    identity_status: "unresolved",
    personnel_category: "commissioned_army_officer",
    commissioned_officer: true,
    research_status: "requires_archival_review",
    immediate_pre_oss_affiliations: [],
    last_civilian_pre_service: [],
    other_pre_oss_affiliations: [],
    claims: [],
  });
  expect(harvey.identity_evidence).toContain("were not assigned");
});

test("Batch 519 leaves six unsupported cases unresolved and directs them to Box 164", () => {
  const ids = [
    "fbd61f6c-2597-5d29-b8ae-7c0629344a13",
    "8c34f4dc-c4a1-5b37-99f7-a050cf5736ec",
    "c92c4d78-2b39-5982-8e05-6a0ba276ac3e",
    "45b86bd5-f46a-56fc-8ce5-665fe407cfb7",
    "ed64b606-9b10-5984-b864-17edb72d97b8",
    "e7978ab6-aac5-5e97-9dd7-2bd37f556ccb",
  ];
  for (const id of ids) {
    expect(profile(id)).toMatchObject({
      identity_status: "unresolved",
      personnel_category: "unknown_or_indeterminate",
      commissioned_officer: null,
      research_status: "requires_archival_review",
      immediate_pre_oss_affiliations: [],
      last_civilian_pre_service: [],
      other_pre_oss_affiliations: [],
      claims: [],
      archival_file: { box: "164", indexed: true, digitized: false, reviewed: false },
    });
  }
});

test("Batch 519 advances exact aggregate coverage without changing the index denominator", () => {
  expect(stats).toMatchObject({
    source_rows: 23978,
    person_entities: 23940,
    research_attempted_people: 4957,
    research_attempt_percent: 20.7059,
    verified_affiliation_people: 565,
    verified_affiliation_percent: 2.3601,
    verified_employer_people: 252,
    verified_employer_percent: 1.0526,
    archival_review_assessed_people: 4912,
    archival_review_percent: 20.518,
    published_claims: 3912,
    public_sources: 3355,
  });
  expect(stats.research_status_counts).toMatchObject({
    completed: 142,
    not_started: 18983,
    occupation_only_found: 900,
    requires_archival_review: 3064,
    verified_employer_found: 237,
  });
});

test.describe("Batch 519 direct profile routes", () => {
  for (const [id, name] of cohort) {
    test(`${name} renders from a direct route`, async ({ page }) => {
      await page.goto(`./people/${id}/`);
      await expect(page.locator("h1")).toContainText(name);
      await expect(page.locator("body")).toContainText("Box 164");
    });
  }
});
