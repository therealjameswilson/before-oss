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
    "../../research/evidence-page-one-hundred-and-ten-edmund-j-decaussin-jr-through-francis-e-decker-pathways_batch-548_2026-09-15.json",
    import.meta.url,
  ),
  "utf8",
);
const profile = (id: string) =>
  people.find((person: { person_id: string }) => person.person_id === id);

const cohort = [
  ["61bd8997-6f8c-55ff-8813-b08f286ab1ff", "Edmund J Decaussin Jr.", "137ef155-3df8-5f5c-8786-fb60fe50b356", "175", "230/86/29/06", true],
  ["386fbb84-d58f-55b1-a8de-6163e64953f1", "Eugene Dechelette", "0e20f2b4-b0cc-5aff-9f2a-3b0ea80830ee", "175", "230/86/29/06", false],
  ["2f0417ae-6e3e-57fa-842a-9a3a3988505c", "Pierre F D'Echert", "17bbed2d-e483-5d5c-a8ab-48fdb17a3548", "176", "230/86/29/07", false],
  ["4998fc7f-67c1-5569-bd59-11302aa632a5", "Jean DeChezelles", "81b01c91-3476-5b70-9184-9e298fe2272c", "175", "230/86/29/06", false],
  ["67e0d022-5e06-5fb3-98ba-46ed7913ee7c", "Jorg DeChochor", "433528ab-a5f6-5fc7-9e84-bbe82126c4a9", "175", "230/86/29/06", true],
  ["fda85ada-1838-5035-b8ac-77cf9819e48e", "Anthony J DeCicco", "89f3ded2-de1e-54a6-a69e-861a4b6f45ba", "175", "230/86/29/06", true],
  ["6d0ded3e-b5b9-555b-a8b2-52cf4b483ae2", "Joseph G Decicco", "10ce6cd8-4e66-5659-8d66-73c099c62050", "175", "230/86/29/06", true],
  ["d0b9e896-ea0f-5403-9a5a-a54c4e8fb1cf", "Ha Deck", "c41f2233-2d24-5186-8331-dc72714dcbdf", "175", "230/86/29/06", true],
  ["23aae3ce-eab9-5208-9a5b-5577290bf0a1", "Robert Deckelbaum", "2745454b-8573-5d53-b70f-c0f3cc9912a9", "175", "230/86/29/06", false],
  ["50382663-a6d9-5e70-91f2-82acc4c20cdd", "Francis E Decker", "21929ace-d67a-5ad7-bd28-cd536867f6fc", "175", "230/86/29/06", true],
] as const;

test("Batch 548 preserves ten page 110 rows, the Box 176 boundary, and six masked private fields", () => {
  for (const [id, name, sourceRecordId, box, location, hasPrivateIdentifier] of cohort) {
    const person = profile(id);
    expect(person).toMatchObject({ display_name: name });
    const sourceRecord = person.source_records.find(
      (record: { source_record_id: string }) => record.source_record_id === sourceRecordId,
    );
    expect(sourceRecord).toMatchObject({
      archive_location: location,
      box,
      pdf_page: 110,
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

test("Batch 548 publishes three identifier-confirmed Army occupations without inventing employers", () => {
  const expected = [
    ["61bd8997-6f8c-55ff-8813-b08f286ab1ff", "Occupations in manufacture of automobiles, n. e. c.", "1942-12-14"],
    ["67e0d022-5e06-5fb3-98ba-46ed7913ee7c", "Agents and appraisers, n. e. c.", "1942-01-27"],
    ["6d0ded3e-b5b9-555b-a8b2-52cf4b483ae2", "Mechanics and repairmen, n. e. c.", "1942-02-16"],
  ] as const;
  for (const [id, occupation, entryDate] of expected) {
    const person = profile(id);
    expect(person).toMatchObject({
      identity_status: "confirmed",
      personnel_category: "enlisted_army_personnel",
      commissioned_officer: false,
      research_status: "occupation_only_found",
      research_attempt_count: 5,
    });
    expect(person.immediate_pre_oss_affiliations).toEqual([]);
    expect(person.last_civilian_pre_service).toEqual([]);
    expect(person.other_pre_oss_affiliations).toHaveLength(1);
    expect(person.other_pre_oss_affiliations[0]).toMatchObject({
      canonical_organization: null,
      occupation,
      end_date: entryDate,
      temporal_basis: "strongly_date_bounded",
      identity_confidence: "confirmed",
      claim_confidence: "medium",
      publication_status: "publish_qualified",
    });
    expect(person.claims).toHaveLength(2);
    expect(JSON.stringify(person)).toContain("no employer is named");
  }
});

test("Batch 548 documents Eugène Déchelette's last civilian employer but not an immediate OSS predecessor", () => {
  const person = profile("386fbb84-d58f-55b1-a8de-6163e64953f1");
  expect(person).toMatchObject({
    identity_status: "high_confidence",
    personnel_category: "foreign_or_allied_military_personnel",
    commissioned_officer: true,
    allied_or_foreign_personnel: true,
    research_status: "verified_employer_found",
    research_attempt_count: 5,
  });
  expect(person.name_variants).toContain("Eugène Déchelette");
  expect(person.immediate_pre_oss_affiliations).toEqual([]);
  expect(person.last_civilian_pre_service).toHaveLength(1);
  expect(person.last_civilian_pre_service[0]).toMatchObject({
    canonical_organization: "S.A. Déchelette-Despierres",
    historical_organization: "S.A. Déchelette-Despierres",
    role_title: "administrator",
    relationship_type: "employment",
    end_date: "1939-08",
    city: "Roanne",
    state_or_region: "Loire",
    country: "France",
    immediate_pre_oss: false,
    last_civilian_pre_service: true,
    temporal_basis: "strongly_date_bounded",
    identity_confidence: "high_confidence",
    claim_confidence: "high",
    publication_status: "published",
  });
  expect(JSON.stringify(person)).toContain("administrateur d'une société de textiles familiale");
  expect(JSON.stringify(person)).toContain("does not date the OSS personnel-file relationship");
});

test("Batch 548 preserves Jean DeChezelles's truncated alias note without inference", () => {
  const person = profile("4998fc7f-67c1-5569-bd59-11302aa632a5");
  expect(person).toMatchObject({
    identity_status: "unresolved",
    personnel_category: "commissioned_army_officer",
    commissioned_officer: true,
    allied_or_foreign_personnel: null,
    research_status: "requires_archival_review",
    research_attempt_count: 5,
  });
  expect(person.source_records[0].notes_as_indexed).toBe("Alias Fa");
  expect(person.archival_file).toMatchObject({ review_priority: "critical" });
  expect(person.claims).toEqual([]);
  expect(person.identity_evidence).toContain("the note is not expanded");
});

test("Batch 548 leaves Ha Deck unresolved after rejecting the postwar LoC phrase collision", () => {
  const person = profile("d0b9e896-ea0f-5403-9a5a-a54c4e8fb1cf");
  expect(person).toMatchObject({
    identity_status: "unresolved",
    research_status: "requires_archival_review",
    research_attempt_count: 5,
  });
  expect(person.archival_file).toMatchObject({ review_priority: "critical" });
  expect(person.claims).toEqual([]);
  expect(person.next_action).toContain("recover the complete name");
  expect(person.identity_evidence).toContain("1948 Montana newspaper item was rejected");
});

test("Batch 548 preserves the Francis E Decker differing-identifier ambiguity", () => {
  const person = profile("50382663-a6d9-5e70-91f2-82acc4c20cdd");
  expect(person).toMatchObject({
    identity_status: "ambiguous",
    research_status: "needs_identity_review",
    research_attempt_count: 5,
    manual_review_required: true,
  });
  expect(person.archival_file).toMatchObject({ review_priority: "critical" });
  expect(person.immediate_pre_oss_affiliations).toEqual([]);
  expect(person.last_civilian_pre_service).toEqual([]);
  expect(person.other_pre_oss_affiliations).toEqual([]);
  expect(person.claims).toEqual([]);
  expect(person.identity_evidence).toContain("different private identifier");
});

test("Batch 548 advances research, employer, identity, officer, and archival coverage exactly", () => {
  expect(stats).toMatchObject({
    source_rows: 23978,
    person_entities: 23940,
    possible_duplicate_groups: 248,
    research_attempted_people: 5248,
    research_attempt_percent: 21.9215,
    verified_affiliation_people: 575,
    verified_affiliation_percent: 2.4018,
    verified_employer_people: 255,
    verified_employer_percent: 1.0652,
    archival_review_assessed_people: 5203,
    archival_review_percent: 21.7335,
    public_sources: 3500,
    published_claims: 4116,
  });
  expect(stats.research_status_counts).toMatchObject({
    needs_identity_review: 287,
    no_reliable_result_after_protocol: 194,
    not_started: 18692,
    occupation_only_found: 961,
    requires_archival_review: 3139,
    verified_employer_found: 239,
  });
  expect(stats.identity_status_counts).toEqual({
    ambiguous: 248,
    confirmed: 1073,
    conflicting: 109,
    high_confidence: 718,
    probable: 163,
    unresolved: 21629,
  });
  expect(stats.commissioned_status_counts).toEqual({
    commissioned: 2275,
    not_commissioned: 5985,
    unknown: 15680,
  });
});

test("Batch 548 evidence is citation-linked, uncertainty-preserving, and private-value free", () => {
  const bundle = JSON.parse(evidence);
  expect(bundle).toMatchObject({ bundle_version: "1.0" });
  expect(bundle.sources).toHaveLength(4);
  expect(bundle.organizations).toHaveLength(1);
  expect(bundle.affiliations).toHaveLength(4);
  expect(bundle.claims).toHaveLength(8);
  expect(bundle.claims.flatMap((claim: { sources: unknown[] }) => claim.sources)).toHaveLength(15);
  expect(bundle.person_updates).toHaveLength(10);
  expect(bundle.research_attempts).toHaveLength(20);
  expect(bundle.claims.filter((claim: { claim_confidence: string }) => claim.claim_confidence === "confirmed")).toHaveLength(3);
  expect(bundle.claims.filter((claim: { claim_confidence: string }) => claim.claim_confidence === "high")).toHaveLength(2);
  expect(bundle.claims.filter((claim: { claim_confidence: string }) => claim.claim_confidence === "medium")).toHaveLength(3);
  expect(evidence).toContain("No reliable pre-OSS employer has yet been identified");
  expect(evidence).toContain("One exact-name Army row carries a different private identifier");
  expect(evidence).toContain("The literal truncated note 'Alias Fa' is preserved without expansion");
  expect(evidence).not.toMatch(/serial_number|service_number|matched_name/);
});

test("Batch 548 gives every public claim an inspectable citation", () => {
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

test.describe("Batch 548 direct profile routes", () => {
  for (const [id, name, , box] of cohort) {
    test(`${name} ${id.slice(0, 8)} renders from a direct route`, async ({ page }) => {
      await page.goto(`./people/${id}/`);
      await expect(page.locator("h1")).toContainText(name);
      await expect(page.locator("body")).toContainText(`Box${box}`);
      await expect(page.locator("body")).toContainText("Archival-review priority");
    });
  }
});
