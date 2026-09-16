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
    "../../research/evidence-pages-one-hundred-and-twelve-and-thirteen-george-c-demas-through-leon-m-demers-pathways_batch-561_2026-09-16.json",
    import.meta.url,
  ),
  "utf8",
);
const profile = (id: string) =>
  people.find((person: { person_id: string }) => person.person_id === id);

const cohort = [
  ["6c6c1e3e-ab48-5bfc-a544-7c86f9b56096", "George C Demas", "52bc7f67-d803-5b62-b985-4cb7ae494cf4", 112, null, false],
  ["04e3e66c-a3ac-5f62-8c06-335cc6e9aa9e", "John Demas Jr.", "de6a32a2-69bc-5be5-bcab-01020005a278", 112, "Pfc", true],
  ["514a128b-36e7-5a75-a1bb-2e64ef885b8e", "Samuel F Demastrie", "7ccd79df-8bb1-5ef8-9b77-c2cc66dfbf6f", 112, null, true],
  ["2ea94b9f-0205-535c-be83-a75533088c97", "Joseph A Dematteo", "58de4bb2-589b-525f-af9e-70520727ea92", 112, null, true],
  ["402b1043-9708-51ea-a34d-6b10cd48c77a", "Priscilla DeMauduit", "47d4ecc0-a075-5ca2-b824-8c534110f9a0", 112, null, false],
  ["3767278c-1c50-57c7-accd-4df159802c22", "Anthony DeMayo", "6bcc3fda-3ebd-57c4-9a71-7bad3ee185dc", 112, null, false],
  ["85d37065-4914-51b3-910d-c2476032c7cb", "Gertrude J Dembe", "f494cda5-c6d3-54f8-8bd7-19d99561e0bd", 112, null, false],
  ["8413428e-0fab-5ebc-b098-5658bb623511", "Fernando DeMello", "647ef354-792f-5218-99d6-eda8b475d28e", 113, null, false],
  ["4a9316d7-ce0f-5411-a621-43b98b2f23db", "Gilbert Dementis", "6dd44c7a-f226-5161-bb0b-642c215c0f54", 113, null, true],
  ["ac37d7a8-6698-57c1-b9e7-a3d8674b8736", "Leon M Demers", "f2fe05ae-899b-52dc-9255-56ba147aff76", 113, null, true],
] as const;

test("Batch 561 preserves page 112 rows 40-46 and page 113 rows 1-3", () => {
  for (const [id, name, sourceRecordId, page, rank, hasPrivateIdentifier] of cohort) {
    const person = profile(id);
    expect(person.display_name).toBe(name);
    expect(person.research_attempt_count).toBe(5);
    const sourceRecord = person.source_records.find(
      (record: { source_record_id: string }) => record.source_record_id === sourceRecordId,
    );
    expect(sourceRecord).toMatchObject({
      archive_location: "230/86/29/07",
      box: "179",
      pdf_page: page,
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

test("Batch 561 publishes only three exact-identifier Army statuses", () => {
  const expectations = [
    ["04e3e66c-a3ac-5f62-8c06-335cc6e9aa9e", "Student", "student", "1943-03-29"],
    ["2ea94b9f-0205-535c-be83-a75533088c97", "Machinists", "unknown", "1942-11-17"],
    ["4a9316d7-ce0f-5411-a621-43b98b2f23db", "Student", "student", "1944-04-10"],
  ] as const;
  for (const [id, occupation, relationshipType, endDate] of expectations) {
    const person = profile(id);
    expect(person).toMatchObject({
      identity_status: "confirmed",
      research_status: "occupation_only_found",
      personnel_category: "enlisted_army_personnel",
      commissioned_officer: false,
      manual_review_required: true,
    });
    expect(person.immediate_pre_oss_affiliations).toEqual([]);
    expect(person.last_civilian_pre_service).toEqual([]);
    expect(person.other_pre_oss_affiliations).toEqual([
      expect.objectContaining({
        canonical_organization: null,
        occupation,
        relationship_type: relationshipType,
        end_date: endDate,
        temporal_basis: "strongly_date_bounded",
        identity_confidence: "confirmed",
        claim_confidence: "medium",
      }),
    ]);
  }
});

test("Batch 561 keeps student status distinct from employment", () => {
  for (const id of [
    "04e3e66c-a3ac-5f62-8c06-335cc6e9aa9e",
    "4a9316d7-ce0f-5411-a621-43b98b2f23db",
  ]) {
    const person = profile(id);
    const status = person.other_pre_oss_affiliations[0];
    expect(status.relationship_type).toBe("student");
    expect(status.canonical_organization).toBeNull();
    expect(JSON.stringify(person)).toContain("Student status is not an employer");
  }
});

test("Batch 561 exposes the Samuel Demastrie identifier conflict without leaking the namesake", () => {
  const samuel = profile("514a128b-36e7-5a75-a1bb-2e64ef885b8e");
  expect(samuel).toMatchObject({
    identity_status: "conflicting",
    research_status: "conflicting_sources",
    personnel_category: "unknown_or_indeterminate",
    commissioned_officer: null,
    manual_review_required: true,
  });
  expect(samuel.immediate_pre_oss_affiliations).toEqual([]);
  expect(samuel.last_civilian_pre_service).toEqual([]);
  expect(samuel.other_pre_oss_affiliations).toEqual([]);
  expect(JSON.stringify(samuel)).toContain("conflicts with the official Army merged file");
  expect(JSON.stringify(samuel)).toContain("differently named Army entrant");
  expect(JSON.stringify(samuel)).not.toContain("occupation value");
});

test("Batch 561 does not pad Leon Demers's seven-digit source value", () => {
  const leon = profile("ac37d7a8-6698-57c1-b9e7-a3d8674b8736");
  expect(leon).toMatchObject({
    identity_status: "unresolved",
    research_status: "requires_archival_review",
    personnel_category: "unknown_or_indeterminate",
    commissioned_officer: null,
    manual_review_required: true,
  });
  expect(leon.immediate_pre_oss_affiliations).toEqual([]);
  expect(leon.last_civilian_pre_service).toEqual([]);
  expect(leon.other_pre_oss_affiliations).toEqual([]);
  expect(JSON.stringify(leon)).toContain("seven-digit");
  expect(JSON.stringify(leon)).toContain("cannot be silently padded");
  expect(JSON.stringify(leon)).not.toContain("manufacture of boots and shoes");
});

test("Batch 561 completes the accessible protocol for six other unresolved profiles", () => {
  for (const id of [
    "6c6c1e3e-ab48-5bfc-a544-7c86f9b56096",
    "402b1043-9708-51ea-a34d-6b10cd48c77a",
    "3767278c-1c50-57c7-accd-4df159802c22",
    "85d37065-4914-51b3-910d-c2476032c7cb",
    "8413428e-0fab-5ebc-b098-5658bb623511",
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

test("Batch 561 advances research and archival coverage without adding an employer", () => {
  expect(stats).toMatchObject({
    source_rows: 23978,
    person_entities: 23940,
    possible_duplicate_groups: 251,
    research_attempted_people: 5376,
    research_attempt_percent: 22.4561,
    verified_affiliation_people: 583,
    verified_affiliation_percent: 2.4353,
    verified_employer_people: 258,
    verified_employer_percent: 1.0777,
    archival_review_assessed_people: 5331,
    archival_review_percent: 22.2682,
    public_sources: 3583,
    published_claims: 4283,
  });
  expect(stats.research_status_counts).toMatchObject({
    conflicting_sources: 112,
    not_started: 18564,
    occupation_only_found: 997,
    requires_archival_review: 3183,
    verified_employer_found: 241,
  });
  expect(stats.identity_status_counts).toEqual({
    ambiguous: 263,
    confirmed: 1110,
    conflicting: 114,
    high_confidence: 730,
    probable: 172,
    unresolved: 21551,
  });
});

test("Batch 561 evidence package exposes neither private identifiers nor credentials", () => {
  expect(evidence).not.toMatch(/serial_number(_raw|_normalized)?/);
  expect(evidence).not.toContain('"serial_number"');
  expect(evidence).not.toContain("NARA_API_KEY");
  expect(evidence).not.toContain("x-api-key");
});
