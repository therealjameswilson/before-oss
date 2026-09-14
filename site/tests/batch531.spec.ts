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
    "../../research/evidence-page-one-hundred-and-six-isabelle-davenport-through-elizabeth-davey-pathways_batch-531_2026-09-14.json",
    import.meta.url,
  ),
  "utf8",
);
const profile = (id: string) =>
  people.find((person: { person_id: string }) => person.person_id === id);

const cohort = [
  ["88f84250-1fa2-575b-91c9-2769b1f6f699", "Isabelle Davenport", "d1d884bc-6463-5739-954e-9ba5029cecc9", false],
  ["46cb091c-ff76-594c-865f-e83c405d5bdc", "James L Davenport", "3bb23e2f-2b63-56aa-a784-d73c3cd2e2b8", true],
  ["586e460c-0c27-5f8a-90a1-617d567f0add", "John S Davenport III", "0af7042f-c25d-5261-8121-6dfbd532eeb7", false],
  ["5d918f75-c7c4-5f80-a177-25a1c1be1c54", "John H Davenport Jr.", "cc9b95ac-5985-57da-94d1-690f532d5ec0", true],
  ["d2b46ec0-3811-5932-9e8f-8e5e61c5e0e2", "Leo Davenport", "555d935c-f9c4-58ff-8a07-9cbcba9f3afc", true],
  ["f9ca8946-208c-5289-808e-0100aff46e9c", "Riley Davenport", "06944786-5edc-5aad-a095-46b05b5bd15f", true],
  ["d7951bdf-f0fe-5319-bf43-401b2e6ae28f", "Roslyn Davenport", "8277ae9f-5db1-5cc2-b60b-aab6aa652b68", false],
  ["f08c54f3-871f-53a2-b48e-6af9b3d06283", "Donald L Davey", "5cdea293-1592-542a-9cc7-a3176baa7eed", true],
  ["b8f19870-a594-59ad-bffa-cb030fc8e24c", "Donald L Davey", "2e295d66-6105-587e-beb7-21caded1df58", false],
  ["4b34b649-eebd-5978-9b6f-c42f1331b3ea", "Elizabeth Davey", "ec2e7d27-220d-5f31-9468-53a884ab42ac", false],
] as const;

test("Batch 531 preserves page 106 rows 16-25 and masks every private field", () => {
  for (const [id, name, sourceRecordId, hasPrivateIdentifier] of cohort) {
    const person = profile(id);
    expect(person).toMatchObject({ display_name: name });
    const sourceRecord = person.source_records.find(
      (record: { source_record_id: string }) => record.source_record_id === sourceRecordId,
    );
    expect(sourceRecord).toMatchObject({
      archive_location: "230/86/29/05",
      box: "168",
      pdf_page: 106,
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
});

test("Batch 531 publishes three confirmed Army-entry occupations without employers", () => {
  const expected = [
    ["46cb091c-ff76-594c-865f-e83c405d5bdc", "Carpenters", "1942-10-30", 3],
    ["5d918f75-c7c4-5f80-a177-25a1c1be1c54", "Occupations in manufacture of textiles, n.e.c.", "1942-08-10", 4],
    ["f08c54f3-871f-53a2-b48e-6af9b3d06283", "Linemen and servicemen, telegraph, telephone, and power", "1942-10-17", 3],
  ] as const;
  for (const [id, occupation, endDate, attemptCount] of expected) {
    const person = profile(id);
    expect(person).toMatchObject({
      identity_status: "confirmed",
      personnel_category: "enlisted_army_personnel",
      commissioned_officer: false,
      research_status: "occupation_only_found",
      research_attempt_count: attemptCount,
    });
    expect(person.immediate_pre_oss_affiliations).toEqual([]);
    expect(person.last_civilian_pre_service).toEqual([]);
    expect(person.other_pre_oss_affiliations).toHaveLength(1);
    expect(person.other_pre_oss_affiliations[0]).toMatchObject({
      canonical_organization: null,
      occupation,
      end_date: endDate,
      relationship_type: "unknown",
      temporal_basis: "strongly_date_bounded",
      identity_confidence: "confirmed",
      claim_confidence: "medium",
      publication_status: "publish_qualified",
    });
  }
});

test("Batch 531 keeps the two Donald L Davey rows separate", () => {
  const matched = profile("f08c54f3-871f-53a2-b48e-6af9b3d06283");
  const unmatched = profile("b8f19870-a594-59ad-bffa-cb030fc8e24c");
  expect(matched.person_id).not.toBe(unmatched.person_id);
  expect(matched.possible_duplicate_group).toBeTruthy();
  expect(unmatched.possible_duplicate_group).toBe(matched.possible_duplicate_group);
  expect(matched).toMatchObject({ identity_status: "confirmed", research_status: "occupation_only_found" });
  expect(unmatched).toMatchObject({ identity_status: "unresolved", research_status: "requires_archival_review" });
  expect(matched.other_pre_oss_affiliations).toHaveLength(1);
  expect(unmatched.other_pre_oss_affiliations).toEqual([]);
  expect(unmatched.claims).toEqual([]);
  expect(unmatched.identity_evidence).toContain("not assigned or used to merge row 24");
});

test("Batch 531 publishes Leo Davenport as an unresolved official-record conflict", () => {
  const leo = profile("d2b46ec0-3811-5932-9e8f-8e5e61c5e0e2");
  expect(leo).toMatchObject({
    identity_status: "conflicting",
    research_status: "conflicting_sources",
    personnel_category: "unknown_or_indeterminate",
    commissioned_officer: null,
    research_attempt_count: 4,
  });
  expect(leo.immediate_pre_oss_affiliations).toEqual([]);
  expect(leo.last_civilian_pre_service).toEqual([]);
  expect(leo.other_pre_oss_affiliations).toEqual([]);
  expect(leo.claims).toEqual([]);
  expect(leo.identity_evidence).toContain("different full name");
  expect(leo.identity_evidence).toContain("different identifier");
});

test("Batch 531 withholds the Elizabeth Davey Velen lead and invents no employer", () => {
  const elizabeth = profile("4b34b649-eebd-5978-9b6f-c42f1331b3ea");
  expect(elizabeth).toMatchObject({
    identity_status: "unresolved",
    research_status: "requires_archival_review",
    personnel_category: "unknown_or_indeterminate",
    commissioned_officer: null,
    research_attempt_count: 3,
  });
  expect(elizabeth.possible_duplicate_group).toBeTruthy();
  expect(elizabeth.name_variants).not.toContain("Elizabeth Davey Velen");
  expect(elizabeth.claims).toEqual([]);
  expect(elizabeth.immediate_pre_oss_affiliations).toEqual([]);
  expect(elizabeth.last_civilian_pre_service).toEqual([]);
  expect(elizabeth.other_pre_oss_affiliations).toEqual([]);
  expect(elizabeth.identity_evidence).toContain("withheld and unassigned");
  expect(elizabeth.next_action).toContain("Do not treat Radcliffe attendance as employment");
});

test("Batch 531 leaves four unsupported identities visibly unresolved", () => {
  const expected = [
    ["88f84250-1fa2-575b-91c9-2769b1f6f699", 3],
    ["586e460c-0c27-5f8a-90a1-617d567f0add", 3],
    ["f9ca8946-208c-5289-808e-0100aff46e9c", 4],
    ["d7951bdf-f0fe-5319-bf43-401b2e6ae28f", 4],
  ] as const;
  for (const [id, attemptCount] of expected) {
    const person = profile(id);
    expect(person).toMatchObject({
      identity_status: "unresolved",
      research_status: "no_reliable_result_after_protocol",
      research_attempt_count: attemptCount,
    });
    expect(person.immediate_pre_oss_affiliations).toEqual([]);
    expect(person.last_civilian_pre_service).toEqual([]);
    expect(person.other_pre_oss_affiliations).toEqual([]);
    expect(person.claims).toEqual([]);
    expect(person.next_action).toContain("No reliable pre-OSS employer has yet been identified");
  }
});

test("Batch 531 advances attempted and archival coverage with reproducible totals", () => {
  expect(stats).toMatchObject({
    source_rows: 23978,
    person_entities: 23940,
    research_attempted_people: 5078,
    research_attempt_percent: 21.2114,
    verified_affiliation_people: 569,
    verified_affiliation_percent: 2.3768,
    verified_employer_people: 253,
    verified_employer_percent: 1.0568,
    archival_review_assessed_people: 5033,
    archival_review_percent: 21.0234,
    published_claims: 4006,
    public_sources: 3417,
  });
  expect(stats.research_status_counts).toMatchObject({
    not_started: 18862,
    conflicting_sources: 96,
    no_reliable_result_after_protocol: 104,
    occupation_only_found: 933,
    documented_prewar_employer_found: 101,
    requires_archival_review: 3109,
  });
});

test("Batch 531 evidence is complete, citation-linked, and private-value free", () => {
  const bundle = JSON.parse(evidence);
  expect(bundle).toMatchObject({ bundle_version: "1.0" });
  expect(bundle.sources).toHaveLength(4);
  expect(bundle.organizations).toHaveLength(0);
  expect(bundle.affiliations).toHaveLength(3);
  expect(bundle.claims).toHaveLength(7);
  expect(bundle.claims.reduce(
    (sum: number, claim: { sources: unknown[] }) => sum + claim.sources.length,
    0,
  )).toBe(14);
  expect(bundle.person_updates).toHaveLength(10);
  expect(bundle.research_attempts).toHaveLength(10);
  expect(bundle.claims.filter(
    (claim: { claim_type: string }) => claim.claim_type === "last_civilian_pre_service",
  )).toHaveLength(0);
  expect(bundle.claims.filter(
    (claim: { claim_type: string }) => claim.claim_type === "occupation",
  )).toHaveLength(3);
  const withheld = bundle.claims.filter(
    (claim: { publication_status: string }) => claim.publication_status === "withheld_low_confidence",
  );
  expect(withheld).toHaveLength(1);
  expect(withheld[0]).toMatchObject({ claim_confidence: "low", person_id: "4b34b649-eebd-5978-9b6f-c42f1331b3ea" });
  expect(evidence).not.toMatch(/serial_number|service_number/);
});

test.describe("Batch 531 direct profile routes", () => {
  for (const [id, name] of cohort) {
    test(`${name} ${id.slice(0, 8)} renders from a direct route`, async ({ page }) => {
      await page.goto(`./people/${id}/`);
      await expect(page.locator("h1")).toContainText(name);
      await expect(page.locator("body")).toContainText("Box168");
      await expect(page.locator("body")).toContainText("Archival-review priority");
    });
  }
});
