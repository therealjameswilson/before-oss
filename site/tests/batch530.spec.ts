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
    "../../research/evidence-page-one-hundred-and-six-charles-datcher-through-may-j-dausch-pathways_batch-530_2026-09-14.json",
    import.meta.url,
  ),
  "utf8",
);
const profile = (id: string) =>
  people.find((person: { person_id: string }) => person.person_id === id);

const cohort = [
  ["b0a55cdd-367b-5d0d-8846-b6c208b5b949", "Charles Datcher", "332631d5-bec8-5549-90fd-e1d8e66eef7c", false],
  ["210b979e-6192-5d6e-8da6-898ced0be616", "Dominick Dattoma", "4ce09fc0-80b2-567a-9240-ca41d317b274", true],
  ["4b8aa126-5744-5c9a-8dab-cc61f72e0980", "Joseph A Daudelin", "e1a964db-c67f-5a56-b79e-7d8c43f288e3", true],
  ["8daab9c0-82b0-5876-9469-9a9ca013c4ba", "Joseph H Daugherty", "5bc54430-4e08-5e3a-baa7-c9ea5ad04678", true],
  ["7916a304-2da6-55a0-9d1b-38355bc3a66c", "Thomas J Daughtry", "baf193c7-932d-55dd-90a1-e54170b03f00", true],
  ["ced5c64a-e427-5412-bc0e-0edfb07599a4", "* Daulne", "6d44bccf-cf47-5fde-88e3-0161c5aa65f7", false],
  ["9d767353-1b5c-5c54-bbd2-501643a71403", "Frances L Dauphin", "6ae85205-bf21-5b5c-85f8-3fdfec9a076e", false],
  ["7bed825d-dd78-51a9-b85c-2457bee7848b", "Joseph H Dauphin", "3d9b750d-bd0b-54e6-807f-59050da20c44", true],
  ["a6eeb3c7-fc11-50a0-a483-80d2b4ceb6d5", "Edmund D'Auriol", "e853ade4-bbdc-5479-9a30-3e4b6ddaec2e", false],
  ["e656113e-dd73-528b-a55e-235042d162fc", "May J Dausch", "a31d5155-9f55-5264-8912-3115c18fb800", false],
] as const;

test("Batch 530 preserves page 106 rows 6-15 and masks every private field", () => {
  for (const [id, name, sourceRecordId, hasPrivateIdentifier] of cohort) {
    const person = profile(id);
    expect(person).toMatchObject({ display_name: name });
    const sourceRecord = person.source_records.find(
      (record: { source_record_id: string }) => record.source_record_id === sourceRecordId,
    );
    expect(sourceRecord).toMatchObject({
      archive_location: "230/86/29/05",
      box: "168",
      pdf_page: 106,
    });
    if (hasPrivateIdentifier) {
      expect(sourceRecord.serial_masked).toMatch(/^••••\d{2,4}$/);
    } else {
      expect(sourceRecord.serial_masked).toBeNull();
    }
    expect(JSON.stringify(person)).not.toMatch(
      /"serial_number"|"serial_number_raw"|"serial_number_normalized"/,
    );
  }
});

test("Batch 530 preserves Daulne's incomplete printed fields without expanding them", () => {
  const daulne = profile("ced5c64a-e427-5412-bc0e-0edfb07599a4");
  expect(daulne).toMatchObject({
    display_name: "* Daulne",
    identity_status: "unresolved",
    personnel_category: "unknown_or_indeterminate",
    commissioned_officer: null,
  });
  expect(daulne.source_records[0]).toMatchObject({
    indexed_first_name: "*",
    rank_as_indexed: "Cdt",
    notes_as_indexed: "aka Jea",
  });
  expect(daulne.identity_evidence).toContain("not expanded");
  expect(daulne.name_variants).not.toContain("Jean Daulne");
});

test("Batch 530 publishes three exact Army matches as occupations, not employers", () => {
  const expected = [
    ["4b8aa126-5744-5c9a-8dab-cc61f72e0980", "Shipping and receiving clerks", "1943-09-11"],
    ["8daab9c0-82b0-5876-9469-9a9ca013c4ba", "Salespersons", "1943-09-25"],
    ["7bed825d-dd78-51a9-b85c-2457bee7848b", "Brakemen, railroad", "1942-03-10"],
  ] as const;
  for (const [id, occupation, endDate] of expected) {
    const person = profile(id);
    expect(person).toMatchObject({
      identity_status: "confirmed",
      personnel_category: "enlisted_army_personnel",
      commissioned_officer: false,
      research_status: "occupation_only_found",
      research_attempt_count: 3,
    });
    expect(person.immediate_pre_oss_affiliations).toEqual([]);
    expect(person.last_civilian_pre_service).toEqual([]);
    expect(person.other_pre_oss_affiliations).toHaveLength(1);
    expect(person.other_pre_oss_affiliations[0]).toMatchObject({
      canonical_organization: null,
      occupation,
      end_date: endDate,
      relationship_type: "unknown",
      temporal_basis: "strongly_date_bounded",
      identity_confidence: "confirmed",
      claim_confidence: "medium",
      publication_status: "publish_qualified",
    });
  }
});

test("Batch 530 confirms Dattoma while withholding the undefined occupation code", () => {
  const dominick = profile("210b979e-6192-5d6e-8da6-898ced0be616");
  expect(dominick).toMatchObject({
    identity_status: "confirmed",
    personnel_category: "enlisted_army_personnel",
    commissioned_officer: false,
    research_status: "requires_archival_review",
    research_attempt_count: 3,
  });
  expect(dominick.immediate_pre_oss_affiliations).toEqual([]);
  expect(dominick.last_civilian_pre_service).toEqual([]);
  expect(dominick.other_pre_oss_affiliations).toEqual([]);
  expect(dominick.claims).toHaveLength(1);
  expect(dominick.claims[0]).toMatchObject({
    claim_type: "identity",
    claim_confidence: "confirmed",
  });
  expect(dominick.identity_evidence).toContain("not interpreted");
  expect(JSON.stringify(dominick)).not.toContain("Apprentice");
});

test("Batch 530 leaves six unsupported identities visibly unresolved", () => {
  const ids = [
    "b0a55cdd-367b-5d0d-8846-b6c208b5b949",
    "7916a304-2da6-55a0-9d1b-38355bc3a66c",
    "ced5c64a-e427-5412-bc0e-0edfb07599a4",
    "9d767353-1b5c-5c54-bbd2-501643a71403",
    "a6eeb3c7-fc11-50a0-a483-80d2b4ceb6d5",
    "e656113e-dd73-528b-a55e-235042d162fc",
  ];
  for (const id of ids) {
    const person = profile(id);
    expect(person).toMatchObject({
      identity_status: "unresolved",
      research_status: "no_reliable_result_after_protocol",
      research_attempt_count: 3,
    });
    expect(person.immediate_pre_oss_affiliations).toEqual([]);
    expect(person.last_civilian_pre_service).toEqual([]);
    expect(person.other_pre_oss_affiliations).toEqual([]);
    expect(person.claims).toEqual([]);
    expect(person.next_action).toContain("No reliable pre-OSS employer has yet been identified");
  }
  expect(profile("a6eeb3c7-fc11-50a0-a483-80d2b4ceb6d5").identity_evidence).toContain(
    "postwar Edmund A. D'Auriol",
  );
  expect(profile("7916a304-2da6-55a0-9d1b-38355bc3a66c").identity_evidence).toContain(
    "name alone",
  );
});

test("Batch 530 advances attempted and archival coverage with reproducible totals", () => {
  expect(stats).toMatchObject({
    source_rows: 23978,
    person_entities: 23940,
    research_attempted_people: 5068,
    research_attempt_percent: 21.1696,
    verified_affiliation_people: 569,
    verified_affiliation_percent: 2.3768,
    verified_employer_people: 253,
    verified_employer_percent: 1.0568,
    archival_review_assessed_people: 5023,
    archival_review_percent: 20.9816,
    published_claims: 4000,
    public_sources: 3414,
  });
  expect(stats.research_status_counts).toMatchObject({
    not_started: 18872,
    no_reliable_result_after_protocol: 100,
    occupation_only_found: 930,
    documented_prewar_employer_found: 101,
    requires_archival_review: 3107,
  });
});

test("Batch 530 evidence is complete, citation-linked, and private-value free", () => {
  const bundle = JSON.parse(evidence);
  expect(bundle).toMatchObject({ bundle_version: "1.0" });
  expect(bundle.sources).toHaveLength(3);
  expect(bundle.organizations).toHaveLength(0);
  expect(bundle.affiliations).toHaveLength(3);
  expect(bundle.claims).toHaveLength(7);
  expect(bundle.claims.reduce(
    (sum: number, claim: { sources: unknown[] }) => sum + claim.sources.length,
    0,
  )).toBe(14);
  expect(bundle.person_updates).toHaveLength(10);
  expect(bundle.research_attempts).toHaveLength(10);
  expect(bundle.claims.filter(
    (claim: { claim_type: string }) => claim.claim_type === "last_civilian_pre_service",
  )).toHaveLength(0);
  expect(bundle.claims.filter(
    (claim: { claim_type: string }) => claim.claim_type === "occupation",
  )).toHaveLength(3);
  expect(evidence).not.toMatch(/serial_number|service_number/);
});

test.describe("Batch 530 direct profile routes", () => {
  for (const [id, name] of cohort) {
    test(`${name} renders from a direct route`, async ({ page }) => {
      await page.goto(`./people/${id}/`);
      await expect(page.locator("h1")).toContainText(name);
      await expect(page.locator("body")).toContainText("Box168");
      await expect(page.locator("body")).toContainText("Archival-review priority");
    });
  }
});
