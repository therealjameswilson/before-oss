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
    "../../research/evidence-page-one-hundred-and-twelve-william-h-demant-through-joseph-r-demartino-pathways_batch-560_2026-09-16.json",
    import.meta.url,
  ),
  "utf8",
);
const profile = (id: string) =>
  people.find((person: { person_id: string }) => person.person_id === id);

const cohort = [
  ["64ab5daa-fbd6-553b-a428-6c2f749217ee", "William H Demant", "eeac3d0f-fde4-5e8b-8ce8-8798f3c01c55", "2nd Lt", true],
  ["1e2f25ce-4da2-5ddf-bbc6-eba595374d03", "Michael A Demarco", "db3418e3-4e55-5988-be56-b69087482844", "1st Lt", true],
  ["c6a14637-d28f-528b-b0ff-6ac5dfecf684", "Rene Demarcq", "52ceb2d3-9898-5008-986f-cdaf638721ce", null, false],
  ["3e0ccbb4-6d51-532c-9a20-5dc8978740ca", "Donald E Demaree", "d900f87d-b316-5c1c-98d2-29b4b43c7dd3", null, true],
  ["b7c83df3-9156-55ee-b40f-e0fbd57aed28", "Rosemary R Demarest", "ca399817-df28-51ed-a677-54045bdc07af", null, false],
  ["d0042f95-e917-5a02-9973-6ed3330f0f68", "Henry A DeMarey", "d5ee658c-c790-51b2-b07d-f6c1fbb0d53a", null, true],
  ["84a45cbf-2e26-5e14-bc8a-74ace7c791d1", "Henry A DeMarey", "916d36f6-7bdb-5c6c-a558-34cb5c325241", null, false],
  ["2af96ab8-5891-50c9-8a71-acb6c9f08564", "Lawrence J DeMaria", "67208ba0-0853-58f5-a3eb-acd442cdf2ff", "S/Sgt", true],
  ["1d2197af-4d50-5716-b67d-1b35eaf1b8b0", "Alfred J DeMartino", "c1eb0f47-06e1-5d8b-b6b7-0be0c3826a68", null, true],
  ["616316a4-dc07-5c53-9e1d-824f5f07a0dc", "Joseph R Demartino", "80f19047-7394-5af7-9b74-75caaf9654eb", null, true],
] as const;

test("Batch 560 preserves page 112 rows 30-39 and masks seven private fields", () => {
  for (const [id, name, sourceRecordId, rank, hasPrivateIdentifier] of cohort) {
    const person = profile(id);
    expect(person.display_name).toBe(name);
    expect(person.research_attempt_count).toBe(5);
    const sourceRecord = person.source_records.find(
      (record: { source_record_id: string }) => record.source_record_id === sourceRecordId,
    );
    expect(sourceRecord).toMatchObject({
      archive_location: "230/86/29/07",
      box: "179",
      pdf_page: 112,
      rank_as_indexed: rank,
      notes_as_indexed: null,
    });
    if (hasPrivateIdentifier) {
      expect(sourceRecord.serial_masked).toMatch(/^•+\d{4}$/);
    } else {
      expect(sourceRecord.serial_masked).toBeNull();
    }
    expect(JSON.stringify(person)).not.toMatch(
      /"serial_number"|"serial_number_raw"|"serial_number_normalized"/,
    );
  }
});

test("Batch 560 retains printed commissioned classifications without assigning namesakes", () => {
  for (const id of [
    "64ab5daa-fbd6-553b-a428-6c2f749217ee",
    "1e2f25ce-4da2-5ddf-bbc6-eba595374d03",
  ]) {
    const person = profile(id);
    expect(person).toMatchObject({
      identity_status: "unresolved",
      research_status: "requires_archival_review",
      personnel_category: "commissioned_army_officer",
      commissioned_officer: true,
      manual_review_required: true,
    });
    expect(person.immediate_pre_oss_affiliations).toEqual([]);
    expect(person.last_civilian_pre_service).toEqual([]);
    expect(person.other_pre_oss_affiliations).toEqual([]);
  }
});

test("Batch 560 publishes Rene Demarcq's immediate student status with qualified identity", () => {
  const rene = profile("c6a14637-d28f-528b-b0ff-6ac5dfecf684");
  expect(rene).toMatchObject({
    identity_status: "high_confidence",
    research_status: "completed",
    personnel_category: "foreign_or_allied_military_personnel",
    commissioned_officer: null,
    allied_or_foreign_personnel: true,
    manual_review_required: false,
  });
  expect(rene.name_variants).toContain("René Demarcq");
  expect(rene.immediate_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      canonical_organization: null,
      occupation: "Student",
      relationship_type: "student",
      temporal_basis: "explicit_immediate",
      identity_confidence: "high_confidence",
      claim_confidence: "high",
    }),
  ]);
  expect(rene.last_civilian_pre_service).toEqual([]);
  expect(rene.other_pre_oss_affiliations).toEqual([]);
  expect(JSON.stringify(rene)).toContain("young student recruited by Ludovic");
  expect(JSON.stringify(rene)).toContain("museedelaresistanceenligne.org");
});

test("Batch 560 keeps the two Henry DeMarey rows separate and prevents evidence leakage", () => {
  const confirmed = profile("d0042f95-e917-5a02-9973-6ed3330f0f68");
  const noIdentifier = profile("84a45cbf-2e26-5e14-bc8a-74ace7c791d1");
  expect(confirmed.person_id).not.toBe(noIdentifier.person_id);
  expect(confirmed.possible_duplicate_group).toBeTruthy();
  expect(noIdentifier.possible_duplicate_group).toBe(confirmed.possible_duplicate_group);
  expect(confirmed).toMatchObject({
    identity_status: "confirmed",
    research_status: "occupation_only_found",
    personnel_category: "enlisted_army_personnel",
    commissioned_officer: false,
    manual_review_required: true,
  });
  expect(noIdentifier).toMatchObject({
    identity_status: "ambiguous",
    research_status: "needs_identity_review",
    personnel_category: "unknown_or_indeterminate",
    commissioned_officer: null,
    manual_review_required: true,
  });
  expect(confirmed.other_pre_oss_affiliations).toEqual([
    expect.objectContaining({ occupation: "Bakery products occupations, production" }),
  ]);
  expect(noIdentifier.immediate_pre_oss_affiliations).toEqual([]);
  expect(noIdentifier.last_civilian_pre_service).toEqual([]);
  expect(noIdentifier.other_pre_oss_affiliations).toEqual([]);
  expect(JSON.stringify(noIdentifier)).toContain("does not establish that merge");
  expect(JSON.stringify(noIdentifier)).not.toContain(
    "Bakery products occupations, production",
  );
});

test("Batch 560 publishes only three identifier-backed Army occupation categories", () => {
  const expectations = [
    ["d0042f95-e917-5a02-9973-6ed3330f0f68", "Bakery products occupations, production", "1940-07-16"],
    ["2af96ab8-5891-50c9-8a71-acb6c9f08564", "Sales clerks", "1941-04-18"],
    ["1d2197af-4d50-5716-b67d-1b35eaf1b8b0", "Mechanics and repairmen, n.e.c.", "1942-05-16"],
  ] as const;
  for (const [id, occupation, endDate] of expectations) {
    const person = profile(id);
    expect(person).toMatchObject({
      identity_status: "confirmed",
      research_status: "occupation_only_found",
      personnel_category: "enlisted_army_personnel",
      commissioned_officer: false,
    });
    expect(person.immediate_pre_oss_affiliations).toEqual([]);
    expect(person.last_civilian_pre_service).toEqual([]);
    expect(person.other_pre_oss_affiliations).toEqual([
      expect.objectContaining({
        canonical_organization: null,
        occupation,
        relationship_type: "unknown",
        end_date: endDate,
        temporal_basis: "strongly_date_bounded",
        identity_confidence: "confirmed",
        claim_confidence: "medium",
      }),
    ]);
  }
});

test("Batch 560 completes the accessible protocol for unresolved profiles", () => {
  for (const id of [
    "3e0ccbb4-6d51-532c-9a20-5dc8978740ca",
    "b7c83df3-9156-55ee-b40f-e0fbd57aed28",
    "616316a4-dc07-5c53-9e1d-824f5f07a0dc",
  ]) {
    const person = profile(id);
    expect(person).toMatchObject({
      identity_status: "unresolved",
      research_status: "requires_archival_review",
      manual_review_required: true,
    });
    expect(person.immediate_pre_oss_affiliations).toEqual([]);
    expect(person.last_civilian_pre_service).toEqual([]);
    expect(person.other_pre_oss_affiliations).toEqual([]);
    expect(JSON.stringify(person)).toContain(
      "No reliable pre-OSS employer has yet been identified",
    );
  }
});

test("Batch 560 advances research, affiliation and archival coverage without adding an employer", () => {
  expect(stats).toMatchObject({
    source_rows: 23978,
    person_entities: 23940,
    possible_duplicate_groups: 251,
    research_attempted_people: 5366,
    research_attempt_percent: 22.4144,
    verified_affiliation_people: 583,
    verified_affiliation_percent: 2.4353,
    verified_employer_people: 258,
    verified_employer_percent: 1.0777,
    archival_review_assessed_people: 5321,
    archival_review_percent: 22.2264,
    public_sources: 3580,
    published_claims: 4266,
  });
  expect(stats.research_status_counts).toMatchObject({
    completed: 147,
    needs_identity_review: 307,
    not_started: 18574,
    occupation_only_found: 994,
    requires_archival_review: 3177,
    verified_employer_found: 241,
  });
  expect(stats.identity_status_counts).toEqual({
    ambiguous: 263,
    confirmed: 1107,
    conflicting: 113,
    high_confidence: 730,
    probable: 172,
    unresolved: 21555,
  });
});

test("Batch 560 evidence package exposes neither private identifiers nor credentials", () => {
  expect(evidence).not.toMatch(/serial_number(_raw|_normalized)?/);
  expect(evidence).not.toContain('"serial_number"');
  expect(evidence).not.toContain("NARA_API_KEY");
  expect(evidence).not.toContain("x-api-key");
});
