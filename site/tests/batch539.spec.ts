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
    "../../research/evidence-page-one-hundred-and-eight-mary-p-davis-through-robert-t-davis-pathways_batch-539_2026-09-15.json",
    import.meta.url,
  ),
  "utf8",
);
const profile = (id: string) =>
  people.find((person: { person_id: string }) => person.person_id === id);

const cohort = [
  ["bed59d15-66fe-5cfd-a2bd-a41648e38a86", "Mary P Davis", "c2e99027-9dd3-5c27-98d4-5fcd9d7518d5", false, "171"],
  ["74a3e55c-f716-5672-ae2a-871108ca67ec", "Minor M Davis", "4f0fed1b-36b5-5ea0-82e2-493c0569c50f", true, "171"],
  ["13bb115c-47cc-5c19-97d9-8039d5036f95", "Peggy M Davis", "e2a7fad3-a555-533c-98c0-ba48ccc6895c", false, "171"],
  ["e7cf43fd-0bcb-592a-9726-0e315671642c", "Ray Davis", "a50cc0a8-d77b-5068-801e-0eb04bed9914", true, "171"],
  ["96743f6b-b6f5-5443-8207-f0dce6966053", "Richard G Davis", "76511bc7-38e7-5047-9c32-b37a3f210708", true, "171"],
  ["f2684834-3532-5a21-9216-632a4f2c6b22", "Robert H Davis", "c6f53240-60b4-5c39-afe6-ff50caf4780e", true, "171"],
  ["13b34e92-909a-5e1a-901b-418282a3c346", "Robert W Davis", "20571ed9-ff8f-5eba-b955-e7b145136641", false, "172"],
  ["6b6a26ab-e25d-5b81-ae7d-9b0ea1a27d24", "Robert P Davis", "4197321e-48df-5cd8-9143-3b5a31e86375", true, "171"],
  ["a081662b-2adf-5951-bb48-09b521f2a022", "Robert E Davis", "bd52a31b-9874-5a79-917e-05de7ba910a1", true, "171"],
  ["0f01525b-21aa-5a17-92d8-05d651be5ce5", "Robert T Davis", "d4bf9621-3700-590b-935a-194160c7fa43", true, "171"],
] as const;

test("Batch 539 preserves ten page 108 rows and masks seven private fields", () => {
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

test("Batch 539 makes the Minor M Davis identifier conflict explicit", () => {
  const person = profile("74a3e55c-f716-5672-ae2a-871108ca67ec");
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
  expect(person.identity_evidence).toContain("additional initials");
  expect(person.next_action).toContain("resolve the private-identifier/name conflict");
});

test("Batch 539 confirms Robert H Davis and publishes retail occupation only", () => {
  const person = profile("f2684834-3532-5a21-9216-632a4f2c6b22");
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
    role_title: null,
    occupation: "Retail managers",
    relationship_type: "unknown",
    end_date: "1942-10-23",
    immediate_pre_oss: false,
    last_civilian_pre_service: false,
    temporal_basis: "strongly_date_bounded",
    claim_confidence: "medium",
  });
  expect(person.claims).toHaveLength(2);
  expect(person.claims.find((claim: { claim_type: string }) => claim.claim_type === "identity")).toMatchObject({
    claim_confidence: "confirmed",
    publication_status: "published",
  });
  expect(person.claims.find((claim: { claim_type: string }) => claim.claim_type === "occupation")).toMatchObject({
    claim_confidence: "medium",
    publication_status: "publish_qualified",
  });
  expect(person.next_action).toContain("no employer");
});

test("Batch 539 confirms Robert T Davis without inferring a spouse, farm or employer", () => {
  const person = profile("0f01525b-21aa-5a17-92d8-05d651be5ce5");
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
    role_title: null,
    occupation: "Farm couples",
    relationship_type: "unknown",
    end_date: "1943-04-05",
    immediate_pre_oss: false,
    last_civilian_pre_service: false,
    temporal_basis: "strongly_date_bounded",
    claim_confidence: "medium",
  });
  expect(person.claims).toHaveLength(2);
  expect(person.claims.find((claim: { claim_type: string }) => claim.claim_type === "occupation")).toMatchObject({
    evidence_excerpt: "3-36. Farm couples",
    claim_confidence: "medium",
    publication_status: "publish_qualified",
  });
  expect(person.next_action).toContain("does not establish a spouse, farm, employer");
});

test("Batch 539 confirms Robert E Davis without interpreting value 999", () => {
  const person = profile("a081662b-2adf-5951-bb48-09b521f2a022");
  expect(person).toMatchObject({
    identity_status: "confirmed",
    personnel_category: "enlisted_army_personnel",
    commissioned_officer: false,
    research_status: "requires_archival_review",
    research_attempt_count: 4,
  });
  expect(person.archival_file).toMatchObject({ review_priority: "critical" });
  expect(person.other_pre_oss_affiliations).toEqual([]);
  expect(person.claims).toHaveLength(1);
  expect(person.claims[0]).toMatchObject({
    claim_type: "identity",
    claim_confidence: "confirmed",
    publication_status: "published",
  });
  expect(person.next_action).toContain("occupation value 999 is not defined");
});

test("Batch 539 leaves six identities unresolved with Box 171 or 172 guidance", () => {
  const resolvedIds = new Set([
    "74a3e55c-f716-5672-ae2a-871108ca67ec",
    "f2684834-3532-5a21-9216-632a4f2c6b22",
    "a081662b-2adf-5951-bb48-09b521f2a022",
    "0f01525b-21aa-5a17-92d8-05d651be5ce5",
  ]);
  for (const [id] of cohort.filter(([id]) => !resolvedIds.has(id))) {
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
    expect(person.next_action).toContain("No reliable pre-OSS employer");
  }
});

test("Batch 539 advances attempted and archival coverage without inflating employer coverage", () => {
  expect(stats).toMatchObject({
    source_rows: 23978,
    person_entities: 23940,
    research_attempted_people: 5158,
    research_attempt_percent: 21.5455,
    verified_affiliation_people: 569,
    verified_affiliation_percent: 2.3768,
    verified_employer_people: 253,
    verified_employer_percent: 1.0568,
    archival_review_assessed_people: 5113,
    archival_review_percent: 21.3576,
    public_sources: 3441,
    published_claims: 4042,
  });
  expect(stats.research_status_counts).toMatchObject({
    not_started: 18782,
    conflicting_sources: 99,
    no_reliable_result_after_protocol: 160,
    occupation_only_found: 948,
    documented_prewar_employer_found: 101,
    requires_archival_review: 3114,
  });
});

test("Batch 539 evidence is citation-linked and private-value free", () => {
  const bundle = JSON.parse(evidence);
  expect(bundle).toMatchObject({ bundle_version: "1.0" });
  expect(bundle.sources).toHaveLength(3);
  expect(bundle.organizations).toHaveLength(0);
  expect(bundle.affiliations).toHaveLength(2);
  expect(bundle.claims).toHaveLength(6);
  expect(bundle.claims.flatMap((claim: { sources: unknown[] }) => claim.sources)).toHaveLength(12);
  expect(bundle.person_updates).toHaveLength(10);
  expect(bundle.research_attempts).toHaveLength(10);
  expect(bundle.claims.filter((claim: { claim_confidence: string }) => claim.claim_confidence === "confirmed")).toHaveLength(3);
  expect(bundle.claims.filter((claim: { claim_confidence: string }) => claim.claim_confidence === "conflicting")).toHaveLength(1);
  expect(evidence).toContain("0-72. Retail managers");
  expect(evidence).toContain("3-36. Farm couples");
  expect(evidence).toContain("not 9-99");
  expect(evidence).not.toMatch(/serial_number|service_number/);
});

test.describe("Batch 539 direct profile routes", () => {
  for (const [id, name, , , box] of cohort) {
    test(`${name} ${id.slice(0, 8)} renders from a direct route`, async ({ page }) => {
      await page.goto(`./people/${id}/`);
      await expect(page.locator("h1")).toContainText(name);
      await expect(page.locator("body")).toContainText(`Box${box}`);
      await expect(page.locator("body")).toContainText("Archival-review priority");
    });
  }
});
