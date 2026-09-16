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
    "../../research/evidence-pages-one-hundred-and-thirteen-and-one-hundred-and-fourteen-nancy-dennis-through-robert-p-dent-pathways_batch-566_2026-09-16.json",
    import.meta.url,
  ),
  "utf8",
);
const profile = (id: string) =>
  people.find((person: { person_id: string }) => person.person_id === id);

const cohort = [
  ["b6bfbd56-ea40-5166-bcae-92aaaf1a263f", "Nancy Dennis", "fce88981-49bc-5b1f-b056-492a7acd128a", 113, "180", false],
  ["7d44e1d1-b668-592c-9622-8693280b423d", "Edward E Denniston", "77090751-0317-5d95-919e-cca8714b2489", 113, "180", true],
  ["9250e2a1-4aad-5ef4-98e9-762231fe4030", "Jack H Denniston", "0a4d4eac-50ec-5b42-82da-489909ac259b", 113, "180", false],
  ["3d2a531e-4e68-55e9-a620-5da1ae8a053d", "Charles P Denny Jr.", "fd16b91e-4602-57b7-9c9f-90b921ddd74b", 114, "180", true],
  ["f5b35619-eb87-565a-b9d0-70ee754ea86c", "Philippe A DeNoailles", "104b235d-52b0-5d85-a848-abb1783fcb49", 114, "180", false],
  ["7eed6672-575e-506f-8e2c-ee0f0ac489ad", "Anthony DeNoia", "f6ccf229-e12e-5c8a-a456-4f609a1e039e", 114, "180", true],
  ["bd570f16-80fc-5d2f-ab66-16732dbbceb6", "Charles M Densler", "430d804a-dfbb-50b7-b8c2-a39e8005086b", 114, "181", true],
  ["d9b22413-66c2-546c-82b7-1908e36f884d", "Frederick E Densmore", "28132991-4d8f-50d7-a464-e02d3d959aa8", 114, "181", false],
  ["06ea271f-bb85-593a-a2c1-488645685db1", "Ralph E Densmore", "9b510faa-a6b3-5075-b540-1572cec1869e", 114, "181", false],
] as const;

test("Batch 566 preserves page 113 rows 44-46 and page 114 rows 1-8", () => {
  for (const [id, name, sourceRecordId, page, box, hasPrivateIdentifier] of cohort) {
    const person = profile(id);
    expect(person.display_name).toBe(name);
    expect(person.research_attempt_count).toBe(5);
    const sourceRecord = person.source_records.find(
      (record: { source_record_id: string }) =>
        record.source_record_id === sourceRecordId,
    );
    expect(sourceRecord).toMatchObject({
      archive_location: "230/86/29/07",
      box,
      pdf_page: page,
      rank_as_indexed: null,
      notes_as_indexed: null,
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

  const robert = profile("df5cd92a-c30b-5693-9516-0d349473c334");
  expect(robert.display_name).toBe("Robert P Dent");
  expect(robert.research_attempt_count).toBe(5);
  expect(robert.source_records).toHaveLength(2);
  expect(robert.source_records.map((row: { source_record_id: string }) => row.source_record_id)).toEqual([
    "9c956ba7-d3b3-589d-b10c-0b13c0eadec8",
    "b4bb1525-2174-51d7-ab55-86afae905ad8",
  ]);
  for (const row of robert.source_records) {
    expect(row).toMatchObject({
      box: "181",
      pdf_page: 114,
      serial_masked: expect.stringMatching(/^•+\d{4}$/),
    });
  }
  expect(robert.possible_duplicate_group).toBeTruthy();
});

test("Batch 566 publishes DeNoia's broad occupation without inventing an employer", () => {
  const anthony = profile("7eed6672-575e-506f-8e2c-ee0f0ac489ad");
  expect(anthony).toMatchObject({
    identity_status: "confirmed",
    research_status: "occupation_only_found",
    personnel_category: "enlisted_army_personnel",
    commissioned_officer: false,
  });
  expect(anthony.name_variants).toContain("Anthony De Noia");
  expect(anthony.immediate_pre_oss_affiliations).toEqual([]);
  expect(anthony.last_civilian_pre_service).toEqual([]);
  expect(anthony.other_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      occupation: "Chemical products producing occupation, not elsewhere classified",
      relationship_type: "unknown",
      end_date: "1942-08-17",
      temporal_basis: "strongly_date_bounded",
      identity_confidence: "confirmed",
      claim_confidence: "medium",
      canonical_organization: null,
    }),
  ]);
  expect(JSON.stringify(anthony)).toContain(
    "No named employer, product, plant or precise task is inferred",
  );
});

test("Batch 566 preserves Dent's duplicate rows and publishes secretary occupation only", () => {
  const robert = profile("df5cd92a-c30b-5693-9516-0d349473c334");
  expect(robert).toMatchObject({
    identity_status: "confirmed",
    research_status: "occupation_only_found",
    personnel_category: "enlisted_army_personnel",
    commissioned_officer: false,
    manual_review_required: true,
  });
  expect(robert.immediate_pre_oss_affiliations).toEqual([]);
  expect(robert.last_civilian_pre_service).toEqual([]);
  expect(robert.other_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      occupation: "Secretary",
      relationship_type: "unknown",
      end_date: "1942-11-27",
      temporal_basis: "strongly_date_bounded",
      identity_confidence: "confirmed",
      claim_confidence: "medium",
      canonical_organization: null,
    }),
  ]);
  expect(JSON.stringify(robert)).toContain(
    "two printed index rows remain separate source records",
  );
  expect(JSON.stringify(robert)).toContain(
    "No named employer or office is inferred",
  );
});

test("Batch 566 keeps three namesake cases visibly ambiguous", () => {
  for (const id of [
    "9250e2a1-4aad-5ef4-98e9-762231fe4030",
    "f5b35619-eb87-565a-b9d0-70ee754ea86c",
    "d9b22413-66c2-546c-82b7-1908e36f884d",
  ]) {
    const person = profile(id);
    expect(person.identity_status).toBe("ambiguous");
    expect(person.research_status).toBe("needs_identity_review");
    expect(person.archival_file.review_priority).toBe("critical");
    expect(person.immediate_pre_oss_affiliations).toEqual([]);
    expect(person.last_civilian_pre_service).toEqual([]);
    expect(person.other_pre_oss_affiliations).toEqual([]);
    expect(JSON.stringify(person)).toContain(
      "No reliable pre-OSS employer has yet been identified",
    );
  }
});

test("Batch 566 routes five unresolved profiles to archival review", () => {
  for (const id of [
    "b6bfbd56-ea40-5166-bcae-92aaaf1a263f",
    "7d44e1d1-b668-592c-9622-8693280b423d",
    "3d2a531e-4e68-55e9-a620-5da1ae8a053d",
    "bd570f16-80fc-5d2f-ab66-16732dbbceb6",
    "06ea271f-bb85-593a-a2c1-488645685db1",
  ]) {
    const person = profile(id);
    expect(person.identity_status).toBe("unresolved");
    expect(person.research_status).toBe("requires_archival_review");
    expect(person.archival_file.review_priority).toBe("high");
    expect(person.immediate_pre_oss_affiliations).toEqual([]);
    expect(person.last_civilian_pre_service).toEqual([]);
    expect(person.other_pre_oss_affiliations).toEqual([]);
  }
});

test("Batch 566 advances coverage without verified-employer inflation", () => {
  expect(stats).toMatchObject({
    source_rows: 23978,
    person_entities: 23940,
    possible_duplicate_groups: 254,
    research_attempted_people: 5426,
    research_attempt_percent: 22.665,
    verified_affiliation_people: 585,
    verified_affiliation_percent: 2.4436,
    verified_employer_people: 259,
    verified_employer_percent: 1.0819,
    archival_review_assessed_people: 5381,
    archival_review_percent: 22.477,
    public_sources: 3616,
    published_claims: 4366,
  });
  expect(stats.research_status_counts).toMatchObject({
    conflicting_sources: 114,
    documented_prewar_employer_found: 111,
    needs_identity_review: 319,
    not_started: 18514,
    occupation_only_found: 1006,
    requires_archival_review: 3207,
    verified_employer_found: 242,
  });
  expect(stats.identity_status_counts).toEqual({
    ambiguous: 272,
    confirmed: 1123,
    conflicting: 116,
    high_confidence: 733,
    probable: 176,
    unresolved: 21520,
  });
});

test("Batch 566 evidence exposes neither private identifiers nor credentials", () => {
  expect(evidence).not.toMatch(/serial_number(_raw|_normalized)?/);
  expect(evidence).not.toContain('"serial_number"');
  expect(evidence).not.toContain("NARA_API_KEY");
  expect(evidence).not.toContain("x-api-key");
});
