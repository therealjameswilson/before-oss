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
    "../../research/evidence-page-one-hundred-and-nine-through-one-hundred-and-ten-michel-debourbon-through-louis-decastro-pathways_batch-547_2026-09-15.json",
    import.meta.url,
  ),
  "utf8",
);
const profile = (id: string) =>
  people.find((person: { person_id: string }) => person.person_id === id);

const cohort = [
  ["6822fdde-96f2-5cb2-91ad-5dc548654386", "Michel DeBourbon", "9bb2bdd7-9508-57ad-aabc-9f54a77c0ee0", 109, false],
  ["9e82b91d-0988-5da1-9030-fc80083817ed", "John W DeBoy", "b9b98ae4-9d5a-5f1f-9300-b1fbd621a94b", 109, true],
  ["d4e16f1d-26c7-50bc-af15-e715a5452647", "George DeBraux", "f4bb1d65-c13a-576b-9db4-4d4835cb46eb", 109, false],
  ["ec794fab-09d9-5b0f-97fa-3bf75d0c2f44", "Mary E DeBurr", "339552fd-4ec4-5c4c-a55b-262ba3cac1b1", 109, false],
  ["1c7528ce-372c-56d0-942c-8b3ac9ed5d00", "William D DeCamp", "c00d831d-8fcb-57aa-96c9-06b136574f27", 109, false],
  ["fd248546-1bd4-5887-a14c-3536a3ef00ce", "Michael Decapite", "94a892fe-9f44-5248-9412-8481fe11d9e1", 109, true],
  ["7156c52b-686c-5647-9540-f2202e17f7be", "Joseph F DeCarli", "67acdfff-42ce-51fb-83ce-197ceb1428f7", 109, true],
  ["50b068b0-8ce8-5303-bc9e-2f7cd488ca4a", "Rinaldo DeCarolis", "09d50c3b-1067-51fd-8345-30fdd06e1d78", 109, false],
  ["bd2d6ce5-a218-5ab0-a7f7-18b3b9008ec5", "Laura F DeCarvalho", "d3934172-3112-5391-ab75-17f39b9b125c", 109, false],
  ["9939427e-c2fd-5088-9200-89c9d50e5e75", "Louis DeCastro", "17a1ccff-b292-5461-8ce7-a3cea69064ee", 110, false],
] as const;

test("Batch 547 preserves ten Box 175 rows across pages 109-110 and masks three private fields", () => {
  for (const [id, name, sourceRecordId, pdfPage, hasPrivateIdentifier] of cohort) {
    const person = profile(id);
    expect(person).toMatchObject({ display_name: name });
    const sourceRecord = person.source_records.find(
      (record: { source_record_id: string }) => record.source_record_id === sourceRecordId,
    );
    expect(sourceRecord).toMatchObject({
      archive_location: "230/86/29/06",
      box: "175",
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

test("Batch 547 publishes Michel DeBourbon's explicit immediate Army assignment", () => {
  const person = profile("6822fdde-96f2-5cb2-91ad-5dc548654386");
  expect(person).toMatchObject({
    identity_status: "high_confidence",
    personnel_category: "commissioned_army_officer",
    commissioned_officer: true,
    allied_or_foreign_personnel: true,
    research_status: "requires_archival_review",
    research_attempt_count: 5,
  });
  expect(person.name_variants).toContain("Michel de Bourbon-Parma");
  expect(person.immediate_pre_oss_affiliations).toHaveLength(1);
  expect(person.immediate_pre_oss_affiliations[0]).toMatchObject({
    canonical_organization: "United States Army",
    role_title: "second lieutenant",
    relationship_type: "military_assignment",
    immediate_pre_oss: true,
    last_civilian_pre_service: false,
    temporal_basis: "explicit_immediate",
    identity_confidence: "high_confidence",
    claim_confidence: "high",
    publication_status: "published",
  });
  expect(person.last_civilian_pre_service).toEqual([]);
  expect(person.other_pre_oss_affiliations).toEqual([]);
  expect(JSON.stringify(person)).toContain("William Casey");
  expect(JSON.stringify(person)).toContain("After the ceremony");
});

test("Batch 547 preserves John DeBoy's W-versus-M identifier conflict", () => {
  const person = profile("9e82b91d-0988-5da1-9030-fc80083817ed");
  expect(person).toMatchObject({
    identity_status: "conflicting",
    research_status: "conflicting_sources",
    research_attempt_count: 5,
    manual_review_required: true,
  });
  expect(person.archival_file).toMatchObject({ review_priority: "critical" });
  expect(person.immediate_pre_oss_affiliations).toEqual([]);
  expect(person.last_civilian_pre_service).toEqual([]);
  expect(person.other_pre_oss_affiliations).toEqual([]);
  expect(person.claims).toHaveLength(1);
  expect(person.claims[0]).toMatchObject({
    claim_confidence: "conflicting",
    publication_status: "conflicting",
  });
  expect(JSON.stringify(person)).toContain("middle initial M rather than W");
  expect(JSON.stringify(person)).not.toContain("occupation code 025");
});

test("Batch 547 confirms Michael De Capite and qualifies authorship without inventing an employer", () => {
  const person = profile("fd248546-1bd4-5887-a14c-3536a3ef00ce");
  expect(person).toMatchObject({
    identity_status: "confirmed",
    personnel_category: "enlisted_army_personnel",
    commissioned_officer: false,
    research_status: "occupation_only_found",
    research_attempt_count: 5,
  });
  expect(person.name_variants).toContain("Michael De Capite");
  expect(person.immediate_pre_oss_affiliations).toEqual([]);
  expect(person.last_civilian_pre_service).toEqual([]);
  expect(person.other_pre_oss_affiliations).toHaveLength(1);
  expect(person.other_pre_oss_affiliations[0]).toMatchObject({
    canonical_organization: "Common Ground",
    role_title: "contributing author",
    occupation: "author",
    relationship_type: "professional_affiliation",
    temporal_basis: "temporal_relation_uncertain",
    identity_confidence: "confirmed",
    claim_confidence: "high",
    publication_status: "published",
  });
  expect(person.claims).toHaveLength(2);
  expect(JSON.stringify(person)).toContain("Authors, editors, and reporters");
  expect(JSON.stringify(person)).toContain("relation to OSS service remains uncertain");
  expect(person.next_action).toContain("no employer or immediate Army-to-OSS sequence");
});

test("Batch 547 confirms Joseph DeCarli while leaving the occupation undecoded", () => {
  const person = profile("7156c52b-686c-5647-9540-f2202e17f7be");
  expect(person).toMatchObject({
    identity_status: "confirmed",
    personnel_category: "enlisted_army_personnel",
    commissioned_officer: false,
    research_status: "requires_archival_review",
    research_attempt_count: 5,
  });
  expect(person.source_records[0]).toMatchObject({ rank_as_indexed: "T-3" });
  expect(person.immediate_pre_oss_affiliations).toEqual([]);
  expect(person.last_civilian_pre_service).toEqual([]);
  expect(person.other_pre_oss_affiliations).toEqual([]);
  expect(person.claims).toHaveLength(1);
  expect(person.claims[0]).toMatchObject({
    claim_type: "identity",
    claim_confidence: "confirmed",
    publication_status: "published",
  });
  expect(person.next_action).toContain("occupation value remains undecoded");
  expect(JSON.stringify(person)).not.toMatch(/code 078|occupation code 078/);
});

test("Batch 547 withholds William DeCamp's same-name roster candidate", () => {
  const person = profile("1c7528ce-372c-56d0-942c-8b3ac9ed5d00");
  expect(person).toMatchObject({
    identity_status: "ambiguous",
    personnel_category: "enlisted_army_personnel",
    commissioned_officer: false,
    research_status: "needs_identity_review",
    research_attempt_count: 5,
  });
  expect(person.source_records[0]).toMatchObject({ rank_as_indexed: "T/Sgt" });
  expect(person.immediate_pre_oss_affiliations).toEqual([]);
  expect(person.last_civilian_pre_service).toEqual([]);
  expect(person.other_pre_oss_affiliations).toEqual([]);
  expect(person.claims).toEqual([]);
  expect(person.next_action).toContain("second corroborating identifier");
});

test("Batch 547 gives four no-result cases dignified archival next actions", () => {
  for (const id of [
    "d4e16f1d-26c7-50bc-af15-e715a5452647",
    "ec794fab-09d9-5b0f-97fa-3bf75d0c2f44",
    "bd2d6ce5-a218-5ab0-a7f7-18b3b9008ec5",
    "9939427e-c2fd-5088-9200-89c9d50e5e75",
  ]) {
    const person = profile(id);
    expect(person).toMatchObject({
      identity_status: "unresolved",
      research_status: "no_reliable_result_after_protocol",
      research_attempt_count: 5,
      manual_review_required: true,
    });
    expect(person.archival_file).toMatchObject({ review_priority: "high" });
    expect(person.immediate_pre_oss_affiliations).toEqual([]);
    expect(person.last_civilian_pre_service).toEqual([]);
    expect(person.other_pre_oss_affiliations).toEqual([]);
    expect(person.claims).toEqual([]);
    expect(person.next_action).toContain(
      "No reliable pre-OSS employer has yet been identified in the accessible sources reviewed",
    );
  }
});

test("Batch 547 preserves Rinaldo DeCarolis's truncated Italian note literally", () => {
  const person = profile("50b068b0-8ce8-5303-bc9e-2f7cd488ca4a");
  expect(person).toMatchObject({
    identity_status: "unresolved",
    allied_or_foreign_personnel: true,
    research_status: "requires_archival_review",
    research_attempt_count: 5,
  });
  expect(person.source_records[0].notes_as_indexed).toBe("Italian Ci");
  expect(person.archival_file).toMatchObject({ review_priority: "critical" });
  expect(person.claims).toEqual([]);
  expect(person.next_action).toContain("recover the full meaning of 'Italian Ci'");
  expect(person.identity_evidence).toContain("not expanded by inference");
});

test("Batch 547 advances research, affiliation, officer, and archival coverage exactly", () => {
  expect(stats).toMatchObject({
    source_rows: 23978,
    person_entities: 23940,
    possible_duplicate_groups: 248,
    research_attempted_people: 5238,
    research_attempt_percent: 21.8797,
    verified_affiliation_people: 574,
    verified_affiliation_percent: 2.3977,
    verified_employer_people: 254,
    verified_employer_percent: 1.061,
    archival_review_assessed_people: 5193,
    archival_review_percent: 21.6917,
    public_sources: 3496,
    published_claims: 4108,
  });
  expect(stats.research_status_counts).toMatchObject({
    conflicting_sources: 109,
    documented_prewar_employer_found: 104,
    needs_identity_review: 286,
    no_reliable_result_after_protocol: 191,
    not_started: 18702,
    occupation_only_found: 958,
    requires_archival_review: 3137,
  });
  expect(stats.identity_status_counts).toEqual({
    ambiguous: 247,
    confirmed: 1070,
    conflicting: 109,
    high_confidence: 717,
    probable: 163,
    unresolved: 21634,
  });
  expect(stats.commissioned_status_counts).toEqual({
    commissioned: 2275,
    not_commissioned: 5982,
    unknown: 15683,
  });
});

test("Batch 547 evidence is citation-linked, uncertainty-preserving, and private-value free", () => {
  const bundle = JSON.parse(evidence);
  expect(bundle).toMatchObject({ bundle_version: "1.0" });
  expect(bundle.sources).toHaveLength(7);
  expect(bundle.organizations).toHaveLength(2);
  expect(bundle.affiliations).toHaveLength(2);
  expect(bundle.claims).toHaveLength(6);
  expect(bundle.claims.flatMap((claim: { sources: unknown[] }) => claim.sources)).toHaveLength(15);
  expect(bundle.person_updates).toHaveLength(10);
  expect(bundle.research_attempts).toHaveLength(20);
  expect(bundle.claims.filter((claim: { claim_confidence: string }) => claim.claim_confidence === "confirmed")).toHaveLength(2);
  expect(bundle.claims.filter((claim: { claim_confidence: string }) => claim.claim_confidence === "high")).toHaveLength(3);
  expect(bundle.claims.filter((claim: { claim_confidence: string }) => claim.claim_confidence === "conflicting")).toHaveLength(1);
  expect(evidence).toContain("No reliable pre-OSS employer has yet been identified");
  expect(evidence).toContain("temporal_relation_uncertain");
  expect(evidence).toContain("occupation value remains undecoded");
  expect(evidence).not.toMatch(/serial_number|service_number|matched_name/);
});

test("Batch 547 gives every published or conflicting claim an inspectable citation", () => {
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

test.describe("Batch 547 direct profile routes", () => {
  for (const [id, name] of cohort) {
    test(`${name} ${id.slice(0, 8)} renders from a direct route`, async ({ page }) => {
      await page.goto(`./people/${id}/`);
      await expect(page.locator("h1")).toContainText(name);
      await expect(page.locator("body")).toContainText("Box175");
      await expect(page.locator("body")).toContainText("Archival-review priority");
    });
  }
});
