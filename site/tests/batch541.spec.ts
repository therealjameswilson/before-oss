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
    "../../research/evidence-page-one-hundred-and-eight-william-g-davis-through-camille-l-dawson-pathways_batch-541_2026-09-15.json",
    import.meta.url,
  ),
  "utf8",
);
const profile = (id: string) =>
  people.find((person: { person_id: string }) => person.person_id === id);

const cohort = [
  ["1ddcf644-e869-538f-ae7a-cb088254bda4", "William G Davis", "bdcd7913-726b-54f4-b274-242ee5339f4d", false],
  ["c2941d16-9308-5766-aadb-ffee0d90a3be", "William H Davis", "9e457c54-0fd0-5927-b631-42564f150b6b", false],
  ["f6899ec3-176a-573e-850c-a1db992ada6f", "William P Davis", "abc41d6d-463a-5d7f-a5c1-a399b5e75087", true],
  ["469fe136-c1a1-5767-857c-65ecfbfaa08c", "Walter P Davison", "c566d867-68d3-5464-8a8b-16b44ea6c453", true],
  ["e4203afa-2cd2-5ab6-9ef5-0a0e7ea7a00a", "Walter P Davison", "750bd0f8-3dcf-591d-9219-2b1ddc3c6e6d", true],
  ["53dcfba1-c3a4-5eee-84ee-c8bc58215d17", "Robert W Davy", "fe4ec42c-15be-5881-9ad0-2f3b494c30b9", true],
  ["e34c0c68-97b8-5815-9a44-8b7550b79708", "Carlos B Dawes", "b0e05ab2-52f3-5c6c-a81d-a5b91730d35f", false],
  ["86f7da9f-6ca1-555f-9a3d-f5a9ba9cbbe2", "Carlos B Dawes", "1ba77c7c-612f-5a5e-bbdf-b2a42e4b6832", true],
  ["d27f9b24-ed48-5637-bd17-8b9188f9d7bd", "Louise M Dawley", "ee2d0daa-8281-5c7d-97aa-297e91531fc9", false],
  ["bee798b2-4be1-56d9-824e-b8924092961b", "Camille L Dawson", "4cdf6ff1-3e11-5759-b97a-6be8bcf5aff6", false],
] as const;

test("Batch 541 preserves ten page 108 rows and masks five private fields", () => {
  for (const [id, name, sourceRecordId, hasPrivateIdentifier] of cohort) {
    const person = profile(id);
    expect(person).toMatchObject({ display_name: name });
    const sourceRecord = person.source_records.find(
      (record: { source_record_id: string }) => record.source_record_id === sourceRecordId,
    );
    expect(sourceRecord).toMatchObject({
      archive_location: "230/86/29/06",
      box: "172",
      pdf_page: 108,
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

test("Batch 541 confirms Robert W Davy and publishes occupation only", () => {
  const person = profile("53dcfba1-c3a4-5eee-84ee-c8bc58215d17");
  expect(person).toMatchObject({
    identity_status: "confirmed",
    personnel_category: "enlisted_army_personnel",
    commissioned_officer: false,
    research_status: "occupation_only_found",
    research_attempt_count: 4,
  });
  expect(person.archival_file).toMatchObject({ review_priority: "high" });
  expect(person.immediate_pre_oss_affiliations).toEqual([]);
  expect(person.last_civilian_pre_service).toEqual([]);
  expect(person.other_pre_oss_affiliations).toHaveLength(1);
  expect(person.other_pre_oss_affiliations[0]).toMatchObject({
    organization_id: null,
    occupation: "Purchasing agents and buyers, n. e. c.",
    relationship_type: "unknown",
    end_date: "1942-04-05",
    immediate_pre_oss: false,
    last_civilian_pre_service: false,
    temporal_basis: "strongly_date_bounded",
    identity_confidence: "confirmed",
    claim_confidence: "medium",
    publication_status: "publish_qualified",
  });
  expect(person.claims).toHaveLength(2);
  expect(person.claims.find((claim: { claim_type: string }) => claim.claim_type === "identity")).toMatchObject({
    claim_confidence: "confirmed",
    publication_status: "published",
  });
  expect(person.claims.find((claim: { claim_type: string }) => claim.claim_type === "occupation")).toMatchObject({
    evidence_excerpt: "0-91. Purchasing agents and buyers, n. e. c.",
    publication_status: "publish_qualified",
  });
  expect(person.next_action).toContain("no employer");
});

test("Batch 541 publishes Carlos B Dawes's dated Treasury assignment", () => {
  const person = profile("e34c0c68-97b8-5815-9a44-8b7550b79708");
  expect(person).toMatchObject({
    identity_status: "high_confidence",
    personnel_category: "commissioned_army_officer",
    commissioned_officer: true,
    research_status: "completed",
    research_attempt_count: 4,
    manual_review_required: true,
  });
  expect(person.archival_file).toMatchObject({ review_priority: "high" });
  expect(person.source_records[0]).toMatchObject({ rank_as_indexed: "Capt" });
  expect(person.immediate_pre_oss_affiliations).toEqual([]);
  expect(person.last_civilian_pre_service).toEqual([]);
  expect(person.other_pre_oss_affiliations).toHaveLength(1);
  expect(person.other_pre_oss_affiliations[0]).toMatchObject({
    canonical_organization: "United States Department of the Treasury",
    organization_name_as_found: "Treasury Department",
    role_title: "national-bank examiner",
    occupation: "bank examiner",
    relationship_type: "government_assignment",
    start_date: "1930-03-05",
    city: "Albany",
    state_or_region: "New York",
    immediate_pre_oss: false,
    last_civilian_pre_service: false,
    temporal_basis: "documented_prewar",
    identity_confidence: "high_confidence",
    claim_confidence: "high",
    publication_status: "published",
  });
  expect(person.claims).toHaveLength(2);
  expect(person.claims.every((claim: { claim_confidence: string }) => claim.claim_confidence === "high")).toBe(true);
  expect(person.next_action).toContain("not shown to be immediate");
});

test("Batch 541 keeps the second Carlos B Dawes separate and withholds the candidate", () => {
  const person = profile("86f7da9f-6ca1-555f-9a3d-f5a9ba9cbbe2");
  const ranked = profile("e34c0c68-97b8-5815-9a44-8b7550b79708");
  expect(person).toMatchObject({
    identity_status: "ambiguous",
    personnel_category: "unknown_or_indeterminate",
    commissioned_officer: null,
    research_status: "requires_archival_review",
    research_attempt_count: 4,
    manual_review_required: true,
  });
  expect(person.possible_duplicate_group).toBe(ranked.possible_duplicate_group);
  expect(person.archival_file).toMatchObject({ review_priority: "critical" });
  expect(person.immediate_pre_oss_affiliations).toEqual([]);
  expect(person.last_civilian_pre_service).toEqual([]);
  expect(person.other_pre_oss_affiliations).toEqual([]);
  expect(person.claims).toEqual([]);
  expect(person.next_action).toContain("before merging or assigning");
});

test("Batch 541 preserves both Walter P Davison rows as unresolved duplicates", () => {
  const first = profile("469fe136-c1a1-5767-857c-65ecfbfaa08c");
  const second = profile("e4203afa-2cd2-5ab6-9ef5-0a0e7ea7a00a");
  for (const person of [first, second]) {
    expect(person).toMatchObject({
      display_name: "Walter P Davison",
      identity_status: "ambiguous",
      research_status: "requires_archival_review",
      research_attempt_count: 4,
      manual_review_required: true,
    });
    expect(person.archival_file).toMatchObject({ review_priority: "critical" });
    expect(person.immediate_pre_oss_affiliations).toEqual([]);
    expect(person.last_civilian_pre_service).toEqual([]);
    expect(person.other_pre_oss_affiliations).toEqual([]);
    expect(person.claims).toEqual([]);
  }
  expect(first.person_id).not.toBe(second.person_id);
  expect(first.possible_duplicate_group).toBe(second.possible_duplicate_group);
  expect(first.source_records[0].serial_masked).not.toBe(second.source_records[0].serial_masked);
});

test("Batch 541 withholds the William P Davis Colonel candidate", () => {
  const person = profile("f6899ec3-176a-573e-850c-a1db992ada6f");
  expect(person).toMatchObject({
    identity_status: "ambiguous",
    personnel_category: "unknown_or_indeterminate",
    commissioned_officer: null,
    research_status: "requires_archival_review",
    research_attempt_count: 4,
    manual_review_required: true,
  });
  expect(person.archival_file).toMatchObject({ review_priority: "critical" });
  expect(person.immediate_pre_oss_affiliations).toEqual([]);
  expect(person.last_civilian_pre_service).toEqual([]);
  expect(person.other_pre_oss_affiliations).toEqual([]);
  expect(person.claims).toEqual([]);
  expect(person.next_action).toContain("test the Colonel candidate");
});

test("Batch 541 leaves four identities unresolved with archival guidance", () => {
  const unresolvedIds = [
    "1ddcf644-e869-538f-ae7a-cb088254bda4",
    "c2941d16-9308-5766-aadb-ffee0d90a3be",
    "d27f9b24-ed48-5637-bd17-8b9188f9d7bd",
    "bee798b2-4be1-56d9-824e-b8924092961b",
  ];
  for (const id of unresolvedIds) {
    const person = profile(id);
    expect(person).toMatchObject({
      identity_status: "unresolved",
      research_status: "no_reliable_result_after_protocol",
      research_attempt_count: 4,
    });
    expect(person.archival_file).toMatchObject({ review_priority: "critical" });
    expect(person.immediate_pre_oss_affiliations).toEqual([]);
    expect(person.last_civilian_pre_service).toEqual([]);
    expect(person.other_pre_oss_affiliations).toEqual([]);
    expect(person.claims).toEqual([]);
    expect(person.next_action).toContain("No reliable pre-OSS employer has yet been identified");
  }
});

test("Batch 541 advances attempt and affiliation coverage without inventing an employer", () => {
  expect(stats).toMatchObject({
    source_rows: 23978,
    person_entities: 23940,
    possible_duplicate_groups: 246,
    research_attempted_people: 5178,
    research_attempt_percent: 21.6291,
    verified_affiliation_people: 571,
    verified_affiliation_percent: 2.3851,
    verified_employer_people: 253,
    verified_employer_percent: 1.0568,
    archival_review_assessed_people: 5133,
    archival_review_percent: 21.4411,
    public_sources: 3454,
    published_claims: 4052,
  });
  expect(stats.research_status_counts).toMatchObject({
    completed: 145,
    conflicting_sources: 100,
    no_reliable_result_after_protocol: 170,
    not_started: 18762,
    occupation_only_found: 950,
    requires_archival_review: 3119,
  });
  expect(stats.identity_status_counts).toMatchObject({
    ambiguous: 243,
    confirmed: 1060,
    conflicting: 101,
    high_confidence: 710,
    unresolved: 21666,
  });
  expect(stats.commissioned_status_counts).toEqual({
    commissioned: 2273,
    not_commissioned: 5977,
    unknown: 15690,
  });
});

test("Batch 541 evidence is citation-linked and private-value free", () => {
  const bundle = JSON.parse(evidence);
  expect(bundle).toMatchObject({ bundle_version: "1.0" });
  expect(bundle.sources).toHaveLength(8);
  expect(bundle.organizations).toHaveLength(1);
  expect(bundle.affiliations).toHaveLength(2);
  expect(bundle.claims).toHaveLength(7);
  expect(bundle.claims.flatMap((claim: { sources: unknown[] }) => claim.sources)).toHaveLength(16);
  expect(bundle.person_updates).toHaveLength(10);
  expect(bundle.research_attempts).toHaveLength(10);
  expect(bundle.claims.filter((claim: { claim_confidence: string }) => claim.claim_confidence === "high")).toHaveLength(2);
  expect(bundle.claims.filter((claim: { claim_confidence: string }) => claim.claim_confidence === "low")).toHaveLength(3);
  expect(evidence).toContain("0-91. Purchasing agents and buyers, n. e. c.");
  expect(evidence).toContain("Treasury Department national-bank examiner");
  expect(evidence).toContain("was a Major with the Office of Strategic Services");
  expect(evidence).toContain("Five printed private values are withheld");
  expect(evidence).not.toMatch(/serial_number|service_number/);
});

test.describe("Batch 541 direct profile routes", () => {
  for (const [id, name] of cohort) {
    test(`${name} ${id.slice(0, 8)} renders from a direct route`, async ({ page }) => {
      await page.goto(`./people/${id}/`);
      await expect(page.locator("h1")).toContainText(name);
      await expect(page.locator("body")).toContainText("Box172");
      await expect(page.locator("body")).toContainText("Archival-review priority");
    });
  }
});
