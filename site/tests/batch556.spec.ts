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
    "../../research/evidence-page-one-hundred-and-eleven-bruce-e-delapp-through-marion-m-deleva-pathways_batch-556_2026-09-15.json",
    import.meta.url,
  ),
  "utf8",
);
const profile = (id: string) =>
  people.find((person: { person_id: string }) => person.person_id === id);

const cohort = [
  ["52658f7e-f1f9-5179-9aa8-525ed6be9c23", "Bruce E DeLapp", "57e755ec-0822-5e02-9e6a-5d4afaed2f46", null, null, true],
  ["c45ea48a-dfce-50cb-8b1d-d0ab46ff1682", "Albert V DeL'Arbre", "44aa89f3-79ca-5703-b466-01fb1f16bb12", null, null, true],
  ["d6a6a54d-6f8e-5c7b-ae1d-8f05777e8688", "DuRanzet DelaRoche", "31bd893c-9ee6-5ce8-b27f-b9f4511a0b0e", "Capt", "French", false],
  ["78860eb1-3b5b-5216-92a2-54db5afe26d2", "Antonio M DeLaTorre", "5dbb2261-7dcb-57e8-bdf3-076fd8cfd0f3", null, null, false],
  ["a01a2e73-fbe2-5b3f-85cb-ec4e82e2b4fb", "Gottfried Delatour", "7c768440-e182-5eea-b809-579b87535367", null, null, false],
  ["86a0a709-57c4-52d0-b0e1-3a55768826bd", "Jean P DeLaValdene", "0fff909f-966e-506f-a71d-6815edf1a110", null, null, false],
  ["8d76ef5c-53a3-5716-924d-b035def7610c", "Domenico DelBianco", "841e24e0-15c6-5d5a-8faa-0ba2bb55917d", null, null, true],
  ["8503fac3-fd47-534a-85b8-6bd1a04599b3", "Rene Delbos", "de257f0b-f934-5d20-a399-4c372372255d", null, null, false],
  ["6cc80245-c98a-5f79-8565-1774c9507999", "Edward A DelCarlo", "f75475ec-7062-5d46-b6b8-35cc8c85aa38", null, null, true],
  ["6ca4d542-7288-50b8-a656-b7fe66ac2f24", "Marion M DeLeva", "fdf30c7d-fe48-5cf3-b1c1-89d0813807a9", null, null, false],
] as const;

test("Batch 556 preserves page 111 rows 36-45 and masks four private fields", () => {
  for (const [id, name, sourceRecordId, rank, notes, hasPrivateIdentifier] of cohort) {
    const person = profile(id);
    expect(person.display_name).toBe(name);
    expect(person.research_attempt_count).toBeGreaterThanOrEqual(5);
    const sourceRecord = person.source_records.find(
      (record: { source_record_id: string }) => record.source_record_id === sourceRecordId,
    );
    expect(sourceRecord).toMatchObject({
      archive_location: "230/86/29/07",
      box: "178",
      pdf_page: 111,
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

test("Batch 556 confirms four Army identities but publishes only supported occupations", () => {
  const expectations = [
    ["52658f7e-f1f9-5179-9aa8-525ed6be9c23", "Student", "student", "1943-03-16"],
    ["c45ea48a-dfce-50cb-8b1d-d0ab46ff1682", "Secretary", "unknown", "1943-02-03"],
    ["6cc80245-c98a-5f79-8565-1774c9507999", "Farm hand, general farm", "unknown", "1942-10-16"],
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
    expect(person.other_pre_oss_affiliations).toHaveLength(1);
    expect(person.other_pre_oss_affiliations[0]).toMatchObject({
      canonical_organization: null,
      occupation,
      relationship_type: relationshipType,
      end_date: endDate,
      temporal_basis: "strongly_date_bounded",
      identity_confidence: "confirmed",
      claim_confidence: "medium",
    });
  }
  const domenico = profile("8d76ef5c-53a3-5716-924d-b035def7610c");
  expect(domenico).toMatchObject({
    identity_status: "confirmed",
    personnel_category: "enlisted_army_personnel",
    research_status: "requires_archival_review",
  });
  expect(domenico.other_pre_oss_affiliations).toEqual([]);
  expect(domenico.next_action).toContain("code 993 is undefined");
});

test("Batch 556 qualifies the Delatour and de la Valdene pathways", () => {
  const gottfried = profile("a01a2e73-fbe2-5b3f-85cb-ec4e82e2b4fb");
  expect(gottfried).toMatchObject({
    identity_status: "probable",
    research_status: "documented_prewar_employer_found",
  });
  expect(gottfried.name_variants).toContain("Gottfried Salomon-Delatour");
  expect(gottfried.other_pre_oss_affiliations).toEqual(expect.arrayContaining([
    expect.objectContaining({
      canonical_organization: "New School for Social Research",
      relationship_type: "employment",
      identity_confidence: "probable",
      claim_confidence: "medium",
      temporal_basis: "temporal_relation_uncertain",
    }),
    expect.objectContaining({
      canonical_organization: "University of Denver",
      relationship_type: "professional_affiliation",
      identity_confidence: "probable",
      claim_confidence: "medium",
    }),
  ]));
  expect(gottfried.immediate_pre_oss_affiliations).toEqual([]);
  expect(gottfried.last_civilian_pre_service).toEqual([]);

  const jean = profile("86a0a709-57c4-52d0-b0e1-3a55768826bd");
  expect(jean).toMatchObject({
    identity_status: "probable",
    research_status: "documented_prewar_employer_found",
  });
  expect(jean.name_variants).toContain("Jean Pierre de la Valdene");
  expect(jean.other_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      canonical_organization: null,
      occupation: "engineer",
      relationship_type: "self_employment",
      start_date: "1935",
      end_date: "1938",
      temporal_basis: "documented_prewar",
      identity_confidence: "probable",
      claim_confidence: "medium",
    }),
  ]);
});

test("Batch 556 keeps French archival leads separate and visible", () => {
  const duranzet = profile("d6a6a54d-6f8e-5c7b-ae1d-8f05777e8688");
  expect(duranzet).toMatchObject({
    identity_status: "ambiguous",
    personnel_category: "foreign_or_allied_military_personnel",
    commissioned_officer: true,
    allied_or_foreign_personnel: true,
    research_status: "needs_identity_review",
  });
  expect(duranzet.other_pre_oss_affiliations).toEqual([]);
  expect(JSON.stringify(duranzet)).toContain("GR 16 P 168164");

  const rene = profile("8503fac3-fd47-534a-85b8-6bd1a04599b3");
  expect(rene).toMatchObject({
    identity_status: "ambiguous",
    research_status: "needs_identity_review",
  });
  expect(rene.other_pre_oss_affiliations).toEqual([]);
  expect(JSON.stringify(rene)).toContain("GR 16 P 169127-169130");
  expect(rene.name_variants).toEqual(expect.arrayContaining([
    "Rene Georges Delbos",
    "Rene Louis Delbos",
    "Rene Pierre Delbos",
  ]));
});

test("Batch 556 leaves two name-only cases candidly unresolved", () => {
  for (const id of [
    "78860eb1-3b5b-5216-92a2-54db5afe26d2",
    "6ca4d542-7288-50b8-a656-b7fe66ac2f24",
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
    expect(person.claims).toEqual([
      expect.objectContaining({
        claim_type: "archival_file_status",
        claim_confidence: "high",
        publication_status: "published",
      }),
    ]);
  }
});

test("Batch 556 advances exact coverage without changing verified-employer totals", () => {
  expect(stats).toMatchObject({
    source_rows: 23978,
    person_entities: 23940,
    possible_duplicate_groups: 248,
    research_attempted_people: 5327,
    research_attempt_percent: 22.2515,
    verified_affiliation_people: 582,
    verified_affiliation_percent: 2.4311,
    verified_employer_people: 258,
    verified_employer_percent: 1.0777,
    archival_review_assessed_people: 5282,
    archival_review_percent: 22.0635,
    public_sources: 3559,
    published_claims: 4208,
  });
  expect(stats.research_status_counts).toMatchObject({
    documented_prewar_employer_found: 109,
    needs_identity_review: 299,
    not_started: 18613,
    occupation_only_found: 983,
    requires_archival_review: 3158,
    verified_employer_found: 241,
  });
  expect(stats.identity_status_counts).toEqual({
    ambiguous: 256,
    confirmed: 1094,
    conflicting: 113,
    high_confidence: 728,
    probable: 172,
    unresolved: 21577,
  });
});

test("Batch 556 evidence package contains no exposed private identifier", () => {
  expect(evidence).not.toMatch(/serial_number(_raw|_normalized)?/);
  expect(evidence).not.toContain('"serial_number"');
  expect(evidence).not.toContain("NARA_API_KEY");
  expect(evidence).not.toContain("x-api-key");
});
