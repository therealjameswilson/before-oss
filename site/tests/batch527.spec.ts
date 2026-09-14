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
    "../../research/evidence-page-one-hundred-and-five-joseph-a-dann-through-f-a-daprix-pathways_batch-527_2026-09-14.json",
    import.meta.url,
  ),
  "utf8",
);
const profile = (id: string) =>
  people.find((person: { person_id: string }) => person.person_id === id);

const cohort = [
  ["3275a0c2-9fbf-54a7-9b6a-2e19fd9f9f8e", "Joseph A Dann", "1a511765-7922-5615-b3b1-e7885c499f93", "166", true],
  ["fa6a5f45-9ec4-57b6-9d76-118c8ccd8774", "Alice Dannenberg", "2504ada0-8c1a-5575-83b0-5193e51bf44d", "166", false],
  ["84729312-da52-5214-9ddd-350f7b492aa8", "John A Danner", "87655878-18b0-59b5-afb1-ad38fecbabe1", "166", true],
  ["813e0130-73a3-5bb9-beaa-5c1e585f8346", "Gerald A Danni", "ad59bf54-d557-5823-bb9c-561cf5f5662b", "166", true],
  ["2a912191-078b-5900-a818-38f74d41c556", "Nicholas J D'Annunzio", "e5c99817-049d-5873-ad2f-82b639c2d2bc", "167", true],
  ["c681ba92-cfe7-5253-982a-e5fc5c1186bc", "Anna M Danovsky", "cc443049-9d29-5cdc-bbbe-63a88507e4f4", "167", true],
  ["ce859bd0-f8c0-5ef0-bf66-1eb19aaa52da", "Claude E Dansey", "da66aafa-26d3-5048-a79d-04e8fd9fc47f", "167", false],
  ["afd7eabc-53f0-5b35-b600-f10b4e185bee", "Ebert W D'Anton", "271f7819-8c8a-5e96-be2a-b87e95e85dd0", "167", true],
  ["bd01251f-5b08-57fe-a985-7e58b8af8a93", "Rene J Daon", "fe63881a-9ac9-5867-b37b-fe31ed1ce45e", "167", false],
  ["941532c9-9b39-5856-bbff-7665c0219eb5", "F A D'Aprix", "659da837-9f08-50c1-825a-61f3de037188", "167", false],
] as const;

test("Batch 527 preserves ten printed rows across Boxes 166-167 and masks private fields", () => {
  for (const [id, name, sourceRecordId, box, hasPrivateIdentifier] of cohort) {
    const person = profile(id);
    expect(person).toMatchObject({ display_name: name });
    const sourceRecord = person.source_records.find(
      (record: { source_record_id: string }) => record.source_record_id === sourceRecordId,
    );
    expect(sourceRecord).toMatchObject({ archive_location: "230/86/29/05", box, pdf_page: 105 });
    if (hasPrivateIdentifier) {
      expect(sourceRecord.serial_masked).toMatch(/^••••\d{2,4}$/);
    } else {
      expect(sourceRecord.serial_masked).toBeNull();
    }
    expect(JSON.stringify(person)).not.toMatch(
      /"serial_number"|"serial_number_raw"|"serial_number_normalized"/,
    );
  }
  expect(profile("ce859bd0-f8c0-5ef0-bf66-1eb19aaa52da").source_records[0]).toMatchObject({
    notes_as_indexed: "British A",
    rank_as_indexed: "Lt Col",
  });
});

test("Batch 527 separates Alice Dannenberg's COI affiliation and last civilian employer", () => {
  const alice = profile("fa6a5f45-9ec4-57b6-9d76-118c8ccd8774");
  expect(alice).toMatchObject({
    identity_status: "high_confidence",
    personnel_category: "civilian_professional_or_administrative_grade",
    commissioned_officer: false,
    research_status: "verified_employer_found",
    research_attempt_count: 3,
  });
  expect(alice.immediate_pre_oss_affiliations).toHaveLength(1);
  expect(alice.immediate_pre_oss_affiliations[0]).toMatchObject({
    canonical_organization: "Office of the Coordinator of Information",
    relationship_type: "government_assignment",
    temporal_basis: "strongly_date_bounded",
    claim_confidence: "high",
  });
  expect(alice.last_civilian_pre_service).toHaveLength(1);
  expect(alice.last_civilian_pre_service[0]).toMatchObject({
    canonical_organization: "Columbia Broadcasting System",
    relationship_type: "employment",
    temporal_basis: "explicit_immediate",
    claim_confidence: "high",
  });
  expect(alice.other_pre_oss_affiliations).toEqual([]);
  expect(alice.claims).toHaveLength(3);
});

test("Batch 527 publishes four qualified entry-time status findings without employers", () => {
  const expected = [
    ["3275a0c2-9fbf-54a7-9b6a-2e19fd9f9f8e", "confirmed", "Radio operators"],
    ["813e0130-73a3-5bb9-beaa-5c1e585f8346", "confirmed", "Repairmen and mechanics, n.e.c."],
    ["2a912191-078b-5900-a818-38f74d41c556", "confirmed", "Tailors and tailoresses"],
    ["afd7eabc-53f0-5b35-b600-f10b4e185bee", "high_confidence", "Student"],
  ] as const;
  for (const [id, identityStatus, occupation] of expected) {
    const person = profile(id);
    expect(person).toMatchObject({
      identity_status: identityStatus,
      personnel_category: "enlisted_army_personnel",
      commissioned_officer: false,
      research_status: "occupation_only_found",
      research_attempt_count: 3,
    });
    expect(person.immediate_pre_oss_affiliations).toEqual([]);
    expect(person.last_civilian_pre_service).toEqual([]);
    expect(person.other_pre_oss_affiliations).toHaveLength(1);
    expect(person.other_pre_oss_affiliations[0]).toMatchObject({ occupation, claim_confidence: "medium" });
  }
});

test("Batch 527 qualifies Claude Dansey's Allied assignment without labeling SIS as OSS", () => {
  const claude = profile("ce859bd0-f8c0-5ef0-bf66-1eb19aaa52da");
  expect(claude).toMatchObject({
    identity_status: "high_confidence",
    personnel_category: "foreign_or_allied_military_personnel",
    commissioned_officer: true,
    allied_or_foreign_personnel: true,
    research_status: "occupation_only_found",
    research_attempt_count: 3,
  });
  expect(claude.immediate_pre_oss_affiliations).toEqual([]);
  expect(claude.last_civilian_pre_service).toEqual([]);
  expect(claude.other_pre_oss_affiliations).toHaveLength(1);
  expect(claude.other_pre_oss_affiliations[0]).toMatchObject({
    canonical_organization: "Secret Intelligence Service",
    relationship_type: "government_assignment",
    temporal_basis: "temporal_relation_uncertain",
    claim_confidence: "high",
  });
});

test("Batch 527 keeps four unsupported identities visibly ambiguous or unresolved", () => {
  const expected = [
    ["84729312-da52-5214-9ddd-350f7b492aa8", "unresolved", "no_reliable_result_after_protocol", 3],
    ["c681ba92-cfe7-5253-982a-e5fc5c1186bc", "ambiguous", "needs_identity_review", 3],
    ["bd01251f-5b08-57fe-a985-7e58b8af8a93", "unresolved", "no_reliable_result_after_protocol", 4],
    ["941532c9-9b39-5856-bbff-7665c0219eb5", "ambiguous", "needs_identity_review", 4],
  ] as const;
  for (const [id, identityStatus, researchStatus, attemptCount] of expected) {
    const person = profile(id);
    expect(person).toMatchObject({
      identity_status: identityStatus,
      research_status: researchStatus,
      research_attempt_count: attemptCount,
    });
    expect(person.immediate_pre_oss_affiliations).toEqual([]);
    expect(person.last_civilian_pre_service).toEqual([]);
    expect(person.other_pre_oss_affiliations).toEqual([]);
    expect(person.claims).toEqual([]);
    expect(person.next_action).toContain("No reliable pre-OSS employer has yet been identified");
  }
});

test("Batch 527 advances attempted, employer and archival coverage with reproducible totals", () => {
  expect(stats).toMatchObject({
    source_rows: 23978,
    person_entities: 23940,
    research_attempted_people: 5038,
    research_attempt_percent: 21.0443,
    verified_affiliation_people: 568,
    verified_affiliation_percent: 2.3726,
    verified_employer_people: 253,
    verified_employer_percent: 1.0568,
    archival_review_assessed_people: 4993,
    archival_review_percent: 20.8563,
    published_claims: 3969,
    public_sources: 3397,
  });
  expect(stats.research_status_counts).toMatchObject({
    not_started: 18902,
    needs_identity_review: 284,
    no_reliable_result_after_protocol: 86,
    occupation_only_found: 920,
    verified_employer_found: 238,
  });
});

test("Batch 527 evidence is complete, citation-linked and private-value free", () => {
  const bundle = JSON.parse(evidence);
  expect(bundle).toMatchObject({ bundle_version: "1.0" });
  expect(bundle.sources).toHaveLength(8);
  expect(bundle.organizations).toHaveLength(3);
  expect(bundle.affiliations).toHaveLength(7);
  expect(bundle.claims).toHaveLength(13);
  expect(bundle.claims.reduce(
    (sum: number, claim: { sources: unknown[] }) => sum + claim.sources.length,
    0,
  )).toBe(28);
  expect(bundle.person_updates).toHaveLength(10);
  expect(bundle.research_attempts).toHaveLength(10);
  expect(bundle.claims.filter(
    (claim: { claim_type: string }) => claim.claim_type === "last_civilian_pre_service",
  )).toHaveLength(1);
  expect(evidence).not.toMatch(/serial_number|service_number/);
});

test.describe("Batch 527 direct profile routes", () => {
  for (const [id, name, , box] of cohort) {
    test(`${name} renders from a direct route`, async ({ page }) => {
      await page.goto(`./people/${id}/`);
      await expect(page.locator("h1")).toContainText(name);
      await expect(page.locator("body")).toContainText(`Box${box}`);
      await expect(page.locator("body")).toContainText("Archival-review priority");
    });
  }
});
