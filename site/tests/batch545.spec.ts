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
    "../../research/evidence-page-one-hundred-and-nine-john-j-deangelis-through-daniel-debardeleben-pathways_batch-545_2026-09-15.json",
    import.meta.url,
  ),
  "utf8",
);
const profile = (id: string) =>
  people.find((person: { person_id: string }) => person.person_id === id);

const cohort = [
  ["d593feba-7881-5a10-a0e5-21f9cd160905", "John J Deangelis", "1699c1c7-9e86-5f60-acbc-1107cad93b28", "174", true],
  ["5384720e-fa95-54b8-b0ed-61ca7e9dd005", "Peter L Deangelis", "751555d4-c204-5177-b4df-fef0332dbd60", "174", true],
  ["2174b0f7-dabd-59af-9101-43fbed2aa4c7", "Rita E DeAngelis", "3212a4c8-b775-5263-8499-1d2084a9fec7", "174", false],
  ["e3ed20fb-6b40-5139-87b0-281802104daf", "Frances V Dearborn", "398bc349-a1c3-52eb-b8ef-d2a83d28267d", "174", true],
  ["6806ccc5-d88b-54b5-8d82-6b0b2e5530a1", "Fila R DeArellano", "bd280e1a-1895-50d2-abeb-859da1ae5c10", "175", false],
  ["32046bbe-c39c-5d11-aef4-a81edaaf4028", "Albin P Dearing", "6e10acfa-88e0-55f9-a20b-cf800285faa3", "175", true],
  ["28957e5f-5790-5ae4-a204-f0b9d95645e1", "Edward P Deason", "ae718c78-e82e-56c8-a50e-b4734e592135", "175", true],
  ["b45e9d39-de70-5245-a622-29487dee8454", "Felix R Deasonb", "dda658ca-3426-50f2-817f-25580bdbbefc", "175", true],
  ["c5e2679f-8ba1-58f5-b56f-39b5f2d32767", "David C Deaver", "c5a29510-f00f-5c9c-89ca-d516cf1473d3", "175", true],
  ["12c6802d-18ec-55e6-b114-2e9bf3aa255e", "Daniel Debardeleben", "3fea03bb-2dfc-56d0-87af-8749cbc98502", "175", false],
] as const;

test("Batch 545 preserves ten page-109 rows and masks seven private fields", () => {
  for (const [id, name, sourceRecordId, box, hasPrivateIdentifier] of cohort) {
    const person = profile(id);
    expect(person).toMatchObject({ display_name: name });
    const sourceRecord = person.source_records.find(
      (record: { source_record_id: string }) => record.source_record_id === sourceRecordId,
    );
    expect(sourceRecord).toMatchObject({
      archive_location: "230/86/29/06",
      box,
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

test("Batch 545 preserves both Deangelis identifier conflicts without naming other subjects", () => {
  for (const id of [
    "d593feba-7881-5a10-a0e5-21f9cd160905",
    "5384720e-fa95-54b8-b0ed-61ca7e9dd005",
  ]) {
    const person = profile(id);
    expect(person).toMatchObject({
      identity_status: "conflicting",
      research_status: "conflicting_sources",
      research_attempt_count: 4,
      manual_review_required: true,
    });
    expect(person.archival_file).toMatchObject({ review_priority: "critical" });
    expect(person.immediate_pre_oss_affiliations).toEqual([]);
    expect(person.last_civilian_pre_service).toEqual([]);
    expect(person.other_pre_oss_affiliations).toEqual([]);
    expect(person.claims).toHaveLength(1);
    expect(person.claims[0]).toMatchObject({
      claim_confidence: "conflicting",
      publication_status: "conflicting",
    });
    expect(JSON.stringify(person)).toContain("different surname");
    expect(JSON.stringify(person)).toContain("unrelated");
  }
});

test("Batch 545 keeps Frances Dearborn's Army occupation candidate visibly qualified", () => {
  const person = profile("e3ed20fb-6b40-5139-87b0-281802104daf");
  expect(person).toMatchObject({
    identity_status: "probable",
    personnel_category: "unknown_or_indeterminate",
    commissioned_officer: null,
    research_status: "requires_archival_review",
    research_attempt_count: 4,
    manual_review_required: true,
  });
  expect(person.archival_file).toMatchObject({ review_priority: "critical" });
  expect(person.immediate_pre_oss_affiliations).toEqual([]);
  expect(person.last_civilian_pre_service).toEqual([]);
  expect(person.other_pre_oss_affiliations).toHaveLength(1);
  expect(person.other_pre_oss_affiliations[0]).toMatchObject({
    organization_id: null,
    occupation: "Statistical clerks and compilers",
    relationship_type: "employment",
    end_date: "1943-05-08",
    temporal_basis: "strongly_date_bounded",
    identity_confidence: "probable",
    claim_confidence: "medium",
    publication_status: "publish_qualified",
  });
  expect(person.claims).toHaveLength(2);
  expect(person.next_action).toContain("Keep the statistical-clerk category qualified");
});

test("Batch 545 confirms Edward Deason and David Deaver but publishes student status only", () => {
  for (const [id, rank, date] of [
    ["28957e5f-5790-5ae4-a204-f0b9d95645e1", "Sgt", "1943-03-04"],
    ["c5e2679f-8ba1-58f5-b56f-39b5f2d32767", "Pfc", "1943-06-29"],
  ] as const) {
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
    expect(person.source_records[0].rank_as_indexed).toBe(rank);
    expect(person.immediate_pre_oss_affiliations).toEqual([]);
    expect(person.last_civilian_pre_service).toEqual([]);
    expect(person.other_pre_oss_affiliations).toHaveLength(1);
    expect(person.other_pre_oss_affiliations[0]).toMatchObject({
      organization_id: null,
      occupation: "Student",
      relationship_type: "student",
      end_date: date,
      temporal_basis: "strongly_date_bounded",
      identity_confidence: "confirmed",
      claim_confidence: "medium",
      publication_status: "publish_qualified",
    });
    expect(person.claims).toHaveLength(2);
    expect(person.next_action).toContain("names no institution or employer");
  }
});

test("Batch 545 documents Albin Dearing's high-confidence OSS identity without projecting his postwar firm backward", () => {
  const person = profile("32046bbe-c39c-5d11-aef4-a81edaaf4028");
  expect(person).toMatchObject({
    identity_status: "high_confidence",
    personnel_category: "unknown_or_indeterminate",
    commissioned_officer: null,
    research_status: "no_reliable_result_after_protocol",
    research_attempt_count: 4,
    manual_review_required: true,
  });
  expect(person.immediate_pre_oss_affiliations).toEqual([]);
  expect(person.last_civilian_pre_service).toEqual([]);
  expect(person.other_pre_oss_affiliations).toEqual([]);
  expect(person.claims).toHaveLength(2);
  expect(person.claims.every((claim: { claim_confidence: string }) => claim.claim_confidence === "high")).toBe(true);
  expect(JSON.stringify(person)).toContain("original OSS member");
  expect(person.next_action).toContain("Do not project the documented postwar firm backward");
});

test("Batch 545 documents Daniel DeBardeleben's high-confidence OSS SI identity without inventing employment", () => {
  const person = profile("12c6802d-18ec-55e6-b114-2e9bf3aa255e");
  expect(person).toMatchObject({
    identity_status: "high_confidence",
    personnel_category: "unknown_or_indeterminate",
    commissioned_officer: null,
    research_status: "no_reliable_result_after_protocol",
    research_attempt_count: 4,
    manual_review_required: true,
  });
  expect(person.immediate_pre_oss_affiliations).toEqual([]);
  expect(person.last_civilian_pre_service).toEqual([]);
  expect(person.other_pre_oss_affiliations).toEqual([]);
  expect(person.claims).toHaveLength(2);
  expect(person.claims.every((claim: { claim_confidence: string }) => claim.claim_confidence === "high")).toBe(true);
  expect(JSON.stringify(person)).toContain("Chief, SI");
  expect(person.next_action).toContain("No reliable pre-OSS employer has yet been identified");
});

test("Batch 545 preserves three dignified unresolved profiles and the printed Deasonb spelling", () => {
  for (const id of [
    "2174b0f7-dabd-59af-9101-43fbed2aa4c7",
    "6806ccc5-d88b-54b5-8d82-6b0b2e5530a1",
    "b45e9d39-de70-5245-a622-29487dee8454",
  ]) {
    const person = profile(id);
    expect(person).toMatchObject({
      identity_status: "unresolved",
      research_status: "no_reliable_result_after_protocol",
      research_attempt_count: 4,
      manual_review_required: true,
    });
    expect(person.claims).toEqual([]);
    expect(person.next_action).toContain("No reliable pre-OSS employer has yet been identified");
  }
  const felix = profile("b45e9d39-de70-5245-a622-29487dee8454");
  expect(felix.display_name).toBe("Felix R Deasonb");
  expect(felix.name_variants).toContain("Felix R Deason (search alias only)");
});

test("Batch 545 advances attempted and archival coverage without overstating verified coverage", () => {
  expect(stats).toMatchObject({
    source_rows: 23978,
    person_entities: 23940,
    possible_duplicate_groups: 247,
    research_attempted_people: 5218,
    research_attempt_percent: 21.7962,
    verified_affiliation_people: 571,
    verified_affiliation_percent: 2.3851,
    verified_employer_people: 253,
    verified_employer_percent: 1.0568,
    archival_review_assessed_people: 5173,
    archival_review_percent: 21.6082,
    public_sources: 3479,
    published_claims: 4088,
  });
  expect(stats.research_status_counts).toMatchObject({
    conflicting_sources: 104,
    documented_prewar_employer_found: 103,
    no_reliable_result_after_protocol: 186,
    not_started: 18722,
    occupation_only_found: 957,
    requires_archival_review: 3130,
  });
  expect(stats.identity_status_counts).toMatchObject({
    ambiguous: 246,
    confirmed: 1068,
    conflicting: 104,
    high_confidence: 713,
    probable: 162,
    unresolved: 21647,
  });
  expect(stats.commissioned_status_counts).toEqual({
    commissioned: 2273,
    not_commissioned: 5981,
    unknown: 15686,
  });
});

test("Batch 545 evidence is citation-linked, uncertainty-preserving, and private-value free", () => {
  const bundle = JSON.parse(evidence);
  expect(bundle).toMatchObject({ bundle_version: "1.0" });
  expect(bundle.sources).toHaveLength(7);
  expect(bundle.organizations).toHaveLength(0);
  expect(bundle.affiliations).toHaveLength(3);
  expect(bundle.claims).toHaveLength(12);
  expect(bundle.claims.flatMap((claim: { sources: unknown[] }) => claim.sources)).toHaveLength(26);
  expect(bundle.person_updates).toHaveLength(10);
  expect(bundle.research_attempts).toHaveLength(10);
  expect(bundle.claims.filter((claim: { claim_confidence: string }) => claim.claim_confidence === "confirmed")).toHaveLength(2);
  expect(bundle.claims.filter((claim: { claim_confidence: string }) => claim.claim_confidence === "high")).toHaveLength(4);
  expect(bundle.claims.filter((claim: { claim_confidence: string }) => claim.claim_confidence === "medium")).toHaveLength(4);
  expect(bundle.claims.filter((claim: { claim_confidence: string }) => claim.claim_confidence === "conflicting")).toHaveLength(2);
  expect(evidence).toContain("No reliable pre-OSS employer has yet been identified");
  expect(evidence).toContain("unrelated identity");
  expect(evidence).not.toMatch(/serial_number|service_number|matched_name/);
  expect(evidence).not.toContain("jessie-lynne.kerr@");
  expect(evidence).not.toContain("Stockton St.");
});

test("Batch 545 gives every public claim an inspectable citation", () => {
  for (const id of [
    "d593feba-7881-5a10-a0e5-21f9cd160905",
    "5384720e-fa95-54b8-b0ed-61ca7e9dd005",
    "e3ed20fb-6b40-5139-87b0-281802104daf",
    "32046bbe-c39c-5d11-aef4-a81edaaf4028",
    "28957e5f-5790-5ae4-a204-f0b9d95645e1",
    "c5e2679f-8ba1-58f5-b56f-39b5f2d32767",
    "12c6802d-18ec-55e6-b114-2e9bf3aa255e",
  ]) {
    const person = profile(id);
    for (const claim of person.claims) {
      expect(claim.sources.length).toBeGreaterThan(0);
      expect(claim.sources.every((link: { source: { stable_url: string } }) => Boolean(link.source.stable_url))).toBe(true);
    }
  }
});

test.describe("Batch 545 direct profile routes", () => {
  for (const [id, name, , box] of cohort) {
    test(`${name} ${id.slice(0, 8)} renders from a direct route`, async ({ page }) => {
      await page.goto(`./people/${id}/`);
      await expect(page.locator("h1")).toContainText(name);
      await expect(page.locator("body")).toContainText(`Box${box}`);
      await expect(page.locator("body")).toContainText("Archival-review priority");
    });
  }
});
