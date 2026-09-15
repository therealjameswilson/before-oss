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
    "../../research/evidence-page-one-hundred-and-ten-george-l-decoster-through-joseph-l-dees-pathways_batch-549_2026-09-15.json",
    import.meta.url,
  ),
  "utf8",
);
const profile = (id: string) =>
  people.find((person: { person_id: string }) => person.person_id === id);

const cohort = [
  ["0c3b93b3-cd8e-5132-a69b-d7d060bcc2fa", "George L DeCoster", "acc9dcc7-1779-5c1b-aa2f-7ef384e1016d", true],
  ["507e3333-8091-5dd5-b422-4d04602d1561", "Calvin C DeCray", "1f75126e-8d86-53a4-8f6b-4049c20805fd", true],
  ["7fa4bc70-a774-54d4-af19-34e2c00e38b5", "Jehan DeCrequy", "e3a51a2d-9db9-5ecd-81d7-9880d799755a", false],
  ["bc7f7962-6444-5f08-a25c-b30c761fbdbb", "Fiore DeCristoforo", "b11d63d6-5cc6-5c48-bcdb-996645dea34d", true],
  ["bbffe1af-842a-5f7c-8d76-7c3db4f1eeb9", "Nicholas G D'Ecsery", "65775cc2-b03e-5835-af03-48902a6ecb2a", true],
  ["ae3006b4-5cd8-5897-aeff-4488fad19329", "Leonard Decunha", "661ecacb-35dc-54b8-8a72-9d066ef799b1", true],
  ["4afb6f23-b8da-5087-a5ab-f4b996931970", "Charles J DeDero", "3631c915-4f03-5ada-a2d0-339b77582f1e", true],
  ["84225e99-8651-5db6-9ea2-05207fd13760", "John Dedes", "7da452bd-ceba-59e9-83b4-b4471d0ee008", false],
  ["e3702c63-e110-5b09-ae79-52529bf7e504", "E T Deerfield", "ebb19cbd-d347-551e-ac4f-ce9b5df6527e", false],
  ["34e89063-16a3-58d0-abf5-374f570fdda8", "Joseph L Dees", "08135339-b3ea-5f53-8369-2100449871b8", false],
] as const;

test("Batch 549 preserves ten page 110 rows in Box 176 and masks six private fields", () => {
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

test("Batch 549 publishes three identifier-confirmed Army occupations without inventing employers", () => {
  const expected = [
    ["bc7f7962-6444-5f08-a25c-b30c761fbdbb", "Laundering occupations, apparel and other articles", "1943-08-27"],
    ["bbffe1af-842a-5f7c-8d76-7c3db4f1eeb9", "Kitchen workers in hotels, restaurants, railroads, steamships, etc., n. e. c.", "1941-09-26"],
    ["ae3006b4-5cd8-5897-aeff-4488fad19329", "Financial institution clerks, n. e. c.", "1943-04-20"],
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

test("Batch 549 preserves Jehan DeCrequy's rank and French note without expanding the abbreviation", () => {
  const person = profile("7fa4bc70-a774-54d4-af19-34e2c00e38b5");
  expect(person).toMatchObject({
    identity_status: "unresolved",
    personnel_category: "foreign_or_allied_military_personnel",
    commissioned_officer: true,
    allied_or_foreign_personnel: true,
    research_status: "requires_archival_review",
    research_attempt_count: 5,
  });
  expect(person.source_records[0]).toMatchObject({ rank_as_indexed: "S/Lt", notes_as_indexed: "French" });
  expect(person.archival_file).toMatchObject({ review_priority: "critical" });
  expect(person.claims).toEqual([]);
  expect(person.identity_evidence).toContain("preserved without silent expansion");
});

test("Batch 549 exposes the DeDero and De Fero conflict without carrying over an occupation", () => {
  const person = profile("4afb6f23-b8da-5087-a5ab-f4b996931970");
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
    claim_type: "identity",
    claim_confidence: "conflicting",
    publication_status: "conflicting",
  });
  expect(JSON.stringify(person)).toContain("De Fero rather than DeDero");
  expect(JSON.stringify(person)).toContain("No occupation or other Army detail is assigned");
});

test("Batch 549 retains the commissioned classifications without identity overreach", () => {
  for (const id of [
    "0c3b93b3-cd8e-5132-a69b-d7d060bcc2fa",
    "507e3333-8091-5dd5-b422-4d04602d1561",
  ]) {
    const person = profile(id);
    expect(person).toMatchObject({
      identity_status: "unresolved",
      personnel_category: "commissioned_army_officer",
      commissioned_officer: true,
      research_status: "requires_archival_review",
      research_attempt_count: 5,
    });
    expect(person.claims).toEqual([]);
    expect(person.archival_file).toMatchObject({ review_priority: "high" });
  }
});

test("Batch 549 rejects all five E T Deerfield newspaper false positives", () => {
  const person = profile("e3702c63-e110-5b09-ae79-52529bf7e504");
  expect(person).toMatchObject({
    identity_status: "unresolved",
    research_status: "requires_archival_review",
    research_attempt_count: 5,
  });
  expect(person.archival_file).toMatchObject({ review_priority: "critical" });
  expect(person.claims).toEqual([]);
  expect(person.identity_evidence).toContain("Five LoC hits were reviewed and rejected");
  expect(person.next_action).toContain("recover the full given names");
});

test("Batch 549 advances research, identity, conflict, officer, and archival coverage exactly", () => {
  expect(stats).toMatchObject({
    source_rows: 23978,
    person_entities: 23940,
    possible_duplicate_groups: 248,
    research_attempted_people: 5258,
    research_attempt_percent: 21.9632,
    verified_affiliation_people: 575,
    verified_affiliation_percent: 2.4018,
    verified_employer_people: 255,
    verified_employer_percent: 1.0652,
    archival_review_assessed_people: 5213,
    archival_review_percent: 21.7753,
    public_sources: 3503,
    published_claims: 4123,
  });
  expect(stats.research_status_counts).toMatchObject({
    conflicting_sources: 110,
    needs_identity_review: 287,
    no_reliable_result_after_protocol: 196,
    not_started: 18682,
    occupation_only_found: 964,
    requires_archival_review: 3143,
    verified_employer_found: 239,
  });
  expect(stats.identity_status_counts).toEqual({
    ambiguous: 248,
    confirmed: 1076,
    conflicting: 110,
    high_confidence: 718,
    probable: 163,
    unresolved: 21625,
  });
  expect(stats.commissioned_status_counts).toEqual({
    commissioned: 2276,
    not_commissioned: 5988,
    unknown: 15676,
  });
});

test("Batch 549 evidence is citation-linked, uncertainty-preserving, and private-value free", () => {
  const bundle = JSON.parse(evidence);
  expect(bundle).toMatchObject({ bundle_version: "1.0" });
  expect(bundle.sources).toHaveLength(3);
  expect(bundle.organizations).toHaveLength(0);
  expect(bundle.affiliations).toHaveLength(3);
  expect(bundle.claims).toHaveLength(7);
  expect(bundle.claims.flatMap((claim: { sources: unknown[] }) => claim.sources)).toHaveLength(14);
  expect(bundle.person_updates).toHaveLength(10);
  expect(bundle.research_attempts).toHaveLength(20);
  expect(bundle.claims.filter((claim: { claim_confidence: string }) => claim.claim_confidence === "confirmed")).toHaveLength(3);
  expect(bundle.claims.filter((claim: { claim_confidence: string }) => claim.claim_confidence === "medium")).toHaveLength(3);
  expect(bundle.claims.filter((claim: { claim_confidence: string }) => claim.claim_confidence === "conflicting")).toHaveLength(1);
  expect(evidence).toContain("No reliable pre-OSS employer has yet been identified");
  expect(evidence).toContain("Five current LoC candidates were inspected and rejected");
  expect(evidence).toContain("DeDero and De Fero are substantively different surname readings");
  expect(evidence).not.toMatch(/serial_number|service_number|matched_name/);
});

test("Batch 549 gives every public or conflicting claim an inspectable citation", () => {
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

test.describe("Batch 549 direct profile routes", () => {
  for (const [id, name] of cohort) {
    test(`${name} ${id.slice(0, 8)} renders from a direct route`, async ({ page }) => {
      await page.goto(`./people/${id}/`);
      await expect(page.locator("h1")).toContainText(name);
      await expect(page.locator("body")).toContainText("Box176");
      await expect(page.locator("body")).toContainText("Archival-review priority");
    });
  }
});
