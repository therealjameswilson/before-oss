import { expect, test } from "@playwright/test";
import fs from "node:fs";

const people = JSON.parse(
  fs.readFileSync(
    new URL("../src/data/generated/people.json", import.meta.url),
    "utf8",
  ),
);
const stats = JSON.parse(
  fs.readFileSync(
    new URL("../src/data/generated/stats.json", import.meta.url),
    "utf8",
  ),
);
const evidence = fs.readFileSync(
  new URL(
    "../../research/evidence-page-one-hundred-and-fourteen-bernard-f-deren-through-king-derr-pathways_batch-569_2026-09-16.json",
    import.meta.url,
  ),
  "utf8",
);
const profile = (id: string) =>
  people.find((person: { person_id: string }) => person.person_id === id);

const cohort = [
  ["2c682422-1d95-53d6-a84e-b8884421e528", "Bernard F Deren", "00fe108e-5972-52ba-bef5-23b80f36b0b2", null, true],
  ["7ad6d261-8790-5f7c-97c7-011d68f74545", "Bernice A Deren", "765dd68f-b5e7-50ab-9ed0-370902fe7986", null, false],
  ["ae687867-a68a-5862-ad87-d1e53e54985f", "Henrietta E DeRestie", "cf91bbc5-2cfa-5ae7-87d0-87f0f46bca3f", "T-4", true],
  ["acb4990d-bce9-516b-a728-e67e0072ab9c", "Marinus G DeRidder", "cd223f5b-833c-5f39-a32e-2591ae3b5e2c", null, true],
  ["8095d5fa-1ca2-5958-b572-0fa680d9a5f9", "William B Dern", "9bcc5978-be06-5f32-9b28-ffa6b02a6f2b", "Capt", true],
  ["184dc31a-d4f1-5d1a-8e50-980c572317da", "Francis J Derocher", "6731018c-cdfe-561a-8058-147fb3c16d08", null, true],
  ["61b7ea6d-f2a1-5950-9c24-af75d23eeba4", "Maurice DeRome", "d88579cf-3968-55b5-8802-b6fda654647f", "LtCol", false],
  ["3f2d6473-cb73-5600-85a7-30074e21e3a4", "Richard DeRoussyDeD", "2b16cd62-2689-5c65-8da1-6afa39ebf656", "Lt", false],
  ["b78e7a77-6fd2-5010-bf78-0823ce79b9c8", "Charles R Derr", "09205bdf-78ee-5f19-b2d7-225d05536677", null, true],
  ["e1fd5b65-db48-5804-ade3-fe98fb8fa179", "King Derr", "009a1387-b583-5c8f-b5f5-4e7f286fbc7d", null, false],
] as const;

test("Batch 569 preserves page 114 rows 29-38 and masks all six private values", () => {
  for (const [id, name, sourceRecordId, rank, hasPrivateIdentifier] of cohort) {
    const person = profile(id);
    expect(person.display_name).toBe(name);
    expect(person.research_attempt_count).toBe(5);
    const sourceRecord = person.source_records.find(
      (record: { source_record_id: string }) =>
        record.source_record_id === sourceRecordId,
    );
    expect(sourceRecord).toMatchObject({
      archive_location: "230/86/29/07",
      box: "181",
      pdf_page: 114,
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

test("Batch 569 publishes only broad Army-entry occupation categories for DeRidder and Derocher", () => {
  const deridder = profile("acb4990d-bce9-516b-a728-e67e0072ab9c");
  expect(deridder).toMatchObject({
    identity_status: "confirmed",
    research_status: "occupation_only_found",
    personnel_category: "enlisted_army_personnel",
    commissioned_officer: false,
  });
  expect(deridder.name_variants).toContain("Marinus G DeRidder Jr.");
  expect(deridder.immediate_pre_oss_affiliations).toEqual([]);
  expect(deridder.last_civilian_pre_service).toEqual([]);
  expect(deridder.other_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      occupation: "Chauffeur or bus, taxi, truck, or tractor driver category",
      relationship_type: "unknown",
      end_date: "1941-10-02",
      temporal_basis: "strongly_date_bounded",
      identity_confidence: "confirmed",
      claim_confidence: "medium",
    }),
  ]);

  const derocher = profile("184dc31a-d4f1-5d1a-8e50-980c572317da");
  expect(derocher).toMatchObject({
    identity_status: "confirmed",
    research_status: "occupation_only_found",
    personnel_category: "enlisted_army_personnel",
    commissioned_officer: false,
  });
  expect(derocher.immediate_pre_oss_affiliations).toEqual([]);
  expect(derocher.last_civilian_pre_service).toEqual([]);
  expect(derocher.other_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      occupation: "Occupation in the production of paint and varnish",
      relationship_type: "unknown",
      end_date: "1942-12-04",
      temporal_basis: "strongly_date_bounded",
      identity_confidence: "confirmed",
      claim_confidence: "medium",
    }),
  ]);
  expect(JSON.stringify([deridder, derocher])).toContain(
    "No reliable named pre-OSS employer has yet been identified",
  );
});

test("Batch 569 confirms DeRestie and de Rome without inflating their employer record", () => {
  const derestie = profile("ae687867-a68a-5862-ad87-d1e53e54985f");
  expect(derestie).toMatchObject({
    identity_status: "high_confidence",
    research_status: "requires_archival_review",
    personnel_category: "enlisted_army_personnel",
    commissioned_officer: false,
  });
  expect(derestie.immediate_pre_oss_affiliations).toEqual([]);
  expect(derestie.last_civilian_pre_service).toEqual([]);
  expect(JSON.stringify(derestie)).toContain(
    "T/4 Henrietta E. DeRestie — Approved",
  );

  const derome = profile("61b7ea6d-f2a1-5950-9c24-af75d23eeba4");
  expect(derome).toMatchObject({
    identity_status: "confirmed",
    research_status: "requires_archival_review",
    personnel_category: "foreign_or_allied_military_personnel",
    commissioned_officer: true,
    allied_or_foreign_personnel: true,
  });
  expect(derome.immediate_pre_oss_affiliations).toEqual([]);
  expect(derome.last_civilian_pre_service).toEqual([]);
  expect(derome.other_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      canonical_organization: "Le Régiment de Maisonneuve",
      relationship_type: "military_assignment",
      start_date: "1935",
      end_date: "1939-09",
      temporal_basis: "documented_prewar",
      claim_confidence: "medium",
    }),
  ]);
  expect(JSON.stringify(derome)).toContain(
    "No reliable civilian pre-OSS employer has yet been identified",
  );
});

test("Batch 569 preserves the truncated de Roussy name and much earlier military service as qualified evidence", () => {
  const roussy = profile("3f2d6473-cb73-5600-85a7-30074e21e3a4");
  expect(roussy).toMatchObject({
    display_name: "Richard DeRoussyDeD",
    identity_status: "high_confidence",
    research_status: "requires_archival_review",
    personnel_category: "commissioned_army_officer",
    commissioned_officer: true,
  });
  expect(roussy.name_variants).toContain("Richard de Roussy de Sales");
  expect(roussy.immediate_pre_oss_affiliations).toEqual([]);
  expect(roussy.last_civilian_pre_service).toEqual([]);
  expect(roussy.other_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      canonical_organization: "French Army artillery",
      role_title: "Noncommissioned officer",
      relationship_type: "military_assignment",
      temporal_basis: "documented_prewar",
      identity_confidence: "high_confidence",
      claim_confidence: "medium",
    }),
  ]);
  expect(JSON.stringify(roussy)).toContain(
    "No reliable immediate pre-OSS employer or affiliation has yet been identified",
  );
});

test("Batch 569 advances attempted coverage while verified-employer coverage stays unchanged", () => {
  expect(stats).toMatchObject({
    source_rows: 23978,
    person_entities: 23940,
    possible_duplicate_groups: 254,
    research_attempted_people: 5456,
    research_attempt_percent: 22.7903,
    verified_affiliation_people: 586,
    verified_affiliation_percent: 2.4478,
    verified_employer_people: 259,
    verified_employer_percent: 1.0819,
    archival_review_assessed_people: 5411,
    archival_review_percent: 22.6023,
    public_sources: 3637,
    published_claims: 4417,
  });
  expect(stats.research_status_counts).toMatchObject({
    conflicting_sources: 114,
    documented_prewar_employer_found: 111,
    needs_identity_review: 322,
    not_started: 18484,
    occupation_only_found: 1011,
    requires_archival_review: 3229,
    verified_employer_found: 242,
  });
  expect(stats.identity_status_counts).toEqual({
    ambiguous: 276,
    confirmed: 1129,
    conflicting: 116,
    high_confidence: 740,
    probable: 176,
    unresolved: 21503,
  });
  expect(stats.commissioned_status_counts).toEqual({
    commissioned: 2287,
    not_commissioned: 6046,
    unknown: 15607,
  });
});

test("Batch 569 evidence exposes neither private identifier fields nor credentials", () => {
  expect(evidence).not.toMatch(/serial_number(_raw|_normalized)?/);
  expect(evidence).not.toContain('"serial_number"');
  expect(evidence).not.toContain("NARA_API_KEY");
  expect(evidence).not.toContain("x-api-key");
});
