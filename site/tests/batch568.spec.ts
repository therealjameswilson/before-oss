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
    "../../research/evidence-page-one-hundred-and-fourteen-wallace-a-deponio-through-anne-b-deren-pathways_batch-568_2026-09-16.json",
    import.meta.url,
  ),
  "utf8",
);
const profile = (id: string) =>
  people.find((person: { person_id: string }) => person.person_id === id);

const cohort = [
  ["b0c253bd-47cc-5e74-a31a-2b768cc4d472", "Wallace A DePonio", "5daf4791-f840-52d1-be07-fdae520c6116", null, true, 6],
  ["6ce40b8a-6b27-5f75-8419-ad5ac225eaf9", "Larry W DeRall", "07e38305-c201-508e-9e12-b917798c3193", null, false, 5],
  ["e516c34b-8977-5fd4-8890-084c4b2daefa", "B N Deranian", "77c3f22b-d2d3-57cc-81f2-4ac65b2d723e", "Lt Cmdr", false, 5],
  ["d99dfed2-f59e-5bad-83bc-af3e4ea9281c", "Arthur L Derby", "d2212c95-5714-5530-94c3-dbf957288b17", null, false, 5],
  ["6b8f42a1-142a-5c44-b8f1-700b6cc10feb", "Roger B Derby", "047144e4-2863-5e10-81e6-ef63157941f2", null, true, 5],
  ["970e8a9c-7c10-5126-ab7a-a4f6d7433ea3", "Samuel H Derbyshire", "01d43cf2-be4a-55c3-a05a-572c70bfbda4", null, false, 5],
  ["6bc81afe-db85-5b4d-b580-3fdd062e84f6", "Antoine DeRecy", "5e791dd7-e8eb-564c-9ef5-3f16d9acac86", "Capt", false, 5],
  ["7568196b-1ed0-5a37-b74b-c2b1f4b27801", "John Dereki", "4edcfc25-d165-5938-9714-c5d5bfe9d14a", null, false, 5],
  ["4ee4e236-ae77-5a93-ac91-0955f99226b3", "Eleanor DeRemer", "a6c10f75-d6a1-54cc-bdfb-21eade558f33", null, false, 5],
  ["db92773a-a067-55ed-bd8f-65ed5a82162c", "Anne B Deren", "f457e8da-a8ab-509e-934f-a4ede655373d", null, false, 5],
] as const;

test("Batch 568 preserves page 114 rows 19-28 and masks both private values", () => {
  for (const [id, name, sourceRecordId, rank, hasPrivateIdentifier, attempts] of cohort) {
    const person = profile(id);
    expect(person.display_name).toBe(name);
    expect(person.research_attempt_count).toBe(attempts);
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

test("Batch 568 publishes B. Nelson Deranian only as a qualified identity", () => {
  const deranian = profile("e516c34b-8977-5fd4-8890-084c4b2daefa");
  expect(deranian).toMatchObject({
    identity_status: "high_confidence",
    research_status: "requires_archival_review",
    personnel_category: "commissioned_naval_officer",
    commissioned_officer: true,
  });
  expect(deranian.name_variants).toEqual(
    expect.arrayContaining(["B. Nelson Deranian", "Nelson B. Deranian"]),
  );
  expect(deranian.immediate_pre_oss_affiliations).toEqual([]);
  expect(deranian.last_civilian_pre_service).toEqual([]);
  expect(deranian.other_pre_oss_affiliations).toEqual([]);
  expect(JSON.stringify(deranian)).toContain("chief of SO-Bari");
  expect(JSON.stringify(deranian)).toContain("initial order and rank wording");
  expect(JSON.stringify(deranian)).toContain(
    "No reliable pre-OSS employer has yet been identified",
  );
});

test("Batch 568 separates Antoine de Récy's earlier military assignment from employment", () => {
  const recy = profile("6bc81afe-db85-5b4d-b580-3fdd062e84f6");
  expect(recy).toMatchObject({
    identity_status: "high_confidence",
    research_status: "requires_archival_review",
    personnel_category: "commissioned_army_officer",
    commissioned_officer: true,
    allied_or_foreign_personnel: true,
  });
  expect(recy.name_variants).toEqual(
    expect.arrayContaining(["Antoine de Récy", "Antoine Chalvet de Récy"]),
  );
  expect(recy.immediate_pre_oss_affiliations).toEqual([]);
  expect(recy.last_civilian_pre_service).toEqual([]);
  expect(recy.other_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      canonical_organization:
        "Provisional Government of the French Republic, Ministry of War",
      role_title:
        "Aide-de-camp to André Diethelm; organizer of the Commandos de France",
      relationship_type: "military_assignment",
      end_date: "1944",
      temporal_basis: "strongly_date_bounded",
      identity_confidence: "high_confidence",
      claim_confidence: "high",
    }),
  ]);
  expect(JSON.stringify(recy)).toContain(
    "not proven to be the immediate predecessor",
  );
  expect(JSON.stringify(recy)).toContain(
    "No reliable civilian pre-OSS employer has yet been identified",
  );
});

test("Batch 568 preserves name-only Army rows as unresolved candidates", () => {
  for (const id of [
    "b0c253bd-47cc-5e74-a31a-2b768cc4d472",
    "970e8a9c-7c10-5126-ab7a-a4f6d7433ea3",
    "7568196b-1ed0-5a37-b74b-c2b1f4b27801",
  ]) {
    const person = profile(id);
    expect(person.identity_status).toBe("ambiguous");
    expect(person.research_status).toBe("needs_identity_review");
    expect(person.immediate_pre_oss_affiliations).toEqual([]);
    expect(person.last_civilian_pre_service).toEqual([]);
    expect(person.other_pre_oss_affiliations).toEqual([]);
    expect(person.archival_file.review_priority).toBe("critical");
  }

  expect(JSON.stringify(profile("970e8a9c-7c10-5126-ab7a-a4f6d7433ea3"))).toContain(
    "name alone cannot connect",
  );
  expect(JSON.stringify(profile("7568196b-1ed0-5a37-b74b-c2b1f4b27801"))).toContain(
    "neither source supplies a direct Box 181",
  );
});

test("Batch 568 advances attempted and affiliation coverage without employer inflation", () => {
  expect(stats).toMatchObject({
    source_rows: 23978,
    person_entities: 23940,
    possible_duplicate_groups: 254,
    research_attempted_people: 5446,
    research_attempt_percent: 22.7485,
    verified_affiliation_people: 586,
    verified_affiliation_percent: 2.4478,
    verified_employer_people: 259,
    verified_employer_percent: 1.0819,
    archival_review_assessed_people: 5401,
    archival_review_percent: 22.5606,
    public_sources: 3628,
    published_claims: 4398,
  });
  expect(stats.research_status_counts).toMatchObject({
    conflicting_sources: 114,
    documented_prewar_employer_found: 111,
    needs_identity_review: 322,
    not_started: 18494,
    occupation_only_found: 1009,
    requires_archival_review: 3221,
    verified_employer_found: 242,
  });
  expect(stats.identity_status_counts).toEqual({
    ambiguous: 275,
    confirmed: 1126,
    conflicting: 116,
    high_confidence: 738,
    probable: 176,
    unresolved: 21509,
  });
  expect(stats.commissioned_status_counts).toEqual({
    commissioned: 2287,
    not_commissioned: 6044,
    unknown: 15609,
  });
});

test("Batch 568 evidence exposes neither private identifier fields nor credentials", () => {
  expect(evidence).not.toMatch(/serial_number(_raw|_normalized)?/);
  expect(evidence).not.toContain('"serial_number"');
  expect(evidence).not.toContain("NARA_API_KEY");
  expect(evidence).not.toContain("x-api-key");
});
