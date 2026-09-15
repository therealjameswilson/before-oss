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
    "../../research/evidence-page-one-hundred-and-nine-harlowe-f-dean-jr-through-nato-deangeles-pathways_batch-544_2026-09-15.json",
    import.meta.url,
  ),
  "utf8",
);
const profile = (id: string) =>
  people.find((person: { person_id: string }) => person.person_id === id);

const cohort = [
  ["9176d1b5-5092-5cd5-9602-f8892227960c", "Harlowe F Dean Jr.", "b6ec2baa-796b-5cfc-989f-9d73506b5827", false],
  ["bfdf95ff-466c-5571-840e-e096dfc5ff96", "Junius S Dean", "cd3294f1-410b-51af-b8fa-5db28fceeab5", true],
  ["8e4db147-8045-5423-b361-696e83827fb4", "Sidney W Dean Jr.", "2076ff25-b580-541c-a4f3-e7da0530da1e", false],
  ["f2cc738c-e46b-54ff-82c7-5f1d5b22387d", "Vaudie Dean", "433eda13-4fad-555f-9d81-46b3e1fa844e", false],
  ["d0b62865-623d-5a43-863f-7f1bcea90305", "William Dean", "2c8e16a1-8097-5c79-96b5-b228d9654b2b", true],
  ["0c0a0e8b-7394-5a73-9746-9843ffa969c8", "William A Dean", "7a7e4aa4-223f-5e70-8e0f-4ccd55ccc665", true],
  ["9943a542-2744-5468-9e5a-fb73dde9fa04", "Elmer L Deane", "6ec68ccb-7bcc-5876-974c-5399abc2dbef", true],
  ["23c3c78e-05d3-57f2-81d3-ef477b1e7492", "Margaret W Deane", "5af55e0c-7960-5741-ada2-a60a300c3126", false],
  ["2ee2761a-5167-526c-81c2-abb2f8d8f331", "Rex D Deane", "fce9a987-8e9c-5414-9929-f541c4db1bb4", false],
  ["8b53835a-2229-5628-9934-118ef4e52c08", "Nato DeAngeles", "628731bd-bfd2-5d0f-a07c-5f109a05b446", true],
] as const;

test("Batch 544 preserves ten page-109 rows and masks five private fields", () => {
  for (const [id, name, sourceRecordId, hasPrivateIdentifier] of cohort) {
    const person = profile(id);
    expect(person).toMatchObject({ display_name: name });
    const sourceRecord = person.source_records.find(
      (record: { source_record_id: string }) => record.source_record_id === sourceRecordId,
    );
    expect(sourceRecord).toMatchObject({
      archive_location: "230/86/29/06",
      box: "174",
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

test("Batch 544 publishes Harlowe Dean's Civic Concerts role only as qualified evidence", () => {
  const person = profile("9176d1b5-5092-5cd5-9602-f8892227960c");
  expect(person).toMatchObject({
    identity_status: "probable",
    personnel_category: "unknown_or_indeterminate",
    commissioned_officer: null,
    research_status: "documented_prewar_employer_found",
    research_attempt_count: 5,
    manual_review_required: true,
  });
  expect(person.archival_file).toMatchObject({ review_priority: "critical" });
  expect(person.immediate_pre_oss_affiliations).toEqual([]);
  expect(person.last_civilian_pre_service).toEqual([]);
  expect(person.other_pre_oss_affiliations).toHaveLength(1);
  expect(person.other_pre_oss_affiliations[0]).toMatchObject({
    canonical_organization: "Civic Concert Service",
    organization_name_as_found: "Civic Concerts",
    role_title: "Representative",
    relationship_type: "employment",
    end_date: "1940-03-31",
    temporal_basis: "documented_prewar",
    identity_confidence: "probable",
    claim_confidence: "medium",
    publication_status: "publish_qualified",
  });
  expect(person.claims).toHaveLength(2);
  expect(person.next_action).toContain("Keep the 1940 role qualified");
});

test("Batch 544 confirms Elmer Deane but keeps the Army result occupation-only", () => {
  const person = profile("9943a542-2744-5468-9e5a-fb73dde9fa04");
  expect(person).toMatchObject({
    identity_status: "confirmed",
    personnel_category: "enlisted_army_personnel",
    commissioned_officer: false,
    research_status: "occupation_only_found",
    research_attempt_count: 5,
    manual_review_required: false,
  });
  expect(person.archival_file).toMatchObject({ review_priority: "high" });
  expect(person.immediate_pre_oss_affiliations).toEqual([]);
  expect(person.last_civilian_pre_service).toEqual([]);
  expect(person.other_pre_oss_affiliations).toHaveLength(1);
  expect(person.other_pre_oss_affiliations[0]).toMatchObject({
    organization_id: null,
    occupation: "Stamping occupations in mechanical treatment of metals",
    relationship_type: "employment",
    end_date: "1942-12-16",
    temporal_basis: "strongly_date_bounded",
    identity_confidence: "confirmed",
    claim_confidence: "medium",
    publication_status: "publish_qualified",
  });
  expect(person.claims).toHaveLength(2);
  expect(JSON.stringify(person)).not.toContain("last civilian employer");
});

test("Batch 544 preserves Nato de Angeles's strong OSS evidence and identifier conflict", () => {
  const person = profile("8b53835a-2229-5628-9934-118ef4e52c08");
  expect(person).toMatchObject({
    identity_status: "conflicting",
    personnel_category: "enlisted_army_personnel",
    commissioned_officer: false,
    research_status: "conflicting_sources",
    research_attempt_count: 5,
    manual_review_required: true,
  });
  expect(person.archival_file).toMatchObject({ review_priority: "critical" });
  expect(person.immediate_pre_oss_affiliations).toEqual([]);
  expect(person.last_civilian_pre_service).toEqual([]);
  expect(person.other_pre_oss_affiliations).toEqual([]);
  expect(person.claims).toHaveLength(3);
  expect(person.claims.filter((claim: { claim_confidence: string }) => claim.claim_confidence === "high")).toHaveLength(2);
  expect(person.claims.filter((claim: { claim_confidence: string }) => claim.claim_confidence === "conflicting")).toHaveLength(1);
  expect(JSON.stringify(person)).toContain("Private (Acting Sergeant) Nato de Angeles");
  expect(JSON.stringify(person)).toContain("different surname");
  expect(JSON.stringify(person)).not.toContain("pre-OSS employer found");
});

test("Batch 544 keeps the two William Dean rows separate and unresolved", () => {
  const william = profile("d0b62865-623d-5a43-863f-7f1bcea90305");
  const williamA = profile("0c0a0e8b-7394-5a73-9746-9843ffa969c8");
  expect(william.person_id).not.toBe(williamA.person_id);
  for (const person of [william, williamA]) {
    expect(person).toMatchObject({
      identity_status: "unresolved",
      research_status: "requires_archival_review",
      research_attempt_count: 5,
      manual_review_required: true,
    });
    expect(person.archival_file).toMatchObject({ review_priority: "critical" });
    expect(person.claims).toEqual([]);
    expect(person.next_action).toContain("No reliable pre-OSS employer has yet been identified");
  }
  expect(william.source_records[0].indexed_middle).toBeNull();
  expect(williamA.source_records[0].indexed_middle).toBe("A");
});

test("Batch 544 preserves index-derived commissioned classifications without resolving identity", () => {
  const junius = profile("bfdf95ff-466c-5571-840e-e096dfc5ff96");
  const rex = profile("2ee2761a-5167-526c-81c2-abb2f8d8f331");
  expect(junius).toMatchObject({
    identity_status: "unresolved",
    personnel_category: "commissioned_army_officer",
    commissioned_officer: true,
    research_status: "requires_archival_review",
  });
  expect(junius.source_records[0].rank_as_indexed).toBe("Col");
  expect(rex).toMatchObject({
    identity_status: "ambiguous",
    personnel_category: "commissioned_army_officer",
    commissioned_officer: true,
    research_status: "requires_archival_review",
  });
  expect(rex.source_records[0].rank_as_indexed).toBe("1st Lt");
  for (const person of [junius, rex]) {
    expect(person.claims).toEqual([]);
    expect(person.next_action).toContain("No reliable pre-OSS employer has yet been identified");
  }
});

test("Batch 544 rejects unbridged author, patent, education, and common-name leads", () => {
  for (const id of [
    "8e4db147-8045-5423-b361-696e83827fb4",
    "f2cc738c-e46b-54ff-82c7-5f1d5b22387d",
    "23c3c78e-05d3-57f2-81d3-ef477b1e7492",
  ]) {
    const person = profile(id);
    expect(person).toMatchObject({
      identity_status: "unresolved",
      research_attempt_count: 5,
      manual_review_required: true,
    });
    expect(person.archival_file).toMatchObject({ review_priority: "critical" });
    expect(person.claims).toEqual([]);
    expect(person.next_action).toContain("No reliable pre-OSS employer has yet been identified");
  }
});

test("Batch 544 advances attempted and archival coverage without overstating verified coverage", () => {
  expect(stats).toMatchObject({
    source_rows: 23978,
    person_entities: 23940,
    possible_duplicate_groups: 247,
    research_attempted_people: 5208,
    research_attempt_percent: 21.7544,
    verified_affiliation_people: 571,
    verified_affiliation_percent: 2.3851,
    verified_employer_people: 253,
    verified_employer_percent: 1.0568,
    archival_review_assessed_people: 5163,
    archival_review_percent: 21.5664,
    public_sources: 3472,
    published_claims: 4076,
  });
  expect(stats.research_status_counts).toMatchObject({
    conflicting_sources: 102,
    documented_prewar_employer_found: 103,
    no_reliable_result_after_protocol: 181,
    not_started: 18732,
    occupation_only_found: 955,
    requires_archival_review: 3129,
  });
  expect(stats.identity_status_counts).toMatchObject({
    ambiguous: 246,
    confirmed: 1066,
    conflicting: 102,
    probable: 161,
    unresolved: 21654,
  });
  expect(stats.commissioned_status_counts).toEqual({
    commissioned: 2273,
    not_commissioned: 5981,
    unknown: 15686,
  });
});

test("Batch 544 evidence is citation-linked, uncertainty-preserving, and private-value free", () => {
  const bundle = JSON.parse(evidence);
  expect(bundle).toMatchObject({ bundle_version: "1.0" });
  expect(bundle.sources).toHaveLength(6);
  expect(bundle.organizations).toHaveLength(1);
  expect(bundle.affiliations).toHaveLength(2);
  expect(bundle.claims).toHaveLength(7);
  expect(bundle.claims.flatMap((claim: { sources: unknown[] }) => claim.sources)).toHaveLength(14);
  expect(bundle.person_updates).toHaveLength(10);
  expect(bundle.research_attempts).toHaveLength(10);
  expect(bundle.claims.filter((claim: { claim_confidence: string }) => claim.claim_confidence === "confirmed")).toHaveLength(1);
  expect(bundle.claims.filter((claim: { claim_confidence: string }) => claim.claim_confidence === "high")).toHaveLength(2);
  expect(bundle.claims.filter((claim: { claim_confidence: string }) => claim.claim_confidence === "medium")).toHaveLength(3);
  expect(bundle.claims.filter((claim: { claim_confidence: string }) => claim.claim_confidence === "conflicting")).toHaveLength(1);
  expect(evidence).toContain("No reliable pre-OSS employer has yet been identified");
  expect(evidence).toContain("unrelated name and all full identifiers are withheld");
  expect(evidence).not.toMatch(/serial_number|service_number/);
  expect(evidence).not.toMatch(/\b\d{8}\b/);
});

test("Batch 544 gives every public claim an inspectable citation", () => {
  for (const id of [
    "9176d1b5-5092-5cd5-9602-f8892227960c",
    "9943a542-2744-5468-9e5a-fb73dde9fa04",
    "8b53835a-2229-5628-9934-118ef4e52c08",
  ]) {
    const person = profile(id);
    for (const claim of person.claims) {
      expect(claim.sources.length).toBeGreaterThan(0);
      expect(claim.sources.every((link: { source: { stable_url: string } }) => Boolean(link.source.stable_url))).toBe(true);
    }
  }
});

test("Batch 544 organization route renders the qualified Civic Concerts relationship", async ({ page }) => {
  const person = profile("9176d1b5-5092-5cd5-9602-f8892227960c");
  const organizationId = person.other_pre_oss_affiliations[0].organization_id;
  await page.goto(`./organizations/${organizationId}/`);
  await expect(page.locator("h1")).toContainText("Civic Concert Service");
  await expect(page.locator("body")).toContainText("Harlowe F Dean Jr.");
  await expect(page.locator("body")).toContainText("medium documented pre-OSS");
});

test.describe("Batch 544 direct profile routes", () => {
  for (const [id, name] of cohort) {
    test(`${name} ${id.slice(0, 8)} renders from a direct route`, async ({ page }) => {
      await page.goto(`./people/${id}/`);
      await expect(page.locator("h1")).toContainText(name);
      await expect(page.locator("body")).toContainText("Box174");
      await expect(page.locator("body")).toContainText("Archival-review priority");
    });
  }
});
