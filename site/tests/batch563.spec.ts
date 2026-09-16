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
    "../../research/evidence-page-one-hundred-and-thirteen-john-d-dempsey-through-gusbert-denbesten-pathways_batch-563_2026-09-16.json",
    import.meta.url,
  ),
  "utf8",
);
const profile = (id: string) =>
  people.find((person: { person_id: string }) => person.person_id === id);

const cohort = [
  [
    "c578149c-a3ce-535c-9e00-cb5ee49f4fef",
    "John D Dempsey",
    "53eaab7f-0c48-5935-8bea-df746c3d04fd",
    "179",
    null,
    null,
    true,
  ],
  [
    "c2db85ef-4192-5521-9701-26f5e66c8d94",
    "John F Dempsey",
    "77026443-38bd-5a3d-a848-35c98352e1c7",
    "179",
    "Capt",
    null,
    true,
  ],
  [
    "a4250eaf-d4ca-556b-8abb-bd27113e8d47",
    "Mary E Demsford",
    "42a0a79f-22e6-5ac4-8cc6-7052b6edc8a4",
    "179",
    null,
    null,
    false,
  ],
  [
    "af20fa45-9ad6-539c-825d-7f2dc7b155c5",
    "Robert E Demuth",
    "08a915bf-248d-59dc-84d2-cc15d3799665",
    "179",
    null,
    null,
    true,
  ],
  [
    "5e9bdd16-b771-5b64-9164-aa332ad8f1ff",
    "Livia M Denain",
    "70be1d2f-ef5a-5c36-b0c3-38c254fe3d31",
    "179",
    null,
    null,
    false,
  ],
  [
    "4c1b9919-6e72-5d59-9496-c9c4d4b3402b",
    "Jean Denamiel",
    "aee60ac1-00ba-5f7e-a321-dc2994a5a43c",
    "179",
    "S/Lt",
    "French",
    false,
  ],
  [
    "0474843e-f742-5073-bd85-cdc8ba7fe6b9",
    "Lorene Denard",
    "e4f2a3a4-7dba-5783-afd9-0de82db1e7bd",
    "179",
    null,
    null,
    false,
  ],
  [
    "4bad86f5-ac40-53f4-96fc-55fd71718d3e",
    "Joseph Denaro",
    "0c030bae-142b-5a68-ba78-e762d4d37991",
    "179",
    null,
    null,
    true,
  ],
  [
    "05017bd7-cb68-5c46-ae9e-9234230c65c5",
    "Dennis Denaxas",
    "46c69c57-6990-57e5-9092-799213799728",
    "180",
    null,
    null,
    true,
  ],
  [
    "71814f14-0513-5e21-a2d1-2b018bc75d5e",
    "Gusbert DenBesten",
    "5d30f110-f603-596d-bd53-bb2e68f047c0",
    "180",
    null,
    "possibly",
    false,
  ],
] as const;

test("Batch 563 preserves page 113 rows 14-23", () => {
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

test("Batch 563 publishes Joseph Denaro's high-confidence Mabley's employment", () => {
  const joseph = profile("4bad86f5-ac40-53f4-96fc-55fd71718d3e");
  expect(joseph).toMatchObject({
    identity_status: "confirmed",
    research_status: "verified_employer_found",
    personnel_category: "enlisted_army_personnel",
    commissioned_officer: false,
    manual_review_required: false,
  });
  const expected = expect.objectContaining({
    canonical_organization: "Mabley's",
    historical_organization: "Mabley's",
    role_title: "Hairdresser and beauty-salon personnel supervisor",
    occupation: "Hairdresser; beauty-salon personnel supervisor",
    relationship_type: "employment",
    city: "Cincinnati",
    state_or_region: "Ohio",
    temporal_basis: "strongly_date_bounded",
    identity_confidence: "confirmed",
    claim_confidence: "high",
  });
  expect(joseph.immediate_pre_oss_affiliations).toEqual([expected]);
  expect(joseph.last_civilian_pre_service).toEqual([expected]);
  expect(joseph.other_pre_oss_affiliations).toEqual([]);
  expect(JSON.stringify(joseph)).toContain(
    "Was in charge of personnel for beauty salon",
  );
  expect(JSON.stringify(joseph)).toContain("Jos (Alice) hairdrsr Mabley's");
});

test("Batch 563 withholds unresolved Dempsey and Denamiel candidates", () => {
  const john = profile("c578149c-a3ce-535c-9e00-cb5ee49f4fef");
  expect(john).toMatchObject({
    identity_status: "ambiguous",
    research_status: "needs_identity_review",
    archival_file: { review_priority: "critical" },
  });
  expect(JSON.stringify(john)).not.toContain("served in Burma");

  const jean = profile("4c1b9919-6e72-5d59-9496-c9c4d4b3402b");
  expect(jean).toMatchObject({
    identity_status: "probable",
    research_status: "needs_identity_review",
    personnel_category: "foreign_or_allied_military_personnel",
    allied_or_foreign_personnel: true,
  });
  expect(jean.immediate_pre_oss_affiliations).toEqual([]);
  expect(jean.last_civilian_pre_service).toEqual([]);
  expect(jean.other_pre_oss_affiliations).toEqual([]);
});

test("Batch 563 preserves the Livia Demian-Denain duplicate question", () => {
  const demian = profile("3d68087b-abcc-5d13-9e9f-199f71b0369b");
  const denain = profile("5e9bdd16-b771-5b64-9164-aa332ad8f1ff");
  expect(denain).toMatchObject({
    identity_status: "ambiguous",
    research_status: "needs_identity_review",
    research_attempt_count: 5,
  });
  expect(denain.possible_duplicate_group).toBeTruthy();
  expect(denain.possible_duplicate_group).toBe(demian.possible_duplicate_group);
});

test("Batch 563 leaves six unsupported profiles without affiliations", () => {
  for (const id of [
    "c2db85ef-4192-5521-9701-26f5e66c8d94",
    "a4250eaf-d4ca-556b-8abb-bd27113e8d47",
    "af20fa45-9ad6-539c-825d-7f2dc7b155c5",
    "0474843e-f742-5073-bd85-cdc8ba7fe6b9",
    "05017bd7-cb68-5c46-ae9e-9234230c65c5",
    "71814f14-0513-5e21-a2d1-2b018bc75d5e",
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

test("Batch 563 advances verified employer and archival coverage", () => {
  expect(stats).toMatchObject({
    source_rows: 23978,
    person_entities: 23940,
    possible_duplicate_groups: 253,
    research_attempted_people: 5396,
    research_attempt_percent: 22.5397,
    verified_affiliation_people: 585,
    verified_affiliation_percent: 2.4436,
    verified_employer_people: 259,
    verified_employer_percent: 1.0819,
    archival_review_assessed_people: 5351,
    archival_review_percent: 22.3517,
    public_sources: 3596,
    published_claims: 4313,
  });
  expect(stats.research_status_counts).toMatchObject({
    conflicting_sources: 113,
    needs_identity_review: 313,
    not_started: 18544,
    occupation_only_found: 999,
    requires_archival_review: 3193,
    verified_employer_found: 242,
  });
  expect(stats.identity_status_counts).toEqual({
    ambiguous: 266,
    confirmed: 1113,
    conflicting: 115,
    high_confidence: 732,
    probable: 175,
    unresolved: 21539,
  });
});

test("Batch 563 evidence exposes neither private identifiers nor credentials", () => {
  expect(evidence).not.toMatch(/serial_number(_raw|_normalized)?/);
  expect(evidence).not.toContain('"serial_number"');
  expect(evidence).not.toContain("NARA_API_KEY");
  expect(evidence).not.toContain("x-api-key");
});
