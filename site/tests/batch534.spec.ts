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
    "../../research/evidence-page-one-hundred-and-six-and-one-hundred-and-seven-john-r-davies-through-charles-n-davis-pathways_batch-534_2026-09-14.json",
    import.meta.url,
  ),
  "utf8",
);
const profile = (id: string) =>
  people.find((person: { person_id: string }) => person.person_id === id);

const cohort = [
  ["32bbcbe1-c581-50ae-87ad-3dcaaaa622e2", "John R Davies", "cebde9b6-3946-56e8-b56b-cbad528e3845", 106, false],
  ["2bb59c52-cdda-55b2-99cd-b1e0deffc527", "John H Davies", "c93b6f17-4b54-5d41-94e0-f99e89e1a87f", 107, true],
  ["624e4f2a-828e-5dfa-b6a2-229f08764a3a", "Martha A Davies", "4b0a41b7-126c-5dc8-9c58-8eb61d064689", 107, false],
  ["ba89c8f1-2483-52e2-9e67-8940603b53aa", "Thomas M Davies", "2f77a92e-6b5f-58bf-9607-154c39fdb985", 107, true],
  ["fcb095ba-a71d-51e7-96e2-7ad9c401b43c", "W O Davies", "a28a5139-fa4a-5f0a-b7b2-8fd48267b983", 107, true],
  ["6859f328-a32f-5fcb-94d9-333cefe7ea49", "Amos Davis", "e7ff6dcd-0a2d-5fb8-b32f-e28d7e3158ff", 107, true],
  ["f88a5714-6e16-5466-a7fa-ed61c8e897c0", "Buster B Davis", "0513c192-779d-56b6-a533-3ee5eab5eaac", 107, true],
  ["c9795ded-be2f-57ce-8361-1a6f6ba3c77f", "Charles T Davis", "23d7bc92-60bf-59fe-a591-b22482d5e863", 107, true],
  ["747831e4-0e1e-5f36-aff8-781323c86cf3", "Charles C Davis", "05324fc2-b855-5b9b-a05e-0a0f67a7d192", 107, true],
  ["18517786-fa7f-52af-834b-abbc9ea4eb69", "Charles N Davis", "0f19bce3-e7ad-5e0f-be8c-6869b31e2267", 107, true],
] as const;

test("Batch 534 preserves the page boundary and masks every private field", () => {
  for (const [id, name, sourceRecordId, pdfPage, hasPrivateIdentifier] of cohort) {
    const person = profile(id);
    expect(person).toMatchObject({ display_name: name });
    const sourceRecord = person.source_records.find(
      (record: { source_record_id: string }) => record.source_record_id === sourceRecordId,
    );
    expect(sourceRecord).toMatchObject({
      archive_location: "230/86/29/06",
      box: "169",
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

test("Batch 534 publishes three confirmed Army-entry occupations without employers", () => {
  const expected = [
    ["6859f328-a32f-5fcb-94d9-333cefe7ea49", "Farm hands, general farms", "1942-04-15"],
    ["f88a5714-6e16-5466-a7fa-ed61c8e897c0", "Pressmen and plate printers, printing", "1942-04-09"],
    ["747831e4-0e1e-5f36-aff8-781323c86cf3", "Teachers (secondary school) and principals", "1942-06-29"],
  ] as const;
  for (const [id, occupation, endDate] of expected) {
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
      temporal_basis: "strongly_date_bounded",
      identity_confidence: "confirmed",
      claim_confidence: "medium",
      publication_status: "publish_qualified",
    });
    expect(person.claims).toHaveLength(2);
  }
});

test("Batch 534 leaves seven identities unresolved without publishing candidates", () => {
  for (const id of [
    "32bbcbe1-c581-50ae-87ad-3dcaaaa622e2",
    "2bb59c52-cdda-55b2-99cd-b1e0deffc527",
    "624e4f2a-828e-5dfa-b6a2-229f08764a3a",
    "ba89c8f1-2483-52e2-9e67-8940603b53aa",
    "fcb095ba-a71d-51e7-96e2-7ad9c401b43c",
    "c9795ded-be2f-57ce-8361-1a6f6ba3c77f",
    "18517786-fa7f-52af-834b-abbc9ea4eb69",
  ]) {
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
    expect(person.next_action).toContain("No reliable pre-OSS employer has yet been identified");
  }
});

test("Batch 534 keeps John R Davies enlisted from the index without resolving identity", () => {
  expect(profile("32bbcbe1-c581-50ae-87ad-3dcaaaa622e2")).toMatchObject({
    identity_status: "unresolved",
    personnel_category: "enlisted_army_personnel",
    commissioned_officer: false,
  });
});

test("Batch 534 advances attempted and archival coverage with reproducible totals", () => {
  expect(stats).toMatchObject({
    source_rows: 23978,
    person_entities: 23940,
    research_attempted_people: 5108,
    research_attempt_percent: 21.3367,
    verified_affiliation_people: 569,
    verified_affiliation_percent: 2.3768,
    verified_employer_people: 253,
    verified_employer_percent: 1.0568,
    archival_review_assessed_people: 5063,
    archival_review_percent: 21.1487,
    published_claims: 4025,
    public_sources: 3427,
  });
  expect(stats.research_status_counts).toMatchObject({
    not_started: 18832,
    conflicting_sources: 97,
    no_reliable_result_after_protocol: 121,
    occupation_only_found: 942,
    documented_prewar_employer_found: 101,
    requires_archival_review: 3111,
  });
});

test("Batch 534 evidence is complete, citation-linked, and private-value free", () => {
  const bundle = JSON.parse(evidence);
  expect(bundle).toMatchObject({ bundle_version: "1.0" });
  expect(bundle.sources).toHaveLength(3);
  expect(bundle.organizations).toHaveLength(0);
  expect(bundle.affiliations).toHaveLength(3);
  expect(bundle.claims).toHaveLength(6);
  expect(bundle.claims.reduce(
    (sum: number, claim: { sources: unknown[] }) => sum + claim.sources.length,
    0,
  )).toBe(12);
  expect(bundle.person_updates).toHaveLength(10);
  expect(bundle.research_attempts).toHaveLength(10);
  expect(bundle.claims.filter(
    (claim: { claim_type: string }) => claim.claim_type === "occupation",
  )).toHaveLength(3);
  expect(bundle.claims.every(
    (claim: { publication_status: string }) => ["published", "publish_qualified"].includes(claim.publication_status),
  )).toBe(true);
  expect(evidence).not.toMatch(/serial_number|service_number/);
});

test.describe("Batch 534 direct profile routes", () => {
  for (const [id, name] of cohort) {
    test(`${name} ${id.slice(0, 8)} renders from a direct route`, async ({ page }) => {
      await page.goto(`./people/${id}/`);
      await expect(page.locator("h1")).toContainText(name);
      await expect(page.locator("body")).toContainText("Box169");
      await expect(page.locator("body")).toContainText("Archival-review priority");
    });
  }
});
