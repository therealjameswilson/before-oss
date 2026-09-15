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
    "../../research/evidence-page-one-hundred-and-seven-howell-a-davis-jr-through-jean-davis-pathways_batch-537_2026-09-15.json",
    import.meta.url,
  ),
  "utf8",
);
const profile = (id: string) =>
  people.find((person: { person_id: string }) => person.person_id === id);

const cohort = [
  ["b62f290b-7f6b-5ed2-82e0-07b32e59536b", "Howell A Davis Jr.", "31686f76-05f4-5213-99aa-2d7e7faeda6d", true],
  ["4bae7a16-bbff-5450-a178-963759ddfd42", "Hoyt B Davis", "51cb8b7c-c45e-5beb-9c36-46163253d0ba", true],
  ["ca4d52ae-743e-5e0e-8394-31c202f5a719", "Irvin P Davis", "550b20a3-eb3e-5de1-b9de-1dd4415d13a3", true],
  ["3c2ae6fe-a858-53ba-8d08-46f9f7d2f5c3", "Isabelle M Davis", "6db2f70e-8af4-593b-87b9-b53ee638c0e6", false],
  ["0c93f7ad-d011-53dd-8be3-ad451eb70185", "Jack E Davis", "db0fe113-cc21-526e-8694-3b8589423f79", true],
  ["f8810526-dfbe-5d21-abb7-cd54431c0d01", "James A Davis", "31e7035d-3235-5d17-ada3-e542f124c9da", true],
  ["330f89fe-6008-5162-b697-3b2396a69d57", "James E Davis", "009318c4-b362-5f1b-9ab2-f6086a9e4a71", true],
  ["ca6eb565-d431-512d-8827-ebe6ebcfa889", "James M Davis", "5c1d7055-36dc-509c-8c7d-89e147c55c83", true],
  ["da56d687-2bde-5d66-8a43-a6edd975c394", "Jane M Davis", "3a9b2f91-2833-5cf5-8752-0c9daf6e1b08", false],
  ["d54eba4c-1174-5007-a577-a9fa53a4fb36", "Jean Davis", "f4c49b46-f311-5ff6-9efa-1c9dfbe8c5c2", false],
] as const;

test("Batch 537 preserves ten page 107 rows and masks seven private fields", () => {
  for (const [id, name, sourceRecordId, hasPrivateIdentifier] of cohort) {
    const person = profile(id);
    expect(person).toMatchObject({ display_name: name });
    const sourceRecord = person.source_records.find(
      (record: { source_record_id: string }) => record.source_record_id === sourceRecordId,
    );
    expect(sourceRecord).toMatchObject({
      archive_location: "230/86/29/06",
      box: "170",
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
});

test("Batch 537 confirms James M Davis and publishes occupation only", () => {
  const person = profile("ca6eb565-d431-512d-8827-ebe6ebcfa889");
  expect(person).toMatchObject({
    identity_status: "confirmed",
    personnel_category: "enlisted_army_personnel",
    commissioned_officer: false,
    research_status: "occupation_only_found",
    research_attempt_count: 3,
  });
  expect(person.archival_file).toMatchObject({ review_priority: "high" });
  expect(person.immediate_pre_oss_affiliations).toEqual([]);
  expect(person.last_civilian_pre_service).toEqual([]);
  expect(person.other_pre_oss_affiliations).toHaveLength(1);
  expect(person.other_pre_oss_affiliations[0]).toMatchObject({
    organization_id: null,
    role_title: "Structural- and ornamental-metal worker",
    relationship_type: "unknown",
    end_date: "1942-03-01",
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

test("Batch 537 makes the Irvin P Davis identifier conflict explicit", () => {
  const person = profile("ca4d52ae-743e-5e0e-8394-31c202f5a719");
  expect(person).toMatchObject({
    identity_status: "conflicting",
    personnel_category: "unknown_or_indeterminate",
    commissioned_officer: null,
    research_status: "conflicting_sources",
    research_attempt_count: 3,
  });
  expect(person.immediate_pre_oss_affiliations).toEqual([]);
  expect(person.last_civilian_pre_service).toEqual([]);
  expect(person.other_pre_oss_affiliations).toEqual([]);
  expect(person.claims).toHaveLength(1);
  expect(person.claims[0]).toMatchObject({
    claim_type: "identity",
    claim_confidence: "conflicting",
    publication_status: "conflicting",
  });
  expect(person.identity_evidence).toContain("entirely different full name");
  expect(person.next_action).toContain("resolve the identifier/name conflict");
});

test("Batch 537 leaves eight identities unresolved with critical Box 170 guidance", () => {
  const unresolvedIds = cohort
    .map(([id]) => id)
    .filter(
      (id) =>
        id !== "ca4d52ae-743e-5e0e-8394-31c202f5a719" &&
        id !== "ca6eb565-d431-512d-8827-ebe6ebcfa889",
    );
  for (const id of unresolvedIds) {
    const person = profile(id);
    expect(person).toMatchObject({
      identity_status: "unresolved",
      research_status: "no_reliable_result_after_protocol",
      research_attempt_count: 3,
    });
    expect(person.archival_file).toMatchObject({ review_priority: "critical" });
    expect(person.immediate_pre_oss_affiliations).toEqual([]);
    expect(person.last_civilian_pre_service).toEqual([]);
    expect(person.other_pre_oss_affiliations).toEqual([]);
    expect(person.claims).toEqual([]);
    expect(person.next_action).toContain("No reliable pre-OSS employer has yet been identified");
  }
});

test("Batch 537 advances attempted and archival coverage without inflating employer coverage", () => {
  expect(stats).toMatchObject({
    source_rows: 23978,
    person_entities: 23940,
    research_attempted_people: 5138,
    research_attempt_percent: 21.462,
    verified_affiliation_people: 569,
    verified_affiliation_percent: 2.3768,
    verified_employer_people: 253,
    verified_employer_percent: 1.0568,
    archival_review_assessed_people: 5093,
    archival_review_percent: 21.274,
    public_sources: 3435,
    published_claims: 4033,
  });
  expect(stats.research_status_counts).toMatchObject({
    not_started: 18802,
    conflicting_sources: 98,
    no_reliable_result_after_protocol: 146,
    occupation_only_found: 945,
    documented_prewar_employer_found: 101,
    requires_archival_review: 3112,
  });
});

test("Batch 537 evidence is citation-linked and private-value free", () => {
  const bundle = JSON.parse(evidence);
  expect(bundle).toMatchObject({ bundle_version: "1.0" });
  expect(bundle.sources).toHaveLength(3);
  expect(bundle.organizations).toHaveLength(0);
  expect(bundle.affiliations).toHaveLength(1);
  expect(bundle.claims).toHaveLength(3);
  expect(bundle.claims.flatMap((claim: { sources: unknown[] }) => claim.sources)).toHaveLength(6);
  expect(bundle.person_updates).toHaveLength(10);
  expect(bundle.research_attempts).toHaveLength(10);
  expect(bundle.claims.filter((claim: { claim_confidence: string }) => claim.claim_confidence === "conflicting")).toHaveLength(1);
  expect(evidence).toContain("6-84. Structural- and ornamental-metal workers");
  expect(evidence).not.toMatch(/serial_number|service_number/);
});

test.describe("Batch 537 direct profile routes", () => {
  for (const [id, name] of cohort) {
    test(`${name} ${id.slice(0, 8)} renders from a direct route`, async ({ page }) => {
      await page.goto(`./people/${id}/`);
      await expect(page.locator("h1")).toContainText(name);
      await expect(page.locator("body")).toContainText("Box170");
      await expect(page.locator("body")).toContainText("Archival-review priority");
    });
  }
});
