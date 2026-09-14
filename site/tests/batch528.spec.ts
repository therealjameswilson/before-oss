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
    "../../research/evidence-page-one-hundred-and-five-grant-darby-through-marceau-darques-pathways_batch-528_2026-09-14.json",
    import.meta.url,
  ),
  "utf8",
);
const profile = (id: string) =>
  people.find((person: { person_id: string }) => person.person_id === id);

const cohort = [
  ["092e6364-2cea-50c2-a37e-b376582c688e", "Grant Darby", "83e5d4ec-5631-5900-aa09-145174961aad", true],
  ["2213fc11-7a34-5f65-8433-fb45a8be5d2c", "Margaret M Darcy", "dd642d74-a795-5ee3-b749-3af033ad53b8", false],
  ["8c3e2259-35d1-59d2-b3e0-54b095a111df", "Edmund D'Areienzo", "109c7fa5-dab0-53b6-a6f9-cf461086795e", true],
  ["163d3423-2748-5814-85d4-4f666d150612", "Edmund Darey", "ee001158-dbb9-54b7-a2aa-c5514b03a5ad", false],
  ["f0baab81-9ac1-57ea-9810-5bded8e3043d", "Luigi D'Arezzo", "975e7526-7d92-5712-84d0-9018bcdbb539", true],
  ["42dc3525-d72f-5d37-b250-1c84cf2de812", "Caesar J Dario", "d683d4d6-818c-5b8a-9b10-91cb96423fd5", true],
  ["bfc9b825-1d5b-5873-8467-2526f1aed338", "Chris Dariotis", "d46ffc22-b483-5884-acf8-6d1ac77d0690", true],
  ["25035f7f-9c9a-54d6-b029-271e7097d6bb", "Joseph H Darlington", "1d78dbed-a5ba-538b-886a-d9d5f66025b2", false],
  ["1ae512a2-f86b-5ddd-92ef-ba396a1483e8", "Clinton B Darnell", "6063f5c9-6d6e-59c1-b9a8-14a406dacbd4", false],
  ["81ac3d7c-3e64-5001-bbab-2f91eb1e8ab9", "Marceau Darques", "9ca04b96-2adf-56dc-b364-23331160b5ad", false],
] as const;

test("Batch 528 preserves ten printed rows in Box 167 and masks private fields", () => {
  for (const [id, name, sourceRecordId, hasPrivateIdentifier] of cohort) {
    const person = profile(id);
    expect(person).toMatchObject({ display_name: name });
    const sourceRecord = person.source_records.find(
      (record: { source_record_id: string }) => record.source_record_id === sourceRecordId,
    );
    expect(sourceRecord).toMatchObject({
      archive_location: "230/86/29/05",
      box: "167",
      pdf_page: 105,
    });
    if (hasPrivateIdentifier) {
      expect(sourceRecord.serial_masked).toMatch(/^••••\d{2,4}$/);
    } else {
      expect(sourceRecord.serial_masked).toBeNull();
    }
    expect(JSON.stringify(person)).not.toMatch(
      /"serial_number"|"serial_number_raw"|"serial_number_normalized"/,
    );
  }
  expect(profile("bfc9b825-1d5b-5873-8467-2526f1aed338").source_records[0].rank_as_indexed).toBe("2nd Lt");
  expect(profile("81ac3d7c-3e64-5001-bbab-2f91eb1e8ab9").source_records[0]).toMatchObject({
    rank_as_indexed: "S/Lt",
    notes_as_indexed: "French",
  });
});

test("Batch 528 publishes three exact Army matches as entry-time occupations, not employers", () => {
  const expected = [
    ["8c3e2259-35d1-59d2-b3e0-54b095a111df", "Student", "student"],
    ["f0baab81-9ac1-57ea-9810-5bded8e3043d", "Occupations in manufacture of textiles, n.e.c.", "unknown"],
    ["42dc3525-d72f-5d37-b250-1c84cf2de812", "Bakery products occupations, production", "unknown"],
  ] as const;
  for (const [id, occupation, relationshipType] of expected) {
    const person = profile(id);
    expect(person).toMatchObject({
      identity_status: "confirmed",
      personnel_category: "enlisted_army_personnel",
      commissioned_officer: false,
      research_status: "occupation_only_found",
      research_attempt_count: 3,
    });
    expect(person.immediate_pre_oss_affiliations).toEqual([]);
    expect(person.last_civilian_pre_service).toEqual([]);
    expect(person.other_pre_oss_affiliations).toHaveLength(1);
    expect(person.other_pre_oss_affiliations[0]).toMatchObject({
      occupation,
      relationship_type: relationshipType,
      temporal_basis: "strongly_date_bounded",
      claim_confidence: "medium",
    });
  }
});

test("Batch 528 distinguishes Chris Dariotis's military, student and earlier employment paths", () => {
  const chris = profile("bfc9b825-1d5b-5873-8467-2526f1aed338");
  expect(chris).toMatchObject({
    identity_status: "high_confidence",
    personnel_category: "commissioned_army_officer",
    commissioned_officer: true,
    research_status: "documented_prewar_employer_found",
    research_attempt_count: 3,
  });
  expect(chris.immediate_pre_oss_affiliations).toHaveLength(1);
  expect(chris.immediate_pre_oss_affiliations[0]).toMatchObject({
    canonical_organization: "U.S. Army Air Corps",
    relationship_type: "military_assignment",
    temporal_basis: "probable_immediate",
    claim_confidence: "high",
  });
  expect(chris.last_civilian_pre_service).toEqual([]);
  expect(chris.other_pre_oss_affiliations).toEqual(
    expect.arrayContaining([
      expect.objectContaining({
        canonical_organization: "University of Washington",
        relationship_type: "student",
        claim_confidence: "high",
      }),
      expect.objectContaining({
        canonical_organization: "Imperial Linen Supply",
        relationship_type: "employment",
        claim_confidence: "medium",
      }),
    ]),
  );
});

test("Batch 528 keeps Grant Darby and Marceau Darques as archival leads, not employer findings", () => {
  const grant = profile("092e6364-2cea-50c2-a37e-b376582c688e");
  expect(grant).toMatchObject({
    identity_status: "high_confidence",
    research_status: "requires_archival_review",
    research_attempt_count: 3,
  });
  expect(grant.claims).toHaveLength(1);
  expect(grant.claims[0]).toMatchObject({ claim_type: "identity", claim_confidence: "high" });

  const marceau = profile("81ac3d7c-3e64-5001-bbab-2f91eb1e8ab9");
  expect(marceau).toMatchObject({
    identity_status: "high_confidence",
    personnel_category: "foreign_or_allied_military_personnel",
    commissioned_officer: null,
    allied_or_foreign_personnel: true,
    research_status: "requires_archival_review",
    research_attempt_count: 3,
  });
  expect(marceau.immediate_pre_oss_affiliations).toEqual([]);
  expect(marceau.last_civilian_pre_service).toEqual([]);
  expect(marceau.claims).toEqual(
    expect.arrayContaining([
      expect.objectContaining({ claim_type: "archival_file_status", claim_confidence: "high" }),
      expect.objectContaining({ claim_type: "identity", claim_confidence: "high" }),
    ]),
  );
});

test("Batch 528 leaves four unsupported identities visibly unresolved", () => {
  const ids = [
    "2213fc11-7a34-5f65-8433-fb45a8be5d2c",
    "163d3423-2748-5814-85d4-4f666d150612",
    "25035f7f-9c9a-54d6-b029-271e7097d6bb",
    "1ae512a2-f86b-5ddd-92ef-ba396a1483e8",
  ];
  for (const id of ids) {
    const person = profile(id);
    expect(person).toMatchObject({
      identity_status: "unresolved",
      research_status: "no_reliable_result_after_protocol",
      research_attempt_count: 3,
    });
    expect(person.immediate_pre_oss_affiliations).toEqual([]);
    expect(person.last_civilian_pre_service).toEqual([]);
    expect(person.other_pre_oss_affiliations).toEqual([]);
    expect(person.claims).toEqual([]);
    expect(person.next_action).toContain("No reliable pre-OSS employer has yet been identified");
  }
});

test("Batch 528 advances attempted and archival coverage with reproducible totals", () => {
  expect(stats).toMatchObject({
    source_rows: 23978,
    person_entities: 23940,
    research_attempted_people: 5048,
    research_attempt_percent: 21.086,
    verified_affiliation_people: 569,
    verified_affiliation_percent: 2.3768,
    verified_employer_people: 253,
    verified_employer_percent: 1.0568,
    archival_review_assessed_people: 5003,
    archival_review_percent: 20.8981,
    published_claims: 3982,
    public_sources: 3403,
  });
  expect(stats.research_status_counts).toMatchObject({
    not_started: 18892,
    no_reliable_result_after_protocol: 90,
    occupation_only_found: 923,
    documented_prewar_employer_found: 100,
    requires_archival_review: 3105,
  });
});

test("Batch 528 evidence is complete, citation-linked and private-value free", () => {
  const bundle = JSON.parse(evidence);
  expect(bundle).toMatchObject({ bundle_version: "1.0" });
  expect(bundle.sources).toHaveLength(6);
  expect(bundle.organizations).toHaveLength(3);
  expect(bundle.affiliations).toHaveLength(6);
  expect(bundle.claims).toHaveLength(13);
  expect(bundle.claims.reduce(
    (sum: number, claim: { sources: unknown[] }) => sum + claim.sources.length,
    0,
  )).toBe(22);
  expect(bundle.person_updates).toHaveLength(10);
  expect(bundle.research_attempts).toHaveLength(10);
  expect(bundle.claims.filter(
    (claim: { claim_type: string }) => claim.claim_type === "last_civilian_pre_service",
  )).toHaveLength(0);
  expect(evidence).not.toMatch(/serial_number|service_number/);
});

test.describe("Batch 528 direct profile routes", () => {
  for (const [id, name] of cohort) {
    test(`${name} renders from a direct route`, async ({ page }) => {
      await page.goto(`./people/${id}/`);
      await expect(page.locator("h1")).toContainText(name);
      await expect(page.locator("body")).toContainText("Box167");
      await expect(page.locator("body")).toContainText("Archival-review priority");
    });
  }
});
