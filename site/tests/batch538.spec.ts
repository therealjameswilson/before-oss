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
    "../../research/evidence-page-one-hundred-and-seven-john-t-davis-through-page-one-hundred-and-eight-mary-l-davis-pathways_batch-538_2026-09-15.json",
    import.meta.url,
  ),
  "utf8",
);
const locDecisions = fs.readFileSync(
  new URL("../../research/loc_review_decisions_2026-09-15_batch538.csv", import.meta.url),
  "utf8",
);
const profile = (id: string) =>
  people.find((person: { person_id: string }) => person.person_id === id);

const cohort = [
  ["6ca4ef9a-dc1b-59cd-be80-ada20139703f", "John T Davis", "df9d2aed-d603-5b37-9a6b-00efb4579791", false, 107, "171"],
  ["fc29c01f-e6d1-5966-afc8-d01cf8a6d15b", "John R Davis Jr.", "7c6a45f8-62c3-507c-a9b0-fc8a997613eb", true, 107, "170"],
  ["344ba533-e8b9-53cc-b5b8-29d32026e214", "Joseph W Davis", "ab51056e-d69c-59d5-b64d-1ed700089581", false, 107, "171"],
  ["a08fced3-5874-5724-ac83-b35c41c7ef93", "Leonard R Davis", "438cf635-b39e-5be8-a27f-fb2735e950de", false, 107, "171"],
  ["3f99df4f-3ca0-54cf-8bbb-cabaebdc70bb", "Lloyd G Davis", "a3970330-e2eb-56c2-a027-a2a429ee629c", true, 107, "171"],
  ["bc45da48-63ad-596d-b657-f60237bd2a15", "Louie D Davis", "e622d0f3-c6b1-5967-a044-a1d469f59775", true, 107, "171"],
  ["73c434fa-35a7-5436-b785-7a8784c387e2", "Louis B Davis", "986969e3-5c31-50a0-aa35-63551b0d5fce", true, 107, "171"],
  ["5cf9b950-cd92-5702-a81a-0177fce48aa9", "Malcolm W Davis", "65337db6-a958-558a-ace2-1f8fc52e3edc", false, 108, "171"],
  ["c9005af8-2f62-545f-91dd-f27dd362dbb0", "Marion R Davis", "17fc3671-db43-5269-942d-ce1e878f8984", false, 108, "171"],
  ["9847c8d8-3763-516a-91fe-1931746d7cef", "Mary L Davis", "1da310b5-edbc-525d-9fb1-1e3990248e68", false, 108, "171"],
] as const;

test("Batch 538 preserves ten cross-page rows and masks four private fields", () => {
  for (const [id, name, sourceRecordId, hasPrivateIdentifier, pdfPage, box] of cohort) {
    const person = profile(id);
    expect(person).toMatchObject({ display_name: name });
    const sourceRecord = person.source_records.find(
      (record: { source_record_id: string }) => record.source_record_id === sourceRecordId,
    );
    expect(sourceRecord).toMatchObject({
      archive_location: "230/86/29/06",
      box,
      pdf_page: pdfPage,
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

test("Batch 538 confirms John R Davis Jr without interpreting value 992", () => {
  const person = profile("fc29c01f-e6d1-5966-afc8-d01cf8a6d15b");
  expect(person).toMatchObject({
    identity_status: "confirmed",
    personnel_category: "enlisted_army_personnel",
    commissioned_officer: false,
    research_status: "requires_archival_review",
    research_attempt_count: 3,
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
  expect(person.identity_evidence).toContain("September 23, 1942");
  expect(person.next_action).toContain("occupation value 992 is not defined");
});

test("Batch 538 confirms Lloyd G Davis and publishes occupation only", () => {
  const person = profile("3f99df4f-3ca0-54cf-8bbb-cabaebdc70bb");
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
    role_title: "Stenographer or typist",
    relationship_type: "unknown",
    end_date: "1940-10-30",
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

test("Batch 538 preserves index-derived Lieutenant and Sergeant classifications", () => {
  expect(profile("a08fced3-5874-5724-ac83-b35c41c7ef93")).toMatchObject({
    identity_status: "unresolved",
    personnel_category: "commissioned_army_officer",
    commissioned_officer: true,
  });
  expect(profile("bc45da48-63ad-596d-b657-f60237bd2a15")).toMatchObject({
    identity_status: "unresolved",
    personnel_category: "enlisted_army_personnel",
    commissioned_officer: false,
  });
});

test("Batch 538 leaves eight identities unresolved with archival guidance", () => {
  const unresolvedIds = cohort
    .map(([id]) => id)
    .filter(
      (id) =>
        id !== "fc29c01f-e6d1-5966-afc8-d01cf8a6d15b" &&
        id !== "3f99df4f-3ca0-54cf-8bbb-cabaebdc70bb",
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
    expect(person.next_action).toContain("No reliable pre-OSS employer");
  }
});

test("Batch 538 advances attempted and archival coverage without inflating employer coverage", () => {
  expect(stats).toMatchObject({
    source_rows: 23978,
    person_entities: 23940,
    research_attempted_people: 5148,
    research_attempt_percent: 21.5038,
    verified_affiliation_people: 569,
    verified_affiliation_percent: 2.3768,
    verified_employer_people: 253,
    verified_employer_percent: 1.0568,
    archival_review_assessed_people: 5103,
    archival_review_percent: 21.3158,
    public_sources: 3438,
    published_claims: 4036,
  });
  expect(stats.research_status_counts).toMatchObject({
    not_started: 18792,
    conflicting_sources: 98,
    no_reliable_result_after_protocol: 154,
    occupation_only_found: 946,
    documented_prewar_employer_found: 101,
    requires_archival_review: 3113,
  });
});

test("Batch 538 evidence and all 25 LoC rejections are durable and private-value free", () => {
  const bundle = JSON.parse(evidence);
  expect(bundle).toMatchObject({ bundle_version: "1.0" });
  expect(bundle.sources).toHaveLength(3);
  expect(bundle.organizations).toHaveLength(0);
  expect(bundle.affiliations).toHaveLength(1);
  expect(bundle.claims).toHaveLength(3);
  expect(bundle.claims.flatMap((claim: { sources: unknown[] }) => claim.sources)).toHaveLength(6);
  expect(bundle.person_updates).toHaveLength(10);
  expect(bundle.research_attempts).toHaveLength(10);
  expect(evidence).toContain("1-37. Stenographers and typists");
  expect(evidence).toContain("not 9-92");
  expect(evidence).not.toMatch(/serial_number|service_number/);
  const decisionRows = locDecisions.trim().split("\n");
  expect(decisionRows).toHaveLength(26);
  expect(decisionRows.slice(1).every((row) => row.includes(",rejected,"))).toBe(true);
});

test.describe("Batch 538 direct profile routes", () => {
  for (const [id, name, , , , box] of cohort) {
    test(`${name} ${id.slice(0, 8)} renders from a direct route`, async ({ page }) => {
      await page.goto(`./people/${id}/`);
      await expect(page.locator("h1")).toContainText(name);
      await expect(page.locator("body")).toContainText(`Box${box}`);
      await expect(page.locator("body")).toContainText("Archival-review priority");
    });
  }
});
