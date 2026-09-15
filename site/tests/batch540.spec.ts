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
    "../../research/evidence-page-one-hundred-and-eight-roger-f-davis-through-william-a-davis-pathways_batch-540_2026-09-15.json",
    import.meta.url,
  ),
  "utf8",
);
const profile = (id: string) =>
  people.find((person: { person_id: string }) => person.person_id === id);

const cohort = [
  ["ba7726dc-5511-5efc-829c-4368317635f1", "Roger F Davis", "4bfa16c7-3d9d-5a67-9950-b4bae46b781b", false, "172"],
  ["5873e471-617a-5e85-ab6a-de6fe1d17018", "Russell R Davis", "a113fcd2-ddaa-5851-93cf-fb6106b0fd6d", true, "172"],
  ["8cb806ca-a0dd-51af-a52f-8acdd0405027", "Rymond I Davis", "cc72ed38-b997-56f6-ad18-78129b114c1b", false, "171"],
  ["5119ce4f-bb2b-554f-a2bf-2ec89f70cafb", "Sidney A Davis", "384d0bef-70d8-56cd-b3bc-1c517a2efbcd", false, "172"],
  ["943c46f7-442d-5674-85f4-63da15f02c84", "Thomas J Davis Jr.", "a0751dc8-3bab-583d-b1c2-d3f9904e53bf", false, "172"],
  ["c330e602-554b-533b-b0bd-445332909f9e", "Walter W Davis", "cbed39a2-863f-5bd5-bf4a-5f5d7aaa9617", false, "172"],
  ["b2d24ff9-3111-5b62-a6dc-fd7dcbff1201", "Walter H Davis", "bf48e8e8-2911-5c1e-94cb-a9cc1b605f9f", true, "172"],
  ["5a86c87d-bb0f-5443-bc47-991328da2cb1", "Ward P Davis", "252bd8e1-c1f7-5b39-8852-77e79c23b790", false, "172"],
  ["3ac33317-3c87-590d-8bfd-97ec456a58f5", "Ward Davis", "3a6f8b0e-6684-503e-8675-1e29bf96bbe2", false, "172"],
  ["5edb4181-57e8-51b1-b3a7-462a1dee994a", "William A Davis", "c46573e4-7e0e-5d06-b7ed-4ea70f26d09d", false, "172"],
] as const;

test("Batch 540 preserves ten page 108 rows and masks two private fields", () => {
  for (const [id, name, sourceRecordId, hasPrivateIdentifier, box] of cohort) {
    const person = profile(id);
    expect(person).toMatchObject({ display_name: name });
    const sourceRecord = person.source_records.find(
      (record: { source_record_id: string }) => record.source_record_id === sourceRecordId,
    );
    expect(sourceRecord).toMatchObject({
      archive_location: "230/86/29/06",
      box,
      pdf_page: 108,
    });
    if (hasPrivateIdentifier) {
      expect(sourceRecord.serial_masked).toMatch(/^••••\d{4}$/);
    } else {
      expect(sourceRecord.serial_masked).toBeNull();
    }
    expect(JSON.stringify(person)).not.toMatch(
      /"serial_number"|"serial_number_raw"|"serial_number_normalized"/,
    );
  }
});

test("Batch 540 confirms Russell R Davis and publishes occupation only", () => {
  const person = profile("5873e471-617a-5e85-ab6a-de6fe1d17018");
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
    occupation: "Farm hands, general farms",
    relationship_type: "unknown",
    end_date: "1941-08-07",
    immediate_pre_oss: false,
    last_civilian_pre_service: false,
    temporal_basis: "strongly_date_bounded",
    identity_confidence: "confirmed",
    claim_confidence: "medium",
  });
  expect(person.claims).toHaveLength(2);
  expect(person.claims.find((claim: { claim_type: string }) => claim.claim_type === "identity")).toMatchObject({
    claim_confidence: "confirmed",
    publication_status: "published",
  });
  expect(person.claims.find((claim: { claim_type: string }) => claim.claim_type === "occupation")).toMatchObject({
    evidence_excerpt: "3-16. Farm hands, general farms",
    publication_status: "publish_qualified",
  });
  expect(person.next_action).toContain("no employer");
});

test("Batch 540 makes the Walter H Davis identifier conflict explicit", () => {
  const person = profile("b2d24ff9-3111-5b62-a6dc-fd7dcbff1201");
  expect(person).toMatchObject({
    identity_status: "conflicting",
    personnel_category: "unknown_or_indeterminate",
    commissioned_officer: null,
    research_status: "conflicting_sources",
    research_attempt_count: 4,
  });
  expect(person.archival_file).toMatchObject({ review_priority: "critical" });
  expect(person.immediate_pre_oss_affiliations).toEqual([]);
  expect(person.last_civilian_pre_service).toEqual([]);
  expect(person.other_pre_oss_affiliations).toEqual([]);
  expect(person.claims).toHaveLength(1);
  expect(person.claims[0]).toMatchObject({
    claim_type: "identity",
    claim_confidence: "conflicting",
    publication_status: "conflicting",
  });
  expect(person.identity_evidence).toContain("additional components");
  expect(person.next_action).toContain("resolve the private-identifier/name conflict");
});

test("Batch 540 publishes Ward P Davis's qualified naval pathway", () => {
  const person = profile("5a86c87d-bb0f-5443-bc47-991328da2cb1");
  expect(person).toMatchObject({
    identity_status: "high_confidence",
    personnel_category: "commissioned_naval_officer",
    commissioned_officer: true,
    research_status: "completed",
    research_attempt_count: 4,
    manual_review_required: true,
  });
  expect(person.possible_duplicate_group).toMatch(/^duplicate-/);
  expect(person.archival_file).toMatchObject({ review_priority: "high" });
  expect(person.last_civilian_pre_service).toEqual([]);
  expect(person.immediate_pre_oss_affiliations).toHaveLength(1);
  expect(person.immediate_pre_oss_affiliations[0]).toMatchObject({
    canonical_organization: "United States Navy",
    organization_name_as_found: "USS Raleigh (CL-7)",
    role_title: "Commanding officer",
    relationship_type: "military_assignment",
    end_date: "1943-04-14",
    immediate_pre_oss: true,
    temporal_basis: "probable_immediate",
    claim_confidence: "medium",
    publication_status: "publish_qualified",
  });
  expect(person.other_pre_oss_affiliations).toHaveLength(1);
  expect(person.other_pre_oss_affiliations[0]).toMatchObject({
    canonical_organization: "United States Navy",
    occupation: "career naval officer",
    relationship_type: "military_assignment",
    temporal_basis: "documented_prewar",
    claim_confidence: "high",
    publication_status: "published",
  });
  expect(person.claims).toHaveLength(3);
  expect(person.claims.filter((claim: { claim_confidence: string }) => claim.claim_confidence === "high")).toHaveLength(2);
  expect(person.claims.find((claim: { claim_type: string }) => claim.claim_type === "immediate_pre_oss_affiliation")).toMatchObject({
    claim_confidence: "medium",
    publication_status: "publish_qualified",
  });
});

test("Batch 540 keeps adjacent Ward Davis separate and withholds the candidate", () => {
  const person = profile("3ac33317-3c87-590d-8bfd-97ec456a58f5");
  const wardP = profile("5a86c87d-bb0f-5443-bc47-991328da2cb1");
  expect(person).toMatchObject({
    identity_status: "ambiguous",
    personnel_category: "unknown_or_indeterminate",
    commissioned_officer: null,
    research_status: "requires_archival_review",
    research_attempt_count: 4,
    manual_review_required: true,
  });
  expect(person.possible_duplicate_group).toBe(wardP.possible_duplicate_group);
  expect(person.archival_file).toMatchObject({ review_priority: "critical" });
  expect(person.immediate_pre_oss_affiliations).toEqual([]);
  expect(person.last_civilian_pre_service).toEqual([]);
  expect(person.other_pre_oss_affiliations).toEqual([]);
  expect(person.claims).toEqual([]);
  expect(person.next_action).toContain("do not assign the Navy pathway");
});

test("Batch 540 leaves six identities unresolved with index facts intact", () => {
  const unresolvedIds = new Set([
    "ba7726dc-5511-5efc-829c-4368317635f1",
    "8cb806ca-a0dd-51af-a52f-8acdd0405027",
    "5119ce4f-bb2b-554f-a2bf-2ec89f70cafb",
    "943c46f7-442d-5674-85f4-63da15f02c84",
    "c330e602-554b-533b-b0bd-445332909f9e",
    "5edb4181-57e8-51b1-b3a7-462a1dee994a",
  ]);
  for (const [id] of cohort.filter(([id]) => unresolvedIds.has(id))) {
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
  }
  expect(profile("943c46f7-442d-5674-85f4-63da15f02c84")).toMatchObject({
    personnel_category: "commissioned_army_officer",
    commissioned_officer: true,
  });
  expect(profile("8cb806ca-a0dd-51af-a52f-8acdd0405027").display_name).toBe("Rymond I Davis");
  expect(profile("8cb806ca-a0dd-51af-a52f-8acdd0405027").next_action).toContain("whether Rymond is the full spelling");
});

test("Batch 540 advances coverage while holding employer coverage constant", () => {
  expect(stats).toMatchObject({
    source_rows: 23978,
    person_entities: 23940,
    possible_duplicate_groups: 244,
    research_attempted_people: 5168,
    research_attempt_percent: 21.5873,
    verified_affiliation_people: 570,
    verified_affiliation_percent: 2.381,
    verified_employer_people: 253,
    verified_employer_percent: 1.0568,
    archival_review_assessed_people: 5123,
    archival_review_percent: 21.3993,
    public_sources: 3448,
    published_claims: 4048,
  });
  expect(stats.research_status_counts).toMatchObject({
    completed: 144,
    conflicting_sources: 100,
    no_reliable_result_after_protocol: 166,
    not_started: 18772,
    occupation_only_found: 949,
    requires_archival_review: 3115,
  });
  expect(stats.identity_status_counts).toMatchObject({
    ambiguous: 239,
    confirmed: 1059,
    conflicting: 101,
    high_confidence: 709,
    unresolved: 21672,
  });
  expect(stats.commissioned_status_counts).toEqual({
    commissioned: 2273,
    not_commissioned: 5976,
    unknown: 15691,
  });
});

test("Batch 540 evidence is citation-linked and private-value free", () => {
  const bundle = JSON.parse(evidence);
  expect(bundle).toMatchObject({ bundle_version: "1.0" });
  expect(bundle.sources).toHaveLength(7);
  expect(bundle.organizations).toHaveLength(1);
  expect(bundle.affiliations).toHaveLength(3);
  expect(bundle.claims).toHaveLength(7);
  expect(bundle.claims.flatMap((claim: { sources: unknown[] }) => claim.sources)).toHaveLength(15);
  expect(bundle.person_updates).toHaveLength(10);
  expect(bundle.research_attempts).toHaveLength(10);
  expect(bundle.claims.filter((claim: { claim_confidence: string }) => claim.claim_confidence === "high")).toHaveLength(2);
  expect(bundle.claims.filter((claim: { claim_confidence: string }) => claim.claim_confidence === "conflicting")).toHaveLength(1);
  expect(evidence).toContain("3-16. Farm hands, general farms");
  expect(evidence).toContain("CAPT Ward Davis (USN), chief of OSS Naval Command");
  expect(evidence).toContain("Ward Percival Davis");
  expect(evidence).toContain("USS Raleigh (CL-7)");
  expect(evidence).not.toMatch(/serial_number|service_number/);
});

test.describe("Batch 540 direct profile routes", () => {
  for (const [id, name, , , box] of cohort) {
    test(`${name} ${id.slice(0, 8)} renders from a direct route`, async ({ page }) => {
      await page.goto(`./people/${id}/`);
      await expect(page.locator("h1")).toContainText(name);
      await expect(page.locator("body")).toContainText(`Box${box}`);
      await expect(page.locator("body")).toContainText("Archival-review priority");
    });
  }
});
