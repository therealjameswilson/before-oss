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
    "../../research/evidence-page-one-hundred-and-eleven-andries-deinum-through-egilio-p-delaini-pathways_batch-554_2026-09-15.json",
    import.meta.url,
  ),
  "utf8",
);
const profile = (id: string) =>
  people.find((person: { person_id: string }) => person.person_id === id);

const cohort = [
  ["2ad8789d-952b-5baa-a739-331d3324a1d9", "Andries Deinum", "7493749a-cbcc-579e-8e73-d35f0db88704", null, false, 5],
  ["7c4565ee-9df2-5a95-b22b-471ac5102cac", "Harvey T Deinzer", "4ca10e5f-4895-5836-9bc1-d2c286661d97", "2nd Lt", true, 5],
  ["264a44a0-6a03-5451-a2aa-8fd8805c0cf0", "Raymond W Deisher", "1656c2a5-1fc0-5247-b884-70e242053604", null, true, 6],
  ["cf2ee071-0b16-5c6b-a3e4-daf05f058272", "Francois Deixonne", "4bcb6af7-522c-5e77-a8e4-091d87241537", "Lt", false, 5],
  ["b453354f-47c5-5830-a3cb-ff5319f6706f", "Pierre M DeJussieu-Po", "12423732-85d1-5011-bea6-44b7931ec4bb", "General", false, 5],
  ["cabc9f4b-d2ca-514e-a705-0e9dc1f5947b", "J W Delafield", "f9ecdf37-cbbc-5a66-a193-4e67d477c5af", "Capt", false, 5],
  ["1f3e57f8-d8ff-5119-a662-377d45153df1", "John W Delafield", "1fcbf42b-3769-5ff7-897e-5c1632bda6ff", "Maj", true, 5],
  ["09898871-9e9d-5e99-b333-15d87ec992a0", "Francis J DeLage", "e0e8039c-7a17-52bd-b897-ca68e579fcaa", null, true, 5],
  ["ee2d99d3-0ae5-5c81-b278-2d5a2687fbec", "Dorothy B Delahanty", "38f7f985-8e3f-5259-b0ab-ab628a8d8066", null, false, 5],
  ["e4cfb3d0-168c-50b4-bfa3-3ed18b94a637", "Egilio P Delaini", "5d75e0a2-8262-5732-92db-1b6bab61970a", "S/Sgt", true, 6],
] as const;

test("Batch 554 preserves page 111 rows 16-25 and masks five private fields", () => {
  for (const [id, name, sourceRecordId, rank, hasPrivateIdentifier, attemptCount] of cohort) {
    const person = profile(id);
    expect(person).toMatchObject({ display_name: name, research_attempt_count: attemptCount });
    const sourceRecord = person.source_records.find(
      (record: { source_record_id: string }) => record.source_record_id === sourceRecordId,
    );
    expect(sourceRecord).toMatchObject({
      archive_location: "230/86/29/07",
      box: "177",
      pdf_page: 111,
      rank_as_indexed: rank,
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

test("Batch 554 qualifies Andries Deinum's film pathway and keeps Stanford educational", () => {
  const person = profile("2ad8789d-952b-5baa-a739-331d3324a1d9");
  expect(person).toMatchObject({
    identity_status: "high_confidence",
    personnel_category: "unknown_or_indeterminate",
    commissioned_officer: null,
    research_status: "occupation_only_found",
  });
  expect(person.immediate_pre_oss_affiliations).toHaveLength(1);
  expect(person.immediate_pre_oss_affiliations[0]).toMatchObject({
    canonical_organization: null,
    occupation: "filmmaking study and film production work",
    relationship_type: "professional_affiliation",
    immediate_pre_oss: true,
    last_civilian_pre_service: false,
    temporal_basis: "probable_immediate",
    claim_confidence: "medium",
    publication_status: "publish_qualified",
  });
  expect(person.last_civilian_pre_service).toEqual([]);
  expect(person.other_pre_oss_affiliations).toHaveLength(1);
  expect(person.other_pre_oss_affiliations[0]).toMatchObject({
    canonical_organization: "Stanford University",
    role_title: "student",
    relationship_type: "student",
    immediate_pre_oss: false,
    last_civilian_pre_service: false,
    claim_confidence: "high",
  });
  expect(JSON.stringify(person)).toContain("no employer is established");
});

test("Batch 554 preserves Pierre's indexed form while publishing documented French assignments", () => {
  const person = profile("b453354f-47c5-5830-a3cb-ff5319f6706f");
  expect(person).toMatchObject({
    display_name: "Pierre M DeJussieu-Po",
    identity_status: "high_confidence",
    personnel_category: "foreign_or_allied_military_personnel",
    commissioned_officer: true,
    allied_or_foreign_personnel: true,
    research_status: "requires_archival_review",
  });
  expect(person.name_variants).toContain("Pierre Marie Philippe Dejussieu-Pontcarral");
  expect(person.source_records[0]).toMatchObject({
    indexed_last_name: "DeJussieu-Po",
    rank_as_indexed: "General",
    notes_as_indexed: "French",
  });
  expect(person.immediate_pre_oss_affiliations).toEqual([]);
  expect(person.last_civilian_pre_service).toEqual([]);
  expect(person.other_pre_oss_affiliations).toHaveLength(2);
  expect(person.other_pre_oss_affiliations.map(
    (item: { canonical_organization: string }) => item.canonical_organization,
  )).toEqual([
    "French 45th Army Corps headquarters",
    "Regional Armistice Commission, Missions Section (2nd Bureau)",
  ]);
  for (const affiliation of person.other_pre_oss_affiliations) {
    expect(affiliation).toMatchObject({
      relationship_type: "military_assignment",
      immediate_pre_oss: false,
      last_civilian_pre_service: false,
      temporal_basis: "documented_prewar",
      claim_confidence: "high",
    });
  }
});

test("Batch 554 keeps the two Delafield entities separate and does not invent an employer", () => {
  const captain = profile("cabc9f4b-d2ca-514e-a705-0e9dc1f5947b");
  expect(captain).toMatchObject({
    display_name: "J W Delafield",
    identity_status: "unresolved",
    personnel_category: "commissioned_army_officer",
    commissioned_officer: true,
    research_status: "no_reliable_result_after_protocol",
  });
  expect(captain.claims).toEqual([]);
  expect(captain.next_action).toContain("No reliable pre-OSS employer");

  const major = profile("1f3e57f8-d8ff-5119-a662-377d45153df1");
  expect(major).toMatchObject({
    display_name: "John W Delafield",
    identity_status: "high_confidence",
    personnel_category: "commissioned_army_officer",
    commissioned_officer: true,
    research_status: "occupation_only_found",
  });
  expect(major.name_variants).toContain("John White Delafield");
  expect(major.immediate_pre_oss_affiliations).toEqual([]);
  expect(major.last_civilian_pre_service).toEqual([]);
  expect(major.other_pre_oss_affiliations).toHaveLength(2);
  expect(major.other_pre_oss_affiliations).toEqual(expect.arrayContaining([
    expect.objectContaining({
      occupation: "finance",
      canonical_organization: null,
      relationship_type: "unknown",
      claim_confidence: "medium",
    }),
    expect.objectContaining({
      organization_name_as_found: "the state's military communication section",
      relationship_type: "military_assignment",
      claim_confidence: "medium",
    }),
  ]));
  expect(JSON.stringify(major)).toContain("names no firm");
});

test("Batch 554 confirms Egilio P Delaini's broad Army occupation without an employer", () => {
  const person = profile("e4cfb3d0-168c-50b4-bfa3-3ed18b94a637");
  expect(person).toMatchObject({
    identity_status: "confirmed",
    personnel_category: "enlisted_army_personnel",
    commissioned_officer: false,
    allied_or_foreign_personnel: false,
    research_status: "occupation_only_found",
  });
  expect(person.immediate_pre_oss_affiliations).toEqual([]);
  expect(person.last_civilian_pre_service).toEqual([]);
  expect(person.other_pre_oss_affiliations).toHaveLength(1);
  expect(person.other_pre_oss_affiliations[0]).toMatchObject({
    canonical_organization: null,
    occupation: "Waiters and waitresses, except private family",
    end_date: "1941-06-05",
    relationship_type: "unknown",
    temporal_basis: "strongly_date_bounded",
    identity_confidence: "confirmed",
    claim_confidence: "medium",
  });
  expect(JSON.stringify(person)).toContain("no employer is named");
});

test("Batch 554 limits Francois Deixonne to a qualified probable identity", () => {
  const person = profile("cf2ee071-0b16-5c6b-a3e4-daf05f058272");
  expect(person).toMatchObject({
    identity_status: "probable",
    personnel_category: "commissioned_army_officer",
    commissioned_officer: true,
    allied_or_foreign_personnel: true,
    research_status: "requires_archival_review",
  });
  expect(person.name_variants).toContain("François Deixonne");
  expect(person.immediate_pre_oss_affiliations).toEqual([]);
  expect(person.last_civilian_pre_service).toEqual([]);
  expect(person.other_pre_oss_affiliations).toEqual([]);
  expect(person.claims).toHaveLength(1);
  expect(person.claims[0]).toMatchObject({
    claim_type: "identity",
    claim_confidence: "medium",
    publication_status: "publish_qualified",
  });
  expect(person.next_action).toContain("identity match is probable only");
});

test("Batch 554 exposes Francis J DeLage's two-way identifier conflict", () => {
  const person = profile("09898871-9e9d-5e99-b333-15d87ec992a0");
  expect(person).toMatchObject({
    identity_status: "conflicting",
    personnel_category: "unknown_or_indeterminate",
    commissioned_officer: null,
    research_status: "conflicting_sources",
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
  expect(person.identity_evidence).toContain("different identifier");
  expect(JSON.stringify(person)).toContain("No Army fields are adopted");
});

test("Batch 554 leaves Harvey, Raymond and Dorothy candidly unresolved or ambiguous", () => {
  const expectations = [
    ["7c4565ee-9df2-5a95-b22b-471ac5102cac", "ambiguous", "needs_identity_review", "critical"],
    ["264a44a0-6a03-5451-a2aa-8fd8805c0cf0", "ambiguous", "requires_archival_review", "critical"],
    ["ee2d99d3-0ae5-5c81-b278-2d5a2687fbec", "unresolved", "no_reliable_result_after_protocol", "critical"],
  ] as const;
  for (const [id, identityStatus, researchStatus, priority] of expectations) {
    const person = profile(id);
    expect(person).toMatchObject({
      identity_status: identityStatus,
      research_status: researchStatus,
      manual_review_required: true,
    });
    expect(person.archival_file).toMatchObject({ box: "177", review_priority: priority });
    expect(person.immediate_pre_oss_affiliations).toEqual([]);
    expect(person.last_civilian_pre_service).toEqual([]);
    expect(person.other_pre_oss_affiliations).toEqual([]);
    expect(person.next_action).toContain("No reliable pre-OSS employer");
  }
});

test("Batch 554 advances exact research and affiliation coverage without changing employer coverage", () => {
  expect(stats).toMatchObject({
    source_rows: 23978,
    person_entities: 23940,
    possible_duplicate_groups: 248,
    research_attempted_people: 5307,
    research_attempt_percent: 22.1679,
    verified_affiliation_people: 581,
    verified_affiliation_percent: 2.4269,
    verified_employer_people: 257,
    verified_employer_percent: 1.0735,
    archival_review_assessed_people: 5262,
    archival_review_percent: 21.9799,
    public_sources: 3543,
    published_claims: 4177,
  });
  expect(stats.research_status_counts).toMatchObject({
    conflicting_sources: 111,
    needs_identity_review: 295,
    no_reliable_result_after_protocol: 209,
    not_started: 18633,
    occupation_only_found: 978,
    requires_archival_review: 3152,
    verified_employer_found: 240,
  });
  expect(stats.identity_status_counts).toEqual({
    ambiguous: 252,
    confirmed: 1087,
    conflicting: 113,
    high_confidence: 726,
    probable: 168,
    unresolved: 21594,
  });
  expect(stats.commissioned_status_counts).toEqual({
    commissioned: 2278,
    not_commissioned: 5997,
    unknown: 15665,
  });
});

test("Batch 554 evidence is citation-linked, qualified, and private-value free", () => {
  const bundle = JSON.parse(evidence);
  expect(bundle).toMatchObject({ bundle_version: "1.0" });
  expect(bundle.sources).toHaveLength(8);
  expect(bundle.organizations).toHaveLength(3);
  expect(bundle.affiliations).toHaveLength(7);
  expect(bundle.claims).toHaveLength(13);
  expect(bundle.claims.flatMap((claim: { sources: unknown[] }) => claim.sources)).toHaveLength(21);
  expect(bundle.person_updates).toHaveLength(10);
  expect(bundle.research_attempts).toHaveLength(20);
  expect(bundle.claims.filter((claim: { claim_confidence: string }) => claim.claim_confidence === "confirmed")).toHaveLength(1);
  expect(bundle.claims.filter((claim: { claim_confidence: string }) => claim.claim_confidence === "high")).toHaveLength(6);
  expect(bundle.claims.filter((claim: { claim_confidence: string }) => claim.claim_confidence === "medium")).toHaveLength(5);
  expect(bundle.claims.filter((claim: { claim_confidence: string }) => claim.claim_confidence === "conflicting")).toHaveLength(1);
  expect(evidence).toContain("No reliable pre-OSS employer");
  expect(evidence).toContain("no employer is established");
  expect(evidence).toContain("no firm or exact role");
  expect(evidence).not.toMatch(/serial_number|service_number/);
});

test("Batch 554 gives every public or conflicting claim an inspectable citation", () => {
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

test.describe("Batch 554 direct profile routes", () => {
  for (const [id, name] of cohort) {
    test(`${name} ${id.slice(0, 8)} renders from a direct route`, async ({ page }) => {
      await page.goto(`./people/${id}/`);
      await expect(page.locator("h1")).toContainText(name);
      await expect(page.locator("body")).toContainText("Box177");
      await expect(page.locator("body")).toContainText("Archival-review priority");
    });
  }
});
