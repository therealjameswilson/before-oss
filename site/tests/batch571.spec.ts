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
    "../../research/evidence-page-one-hundred-and-fifteen-vincent-desanto-through-daniel-b-desich-pathways_batch-571_2026-09-16.json",
    import.meta.url,
  ),
  "utf8",
);
const profile = (id: string) =>
  people.find((person: { person_id: string }) => person.person_id === id);

const cohort = [
  ["66ffe91d-31aa-5a43-b6c0-96b252806930", "Vincent DeSanto", "d28f4697-e8f5-5983-8452-8d4c0df15913", null, null, true],
  ["f29a7133-eba5-5b5d-bab4-175a93acf89b", "Bunmag Desaputra", "7bc71123-c01f-5986-96ae-f49913da41c8", null, null, false],
  ["aec04724-b0f3-5a6b-8d82-a71466804cd6", "John M DeSaussure", "c0eb01e8-53ef-5e29-8dcb-f4a3fa15e61e", null, null, true],
  ["261987dd-c7f2-5e62-b3b3-fa925c7a3a9b", "Bernard D'Escayrac", "abde25d3-65ed-5425-a7de-e1ea350bfd2c", null, null, false],
  ["640101ff-3987-522e-b7fb-16afc8602c8b", "James B Desch", "a181b3f7-1426-5708-8077-f072416ed4e9", null, null, true],
  ["e7a6cb26-59d6-509b-97d8-1d83c93d6346", "Marcel Descours", "422db7c8-1cee-51cf-bdc7-d1d8bc26b5e9", "French", null, false],
  ["40603d77-719f-5bdc-a905-24bdf5b35ed8", "Phillip Deshaw", "e75c47db-37bc-5093-8b3a-92868c57ddf4", null, null, true],
  ["73c503e1-b91d-5ff3-ab5b-dd3bb38b17e9", "Blaise DeSibour", "c73d7e51-6c23-5c3a-a74f-646ae5a7a029", null, null, false],
  ["926889b8-5fe6-52e4-8d78-6380fb97527b", "Jacques B DeSibour", "ff4473ac-018d-5ea1-9f2c-c16637414291", null, null, true],
  ["fc7008c4-a612-55de-bbf2-b16d109002ad", "Daniel B Desich", "0cc32078-f770-50ed-ad2d-b1a05c15e874", "also AS", null, false],
] as const;

test("Batch 571 preserves page 115 rows 3-12 and masks all five private values", () => {
  for (const [id, name, sourceRecordId, note, rank, hasPrivateIdentifier] of cohort) {
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
      notes_as_indexed: note,
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

test("Batch 571 publishes DeSanto's broad Army-entry occupation without inventing an employer", () => {
  const desanto = profile("66ffe91d-31aa-5a43-b6c0-96b252806930");
  expect(desanto).toMatchObject({
    identity_status: "confirmed",
    personnel_category: "enlisted_army_personnel",
    commissioned_officer: false,
    research_status: "occupation_only_found",
  });
  expect(desanto.name_variants).toContain("Vincent De Santo");
  expect(desanto.immediate_pre_oss_affiliations).toEqual([]);
  expect(desanto.last_civilian_pre_service).toEqual([]);
  expect(desanto.other_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      canonical_organization: null,
      occupation: "Foreman, not elsewhere classified",
      relationship_type: "unknown",
      end_date: "1941-01-18",
      temporal_basis: "strongly_date_bounded",
      identity_confidence: "confirmed",
      claim_confidence: "confirmed",
    }),
  ]);
  expect(JSON.stringify(desanto)).toContain(
    "No reliable pre-OSS employer has yet been identified",
  );
});

test("Batch 571 treats Desch's 1943 schooling as student status rather than employment", () => {
  const desch = profile("640101ff-3987-522e-b7fb-16afc8602c8b");
  expect(desch).toMatchObject({
    identity_status: "confirmed",
    personnel_category: "enlisted_army_personnel",
    commissioned_officer: false,
    research_status: "occupation_only_found",
  });
  expect(desch.immediate_pre_oss_affiliations).toEqual([]);
  expect(desch.last_civilian_pre_service).toEqual([]);
  expect(desch.other_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      canonical_organization: "Chaminade High School",
      organization_name_as_found: "Chaminade High School",
      role_title: "student",
      relationship_type: "student",
      end_date: "1943",
      temporal_basis: "strongly_date_bounded",
      claim_confidence: "high",
    }),
  ]);
});

test("Batch 571 separates de Sibour's civilian employer from his probable immediate military assignment", () => {
  const desibour = profile("926889b8-5fe6-52e4-8d78-6380fb97527b");
  expect(desibour).toMatchObject({
    identity_status: "high_confidence",
    personnel_category: "commissioned_army_officer",
    commissioned_officer: true,
    research_status: "documented_prewar_employer_found",
  });
  expect(desibour.last_civilian_pre_service).toEqual([
    expect.objectContaining({
      canonical_organization: "International Aviation Associates",
      organization_name_as_found: "Intava",
      relationship_type: "employment",
      start_date: "1936",
      end_date: "1939-09-03",
      temporal_basis: "strongly_date_bounded",
      claim_confidence: "medium",
      sector: "business_and_industry",
    }),
  ]);
  expect(desibour.immediate_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      canonical_organization: "Services of Supply, United States Army",
      role_title: "petroleum administrator for French West Africa",
      relationship_type: "military_assignment",
      start_date: "1943-02",
      end_date: "1943-07",
      temporal_basis: "probable_immediate",
      claim_confidence: "medium",
      sector: "military",
    }),
  ]);
  expect(JSON.stringify(desibour)).toContain(
    "the July-to-December interval is not fully explained",
  );
  expect(JSON.stringify(desibour)).toContain("Intava is not categorized as an oil company");
});

test("Batch 571 keeps Desich's name-only Army occupation candidate out of public facts", () => {
  const desich = profile("fc7008c4-a612-55de-bbf2-b16d109002ad");
  expect(desich).toMatchObject({
    identity_status: "high_confidence",
    personnel_category: "commissioned_army_officer",
    commissioned_officer: true,
    research_status: "requires_archival_review",
  });
  expect(desich.immediate_pre_oss_affiliations).toEqual([]);
  expect(desich.last_civilian_pre_service).toEqual([]);
  expect(desich.other_pre_oss_affiliations).toEqual([]);
  expect(JSON.stringify(desich)).not.toContain("Automobile manufacturing");
  expect(JSON.stringify(desich)).toContain("Second Lieutenant Daniel B. Desich");
});

test("Batch 571 preserves qualified and ambiguous non-employer identities", () => {
  const bunmag = profile("f29a7133-eba5-5b5d-bab4-175a93acf89b");
  expect(bunmag).toMatchObject({
    identity_status: "high_confidence",
    personnel_category: "foreign_or_allied_military_personnel",
    commissioned_officer: null,
  });
  expect(bunmag.name_variants).toContain("Bunmak Thesabut");
  expect(bunmag.last_civilian_pre_service).toEqual([]);

  const marcel = profile("e7a6cb26-59d6-509b-97d8-1d83c93d6346");
  expect(marcel).toMatchObject({
    identity_status: "probable",
    personnel_category: "unknown_or_indeterminate",
    commissioned_officer: null,
  });
  expect(marcel.name_variants).toContain("Marcel Descour");
  expect(marcel.immediate_pre_oss_affiliations).toEqual([]);

  const blaise = profile("73c503e1-b91d-5ff3-ab5b-dd3bb38b17e9");
  expect(blaise).toMatchObject({
    identity_status: "ambiguous",
    research_status: "requires_archival_review",
  });
  expect(blaise.claims).toHaveLength(1);
  expect(blaise.claims[0].claim_type).toBe("archival_file_status");
});

test("Batch 571 advances attempted and verified-affiliation coverage without inflating employer coverage", () => {
  expect(stats).toMatchObject({
    source_rows: 23978,
    person_entities: 23940,
    possible_duplicate_groups: 255,
    research_attempted_people: 5476,
    research_attempt_percent: 22.8739,
    verified_affiliation_people: 590,
    verified_affiliation_percent: 2.4645,
    verified_employer_people: 260,
    verified_employer_percent: 1.086,
    archival_review_assessed_people: 5431,
    archival_review_percent: 22.6859,
    public_sources: 3651,
    published_claims: 4452,
  });
  expect(stats.research_status_counts).toMatchObject({
    conflicting_sources: 114,
    documented_prewar_employer_found: 112,
    needs_identity_review: 322,
    not_started: 18464,
    occupation_only_found: 1013,
    requires_archival_review: 3245,
    verified_employer_found: 243,
  });
  expect(stats.identity_status_counts).toEqual({
    ambiguous: 278,
    confirmed: 1132,
    conflicting: 116,
    high_confidence: 745,
    probable: 178,
    unresolved: 21491,
  });
  expect(stats.commissioned_status_counts).toEqual({
    commissioned: 2289,
    not_commissioned: 6048,
    unknown: 15603,
  });
});

test("Batch 571 evidence exposes neither private identifier fields nor credentials", () => {
  expect(evidence).not.toMatch(/serial_number(_raw|_normalized)?/);
  expect(evidence).not.toContain('"serial_number"');
  expect(evidence).not.toContain("NARA_API_KEY");
  expect(evidence).not.toContain("x-api-key");
});
