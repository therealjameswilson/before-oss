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
    "../../research/evidence-page-one-hundred-and-five-elmer-daniels-through-frank-p-dann-pathways_batch-526_2026-09-14.json",
    import.meta.url,
  ),
  "utf8",
);
const profile = (id: string) =>
  people.find((person: { person_id: string }) => person.person_id === id);

const cohort = [
  ["230d8c01-207b-592e-b09d-a253781c959c", "Elmer Daniels", "fc84bf8b-b9e7-5780-957d-8331931c2fcc", false],
  ["00b06f2c-52e5-5855-9984-b4f0269076ae", "Eugene B Daniels", "a610f737-7fb5-578e-bf84-e708d2da9d96", true],
  ["6cbe1f06-9f6a-5663-a85c-cfd1433f86f0", "Jack Daniels", "2347ed45-cd5c-54f3-8b50-c3c9b568346a", true],
  ["e309b17a-0d33-5ecd-9951-dc281883aa70", "William H Daniels", "b72e840d-aa61-5558-a1bc-fddeb1782240", false],
  ["6a6db098-b83d-54a9-93bb-773aff9b367c", "Raymond Danielson", "b94af4ce-59af-5fd4-afff-aa64d16a19ae", false],
  ["e40b36c6-425b-579c-8110-c12cdd68589f", "Richard E Danielson", "d5283794-bfb1-5b8d-a2fd-1f1a65c339d2", false],
  ["7d8bc894-4746-550b-bc37-350c1867e0b1", "Serge Daniloff", "0f99543e-536c-5c65-b55e-57408598103d", false],
  ["285517f9-fd5c-5d83-9fbc-47e4b5e8f4b3", "Serge Daniluck", "fa82e384-5eab-5190-948e-3b5105d24743", true],
  ["c979610b-73c1-52bb-b1d3-c8be8972788e", "Albert P Dankwardt", "158fc1f8-9606-528d-9033-2e5e2191a5de", false],
  ["78f1e3b1-df47-544a-9ecb-fa84895f5c60", "Frank P Dann", "bb76caa1-6eae-5b2f-b9fc-6579fd0cc7c2", true],
] as const;

test("Batch 526 preserves ten printed Box 166 rows and masks every private field", () => {
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

test("Batch 526 confirms Daniluck and the documented Dann-Dannelly variant", () => {
  const daniluck = profile("285517f9-fd5c-5d83-9fbc-47e4b5e8f4b3");
  expect(daniluck).toMatchObject({
    identity_status: "confirmed",
    personnel_category: "enlisted_army_personnel",
    commissioned_officer: false,
    research_status: "occupation_only_found",
    research_attempt_count: 3,
  });
  expect(daniluck.other_pre_oss_affiliations).toHaveLength(2);
  expect(daniluck.other_pre_oss_affiliations.map((item: { occupation: string }) => item.occupation)).toEqual(
    expect.arrayContaining(["Mail clerk", "Stenographers and typists"]),
  );
  expect(daniluck.claims).toHaveLength(3);

  const dann = profile("78f1e3b1-df47-544a-9ecb-fa84895f5c60");
  expect(dann).toMatchObject({
    display_name: "Frank P Dann",
    identity_status: "confirmed",
    personnel_category: "enlisted_army_personnel",
    commissioned_officer: false,
    research_status: "occupation_only_found",
    research_attempt_count: 3,
  });
  expect(dann.name_variants).toContain("Frank P Dannelly");
  expect(dann.other_pre_oss_affiliations).toHaveLength(1);
  expect(dann.other_pre_oss_affiliations[0]).toMatchObject({
    relationship_type: "student",
    occupation: "Student",
    claim_confidence: "medium",
  });
  expect(dann.claims).toHaveLength(2);
});

test("Batch 526 qualifies the Daniloff-Packard and Danielson-Atlantic matches", () => {
  const daniloff = profile("7d8bc894-4746-550b-bc37-350c1867e0b1");
  expect(daniloff).toMatchObject({
    identity_status: "probable",
    research_status: "needs_identity_review",
    research_attempt_count: 3,
  });
  expect(daniloff.other_pre_oss_affiliations).toHaveLength(1);
  expect(daniloff.other_pre_oss_affiliations[0]).toMatchObject({
    organization_name_as_found: "Packard Motors Export Corporation",
    canonical_organization: "Packard Motors Export Corporation",
    role_title: "Regional manager",
    relationship_type: "employment",
    temporal_basis: "documented_prewar",
    claim_confidence: "medium",
  });

  const danielson = profile("e40b36c6-425b-579c-8110-c12cdd68589f");
  expect(danielson).toMatchObject({
    identity_status: "probable",
    research_status: "needs_identity_review",
    research_attempt_count: 3,
  });
  expect(danielson.name_variants).toContain("Richard Ely Danielson");
  expect(danielson.other_pre_oss_affiliations).toHaveLength(1);
  expect(danielson.other_pre_oss_affiliations[0]).toMatchObject({
    organization_name_as_found: "Atlantic Monthly",
    canonical_organization: "Atlantic Monthly Company",
    relationship_type: "employment",
    temporal_basis: "documented_prewar",
    claim_confidence: "medium",
  });

  for (const person of [daniloff, danielson]) {
    expect(person.immediate_pre_oss_affiliations).toEqual([]);
    expect(person.last_civilian_pre_service).toEqual([]);
    expect(person.claims).toHaveLength(2);
  }
});

test("Batch 526 leaves unsupported common-name and no-result cases unresolved", () => {
  for (const id of [
    "230d8c01-207b-592e-b09d-a253781c959c",
    "00b06f2c-52e5-5855-9984-b4f0269076ae",
    "6cbe1f06-9f6a-5663-a85c-cfd1433f86f0",
    "e309b17a-0d33-5ecd-9951-dc281883aa70",
  ]) {
    expect(profile(id).identity_status).toBe("ambiguous");
  }
  for (const id of [
    "6a6db098-b83d-54a9-93bb-773aff9b367c",
    "c979610b-73c1-52bb-b1d3-c8be8972788e",
  ]) {
    expect(profile(id).identity_status).toBe("unresolved");
  }
  for (const id of [
    "230d8c01-207b-592e-b09d-a253781c959c",
    "00b06f2c-52e5-5855-9984-b4f0269076ae",
    "6cbe1f06-9f6a-5663-a85c-cfd1433f86f0",
    "e309b17a-0d33-5ecd-9951-dc281883aa70",
    "6a6db098-b83d-54a9-93bb-773aff9b367c",
    "c979610b-73c1-52bb-b1d3-c8be8972788e",
  ]) {
    const person = profile(id);
    expect(person.research_attempt_count).toBe(3);
    expect(person.immediate_pre_oss_affiliations).toEqual([]);
    expect(person.last_civilian_pre_service).toEqual([]);
    expect(person.other_pre_oss_affiliations).toEqual([]);
    expect(person.claims).toEqual([]);
    expect(person.next_action).toContain(
      "No reliable pre-OSS employer has yet been identified",
    );
  }
  for (const id of [
    "00b06f2c-52e5-5855-9984-b4f0269076ae",
    "e309b17a-0d33-5ecd-9951-dc281883aa70",
  ]) {
    expect(profile(id)).toMatchObject({
      personnel_category: "commissioned_army_officer",
      commissioned_officer: true,
    });
  }
});

test("Batch 526 advances attempted and archival coverage without overstating employer coverage", () => {
  expect(stats).toMatchObject({
    source_rows: 23978,
    person_entities: 23940,
    research_attempted_people: 5028,
    research_attempt_percent: 21.0025,
    verified_affiliation_people: 567,
    verified_affiliation_percent: 2.3684,
    verified_employer_people: 252,
    verified_employer_percent: 1.0526,
    archival_review_assessed_people: 4983,
    archival_review_percent: 20.8145,
    published_claims: 3956,
    public_sources: 3389,
  });
  expect(stats.research_status_counts).toMatchObject({
    needs_identity_review: 282,
    no_reliable_result_after_protocol: 84,
    not_started: 18912,
    occupation_only_found: 915,
    requires_archival_review: 3103,
  });
});

test("Batch 526 evidence is source-linked, bounded, and private-field free", () => {
  const bundle = JSON.parse(evidence);
  expect(bundle).toMatchObject({ bundle_version: "1.0" });
  expect(bundle.sources).toHaveLength(11);
  expect(bundle.organizations).toHaveLength(2);
  expect(bundle.affiliations).toHaveLength(5);
  expect(bundle.claims).toHaveLength(9);
  expect(bundle.person_updates).toHaveLength(10);
  expect(bundle.research_attempts).toHaveLength(10);
  expect(bundle.claims.flatMap((claim: { sources: unknown[] }) => claim.sources)).toHaveLength(23);
  expect(bundle.affiliations.every((item: { immediate_pre_oss: boolean }) => !item.immediate_pre_oss)).toBe(true);
  expect(bundle.affiliations.every((item: { last_civilian_pre_service: boolean }) => !item.last_civilian_pre_service)).toBe(true);
  expect(evidence).not.toMatch(/serial_number|service_number/);
});

test.describe("Batch 526 direct profile routes", () => {
  for (const [id, name] of cohort) {
    test(`${name} renders from a direct route`, async ({ page }) => {
      await page.goto(`./people/${id}/`);
      await expect(page.locator("h1")).toContainText(name);
      await expect(page.locator("body")).toContainText(/Box\s*166/);
    });
  }
});
