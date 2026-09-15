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
    "../../research/evidence-page-one-hundred-and-eleven-john-f-delallo-through-constant-delaporte-pathways_batch-555_2026-09-15.json",
    import.meta.url,
  ),
  "utf8",
);
const profile = (id: string) =>
  people.find((person: { person_id: string }) => person.person_id === id);

const cohort = [
  ["376dcbb0-9607-520e-8f3d-bfc527d08504", "John F DeLallo", "44f5f782-722b-5539-8dd3-ea07a7576482", "177", null, true],
  ["8f2d3a8f-b760-56a8-9700-a78a30fffe7a", "Jaime DelAmo", "f79a8f33-75ae-5201-9294-86eb5325eb60", "177", null, false],
  ["ff309015-47d7-5191-bfd1-6a1af22d2b94", "John S DeLancie", "5b2e49ab-e360-51df-b7cc-697bdd2674ba", "177", null, true],
  ["8e39ba97-c4fd-5a58-a524-7264e8e37554", "Avalda M DeLand", "23aa701f-ee91-507f-ae6f-a14107669197", "177", null, false],
  ["10589a1b-f103-54b3-95fa-a2016cd27ce0", "Albert J Delaney", "a7f7addf-2f69-5f42-8cc2-8eac48b39184", "177", null, false],
  ["cdcd7499-850c-525a-9a62-7fc4d9c200eb", "Robert J Delaney", "1c6d3aba-72dc-56ef-b2b2-25a360881a01", "177", null, false],
  ["40e92070-b2b3-58a8-a584-8c526c6890f7", "Ward Delaney", "03ca9b8f-5acc-5dd1-8162-2eef107555af", "177", null, false],
  ["80da73bc-ef68-590b-98c3-4dfbd971b03f", "Warren Delano", "937d3a21-a941-5acf-9287-63a0134a9a59", "177", "M/Sgt", false],
  ["40f51205-7127-5320-837b-57f06b509fab", "Emilio F Delao", "f9c9dec3-fd7f-5669-9b11-6f5905f2f060", "178", null, true],
  ["3dc5dce1-2190-5df9-981b-d46deecf1b37", "Constant Delaporte", "4344919c-041a-54af-ab7e-6023a2421d09", "178", "Sgt", false],
] as const;

test("Batch 555 preserves page 111 rows 26-35 and masks three private fields", () => {
  for (const [id, name, sourceRecordId, box, rank, hasPrivateIdentifier] of cohort) {
    const person = profile(id);
    expect(person).toMatchObject({ display_name: name, research_attempt_count: 5 });
    const sourceRecord = person.source_records.find(
      (record: { source_record_id: string }) => record.source_record_id === sourceRecordId,
    );
    expect(sourceRecord).toMatchObject({
      archive_location: "230/86/29/07",
      box,
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

test("Batch 555 qualifies Jaime del Amo's company role without labeling it immediate", () => {
  const person = profile("8f2d3a8f-b760-56a8-9700-a78a30fffe7a");
  expect(person).toMatchObject({
    display_name: "Jaime DelAmo",
    identity_status: "probable",
    research_status: "documented_prewar_employer_found",
  });
  expect(person.name_variants).toContain("Jaime del Amo");
  expect(person.immediate_pre_oss_affiliations).toEqual([]);
  expect(person.last_civilian_pre_service).toEqual([]);
  expect(person.other_pre_oss_affiliations).toHaveLength(1);
  expect(person.other_pre_oss_affiliations[0]).toMatchObject({
    canonical_organization: "Del Amo Estate Company",
    role_title: "president",
    relationship_type: "employment",
    start_date: "1941",
    temporal_basis: "documented_prewar",
    identity_confidence: "probable",
    claim_confidence: "medium",
    publication_status: "publish_qualified",
  });
  expect(JSON.stringify(person)).toContain("not established as immediate");
});

test("Batch 555 verifies John de Lancie's civilian employer and separates the military pathway", () => {
  const person = profile("ff309015-47d7-5191-bfd1-6a1af22d2b94");
  expect(person).toMatchObject({
    display_name: "John S DeLancie",
    identity_status: "confirmed",
    personnel_category: "enlisted_army_personnel",
    commissioned_officer: false,
    research_status: "verified_employer_found",
  });
  expect(person.name_variants).toContain("John de Lancie");
  expect(person.last_civilian_pre_service).toHaveLength(1);
  expect(person.last_civilian_pre_service[0]).toMatchObject({
    canonical_organization: "Pittsburgh Symphony Orchestra",
    organization_name_as_found: "Pittsburgh Symphony",
    role_title: "principal oboist",
    relationship_type: "employment",
    start_date: "1940",
    end_date: "1942",
    last_civilian_pre_service: true,
    temporal_basis: "strongly_date_bounded",
    claim_confidence: "high",
  });
  expect(person.immediate_pre_oss_affiliations).toHaveLength(1);
  expect(person.immediate_pre_oss_affiliations[0]).toMatchObject({
    canonical_organization: "Allied Translator and Interpreter Service",
    relationship_type: "military_assignment",
    immediate_pre_oss: true,
    temporal_basis: "probable_immediate",
    claim_confidence: "medium",
  });
  expect(person.other_pre_oss_affiliations).toEqual(expect.arrayContaining([
    expect.objectContaining({
      canonical_organization: "Curtis Institute of Music",
      relationship_type: "student",
      claim_confidence: "high",
    }),
    expect.objectContaining({
      canonical_organization: "United States Army",
      role_title: "bandsman",
      relationship_type: "military_assignment",
      claim_confidence: "high",
    }),
  ]));
});

test("Batch 555 publishes only broad Army occupation codes for John F DeLallo and Emilio F Delao", () => {
  const expectations = [
    ["376dcbb0-9607-520e-8f3d-bfc527d08504", "Automobile manufacturing, n.e.c.", "1942-07-27"],
    ["40f51205-7127-5320-837b-57f06b509fab", "Miscellaneous occupations, n.e.c.", "1942-04-14"],
  ] as const;
  for (const [id, occupation, endDate] of expectations) {
    const person = profile(id);
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
      occupation,
      end_date: endDate,
      relationship_type: "unknown",
      temporal_basis: "strongly_date_bounded",
      identity_confidence: "confirmed",
      claim_confidence: "medium",
    });
    expect(JSON.stringify(person)).toContain("no employer");
  }
});

test("Batch 555 records Ward Delaney and Warren Delano as OSS identities without inventing prehistories", () => {
  const expectations = [
    ["40e92070-b2b3-58a8-a584-8c526c6890f7", "Ward Delaney", null],
    ["80da73bc-ef68-590b-98c3-4dfbd971b03f", "Warren Delano", "M/Sgt"],
  ] as const;
  for (const [id, name, rank] of expectations) {
    const person = profile(id);
    expect(person).toMatchObject({
      display_name: name,
      identity_status: "high_confidence",
      research_status: "requires_archival_review",
    });
    expect(person.source_records[0].rank_as_indexed).toBe(rank);
    expect(person.immediate_pre_oss_affiliations).toEqual([]);
    expect(person.last_civilian_pre_service).toEqual([]);
    expect(person.other_pre_oss_affiliations).toEqual([]);
    expect(person.claims).toHaveLength(1);
    expect(person.claims[0]).toMatchObject({
      claim_type: "identity",
      claim_confidence: "high",
      publication_status: "published",
    });
    expect(person.next_action).toContain("No reliable pre-OSS employer");
  }
});

test("Batch 555 links Constant Delaporte to French archival files but not an employer", () => {
  const person = profile("3dc5dce1-2190-5df9-981b-d46deecf1b37");
  expect(person).toMatchObject({
    display_name: "Constant Delaporte",
    identity_status: "probable",
    personnel_category: "foreign_or_allied_military_personnel",
    commissioned_officer: false,
    allied_or_foreign_personnel: true,
    research_status: "requires_archival_review",
  });
  expect(person.source_records[0]).toMatchObject({
    rank_as_indexed: "Sgt",
    notes_as_indexed: "French",
  });
  expect(person.immediate_pre_oss_affiliations).toEqual([]);
  expect(person.last_civilian_pre_service).toEqual([]);
  expect(person.other_pre_oss_affiliations).toEqual([]);
  expect(person.claims).toEqual(expect.arrayContaining([
    expect.objectContaining({ claim_type: "identity", claim_confidence: "medium" }),
    expect.objectContaining({ claim_type: "archival_file_status", claim_confidence: "high" }),
  ]));
  expect(JSON.stringify(person)).toContain("GR 28 P 4 326/7");
});

test("Batch 555 leaves Avalda, Albert and Robert candidly unresolved or ambiguous", () => {
  const expectations = [
    ["8e39ba97-c4fd-5a58-a524-7264e8e37554", "unresolved", "no_reliable_result_after_protocol"],
    ["10589a1b-f103-54b3-95fa-a2016cd27ce0", "ambiguous", "needs_identity_review"],
    ["cdcd7499-850c-525a-9a62-7fc4d9c200eb", "ambiguous", "needs_identity_review"],
  ] as const;
  for (const [id, identityStatus, researchStatus] of expectations) {
    const person = profile(id);
    expect(person).toMatchObject({
      identity_status: identityStatus,
      research_status: researchStatus,
      manual_review_required: true,
    });
    expect(person.archival_file).toMatchObject({ box: "177", review_priority: "critical" });
    expect(person.immediate_pre_oss_affiliations).toEqual([]);
    expect(person.last_civilian_pre_service).toEqual([]);
    expect(person.other_pre_oss_affiliations).toEqual([]);
    expect(person.next_action).toContain("No reliable pre-OSS employer");
  }
});

test("Batch 555 advances exact research, affiliation and employer coverage", () => {
  expect(stats).toMatchObject({
    source_rows: 23978,
    person_entities: 23940,
    possible_duplicate_groups: 248,
    research_attempted_people: 5317,
    research_attempt_percent: 22.2097,
    verified_affiliation_people: 582,
    verified_affiliation_percent: 2.4311,
    verified_employer_people: 258,
    verified_employer_percent: 1.0777,
    archival_review_assessed_people: 5272,
    archival_review_percent: 22.0217,
    public_sources: 3553,
    published_claims: 4192,
  });
  expect(stats.research_status_counts).toMatchObject({
    documented_prewar_employer_found: 107,
    needs_identity_review: 297,
    no_reliable_result_after_protocol: 210,
    not_started: 18623,
    occupation_only_found: 980,
    requires_archival_review: 3155,
    verified_employer_found: 241,
  });
  expect(stats.identity_status_counts).toEqual({
    ambiguous: 254,
    confirmed: 1090,
    conflicting: 113,
    high_confidence: 728,
    probable: 170,
    unresolved: 21585,
  });
  expect(stats.commissioned_status_counts).toEqual({
    commissioned: 2278,
    not_commissioned: 6001,
    unknown: 15661,
  });
});

test("Batch 555 evidence is citation-linked, qualified, and private-value free", () => {
  const bundle = JSON.parse(evidence);
  expect(bundle).toMatchObject({ bundle_version: "1.0" });
  expect(bundle.sources).toHaveLength(10);
  expect(bundle.organizations).toHaveLength(5);
  expect(bundle.affiliations).toHaveLength(7);
  expect(bundle.claims).toHaveLength(15);
  expect(bundle.claims.flatMap((claim: { sources: unknown[] }) => claim.sources)).toHaveLength(32);
  expect(bundle.person_updates).toHaveLength(10);
  expect(bundle.research_attempts).toHaveLength(20);
  expect(bundle.claims.filter((claim: { claim_confidence: string }) => claim.claim_confidence === "confirmed")).toHaveLength(3);
  expect(bundle.claims.filter((claim: { claim_confidence: string }) => claim.claim_confidence === "high")).toHaveLength(6);
  expect(bundle.claims.filter((claim: { claim_confidence: string }) => claim.claim_confidence === "medium")).toHaveLength(6);
  expect(evidence).toContain("No reliable pre-OSS employer");
  expect(evidence).toContain("not established as immediate");
  expect(evidence).not.toMatch(/serial_number|service_number/);
});

test("Batch 555 gives every public claim an inspectable citation", () => {
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

test.describe("Batch 555 direct profile routes", () => {
  for (const [id, name] of cohort) {
    test(`${name} ${id.slice(0, 8)} renders from a direct route`, async ({ page }) => {
      await page.goto(`./people/${id}/`);
      await expect(page.locator("h1")).toContainText(name);
      await expect(page.locator("body")).toContainText("Box");
      await expect(page.locator("body")).toContainText("Archival-review priority");
    });
  }
});
