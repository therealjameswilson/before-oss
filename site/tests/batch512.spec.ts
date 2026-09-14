import { expect, test } from "@playwright/test";
import fs from "node:fs";

const people = JSON.parse(
  fs.readFileSync(new URL("../src/data/generated/people.json", import.meta.url), "utf8"),
);
const stats = JSON.parse(
  fs.readFileSync(new URL("../src/data/generated/stats.json", import.meta.url), "utf8"),
);
const profile = (id: string) =>
  people.find((person: { person_id: string }) => person.person_id === id);

const cohort = [
  ["79d05c67-7846-5099-91d6-4953cc3c1241", "Joseph T Curtis", "af432d6f-4113-5a3c-a6e8-0f9d810a5080", false],
  ["e630b432-fc4d-54e5-822d-99d7d91ee160", "Leslie S Curtis", "c6c62f7b-90e4-56ec-9b31-5460f7617cc3", true],
  ["ee45b324-4a13-5070-8a67-cf17906b148c", "Paul M Curtis", "e852efaa-b591-55a1-b8f9-e6f5409150b0", true],
  ["c5dd904a-870c-5a79-a9f3-82320190676c", "Phillip D Curtis", "a7567ece-32be-5bbe-8b34-fb11cb4c483e", false],
  ["120d1a30-38ab-5362-997c-178b93a27408", "Reid H Curtis", "8ebb0b58-ae6a-5400-bb96-b1cd7ce03d9a", true],
  ["0951f047-080f-55d6-8661-4712b979c218", "Richard R Curtis", "c97a1589-a86b-5d11-b2e1-109ccaa17588", true],
  ["ef0777d5-05bc-50aa-a447-647fd4b2d111", "Sturgeon E Curtis", "afd6da46-c4d3-5e42-b7a5-591b461e1836", false],
  ["a4bea9af-3408-58c6-b0d4-f55dc126e656", "Thomas L Curtis", "9f3edfb7-8e95-5e8f-86bb-79d5c7f2ebd9", false],
  ["817bb2bb-8ab5-58ec-9aaf-90ed81b989c1", "Carl C Curtiss", "d6ae7c1d-c958-58ee-b3f7-cbf0155cdbc9", false],
  ["1b2e6ed4-a085-5053-988d-cbc45042e445", "John S Curtiss", "4daa849e-f84a-5244-ad2a-ed7cab1adc70", false],
] as const;

test("Batch 512 preserves the Box 161 cohort and masks every private field", () => {
  for (const [id, name, sourceRecordId, hasPrivateIdentifier] of cohort) {
    const person = profile(id);
    expect(person).toMatchObject({ display_name: name });
    const sourceRecord = person.source_records.find(
      (record: { source_record_id: string }) => record.source_record_id === sourceRecordId,
    );
    expect(sourceRecord).toMatchObject({
      box: "161",
      archive_location: "230/86/29/04",
      pdf_page: 102,
      rank_as_indexed: null,
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

test("Batch 512 confirms Leslie and Reid without inventing employers", () => {
  const leslie = profile("e630b432-fc4d-54e5-822d-99d7d91ee160");
  expect(leslie).toMatchObject({
    identity_status: "confirmed",
    personnel_category: "enlisted_army_personnel",
    commissioned_officer: false,
    research_status: "requires_archival_review",
    immediate_pre_oss_affiliations: [],
    last_civilian_pre_service: [],
    other_pre_oss_affiliations: [],
  });
  expect(leslie.name_variants).toContain("Leslie S Curtis Jr");
  expect(JSON.stringify(leslie)).not.toContain('"occupation":"993"');

  const reid = profile("120d1a30-38ab-5362-997c-178b93a27408");
  expect(reid).toMatchObject({
    identity_status: "confirmed",
    personnel_category: "enlisted_army_personnel",
    commissioned_officer: false,
    research_status: "occupation_only_found",
    immediate_pre_oss_affiliations: [],
    last_civilian_pre_service: [],
  });
  expect(reid.other_pre_oss_affiliations).toHaveLength(1);
  expect(reid.other_pre_oss_affiliations[0]).toMatchObject({
    occupation: "Student",
    relationship_type: "student",
    end_date: "1944-02-16",
    temporal_basis: "strongly_date_bounded",
    claim_confidence: "medium",
    publication_status: "publish_qualified",
    organization_id: null,
  });
});

test("Batch 512 publishes Thomas Curtis only as a qualified military pathway", () => {
  const thomas = profile("a4bea9af-3408-58c6-b0d4-f55dc126e656");
  expect(thomas).toMatchObject({
    identity_status: "probable",
    personnel_category: "enlisted_marine_corps_personnel",
    commissioned_officer: false,
    research_status: "needs_identity_review",
    last_civilian_pre_service: [],
    other_pre_oss_affiliations: [],
  });
  expect(thomas.immediate_pre_oss_affiliations).toHaveLength(1);
  expect(thomas.immediate_pre_oss_affiliations[0]).toMatchObject({
    canonical_organization: "Reconnaissance Section, Amphibious Corps, Atlantic",
    role_title: "Rubber-boat handling instructor",
    relationship_type: "military_assignment",
    city: "Quantico",
    state_or_region: "Virginia",
    temporal_basis: "explicit_immediate",
    identity_confidence: "probable",
    claim_confidence: "medium",
    publication_status: "publish_qualified",
  });
  expect(thomas.claims.some((claim: { claim_type: string }) => claim.claim_type === "immediate_pre_oss_affiliation")).toBe(true);
});

test("Batch 512 qualifies John Curtiss's last civilian employer and leaves namesakes unresolved", () => {
  const john = profile("1b2e6ed4-a085-5053-988d-cbc45042e445");
  expect(john).toMatchObject({
    identity_status: "probable",
    personnel_category: "unknown_or_indeterminate",
    commissioned_officer: null,
    research_status: "needs_identity_review",
    immediate_pre_oss_affiliations: [],
    other_pre_oss_affiliations: [],
  });
  expect(john.name_variants).toContain("John Shelton Curtiss");
  expect(john.last_civilian_pre_service).toHaveLength(1);
  expect(john.last_civilian_pre_service[0]).toMatchObject({
    canonical_organization: "Franklin D. Roosevelt Library",
    role_title: "Assistant archivist",
    relationship_type: "employment",
    temporal_basis: "probable_immediate",
    identity_confidence: "probable",
    claim_confidence: "medium",
    publication_status: "publish_qualified",
  });

  for (const id of [
    "79d05c67-7846-5099-91d6-4953cc3c1241",
    "c5dd904a-870c-5a79-a9f3-82320190676c",
    "ef0777d5-05bc-50aa-a447-647fd4b2d111",
    "817bb2bb-8ab5-58ec-9aaf-90ed81b989c1",
  ]) {
    expect(profile(id)).toMatchObject({
      identity_status: "unresolved",
      research_status: "requires_archival_review",
      commissioned_officer: null,
      immediate_pre_oss_affiliations: [],
      last_civilian_pre_service: [],
      other_pre_oss_affiliations: [],
      claims: [],
    });
  }
  for (const id of [
    "ee45b324-4a13-5070-8a67-cf17906b148c",
    "0951f047-080f-55d6-8661-4712b979c218",
  ]) {
    expect(profile(id)).toMatchObject({
      identity_status: "ambiguous",
      research_status: "needs_identity_review",
      commissioned_officer: null,
      immediate_pre_oss_affiliations: [],
      last_civilian_pre_service: [],
      other_pre_oss_affiliations: [],
      claims: [],
    });
  }
});

test("Batch 512 coverage and direct routes expose findings with qualifications", async ({ page }) => {
  expect(stats.research_attempted_people).toBe(4888);
  expect(stats.verified_affiliation_people).toBe(554);
  expect(stats.verified_employer_people).toBe(246);
  expect(stats.archival_review_assessed_people).toBe(4843);

  await page.goto("./people/120d1a30-38ab-5362-997c-178b93a27408/");
  await expect(page.getByRole("heading", { name: "Reid H Curtis", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("Student");
  await expect(page.locator("main")).toContainText("no school, course, employment");

  await page.goto("./people/a4bea9af-3408-58c6-b0d4-f55dc126e656/");
  await expect(page.getByRole("heading", { name: "Thomas L Curtis", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("Reconnaissance Section");
  await expect(page.locator("main")).toContainText("If the probable identity match is correct");

  await page.goto("./people/1b2e6ed4-a085-5053-988d-cbc45042e445/");
  await expect(page.getByRole("heading", { name: "John S Curtiss", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("Franklin D. Roosevelt Library");
  await expect(page.locator("main")).toContainText("probable identity match");
});
