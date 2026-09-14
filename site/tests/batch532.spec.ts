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
    "../../research/evidence-page-one-hundred-and-six-elizabeth-davey-through-jean-davidson-pathways_batch-532_2026-09-14.json",
    import.meta.url,
  ),
  "utf8",
);
const profile = (id: string) =>
  people.find((person: { person_id: string }) => person.person_id === id);

const cohort = [
  ["243c407d-976b-53a5-a08c-5a2939c41ec0", "Elizabeth Davey", "c89fda88-5e88-5b7e-80d2-0b7c6c40fbb8", "168", "230/86/29/05", false],
  ["9e5dd326-d7c8-5423-a2ce-d6843e803100", "Charles W David", "183c6d55-7712-56d9-b169-b37c46a046b7", "168", "230/86/29/05", true],
  ["c6be91fd-e067-52f9-8067-d644dbcdaf03", "Homer David Jr.", "49cb2641-4810-51e1-a0df-059018ab5ffb", "168", "230/86/29/05", true],
  ["bfde1f87-73e4-58c9-80fd-d3113e071436", "Nathan H David", "86d33226-11bc-50d0-ac19-82215d513791", "168", "230/86/29/05", false],
  ["f0b8bbf0-63b9-5fd1-b5c8-bccfc014ce08", "David Davidian", "d87b5d19-abc7-5150-a6c2-e18bf2fc420d", "168", "230/86/29/05", true],
  ["172408f1-a8d0-56c0-a0f6-ae16387e18ef", "Abraham Davidson", "b5540394-390d-50a9-97f6-0af97a9810b9", "168", "230/86/29/05", true],
  ["149e4a21-1703-5ddb-98d5-91d28cf3a9cf", "Donald J Davidson", "6a3ae0da-4d65-52a6-9477-335fcfaa4e56", "168", "230/86/29/05", true],
  ["d9ad3e21-13e2-5bcb-bdbd-d8bbe1f2c80e", "George B Davidson", "4679eefe-e5e0-594b-848a-c81e2f2b47b0", "168", "230/86/29/05", true],
  ["85cd8516-81b3-5773-98ca-2f20e4a8b033", "Henrietta Davidson", "2b750b57-f8a8-508a-ac5b-2485ccbc41e3", "168", "230/86/29/05", false],
  ["038ce0ce-5944-5b38-b776-a0cc6955f212", "Jean A Davidson", "80248154-2695-5c05-af03-19d2f51336d3", "169", "230/86/29/06", false],
] as const;

test("Batch 532 preserves page 106 rows 26-35 and masks every private field", () => {
  for (const [id, name, sourceRecordId, box, location, hasPrivateIdentifier] of cohort) {
    const person = profile(id);
    expect(person).toMatchObject({ display_name: name });
    const sourceRecord = person.source_records.find(
      (record: { source_record_id: string }) => record.source_record_id === sourceRecordId,
    );
    expect(sourceRecord).toMatchObject({ archive_location: location, box, pdf_page: 106 });
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

test("Batch 532 publishes three confirmed Army-entry occupations without employers", () => {
  const expected = [
    ["9e5dd326-d7c8-5423-a2ce-d6843e803100", "Clerks, sales", "1940-07-29", "documented_prewar"],
    ["149e4a21-1703-5ddb-98d5-91d28cf3a9cf", "Actors and actresses", "1943-03-20", "strongly_date_bounded"],
    ["d9ad3e21-13e2-5bcb-bdbd-d8bbe1f2c80e", "Machine shop and related occupations, n.e.c.", "1945-03-17", "strongly_date_bounded"],
  ] as const;
  for (const [id, occupation, endDate, temporalBasis] of expected) {
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
      canonical_organization: null,
      occupation,
      end_date: endDate,
      relationship_type: "unknown",
      temporal_basis: temporalBasis,
      identity_confidence: "confirmed",
      claim_confidence: "medium",
      publication_status: "publish_qualified",
    });
  }
});

test("Batch 532 preserves the second Elizabeth Davey row as a separate unresolved entity", () => {
  const first = profile("4b34b649-eebd-5978-9b6f-c42f1331b3ea");
  const second = profile("243c407d-976b-53a5-a08c-5a2939c41ec0");
  expect(first.person_id).not.toBe(second.person_id);
  expect(second.possible_duplicate_group).toBeTruthy();
  expect(second.possible_duplicate_group).toBe(first.possible_duplicate_group);
  expect(second).toMatchObject({
    identity_status: "unresolved",
    research_status: "requires_archival_review",
    research_attempt_count: 3,
  });
  expect(second.claims).toEqual([]);
  expect(second.other_pre_oss_affiliations).toEqual([]);
  expect(second.identity_evidence).toContain("withheld and unassigned");
});

test("Batch 532 publishes a qualified official OSS identity for Homer David Jr.", () => {
  const homer = profile("c6be91fd-e067-52f9-8067-d644dbcdaf03");
  expect(homer).toMatchObject({
    identity_status: "high_confidence",
    personnel_category: "commissioned_army_officer",
    commissioned_officer: true,
    research_status: "requires_archival_review",
    research_attempt_count: 3,
  });
  expect(homer.immediate_pre_oss_affiliations).toEqual([]);
  expect(homer.last_civilian_pre_service).toEqual([]);
  expect(homer.other_pre_oss_affiliations).toEqual([]);
  expect(homer.claims).toHaveLength(1);
  expect(homer.claims[0]).toMatchObject({
    claim_type: "identity",
    evidence_excerpt: "Major Homer David",
    source_quality: "A_direct_official",
    claim_confidence: "high",
    publication_status: "published",
  });
});

test("Batch 532 keeps David Davidian ambiguous and Abraham Davidson conflicting", () => {
  const davidian = profile("f0b8bbf0-63b9-5fd1-b5c8-bccfc014ce08");
  expect(davidian).toMatchObject({
    identity_status: "ambiguous",
    research_status: "needs_identity_review",
    research_attempt_count: 3,
  });
  expect(davidian.identity_evidence).toContain("two exact-name David Davidian rows");

  const abraham = profile("172408f1-a8d0-56c0-a0f6-ae16387e18ef");
  expect(abraham).toMatchObject({
    identity_status: "conflicting",
    research_status: "conflicting_sources",
    research_attempt_count: 3,
  });
  expect(abraham.identity_evidence).toContain("different full name");
  for (const person of [davidian, abraham]) {
    expect(person.immediate_pre_oss_affiliations).toEqual([]);
    expect(person.last_civilian_pre_service).toEqual([]);
    expect(person.other_pre_oss_affiliations).toEqual([]);
    expect(person.claims).toEqual([]);
  }
});

test("Batch 532 leaves Nathan David, Henrietta Davidson and Jean Davidson unresolved", () => {
  for (const id of [
    "bfde1f87-73e4-58c9-80fd-d3113e071436",
    "85cd8516-81b3-5773-98ca-2f20e4a8b033",
    "038ce0ce-5944-5b38-b776-a0cc6955f212",
  ]) {
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

test("Batch 532 advances attempted and archival coverage with reproducible totals", () => {
  expect(stats).toMatchObject({
    source_rows: 23978,
    person_entities: 23940,
    research_attempted_people: 5088,
    research_attempt_percent: 21.2531,
    verified_affiliation_people: 569,
    verified_affiliation_percent: 2.3768,
    verified_employer_people: 253,
    verified_employer_percent: 1.0568,
    archival_review_assessed_people: 5043,
    archival_review_percent: 21.0652,
    published_claims: 4013,
    public_sources: 3421,
  });
  expect(stats.research_status_counts).toMatchObject({
    not_started: 18852,
    conflicting_sources: 97,
    no_reliable_result_after_protocol: 107,
    occupation_only_found: 936,
    documented_prewar_employer_found: 101,
    requires_archival_review: 3111,
  });
});

test("Batch 532 evidence is complete, citation-linked, and private-value free", () => {
  const bundle = JSON.parse(evidence);
  expect(bundle).toMatchObject({ bundle_version: "1.0" });
  expect(bundle.sources).toHaveLength(5);
  expect(bundle.organizations).toHaveLength(0);
  expect(bundle.affiliations).toHaveLength(3);
  expect(bundle.claims).toHaveLength(8);
  expect(bundle.claims.reduce(
    (sum: number, claim: { sources: unknown[] }) => sum + claim.sources.length,
    0,
  )).toBe(16);
  expect(bundle.person_updates).toHaveLength(10);
  expect(bundle.research_attempts).toHaveLength(10);
  expect(bundle.claims.filter(
    (claim: { claim_type: string }) => claim.claim_type === "occupation",
  )).toHaveLength(3);
  const withheld = bundle.claims.filter(
    (claim: { publication_status: string }) => claim.publication_status === "withheld_low_confidence",
  );
  expect(withheld).toHaveLength(1);
  expect(withheld[0]).toMatchObject({
    claim_confidence: "low",
    person_id: "243c407d-976b-53a5-a08c-5a2939c41ec0",
  });
  expect(evidence).not.toMatch(/serial_number|service_number/);
});

test.describe("Batch 532 direct profile routes", () => {
  for (const [id, name, , box] of cohort) {
    test(`${name} ${id.slice(0, 8)} renders from a direct route`, async ({ page }) => {
      await page.goto(`./people/${id}/`);
      await expect(page.locator("h1")).toContainText(name);
      await expect(page.locator("body")).toContainText(`Box${box}`);
      await expect(page.locator("body")).toContainText("Archival-review priority");
    });
  }
});
