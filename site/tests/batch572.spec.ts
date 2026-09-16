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
    "../../research/evidence-page-one-hundred-and-fifteen-jean-m-desieyes-through-robert-desmond-pathways_batch-572_2026-09-16.json",
    import.meta.url,
  ),
  "utf8",
);
const profile = (id: string) =>
  people.find((person: { person_id: string }) => person.person_id === id);

const cohort = [
  ["eb58ee86-eef2-52ce-8760-ea757f4e8f18", "Jean M DeSieyes", "e19ce4fc-9441-5c42-a380-42c91a14a9ef", "S/Sgt", true],
  ["1e8668a2-d8bd-56cf-8690-943863c27acd", "Peer DeSilva", "cf2d73b6-cd6f-51c5-826c-e23a5a9292e6", null, true],
  ["230e6fdf-6e49-5894-8839-677637334843", "Adele D DeSimone", "f946dc95-1284-5447-8cd4-9f45befd8951", null, false],
  ["7cf772c8-b746-503b-911a-b56fe9322bf8", "Joseph Desipio", "d4481118-d06a-5778-a21e-35463f8ac9a5", null, false],
  ["7a40a6f8-f46d-5d29-9080-f1f90c24d81d", "George C Deskin", "06fe80c6-5136-56ec-993e-af2cd2b7dd56", null, true],
  ["bc1b6eec-f789-5df3-b416-1717e821c3dc", "M H Deslandes", "502833dc-836a-59c3-bcd0-8ff525d0170e", null, false],
  ["c7755531-e843-584d-a1bd-decd81d573c7", "Cletus H Desmaretz", "2f92c1e5-e8b5-5d80-8ee9-a927cb2544f6", "T-5", true],
  ["3ebb5921-2bff-5bb2-b300-af80ca882ff8", "Daniel H Desmond", "4132ed0c-d995-57c2-bad0-f6801693b5b6", null, true],
  ["1dc38d7d-79c4-55e8-afc8-5963dba545d8", "Geral A Desmond", "4ca59f3f-ef40-5759-83c4-0f1d394e632c", null, false],
  ["7319ff54-e69e-58dc-8495-b3b960550744", "Robert Desmond", "1d07dd31-1d54-5ff9-b8ff-8719d49e27f7", null, false],
] as const;

test("Batch 572 preserves page 115 rows 13-22 and masks all five private values", () => {
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
      box: "182",
      pdf_page: 115,
      notes_as_indexed: null,
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

test("Batch 572 preserves Peer de Silva's Manhattan-to-SSU chronology without inventing wartime OSS service", () => {
  const peer = profile("1e8668a2-d8bd-56cf-8690-943863c27acd");
  expect(peer).toMatchObject({
    identity_status: "high_confidence",
    personnel_category: "commissioned_army_officer",
    commissioned_officer: true,
    research_status: "requires_archival_review",
  });
  expect(peer.name_variants).toContain("Peer de Silva");
  expect(peer.immediate_pre_oss_affiliations).toEqual([]);
  expect(peer.last_civilian_pre_service).toEqual([]);
  expect(peer.other_pre_oss_affiliations).toEqual(
    expect.arrayContaining([
      expect.objectContaining({
        canonical_organization: "United States Military Academy",
        relationship_type: "student",
        end_date: "1941",
        claim_confidence: "high",
      }),
      expect.objectContaining({
        canonical_organization: "United States Army Quartermaster Corps",
        relationship_type: "military_assignment",
        start_date: "1941",
        claim_confidence: "high",
      }),
      expect.objectContaining({
        canonical_organization: "Manhattan Engineer District",
        organization_name_as_found: "Manhattan Project",
        role_title: "project security officer",
        relationship_type: "military_assignment",
        start_date: "1943",
        end_date: "1945",
        claim_confidence: "high",
      }),
    ]),
  );
  expect(JSON.stringify(peer)).toContain("postwar Strategic Services Unit");
  expect(
    peer.claims.some(
      (claim: { claim_type: string }) =>
        claim.claim_type === "immediate_pre_oss_affiliation",
    ),
  ).toBe(false);
});

test("Batch 572 publishes Cletus Desmaretz's student evidence without treating a school as an employer", () => {
  const cletus = profile("c7755531-e843-584d-a1bd-decd81d573c7");
  expect(cletus).toMatchObject({
    identity_status: "confirmed",
    personnel_category: "enlisted_army_personnel",
    commissioned_officer: false,
    research_status: "occupation_only_found",
  });
  expect(cletus.name_variants).toContain("Cletus Hen Desmaretz");
  expect(cletus.immediate_pre_oss_affiliations).toEqual([]);
  expect(cletus.last_civilian_pre_service).toEqual([]);
  expect(cletus.other_pre_oss_affiliations).toEqual(
    expect.arrayContaining([
      expect.objectContaining({
        canonical_organization: null,
        occupation: "Student",
        relationship_type: "student",
        end_date: "1943-03-16",
        temporal_basis: "strongly_date_bounded",
        claim_confidence: "confirmed",
      }),
      expect.objectContaining({
        canonical_organization: "Whittier High School",
        role_title: "student or alumnus",
        relationship_type: "student",
        temporal_basis: "documented_prewar",
        claim_confidence: "medium",
      }),
    ]),
  );
  expect(JSON.stringify(cletus)).toContain(
    "No reliable pre-OSS employer has yet been identified",
  );
});

test("Batch 572 confirms George Deskin but withholds uninterpreted occupation code 999", () => {
  const george = profile("7a40a6f8-f46d-5d29-9080-f1f90c24d81d");
  expect(george).toMatchObject({
    identity_status: "confirmed",
    personnel_category: "enlisted_army_personnel",
    commissioned_officer: false,
    research_status: "requires_archival_review",
  });
  expect(george.immediate_pre_oss_affiliations).toEqual([]);
  expect(george.last_civilian_pre_service).toEqual([]);
  expect(george.other_pre_oss_affiliations).toEqual([]);
  expect(
    george.claims.some(
      (claim: { claim_type: string }) => claim.claim_type === "occupation",
    ),
  ).toBe(false);
  expect(JSON.stringify(george)).toContain("not interpreted");
});

test("Batch 572 publishes Daniel Desmond's Army-entry occupation without inventing an employer", () => {
  const daniel = profile("3ebb5921-2bff-5bb2-b300-af80ca882ff8");
  expect(daniel).toMatchObject({
    identity_status: "confirmed",
    personnel_category: "enlisted_army_personnel",
    commissioned_officer: false,
    research_status: "occupation_only_found",
  });
  expect(daniel.immediate_pre_oss_affiliations).toEqual([]);
  expect(daniel.last_civilian_pre_service).toEqual([]);
  expect(daniel.other_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      canonical_organization: null,
      occupation: "General office clerk",
      relationship_type: "unknown",
      end_date: "1942-10-02",
      temporal_basis: "strongly_date_bounded",
      claim_confidence: "confirmed",
    }),
  ]);
  expect(JSON.stringify(daniel)).not.toContain("James M. Desmond");
});

test("Batch 572 keeps low-confidence namesakes and search aliases out of public facts", () => {
  const joseph = profile("7cf772c8-b746-503b-911a-b56fe9322bf8");
  expect(joseph).toMatchObject({
    identity_status: "ambiguous",
    research_status: "requires_archival_review",
  });
  expect(joseph.other_pre_oss_affiliations).toEqual([]);
  expect(joseph.claims).toHaveLength(1);
  expect(JSON.stringify(joseph)).not.toContain("ballet dancer");

  const geral = profile("1dc38d7d-79c4-55e8-afc8-5963dba545d8");
  expect(geral.display_name).toBe("Geral A Desmond");
  expect(geral.name_variants).not.toContain("Gerald A Desmond");

  const robert = profile("7319ff54-e69e-58dc-8495-b3b960550744");
  expect(robert).toMatchObject({
    identity_status: "unresolved",
    research_status: "requires_archival_review",
  });
  expect(robert.other_pre_oss_affiliations).toEqual([]);
  expect(robert.claims).toHaveLength(1);
});

test("Batch 572 advances attempted and verified-affiliation coverage without inflating employer coverage", () => {
  expect(stats).toMatchObject({
    source_rows: 23978,
    person_entities: 23940,
    possible_duplicate_groups: 255,
    research_attempted_people: 5486,
    research_attempt_percent: 22.9156,
    verified_affiliation_people: 593,
    verified_affiliation_percent: 2.477,
    verified_employer_people: 260,
    verified_employer_percent: 1.086,
    archival_review_assessed_people: 5441,
    archival_review_percent: 22.7277,
    public_sources: 3657,
    published_claims: 4472,
  });
  expect(stats.research_status_counts).toMatchObject({
    candidate_found: 7,
    conflicting_sources: 114,
    documented_prewar_employer_found: 112,
    in_progress: 44,
    needs_identity_review: 322,
    not_started: 18454,
    occupation_only_found: 1015,
    requires_archival_review: 3253,
    verified_employer_found: 243,
  });
  expect(stats.identity_status_counts).toEqual({
    ambiguous: 279,
    confirmed: 1135,
    conflicting: 116,
    high_confidence: 746,
    probable: 178,
    unresolved: 21486,
  });
  expect(stats.commissioned_status_counts).toEqual({
    commissioned: 2290,
    not_commissioned: 6050,
    unknown: 15600,
  });
});

test("Batch 572 evidence exposes neither private identifier fields nor credentials", () => {
  expect(evidence).not.toMatch(/serial_number(_raw|_normalized)?/);
  expect(evidence).not.toContain('"serial_number"');
  expect(evidence).not.toContain("NARA_API_KEY");
  expect(evidence).not.toContain("x-api-key");
});
