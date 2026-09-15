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
    "../../research/evidence-page-one-hundred-and-eleven-e-e-dehaan-through-john-b-deik-pathways_batch-553_2026-09-15.json",
    import.meta.url,
  ),
  "utf8",
);
const profile = (id: string) =>
  people.find((person: { person_id: string }) => person.person_id === id);

const cohort = [
  ["a3086222-627a-526a-9a1e-4e19f2045adc", "E E Dehaan", "fcd8ae50-20dd-5c6a-a4a3-b939fb5262c1", false],
  ["5b8dd8f1-63ef-5313-9c3a-8763a378cc65", "Del Dehart", "62bca81d-5348-579e-a644-f89c1289ca36", false],
  ["af731495-ba07-5d5c-87d1-b0457aba2e5b", "Hazel A Dehart", "dca89369-ff8d-59ee-aba0-e6c6cf783da9", false],
  ["6876c90d-006b-54b2-91f4-6305d2b7f10c", "Hilda A Dehart", "a9c2b65d-8be9-5de7-9279-a8ba2ec2e40f", false],
  ["7b8c2b0b-7696-5bfd-bdc0-9885ef132136", "Hendrik Dehartog", "650994fe-b009-5221-b903-efdf545208cd", false],
  ["99c84518-7014-5ffe-81e8-d4669d578eee", "Gwendolyn M DeHaviland", "445eac62-a1cc-53f9-a473-dcb757331cfb", false],
  ["0db372bb-63b7-52b0-bdd4-6703dc46af3e", "Rae W Dehncke", "3acdacd7-e2d7-57f8-9a48-a072f9012ea4", true],
  ["3e3f9b4f-d0eb-54ac-8f44-004e935e87e2", "Bernard U DeHosson", "2fea157d-6447-5615-80b4-cc6f74eb24de", false],
  ["0e1a7376-6dec-5433-8833-2a2456092eb2", "Herbert G Deignan", "abb77f65-3127-543e-9ab2-6697c3c4c2a2", false],
  ["3352925b-1445-5dbe-b0cf-341d66f152f2", "John B Deik", "d5736d24-a310-5577-aaf5-53371d4618a7", true],
] as const;

test("Batch 553 preserves page 111 rows 6-15 and masks two private fields", () => {
  for (const [id, name, sourceRecordId, hasPrivateIdentifier] of cohort) {
    const person = profile(id);
    expect(person).toMatchObject({ display_name: name, research_attempt_count: 5 });
    const sourceRecord = person.source_records.find(
      (record: { source_record_id: string }) => record.source_record_id === sourceRecordId,
    );
    expect(sourceRecord).toMatchObject({
      archive_location: "230/86/29/07",
      box: "177",
      pdf_page: 111,
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

test("Batch 553 publishes Herbert G Deignan's museum pathway without forcing personnel status", () => {
  const person = profile("0e1a7376-6dec-5433-8833-2a2456092eb2");
  expect(person).toMatchObject({
    identity_status: "high_confidence",
    personnel_category: "unknown_or_indeterminate",
    commissioned_officer: null,
    research_status: "verified_employer_found",
    manual_review_required: true,
  });
  expect(person.immediate_pre_oss_affiliations).toHaveLength(1);
  expect(person.immediate_pre_oss_affiliations[0]).toMatchObject({
    canonical_organization: "United States National Museum, Division of Birds",
    role_title: "Associate Curator",
    relationship_type: "employment",
    immediate_pre_oss: true,
    last_civilian_pre_service: true,
    temporal_basis: "strongly_date_bounded",
    identity_confidence: "high_confidence",
    claim_confidence: "high",
  });
  expect(person.last_civilian_pre_service).toHaveLength(1);
  expect(person.other_pre_oss_affiliations).toHaveLength(1);
  expect(person.other_pre_oss_affiliations[0]).toMatchObject({
    canonical_organization: "Prince Royal's College",
    role_title: "Master",
    occupation: "teacher",
    relationship_type: "employment",
    temporal_basis: "documented_prewar",
    claim_confidence: "high",
  });
  expect(person.claims).toHaveLength(3);
  expect(JSON.stringify(person)).toContain("Assistant Curator");
  expect(JSON.stringify(person)).toContain("Associate Curator");
});

test("Batch 553 qualifies Bernard U DeHosson's banking occupation without inventing a bank", () => {
  const person = profile("3e3f9b4f-d0eb-54ac-8f44-004e935e87e2");
  expect(person).toMatchObject({
    identity_status: "probable",
    research_status: "occupation_only_found",
    manual_review_required: true,
  });
  expect(person.immediate_pre_oss_affiliations).toEqual([]);
  expect(person.last_civilian_pre_service).toEqual([]);
  expect(person.other_pre_oss_affiliations).toHaveLength(1);
  expect(person.other_pre_oss_affiliations[0]).toMatchObject({
    canonical_organization: null,
    occupation: "banking",
    relationship_type: "unknown",
    temporal_basis: "documented_prewar",
    identity_confidence: "probable",
    claim_confidence: "medium",
    publication_status: "publish_qualified",
  });
  expect(person.claims).toHaveLength(2);
  expect(JSON.stringify(person)).toContain("no bank");
  expect(JSON.stringify(person)).not.toContain("Sherwood");
});

test("Batch 553 confirms John B Deik's Army occupation without inventing an employer", () => {
  const person = profile("3352925b-1445-5dbe-b0cf-341d66f152f2");
  expect(person).toMatchObject({
    identity_status: "confirmed",
    personnel_category: "enlisted_army_personnel",
    commissioned_officer: false,
    research_status: "occupation_only_found",
  });
  expect(person.immediate_pre_oss_affiliations).toEqual([]);
  expect(person.last_civilian_pre_service).toEqual([]);
  expect(person.other_pre_oss_affiliations).toHaveLength(1);
  expect(person.other_pre_oss_affiliations[0]).toMatchObject({
    canonical_organization: null,
    occupation: "Managers and officials, n.e.c.",
    end_date: "1943-02-13",
    relationship_type: "unknown",
    temporal_basis: "strongly_date_bounded",
    identity_confidence: "confirmed",
    claim_confidence: "medium",
  });
  expect(person.claims).toHaveLength(2);
  expect(JSON.stringify(person)).toContain("no employer is named");
});

test("Batch 553 exposes Rae W Dehncke's identifier conflict without adopting Army fields", () => {
  const person = profile("0db372bb-63b7-52b0-bdd4-6703dc46af3e");
  expect(person).toMatchObject({
    identity_status: "conflicting",
    personnel_category: "unknown_or_indeterminate",
    commissioned_officer: null,
    research_status: "needs_identity_review",
    manual_review_required: true,
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
  expect(person.identity_evidence).toContain("different protected identifier");
  expect(JSON.stringify(person)).toContain("none of that row's date, occupation, branch or rank fields is assigned");
});

test("Batch 553 leaves six completed-protocol profiles unresolved with Box 177 guidance", () => {
  const unresolvedIds = cohort.slice(0, 6).map(([id]) => id);
  for (const id of unresolvedIds) {
    const person = profile(id);
    expect(person).toMatchObject({
      identity_status: "unresolved",
      personnel_category: "unknown_or_indeterminate",
      commissioned_officer: null,
      research_status: "no_reliable_result_after_protocol",
      research_attempt_count: 5,
      manual_review_required: true,
    });
    expect(person.archival_file).toMatchObject({ box: "177", review_priority: "critical" });
    expect(person.immediate_pre_oss_affiliations).toEqual([]);
    expect(person.last_civilian_pre_service).toEqual([]);
    expect(person.other_pre_oss_affiliations).toEqual([]);
    expect(person.claims).toEqual([]);
    expect(person.next_action).toContain(
      "No reliable pre-OSS employer has yet been identified in the accessible sources reviewed.",
    );
  }
});

test("Batch 553 advances research and employer coverage with exact denominators", () => {
  expect(stats).toMatchObject({
    source_rows: 23978,
    person_entities: 23940,
    possible_duplicate_groups: 248,
    research_attempted_people: 5298,
    research_attempt_percent: 22.1303,
    verified_affiliation_people: 579,
    verified_affiliation_percent: 2.4185,
    verified_employer_people: 257,
    verified_employer_percent: 1.0735,
    archival_review_assessed_people: 5253,
    archival_review_percent: 21.9424,
    public_sources: 3535,
    published_claims: 4164,
  });
  expect(stats.research_status_counts).toMatchObject({
    completed: 146,
    documented_prewar_employer_found: 106,
    needs_identity_review: 294,
    no_reliable_result_after_protocol: 207,
    not_started: 18642,
    occupation_only_found: 975,
    requires_archival_review: 3150,
    verified_employer_found: 240,
  });
  expect(stats.identity_status_counts).toEqual({
    ambiguous: 251,
    confirmed: 1086,
    conflicting: 112,
    high_confidence: 723,
    probable: 167,
    unresolved: 21601,
  });
  expect(stats.commissioned_status_counts).toEqual({
    commissioned: 2277,
    not_commissioned: 5997,
    unknown: 15666,
  });
});

test("Batch 553 evidence is citation-linked, qualified, and private-value free", () => {
  const bundle = JSON.parse(evidence);
  expect(bundle).toMatchObject({ bundle_version: "1.0" });
  expect(bundle.sources).toHaveLength(7);
  expect(bundle.organizations).toHaveLength(2);
  expect(bundle.affiliations).toHaveLength(4);
  expect(bundle.claims).toHaveLength(8);
  expect(bundle.claims.flatMap((claim: { sources: unknown[] }) => claim.sources)).toHaveLength(16);
  expect(bundle.person_updates).toHaveLength(10);
  expect(bundle.research_attempts).toHaveLength(20);
  expect(bundle.claims.filter((claim: { claim_confidence: string }) => claim.claim_confidence === "confirmed")).toHaveLength(1);
  expect(bundle.claims.filter((claim: { claim_confidence: string }) => claim.claim_confidence === "high")).toHaveLength(3);
  expect(bundle.claims.filter((claim: { claim_confidence: string }) => claim.claim_confidence === "medium")).toHaveLength(3);
  expect(bundle.claims.filter((claim: { claim_confidence: string }) => claim.claim_confidence === "conflicting")).toHaveLength(1);
  expect(evidence).toContain("No reliable pre-OSS employer");
  expect(evidence).toContain("no Army identity, occupation or unit is assigned");
  expect(evidence).not.toContain("Sherwood");
  expect(evidence).not.toMatch(/serial_number|service_number|\b\d{8}\b/);
});

test("Batch 553 gives every public or conflicting claim an inspectable citation", () => {
  for (const [id] of cohort) {
    const person = profile(id);
    for (const claim of person.claims) {
      expect(claim.sources.length).toBeGreaterThan(0);
      expect(claim.sources.every(
        (link: { source: { stable_url: string } }) => Boolean(link.source.stable_url),
      )).toBe(true);
    }
  }
});

test.describe("Batch 553 direct profile routes", () => {
  for (const [id, name] of cohort) {
    test(`${name} ${id.slice(0, 8)} renders from a direct route`, async ({ page }) => {
      await page.goto(`./people/${id}/`);
      await expect(page.locator("h1")).toContainText(name);
      await expect(page.locator("body")).toContainText("Box177");
      await expect(page.locator("body")).toContainText("Archival-review priority");
    });
  }
});
