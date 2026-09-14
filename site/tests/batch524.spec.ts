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
    "../../research/evidence-page-one-hundred-and-four-beatrice-dancy-through-page-one-hundred-and-five-ernest-daniel-pathways_batch-524_2026-09-14.json",
    import.meta.url,
  ),
  "utf8",
);
const profile = (id: string) =>
  people.find((person: { person_id: string }) => person.person_id === id);

const cohort = [
  ["15f09dd9-8494-56f9-aa03-7dc3ba54496c", "Beatrice Dancy", "b81bae01-0200-5008-a101-1fc696147c04", 104, "165", false],
  ["abe9073f-4266-5201-9851-195a7e2c2ac0", "John Dancy", "31a197ba-c8ec-58d4-9acf-2bb40c031702", 104, "165", true],
  ["895cbddd-81c3-5e2a-9599-f4bdfa90874d", "Mary E D'Andelet", "c839d807-f3cb-5aa8-bcec-e20e44a4f28f", 104, "165", false],
  ["eabf6b12-6e64-5bb1-9fe9-8fef56e97d4e", "Clifton Dandridge", "d0207e6a-e6eb-54d0-8813-83d2cb92f22d", 104, "165", false],
  ["833df3fc-4c23-523d-bff0-f8cfe6245b10", "Joseph P Dangel", "c0aa10b6-bc74-5e2f-8208-3d29e129cd1d", 104, "165", false],
  ["b7ad29dd-eeb6-5102-a05c-c2a12d3b36d1", "Dennis V Dangerfield", "92046ad1-ddff-5237-a45a-5cd35dc881e4", 104, "165", true],
  ["35317165-b4b6-5b66-9e14-6af9d3246374", "Winifred A Dangerfield", "281d0404-442c-5cea-82d6-c1411b43dc24", 104, "165", false],
  ["b634a54e-c858-5438-8f86-8abf48971ca6", "Gerard N D'Anglure", "02da3989-ca66-51d2-897e-74fd05a16ef9", 104, "165", false],
  ["8c391643-72e2-55da-99a5-b01f88991e9e", "Deborah Daniel", "2e4060d6-7b93-5268-abd1-4d31f1da1bff", 104, "166", false],
  ["ca199c87-bedf-5436-a50f-a9e8826ca713", "Ernest Daniel", "803ea945-4629-58ea-a2ae-a47f3b204a2e", 105, "166", true],
] as const;

test("Batch 524 preserves ten printed rows across two pages and masks every private field", () => {
  for (const [id, name, sourceRecordId, pageNumber, box, hasPrivateIdentifier] of cohort) {
    const person = profile(id);
    expect(person).toMatchObject({ display_name: name });
    const sourceRecord = person.source_records.find(
      (record: { source_record_id: string }) => record.source_record_id === sourceRecordId,
    );
    expect(sourceRecord).toMatchObject({
      archive_location: "230/86/29/05",
      box,
      pdf_page: pageNumber,
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

test("Batch 524 limits Army evidence to two identities and two qualified non-employer findings", () => {
  const confirmed = [
    "abe9073f-4266-5201-9851-195a7e2c2ac0",
    "b7ad29dd-eeb6-5102-a05c-c2a12d3b36d1",
  ];
  for (const id of confirmed) {
    const person = profile(id);
    expect(person).toMatchObject({
      identity_status: "confirmed",
      personnel_category: "enlisted_army_personnel",
      commissioned_officer: false,
      research_status: "occupation_only_found",
      research_attempt_count: 3,
    });
    expect(person.other_pre_oss_affiliations).toHaveLength(1);
    expect(person.immediate_pre_oss_affiliations).toEqual([]);
    expect(person.last_civilian_pre_service).toEqual([]);
    expect(person.claims.some((claim: { claim_type: string }) => claim.claim_type === "identity")).toBe(true);
  }
  expect(profile("abe9073f-4266-5201-9851-195a7e2c2ac0").other_pre_oss_affiliations[0]).toMatchObject({
    relationship_type: "student",
    occupation: "student",
    claim_confidence: "medium",
  });
  expect(profile("b7ad29dd-eeb6-5102-a05c-c2a12d3b36d1").other_pre_oss_affiliations[0]).toMatchObject({
    occupation: "Miner or mining-machine operator",
    claim_confidence: "medium",
  });
});

test("Batch 524 keeps eight unsupported identities unresolved and preserves the French classification", () => {
  const unresolved = [
    "15f09dd9-8494-56f9-aa03-7dc3ba54496c",
    "895cbddd-81c3-5e2a-9599-f4bdfa90874d",
    "eabf6b12-6e64-5bb1-9fe9-8fef56e97d4e",
    "833df3fc-4c23-523d-bff0-f8cfe6245b10",
    "35317165-b4b6-5b66-9e14-6af9d3246374",
    "b634a54e-c858-5438-8f86-8abf48971ca6",
    "8c391643-72e2-55da-99a5-b01f88991e9e",
    "ca199c87-bedf-5436-a50f-a9e8826ca713",
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
  expect(profile("b634a54e-c858-5438-8f86-8abf48971ca6")).toMatchObject({
    personnel_category: "foreign_or_allied_military_personnel",
    commissioned_officer: true,
    allied_or_foreign_personnel: true,
  });
});

test("Batch 524 advances attempted and archival coverage without inventing an employer", () => {
  expect(stats).toMatchObject({
    source_rows: 23978,
    person_entities: 23940,
    research_attempted_people: 5008,
    research_attempt_percent: 20.919,
    verified_affiliation_people: 566,
    verified_affiliation_percent: 2.3642,
    verified_employer_people: 252,
    verified_employer_percent: 1.0526,
    archival_review_assessed_people: 4963,
    archival_review_percent: 20.731,
    published_claims: 3946,
    public_sources: 3375,
  });
  expect(stats.research_status_counts).toMatchObject({
    not_started: 18932,
    occupation_only_found: 913,
    requires_archival_review: 3093,
  });
});

test("Batch 524 evidence carries no private value or unsupported employer claim", () => {
  const bundle = JSON.parse(evidence);
  expect(bundle).toMatchObject({
    bundle_version: "1.0",
    organizations: [],
  });
  expect(bundle.sources).toHaveLength(4);
  expect(bundle.affiliations).toHaveLength(2);
  expect(bundle.claims).toHaveLength(4);
  expect(bundle.person_updates).toHaveLength(10);
  expect(bundle.research_attempts).toHaveLength(10);
  expect(bundle.claims.filter((claim: { claim_type: string }) => claim.claim_type === "identity")).toHaveLength(2);
  expect(bundle.claims.filter((claim: { claim_type: string }) => claim.claim_type === "occupation")).toHaveLength(1);
  expect(bundle.claims.some((claim: { claim_type: string }) => claim.claim_type.includes("employer"))).toBe(false);
  expect(evidence).not.toMatch(/serial_number|service_number/);
});

test.describe("Batch 524 direct profile routes", () => {
  for (const [id, name, , , box] of cohort) {
    test(`${name} renders from a direct route`, async ({ page }) => {
      await page.goto(`./people/${id}/`);
      await expect(page.locator("h1")).toContainText(name);
      await expect(page.locator("body")).toContainText(`Box ${box}`);
      await expect(page.locator("body")).toContainText(
        "No reliable pre-OSS employer has yet been identified",
      );
    });
  }
});
