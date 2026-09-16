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
    "../../research/evidence-page-one-hundred-and-fourteen-jeffrey-t-denton-jr-through-alfred-j-depole-pathways_batch-567_2026-09-16.json",
    import.meta.url,
  ),
  "utf8",
);
const profile = (id: string) =>
  people.find((person: { person_id: string }) => person.person_id === id);

const cohort = [
  ["131357dc-d090-56a0-aef6-629d897c9502", "Jeffrey T Denton Jr.", "bf7cecb0-a1fd-58ff-ad64-81ba366d0bbb", null, null, false],
  ["1e92901c-6eb8-5ec8-a243-7961adc813ec", "John D Denton Jr.", "c25078bf-c38f-5de0-bba8-8d170783a75d", null, null, true],
  ["54fe4f71-a7ee-5406-9234-25a283cab43e", "Keith G Denton", "bf681c58-d532-524d-80c8-afdddc99df10", null, null, true],
  ["84055c54-45f7-54c7-a326-db74aa5e88e2", "Otto DePasetti", "8fb03662-7ea8-5df5-9c9c-56c84c526159", null, null, false],
  ["f9e52678-9b71-51f2-b188-38d88462c743", "Harry DePaur", "5fb303ed-bd7e-55ac-8e60-1f90422bb463", null, null, false],
  ["b5a624a2-4177-5faa-b771-20380f275b58", "Claude DePerthius", "552b2335-f4d8-5ad7-aea5-ded68b16f1f9", "S/Lt", "French", false],
  ["c8645131-9d3a-53d7-9d84-41ebfcc13082", "Pierre R Depinay", "ea19090c-272a-5a35-84ac-1ff54b1ae726", "Lt", "French", false],
  ["bb8ca645-9194-5f81-8291-eebb5422d8ea", "Gerard Depiolenc", "a969bc70-5299-5caa-aacd-90caed56a149", null, null, false],
  ["3c25b26f-0104-52cf-a60d-bd7e98811347", "Clyde DePlanche", "178e2701-b833-5f98-b121-48cdd11142cb", "Sgt", "first nam", false],
  ["584ed69a-45a8-55d8-be95-c4001135be27", "Alfred J DePole", "7cb27d44-12c2-5fdf-a79f-16b97dd8b6b3", null, null, true],
] as const;

test("Batch 567 preserves page 114 rows 9-18 and masks every private value", () => {
  for (const [id, name, sourceRecordId, rank, notes, hasPrivateIdentifier] of cohort) {
    const person = profile(id);
    expect(person.display_name).toBe(name);
    expect(person.research_attempt_count).toBe(5);
    const sourceRecord = person.source_records.find(
      (record: { source_record_id: string }) =>
        record.source_record_id === sourceRecordId,
    );
    expect(sourceRecord).toMatchObject({
      archive_location: "230/86/29/07",
      box: "181",
      pdf_page: 114,
      rank_as_indexed: rank,
      notes_as_indexed: notes,
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

test("Batch 567 publishes three broad Army-entry occupations without inventing employers", () => {
  const expected = [
    [
      "1e92901c-6eb8-5ec8-a243-7961adc813ec",
      "Ferrous- or nonferrous-metals production occupation, not elsewhere classified",
      "1943-05-08",
    ],
    [
      "54fe4f71-a7ee-5406-9234-25a283cab43e",
      "Paymaster, payroll clerk, or timekeeper category",
      "1942-10-17",
    ],
    [
      "584ed69a-45a8-55d8-be95-c4001135be27",
      "Chauffeur or bus, taxi, truck, or tractor driver category",
      "1943-06-18",
    ],
  ] as const;

  for (const [id, occupation, endDate] of expected) {
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
        occupation,
        relationship_type: "unknown",
        end_date: endDate,
        temporal_basis: "strongly_date_bounded",
        identity_confidence: "confirmed",
        claim_confidence: "medium",
        canonical_organization: null,
      }),
    ]);
    expect(JSON.stringify(person)).toContain(
      "No reliable named pre-OSS employer has yet been identified",
    );
  }
});

test("Batch 567 publishes three qualified French or French-section OSS identities", () => {
  const claude = profile("b5a624a2-4177-5faa-b771-20380f275b58");
  expect(claude).toMatchObject({
    identity_status: "high_confidence",
    research_status: "requires_archival_review",
    personnel_category: "foreign_or_allied_military_personnel",
    commissioned_officer: true,
  });
  expect(claude.name_variants).toEqual(
    expect.arrayContaining(["Claude de Perthuis", "Ernest Claude de Perthuis", "Jean Bertrand"]),
  );
  expect(JSON.stringify(claude)).toContain("OSS Mission Diane");
  expect(JSON.stringify(claude)).toContain("NARA Mission Report Diane");

  const pierre = profile("c8645131-9d3a-53d7-9d84-41ebfcc13082");
  expect(pierre).toMatchObject({
    identity_status: "high_confidence",
    research_status: "requires_archival_review",
    personnel_category: "foreign_or_allied_military_personnel",
    commissioned_officer: true,
  });
  expect(pierre.name_variants).toContain("Pierre Depinay");
  expect(JSON.stringify(pierre)).toContain("middle initial R");
  expect(JSON.stringify(pierre)).toContain("Sous-Lieutenant");

  const gerard = profile("bb8ca645-9194-5f81-8291-eebb5422d8ea");
  expect(gerard).toMatchObject({
    identity_status: "high_confidence",
    research_status: "requires_archival_review",
    commissioned_officer: true,
  });
  expect(gerard.name_variants).toEqual(
    expect.arrayContaining(["Gerard de Piolenc", "Gérard de Piolenc"]),
  );
  expect(JSON.stringify(gerard)).toContain("The Secrets War");
  expect(JSON.stringify(gerard)).toContain("French section");

  for (const person of [claude, pierre, gerard]) {
    expect(person.immediate_pre_oss_affiliations).toEqual([]);
    expect(person.last_civilian_pre_service).toEqual([]);
    expect(person.other_pre_oss_affiliations).toEqual([]);
    expect(JSON.stringify(person)).toContain(
      "No reliable pre-OSS employer has yet been identified",
    );
  }
});

test("Batch 567 preserves four unresolved cases and Clyde DePlanche's truncated note", () => {
  for (const id of [
    "131357dc-d090-56a0-aef6-629d897c9502",
    "84055c54-45f7-54c7-a326-db74aa5e88e2",
    "f9e52678-9b71-51f2-b188-38d88462c743",
    "3c25b26f-0104-52cf-a60d-bd7e98811347",
  ]) {
    const person = profile(id);
    expect(person.identity_status).toBe("unresolved");
    expect(person.research_status).toBe("requires_archival_review");
    expect(person.immediate_pre_oss_affiliations).toEqual([]);
    expect(person.last_civilian_pre_service).toEqual([]);
    expect(person.other_pre_oss_affiliations).toEqual([]);
  }

  const harry = profile("f9e52678-9b71-51f2-b188-38d88462c743");
  expect(JSON.stringify(harry)).toContain("Leonard de Paur");
  expect(JSON.stringify(harry)).toContain("were rejected");

  const clyde = profile("3c25b26f-0104-52cf-a60d-bd7e98811347");
  expect(clyde.archival_file.review_priority).toBe("critical");
  expect(clyde.source_records[0].notes_as_indexed).toBe("first nam");
  expect(JSON.stringify(clyde)).toContain("truncated printed note");
});

test("Batch 567 advances attempted and archival coverage without employer inflation", () => {
  expect(stats).toMatchObject({
    source_rows: 23978,
    person_entities: 23940,
    possible_duplicate_groups: 254,
    research_attempted_people: 5436,
    research_attempt_percent: 22.7068,
    verified_affiliation_people: 585,
    verified_affiliation_percent: 2.4436,
    verified_employer_people: 259,
    verified_employer_percent: 1.0819,
    archival_review_assessed_people: 5391,
    archival_review_percent: 22.5188,
    public_sources: 3624,
    published_claims: 4385,
  });
  expect(stats.research_status_counts).toMatchObject({
    conflicting_sources: 114,
    documented_prewar_employer_found: 111,
    needs_identity_review: 319,
    not_started: 18504,
    occupation_only_found: 1009,
    requires_archival_review: 3214,
    verified_employer_found: 242,
  });
  expect(stats.identity_status_counts).toEqual({
    ambiguous: 272,
    confirmed: 1126,
    conflicting: 116,
    high_confidence: 736,
    probable: 176,
    unresolved: 21514,
  });
  expect(stats.commissioned_status_counts).toEqual({
    commissioned: 2287,
    not_commissioned: 6044,
    unknown: 15609,
  });
});

test("Batch 567 evidence exposes neither private identifier fields nor credentials", () => {
  expect(evidence).not.toMatch(/serial_number(_raw|_normalized)?/);
  expect(evidence).not.toContain('"serial_number"');
  expect(evidence).not.toContain("NARA_API_KEY");
  expect(evidence).not.toContain("x-api-key");
});
