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
    "../../research/evidence-page-one-hundred-and-seven-charlotte-m-davis-through-emiliy-c-davis-pathways_batch-535_2026-09-14.json",
    import.meta.url,
  ),
  "utf8",
);
const profile = (id: string) =>
  people.find((person: { person_id: string }) => person.person_id === id);

const cohort = [
  ["90c0b7de-0923-5936-a1ff-c6a5bf5e6b27", "Charlotte M Davis", "745e538f-5d52-5506-b841-d6559d171ee0", "169", false, 4],
  ["45f452c9-3575-5fbf-be86-a0460c6cc3be", "Cleveland Davis", "c4c2105d-e44e-5864-a53a-044505d91ce1", "169", false, 4],
  ["436b6ccd-6d7c-5da9-ae07-1fe2aaceb5de", "Cora J Davis", "409a0f59-7770-540f-9a9c-71be9d3d5504", "169", false, 4],
  ["39dda008-4d79-556c-acb5-4f4cafb32559", "Curtis C Davis", "e0549877-e447-5bab-bf8d-167d9c4ad1ba", "169", true, 4],
  ["a3c8ebf8-0301-51ad-ba31-9bf2ba001903", "David R Davis", "d37c4cb6-94d2-57f5-8735-85877faf735e", "169", false, 4],
  ["7491db37-9fd9-55dc-afe4-eca6400dba26", "David M Davis", "f80babe6-8470-5b63-bb14-224c3d509251", "169", true, 4],
  ["0cfb5b81-4fc7-5de2-9009-bf089b9b84e3", "Doris Davis", "522f7b3d-fa0a-5fc3-be19-5312363e14d1", "169", false, 3],
  ["f59cf82f-cb46-5018-85f0-4fdc01034ce5", "Dorothy Davis", "1b8bf629-0712-542d-9edb-2bc707c1308a", "169", false, 3],
  ["3d907752-6913-5b84-baef-cec3dc3aeb13", "Elizabeth T Davis", "bd0b8a13-cbc4-54d2-940a-f8abeac9b088", "169", false, 3],
  ["119caf16-01cd-5536-9fae-d740da6d47a8", "Emiliy C Davis", "61c6728e-59f9-5338-a04e-add8c39ff83a", "170", false, 3],
] as const;

test("Batch 535 preserves the printed spellings and masks both private fields", () => {
  for (const [id, name, sourceRecordId, box, hasPrivateIdentifier] of cohort) {
    const person = profile(id);
    expect(person).toMatchObject({ display_name: name });
    const sourceRecord = person.source_records.find(
      (record: { source_record_id: string }) => record.source_record_id === sourceRecordId,
    );
    expect(sourceRecord).toMatchObject({
      archive_location: "230/86/29/06",
      box,
      pdf_page: 107,
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
  expect(profile("119caf16-01cd-5536-9fae-d740da6d47a8").display_name).toBe("Emiliy C Davis");
});

test("Batch 535 confirms David M Davis without decoding undefined occupation value 944", () => {
  const person = profile("7491db37-9fd9-55dc-afe4-eca6400dba26");
  expect(person).toMatchObject({
    identity_status: "confirmed",
    personnel_category: "enlisted_army_personnel",
    commissioned_officer: false,
    research_status: "requires_archival_review",
    research_attempt_count: 4,
  });
  expect(person.archival_file).toMatchObject({ review_priority: "critical" });
  expect(person.immediate_pre_oss_affiliations).toEqual([]);
  expect(person.last_civilian_pre_service).toEqual([]);
  expect(person.other_pre_oss_affiliations).toEqual([]);
  expect(person.claims).toHaveLength(1);
  expect(person.claims[0]).toMatchObject({
    claim_type: "identity",
    claim_confidence: "confirmed",
    publication_status: "published",
  });
  expect(person.identity_evidence).toContain("but not 9-44");
  expect(person.next_action).toContain("no reliable pre-OSS occupation or employer");
});

test("Batch 535 leaves nine common-name identities unresolved without publishing candidates", () => {
  for (const [id, _name, _sourceRecordId, _box, _hasPrivateIdentifier, attemptCount] of cohort.filter(
    ([personId]) => personId !== "7491db37-9fd9-55dc-afe4-eca6400dba26",
  )) {
    const person = profile(id);
    expect(person).toMatchObject({
      identity_status: "unresolved",
      research_status: "no_reliable_result_after_protocol",
      research_attempt_count: attemptCount,
    });
    expect(person.archival_file).toMatchObject({ review_priority: "critical" });
    expect(person.immediate_pre_oss_affiliations).toEqual([]);
    expect(person.last_civilian_pre_service).toEqual([]);
    expect(person.other_pre_oss_affiliations).toEqual([]);
    expect(person.claims).toEqual([]);
    expect(person.next_action).toContain("No reliable pre-OSS employer has yet been identified");
  }
});

test("Batch 535 advances attempted and archival coverage without inflating employer coverage", () => {
  expect(stats).toMatchObject({
    source_rows: 23978,
    person_entities: 23940,
    research_attempted_people: 5118,
    research_attempt_percent: 21.3784,
    verified_affiliation_people: 569,
    verified_affiliation_percent: 2.3768,
    verified_employer_people: 253,
    verified_employer_percent: 1.0568,
    archival_review_assessed_people: 5073,
    archival_review_percent: 21.1905,
    published_claims: 4026,
    public_sources: 3429,
  });
  expect(stats.research_status_counts).toMatchObject({
    not_started: 18822,
    conflicting_sources: 97,
    no_reliable_result_after_protocol: 130,
    occupation_only_found: 942,
    documented_prewar_employer_found: 101,
    requires_archival_review: 3112,
  });
});

test("Batch 535 evidence is citation-linked, idempotent, and private-value free", () => {
  const bundle = JSON.parse(evidence);
  expect(bundle).toMatchObject({ bundle_version: "1.0" });
  expect(bundle.sources).toHaveLength(3);
  expect(bundle.organizations).toHaveLength(0);
  expect(bundle.affiliations).toHaveLength(0);
  expect(bundle.claims).toHaveLength(1);
  expect(bundle.claims[0].sources).toHaveLength(2);
  expect(bundle.person_updates).toHaveLength(10);
  expect(bundle.research_attempts).toHaveLength(10);
  expect(bundle.claims[0]).toMatchObject({ claim_type: "identity" });
  expect(evidence).toContain("does not define 9-44");
  expect(evidence).not.toMatch(/serial_number|service_number/);
});

test.describe("Batch 535 direct profile routes", () => {
  for (const [id, name, _sourceRecordId, box] of cohort) {
    test(`${name} ${id.slice(0, 8)} renders from a direct route`, async ({ page }) => {
      await page.goto(`./people/${id}/`);
      await expect(page.locator("h1")).toContainText(name);
      await expect(page.locator("body")).toContainText(`Box${box}`);
      await expect(page.locator("body")).toContainText("Archival-review priority");
    });
  }
});
