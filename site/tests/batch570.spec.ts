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
    "../../research/evidence-page-one-hundred-and-fourteen-and-one-hundred-and-fifteen-walter-j-derr-through-william-j-desalvo-pathways_batch-570_2026-09-16.json",
    import.meta.url,
  ),
  "utf8",
);
const profile = (id: string) =>
  people.find((person: { person_id: string }) => person.person_id === id);

const cohort = [
  ["81b1d697-a203-5a42-a043-902eb5163a44", "Walter J Derr", "49026787-964d-5f2a-9f3b-c80889df2cc5", 114, null, false],
  ["882d31ba-3e7d-53d0-8951-3a70ef7534a5", "Jean M D'Errecalde", "f92f02b0-1cd7-5142-986f-74ac9788938b", 114, "1stLt", false],
  ["4a68409f-238b-584f-b226-102dfb86e966", "Delta I Derrom", "c930d632-229d-5b29-a6cf-5a0473cff419", 114, null, false],
  ["3733ff51-7a57-5197-92cb-ac3d130a14da", "Romeo J Derussau", "6752a24f-9e83-5122-ac07-38a6705da6ff", 114, null, false],
  ["b5b3d635-1c5d-5dfa-b722-72893e89e679", "Thibaut DeSaint Phalle", "5026087c-72ec-5e07-9beb-69227c3ffbd5", 114, null, true],
  ["50e34e69-af2b-5095-b5ea-c33a2ee5dbe4", "Pierry F Desaix", "a5572f74-ff70-53dc-ad1b-f4690b70e1b4", 114, "2nd Lt", true],
  ["feb03984-e283-55e5-a721-de4ac69df190", "Gerard D Desales", "dc2db7f1-8c58-5c6d-a6e2-7a1bcfc7e517", 114, null, false],
  ["46294c52-767a-5a2e-a71d-d726e7bab301", "Richard DeSales", "002085c3-9197-5fa5-bc68-584b625f3a2e", 114, null, false],
  ["df8c3a35-1f4b-5b7d-9461-051dc05e7500", "Joseph S DeSalvo", "beee73da-a87a-5b45-830a-655d8ba6b36e", 115, null, true],
  ["8946ed2e-1e06-54b2-abac-519504a63bb3", "William J DeSalvo", "8456d90d-317d-5701-bcc6-f94a0fe3807c", 115, "Capt", true],
] as const;

test("Batch 570 preserves page 114 rows 39-46 and page 115 rows 1-2 while masking private values", () => {
  for (const [id, name, sourceRecordId, page, rank, hasPrivateIdentifier] of cohort) {
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
      pdf_page: page,
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

test("Batch 570 confirms D'Errecalde's Army pathway without inventing a civilian employer", () => {
  const derrecalde = profile("882d31ba-3e7d-53d0-8951-3a70ef7534a5");
  expect(derrecalde).toMatchObject({
    identity_status: "confirmed",
    research_status: "requires_archival_review",
    personnel_category: "commissioned_army_officer",
    commissioned_officer: true,
  });
  expect(derrecalde.name_variants).toContain(
    "Jean Maurice Muthular d’Errecalde",
  );
  expect(derrecalde.immediate_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      canonical_organization: "United States Army",
      role_title: "First Lieutenant, Infantry",
      relationship_type: "military_assignment",
      start_date: "1942-10-13",
      temporal_basis: "explicit_immediate",
      identity_confidence: "confirmed",
      claim_confidence: "high",
    }),
  ]);
  expect(derrecalde.last_civilian_pre_service).toEqual([]);
  expect(derrecalde.other_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      canonical_organization: null,
      role_title: "Lawyer",
      occupation: "Lawyer",
      relationship_type: "unknown",
      city: "New York",
      temporal_basis: "documented_prewar",
      claim_confidence: "medium",
    }),
  ]);
  expect(JSON.stringify(derrecalde)).toContain(
    "No reliable pre-OSS employer has yet been identified",
  );
});

test("Batch 570 identifies de Saint Phalle's last civilian employer with the wartime-overlap qualification", () => {
  const saintPhalle = profile("b5b3d635-1c5d-5dfa-b722-72893e89e679");
  expect(saintPhalle).toMatchObject({
    identity_status: "high_confidence",
    research_status: "verified_employer_found",
  });
  expect(saintPhalle.immediate_pre_oss_affiliations).toEqual([]);
  expect(saintPhalle.last_civilian_pre_service).toEqual([
    expect.objectContaining({
      canonical_organization: "Chadbourne, Wallace, Parke & Whiteside",
      role_title: "Associate attorney",
      occupation: "Attorney",
      relationship_type: "employment",
      start_date: "1941",
      end_date: "1950",
      temporal_basis: "strongly_date_bounded",
      identity_confidence: "high_confidence",
      claim_confidence: "high",
      sector: "law",
    }),
  ]);
  expect(JSON.stringify(saintPhalle)).toContain(
    "overlaps wartime service and is not treated as continuous active office work",
  );
  expect(JSON.stringify(saintPhalle)).toContain(
    "U.S. Navy and Office of Strategic Services from 1942 to 1946",
  );
});

test("Batch 570 keeps DeSaix's postwar full-name lead qualified and unconnected to employment", () => {
  const desaix = profile("50e34e69-af2b-5095-b5ea-c33a2ee5dbe4");
  expect(desaix).toMatchObject({
    identity_status: "probable",
    research_status: "requires_archival_review",
    personnel_category: "commissioned_army_officer",
    commissioned_officer: true,
  });
  expect(desaix.name_variants).toContain("Pierry Francis DeSaix");
  expect(desaix.immediate_pre_oss_affiliations).toEqual([]);
  expect(desaix.last_civilian_pre_service).toEqual([]);
  expect(desaix.other_pre_oss_affiliations).toEqual([]);
  expect(JSON.stringify(desaix)).toContain(
    "probable full-name expansion",
  );
});

test("Batch 570 exposes the DeSales and de Roussy de Sales ambiguity without merging entities", () => {
  const desales = profile("46294c52-767a-5a2e-a71d-d726e7bab301");
  const deroussy = profile("3f2d6473-cb73-5600-85a7-30074e21e3a4");
  expect(desales).toMatchObject({
    display_name: "Richard DeSales",
    identity_status: "ambiguous",
    possible_duplicate_group: "duplicate-5c2124825ec9",
    manual_review_required: true,
  });
  expect(deroussy).toMatchObject({
    display_name: "Richard DeRoussyDeD",
    identity_status: "high_confidence",
    possible_duplicate_group: "duplicate-5c2124825ec9",
    manual_review_required: true,
  });
  expect(desales.person_id).not.toBe(deroussy.person_id);
  expect(desales.source_records[0].box).toBe("182");
  expect(deroussy.source_records[0].box).toBe("181");
});

test("Batch 570 advances verified-affiliation and verified-employer coverage", () => {
  expect(stats).toMatchObject({
    source_rows: 23978,
    person_entities: 23940,
    possible_duplicate_groups: 255,
    research_attempted_people: 5466,
    research_attempt_percent: 22.8321,
    verified_affiliation_people: 588,
    verified_affiliation_percent: 2.4561,
    verified_employer_people: 260,
    verified_employer_percent: 1.086,
    archival_review_assessed_people: 5421,
    archival_review_percent: 22.6441,
    public_sources: 3642,
    published_claims: 4432,
  });
  expect(stats.research_status_counts).toMatchObject({
    conflicting_sources: 114,
    documented_prewar_employer_found: 111,
    needs_identity_review: 322,
    not_started: 18474,
    occupation_only_found: 1011,
    requires_archival_review: 3238,
    verified_employer_found: 243,
  });
  expect(stats.identity_status_counts).toEqual({
    ambiguous: 277,
    confirmed: 1130,
    conflicting: 116,
    high_confidence: 741,
    probable: 177,
    unresolved: 21499,
  });
  expect(stats.commissioned_status_counts).toEqual({
    commissioned: 2287,
    not_commissioned: 6046,
    unknown: 15607,
  });
});

test("Batch 570 evidence exposes neither private identifier fields nor credentials", () => {
  expect(evidence).not.toMatch(/serial_number(_raw|_normalized)?/);
  expect(evidence).not.toContain('"serial_number"');
  expect(evidence).not.toContain("NARA_API_KEY");
  expect(evidence).not.toContain("x-api-key");
});
