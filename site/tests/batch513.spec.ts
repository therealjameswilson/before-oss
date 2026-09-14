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
  ["e29063d9-b5c6-5e43-a38b-c01346fbd289", "Joseph T Curtiss", "956d72e1-ea8f-5a03-bed8-25d03f4268d3", false],
  ["5134260b-480b-539e-8c5e-a3d95a790192", "Congdon Curts", "39871542-08f3-5eac-8045-38c1e59ec34e", true],
  ["5ee2b743-35ce-552a-834d-bde54751d732", "Allen I Cushing", "65a4a1b0-ed97-5f24-8e8d-0b293ba899a9", false],
  ["434cd1b4-e492-517f-8804-b2dc5bc1a042", "Benjaminn H Cushing", "07b6b078-262a-5364-a1fa-c87933cf050a", true],
  ["619d6c35-2402-52a9-890a-52d11c842096", "Edward Cushing", "ed5b7391-4066-5dd2-b365-a7c86d006395", false],
  ["fdcc6ceb-0b24-5c98-a6f7-f0e0d8f503c3", "James R Cushing Jr.", "55a5969b-2d84-5922-a275-abd573aaf6ac", true],
  ["255713c3-b8d8-5440-b695-ffa60adc7a1e", "Lillian E Cushing", "59ad615d-9c01-5d9f-84f5-85f8c8d4fe44", false],
  ["1401a4ac-0777-5872-9506-7fd521e6050c", "Ralph H Cushing", "051a0f3d-f80a-5f97-aa24-ee92bce2ab38", true],
  ["12cbaa30-a821-5d2b-acfb-0baff3785f06", "Virginia Cushing", "6c109d4a-7df1-597e-8625-e879053e2baf", false],
  ["2f1e43d7-5fb0-5276-bb7b-acad1078bceb", "James S Cusick", "74c8d52a-0cb7-5c31-a725-79414a9c7e21", true],
] as const;

test("Batch 513 preserves page 102 rows 18-27 and masks five private fields", () => {
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

test("Batch 513 publishes Joseph Curtiss's Yale pathway at high confidence", () => {
  const joseph = profile("e29063d9-b5c6-5e43-a38b-c01346fbd289");
  expect(joseph).toMatchObject({
    identity_status: "high_confidence",
    research_status: "verified_employer_found",
    commissioned_officer: null,
  });
  expect(joseph.name_variants).toContain("Joseph Toy Curtiss");
  expect(joseph.immediate_pre_oss_affiliations).toHaveLength(1);
  expect(joseph.last_civilian_pre_service).toHaveLength(1);
  expect(joseph.immediate_pre_oss_affiliations[0]).toMatchObject({
    canonical_organization: "Yale University",
    role_title: "Assistant Professor of English",
    relationship_type: "employment",
    temporal_basis: "explicit_immediate",
    identity_confidence: "high_confidence",
    claim_confidence: "high",
    publication_status: "published",
  });
});

test("Batch 513 distinguishes Congdon Curts's Army pathway from civilian employment", () => {
  const congdon = profile("5134260b-480b-539e-8c5e-a3d95a790192");
  expect(congdon).toMatchObject({
    identity_status: "high_confidence",
    personnel_category: "enlisted_army_personnel",
    commissioned_officer: false,
    research_status: "requires_archival_review",
    last_civilian_pre_service: [],
  });
  expect(congdon.immediate_pre_oss_affiliations).toHaveLength(1);
  expect(congdon.immediate_pre_oss_affiliations[0]).toMatchObject({
    canonical_organization: "United States Army",
    role_title: "Staff Sergeant",
    relationship_type: "military_assignment",
    temporal_basis: "explicit_immediate",
    claim_confidence: "high",
  });
});

test("Batch 513 preserves Benjaminn while publishing Benjamin Cushing's two unordered librarian roles", () => {
  const benjamin = profile("434cd1b4-e492-517f-8804-b2dc5bc1a042");
  expect(benjamin).toMatchObject({
    display_name: "Benjaminn H Cushing",
    identity_status: "high_confidence",
    personnel_category: "commissioned_army_officer",
    commissioned_officer: true,
    research_status: "documented_prewar_employer_found",
    immediate_pre_oss_affiliations: [],
    last_civilian_pre_service: [],
  });
  expect(benjamin.name_variants).toContain("Benjamin H Cushing Jr");
  expect(benjamin.other_pre_oss_affiliations).toHaveLength(2);
  expect(
    benjamin.other_pre_oss_affiliations.map(
      (item: { canonical_organization: string }) => item.canonical_organization,
    ),
  ).toEqual(expect.arrayContaining(["New York Public Library", "Purdue University"]));
  for (const affiliation of benjamin.other_pre_oss_affiliations) {
    expect(affiliation).toMatchObject({
      role_title: "Librarian",
      relationship_type: "employment",
      temporal_basis: "documented_prewar",
      claim_confidence: "high",
    });
  }
});

test("Batch 513 keeps Edward Cushing's concurrent roles separate and qualified", () => {
  const edward = profile("619d6c35-2402-52a9-890a-52d11c842096");
  expect(edward).toMatchObject({
    identity_status: "high_confidence",
    research_status: "verified_employer_found",
    commissioned_officer: null,
  });
  expect(edward.name_variants).toContain("Edward Thomas Francis Cushing");
  expect(edward.immediate_pre_oss_affiliations).toHaveLength(2);
  expect(edward.last_civilian_pre_service).toHaveLength(2);
  expect(
    edward.last_civilian_pre_service.map(
      (item: { relationship_type: string }) => item.relationship_type,
    ),
  ).toEqual(expect.arrayContaining(["employment", "self_employment"]));
  for (const affiliation of edward.last_civilian_pre_service) {
    expect(affiliation).toMatchObject({
      temporal_basis: "probable_immediate",
      identity_confidence: "high_confidence",
      claim_confidence: "medium",
      publication_status: "publish_qualified",
    });
  }
});

test("Batch 513 publishes Ralph Cushing only as an identifier-backed occupation", () => {
  const ralph = profile("1401a4ac-0777-5872-9506-7fd521e6050c");
  expect(ralph).toMatchObject({
    identity_status: "confirmed",
    personnel_category: "enlisted_army_personnel",
    commissioned_officer: false,
    research_status: "occupation_only_found",
    immediate_pre_oss_affiliations: [],
    last_civilian_pre_service: [],
  });
  expect(ralph.other_pre_oss_affiliations).toHaveLength(1);
  expect(ralph.other_pre_oss_affiliations[0]).toMatchObject({
    occupation: "Foreman, not elsewhere classified",
    relationship_type: "unknown",
    end_date: "1944-07-17",
    temporal_basis: "strongly_date_bounded",
    claim_confidence: "medium",
    organization_id: null,
  });
});

test("Batch 513 qualifies Virginia and preserves the remaining unresolved identities", () => {
  const virginia = profile("12cbaa30-a821-5d2b-acfb-0baff3785f06");
  expect(virginia).toMatchObject({
    identity_status: "probable",
    research_status: "needs_identity_review",
    commissioned_officer: null,
    last_civilian_pre_service: [],
  });
  expect(virginia.name_variants).toContain("Virginia Rogers Cushing");
  expect(virginia.immediate_pre_oss_affiliations).toHaveLength(1);
  expect(virginia.immediate_pre_oss_affiliations[0]).toMatchObject({
    organization_name_as_found: "Department of the Army",
    role_title: "Prisoner-of-war mail censor",
    relationship_type: "government_assignment",
    identity_confidence: "probable",
    claim_confidence: "medium",
    publication_status: "publish_qualified",
  });

  for (const id of [
    "5ee2b743-35ce-552a-834d-bde54751d732",
    "255713c3-b8d8-5440-b695-ffa60adc7a1e",
  ]) {
    expect(profile(id)).toMatchObject({
      identity_status: "unresolved",
      research_status: "requires_archival_review",
      claims: [],
    });
  }
  for (const id of [
    "fdcc6ceb-0b24-5c98-a6f7-f0e0d8f503c3",
    "2f1e43d7-5fb0-5276-bb7b-acad1078bceb",
  ]) {
    expect(profile(id)).toMatchObject({
      identity_status: "ambiguous",
      research_status: "needs_identity_review",
      claims: [],
    });
  }
});

test("Batch 513 coverage and direct routes expose findings with qualifications", async ({ page }) => {
  expect(stats.research_attempted_people).toBe(4898);
  expect(stats.verified_affiliation_people).toBe(557);
  expect(stats.verified_employer_people).toBe(248);
  expect(stats.archival_review_assessed_people).toBe(4853);

  await page.goto("./people/e29063d9-b5c6-5e43-a38b-c01346fbd289/");
  await expect(page.getByRole("heading", { name: "Joseph T Curtiss", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("Yale University");
  await expect(page.locator("main")).toContainText("Joseph Toy Curtiss");

  await page.goto("./people/434cd1b4-e492-517f-8804-b2dc5bc1a042/");
  await expect(page.getByRole("heading", { name: "Benjaminn H Cushing", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("Purdue University");
  await expect(page.locator("main")).toContainText("New York Public Library");

  await page.goto("./people/619d6c35-2402-52a9-890a-52d11c842096/");
  await expect(page.getByRole("heading", { name: "Edward Cushing", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("Columbia Gramophone Company");
  await expect(page.locator("main")).toContainText("probable immediate");

  await page.goto("./people/12cbaa30-a821-5d2b-acfb-0baff3785f06/");
  await expect(page.getByRole("heading", { name: "Virginia Cushing", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("If the probable identity match is correct");
});
