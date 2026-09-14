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
    "../../research/evidence-page-one-hundred-and-four-george-r-daly-through-caroline-damerau-pathways_batch-522_2026-09-14.json",
    import.meta.url,
  ),
  "utf8",
);
const profile = (id: string) =>
  people.find((person: { person_id: string }) => person.person_id === id);

const cohort = [
  ["3d2376e1-98a5-5907-85f7-82a532bab836", "George R Daly", "56d453e0-316b-5322-bbcf-201ea8ee7d99", false],
  ["fed626b9-42f7-594f-8f1e-d73051f77f92", "John J Daly", "1df3e106-32b2-5f25-bf1f-6f10199d44ad", false],
  ["7006d520-3367-5e54-b7f5-38aad91aadd2", "Joseph T Daly", "75be8ee6-7dfe-554d-b35e-e8f311ba6170", true],
  ["7beeb499-d8d3-553f-92fa-0f875849f54f", "William J Daly", "61151d1d-0b32-58c1-a3bf-08c44583dec4", true],
  ["faa350cd-4293-541d-929e-39f14e3a0d12", "Joseph C D'Amato", "a9d07404-23b4-591f-b86d-a8ac4d4b9424", false],
  ["abd59f4f-ec39-5145-9178-c7dc2c32d82c", "Evelyn Damberg", "65382c53-d78b-55d4-a98b-3ce1f20743c9", false],
  ["2cb74800-cad3-5693-92e0-9a6f40c43e87", "Thomas D Damberg", "93175756-3cdb-5abc-8bdd-1f2d15f3f6ae", false],
  ["8a4ff632-396f-5f4b-8785-891a5e19b5c8", "Arnold H Damen", "2884ebac-c835-58d4-8355-f79366c1c6af", true],
  ["5d12141c-b84b-5d13-a192-798370c31e81", "Edward M Damen", "36a92edb-adf4-5961-be5c-b5f6d64b6f8e", true],
  ["279585de-84e3-5de8-9f53-5182f720ffce", "Caroline Damerau", "4f0cc8f4-a44b-58b0-b7c0-e41504b89b63", false],
  ["092994a6-390d-5137-bae2-6ed97e5bed42", "Arnold H Dammen", "30eeb905-d1ca-5df9-b958-5a8905dad70d", true],
] as const;

test("Batch 522 preserves eleven printed rows and masks every private field", () => {
  for (const [id, name, sourceRecordId, hasPrivateIdentifier] of cohort) {
    const person = profile(id);
    expect(person).toMatchObject({ display_name: name });
    const sourceRecord = person.source_records.find(
      (record: { source_record_id: string }) => record.source_record_id === sourceRecordId,
    );
    expect(sourceRecord).toMatchObject({
      archive_location: "230/86/29/05",
      box: "165",
      pdf_page: 104,
    });
    if (hasPrivateIdentifier) {
      expect(sourceRecord.serial_masked).toMatch(/^••••\d{4}$/);
    } else {
      expect(sourceRecord.serial_masked).toBeNull();
    }
    expect(JSON.stringify(person)).not.toMatch(
      /"serial_number"|"serial_number_raw"|"serial_number_normalized"/,
    );
  }
});

test("Batch 522 publishes no unsupported affiliation or employer claim", () => {
  const expectedIdentity = new Map([
    ["3d2376e1-98a5-5907-85f7-82a532bab836", "ambiguous"],
    ["fed626b9-42f7-594f-8f1e-d73051f77f92", "ambiguous"],
    ["7006d520-3367-5e54-b7f5-38aad91aadd2", "ambiguous"],
    ["7beeb499-d8d3-553f-92fa-0f875849f54f", "ambiguous"],
    ["faa350cd-4293-541d-929e-39f14e3a0d12", "unresolved"],
    ["abd59f4f-ec39-5145-9178-c7dc2c32d82c", "unresolved"],
    ["2cb74800-cad3-5693-92e0-9a6f40c43e87", "unresolved"],
    ["8a4ff632-396f-5f4b-8785-891a5e19b5c8", "conflicting"],
    ["5d12141c-b84b-5d13-a192-798370c31e81", "ambiguous"],
    ["279585de-84e3-5de8-9f53-5182f720ffce", "unresolved"],
    ["092994a6-390d-5137-bae2-6ed97e5bed42", "conflicting"],
  ]);
  for (const [id] of cohort) {
    const person = profile(id);
    expect(person.identity_status).toBe(expectedIdentity.get(id));
    expect(["requires_archival_review", "conflicting_sources"]).toContain(
      person.research_status,
    );
    expect(person.research_attempt_count).toBe(3);
    expect(person.immediate_pre_oss_affiliations).toEqual([]);
    expect(person.last_civilian_pre_service).toEqual([]);
    expect(person.other_pre_oss_affiliations).toEqual([]);
    expect(person.claims).toEqual([]);
    expect(person.next_action).toContain(
      "No reliable pre-OSS employer has yet been identified",
    );
  }
});

test("Batch 522 keeps the Damen and Dammen captain records separate and visibly linked", () => {
  const damen = profile("8a4ff632-396f-5f4b-8785-891a5e19b5c8");
  const dammen = profile("092994a6-390d-5137-bae2-6ed97e5bed42");
  const edward = profile("5d12141c-b84b-5d13-a192-798370c31e81");
  for (const person of [damen, dammen]) {
    expect(person).toMatchObject({
      identity_status: "conflicting",
      personnel_category: "commissioned_army_officer",
      commissioned_officer: true,
      research_status: "conflicting_sources",
      manual_review_required: true,
    });
    expect(person.name_variants).toEqual(
      expect.arrayContaining(["Arnold H Damen", "Arnold H Dammen"]),
    );
  }
  expect(damen.person_id).not.toBe(dammen.person_id);
  expect(damen.possible_duplicate_group).toBe(dammen.possible_duplicate_group);
  expect(damen.possible_duplicate_group).toMatch(/^duplicate-[a-f0-9]{12}$/);
  expect(edward).toMatchObject({
    identity_status: "ambiguous",
    personnel_category: "commissioned_army_officer",
    commissioned_officer: true,
    research_status: "requires_archival_review",
  });
});

test("Batch 522 advances exact coverage without changing unsupported claim totals", () => {
  expect(stats).toMatchObject({
    source_rows: 23978,
    person_entities: 23940,
    research_attempted_people: 4988,
    research_attempt_percent: 20.8354,
    verified_affiliation_people: 566,
    verified_affiliation_percent: 2.3642,
    verified_employer_people: 252,
    verified_employer_percent: 1.0526,
    archival_review_assessed_people: 4943,
    archival_review_percent: 20.6475,
    published_claims: 3936,
    public_sources: 3367,
  });
  expect(stats.research_status_counts).toMatchObject({
    conflicting_sources: 95,
    not_started: 18952,
    requires_archival_review: 3077,
  });
});

test("Batch 522 evidence bundle contains no private value or speculative claim payload", () => {
  const bundle = JSON.parse(evidence);
  expect(bundle).toMatchObject({
    bundle_version: "before-oss-batch522-v1",
    sources: [],
    organizations: [],
    affiliations: [],
    claims: [],
  });
  expect(bundle.person_updates).toHaveLength(11);
  expect(bundle.research_attempts).toHaveLength(11);
  expect(evidence).not.toMatch(/serial_number|service_number|possible_duplicate_group/);
});

test.describe("Batch 522 direct profile routes", () => {
  for (const [id, name] of cohort) {
    test(`${name} renders from a direct route`, async ({ page }) => {
      await page.goto(`./people/${id}/`);
      await expect(page.locator("h1")).toContainText(name);
      await expect(page.locator("body")).toContainText("Box 165");
      await expect(page.locator("body")).toContainText(
        "No reliable pre-OSS employer has yet been identified",
      );
    });
  }
});
