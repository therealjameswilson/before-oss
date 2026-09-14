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
    "../../research/evidence-page-one-hundred-and-four-james-f-damico-through-joseph-c-dance-pathways_batch-523_2026-09-14.json",
    import.meta.url,
  ),
  "utf8",
);
const profile = (id: string) =>
  people.find((person: { person_id: string }) => person.person_id === id);

const cohort = [
  ["c799ac78-2e5f-5312-b3c1-cd4405a39c35", "James F D'Amico", "522b6084-9f2e-5e90-a488-b76410a3e0b8", true],
  ["8ad4370f-692f-5584-8be2-6a1607add3f0", "Jerry M D'Amico", "06a96c6c-1a15-5942-a1e3-b70128825220", true],
  ["0dab8cbd-61d4-5245-8502-0493d2ccdf37", "Jean Damming", "658ae6b6-008a-53fc-9882-ba238104f172", false],
  ["9158ad40-7220-514e-8ef5-8446cc557231", "Henri C Damon", "be32aad7-59a5-5b24-a1d9-6e37e5a3a8a7", false],
  ["813f3345-42dc-5d07-af78-c0b6e3525fba", "Gerald V D'Amore", "79a5aa35-d81e-56b0-9eaa-6c7e7862547a", false],
  ["96bb4ce4-61cd-50b8-b64d-7b3cfe2182b9", "Norma Damuth", "25ceb112-497c-5a66-9b2b-cb96e5adca8b", false],
  ["9c3cdc77-40a5-549a-9abd-d4feb99c9853", "Donald M Dana", "a55de69a-fc06-5c72-b3a3-12012e9bb899", true],
  ["98b6e811-c688-584e-aef3-a250a45dac62", "John J Danahay", "cbb69e2a-4b29-53fa-ab07-2e8cdf5b6b35", true],
  ["ba4f1272-d0ff-5682-b61d-3713197a00eb", "Alice M Danaher", "f4b95b0e-7ed1-55e3-8849-07ab9782889a", false],
  ["71543a72-4238-5b68-a750-e887c29005c9", "Joseph C Dance", "63811370-412d-51e0-8a3c-8fbb6b045149", true],
] as const;

test("Batch 523 preserves ten printed rows and masks every private field", () => {
  for (const [id, name, sourceRecordId, hasPrivateIdentifier] of cohort) {
    const person = profile(id);
    expect(person).toMatchObject({ display_name: name });
    const sourceRecord = person.source_records.find(
      (record: { source_record_id: string }) => record.source_record_id === sourceRecordId,
    );
    expect(sourceRecord).toMatchObject({
      archive_location: "230/86/29/05",
      box: "165",
      pdf_page: 104,
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

test("Batch 523 limits Army evidence to four identities and two qualified occupations", () => {
  const confirmed = [
    "c799ac78-2e5f-5312-b3c1-cd4405a39c35",
    "8ad4370f-692f-5584-8be2-6a1607add3f0",
    "9c3cdc77-40a5-549a-9abd-d4feb99c9853",
    "71543a72-4238-5b68-a750-e887c29005c9",
  ];
  const occupationOnly = [
    "c799ac78-2e5f-5312-b3c1-cd4405a39c35",
    "71543a72-4238-5b68-a750-e887c29005c9",
  ];
  for (const id of confirmed) {
    const person = profile(id);
    expect(person).toMatchObject({
      identity_status: "confirmed",
      personnel_category: "enlisted_army_personnel",
      commissioned_officer: false,
      research_attempt_count: 3,
    });
    expect(person.claims.some((claim: { claim_type: string }) => claim.claim_type === "identity")).toBe(true);
  }
  for (const id of occupationOnly) {
    const person = profile(id);
    expect(person.research_status).toBe("occupation_only_found");
    expect(person.other_pre_oss_affiliations).toHaveLength(1);
    expect(person.claims.some((claim: { claim_type: string }) => claim.claim_type === "occupation")).toBe(true);
    expect(person.immediate_pre_oss_affiliations).toEqual([]);
    expect(person.last_civilian_pre_service).toEqual([]);
  }
  for (const id of [
    "8ad4370f-692f-5584-8be2-6a1607add3f0",
    "9c3cdc77-40a5-549a-9abd-d4feb99c9853",
  ]) {
    const person = profile(id);
    expect(person.research_status).toBe("requires_archival_review");
    expect(person.other_pre_oss_affiliations).toEqual([]);
    expect(person.claims).toHaveLength(1);
  }
});

test("Batch 523 keeps unresolved namesakes unresolved and preserves the French classification", () => {
  const unresolved = [
    "0dab8cbd-61d4-5245-8502-0493d2ccdf37",
    "9158ad40-7220-514e-8ef5-8446cc557231",
    "813f3345-42dc-5d07-af78-c0b6e3525fba",
    "96bb4ce4-61cd-50b8-b64d-7b3cfe2182b9",
    "98b6e811-c688-584e-aef3-a250a45dac62",
    "ba4f1272-d0ff-5682-b61d-3713197a00eb",
  ];
  for (const id of unresolved) {
    const person = profile(id);
    expect(person.identity_status).toBe("unresolved");
    expect(person.research_status).toBe("requires_archival_review");
    expect(person.research_attempt_count).toBe(3);
    expect(person.immediate_pre_oss_affiliations).toEqual([]);
    expect(person.last_civilian_pre_service).toEqual([]);
    expect(person.other_pre_oss_affiliations).toEqual([]);
    expect(person.claims).toEqual([]);
    expect(person.next_action).toContain(
      "No reliable pre-OSS employer has yet been identified",
    );
  }
  expect(profile("9158ad40-7220-514e-8ef5-8446cc557231")).toMatchObject({
    personnel_category: "foreign_or_allied_military_personnel",
    commissioned_officer: true,
    allied_or_foreign_personnel: true,
  });
});

test("Batch 523 advances research and archival coverage without inventing an employer", () => {
  expect(stats).toMatchObject({
    source_rows: 23978,
    person_entities: 23940,
    research_attempted_people: 4998,
    research_attempt_percent: 20.8772,
    verified_affiliation_people: 566,
    verified_affiliation_percent: 2.3642,
    verified_employer_people: 252,
    verified_employer_percent: 1.0526,
    archival_review_assessed_people: 4953,
    archival_review_percent: 20.6892,
    published_claims: 3942,
    public_sources: 3371,
  });
  expect(stats.research_status_counts).toMatchObject({
    not_started: 18942,
    occupation_only_found: 911,
    requires_archival_review: 3085,
  });
});

test("Batch 523 evidence carries no private value or unsupported employer claim", () => {
  const bundle = JSON.parse(evidence);
  expect(bundle).toMatchObject({
    bundle_version: "1.0",
    organizations: [],
  });
  expect(bundle.sources).toHaveLength(4);
  expect(bundle.affiliations).toHaveLength(2);
  expect(bundle.claims).toHaveLength(6);
  expect(bundle.person_updates).toHaveLength(10);
  expect(bundle.research_attempts).toHaveLength(10);
  expect(bundle.claims.filter((claim: { claim_type: string }) => claim.claim_type === "occupation")).toHaveLength(2);
  expect(bundle.claims.filter((claim: { claim_type: string }) => claim.claim_type === "identity")).toHaveLength(4);
  expect(bundle.claims.some((claim: { claim_type: string }) => claim.claim_type.includes("employer"))).toBe(false);
  expect(evidence).not.toMatch(/serial_number|service_number/);
});

test.describe("Batch 523 direct profile routes", () => {
  for (const [id, name] of cohort) {
    test(`${name} renders from a direct route`, async ({ page }) => {
      await page.goto(`./people/${id}/`);
      await expect(page.locator("h1")).toContainText(name);
      await expect(page.locator("body")).toContainText("Box 165");
      await expect(page.locator("body")).toContainText(
        "No reliable pre-OSS employer has yet been identified",
      );
    });
  }
});
