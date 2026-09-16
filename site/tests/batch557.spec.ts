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
    "../../research/evidence-page-one-hundred-and-eleven-joseph-h-delgoffe-through-john-a-dellangelo-pathways_batch-557_2026-09-15.json",
    import.meta.url,
  ),
  "utf8",
);
const profile = (id: string) =>
  people.find((person: { person_id: string }) => person.person_id === id);

const cohort = [
  ["a6bbe33c-1c49-54c1-b059-0b33832ff485", "Joseph H Delgoffe", "60856c14-ace7-56ce-98df-28eafde2922f", 111, null, null, true],
  ["ef42687e-0d91-5e0e-83f7-23ac13ee690b", "John W DelGreco", "ff0707e6-9b76-5bcc-92c9-d8680a43d625", 112, null, null, false],
  ["6ed7459a-f445-533d-8a20-66fd8ea2b91f", "John W Delgreco", "ebc5dae0-30d0-5e20-b3d7-4e149e0d9135", 112, null, null, true],
  ["3246b5d5-408f-5398-b689-97d11e08f1f2", "Marcel Delhomme", "072f0be6-1df4-535d-8648-55ca7765cd45", 112, "S/Lt", "French", false],
  ["4fc8cd62-d615-5494-a6af-e96099bb811f", "Mark M D'Elia", "3b39a3b7-5c77-5c73-b33c-22da326a45a2", 112, null, null, true],
  ["fa519d98-17cd-512d-9410-e4c857455f7b", "John A DeLisa", "a503f390-e0e6-5fc6-b7ac-1f8bd9ab9135", 112, null, null, true],
  ["c13cf7ac-296b-53d4-8c45-b7de60d14e11", "Norman M Delisle", "566fa2a2-5476-5933-99d7-3ec7b7a13e26", 112, null, null, true],
  ["dac038d6-74e9-574b-9de1-1b982dd69535", "William M Delkin", "ff163818-6e55-56f7-bdd4-2d9df9b795b5", 112, null, null, true],
  ["40ff40da-7f0b-5002-87fb-874d04b8e032", "Elizabeth Della", "e299a4f0-12a9-53b3-bf3d-6261d9019205", 112, null, null, true],
  ["f5b6f32c-1bf3-5368-a5d9-70996a8306a3", "John A Dellangelo", "c5c0a11d-8a9f-55cc-90b1-45ab059fec3f", 112, null, null, true],
] as const;

test("Batch 557 preserves the cross-page cohort and masks eight private fields", () => {
  for (const [id, name, sourceRecordId, page, rank, notes, hasPrivateIdentifier] of cohort) {
    const person = profile(id);
    expect(person.display_name).toBe(name);
    expect(person.research_attempt_count).toBeGreaterThanOrEqual(5);
    const sourceRecord = person.source_records.find(
      (record: { source_record_id: string }) => record.source_record_id === sourceRecordId,
    );
    expect(sourceRecord).toMatchObject({
      archive_location: "230/86/29/07",
      box: "178",
      pdf_page: page,
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

test("Batch 557 confines four Army-entry occupations to confirmed rows", () => {
  const expectations = [
    ["6ed7459a-f445-533d-8a20-66fd8ea2b91f", "Stenographer or typist", "unknown", "1941-10-02"],
    ["4fc8cd62-d615-5494-a6af-e96099bb811f", "Carpenter", "unknown", "1943-05-22"],
    ["c13cf7ac-296b-53d4-8c45-b7de60d14e11", "Student", "student", "1943-05-24"],
    ["dac038d6-74e9-574b-9de1-1b982dd69535", "Bookkeeper or cashier, except bank cashier", "unknown", "1942-01-06"],
  ] as const;
  for (const [id, occupation, relationshipType, endDate] of expectations) {
    const person = profile(id);
    expect(person).toMatchObject({
      identity_status: "confirmed",
      personnel_category: "enlisted_army_personnel",
      commissioned_officer: false,
      research_status: "occupation_only_found",
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

test("Batch 557 keeps adjacent DelGreco rows separate", () => {
  const noIdentifier = profile("ef42687e-0d91-5e0e-83f7-23ac13ee690b");
  const identifierConfirmed = profile("6ed7459a-f445-533d-8a20-66fd8ea2b91f");
  expect(noIdentifier.person_id).not.toBe(identifierConfirmed.person_id);
  expect(noIdentifier).toMatchObject({
    identity_status: "ambiguous",
    research_status: "needs_identity_review",
    manual_review_required: true,
  });
  expect(noIdentifier.possible_duplicate_group).toBe(identifierConfirmed.possible_duplicate_group);
  expect(noIdentifier.possible_duplicate_group).toMatch(/^duplicate-/);
  expect(noIdentifier.other_pre_oss_affiliations).toEqual([]);
  expect(identifierConfirmed.other_pre_oss_affiliations).toHaveLength(1);
});

test("Batch 557 publishes both Marcel Delhomme archival leads", () => {
  const marcel = profile("3246b5d5-408f-5398-b689-97d11e08f1f2");
  expect(marcel).toMatchObject({
    identity_status: "high_confidence",
    personnel_category: "foreign_or_allied_military_personnel",
    commissioned_officer: true,
    allied_or_foreign_personnel: true,
    research_status: "needs_identity_review",
  });
  expect(marcel.other_pre_oss_affiliations).toEqual([]);
  expect(JSON.stringify(marcel)).toContain("GR 16 P 170460");
  expect(JSON.stringify(marcel)).toContain("GR 16 P 170461");
});

test("Batch 557 rejects the DeLisa identifier conflict", () => {
  const delisa = profile("fa519d98-17cd-512d-9410-e4c857455f7b");
  expect(delisa).toMatchObject({
    identity_status: "ambiguous",
    research_status: "needs_identity_review",
    manual_review_required: true,
  });
  expect(delisa.other_pre_oss_affiliations).toEqual([]);
  expect(delisa.claims).toEqual([
    expect.objectContaining({
      claim_type: "archival_file_status",
      claim_confidence: "high",
      publication_status: "published",
    }),
  ]);
  expect(JSON.stringify(delisa)).toContain("identifiers disagree");
});

test("Batch 557 leaves three name-only cases candidly unresolved", () => {
  for (const id of [
    "a6bbe33c-1c49-54c1-b059-0b33832ff485",
    "40ff40da-7f0b-5002-87fb-874d04b8e032",
    "f5b6f32c-1bf3-5368-a5d9-70996a8306a3",
  ]) {
    const person = profile(id);
    expect(person).toMatchObject({
      identity_status: "unresolved",
      research_status: "requires_archival_review",
      manual_review_required: true,
    });
    expect(person.archival_file).toMatchObject({ box: "178", review_priority: "critical" });
    expect(person.immediate_pre_oss_affiliations).toEqual([]);
    expect(person.last_civilian_pre_service).toEqual([]);
    expect(person.other_pre_oss_affiliations).toEqual([]);
  }
});

test("Batch 557 advances terminal and archival coverage without inventing employers", () => {
  expect(stats).toMatchObject({
    source_rows: 23978,
    person_entities: 23940,
    possible_duplicate_groups: 249,
    research_attempted_people: 5337,
    research_attempt_percent: 22.2932,
    verified_affiliation_people: 582,
    verified_affiliation_percent: 2.4311,
    verified_employer_people: 258,
    verified_employer_percent: 1.0777,
    archival_review_assessed_people: 5292,
    archival_review_percent: 22.1053,
    public_sources: 3565,
    published_claims: 4223,
  });
  expect(stats.research_status_counts).toMatchObject({
    needs_identity_review: 302,
    not_started: 18603,
    occupation_only_found: 987,
    requires_archival_review: 3161,
    verified_employer_found: 241,
  });
  expect(stats.identity_status_counts).toEqual({
    ambiguous: 258,
    confirmed: 1098,
    conflicting: 113,
    high_confidence: 729,
    probable: 172,
    unresolved: 21570,
  });
});

test("Batch 557 evidence package contains no exposed private identifier", () => {
  expect(evidence).not.toMatch(/serial_number(_raw|_normalized)?/);
  expect(evidence).not.toContain('"serial_number"');
  expect(evidence).not.toContain("NARA_API_KEY");
  expect(evidence).not.toContain("x-api-key");
});
