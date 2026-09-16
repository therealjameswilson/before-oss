import { expect, test } from "@playwright/test";
import fs from "node:fs";

const people = JSON.parse(
  fs.readFileSync(
    new URL("../src/data/generated/people.json", import.meta.url),
    "utf8",
  ),
);
const stats = JSON.parse(
  fs.readFileSync(
    new URL("../src/data/generated/stats.json", import.meta.url),
    "utf8",
  ),
);
const evidence = fs.readFileSync(
  new URL(
    "../../research/evidence-page-one-hundred-and-thirteen-bernard-s-denedde-through-reid-m-denis-pathways_batch-564_2026-09-16.json",
    import.meta.url,
  ),
  "utf8",
);
const profile = (id: string) =>
  people.find((person: { person_id: string }) => person.person_id === id);

const cohort = [
  [
    "574e972b-2af3-535b-9950-a3e20f059c5f",
    "Bernard S DeNedde",
    "6c4899c8-e25e-5934-aea7-5fbabf87069d",
    "180",
    "S/Lt",
    "French",
    false,
  ],
  [
    "8a7d58f2-6ebc-5e2a-9236-c090308563de",
    "Lawrence E DeNeufville",
    "210ca0a8-2c0e-5095-ae6c-7974995b80ae",
    "181",
    null,
    null,
    false,
  ],
  [
    "51343d7e-365d-5bc5-bef3-73e4090a6f81",
    "Lawrence E DeNeufville",
    "9c8b586b-8243-5d12-81f7-c1a081d24f24",
    "180",
    null,
    null,
    false,
  ],
  [
    "0c392fa9-0677-5f13-a949-15c674b36cc4",
    "Joseph P Dengel",
    "8be7e7ed-2cb8-5ad6-b00d-852e3ae16283",
    "180",
    null,
    null,
    true,
  ],
  [
    "47ef7d98-7e11-53ad-ad88-a5825959fad8",
    "Herbert F Dengler",
    "351f56fe-5a86-5aed-9af7-4b6b24f2fb93",
    "180",
    null,
    null,
    false,
  ],
  [
    "7b5e1b49-58e0-5ed7-a292-2f0c6683e8ef",
    "Archie L Denham",
    "a6c13c7c-665c-555b-b0af-81933057fac9",
    "180",
    "1st Lt",
    null,
    true,
  ],
  [
    "71be83d7-a456-5f31-bed9-960ab1504f54",
    "William D Denholm Jr.",
    "d03df3a9-0903-5390-b727-18f166cceb4b",
    "180",
    null,
    null,
    true,
  ],
  [
    "3c792d40-7811-5504-af9c-339bba16d808",
    "John Denicola",
    "6480e389-0a3c-5544-bcb4-e70ef3a6e0dc",
    "180",
    null,
    null,
    true,
  ],
  [
    "419c5b71-0d56-5ff7-bb40-265131df99a5",
    "Anthony D DeNino",
    "cf180e11-3842-52f0-ace9-dc517d9c6a64",
    "180",
    null,
    null,
    true,
  ],
  [
    "54754dfa-a265-52ee-ade3-782df0f5acd7",
    "Reid M Denis",
    "71fb2378-b0cd-5b5c-ab1f-0ccd09840991",
    "180",
    null,
    "also AS",
    true,
  ],
] as const;

test("Batch 564 preserves page 113 rows 24-33", () => {
  for (const [
    id,
    name,
    sourceRecordId,
    box,
    rank,
    note,
    hasPrivateIdentifier,
  ] of cohort) {
    const person = profile(id);
    expect(person.display_name).toBe(name);
    expect(person.research_attempt_count).toBe(5);
    const sourceRecord = person.source_records.find(
      (record: { source_record_id: string }) =>
        record.source_record_id === sourceRecordId,
    );
    expect(sourceRecord).toMatchObject({
      archive_location: "230/86/29/07",
      box,
      pdf_page: 113,
      rank_as_indexed: rank,
      notes_as_indexed: note,
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

test("Batch 564 publishes only qualified Army occupations for Dengel and DeNino", () => {
  const joseph = profile("0c392fa9-0677-5f13-a949-15c674b36cc4");
  expect(joseph).toMatchObject({
    identity_status: "confirmed",
    research_status: "occupation_only_found",
    personnel_category: "enlisted_army_personnel",
    commissioned_officer: false,
  });
  expect(joseph.immediate_pre_oss_affiliations).toEqual([]);
  expect(joseph.last_civilian_pre_service).toEqual([]);
  expect(joseph.other_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      role_title: "Skilled occupation in manufacture of leather",
      relationship_type: "unknown",
      temporal_basis: "strongly_date_bounded",
      identity_confidence: "confirmed",
      claim_confidence: "medium",
    }),
  ]);

  const anthony = profile("419c5b71-0d56-5ff7-bb40-265131df99a5");
  expect(anthony).toMatchObject({
    identity_status: "confirmed",
    research_status: "occupation_only_found",
    personnel_category: "enlisted_army_personnel",
    commissioned_officer: false,
  });
  expect(anthony.immediate_pre_oss_affiliations).toEqual([]);
  expect(anthony.last_civilian_pre_service).toEqual([]);
  expect(anthony.other_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      role_title: "General office clerk",
      relationship_type: "unknown",
      temporal_basis: "strongly_date_bounded",
      identity_confidence: "confirmed",
      claim_confidence: "medium",
    }),
  ]);
});

test("Batch 564 qualifies Bernard de Nedde without inventing an affiliation", () => {
  const bernard = profile("574e972b-2af3-535b-9950-a3e20f059c5f");
  expect(bernard).toMatchObject({
    identity_status: "high_confidence",
    research_status: "requires_archival_review",
    personnel_category: "foreign_or_allied_military_personnel",
    commissioned_officer: true,
    allied_or_foreign_personnel: true,
  });
  expect(bernard.immediate_pre_oss_affiliations).toEqual([]);
  expect(bernard.last_civilian_pre_service).toEqual([]);
  expect(bernard.other_pre_oss_affiliations).toEqual([]);
  expect(JSON.stringify(bernard)).toContain("Sabouret Garat de Nedde");
  expect(JSON.stringify(bernard)).toContain("GR 28 P 4 174 / 166");
});

test("Batch 564 keeps both DeNeufville source rows separate and visible", () => {
  const box181 = profile("8a7d58f2-6ebc-5e2a-9236-c090308563de");
  const box180 = profile("51343d7e-365d-5bc5-bef3-73e4090a6f81");
  for (const person of [box181, box180]) {
    expect(person).toMatchObject({
      identity_status: "ambiguous",
      research_status: "needs_identity_review",
      archival_file: { review_priority: "critical" },
    });
    expect(person.immediate_pre_oss_affiliations).toEqual([]);
    expect(person.last_civilian_pre_service).toEqual([]);
    expect(person.other_pre_oss_affiliations).toEqual([]);
    expect(JSON.stringify(person)).toContain("foreign correspondent");
  }
  expect(box181.possible_duplicate_group).toBeTruthy();
  expect(box181.possible_duplicate_group).toBe(
    box180.possible_duplicate_group,
  );
});

test("Batch 564 publishes the Denholm conflict and withholds unsupported transfer", () => {
  const william = profile("71be83d7-a456-5f31-bed9-960ab1504f54");
  expect(william).toMatchObject({
    identity_status: "conflicting",
    research_status: "conflicting_sources",
    archival_file: { review_priority: "critical" },
  });
  expect(william.immediate_pre_oss_affiliations).toEqual([]);
  expect(william.last_civilian_pre_service).toEqual([]);
  expect(william.other_pre_oss_affiliations).toEqual([]);
  expect(JSON.stringify(william)).toContain(
    "Army Air Corps OSS veteran",
  );
  expect(JSON.stringify(william)).toContain("incompatible Army name");
  expect(JSON.stringify(william)).not.toContain(
    "Kansas Farm Bureau Mutual Insurance Company",
  );
});

test("Batch 564 keeps postwar and name-only Army evidence out of occupations", () => {
  const john = profile("3c792d40-7811-5504-af9c-339bba16d808");
  expect(john).toMatchObject({
    identity_status: "confirmed",
    research_status: "requires_archival_review",
  });
  expect(john.name_variants).toContain("John De Nicola");
  expect(john.immediate_pre_oss_affiliations).toEqual([]);
  expect(john.last_civilian_pre_service).toEqual([]);
  expect(john.other_pre_oss_affiliations).toEqual([]);
  expect(JSON.stringify(john)).toContain("26 August 1946");

  const reid = profile("54754dfa-a265-52ee-ade3-782df0f5acd7");
  expect(reid).toMatchObject({
    identity_status: "ambiguous",
    research_status: "needs_identity_review",
  });
  expect(reid.immediate_pre_oss_affiliations).toEqual([]);
  expect(reid.last_civilian_pre_service).toEqual([]);
  expect(reid.other_pre_oss_affiliations).toEqual([]);
  expect(JSON.stringify(reid)).not.toContain("occupation code 039");
});

test("Batch 564 leaves Herbert Dengler and Archie Denham unresolved", () => {
  for (const id of [
    "47ef7d98-7e11-53ad-ad88-a5825959fad8",
    "7b5e1b49-58e0-5ed7-a292-2f0c6683e8ef",
  ]) {
    const person = profile(id);
    expect(person.identity_status).toBe("unresolved");
    expect(person.research_status).toBe("requires_archival_review");
    expect(person.immediate_pre_oss_affiliations).toEqual([]);
    expect(person.last_civilian_pre_service).toEqual([]);
    expect(person.other_pre_oss_affiliations).toEqual([]);
    expect(JSON.stringify(person)).toContain(
      "No reliable pre-OSS employer has yet been identified",
    );
  }
});

test("Batch 564 advances research and archival coverage without employer inflation", () => {
  expect(stats).toMatchObject({
    source_rows: 23978,
    person_entities: 23940,
    possible_duplicate_groups: 254,
    research_attempted_people: 5406,
    research_attempt_percent: 22.5815,
    verified_affiliation_people: 585,
    verified_affiliation_percent: 2.4436,
    verified_employer_people: 259,
    verified_employer_percent: 1.0819,
    archival_review_assessed_people: 5361,
    archival_review_percent: 22.3935,
    public_sources: 3603,
    published_claims: 4328,
  });
  expect(stats.research_status_counts).toMatchObject({
    conflicting_sources: 114,
    needs_identity_review: 316,
    not_started: 18534,
    occupation_only_found: 1001,
    requires_archival_review: 3197,
    verified_employer_found: 242,
  });
  expect(stats.identity_status_counts).toEqual({
    ambiguous: 269,
    confirmed: 1116,
    conflicting: 116,
    high_confidence: 733,
    probable: 175,
    unresolved: 21531,
  });
});

test("Batch 564 evidence exposes neither private identifiers nor credentials", () => {
  expect(evidence).not.toMatch(/serial_number(_raw|_normalized)?/);
  expect(evidence).not.toContain('"serial_number"');
  expect(evidence).not.toContain("NARA_API_KEY");
  expect(evidence).not.toContain("x-api-key");
});
