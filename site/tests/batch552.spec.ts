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
    "../../research/evidence-pages-one-hundred-and-ten-and-one-hundred-and-eleven-vincent-r-degennaro-through-jean-deguerrif-pathways_batch-552_2026-09-15.json",
    import.meta.url,
  ),
  "utf8",
);
const profile = (id: string) =>
  people.find((person: { person_id: string }) => person.person_id === id);

const cohort = [
  ["d228bcac-533a-5689-953b-7822430cf3e4", "Vincent R DeGennaro", "7fb60f40-701f-541c-aa38-d08a3970e385", 110, "176", true],
  ["9de054f1-a25e-5a4c-8e1f-cdfe7c41f51f", "Henry Degeynst", "4174d82d-2867-53a2-8113-bbb4b00ee899", 110, "176", false],
  ["0c1df448-de13-5f60-9f1b-538819cc017d", "Grace M Degli-Unomini", "46c2c977-8837-5082-a51b-8728c6af6ee9", 110, "176", true],
  ["f7ef5297-30fc-5f37-a798-6b767e902d45", "Antonio Degrassi", "395f60fe-c637-522e-95a9-28048ce980bc", 110, "176", false],
  ["70c32830-0294-5a88-9c47-c85fa4e0c1e5", "Julian DeGray", "c06431b7-0059-5932-8444-7840eca73753", 110, "177", false],
  ["bd4b10f8-d556-5b9d-ad10-32fbb7693e8c", "Sebastian DeGrazia", "fe2e62db-5388-51ee-8556-33704a4f0bd7", 111, "177", false],
  ["b3cffe67-04dd-5e90-a952-1ccf1499fa7e", "Don L DeGroat", "25800f60-912a-5a96-81a3-23b2f7c335e4", 111, "177", true],
  ["3f05dbc5-eae0-575f-8812-4825352309bb", "Herbert L DeGroot", "83e2b6b7-0897-5752-a0aa-cd74a4b1e7fa", 111, "177", true],
  ["022f7e62-701b-57fa-a6ab-50f4949fd79c", "Andre Degrose", "37eaa3e0-0322-5c16-b2f3-0b10d8f507d8", 111, "176", false],
  ["52dbcdc8-304c-5376-89a2-3d65b7f474c8", "Jean DeGuerrif", "8b13ef93-81ff-54e0-8567-5a50b7f44ebe", 111, "177", false],
] as const;

test("Batch 552 preserves ten rows across pages 110-111 and masks four private fields", () => {
  for (const [id, name, sourceRecordId, pdfPage, box, hasPrivateIdentifier] of cohort) {
    const person = profile(id);
    expect(person).toMatchObject({ display_name: name, research_attempt_count: 5 });
    const sourceRecord = person.source_records.find(
      (record: { source_record_id: string }) => record.source_record_id === sourceRecordId,
    );
    expect(sourceRecord).toMatchObject({
      archive_location: "230/86/29/07",
      box,
      pdf_page: pdfPage,
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

test("Batch 552 publishes two identifier-confirmed Army occupations without inventing employers", () => {
  const expected = [
    ["d228bcac-533a-5689-953b-7822430cf3e4", "Stenographers and typists", "1942-09-18"],
    ["3f05dbc5-eae0-575f-8812-4825352309bb", "Motion picture projectionists", "1944-01-25"],
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
      relationship_type: "unknown",
      temporal_basis: "strongly_date_bounded",
      identity_confidence: "confirmed",
      claim_confidence: "medium",
      publication_status: "publish_qualified",
    });
    expect(person.claims).toHaveLength(2);
    expect(JSON.stringify(person)).toContain("no employer is named");
  }
});

test("Batch 552 keeps Sebastian DeGrazia's two FCC assignments distinct from civilian employment", () => {
  const person = profile("bd4b10f8-d556-5b9d-ad10-32fbb7693e8c");
  expect(person).toMatchObject({
    identity_status: "high_confidence",
    personnel_category: "unknown_or_indeterminate",
    commissioned_officer: null,
    research_status: "completed",
  });
  expect(person.immediate_pre_oss_affiliations).toHaveLength(1);
  expect(person.immediate_pre_oss_affiliations[0]).toMatchObject({
    canonical_organization: "Foreign Broadcast Intelligence Service, Federal Communications Commission",
    relationship_type: "government_assignment",
    immediate_pre_oss: true,
    last_civilian_pre_service: false,
    temporal_basis: "probable_immediate",
    claim_confidence: "high",
  });
  expect(person.last_civilian_pre_service).toEqual([]);
  expect(person.other_pre_oss_affiliations).toHaveLength(1);
  expect(person.other_pre_oss_affiliations[0]).toMatchObject({
    canonical_organization: "Foreign Broadcast Monitoring Service, Federal Communications Commission",
    role_title: "propaganda analyst",
    relationship_type: "government_assignment",
    temporal_basis: "documented_prewar",
    claim_confidence: "high",
  });
  expect(person.claims).toHaveLength(3);
  expect(JSON.stringify(person)).toContain("not a civilian employer");
});

test("Batch 552 qualifies Julian DeGray's Bennington College job and does not promote it to immediate", () => {
  const person = profile("70c32830-0294-5a88-9c47-c85fa4e0c1e5");
  expect(person).toMatchObject({
    identity_status: "probable",
    research_status: "documented_prewar_employer_found",
    manual_review_required: true,
  });
  expect(person.immediate_pre_oss_affiliations).toEqual([]);
  expect(person.last_civilian_pre_service).toEqual([]);
  expect(person.other_pre_oss_affiliations).toHaveLength(1);
  expect(person.other_pre_oss_affiliations[0]).toMatchObject({
    canonical_organization: "Bennington College",
    organization_name_as_found: "Bennington college",
    role_title: "music teacher",
    occupation: "pianist and music teacher",
    relationship_type: "employment",
    temporal_basis: "documented_prewar",
    identity_confidence: "probable",
    claim_confidence: "medium",
    publication_status: "publish_qualified",
  });
  expect(person.archival_file).toMatchObject({ review_priority: "critical" });
    expect(JSON.stringify(person)).toContain("Neither source mentions OSS");
});

test("Batch 552 exposes Don L DeGroat's identifier conflict without assigning the Army unit", () => {
  const person = profile("b3cffe67-04dd-5e90-a952-1ccf1499fa7e");
  expect(person).toMatchObject({
    identity_status: "conflicting",
    personnel_category: "enlisted_army_personnel",
    commissioned_officer: false,
    research_status: "needs_identity_review",
    manual_review_required: true,
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
  expect(person.claims[0].sources).toHaveLength(3);
  expect(person.identity_evidence).toContain("different protected identifier");
  expect(JSON.stringify(person)).toContain("no Army identity or unit is assigned");
});

test("Batch 552 leaves five completed-protocol profiles unresolved with Box guidance", () => {
  const expected = [
    ["9de054f1-a25e-5a4c-8e1f-cdfe7c41f51f", "foreign_or_allied_military_personnel", true],
    ["0c1df448-de13-5f60-9f1b-538819cc017d", "unknown_or_indeterminate", null],
    ["f7ef5297-30fc-5f37-a798-6b767e902d45", "unknown_or_indeterminate", null],
    ["022f7e62-701b-57fa-a6ab-50f4949fd79c", "foreign_or_allied_military_personnel", true],
    ["52dbcdc8-304c-5376-89a2-3d65b7f474c8", "unknown_or_indeterminate", null],
  ] as const;
  for (const [id, category, allied] of expected) {
    const person = profile(id);
    expect(person).toMatchObject({
      identity_status: "unresolved",
      personnel_category: category,
      commissioned_officer: null,
      allied_or_foreign_personnel: allied,
      research_status: "no_reliable_result_after_protocol",
      research_attempt_count: 5,
      manual_review_required: true,
    });
    expect(person.archival_file).toMatchObject({ review_priority: "critical" });
    expect(person.immediate_pre_oss_affiliations).toEqual([]);
    expect(person.last_civilian_pre_service).toEqual([]);
    expect(person.other_pre_oss_affiliations).toEqual([]);
    expect(person.claims).toEqual([]);
    expect(person.next_action).toContain(
      "No reliable pre-OSS employer has yet been identified in the accessible sources reviewed.",
    );
  }
});

test("Batch 552 advances research and affiliation coverage without inflating employer coverage", () => {
  expect(stats).toMatchObject({
    source_rows: 23978,
    person_entities: 23940,
    possible_duplicate_groups: 248,
    research_attempted_people: 5288,
    research_attempt_percent: 22.0886,
    verified_affiliation_people: 578,
    verified_affiliation_percent: 2.4144,
    verified_employer_people: 256,
    verified_employer_percent: 1.0693,
    archival_review_assessed_people: 5243,
    archival_review_percent: 21.9006,
    public_sources: 3528,
    published_claims: 4156,
  });
  expect(stats.research_status_counts).toMatchObject({
    completed: 146,
    documented_prewar_employer_found: 106,
    needs_identity_review: 293,
    no_reliable_result_after_protocol: 201,
    not_started: 18652,
    occupation_only_found: 973,
    requires_archival_review: 3150,
    verified_employer_found: 239,
  });
  expect(stats.identity_status_counts).toEqual({
    ambiguous: 251,
    confirmed: 1085,
    conflicting: 111,
    high_confidence: 722,
    probable: 166,
    unresolved: 21605,
  });
  expect(stats.commissioned_status_counts).toEqual({
    commissioned: 2277,
    not_commissioned: 5996,
    unknown: 15667,
  });
});

test("Batch 552 evidence is citation-linked, qualified, and private-value free", () => {
  const bundle = JSON.parse(evidence);
  expect(bundle).toMatchObject({ bundle_version: "1.0" });
  expect(bundle.sources).toHaveLength(11);
  expect(bundle.organizations).toHaveLength(3);
  expect(bundle.affiliations).toHaveLength(5);
  expect(bundle.claims).toHaveLength(10);
  expect(bundle.claims.flatMap((claim: { sources: unknown[] }) => claim.sources)).toHaveLength(29);
  expect(bundle.person_updates).toHaveLength(10);
  expect(bundle.research_attempts).toHaveLength(20);
  expect(bundle.claims.filter((claim: { claim_confidence: string }) => claim.claim_confidence === "confirmed")).toHaveLength(2);
  expect(bundle.claims.filter((claim: { claim_confidence: string }) => claim.claim_confidence === "high")).toHaveLength(3);
  expect(bundle.claims.filter((claim: { claim_confidence: string }) => claim.claim_confidence === "medium")).toHaveLength(4);
  expect(bundle.claims.filter((claim: { claim_confidence: string }) => claim.claim_confidence === "conflicting")).toHaveLength(1);
  expect(evidence).toContain("No reliable pre-OSS employer");
  expect(evidence).toContain("no Army identity or unit is assigned");
  expect(evidence).not.toMatch(/serial_number|service_number|\b\d{8}\b/);
});

test("Batch 552 gives every public or conflicting claim an inspectable citation", () => {
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

test.describe("Batch 552 direct profile routes", () => {
  for (const [id, name, , , box] of cohort) {
    test(`${name} ${id.slice(0, 8)} renders from a direct route`, async ({ page }) => {
      await page.goto(`./people/${id}/`);
      await expect(page.locator("h1")).toContainText(name);
      await expect(page.locator("body")).toContainText(`Box${box}`);
      await expect(page.locator("body")).toContainText("Archival-review priority");
    });
  }
});
