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
    "../../research/evidence-page-one-hundred-and-five-geneva-l-daniel-through-edward-l-daniels-pathways_batch-525_2026-09-14.json",
    import.meta.url,
  ),
  "utf8",
);
const profile = (id: string) =>
  people.find((person: { person_id: string }) => person.person_id === id);

const cohort = [
  ["97f6c213-8af1-55f6-8e21-4ebab79f21b7", "Geneva L Daniel", "f48c9070-b511-56d1-8d5b-11dbfb0c7f42", false],
  ["8238fcdb-7a2e-59b2-89c7-0f097eb10498", "James B Daniel", "e3728e65-ff1a-5d11-a9a7-30a0db6cdd8d", false],
  ["66664c99-022f-5260-8e7f-b2afcec812c5", "John F Daniel", "41eca26c-ab35-584c-a178-926d98043739", true],
  ["774123a9-07fe-586c-847c-25fe8182e3c5", "John W Daniel", "b5f81995-1e3b-5a24-b47e-5f90eb02307c", false],
  ["c83d741d-ded3-5cac-9502-aefe3f33da1c", "Margaret Daniel", "35077173-5775-5b4a-92ea-3e7167dc6bc0", false],
  ["7651d38f-2f40-53ba-b4be-ec7a296429f7", "Robert J Daniel", "723396c1-30a7-540d-8638-5efc7935dd8e", true],
  ["96fdbd36-d557-5870-8510-07af0a370858", "Edward J Danielewicz", "1b7551d9-d63e-5888-893a-fc3ab9796bd1", true],
  ["104ccef3-ff98-5492-a69c-63a673ce95a5", "Tatianna Daniell", "a54c893c-e846-5e62-9843-a9dd5ff4aca6", false],
  ["b5c2a838-9719-5c27-9583-d1013c57ba9c", "Arlan R Daniels", "77ddb91b-c7db-5717-8aa7-aed89a229cfc", true],
  ["d8b387a9-8374-54a2-a8cf-f52c7b8c5efe", "Edward L Daniels", "1e71eee6-b7c8-533c-b299-f495f33e8eaa", true],
] as const;

test("Batch 525 preserves ten printed Box 166 rows and masks every private field", () => {
  for (const [id, name, sourceRecordId, hasPrivateIdentifier] of cohort) {
    const person = profile(id);
    expect(person).toMatchObject({ display_name: name });
    const sourceRecord = person.source_records.find(
      (record: { source_record_id: string }) => record.source_record_id === sourceRecordId,
    );
    expect(sourceRecord).toMatchObject({
      archive_location: "230/86/29/05",
      box: "166",
      pdf_page: 105,
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

test("Batch 525 publishes only Arlan Daniels's exact-identifier identity finding", () => {
  const person = profile("b5c2a838-9719-5c27-9583-d1013c57ba9c");
  expect(person).toMatchObject({
    identity_status: "confirmed",
    personnel_category: "enlisted_army_personnel",
    commissioned_officer: false,
    allied_or_foreign_personnel: false,
    research_status: "requires_archival_review",
    research_attempt_count: 3,
  });
  expect(person.name_variants).toContain("Arlan R D Daniels");
  expect(person.claims).toHaveLength(1);
  expect(person.claims[0]).toMatchObject({
    claim_type: "identity",
    claim_confidence: "confirmed",
  });
  expect(person.immediate_pre_oss_affiliations).toEqual([]);
  expect(person.last_civilian_pre_service).toEqual([]);
  expect(person.other_pre_oss_affiliations).toEqual([]);
});

test("Batch 525 preserves ambiguous and unresolved identities without affiliations", () => {
  const ambiguous = cohort
    .map(([id]) => id)
    .filter((id) => ![
      "97f6c213-8af1-55f6-8e21-4ebab79f21b7",
      "104ccef3-ff98-5492-a69c-63a673ce95a5",
      "b5c2a838-9719-5c27-9583-d1013c57ba9c",
    ].includes(id));
  for (const id of ambiguous) {
    expect(profile(id).identity_status).toBe("ambiguous");
  }
  for (const id of [
    "97f6c213-8af1-55f6-8e21-4ebab79f21b7",
    "104ccef3-ff98-5492-a69c-63a673ce95a5",
  ]) {
    expect(profile(id).identity_status).toBe("unresolved");
  }
  for (const [id] of cohort) {
    const person = profile(id);
    expect(person.research_status).toBe("requires_archival_review");
    expect(person.research_attempt_count).toBe(3);
    expect(person.immediate_pre_oss_affiliations).toEqual([]);
    expect(person.last_civilian_pre_service).toEqual([]);
    expect(person.other_pre_oss_affiliations).toEqual([]);
    expect(person.next_action).toContain(
      "No reliable pre-OSS employer has yet been identified",
    );
  }
  for (const id of [
    "66664c99-022f-5260-8e7f-b2afcec812c5",
    "96fdbd36-d557-5870-8510-07af0a370858",
  ]) {
    expect(profile(id)).toMatchObject({
      personnel_category: "commissioned_army_officer",
      commissioned_officer: true,
      allied_or_foreign_personnel: false,
    });
  }
});

test("Batch 525 advances attempted and archival coverage without inventing an employer", () => {
  expect(stats).toMatchObject({
    source_rows: 23978,
    person_entities: 23940,
    research_attempted_people: 5018,
    research_attempt_percent: 20.9607,
    verified_affiliation_people: 566,
    verified_affiliation_percent: 2.3642,
    verified_employer_people: 252,
    verified_employer_percent: 1.0526,
    archival_review_assessed_people: 4973,
    archival_review_percent: 20.7728,
    published_claims: 3947,
    public_sources: 3378,
  });
  expect(stats.research_status_counts).toMatchObject({
    not_started: 18922,
    occupation_only_found: 913,
    requires_archival_review: 3103,
  });
});

test("Batch 525 evidence carries no private value or unsupported affiliation", () => {
  const bundle = JSON.parse(evidence);
  expect(bundle).toMatchObject({
    bundle_version: "1.0",
    organizations: [],
    affiliations: [],
  });
  expect(bundle.sources).toHaveLength(3);
  expect(bundle.claims).toHaveLength(1);
  expect(bundle.claims[0].sources).toHaveLength(3);
  expect(bundle.person_updates).toHaveLength(10);
  expect(bundle.research_attempts).toHaveLength(10);
  expect(bundle.claims[0].claim_type).toBe("identity");
  expect(bundle.claims.some((claim: { claim_type: string }) => claim.claim_type.includes("employer"))).toBe(false);
  expect(evidence).not.toMatch(/serial_number|service_number/);
});

test.describe("Batch 525 direct profile routes", () => {
  for (const [id, name] of cohort) {
    test(`${name} renders from a direct route`, async ({ page }) => {
      await page.goto(`./people/${id}/`);
      await expect(page.locator("h1")).toContainText(name);
      await expect(page.locator("body")).toContainText("Box 166");
      await expect(page.locator("body")).toContainText(
        "No reliable pre-OSS employer has yet been identified",
      );
    });
  }
});
