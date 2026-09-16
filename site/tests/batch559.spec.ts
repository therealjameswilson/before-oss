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
    "../../research/evidence-page-one-hundred-and-twelve-anthony-deluca-through-anthony-j-demaio-pathways_batch-559_2026-09-16.json",
    import.meta.url,
  ),
  "utf8",
);
const reviewDecisions = fs.readFileSync(
  new URL("../../research/loc_review_decisions_2026-09-16_batch559.csv", import.meta.url),
  "utf8",
);
const profile = (id: string) =>
  people.find((person: { person_id: string }) => person.person_id === id);

const cohort = [
  ["28705044-56c6-570d-b9db-ffd758316581", "Anthony Deluca", "58df6225-15aa-54c9-b809-e0ed44cd2040", null, null, "178", true],
  ["00bb0d8c-4e7e-530e-b17f-4a36167525e9", "Frank F Deluca", "2213a7e3-0410-5be3-8438-4c67f5736d2e", "Sgt", null, "178", true],
  ["42d16aad-9179-5d09-b7cb-54cd609d6e22", "Paula Deluca", "8edf559e-4b34-59fe-8fad-052d66c50c19", null, null, "178", false],
  ["bde6a545-fe1a-5fe3-80a2-234645e09455", "Sara Deluca", "2f892d30-6a0c-5be7-a004-8525dafd19aa", null, null, "178", false],
  ["e5e85d2e-69bd-54ec-963d-4f94adb1239b", "Otto DeLucia", "8946407d-1aec-5995-a8b1-a266cabec24a", null, null, "178", true],
  ["63d2d5ab-ef15-53c9-9a41-c104e0bdcf2b", "Cesare J DelVaglio", "65d5ee0f-458a-593d-b082-85f79e8602fc", null, null, "178", true],
  ["c722f6de-cf99-5ac1-89e6-45a447a36100", "Geraldine S DelVaglio", "b0311c89-055d-5023-9932-a9db331de6ef", null, null, "178", false],
  ["52155de7-6b0d-5fc6-9cc4-d357bec81a2a", "Flora DelVecchio", "248e85a1-e979-5281-a1b9-251f8a37aff3", null, null, "178", false],
  ["6ef40d55-ee5f-55b7-a7d6-63fe77534d2d", "Pierre Delvoye", "a2dff8b9-cc0b-5f60-a835-0036223128b2", null, "Belgian", "178", false],
  ["4baee0d9-0d1a-52dc-bcfe-26934b4a20f9", "Anthony J Demaio", "8fb7a6f5-439c-50ea-b57e-6727c20a9d56", null, null, "179", true],
] as const;

test("Batch 559 preserves page 112 rows 20-29 and masks five private fields", () => {
  for (const [id, name, sourceRecordId, rank, notes, box, hasPrivateIdentifier] of cohort) {
    const person = profile(id);
    expect(person.display_name).toBe(name);
    expect(person.research_attempt_count).toBe(5);
    const sourceRecord = person.source_records.find(
      (record: { source_record_id: string }) => record.source_record_id === sourceRecordId,
    );
    expect(sourceRecord).toMatchObject({
      archive_location: "230/86/29/07",
      box,
      pdf_page: 112,
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

test("Batch 559 keeps common-name Anthony Deluca ambiguous and rejects both newspaper hits", () => {
  const anthony = profile("28705044-56c6-570d-b9db-ffd758316581");
  expect(anthony).toMatchObject({
    identity_status: "ambiguous",
    research_status: "needs_identity_review",
    manual_review_required: true,
  });
  expect(anthony.archival_file).toMatchObject({ box: "178", review_priority: "critical" });
  expect(anthony.immediate_pre_oss_affiliations).toEqual([]);
  expect(anthony.last_civilian_pre_service).toEqual([]);
  expect(anthony.other_pre_oss_affiliations).toEqual([]);
  expect(JSON.stringify(anthony)).toContain("six common-name Army rows");
  expect(reviewDecisions.match(/,rejected,/g)).toHaveLength(2);
  expect(reviewDecisions).toContain("father of a school pupil");
  expect(reviewDecisions).toContain("dinner attendees");
});

test("Batch 559 confirms three identifier-backed Army identities", () => {
  for (const id of [
    "e5e85d2e-69bd-54ec-963d-4f94adb1239b",
    "63d2d5ab-ef15-53c9-9a41-c104e0bdcf2b",
    "4baee0d9-0d1a-52dc-bcfe-26934b4a20f9",
  ]) {
    expect(profile(id)).toMatchObject({
      identity_status: "confirmed",
      personnel_category: "enlisted_army_personnel",
      commissioned_officer: false,
      manual_review_required: true,
    });
  }
  expect(profile("e5e85d2e-69bd-54ec-963d-4f94adb1239b").name_variants).toContain(
    "Otto De Lucia",
  );
  expect(profile("63d2d5ab-ef15-53c9-9a41-c104e0bdcf2b").name_variants).toContain(
    "Cesare J Del Vaglio",
  );
});

test("Batch 559 publishes only Cesare DelVaglio and Anthony Demaio occupation categories", () => {
  const expectations = [
    [
      "63d2d5ab-ef15-53c9-9a41-c104e0bdcf2b",
      "Occupations in manufacture of textiles, n.e.c.",
      "1943-03-02",
    ],
    ["4baee0d9-0d1a-52dc-bcfe-26934b4a20f9", "Machinists", "1942-09-30"],
  ] as const;
  for (const [id, occupation, endDate] of expectations) {
    const person = profile(id);
    expect(person.research_status).toBe("occupation_only_found");
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

test("Batch 559 leaves Otto DeLucia's residual occupation code uninterpreted", () => {
  const otto = profile("e5e85d2e-69bd-54ec-963d-4f94adb1239b");
  expect(otto.research_status).toBe("requires_archival_review");
  expect(otto.immediate_pre_oss_affiliations).toEqual([]);
  expect(otto.last_civilian_pre_service).toEqual([]);
  expect(otto.other_pre_oss_affiliations).toEqual([]);
  expect(JSON.stringify(otto)).toContain("residual civilian-occupation value 999");
  expect(JSON.stringify(otto)).toContain("too nonspecific");
});

test("Batch 559 preserves Pierre Delvoye's Belgian note without inventing a unit", () => {
  const pierre = profile("6ef40d55-ee5f-55b7-a7d6-63fe77534d2d");
  expect(pierre).toMatchObject({
    identity_status: "unresolved",
    research_status: "requires_archival_review",
    personnel_category: "unknown_or_indeterminate",
    commissioned_officer: null,
    allied_or_foreign_personnel: true,
  });
  expect(pierre.source_records[0].notes_as_indexed).toBe("Belgian");
  expect(pierre.immediate_pre_oss_affiliations).toEqual([]);
  expect(pierre.last_civilian_pre_service).toEqual([]);
  expect(pierre.other_pre_oss_affiliations).toEqual([]);
});

test("Batch 559 completes the accessible protocol for all ten people", () => {
  for (const id of [
    "00bb0d8c-4e7e-530e-b17f-4a36167525e9",
    "42d16aad-9179-5d09-b7cb-54cd609d6e22",
    "bde6a545-fe1a-5fe3-80a2-234645e09455",
    "c722f6de-cf99-5ac1-89e6-45a447a36100",
    "52155de7-6b0d-5fc6-9cc4-d357bec81a2a",
  ]) {
    const person = profile(id);
    expect(person).toMatchObject({
      identity_status: "unresolved",
      research_status: "requires_archival_review",
      manual_review_required: true,
    });
    expect(person.other_pre_oss_affiliations).toEqual([]);
    expect(JSON.stringify(person)).toContain(
      "No reliable pre-OSS employer has yet been identified",
    );
  }
});

test("Batch 559 advances research and archival coverage without changing verified-employer coverage", () => {
  expect(stats).toMatchObject({
    source_rows: 23978,
    person_entities: 23940,
    possible_duplicate_groups: 250,
    research_attempted_people: 5356,
    research_attempt_percent: 22.3726,
    verified_affiliation_people: 582,
    verified_affiliation_percent: 2.4311,
    verified_employer_people: 258,
    verified_employer_percent: 1.0777,
    archival_review_assessed_people: 5311,
    archival_review_percent: 22.1846,
    public_sources: 3574,
    published_claims: 4249,
  });
  expect(stats.research_status_counts).toMatchObject({
    needs_identity_review: 306,
    not_started: 18584,
    occupation_only_found: 991,
    requires_archival_review: 3172,
    verified_employer_found: 241,
  });
  expect(stats.identity_status_counts).toEqual({
    ambiguous: 262,
    confirmed: 1104,
    conflicting: 113,
    high_confidence: 729,
    probable: 172,
    unresolved: 21560,
  });
});

test("Batch 559 evidence package exposes neither private identifiers nor credentials", () => {
  expect(evidence).not.toMatch(/serial_number(_raw|_normalized)?/);
  expect(evidence).not.toContain('"serial_number"');
  expect(evidence).not.toContain("NARA_API_KEY");
  expect(evidence).not.toContain("x-api-key");
});
