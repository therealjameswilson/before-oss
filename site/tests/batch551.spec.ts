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
    "../../research/evidence-page-one-hundred-and-ten-clifford-h-deflumear-through-lawrence-degennaro-pathways_batch-551_2026-09-15.json",
    import.meta.url,
  ),
  "utf8",
);
const profile = (id: string) =>
  people.find((person: { person_id: string }) => person.person_id === id);

const cohort = [
  ["1ec235e0-f6d6-5d99-9e6d-11597b9763c5", "Clifford H DeFlumear", "f1a9c230-d93a-5060-8962-79befa699927", true],
  ["b40591dd-1d67-55e0-b6cd-c379317d7ad9", "Alfred L DeFlumeri", "717e1773-ca4c-5a45-814b-39630184e0e5", false],
  ["d132e365-dd0d-548c-ab66-73afc2a9dff6", "Claire DeForbin", "e0fea156-39b2-5f91-bac0-13751532481b", false],
  ["b1afbef7-3bd1-5848-9ac8-9bda010d700f", "Robert B Deford", "b1014a51-d708-5903-8eca-75ebd81ae4c9", false],
  ["0ae8f83b-9fee-57c7-b773-9ff0a20ffd29", "Rene J Defourneaux", "49bced34-b158-531a-bab3-9036bbe3e575", true],
  ["0f9abbe9-8448-5f13-917d-74be1bd88ce4", "Francis J Defrane", "4f6c3c7a-ee76-52e2-ab6f-afbea187b702", true],
  ["6639bb45-198a-5d9a-963a-2cd9fd136394", "Felik DeGaitano", "1dd652bc-30fb-57f5-944a-24082cfffce4", false],
  ["fee0b399-9ba8-51d4-9d9c-05c2acabf24a", "John S Degaitas", "556bd734-e9f6-52e8-ab20-3b39680fc1ff", true],
  ["e021fc1f-2e4c-522e-a370-82c4e244a148", "Rene DeGaston", "aeab91e7-97b1-554c-8d60-2734124f3fb2", false],
  ["1ce809f8-b0b8-5b53-aebe-21f0b3472fba", "Lawrence DeGennaro", "9d3e86c2-ca27-566f-975e-7aa80a644ea2", true],
] as const;

test("Batch 551 preserves ten page 110 rows in Box 176 and masks five private fields", () => {
  for (const [id, name, sourceRecordId, hasPrivateIdentifier] of cohort) {
    const person = profile(id);
    expect(person).toMatchObject({ display_name: name, research_attempt_count: 5 });
    const sourceRecord = person.source_records.find(
      (record: { source_record_id: string }) => record.source_record_id === sourceRecordId,
    );
    expect(sourceRecord).toMatchObject({
      archive_location: "230/86/29/07",
      box: "176",
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

test("Batch 551 publishes two identifier-confirmed Army occupations without inventing employers", () => {
  const expected = [
    ["1ec235e0-f6d6-5d99-9e6d-11597b9763c5", "Warehousing, storekeeping, handling, loading, unloading, and related occupations, n. e. c.", "1942-10-21"],
    ["fee0b399-9ba8-51d4-9d9c-05c2acabf24a", "Cooks, except private family", "1942-11-16"],
  ] as const;
  for (const [id, occupation, entryDate] of expected) {
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

test("Batch 551 confirms Lawrence DeGennaro but refuses to decode unmapped code 9-99", () => {
  const person = profile("1ce809f8-b0b8-5b53-aebe-21f0b3472fba");
  expect(person).toMatchObject({
    identity_status: "confirmed",
    personnel_category: "enlisted_army_personnel",
    commissioned_officer: false,
    research_status: "requires_archival_review",
  });
  expect(person.name_variants).toContain("Lawrence De Gennaro");
  expect(person.immediate_pre_oss_affiliations).toEqual([]);
  expect(person.other_pre_oss_affiliations).toEqual([]);
  expect(person.claims).toHaveLength(1);
  expect(person.identity_evidence).toContain("no definition");
  expect(JSON.stringify(person)).not.toContain('"occupation":"9-99"');
});

test("Batch 551 distinguishes Defourneaux's SOE predecessor from his earlier tool-maker occupation", () => {
  const person = profile("0ae8f83b-9fee-57c7-b773-9ff0a20ffd29");
  expect(person).toMatchObject({
    identity_status: "high_confidence",
    personnel_category: "commissioned_army_officer",
    commissioned_officer: true,
    research_status: "occupation_only_found",
  });
  expect(person.immediate_pre_oss_affiliations).toHaveLength(1);
  expect(person.immediate_pre_oss_affiliations[0]).toMatchObject({
    canonical_organization: "Special Operations Executive",
    relationship_type: "military_assignment",
    immediate_pre_oss: true,
    temporal_basis: "explicit_immediate",
    claim_confidence: "high",
  });
  expect(person.last_civilian_pre_service).toEqual([]);
  expect(person.other_pre_oss_affiliations).toHaveLength(1);
  expect(person.other_pre_oss_affiliations[0]).toMatchObject({
    canonical_organization: null,
    occupation: "tool maker",
    relationship_type: "employment",
    immediate_pre_oss: false,
    claim_confidence: "high",
  });
  expect(JSON.stringify(person)).toContain("source names no employer");
});

test("Batch 551 separates de Gaston's Polish Army predecessor, named casino employer, and unnamed dock work", () => {
  const person = profile("e021fc1f-2e4c-522e-a370-82c4e244a148");
  expect(person).toMatchObject({
    identity_status: "high_confidence",
    personnel_category: "foreign_or_allied_military_personnel",
    commissioned_officer: false,
    allied_or_foreign_personnel: true,
    research_status: "documented_prewar_employer_found",
  });
  expect(person.name_variants).toContain("Zygmunt Barwikowski");
  expect(person.immediate_pre_oss_affiliations).toHaveLength(1);
  expect(person.immediate_pre_oss_affiliations[0]).toMatchObject({
    canonical_organization: "Polish Armed Forces in the West",
    relationship_type: "military_assignment",
    immediate_pre_oss: true,
    temporal_basis: "explicit_immediate",
  });
  expect(person.last_civilian_pre_service).toEqual([]);
  expect(person.other_pre_oss_affiliations).toHaveLength(2);
  expect(person.other_pre_oss_affiliations).toEqual(
    expect.arrayContaining([
      expect.objectContaining({ canonical_organization: "Sopot Casino", role_title: "waiter", temporal_basis: "documented_prewar" }),
      expect.objectContaining({ canonical_organization: null, role_title: "dockworker", temporal_basis: "documented_prewar" }),
    ]),
  );
  expect(person.claims).toHaveLength(4);
});

test("Batch 551 qualifies Claire de Forbin's contemporary resistance affiliation", () => {
  const person = profile("d132e365-dd0d-548c-ab66-73afc2a9dff6");
  expect(person).toMatchObject({
    identity_status: "probable",
    research_status: "needs_identity_review",
    allied_or_foreign_personnel: true,
    manual_review_required: true,
  });
  expect(person.source_records[0]).toMatchObject({ notes_as_indexed: "French" });
  expect(person.immediate_pre_oss_affiliations).toEqual([]);
  expect(person.other_pre_oss_affiliations).toHaveLength(1);
  expect(person.other_pre_oss_affiliations[0]).toMatchObject({
    canonical_organization: "Franco-American Service",
    relationship_type: "volunteer",
    temporal_basis: "temporal_relation_uncertain",
    identity_confidence: "probable",
    claim_confidence: "medium",
    publication_status: "publish_qualified",
  });
  expect(person.archival_file).toMatchObject({ review_priority: "critical" });
  expect(JSON.stringify(person)).toContain("sequence relative to OSS is unverified");
});

test("Batch 551 identifies Alfred DeFlumeri strongly without supplying a pre-OSS employer", () => {
  const person = profile("b40591dd-1d67-55e0-b6cd-c379317d7ad9");
  expect(person).toMatchObject({
    identity_status: "high_confidence",
    personnel_category: "enlisted_army_personnel",
    commissioned_officer: false,
    research_status: "requires_archival_review",
  });
  expect(person.source_records[0]).toMatchObject({ rank_as_indexed: "Sgt" });
  expect(person.immediate_pre_oss_affiliations).toEqual([]);
  expect(person.other_pre_oss_affiliations).toEqual([]);
  expect(person.claims).toHaveLength(1);
  expect(person.claims[0]).toMatchObject({ claim_type: "identity", claim_confidence: "high" });
  expect(person.next_action).toContain("No reliable pre-OSS employer");
});

test("Batch 551 keeps three insufficient identities unassigned", () => {
  const expected = [
    ["b1afbef7-3bd1-5848-9ac8-9bda010d700f", "ambiguous", "needs_identity_review"],
    ["0f9abbe9-8448-5f13-917d-74be1bd88ce4", "ambiguous", "needs_identity_review"],
    ["6639bb45-198a-5d9a-963a-2cd9fd136394", "unresolved", "requires_archival_review"],
  ] as const;
  for (const [id, identityStatus, researchStatus] of expected) {
    const person = profile(id);
    expect(person).toMatchObject({
      identity_status: identityStatus,
      research_status: researchStatus,
      research_attempt_count: 5,
      manual_review_required: true,
    });
    expect(person.immediate_pre_oss_affiliations).toEqual([]);
    expect(person.other_pre_oss_affiliations).toEqual([]);
    expect(person.claims).toEqual([]);
    expect(person.archival_file).toMatchObject({ review_priority: "critical" });
  }
});

test("Batch 551 advances research, affiliation, employer, identity, and archival coverage exactly", () => {
  expect(stats).toMatchObject({
    source_rows: 23978,
    person_entities: 23940,
    possible_duplicate_groups: 248,
    research_attempted_people: 5278,
    research_attempt_percent: 22.0468,
    verified_affiliation_people: 577,
    verified_affiliation_percent: 2.4102,
    verified_employer_people: 256,
    verified_employer_percent: 1.0693,
    archival_review_assessed_people: 5233,
    archival_review_percent: 21.8588,
    public_sources: 3517,
    published_claims: 4146,
  });
  expect(stats.research_status_counts).toMatchObject({
    conflicting_sources: 110,
    documented_prewar_employer_found: 105,
    needs_identity_review: 292,
    no_reliable_result_after_protocol: 196,
    not_started: 18662,
    occupation_only_found: 971,
    requires_archival_review: 3150,
    verified_employer_found: 239,
  });
  expect(stats.identity_status_counts).toEqual({
    ambiguous: 251,
    confirmed: 1083,
    conflicting: 110,
    high_confidence: 721,
    probable: 165,
    unresolved: 21610,
  });
  expect(stats.commissioned_status_counts).toEqual({
    commissioned: 2277,
    not_commissioned: 5995,
    unknown: 15668,
  });
});

test("Batch 551 evidence is citation-linked and private-value free", () => {
  const bundle = JSON.parse(evidence);
  expect(bundle).toMatchObject({ bundle_version: "1.0" });
  expect(bundle.sources).toHaveLength(10);
  expect(bundle.organizations).toHaveLength(4);
  expect(bundle.affiliations).toHaveLength(8);
  expect(bundle.claims).toHaveLength(15);
  expect(bundle.claims.flatMap((claim: { sources: unknown[] }) => claim.sources)).toHaveLength(32);
  expect(bundle.person_updates).toHaveLength(10);
  expect(bundle.research_attempts).toHaveLength(20);
  expect(bundle.claims.filter((claim: { claim_confidence: string }) => claim.claim_confidence === "confirmed")).toHaveLength(3);
  expect(bundle.claims.filter((claim: { claim_confidence: string }) => claim.claim_confidence === "high")).toHaveLength(8);
  expect(bundle.claims.filter((claim: { claim_confidence: string }) => claim.claim_confidence === "medium")).toHaveLength(4);
  expect(evidence).toContain("No reliable pre-OSS employer");
  expect(evidence).toContain("unmapped occupation code");
    expect(evidence).toContain("Probable, not confirmed");
  expect(evidence).not.toMatch(/serial_number|service_number|\b\d{8}\b/);
});

test("Batch 551 gives every public claim an inspectable citation", () => {
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

test.describe("Batch 551 direct profile routes", () => {
  for (const [id, name] of cohort) {
    test(`${name} ${id.slice(0, 8)} renders from a direct route`, async ({ page }) => {
      await page.goto(`./people/${id}/`);
      await expect(page.locator("h1")).toContainText(name);
      await expect(page.locator("body")).toContainText("Box176");
      await expect(page.locator("body")).toContainText("Archival-review priority");
    });
  }
});
