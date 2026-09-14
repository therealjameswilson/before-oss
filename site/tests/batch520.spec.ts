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
  ["1e53babf-16ab-5529-a74a-1d944e8d413f", "John P Dalberg", "0a42b1e9-1cc6-5d4a-9dc7-10c9a48f43ce", 103, true],
  ["239218cd-90f7-5691-8428-fcb850f16847", "Hope Dale", "c6d12d2b-903f-5a8f-87ce-89ed69ecfaa3", 103, false],
  ["f6438eed-0236-5098-853b-3f976a314cea", "Ernest D'Alessandro", "ebac941a-2260-5505-bf3a-c88ca1307d86", 103, true],
  ["477143b5-c899-5111-ab9d-9895d74ad1ea", "Giuseppe D'Alessandro", "8e9e8278-fdf2-57cb-ac9a-d532244a062f", 103, true],
  ["ccdc6027-ee0e-5b5e-9c13-9b9721294ff6", "Donald D Daley", "eea35a78-ea0c-5c1b-950f-95a47ad18b19", 103, false],
  ["e3d99ad9-602d-5e49-9d52-efad9ee68629", "John F Daley", "e6ffc56a-a8d6-5069-8cfd-d119e2c46c5d", 104, false],
  ["d24f062c-1d5f-5cb9-b868-cac337d78fbc", "Mary Daley", "801fbb6a-3b72-57a2-9a77-32d2fd5094c8", 104, true],
  ["b3b2fdf6-fde4-557c-9795-c2a26f3361ab", "John H Dalgarn", "39f48623-6cf2-5ae2-822d-5f74a192589f", 104, true],
  ["751fb3d4-7e8c-5278-933a-a5f33d70fe68", "James B Dalgliesh", "cf37ef9a-9a9c-5f60-ac44-5ff0092aad1a", 104, true],
  ["5f351eb8-9fa1-537e-96a0-02082a43e8c5", "Lucille Dalious", "cab3ecf5-b98b-5334-b7b3-6a9d1bef9908", 104, true],
] as const;

test("Batch 520 preserves the page 103-104 cohort and masks seven private fields", () => {
  for (const [id, name, sourceRecordId, pdfPage, hasPrivateIdentifier] of cohort) {
    const person = profile(id);
    expect(person).toMatchObject({ display_name: name });
    const sourceRecord = person.source_records.find(
      (record: { source_record_id: string }) => record.source_record_id === sourceRecordId,
    );
    expect(sourceRecord).toMatchObject({
      box: "164",
      archive_location: "230/86/29/05",
      pdf_page: pdfPage,
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

test("Batch 520 confirms John Dalberg's bounded petroleum occupation without inventing an employer", () => {
  const john = profile("1e53babf-16ab-5529-a74a-1d944e8d413f");
  expect(john).toMatchObject({
    identity_status: "confirmed",
    personnel_category: "enlisted_army_personnel",
    commissioned_officer: false,
    research_status: "occupation_only_found",
    immediate_pre_oss_affiliations: [],
    last_civilian_pre_service: [],
  });
  expect(john.other_pre_oss_affiliations).toHaveLength(1);
  expect(john.other_pre_oss_affiliations[0]).toMatchObject({
    organization_id: null,
    occupation: "Occupations in refining of petroleum",
    relationship_type: "unknown",
    temporal_basis: "strongly_date_bounded",
    claim_confidence: "medium",
  });
});

test("Batch 520 preserves Ernest D'Alessandro's Army first-name variant and occupation limits", () => {
  const ernest = profile("f6438eed-0236-5098-853b-3f976a314cea");
  expect(ernest).toMatchObject({
    identity_status: "confirmed",
    personnel_category: "enlisted_army_personnel",
    commissioned_officer: false,
    research_status: "occupation_only_found",
  });
  expect(ernest.name_variants).toContain("Ernesto Dalessandro");
  expect(ernest.other_pre_oss_affiliations[0]).toMatchObject({
    organization_id: null,
    occupation: "Occupations in production of rubber goods",
    relationship_type: "unknown",
    claim_confidence: "medium",
  });
  expect(ernest.claims).toHaveLength(2);
});

test("Batch 520 preserves Giuseppe D'Alessandro's misspelled Army variant and no employer", () => {
  const giuseppe = profile("477143b5-c899-5111-ab9d-9895d74ad1ea");
  expect(giuseppe).toMatchObject({
    identity_status: "confirmed",
    personnel_category: "enlisted_army_personnel",
    commissioned_officer: false,
    research_status: "occupation_only_found",
    immediate_pre_oss_affiliations: [],
    last_civilian_pre_service: [],
  });
  expect(giuseppe.name_variants).toContain("Guiseppe Dalessandro");
  expect(giuseppe.other_pre_oss_affiliations[0]).toMatchObject({
    organization_id: null,
    occupation: "Retail managers",
    relationship_type: "unknown",
  });
});

test("Batch 520 confirms James Dalgliesh while retaining the Army spelling variant", () => {
  const james = profile("751fb3d4-7e8c-5278-933a-a5f33d70fe68");
  expect(james).toMatchObject({
    identity_status: "confirmed",
    personnel_category: "enlisted_army_personnel",
    commissioned_officer: false,
    research_status: "occupation_only_found",
    immediate_pre_oss_affiliations: [],
    last_civilian_pre_service: [],
  });
  expect(james.name_variants).toContain("James B Delgliesh");
  expect(james.other_pre_oss_affiliations[0]).toMatchObject({
    organization_id: null,
    occupation: "Retail managers",
    relationship_type: "unknown",
  });
  expect(james.claims).toHaveLength(2);
});

test("Batch 520 distinguishes Lucille Dalious's student status from occupation and employment", () => {
  const lucille = profile("5f351eb8-9fa1-537e-96a0-02082a43e8c5");
  expect(lucille).toMatchObject({
    identity_status: "high_confidence",
    personnel_category: "enlisted_army_personnel",
    commissioned_officer: false,
    research_status: "completed",
    immediate_pre_oss_affiliations: [],
    last_civilian_pre_service: [],
  });
  expect(lucille.other_pre_oss_affiliations).toHaveLength(2);
  expect(lucille.other_pre_oss_affiliations[0]).toMatchObject({
    canonical_organization: "Southern Methodist University",
    organization_name_as_found: "Southern-Methodist University",
    occupation: "Student",
    relationship_type: "student",
    temporal_basis: "documented_prewar",
    claim_confidence: "high",
  });
  expect(lucille.other_pre_oss_affiliations[1]).toMatchObject({
    organization_id: null,
    occupation: "Stenographers and typists",
    relationship_type: "unknown",
    temporal_basis: "strongly_date_bounded",
    claim_confidence: "medium",
  });
  expect(lucille.claims).toHaveLength(3);
});

test("Batch 520 exposes five unresolved or ambiguous cases with Box 164 review actions", () => {
  const expected = new Map([
    ["239218cd-90f7-5691-8428-fcb850f16847", ["ambiguous", "needs_identity_review"]],
    ["ccdc6027-ee0e-5b5e-9c13-9b9721294ff6", ["unresolved", "requires_archival_review"]],
    ["e3d99ad9-602d-5e49-9d52-efad9ee68629", ["ambiguous", "needs_identity_review"]],
    ["d24f062c-1d5f-5cb9-b868-cac337d78fbc", ["unresolved", "requires_archival_review"]],
    ["b3b2fdf6-fde4-557c-9795-c2a26f3361ab", ["ambiguous", "needs_identity_review"]],
  ]);
  for (const [id, [identityStatus, researchStatus]] of expected) {
    expect(profile(id)).toMatchObject({
      identity_status: identityStatus,
      personnel_category: "unknown_or_indeterminate",
      commissioned_officer: null,
      research_status: researchStatus,
      immediate_pre_oss_affiliations: [],
      last_civilian_pre_service: [],
      other_pre_oss_affiliations: [],
      claims: [],
      archival_file: { box: "164", indexed: true, digitized: false, reviewed: false },
    });
  }
});

test("Batch 520 advances exact aggregate coverage without changing the index denominator", () => {
  expect(stats).toMatchObject({
    source_rows: 23978,
    person_entities: 23940,
    research_attempted_people: 4967,
    research_attempt_percent: 20.7477,
    verified_affiliation_people: 566,
    verified_affiliation_percent: 2.3642,
    verified_employer_people: 252,
    verified_employer_percent: 1.0526,
    archival_review_assessed_people: 4922,
    archival_review_percent: 20.5597,
    published_claims: 3923,
    public_sources: 3361,
  });
  expect(stats.research_status_counts).toMatchObject({
    completed: 143,
    needs_identity_review: 273,
    not_started: 18973,
    occupation_only_found: 904,
    requires_archival_review: 3066,
    verified_employer_found: 237,
  });
});

test("Batch 520 creates a direct Southern Methodist University organization route", async ({ page }) => {
  await page.goto("./organizations/634a30e3-feea-5606-ae88-cac8f35bf441/");
  await expect(page.locator("h1")).toContainText("Southern Methodist University");
  await expect(page.locator("body")).toContainText("Lucille Dalious");
  await expect(page.locator("body")).toContainText("Student and Alpha Xi pledge");
});

test.describe("Batch 520 direct profile routes", () => {
  for (const [id, name] of cohort) {
    test(`${name} renders from a direct route`, async ({ page }) => {
      await page.goto(`./people/${id}/`);
      await expect(page.locator("h1")).toContainText(name);
      await expect(page.locator("body")).toContainText("Box 164");
    });
  }
});
