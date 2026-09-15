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
    "../../research/evidence-page-one-hundred-and-ten-kathleen-m-dees-through-serge-defleury-pathways_batch-550_2026-09-15.json",
    import.meta.url,
  ),
  "utf8",
);
const profile = (id: string) =>
  people.find((person: { person_id: string }) => person.person_id === id);

const cohort = [
  ["b8fa3678-4d13-549c-82be-699fae72e068", "Kathleen M Dees", "99b98178-015c-5503-9a09-098a25d7f98b", false],
  ["ad72572e-e95d-597d-9fb8-57f5d403dc96", "Albert W Deese", "14b60a40-69d1-55b1-aefe-149fb2127a73", true],
  ["cbc4ba1a-3b44-5bce-86b7-ee2a0b704627", "Harry A Defarrari", "0f9ff783-8f0f-51e9-af69-92e70c4731f0", false],
  ["0cb4ff63-81cc-5af0-8eff-03be5c5d9f31", "Slyvester S Defazio", "b6f78fe6-ca2e-55e8-a2b1-b2d46599a45d", true],
  ["20af0017-43a2-5f0d-830c-e3e826f0f843", "Joseph A DeFelice", "85ad4f17-f6d6-5a6e-9dd4-b0e843feca54", true],
  ["f6cd240e-4f14-5943-8928-274efa90e495", "Maurice Defenin", "77f6edf9-1859-5a84-bcf1-ca3f4fd099f9", false],
  ["0bd25d2f-bcc2-5550-ac96-eb032a23bc2f", "Nick DeFeo", "10108627-62ff-560f-829b-9e76d4704a88", true],
  ["a8975665-2512-568c-851d-be081485e513", "Edward G Defiore", "4c6d89ba-9458-5f58-8f2c-37293469753a", false],
  ["d95b7ff8-bad3-5b0e-81cc-d5643ec8b176", "Joseph Defire", "0f748a1b-627c-5fe2-8c0f-154387dc6278", false],
  ["72f79993-3867-52e9-becc-dc7e5489e166", "Serge Defleury", "2b1aa248-a4c3-564d-ba11-5fa3ec9fc956", false],
] as const;

test("Batch 550 preserves ten page 110 rows in Box 176 and masks four private fields", () => {
  for (const [id, name, sourceRecordId, hasPrivateIdentifier] of cohort) {
    const person = profile(id);
    expect(person).toMatchObject({ display_name: name });
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

test("Batch 550 publishes four identifier-confirmed Army occupations without inventing employers", () => {
  const expected = [
    ["ad72572e-e95d-597d-9fb8-57f5d403dc96", "Textile manufacturing occupations, n. e. c.", "1942-10-16"],
    ["0cb4ff63-81cc-5af0-8eff-03be5c5d9f31", "Firemen, other than process firemen", "1941-09-29"],
    ["20af0017-43a2-5f0d-830c-e3e826f0f843", "Aircraft building occupations, n. e. c.", "1943-02-12"],
    ["0bd25d2f-bcc2-5550-ac96-eb032a23bc2f", "Machine shop and related occupations, n. e. c.", "1943-03-26"],
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

test("Batch 550 preserves Slyvester Defazio's indexed spelling beside the Army variant", () => {
  const person = profile("0cb4ff63-81cc-5af0-8eff-03be5c5d9f31");
  expect(person.display_name).toBe("Slyvester S Defazio");
  expect(person.name_variants).toContain("Sylvester S De Fazio");
  expect(person.identity_evidence).toContain("transposes");
});

test("Batch 550 qualifies Maurice Defenin's rare-name candidate without assigning its biography", () => {
  const person = profile("f6cd240e-4f14-5943-8928-274efa90e495");
  expect(person).toMatchObject({
    identity_status: "probable",
    personnel_category: "foreign_or_allied_military_personnel",
    commissioned_officer: true,
    allied_or_foreign_personnel: true,
    research_status: "needs_identity_review",
    research_attempt_count: 5,
    manual_review_required: true,
  });
  expect(person.source_records[0]).toMatchObject({ rank_as_indexed: "Lt", notes_as_indexed: "French" });
  expect(person.archival_file).toMatchObject({ review_priority: "critical" });
  expect(person.claims).toEqual([]);
  expect(person.name_variants).toContain("Maurice Défenin (candidate only)");
  expect(person.identity_evidence).toContain("Neither source crosswalks Box 176");
});

test("Batch 550 keeps Serge Defleury ambiguous and its postwar namesake unassigned", () => {
  const person = profile("72f79993-3867-52e9-becc-dc7e5489e166");
  expect(person).toMatchObject({
    identity_status: "ambiguous",
    research_status: "needs_identity_review",
    research_attempt_count: 5,
    manual_review_required: true,
  });
  expect(person.archival_file).toMatchObject({ review_priority: "critical" });
  expect(person.claims).toEqual([]);
  expect(person.name_variants).toContain("Serge de Fleury (candidate only)");
  expect(person.identity_evidence).toContain("establishes pre-OSS employment");
});

test("Batch 550 leaves four no-match identities unresolved with archival guidance", () => {
  for (const id of [
    "b8fa3678-4d13-549c-82be-699fae72e068",
    "cbc4ba1a-3b44-5bce-86b7-ee2a0b704627",
    "a8975665-2512-568c-851d-be081485e513",
    "d95b7ff8-bad3-5b0e-81cc-d5643ec8b176",
  ]) {
    const person = profile(id);
    expect(person).toMatchObject({
      identity_status: "unresolved",
      research_status: "requires_archival_review",
      research_attempt_count: 5,
    });
    expect(person.claims).toEqual([]);
    expect(person.archival_file.review_priority).toMatch(/high|critical/);
  }
});

test("Batch 550 advances research, identity, officer, and archival coverage exactly", () => {
  expect(stats).toMatchObject({
    source_rows: 23978,
    person_entities: 23940,
    possible_duplicate_groups: 248,
    research_attempted_people: 5268,
    research_attempt_percent: 22.005,
    verified_affiliation_people: 575,
    verified_affiliation_percent: 2.4018,
    verified_employer_people: 255,
    verified_employer_percent: 1.0652,
    archival_review_assessed_people: 5223,
    archival_review_percent: 21.817,
    public_sources: 3507,
    published_claims: 4131,
  });
  expect(stats.research_status_counts).toMatchObject({
    conflicting_sources: 110,
    needs_identity_review: 289,
    no_reliable_result_after_protocol: 196,
    not_started: 18672,
    occupation_only_found: 968,
    requires_archival_review: 3147,
    verified_employer_found: 239,
  });
  expect(stats.identity_status_counts).toEqual({
    ambiguous: 249,
    confirmed: 1080,
    conflicting: 110,
    high_confidence: 718,
    probable: 164,
    unresolved: 21619,
  });
  expect(stats.commissioned_status_counts).toEqual({
    commissioned: 2277,
    not_commissioned: 5992,
    unknown: 15671,
  });
});

test("Batch 550 evidence is citation-linked, access-respecting, and private-value free", () => {
  const bundle = JSON.parse(evidence);
  expect(bundle).toMatchObject({ bundle_version: "1.0" });
  expect(bundle.sources).toHaveLength(4);
  expect(bundle.organizations).toHaveLength(0);
  expect(bundle.affiliations).toHaveLength(4);
  expect(bundle.claims).toHaveLength(8);
  expect(bundle.claims.flatMap((claim: { sources: unknown[] }) => claim.sources)).toHaveLength(20);
  expect(bundle.person_updates).toHaveLength(10);
  expect(bundle.research_attempts).toHaveLength(20);
  expect(bundle.claims.filter((claim: { claim_confidence: string }) => claim.claim_confidence === "confirmed")).toHaveLength(4);
  expect(bundle.claims.filter((claim: { claim_confidence: string }) => claim.claim_confidence === "medium")).toHaveLength(4);
  expect(evidence).toContain("No reliable pre-OSS employer has yet been identified");
  expect(evidence).toContain("reading-room-only item");
  expect(evidence).toContain("candidate only");
  expect(evidence).not.toMatch(/serial_number|service_number|\b\d{8}\b/);
});

test("Batch 550 gives every public claim an inspectable citation", () => {
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

test.describe("Batch 550 direct profile routes", () => {
  for (const [id, name] of cohort) {
    test(`${name} ${id.slice(0, 8)} renders from a direct route`, async ({ page }) => {
      await page.goto(`./people/${id}/`);
      await expect(page.locator("h1")).toContainText(name);
      await expect(page.locator("body")).toContainText("Box176");
      await expect(page.locator("body")).toContainText("Archival-review priority");
    });
  }
});
