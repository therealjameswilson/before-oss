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
    "../../research/evidence-pages-one-hundred-and-eight-and-nine-richard-a-day-jr-through-louis-r-dealva-pathways_batch-543_2026-09-15.json",
    import.meta.url,
  ),
  "utf8",
);
const profile = (id: string) =>
  people.find((person: { person_id: string }) => person.person_id === id);

const cohort = [
  ["fd8a5fef-2c4f-542e-a708-995d8c0def35", "Richard A Day Jr.", "e5e53ef0-656a-5af2-b606-6e343bf006bc", 108, "173", false],
  ["83e3d768-87c7-518a-89b1-bd5f8253f9bf", "James L Dayley", "64954567-0bd3-5a8a-b8a4-17a4e4ae5b0c", 108, "173", true],
  ["3af52492-78be-5737-b950-d63fbd35608a", "Arthur Dayton", "bc1bd3b0-3251-52cc-a66c-7abed95ee925", 108, "173", false],
  ["94b930b5-fa96-5013-abaf-6191756d1e5b", "Christine W Dayton", "f7e82781-1437-5975-87c8-f303479883c4", 109, "173", false],
  ["a13e0ddb-ef0c-5520-a181-beac97c536b4", "Thomas P Dazey", "54a4305d-f482-5bb8-b469-0075e8d5bbd5", 109, "173", false],
  ["944013b7-d00b-5acb-8d3b-577544331e8a", "Bruce E Deahl", "2b8758c1-ca2c-5ee4-90cc-2cab2f455867", 109, "174", false],
  ["eab9b93f-a3aa-5f4d-a85a-079c844c987e", "Bruce E Deahl", "58e1a999-211d-592c-a7a6-3c1d548f6aa5", 109, "174", true],
  ["47bdf9b2-f5d7-5a45-b01a-c3fd06324d63", "Nicholas L Deak", "2cda1c00-ce98-51df-9475-223a676d38c0", 109, "174", true],
  ["dae257b9-9e38-5440-a100-4505f03bbbcd", "Ada E Deakman", "672008f4-5bed-52fd-8115-1459fdc9399a", 109, "174", false],
  ["f1441818-a9f7-507f-8fb2-0e95da6fc755", "Louis R DeAlva", "ab41df43-34e9-5532-8b74-9b3451031ceb", 109, "174", true],
] as const;

test("Batch 543 preserves ten rows across pages 108-109 and masks four private fields", () => {
  for (const [id, name, sourceRecordId, page, box, hasPrivateIdentifier] of cohort) {
    const person = profile(id);
    expect(person).toMatchObject({ display_name: name });
    const sourceRecord = person.source_records.find(
      (record: { source_record_id: string }) => record.source_record_id === sourceRecordId,
    );
    expect(sourceRecord).toMatchObject({
      archive_location: "230/86/29/06",
      box,
      pdf_page: page,
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

test("Batch 543 confirms James Dayley and publishes student status without inventing a school", () => {
  const person = profile("83e3d768-87c7-518a-89b1-bd5f8253f9bf");
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
    role_title: "Student",
    occupation: "Student",
    relationship_type: "student",
    end_date: "1943-06-17",
    temporal_basis: "strongly_date_bounded",
    identity_confidence: "confirmed",
    claim_confidence: "medium",
    publication_status: "publish_qualified",
  });
  expect(person.claims).toHaveLength(2);
  expect(JSON.stringify(person)).not.toContain("University");
});

test("Batch 543 keeps the two Bruce Deahl rows separate and explicitly linked for review", () => {
  const ranked = profile("944013b7-d00b-5acb-8d3b-577544331e8a");
  const unranked = profile("eab9b93f-a3aa-5f4d-a85a-079c844c987e");
  expect(ranked.person_id).not.toBe(unranked.person_id);
  expect(ranked.possible_duplicate_group).toBeTruthy();
  expect(unranked.possible_duplicate_group).toBe(ranked.possible_duplicate_group);
  expect(ranked).toMatchObject({
    identity_status: "ambiguous",
    personnel_category: "commissioned_army_officer",
    commissioned_officer: true,
    research_status: "requires_archival_review",
  });
  expect(ranked.source_records[0]).toMatchObject({ rank_as_indexed: "2nd Lt", serial_masked: null });
  expect(unranked).toMatchObject({
    identity_status: "ambiguous",
    personnel_category: "unknown_or_indeterminate",
    commissioned_officer: null,
    research_status: "requires_archival_review",
  });
  expect(unranked.source_records[0].rank_as_indexed).toBeNull();
  expect(unranked.source_records[0].serial_masked).toMatch(/^•+\d{4}$/);
  for (const person of [ranked, unranked]) {
    expect(person.archival_file).toMatchObject({ review_priority: "critical" });
    expect(person.immediate_pre_oss_affiliations).toEqual([]);
    expect(person.last_civilian_pre_service).toEqual([]);
    expect(person.other_pre_oss_affiliations).toEqual([]);
    expect(person.claims).toEqual([]);
  }
});

test("Batch 543 preserves Nicholas Deak's best-supported employer and conflicting chronology", () => {
  const person = profile("47bdf9b2-f5d7-5a45-b01a-c3fd06324d63");
  expect(person).toMatchObject({
    identity_status: "high_confidence",
    personnel_category: "commissioned_army_officer",
    commissioned_officer: true,
    research_status: "conflicting_sources",
    research_attempt_count: 5,
    manual_review_required: true,
  });
  expect(person.source_records[0]).toMatchObject({ rank_as_indexed: "Capt", notes_as_indexed: "also AS" });
  expect(person.archival_file).toMatchObject({ review_priority: "high" });
  expect(person.immediate_pre_oss_affiliations).toEqual([]);
  expect(person.last_civilian_pre_service).toHaveLength(2);
  const korody = person.last_civilian_pre_service.find(
    (item: { canonical_organization: string }) => item.canonical_organization === "Korody and Co., Inc.",
  );
  const disputed = person.last_civilian_pre_service.find(
    (item: { canonical_organization: string }) => item.canonical_organization === "Deak & Co. (reported prewar firm)",
  );
  expect(korody).toMatchObject({
    role_title: "Vice-president and financial advisor, part-time",
    start_date: "1941-09",
    end_date: "1942-12",
    temporal_basis: "strongly_date_bounded",
    identity_confidence: "high_confidence",
    claim_confidence: "high",
    publication_status: "publish_qualified",
  });
  expect(disputed).toMatchObject({
    relationship_type: "self_employment",
    claim_confidence: "conflicting",
    publication_status: "conflicting",
  });
  expect(person.other_pre_oss_affiliations).toHaveLength(2);
  expect(person.other_pre_oss_affiliations.map((item: { canonical_organization: string }) => item.canonical_organization).sort()).toEqual([
    "City College of New York",
    "Perkiomen School",
  ]);
  expect(person.claims).toHaveLength(5);
  expect(person.claims.filter((claim: { claim_confidence: string }) => claim.claim_confidence === "conflicting")).toHaveLength(1);
});

test("Batch 543 withholds the Arthur R Dayton lead until Box 173 supplies an identity bridge", () => {
  const person = profile("3af52492-78be-5737-b950-d63fbd35608a");
  expect(person).toMatchObject({
    identity_status: "unresolved",
    research_status: "requires_archival_review",
    research_attempt_count: 5,
    manual_review_required: true,
  });
  expect(person.archival_file).toMatchObject({ review_priority: "critical" });
  expect(person.immediate_pre_oss_affiliations).toEqual([]);
  expect(person.last_civilian_pre_service).toEqual([]);
  expect(person.other_pre_oss_affiliations).toEqual([]);
  expect(person.claims).toEqual([]);
  expect(person.identity_evidence).toContain("plausible lead");
  expect(person.next_action).toContain("U.S. Steel was described as OSS cover");
  const bundle = JSON.parse(evidence);
  expect(bundle.affiliations.find((item: { key: string }) => item.key === "arthur-r-dayton-unnamed-export-business-b543")).toMatchObject({
    organization_key: null,
    organization_name_as_found: "an unnamed California export business",
    claim_confidence: "low",
    publication_status: "withheld_low_confidence",
  });
});

test("Batch 543 leaves the remaining unresolved profiles with explicit archival guidance", () => {
  const noResultIds = [
    "fd8a5fef-2c4f-542e-a708-995d8c0def35",
    "94b930b5-fa96-5013-abaf-6191756d1e5b",
    "a13e0ddb-ef0c-5520-a181-beac97c536b4",
    "dae257b9-9e38-5440-a100-4505f03bbbcd",
  ];
  for (const id of noResultIds) {
    const person = profile(id);
    expect(person).toMatchObject({
      identity_status: "unresolved",
      research_status: "no_reliable_result_after_protocol",
      research_attempt_count: 5,
      manual_review_required: true,
    });
    expect(person.archival_file).toMatchObject({ review_priority: "critical" });
    expect(person.claims).toEqual([]);
    expect(person.next_action).toContain("No reliable pre-OSS employer has yet been identified");
  }
  const deAlva = profile("f1441818-a9f7-507f-8fb2-0e95da6fc755");
  expect(deAlva).toMatchObject({ identity_status: "unresolved", research_status: "requires_archival_review" });
  expect(deAlva.claims).toEqual([]);
  expect(deAlva.next_action).toContain("Alameda County memorial candidate");
});

test("Batch 543 advances attempted and archival coverage without overstating verified employers", () => {
  expect(stats).toMatchObject({
    source_rows: 23978,
    person_entities: 23940,
    possible_duplicate_groups: 247,
    research_attempted_people: 5198,
    research_attempt_percent: 21.7126,
    verified_affiliation_people: 571,
    verified_affiliation_percent: 2.3851,
    verified_employer_people: 253,
    verified_employer_percent: 1.0568,
    archival_review_assessed_people: 5153,
    archival_review_percent: 21.5246,
    public_sources: 3466,
    published_claims: 4069,
  });
  expect(stats.research_status_counts).toMatchObject({
    conflicting_sources: 101,
    no_reliable_result_after_protocol: 180,
    not_started: 18742,
    occupation_only_found: 954,
    requires_archival_review: 3123,
  });
  expect(stats.identity_status_counts).toMatchObject({
    ambiguous: 245,
    confirmed: 1065,
    high_confidence: 711,
    unresolved: 21658,
  });
  expect(stats.commissioned_status_counts).toEqual({
    commissioned: 2273,
    not_commissioned: 5979,
    unknown: 15688,
  });
});

test("Batch 543 evidence is citation-linked, uncertainty-preserving, and private-value free", () => {
  const bundle = JSON.parse(evidence);
  expect(bundle).toMatchObject({ bundle_version: "1.0" });
  expect(bundle.sources).toHaveLength(6);
  expect(bundle.organizations).toHaveLength(4);
  expect(bundle.affiliations).toHaveLength(6);
  expect(bundle.claims).toHaveLength(9);
  expect(bundle.claims.flatMap((claim: { sources: unknown[] }) => claim.sources)).toHaveLength(16);
  expect(bundle.person_updates).toHaveLength(10);
  expect(bundle.research_attempts).toHaveLength(10);
  expect(bundle.claims.filter((claim: { claim_confidence: string }) => claim.claim_confidence === "confirmed")).toHaveLength(1);
  expect(bundle.claims.filter((claim: { claim_confidence: string }) => claim.claim_confidence === "high")).toHaveLength(2);
  expect(bundle.claims.filter((claim: { claim_confidence: string }) => claim.claim_confidence === "medium")).toHaveLength(3);
  expect(bundle.claims.filter((claim: { claim_confidence: string }) => claim.claim_confidence === "low")).toHaveLength(2);
  expect(bundle.claims.filter((claim: { claim_confidence: string }) => claim.claim_confidence === "conflicting")).toHaveLength(1);
  expect(evidence).toContain("U.S. Steel was Dayton's OSS commercial cover");
  expect(evidence).toContain("UPI's prewar-company account");
  expect(evidence).not.toMatch(/serial_number|service_number/);
  expect(evidence).not.toMatch(/\b\d{8}\b/);
});

test("Batch 543 gives every public claim an inspectable citation", () => {
  for (const id of [
    "83e3d768-87c7-518a-89b1-bd5f8253f9bf",
    "47bdf9b2-f5d7-5a45-b01a-c3fd06324d63",
  ]) {
    const person = profile(id);
    for (const claim of person.claims) {
      expect(claim.sources.length).toBeGreaterThan(0);
      expect(claim.sources.every((link: { source: { stable_url: string } }) => Boolean(link.source.stable_url))).toBe(true);
    }
  }
});

test("Batch 543 organization route renders the qualified Korody relationship", async ({ page }) => {
  const person = profile("47bdf9b2-f5d7-5a45-b01a-c3fd06324d63");
  const organizationId = person.last_civilian_pre_service.find(
    (item: { canonical_organization: string }) => item.canonical_organization === "Korody and Co., Inc.",
  ).organization_id;
  await page.goto(`./organizations/${organizationId}/`);
  await expect(page.locator("h1")).toContainText("Korody and Co., Inc.");
  await expect(page.locator("body")).toContainText("Nicholas L Deak");
  await expect(page.locator("body")).toContainText("high strongly date bounded");
});

test.describe("Batch 543 direct profile routes", () => {
  for (const [id, name, , , box] of cohort) {
    test(`${name} ${id.slice(0, 8)} renders from a direct route`, async ({ page }) => {
      await page.goto(`./people/${id}/`);
      await expect(page.locator("h1")).toContainText(name);
      await expect(page.locator("body")).toContainText(`Box${box}`);
      await expect(page.locator("body")).toContainText("Archival-review priority");
    });
  }
});
