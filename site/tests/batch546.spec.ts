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
    "../../research/evidence-page-one-hundred-and-nine-john-f-debardeleben-through-louis-d-debottari-pathways_batch-546_2026-09-15.json",
    import.meta.url,
  ),
  "utf8",
);
const profile = (id: string) =>
  people.find((person: { person_id: string }) => person.person_id === id);

const cohort = [
  ["37670ef7-e40d-5695-b70c-cafeb134072b", "John F Debardeleben", "0c5685b1-a18e-524f-be2e-b17d7898525e", false],
  ["6df9e322-b3ca-5157-b3b6-c1ecdf0f4c7d", "Sidney A Debarthy", "c223d21b-c03d-5564-8288-1170b599bbef", true],
  ["7b5f0fed-5fc3-588a-bc8d-421eb05546dd", "Hans N Debecker", "1b532bfa-356a-5e6d-ab3a-cc0b502d440c", true],
  ["cbd86278-876b-5575-b199-7af4422a8c77", "Frederick S Debeer Jr.", "01121c5a-ff22-504b-87da-8b978e2326f6", true],
  ["6579195b-415b-5620-b057-b402d33b3a94", "Fritz Debeer", "1cd80af7-4df2-5cfd-967a-e54004c7c21b", false],
  ["31641063-ef97-525a-a73f-cb13c77087b8", "Eugene V DeBell", "0d23c072-6944-5e07-b484-0c77aa518d9f", true],
  ["d3d00834-1172-509f-8e5a-0106efbe3e0c", "Larry V DeBell", "3a7c5d60-707e-510e-91e0-df34612cd7f0", true],
  ["2aa2a81a-9bd0-5c73-9413-a867662cd2b7", "Rene Debia", "7f4481f5-745c-598e-b6dd-c9c8e8ac9db3", false],
  ["bb48fc36-80fd-54c5-9c4e-9e00c945ec78", "* DeBlasi", "6cc3f108-2ffa-5643-8186-a7bb48bdd9ed", false],
  ["032502ea-0a5f-5d8f-9e5d-dbbad2589759", "Louis D DeBottari", "928e1beb-13ba-5af5-9bad-c7217d275a61", false],
] as const;

test("Batch 546 preserves ten page-109 Box 175 rows and masks five private fields", () => {
  for (const [id, name, sourceRecordId, hasPrivateIdentifier] of cohort) {
    const person = profile(id);
    expect(person).toMatchObject({ display_name: name });
    const sourceRecord = person.source_records.find(
      (record: { source_record_id: string }) => record.source_record_id === sourceRecordId,
    );
    expect(sourceRecord).toMatchObject({
      archive_location: "230/86/29/06",
      box: "175",
      pdf_page: 109,
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

test("Batch 546 publishes John DeBardeleben's FCC pathway without calling it immediate", () => {
  const person = profile("37670ef7-e40d-5695-b70c-cafeb134072b");
  expect(person).toMatchObject({
    identity_status: "high_confidence",
    research_status: "requires_archival_review",
    research_attempt_count: 5,
    manual_review_required: true,
  });
  expect(person.immediate_pre_oss_affiliations).toEqual([]);
  expect(person.last_civilian_pre_service).toEqual([]);
  expect(person.other_pre_oss_affiliations).toHaveLength(2);
  expect(person.other_pre_oss_affiliations[0]).toMatchObject({
    relationship_type: "government_assignment",
    temporal_basis: "documented_prewar",
    identity_confidence: "high_confidence",
    claim_confidence: "high",
    publication_status: "published",
  });
  expect(JSON.stringify(person)).toContain("Radio Intelligence Division");
  expect(JSON.stringify(person)).toContain("SS Bessemer City");
  expect(person.next_action).toContain("no source establishes the immediate pre-OSS affiliation");
});

test("Batch 546 keeps all four strict Army identifier conflicts unresolved", () => {
  for (const id of [
    "7b5f0fed-5fc3-588a-bc8d-421eb05546dd",
    "cbd86278-876b-5575-b199-7af4422a8c77",
    "31641063-ef97-525a-a73f-cb13c77087b8",
    "d3d00834-1172-509f-8e5a-0106efbe3e0c",
  ]) {
    const person = profile(id);
    expect(person).toMatchObject({
      identity_status: "conflicting",
      research_status: "conflicting_sources",
      research_attempt_count: 5,
      manual_review_required: true,
    });
    expect(person.archival_file).toMatchObject({ review_priority: "critical" });
    expect(person.immediate_pre_oss_affiliations).toEqual([]);
    expect(person.last_civilian_pre_service).toEqual([]);
    expect(person.other_pre_oss_affiliations).toEqual([]);
    expect(person.claims).toHaveLength(1);
    expect(person.claims[0]).toMatchObject({
      claim_confidence: "conflicting",
      publication_status: "conflicting",
    });
    expect(JSON.stringify(person)).toContain("different surname");
  }
});

test("Batch 546 links the two deBeer rows only as a possible duplicate", () => {
  const frederick = profile("cbd86278-876b-5575-b199-7af4422a8c77");
  const fritz = profile("6579195b-415b-5620-b057-b402d33b3a94");
  expect(frederick.possible_duplicate_group).toMatch(/^duplicate-/);
  expect(fritz.possible_duplicate_group).toBe(frederick.possible_duplicate_group);
  expect(frederick.identity_status).toBe("conflicting");
  expect(fritz).toMatchObject({
    identity_status: "probable",
    research_status: "requires_archival_review",
    research_attempt_count: 5,
  });
  expect(fritz.immediate_pre_oss_affiliations).toEqual([]);
  expect(fritz.last_civilian_pre_service).toEqual([]);
  expect(fritz.other_pre_oss_affiliations).toEqual([]);
  expect(JSON.stringify(fritz)).toContain("FREDERICK S. (FRITZ) deBEER JR.");
  expect(fritz.next_action).toContain("Preserve both source rows");
});

test("Batch 546 identifies Rene Debia while qualifying every government post", () => {
  const person = profile("2aa2a81a-9bd0-5c73-9413-a867662cd2b7");
  expect(person).toMatchObject({
    identity_status: "high_confidence",
    personnel_category: "foreign_or_allied_military_personnel",
    commissioned_officer: true,
    allied_or_foreign_personnel: true,
    research_status: "requires_archival_review",
    research_attempt_count: 5,
  });
  expect(person.source_records[0]).toMatchObject({
    rank_as_indexed: "Lt",
    notes_as_indexed: "French",
  });
  expect(person.immediate_pre_oss_affiliations).toEqual([]);
  expect(person.last_civilian_pre_service).toEqual([]);
  expect(person.other_pre_oss_affiliations).toHaveLength(3);
  expect(person.other_pre_oss_affiliations.every(
    (affiliation: { relationship_type: string; claim_confidence: string }) =>
      affiliation.relationship_type === "government_assignment" &&
      affiliation.claim_confidence === "medium",
  )).toBe(true);
  expect(person.other_pre_oss_affiliations.map(
    (affiliation: { temporal_basis: string }) => affiliation.temporal_basis,
  )).toEqual(["documented_prewar", "documented_prewar", "temporal_relation_uncertain"]);
  expect(person.name_variants).toContain("René Marie Albert Yves Débia");
  expect(JSON.stringify(person)).toContain("GR 16 P 161919");
});

test("Batch 546 publishes Louis DeBottari's RCA employment as documented prewar only", () => {
  const person = profile("032502ea-0a5f-5d8f-9e5d-dbbad2589759");
  expect(person).toMatchObject({
    identity_status: "high_confidence",
    research_status: "documented_prewar_employer_found",
    research_attempt_count: 5,
    manual_review_required: true,
  });
  expect(person.immediate_pre_oss_affiliations).toEqual([]);
  expect(person.last_civilian_pre_service).toEqual([]);
  expect(person.other_pre_oss_affiliations).toHaveLength(1);
  expect(person.other_pre_oss_affiliations[0]).toMatchObject({
    canonical_organization: "RCA Communications, Inc.",
    relationship_type: "employment",
    start_date: "1939",
    temporal_basis: "documented_prewar",
    identity_confidence: "high_confidence",
    claim_confidence: "high",
    publication_status: "published",
  });
  expect(person.next_action).toContain("whether RCA was the immediate pre-OSS affiliation");
});

test("Batch 546 preserves dignified unresolved Sidney Debarthy and incomplete DeBlasi profiles", () => {
  const sidney = profile("6df9e322-b3ca-5157-b3b6-c1ecdf0f4c7d");
  expect(sidney).toMatchObject({
    identity_status: "unresolved",
    research_status: "no_reliable_result_after_protocol",
    research_attempt_count: 5,
  });
  expect(sidney.claims).toEqual([]);
  expect(sidney.next_action).toContain("No reliable pre-OSS employer has yet been identified");

  const deblasi = profile("bb48fc36-80fd-54c5-9c4e-9e00c945ec78");
  expect(deblasi).toMatchObject({
    display_name: "* DeBlasi",
    identity_status: "unresolved",
    research_status: "requires_archival_review",
    research_attempt_count: 5,
  });
  expect(deblasi.source_records[0].notes_as_indexed).toBe("see file o");
  expect(deblasi.archival_file).toMatchObject({ review_priority: "critical" });
  expect(deblasi.claims).toEqual([]);
  expect(deblasi.next_action).toContain("before any person-level research or merge");
});

test("Batch 546 advances research, employer, affiliation, officer, and archival coverage exactly", () => {
  expect(stats).toMatchObject({
    source_rows: 23978,
    person_entities: 23940,
    possible_duplicate_groups: 248,
    research_attempted_people: 5228,
    research_attempt_percent: 21.8379,
    verified_affiliation_people: 573,
    verified_affiliation_percent: 2.3935,
    verified_employer_people: 254,
    verified_employer_percent: 1.061,
    archival_review_assessed_people: 5183,
    archival_review_percent: 21.65,
    public_sources: 3489,
    published_claims: 4102,
  });
  expect(stats.research_status_counts).toMatchObject({
    conflicting_sources: 108,
    documented_prewar_employer_found: 104,
    no_reliable_result_after_protocol: 187,
    not_started: 18712,
    requires_archival_review: 3134,
  });
  expect(stats.identity_status_counts).toMatchObject({
    ambiguous: 246,
    confirmed: 1068,
    conflicting: 108,
    high_confidence: 716,
    probable: 163,
    unresolved: 21639,
  });
  expect(stats.commissioned_status_counts).toEqual({
    commissioned: 2274,
    not_commissioned: 5981,
    unknown: 15685,
  });
});

test("Batch 546 evidence is citation-linked, uncertainty-preserving, and private-value free", () => {
  const bundle = JSON.parse(evidence);
  expect(bundle).toMatchObject({ bundle_version: "1.0" });
  expect(bundle.sources).toHaveLength(10);
  expect(bundle.organizations).toHaveLength(4);
  expect(bundle.affiliations).toHaveLength(6);
  expect(bundle.claims).toHaveLength(14);
  expect(bundle.claims.flatMap((claim: { sources: unknown[] }) => claim.sources)).toHaveLength(32);
  expect(bundle.person_updates).toHaveLength(10);
  expect(bundle.research_attempts).toHaveLength(10);
  expect(bundle.claims.filter((claim: { claim_confidence: string }) => claim.claim_confidence === "high")).toHaveLength(5);
  expect(bundle.claims.filter((claim: { claim_confidence: string }) => claim.claim_confidence === "medium")).toHaveLength(5);
  expect(bundle.claims.filter((claim: { claim_confidence: string }) => claim.claim_confidence === "conflicting")).toHaveLength(4);
  expect(evidence).toContain("No reliable pre-OSS employer has yet been identified");
  expect(evidence).toContain("unrelated identity");
  expect(evidence).not.toMatch(/serial_number|service_number|matched_name/);
});

test("Batch 546 gives every published or conflicting claim an inspectable citation", () => {
  for (const [id] of cohort) {
    const person = profile(id);
    for (const claim of person.claims) {
      expect(claim.sources.length).toBeGreaterThan(0);
      expect(claim.sources.every(
        (link: { source: { stable_url: string } }) => Boolean(link.source.stable_url),
      )).toBe(true);
    }
  }
});

test.describe("Batch 546 direct profile routes", () => {
  for (const [id, name] of cohort) {
    test(`${name} ${id.slice(0, 8)} renders from a direct route`, async ({ page }) => {
      await page.goto(`./people/${id}/`);
      await expect(page.locator("h1")).toContainText(name);
      await expect(page.locator("body")).toContainText("Box175");
      await expect(page.locator("body")).toContainText("Archival-review priority");
    });
  }
});
