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
    "../../research/evidence-pages-one-hundred-and-five-and-six-guy-g-darr-through-leoni-dasmousetis-pathways_batch-529_2026-09-14.json",
    import.meta.url,
  ),
  "utf8",
);
const profile = (id: string) =>
  people.find((person: { person_id: string }) => person.person_id === id);

const cohort = [
  ["d6cff363-66e1-5929-9c39-e526f753f4b2", "Guy G Darr", "76ae6a1e-c06f-522c-bf66-c0e97221184f", 105, "167", true],
  ["58f71d60-124f-537f-a5cb-3dd3bee06c71", "Ronald J Darr", "e78adb26-e6f3-5013-a5ff-cbf83ee751fb", 105, "167", true],
  ["93e29b6c-b3a3-5c29-8d95-777b0fe9cf55", "Lucie S Darst", "78adb930-f883-5146-ad80-a54806ebdb4a", 105, "167", false],
  ["9d5887d3-c1ab-5f7c-9e5e-069cdc944884", "Albert L Dart", "30d1f0df-5c9b-562f-ab11-272311581765", 105, "167", true],
  ["fd1fffd9-a5af-56e6-931c-b4beb07c9116", "Dilip Das", "8c71ddec-61fa-5cd1-af08-8b7a4a57296b", 105, "167", false],
  ["267ababd-faee-5c15-a597-c62d640a803b", "Sala Dasandra", "fe7ab7a2-2e5f-5967-a574-35c943e99e90", 106, "167", false],
  ["fa55e22e-b189-5ac4-9c53-9c8d387d6624", "Joseph Dasher", "0141fd0a-2892-5af7-8218-79fd7191870e", 106, "167", false],
  ["4c188d2e-50c0-5812-9691-a5f87538f09a", "Samuel Dashiell", "96d8184d-9bf7-5405-ad35-c86b9fca0160", 106, "167", false],
  ["4ea0388b-9dda-57bf-b326-7b458b43e5d0", "Harry M Daskam", "04fa2d88-d19c-503f-8672-9f8aed671891", 106, "168", true],
  ["090bf0fa-6172-5f13-a6e4-1745e055a4dd", "Leoni DasMousetis", "a4d2b6c4-41da-547f-aaf2-ef9256426e72", 106, "167", false],
] as const;

test("Batch 529 preserves ten printed rows across pages 105-106 and masks private fields", () => {
  for (const [id, name, sourceRecordId, pdfPage, box, hasPrivateIdentifier] of cohort) {
    const person = profile(id);
    expect(person).toMatchObject({ display_name: name });
    const sourceRecord = person.source_records.find(
      (record: { source_record_id: string }) => record.source_record_id === sourceRecordId,
    );
    expect(sourceRecord).toMatchObject({
      archive_location: "230/86/29/05",
      box,
      pdf_page: pdfPage,
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
  expect(profile("58f71d60-124f-537f-a5cb-3dd3bee06c71").source_records[0].rank_as_indexed).toBe("Capt");
  expect(profile("9d5887d3-c1ab-5f7c-9e5e-069cdc944884").source_records[0].rank_as_indexed).toBe("S/Sgt");
  expect(profile("fa55e22e-b189-5ac4-9c53-9c8d387d6624").source_records[0].rank_as_indexed).toBe("Lt Col");
  expect(profile("090bf0fa-6172-5f13-a6e4-1745e055a4dd").display_name).toBe("Leoni DasMousetis");
});

test("Batch 529 publishes three exact Army matches as entry-time occupations, not employers", () => {
  const expected = [
    ["d6cff363-66e1-5929-9c39-e526f753f4b2", "Post office clerks"],
    ["9d5887d3-c1ab-5f7c-9e5e-069cdc944884", "Managers and officials, n.e.c."],
    ["4ea0388b-9dda-57bf-b326-7b458b43e5d0", "Photographic process occupations"],
  ] as const;
  for (const [id, occupation] of expected) {
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
      relationship_type: "unknown",
      temporal_basis: "strongly_date_bounded",
      claim_confidence: "medium",
    });
  }
  expect(profile("9d5887d3-c1ab-5f7c-9e5e-069cdc944884").claims[0].temporal_assessment).toContain("private/PV3");
  expect(profile("9d5887d3-c1ab-5f7c-9e5e-069cdc944884").claims[0].temporal_assessment).toContain("S/Sgt");
});

test("Batch 529 distinguishes Joseph Dasher's military path from earlier consular employment", () => {
  const joseph = profile("fa55e22e-b189-5ac4-9c53-9c8d387d6624");
  expect(joseph).toMatchObject({
    identity_status: "high_confidence",
    personnel_category: "commissioned_army_officer",
    commissioned_officer: true,
    research_status: "documented_prewar_employer_found",
    research_attempt_count: 3,
  });
  expect(joseph.immediate_pre_oss_affiliations).toHaveLength(1);
  expect(joseph.immediate_pre_oss_affiliations[0]).toMatchObject({
    canonical_organization: "U.S. Army Military Intelligence",
    relationship_type: "military_assignment",
    temporal_basis: "probable_immediate",
    claim_confidence: "medium",
  });
  expect(joseph.last_civilian_pre_service).toEqual([]);
  expect(joseph.other_pre_oss_affiliations).toHaveLength(1);
  expect(joseph.other_pre_oss_affiliations[0]).toMatchObject({
    canonical_organization: "Consulate of the Republic of Poland in Pittsburgh",
    relationship_type: "employment",
    start_date: "1926",
    end_date: "1936",
    temporal_basis: "documented_prewar",
    claim_confidence: "medium",
  });
});

test("Batch 529 keeps Samuel Dashiell's journalist identity and occupation qualified", () => {
  const samuel = profile("4c188d2e-50c0-5812-9691-a5f87538f09a");
  expect(samuel).toMatchObject({
    identity_status: "probable",
    research_status: "occupation_only_found",
    research_attempt_count: 3,
  });
  expect(samuel.immediate_pre_oss_affiliations).toEqual([]);
  expect(samuel.last_civilian_pre_service).toEqual([]);
  expect(samuel.other_pre_oss_affiliations).toHaveLength(1);
  expect(samuel.other_pre_oss_affiliations[0]).toMatchObject({
    canonical_organization: null,
    occupation: "Newspaper correspondent",
    identity_confidence: "probable",
    claim_confidence: "medium",
    publication_status: "publish_qualified",
  });
  expect(samuel.claims[0].claim_text).toContain("probably");
});

test("Batch 529 withholds Ronald Darr's discovery-only candidate from public claims", () => {
  const ronald = profile("58f71d60-124f-537f-a5cb-3dd3bee06c71");
  expect(ronald).toMatchObject({
    identity_status: "probable",
    personnel_category: "commissioned_army_officer",
    commissioned_officer: true,
    research_status: "requires_archival_review",
    research_attempt_count: 3,
  });
  expect(ronald.immediate_pre_oss_affiliations).toEqual([]);
  expect(ronald.last_civilian_pre_service).toEqual([]);
  expect(ronald.other_pre_oss_affiliations).toEqual([]);
  expect(ronald.claims).toEqual([]);
  expect(ronald.next_action).toContain("No reliable pre-OSS employer has yet been identified");
});

test("Batch 529 leaves four unsupported identities visibly unresolved", () => {
  const ids = [
    "93e29b6c-b3a3-5c29-8d95-777b0fe9cf55",
    "fd1fffd9-a5af-56e6-931c-b4beb07c9116",
    "267ababd-faee-5c15-a597-c62d640a803b",
    "090bf0fa-6172-5f13-a6e4-1745e055a4dd",
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

test("Batch 529 advances attempted and archival coverage with reproducible totals", () => {
  expect(stats).toMatchObject({
    source_rows: 23978,
    person_entities: 23940,
    research_attempted_people: 5058,
    research_attempt_percent: 21.1278,
    verified_affiliation_people: 569,
    verified_affiliation_percent: 2.3768,
    verified_employer_people: 253,
    verified_employer_percent: 1.0568,
    archival_review_assessed_people: 5013,
    archival_review_percent: 20.9398,
    published_claims: 3993,
    public_sources: 3411,
  });
  expect(stats.research_status_counts).toMatchObject({
    not_started: 18882,
    no_reliable_result_after_protocol: 94,
    occupation_only_found: 927,
    documented_prewar_employer_found: 101,
    requires_archival_review: 3106,
  });
});

test("Batch 529 evidence is complete, citation-linked and private-value free", () => {
  const bundle = JSON.parse(evidence);
  expect(bundle).toMatchObject({ bundle_version: "1.0" });
  expect(bundle.sources).toHaveLength(9);
  expect(bundle.organizations).toHaveLength(2);
  expect(bundle.affiliations).toHaveLength(6);
  expect(bundle.claims).toHaveLength(12);
  expect(bundle.claims.reduce(
    (sum: number, claim: { sources: unknown[] }) => sum + claim.sources.length,
    0,
  )).toBe(25);
  expect(bundle.person_updates).toHaveLength(10);
  expect(bundle.research_attempts).toHaveLength(10);
  expect(bundle.claims.filter(
    (claim: { claim_type: string }) => claim.claim_type === "last_civilian_pre_service",
  )).toHaveLength(0);
  expect(bundle.claims.filter(
    (claim: { publication_status: string }) => claim.publication_status === "withheld_low_confidence",
  )).toHaveLength(1);
  expect(evidence).not.toMatch(/serial_number|service_number/);
});

test.describe("Batch 529 direct profile routes", () => {
  for (const [id, name, , , box] of cohort) {
    test(`${name} renders from a direct route`, async ({ page }) => {
      await page.goto(`./people/${id}/`);
      await expect(page.locator("h1")).toContainText(name);
      await expect(page.locator("body")).toContainText(`Box${box}`);
      await expect(page.locator("body")).toContainText("Archival-review priority");
    });
  }
});
