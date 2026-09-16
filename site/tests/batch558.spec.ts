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
    "../../research/evidence-page-one-hundred-and-twelve-angelo-j-dellanno-through-alfonso-deluca-pathways_batch-558_2026-09-16.json",
    import.meta.url,
  ),
  "utf8",
);
const profile = (id: string) =>
  people.find((person: { person_id: string }) => person.person_id === id);

const cohort = [
  ["6bcc9184-fc3e-52b3-baff-cb55e62a6a80", "Angelo J Dell'Anno", "89489938-29e7-5d52-982b-1a7712b9c8d2", null, null, true],
  ["33ab954d-083d-53fb-b2d5-867363013a50", "Angelo J Dellano", "32852bbd-be2d-58de-b337-d22088b0634c", null, null, false],
  ["b87166c0-7516-5063-b775-372847309537", "Geroge Delmas", "4e4e778f-13b2-5747-ad50-e0a8a543baad", "Lt. Col", "French", false],
  ["86a952a7-c08e-50b9-be06-fbcdb2af8f37", "Jacques Delmas", "9f28d6f7-e0b9-5001-a8a7-4760c5a6f6c5", null, "French", false],
  ["fa2378b2-c115-5a6a-8a15-32cbf486adc0", "Adolph Delmotte Jr.", "d5e9911b-d758-519f-93a2-5c31930fab9d", null, null, true],
  ["63e591e1-56d2-585d-b73d-c7e6ca9ad462", "Armand Delong", "29208b28-b7f2-5033-bf07-dd393d92f7f3", null, null, false],
  ["69653221-4857-5c8c-b877-68097bcead96", "Roland C DeLormae", "96ab6900-5d1e-50fa-904c-5540cc6248ae", null, null, true],
  ["d409388e-72ba-595e-bee2-173c04325fd3", "John S Delphenich", "74ea77f4-a7d7-582b-ad65-bc917758598a", "T/Sgt", null, true],
  ["051d687b-4485-5eab-ba91-d0ac0197ec27", "Peter J Delpome", "67a51a2e-6bbe-57d5-b067-f609b9061ed2", null, null, true],
  ["a60a5968-ca2d-59a1-b35c-65642f39b29d", "Alfonso DeLuca", "becab382-4f1e-5f37-b6d7-02c1f56b65c7", null, null, false],
] as const;

test("Batch 558 preserves page 112 rows 10-19 and masks five private fields", () => {
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
  expect(profile("86a952a7-c08e-50b9-be06-fbcdb2af8f37").research_attempt_count).toBe(16);
});

test("Batch 558 keeps the adjacent Dell'Anno and Dellano rows separate", () => {
  const withIdentifier = profile("6bcc9184-fc3e-52b3-baff-cb55e62a6a80");
  const withoutIdentifier = profile("33ab954d-083d-53fb-b2d5-867363013a50");
  expect(withIdentifier.person_id).not.toBe(withoutIdentifier.person_id);
  for (const person of [withIdentifier, withoutIdentifier]) {
    expect(person).toMatchObject({
      identity_status: "ambiguous",
      research_status: "needs_identity_review",
      manual_review_required: true,
    });
    expect(person.possible_duplicate_group).toMatch(/^duplicate-/);
    expect(person.other_pre_oss_affiliations).toEqual([]);
  }
  expect(withIdentifier.possible_duplicate_group).toBe(withoutIdentifier.possible_duplicate_group);
  expect(JSON.stringify(withIdentifier)).toContain("identifiers");
});

test("Batch 558 preserves Geroge and publishes unresolved French archival alternatives", () => {
  const geroge = profile("b87166c0-7516-5063-b775-372847309537");
  expect(geroge).toMatchObject({
    display_name: "Geroge Delmas",
    identity_status: "ambiguous",
    personnel_category: "foreign_or_allied_military_personnel",
    commissioned_officer: true,
    allied_or_foreign_personnel: true,
    research_status: "needs_identity_review",
  });
  expect(geroge.name_variants).toContain("George Delmas (unconfirmed search alias)");
  expect(JSON.stringify(geroge)).toContain("GR 16 P 171027");
  expect(JSON.stringify(geroge)).toContain("171030");

  const jacques = profile("86a952a7-c08e-50b9-be06-fbcdb2af8f37");
  expect(jacques).toMatchObject({
    identity_status: "ambiguous",
    research_status: "requires_archival_review",
    allied_or_foreign_personnel: true,
  });
  expect(JSON.stringify(jacques)).toContain("GR 16 P 171046");
  expect(JSON.stringify(jacques)).toContain("GR 16 P 171050");
});

test("Batch 558 confirms Roland's spelling variant but rejects postwar occupation inference", () => {
  const roland = profile("69653221-4857-5c8c-b877-68097bcead96");
  expect(roland).toMatchObject({
    identity_status: "confirmed",
    personnel_category: "enlisted_army_personnel",
    commissioned_officer: false,
    research_status: "requires_archival_review",
  });
  expect(roland.name_variants).toContain("Roland C Delorme");
  expect(roland.immediate_pre_oss_affiliations).toEqual([]);
  expect(roland.last_civilian_pre_service).toEqual([]);
  expect(roland.other_pre_oss_affiliations).toEqual([]);
  expect(JSON.stringify(roland)).toContain("1946-02-05");
  expect(JSON.stringify(roland)).toContain("not published as a pre-OSS affiliation");
});

test("Batch 558 publishes only two qualified pre-service statuses", () => {
  const expectations = [
    ["d409388e-72ba-595e-bee2-173c04325fd3", "Student", "student", "1942-09-12"],
    ["051d687b-4485-5eab-ba91-d0ac0197ec27", "Metal filer, grinder, buffer or polisher", "unknown", "1942-10-02"],
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
  expect(JSON.stringify(profile("d409388e-72ba-595e-bee2-173c04325fd3"))).toContain(
    "104-10165-10141",
  );
});

test("Batch 558 leaves three name-only cases candidly unresolved", () => {
  for (const id of [
    "fa2378b2-c115-5a6a-8a15-32cbf486adc0",
    "63e591e1-56d2-585d-b73d-c7e6ca9ad462",
    "a60a5968-ca2d-59a1-b35c-65642f39b29d",
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

test("Batch 558 advances research and archival coverage without inventing employers", () => {
  expect(stats).toMatchObject({
    source_rows: 23978,
    person_entities: 23940,
    possible_duplicate_groups: 250,
    research_attempted_people: 5346,
    research_attempt_percent: 22.3308,
    verified_affiliation_people: 582,
    verified_affiliation_percent: 2.4311,
    verified_employer_people: 258,
    verified_employer_percent: 1.0777,
    archival_review_assessed_people: 5301,
    archival_review_percent: 22.1429,
    public_sources: 3570,
    published_claims: 4236,
  });
  expect(stats.research_status_counts).toMatchObject({
    needs_identity_review: 305,
    not_started: 18594,
    occupation_only_found: 989,
    requires_archival_review: 3165,
    verified_employer_found: 241,
  });
  expect(stats.identity_status_counts).toEqual({
    ambiguous: 261,
    confirmed: 1101,
    conflicting: 113,
    high_confidence: 729,
    probable: 172,
    unresolved: 21564,
  });
});

test("Batch 558 evidence package contains no exposed private identifier", () => {
  expect(evidence).not.toMatch(/serial_number(_raw|_normalized)?/);
  expect(evidence).not.toContain('"serial_number"');
  expect(evidence).not.toContain("NARA_API_KEY");
  expect(evidence).not.toContain("x-api-key");
});
