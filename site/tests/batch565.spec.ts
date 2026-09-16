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
    "../../research/evidence-page-one-hundred-and-thirteen-william-denit-through-john-m-dennis-pathways_batch-565_2026-09-16.json",
    import.meta.url,
  ),
  "utf8",
);
const profile = (id: string) =>
  people.find((person: { person_id: string }) => person.person_id === id);

const cohort = [
  [
    "59c682ab-bb74-5fc5-9f42-6922c12ddc94",
    "William Denit",
    "d6b26df7-3c17-5727-9980-40b98b40ddb9",
    null,
    false,
  ],
  [
    "6bb9b4f1-cdae-5a5f-962c-9654281f0722",
    "Anthony J Denneau",
    "c318345f-5d41-5555-b46e-35d08e6fcefd",
    "1st Sgt",
    true,
  ],
  [
    "ff8d9423-3d2c-51cf-be95-7c5e2ddab8ac",
    "Daniel C Dennet Jr.",
    "c0352cd1-b48e-58dc-aa7c-e0346fcf4f19",
    null,
    false,
  ],
  [
    "9206b213-e887-511d-a1c4-02d21752425e",
    "Donald J Dennhardt",
    "67947d5f-bf61-556e-a2a4-c5fb83da1a89",
    null,
    true,
  ],
  [
    "1a5a6a85-de3c-5cf6-ae88-30abdceaa08a",
    "Alfred P Dennis",
    "73ef8154-0e12-59a8-aab4-81a0de64ce1d",
    null,
    false,
  ],
  [
    "f3de5438-6446-580a-a53c-454fcbabe8d4",
    "Edward J Dennis",
    "f50464ed-da1b-582a-a7b6-aa920d9c88ea",
    null,
    true,
  ],
  [
    "f95dcbe9-afee-568d-a7b9-62ad20ca43f5",
    "James A Dennis",
    "332bc4d4-65d4-5d09-914c-12a04cae9480",
    "1st Lt",
    true,
  ],
  [
    "f6af9284-77a9-56f5-aef5-52534a83791b",
    "James H Dennis",
    "b7d51002-e582-500a-99b9-592293fbe96a",
    null,
    true,
  ],
  [
    "8effbe20-4379-57cd-becd-326ebd8a3de4",
    "James S Dennis",
    "a3c577a0-8d44-59d3-972b-8698e31f8681",
    null,
    false,
  ],
  [
    "b5f771d9-823a-53ef-b17e-bfd0c260c114",
    "John M Dennis",
    "a05628f5-afcc-50b9-8f18-3da9688fc587",
    null,
    true,
  ],
] as const;

test("Batch 565 preserves page 113 rows 34-43", () => {
  for (const [id, name, sourceRecordId, rank, hasPrivateIdentifier] of cohort) {
    const person = profile(id);
    expect(person.display_name).toBe(name);
    expect(person.research_attempt_count).toBe(5);
    const sourceRecord = person.source_records.find(
      (record: { source_record_id: string }) =>
        record.source_record_id === sourceRecordId,
    );
    expect(sourceRecord).toMatchObject({
      archive_location: "230/86/29/07",
      box: "180",
      pdf_page: 113,
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

test("Batch 565 publishes Denit's Agriculture role without inventing immediacy", () => {
  const william = profile("59c682ab-bb74-5fc5-9f42-6922c12ddc94");
  expect(william).toMatchObject({
    identity_status: "probable",
    research_status: "documented_prewar_employer_found",
    archival_file: { review_priority: "high" },
  });
  expect(william.immediate_pre_oss_affiliations).toEqual([]);
  expect(william.last_civilian_pre_service).toEqual([]);
  expect(william.other_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      canonical_organization: "United States Department of Agriculture",
      historical_organization: "Department of Agriculture",
      role_title: "Accounting clerk",
      relationship_type: "government_assignment",
      temporal_basis: "documented_prewar",
      identity_confidence: "probable",
      claim_confidence: "medium",
    }),
  ]);
  expect(JSON.stringify(william)).toContain(
    "Before World War II he was an accounting clerk",
  );
});

test("Batch 565 confirms Denneau and publishes occupation only", () => {
  const anthony = profile("6bb9b4f1-cdae-5a5f-962c-9654281f0722");
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
      role_title: "Stock clerk",
      relationship_type: "unknown",
      temporal_basis: "strongly_date_bounded",
      identity_confidence: "confirmed",
      claim_confidence: "medium",
    }),
  ]);
  expect(JSON.stringify(anthony)).toContain("SO-ET to SO-CBI");
  expect(JSON.stringify(anthony)).toContain("regular radioman");
});

test("Batch 565 separates Dennett's probable Clark role from earlier AUB work", () => {
  const daniel = profile("ff8d9423-3d2c-51cf-be95-7c5e2ddab8ac");
  expect(daniel).toMatchObject({
    identity_status: "high_confidence",
    research_status: "documented_prewar_employer_found",
    archival_file: { review_priority: "high" },
  });
  const clark = expect.objectContaining({
    canonical_organization: "Clark University",
    role_title: "Professor of Islamic history",
    relationship_type: "employment",
    temporal_basis: "probable_immediate",
    identity_confidence: "high_confidence",
    claim_confidence: "medium",
  });
  expect(daniel.immediate_pre_oss_affiliations).toEqual([clark]);
  expect(daniel.last_civilian_pre_service).toEqual([clark]);
  expect(daniel.other_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      canonical_organization: "American University of Beirut",
      role_title: "Teacher of Islamic history",
      relationship_type: "employment",
      temporal_basis: "documented_prewar",
      claim_confidence: "medium",
    }),
  ]);
  expect(daniel.name_variants).toContain("Daniel Clement Dennett Jr.");
  expect(JSON.stringify(daniel)).not.toContain("Harvard University\"}");
});

test("Batch 565 publishes only date-bounded student status for Dennhardt and John Dennis", () => {
  for (const id of [
    "9206b213-e887-511d-a1c4-02d21752425e",
    "b5f771d9-823a-53ef-b17e-bfd0c260c114",
  ]) {
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
        role_title: "Student",
        relationship_type: "student",
        temporal_basis: "strongly_date_bounded",
        identity_confidence: "confirmed",
        claim_confidence: "medium",
      }),
    ]);
  }
});

test("Batch 565 withholds unsupported Edward and James H occupations", () => {
  for (const id of [
    "f3de5438-6446-580a-a53c-454fcbabe8d4",
    "f6af9284-77a9-56f5-aef5-52534a83791b",
  ]) {
    const person = profile(id);
    expect(person).toMatchObject({
      identity_status: "confirmed",
      research_status: "requires_archival_review",
      personnel_category: "enlisted_army_personnel",
      commissioned_officer: false,
    });
    expect(person.immediate_pre_oss_affiliations).toEqual([]);
    expect(person.last_civilian_pre_service).toEqual([]);
    expect(person.other_pre_oss_affiliations).toEqual([]);
  }
  expect(JSON.stringify(profile("f3de5438-6446-580a-a53c-454fcbabe8d4"))).not.toContain(
    "occupation code 999",
  );
  expect(JSON.stringify(profile("f6af9284-77a9-56f5-aef5-52534a83791b"))).toContain(
    "after OSS dissolution",
  );
});

test("Batch 565 leaves three unsupported common-name profiles unresolved", () => {
  for (const id of [
    "1a5a6a85-de3c-5cf6-ae88-30abdceaa08a",
    "f95dcbe9-afee-568d-a7b9-62ad20ca43f5",
    "8effbe20-4379-57cd-becd-326ebd8a3de4",
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
  expect(profile("f95dcbe9-afee-568d-a7b9-62ad20ca43f5")).toMatchObject({
    personnel_category: "commissioned_army_officer",
    commissioned_officer: true,
    archival_file: { review_priority: "critical" },
  });
});

test("Batch 565 advances research and archival coverage without verified-employer inflation", () => {
  expect(stats).toMatchObject({
    source_rows: 23978,
    person_entities: 23940,
    possible_duplicate_groups: 254,
    research_attempted_people: 5416,
    research_attempt_percent: 22.6232,
    verified_affiliation_people: 585,
    verified_affiliation_percent: 2.4436,
    verified_employer_people: 259,
    verified_employer_percent: 1.0819,
    archival_review_assessed_people: 5371,
    archival_review_percent: 22.4353,
    public_sources: 3612,
    published_claims: 4352,
  });
  expect(stats.research_status_counts).toMatchObject({
    conflicting_sources: 114,
    documented_prewar_employer_found: 111,
    needs_identity_review: 316,
    not_started: 18524,
    occupation_only_found: 1004,
    requires_archival_review: 3202,
    verified_employer_found: 242,
  });
  expect(stats.identity_status_counts).toEqual({
    ambiguous: 269,
    confirmed: 1121,
    conflicting: 116,
    high_confidence: 734,
    probable: 176,
    unresolved: 21524,
  });
});

test("Batch 565 evidence exposes neither private identifiers nor credentials", () => {
  expect(evidence).not.toMatch(/serial_number(_raw|_normalized)?/);
  expect(evidence).not.toContain('"serial_number"');
  expect(evidence).not.toContain("NARA_API_KEY");
  expect(evidence).not.toContain("x-api-key");
});
