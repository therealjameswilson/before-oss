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
    "../../research/evidence-page-one-hundred-and-thirteen-lawrence-g-demgen-through-john-j-demoore-pathways_batch-562_2026-09-16.json",
    import.meta.url,
  ),
  "utf8",
);
const profile = (id: string) =>
  people.find((person: { person_id: string }) => person.person_id === id);

const cohort = [
  ["1f2eb0fe-f1c1-588e-9b58-ea5258cfbc88", "Lawrence G Demgen", "53006725-0c23-5003-a992-74c8a7295c80", "Capt", null, false],
  ["3d68087b-abcc-5d13-9e9f-199f71b0369b", "Livia M Demian", "3647f5c2-ee31-5cc3-804f-cd1dfe5c3f02", null, null, false],
  ["37c1697a-cd31-50e7-b400-1fbb87f6dc50", "Igor Demidoff", "8446a327-c49e-5c1d-93c0-9dcf0d8485ba", "Lt", "French", false],
  ["fea7cf0e-7a0d-571a-85c3-da2ae8e498ae", "Evelyn Demier", "5be2d0e2-5173-528b-88e0-4395c950cbba", null, null, false],
  ["7de6016d-5cd5-5248-8d9a-df12900421ba", "Arto DeMirjian", "e7d8d671-7fa8-5920-9953-bf194e283535", null, null, true],
  ["5671e8e5-966d-587c-8215-cd18c384ce43", "Jerome E Demontesante", "3a5695d7-39af-5986-b084-4ae546d49e99", null, null, true],
  ["f5c757fd-e243-552e-968c-7f1a6a8b7f1a", "Giovanni DeMontis", "106a3252-66e4-574e-9261-62dc39607cc3", null, null, false],
  ["32753f1b-c22e-5f27-ae3e-f02c12957b89", "John Demontis", "8e015323-28c0-5918-875d-0146d1a937d8", null, null, true],
  ["4417eefa-4882-5695-9631-ed5232e5fb7c", "Eugene W Demoore", "45f3994c-dd0f-599f-8a08-ff4d8fd5367e", null, null, true],
  ["b8a4fb62-a0bd-537a-a3db-aa30d34921e4", "John J DeMoore", "fd53fe67-f621-5da5-ae3c-7d2ccf29b7ba", null, null, true],
] as const;

test("Batch 562 preserves page 113 rows 4-13", () => {
  for (const [id, name, sourceRecordId, rank, note, hasPrivateIdentifier] of cohort) {
    const person = profile(id);
    expect(person.display_name).toBe(name);
    expect(person.research_attempt_count).toBe(5);
    const sourceRecord = person.source_records.find(
      (record: { source_record_id: string }) => record.source_record_id === sourceRecordId,
    );
    expect(sourceRecord).toMatchObject({
      archive_location: "230/86/29/07",
      box: "179",
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

test("Batch 562 confirms Eugene DeMoore's Army pathway without inventing an employer", () => {
  const eugene = profile("4417eefa-4882-5695-9631-ed5232e5fb7c");
  expect(eugene).toMatchObject({
    identity_status: "confirmed",
    research_status: "occupation_only_found",
    personnel_category: "commissioned_army_officer",
    commissioned_officer: true,
    manual_review_required: true,
  });
  expect(eugene.immediate_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      canonical_organization: "United States Army Field Artillery",
      relationship_type: "military_assignment",
      immediate_pre_oss: true,
      temporal_basis: "explicit_immediate",
      claim_confidence: "confirmed",
    }),
  ]);
  expect(eugene.last_civilian_pre_service).toEqual([]);
  expect(eugene.other_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      canonical_organization: null,
      occupation: "Civil engineer",
      city: "New York",
      relationship_type: "unknown",
      end_date: "1940-10-08",
      claim_confidence: "high",
    }),
  ]);
  expect(JSON.stringify(eugene)).toContain("names no firm, agency or practice arrangement");
});

test("Batch 562 publishes John J DeMoore's exact-identifier occupation only", () => {
  const john = profile("b8a4fb62-a0bd-537a-a3db-aa30d34921e4");
  expect(john).toMatchObject({
    identity_status: "confirmed",
    research_status: "occupation_only_found",
    personnel_category: "enlisted_army_personnel",
    commissioned_officer: false,
  });
  expect(john.immediate_pre_oss_affiliations).toEqual([]);
  expect(john.last_civilian_pre_service).toEqual([]);
  expect(john.other_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      canonical_organization: null,
      occupation: "Tinsmiths, coppersmiths, and sheet metal workers",
      relationship_type: "unknown",
      end_date: "1943-04-26",
      temporal_basis: "strongly_date_bounded",
      claim_confidence: "medium",
    }),
  ]);
});

test("Batch 562 keeps Igor Demidoff's official file pointer separate from affiliation claims", () => {
  const igor = profile("37c1697a-cd31-50e7-b400-1fbb87f6dc50");
  expect(igor).toMatchObject({
    identity_status: "high_confidence",
    research_status: "requires_archival_review",
    personnel_category: "foreign_or_allied_military_personnel",
    commissioned_officer: true,
    allied_or_foreign_personnel: true,
  });
  expect(igor.immediate_pre_oss_affiliations).toEqual([]);
  expect(igor.last_civilian_pre_service).toEqual([]);
  expect(igor.other_pre_oss_affiliations).toEqual([]);
  expect(JSON.stringify(igor)).toContain("GR 28 P 4 113 / 57");
  expect(JSON.stringify(igor)).toContain("GR 16 P 173874");
});

test("Batch 562 preserves the Demian-Denain and Giovanni-John duplicate questions", () => {
  const demian = profile("3d68087b-abcc-5d13-9e9f-199f71b0369b");
  const denain = profile("5e9bdd16-b771-5b64-9164-aa332ad8f1ff");
  expect(demian.possible_duplicate_group).toBeTruthy();
  expect(demian.possible_duplicate_group).toBe(denain.possible_duplicate_group);
  expect(denain).toMatchObject({
    identity_status: "ambiguous",
    research_status: "not_started",
    research_attempt_count: 0,
  });

  const giovanni = profile("f5c757fd-e243-552e-968c-7f1a6a8b7f1a");
  const john = profile("32753f1b-c22e-5f27-ae3e-f02c12957b89");
  expect(giovanni.possible_duplicate_group).toBeTruthy();
  expect(giovanni.possible_duplicate_group).toBe(john.possible_duplicate_group);
  expect(john).toMatchObject({
    identity_status: "high_confidence",
    research_status: "requires_archival_review",
    personnel_category: "enlisted_army_personnel",
  });
  expect(john.immediate_pre_oss_affiliations).toEqual([]);
  expect(john.last_civilian_pre_service).toEqual([]);
  expect(john.other_pre_oss_affiliations).toEqual([]);
  expect(JSON.stringify(john)).toContain("Bathtub 1 mission to Sardinia");
});

test("Batch 562 withholds unresolved, conflicting, and low-confidence candidates", () => {
  const jerome = profile("5671e8e5-966d-587c-8215-cd18c384ce43");
  expect(jerome).toMatchObject({
    identity_status: "conflicting",
    research_status: "conflicting_sources",
    manual_review_required: true,
  });
  expect(JSON.stringify(jerome)).toContain("differently named Army entrant");
  expect(jerome.immediate_pre_oss_affiliations).toEqual([]);
  expect(jerome.last_civilian_pre_service).toEqual([]);
  expect(jerome.other_pre_oss_affiliations).toEqual([]);

  const arto = profile("7de6016d-5cd5-5248-8d9a-df12900421ba");
  expect(arto).toMatchObject({
    identity_status: "probable",
    research_status: "needs_identity_review",
  });
  expect(arto.immediate_pre_oss_affiliations).toEqual([]);
  expect(arto.last_civilian_pre_service).toEqual([]);
  expect(arto.other_pre_oss_affiliations).toEqual([]);

  for (const id of [
    "1f2eb0fe-f1c1-588e-9b58-ea5258cfbc88",
    "fea7cf0e-7a0d-571a-85c3-da2ae8e498ae",
  ]) {
    const person = profile(id);
    expect(person.identity_status).toBe("unresolved");
    expect(person.research_status).toBe("requires_archival_review");
    expect(person.immediate_pre_oss_affiliations).toEqual([]);
    expect(person.last_civilian_pre_service).toEqual([]);
    expect(person.other_pre_oss_affiliations).toEqual([]);
  }
});

test("Batch 562 advances affiliation and archival coverage without adding an employer", () => {
  expect(stats).toMatchObject({
    source_rows: 23978,
    person_entities: 23940,
    possible_duplicate_groups: 253,
    research_attempted_people: 5386,
    research_attempt_percent: 22.4979,
    verified_affiliation_people: 584,
    verified_affiliation_percent: 2.4394,
    verified_employer_people: 258,
    verified_employer_percent: 1.0777,
    archival_review_assessed_people: 5342,
    archival_review_percent: 22.3141,
    public_sources: 3591,
    published_claims: 4301,
  });
  expect(stats.research_status_counts).toMatchObject({
    conflicting_sources: 113,
    needs_identity_review: 310,
    not_started: 18554,
    occupation_only_found: 999,
    requires_archival_review: 3187,
    verified_employer_found: 241,
  });
  expect(stats.identity_status_counts).toEqual({
    ambiguous: 265,
    confirmed: 1112,
    conflicting: 115,
    high_confidence: 732,
    probable: 174,
    unresolved: 21542,
  });
});

test("Batch 562 evidence package exposes neither private identifiers nor credentials", () => {
  expect(evidence).not.toMatch(/serial_number(_raw|_normalized)?/);
  expect(evidence).not.toContain('"serial_number"');
  expect(evidence).not.toContain("NARA_API_KEY");
  expect(evidence).not.toContain("x-api-key");
});
