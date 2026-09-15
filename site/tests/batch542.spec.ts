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
    "../../research/evidence-page-one-hundred-and-eight-chiles-w-dawson-through-raymond-l-day-pathways_batch-542_2026-09-15.json",
    import.meta.url,
  ),
  "utf8",
);
const profile = (id: string) =>
  people.find((person: { person_id: string }) => person.person_id === id);

const cohort = [
  ["9be8756a-2b2b-5f9e-aee6-37a894146570", "Chiles W Dawson", "da59a4b0-8722-5ae5-bdef-84338e75fc78", false],
  ["a1882a5a-a0e4-5fb7-b58a-d65cea84624e", "Joseph T Dawson", "3e3f5f96-b6b9-5e75-a3f4-35a54842905f", true],
  ["9d6cb300-ba28-5184-ae54-e40fffe43bee", "Titus C Dawson", "4d5dea6f-8e99-54f0-96e9-23fdf48840cf", true],
  ["e79bd4e2-ab2f-5ff0-b962-4d6bd428e888", "Audrey S Day", "11260b41-2412-539f-9463-8fd77dac97b7", false],
  ["0b57fe91-acac-550e-9ca7-4d0edc25f7a5", "Cletis O Day", "df1d4ec8-c8da-5439-b320-4d4b57d6b9a1", true],
  ["47c88a9c-65e4-55a2-98e2-2ba6f87be968", "Elizabeth A Day", "2a625020-ef63-56b5-9c3c-139a30c8cb9b", false],
  ["2026b6aa-fd54-5136-9595-0af4cbd0a438", "Ernest A Day", "a5389ed2-66c0-57d8-be12-2ac3c30b2bb3", true],
  ["a954252e-6d05-5b22-bbc2-a56d7dd8cbf2", "Linard F Day", "bac21e19-8e8d-5b34-8970-6991743f9a81", true],
  ["16a4108c-eb0f-5e1b-b42a-5accfa4fc072", "Paul W Day", "01b2f540-e911-553c-a93e-2ce51102ab71", true],
  ["aa5fd8ce-e0f5-53a1-8d1e-9a0b5894e8ed", "Raymond L Day", "08ac71e9-321e-5e9e-abb8-c4ed29c4aa78", true],
] as const;

test("Batch 542 preserves ten page 108 rows and masks seven private fields", () => {
  for (const [id, name, sourceRecordId, hasPrivateIdentifier] of cohort) {
    const person = profile(id);
    expect(person).toMatchObject({ display_name: name });
    const sourceRecord = person.source_records.find(
      (record: { source_record_id: string }) => record.source_record_id === sourceRecordId,
    );
    expect(sourceRecord).toMatchObject({
      archive_location: "230/86/29/06",
      box: "173",
      pdf_page: 108,
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

test("Batch 542 confirms Joseph Turner Dawson and keeps three pathways distinct", () => {
  const person = profile("a1882a5a-a0e4-5fb7-b58a-d65cea84624e");
  expect(person).toMatchObject({
    identity_status: "confirmed",
    personnel_category: "commissioned_army_officer",
    commissioned_officer: true,
    research_status: "documented_prewar_employer_found",
    research_attempt_count: 4,
    manual_review_required: true,
  });
  expect(person.source_records[0]).toMatchObject({ rank_as_indexed: "Capt" });
  expect(person.archival_file).toMatchObject({ review_priority: "high" });
  expect(person.immediate_pre_oss_affiliations).toHaveLength(1);
  expect(person.immediate_pre_oss_affiliations[0]).toMatchObject({
    canonical_organization: "1st Infantry Division, United States Army",
    relationship_type: "military_assignment",
    immediate_pre_oss: true,
    last_civilian_pre_service: false,
    temporal_basis: "probable_immediate",
    claim_confidence: "medium",
    publication_status: "publish_qualified",
  });
  expect(person.last_civilian_pre_service).toHaveLength(1);
  expect(person.last_civilian_pre_service[0]).toMatchObject({
    canonical_organization: "Ren-War Oil Corporation",
    organization_name_as_found: "Renwar Oil Corp.",
    role_title: "geologist",
    relationship_type: "employment",
    start_date: "1938",
    end_date: "1941-05",
    immediate_pre_oss: false,
    last_civilian_pre_service: true,
    temporal_basis: "strongly_date_bounded",
    claim_confidence: "medium",
    publication_status: "publish_qualified",
  });
  expect(person.other_pre_oss_affiliations).toHaveLength(1);
  expect(person.other_pre_oss_affiliations[0]).toMatchObject({
    canonical_organization: "Humble Oil and Refining Company",
    occupation: "geologist",
    temporal_basis: "documented_prewar",
    claim_confidence: "medium",
  });
  expect(person.claims).toHaveLength(4);
});

test("Batch 542 confirms three Army identities and publishes occupations only", () => {
  const expected = [
    ["9d6cb300-ba28-5184-ae54-e40fffe43bee", "Construction occupations, n. e. c.", "1942-05-05"],
    ["a954252e-6d05-5b22-bbc2-a56d7dd8cbf2", "Newsboys", "1942-02-04"],
    ["16a4108c-eb0f-5e1b-b42a-5accfa4fc072", "Chauffeurs and drivers, bus, taxi, truck, and tractor", "1943-09-04"],
  ];
  for (const [id, occupation, endDate] of expected) {
    const person = profile(id);
    expect(person).toMatchObject({
      identity_status: "confirmed",
      personnel_category: "enlisted_army_personnel",
      commissioned_officer: false,
      research_status: "occupation_only_found",
      research_attempt_count: 4,
      manual_review_required: false,
    });
    expect(person.archival_file).toMatchObject({ review_priority: "high" });
    expect(person.immediate_pre_oss_affiliations).toEqual([]);
    expect(person.last_civilian_pre_service).toEqual([]);
    expect(person.other_pre_oss_affiliations).toHaveLength(1);
    expect(person.other_pre_oss_affiliations[0]).toMatchObject({
      organization_id: null,
      occupation,
      end_date: endDate,
      relationship_type: "unknown",
      immediate_pre_oss: false,
      last_civilian_pre_service: false,
      temporal_basis: "strongly_date_bounded",
      identity_confidence: "confirmed",
      claim_confidence: "medium",
      publication_status: "publish_qualified",
    });
    expect(person.claims).toHaveLength(2);
  }
});

test("Batch 542 leaves six people unresolved with critical Box 173 guidance", () => {
  const unresolvedIds = [
    "9be8756a-2b2b-5f9e-aee6-37a894146570",
    "e79bd4e2-ab2f-5ff0-b962-4d6bd428e888",
    "0b57fe91-acac-550e-9ca7-4d0edc25f7a5",
    "47c88a9c-65e4-55a2-98e2-2ba6f87be968",
    "2026b6aa-fd54-5136-9595-0af4cbd0a438",
    "aa5fd8ce-e0f5-53a1-8d1e-9a0b5894e8ed",
  ];
  for (const id of unresolvedIds) {
    const person = profile(id);
    expect(person).toMatchObject({
      identity_status: "unresolved",
      personnel_category: "unknown_or_indeterminate",
      commissioned_officer: null,
      research_status: "no_reliable_result_after_protocol",
      research_attempt_count: 4,
      manual_review_required: true,
    });
    expect(person.archival_file).toMatchObject({ review_priority: "critical" });
    expect(person.immediate_pre_oss_affiliations).toEqual([]);
    expect(person.last_civilian_pre_service).toEqual([]);
    expect(person.other_pre_oss_affiliations).toEqual([]);
    expect(person.claims).toEqual([]);
    expect(person.next_action).toContain("No reliable pre-OSS employer has yet been identified");
  }
});

test("Batch 542 keeps medium Dawson pathways out of verified analytics", () => {
  expect(stats).toMatchObject({
    source_rows: 23978,
    person_entities: 23940,
    possible_duplicate_groups: 246,
    research_attempted_people: 5188,
    research_attempt_percent: 21.6708,
    verified_affiliation_people: 571,
    verified_affiliation_percent: 2.3851,
    verified_employer_people: 253,
    verified_employer_percent: 1.0568,
    archival_review_assessed_people: 5143,
    archival_review_percent: 21.4829,
    public_sources: 3461,
    published_claims: 4062,
  });
  expect(stats.research_status_counts).toMatchObject({
    documented_prewar_employer_found: 102,
    no_reliable_result_after_protocol: 176,
    not_started: 18752,
    occupation_only_found: 953,
  });
  expect(stats.identity_status_counts).toMatchObject({
    confirmed: 1064,
    unresolved: 21662,
  });
  expect(stats.commissioned_status_counts).toEqual({
    commissioned: 2273,
    not_commissioned: 5978,
    unknown: 15689,
  });
});

test("Batch 542 evidence is citation-linked, qualified, and private-value free", () => {
  const bundle = JSON.parse(evidence);
  expect(bundle).toMatchObject({ bundle_version: "1.0" });
  expect(bundle.sources).toHaveLength(7);
  expect(bundle.organizations).toHaveLength(3);
  expect(bundle.affiliations).toHaveLength(6);
  expect(bundle.claims).toHaveLength(10);
  expect(bundle.claims.flatMap((claim: { sources: unknown[] }) => claim.sources)).toHaveLength(23);
  expect(bundle.person_updates).toHaveLength(10);
  expect(bundle.research_attempts).toHaveLength(10);
  expect(bundle.claims.filter((claim: { claim_confidence: string }) => claim.claim_confidence === "confirmed")).toHaveLength(4);
  expect(bundle.claims.filter((claim: { claim_confidence: string }) => claim.claim_confidence === "medium")).toHaveLength(6);
  expect(evidence).toContain("Seven printed private values are withheld");
  expect(evidence).toContain("The dated biography is retained only as discovery context");
  expect(evidence).not.toMatch(/serial_number|service_number/);
  expect(evidence).not.toMatch(/\b\d{8}\b/);
});

test("Batch 542 gives every published claim an inspectable citation", () => {
  for (const id of [
    "a1882a5a-a0e4-5fb7-b58a-d65cea84624e",
    "9d6cb300-ba28-5184-ae54-e40fffe43bee",
    "a954252e-6d05-5b22-bbc2-a56d7dd8cbf2",
    "16a4108c-eb0f-5e1b-b42a-5accfa4fc072",
  ]) {
    const person = profile(id);
    for (const claim of person.claims) {
      expect(claim.sources.length).toBeGreaterThan(0);
      expect(claim.sources.every((link: { source: { stable_url: string } }) => Boolean(link.source.stable_url))).toBe(true);
    }
  }
});

test("Batch 542 preserves the Dawson discovery source as context only", () => {
  const person = profile("a1882a5a-a0e4-5fb7-b58a-d65cea84624e");
  const discoveryLinks = person.claims.flatMap((claim: { sources: Array<{ support_type: string; source: { source_quality: string } }> }) =>
    claim.sources.filter((link) => link.source.source_quality === "E_discovery_only"),
  );
  expect(discoveryLinks).toHaveLength(3);
  expect(discoveryLinks.every((link: { support_type: string }) => link.support_type === "context_only")).toBe(true);
  expect(person.claims.filter((claim: { claim_confidence: string }) => claim.claim_confidence === "medium")).toHaveLength(3);
});

test("Batch 542 organization route renders the qualified Ren-War relationship", async ({ page }) => {
  const person = profile("a1882a5a-a0e4-5fb7-b58a-d65cea84624e");
  const organizationId = person.last_civilian_pre_service[0].organization_id;
  await page.goto(`./organizations/${organizationId}/`);
  await expect(page.locator("h1")).toContainText("Ren-War Oil Corporation");
  await expect(page.locator("body")).toContainText("Joseph T Dawson");
  await expect(page.locator("body")).toContainText("medium strongly date bounded");
});

test.describe("Batch 542 direct profile routes", () => {
  for (const [id, name] of cohort) {
    test(`${name} ${id.slice(0, 8)} renders from a direct route`, async ({ page }) => {
      await page.goto(`./people/${id}/`);
      await expect(page.locator("h1")).toContainText(name);
      await expect(page.locator("body")).toContainText("Box173");
      await expect(page.locator("body")).toContainText("Archival-review priority");
    });
  }
});
