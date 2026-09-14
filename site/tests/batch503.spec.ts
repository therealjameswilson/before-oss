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
  ["82f178fe-ccca-55cf-a628-a8775292094c", "Malcolm A Crusius", "8abda086-6f0b-50e4-8f74-2e46c2c2f813", false],
  ["24a25b2a-49b9-52e8-a0c2-6fb90abfab2f", "Ashley W Crutchfield", "1ac63501-0e29-508e-90bc-642f778beccd", true],
  ["3400baed-e8ef-5006-8a75-a7dd7bc1bd84", "Frank E Cruz", "2d27049b-0256-51ac-b3a1-0a2b743634e1", true],
  ["b3b3d8c2-c8c5-54f3-a2b2-621597c304e5", "Manuel P Cruz Jr.", "cd58478f-1912-543e-8829-02a34f01b97e", true],
  ["2dd19716-b123-559c-b0a3-5b0c5c02b253", "Joseph Cryan", "a8b8ede6-75b6-577e-a2e6-6b82bfc78a0b", false],
  ["eca1a09c-d2c8-5464-bf0e-ca64bd30c31e", "James A Cryer Jr.", "28e9a08d-7ccc-58b5-9a82-c2d19d8ea372", true],
  ["18ee63ce-db20-5b1c-9f8f-98b7591d4bd2", "Sophie B Crystal", "5aee95f9-745a-5757-bd90-814d7c64aa39", false],
  ["40e70d9b-f075-5714-b4e2-3cc167d9b549", "Charles J Csar", "9e938181-9360-5f3a-95e0-4cfea8ee7c01", true],
  ["e7c8ab8e-9653-5b5a-9be8-fd10e51cfb2f", "John A Cucco", "6dc29868-fe53-58a1-a4c2-6b90c8f1232b", true],
  ["c761718b-f471-5e3c-a170-c70cad41522f", "Michael A Cucinotta", "d59e8631-01b4-525a-9cf5-7aa4f67a5422", true],
] as const;

test("Batch 503 preserves all ten page 100 rows and masks every printed identifier", () => {
  for (const [id, name, sourceRecordId, hasPrivateIdentifier] of cohort) {
    const person = profile(id);
    expect(person).toMatchObject({ display_name: name });
    const sourceRecord = person.source_records.find(
      (record: { source_record_id: string }) => record.source_record_id === sourceRecordId,
    );
    expect(sourceRecord).toMatchObject({
      box: "157",
      archive_location: "230/86/29/04",
      pdf_page: 100,
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

test("Batch 503 qualifies Malcolm Crusius without claiming an immediate employer", () => {
  const malcolm = profile("82f178fe-ccca-55cf-a628-a8775292094c");
  expect(malcolm).toMatchObject({
    identity_status: "probable",
    personnel_category: "commissioned_army_officer",
    commissioned_officer: true,
    research_status: "needs_identity_review",
    immediate_pre_oss_affiliations: [],
    last_civilian_pre_service: [],
  });
  expect(malcolm.other_pre_oss_affiliations).toEqual(
    expect.arrayContaining([
      expect.objectContaining({
        canonical_organization: "United States Attorney's Office for the Southern District of New York",
        role_title: "Assistant United States Attorney",
        relationship_type: "government_assignment",
        temporal_basis: "documented_prewar",
        claim_confidence: "medium",
      }),
      expect.objectContaining({
        canonical_organization: "Headquarters, First Bombardment Division, Eighth Air Force",
        relationship_type: "military_assignment",
        temporal_basis: "temporal_relation_uncertain",
        claim_confidence: "medium",
      }),
    ]),
  );
});

test("Batch 503 publishes four occupations and one student status without employers", () => {
  const expectations = [
    ["3400baed-e8ef-5006-8a75-a7dd7bc1bd84", "Construction occupation, n.e.c.", "unknown"],
    ["b3b3d8c2-c8c5-54f3-a2b2-621597c304e5", "Semiskilled occupation in canning and preserving of foods", "unknown"],
    ["eca1a09c-d2c8-5464-bf0e-ca64bd30c31e", "Mechanic and repairman, airplane", "unknown"],
    ["40e70d9b-f075-5714-b4e2-3cc167d9b549", "Student; institution not recorded", "student"],
    ["e7c8ab8e-9653-5b5a-9be8-fd10e51cfb2f", "Tailor", "unknown"],
  ] as const;

  for (const [id, occupation, relationshipType] of expectations) {
    const person = profile(id);
    expect(person).toMatchObject({
      identity_status: "confirmed",
      personnel_category: "enlisted_army_personnel",
      commissioned_officer: false,
      research_status: "occupation_only_found",
      immediate_pre_oss_affiliations: [],
      last_civilian_pre_service: [],
    });
    expect(person.other_pre_oss_affiliations).toContainEqual(
      expect.objectContaining({
        canonical_organization: null,
        occupation,
        relationship_type: relationshipType,
        temporal_basis: "strongly_date_bounded",
        claim_confidence: "medium",
        publication_status: "publish_qualified",
      }),
    );
  }
});

test("Batch 503 keeps Ashley, Joseph and Sophie candidates out of public facts", () => {
  const ashley = profile("24a25b2a-49b9-52e8-a0c2-6fb90abfab2f");
  expect(ashley).toMatchObject({
    identity_status: "ambiguous",
    personnel_category: "unknown_or_indeterminate",
    commissioned_officer: null,
    research_status: "needs_identity_review",
    immediate_pre_oss_affiliations: [],
    last_civilian_pre_service: [],
    other_pre_oss_affiliations: [],
    claims: [],
  });

  const joseph = profile("2dd19716-b123-559c-b0a3-5b0c5c02b253");
  expect(joseph).toMatchObject({
    identity_status: "ambiguous",
    personnel_category: "foreign_or_allied_military_personnel",
    commissioned_officer: false,
    allied_or_foreign_personnel: true,
    research_status: "needs_identity_review",
    immediate_pre_oss_affiliations: [],
    last_civilian_pre_service: [],
    other_pre_oss_affiliations: [],
    claims: [],
  });

  const sophie = profile("18ee63ce-db20-5b1c-9f8f-98b7591d4bd2");
  expect(sophie).toMatchObject({
    identity_status: "unresolved",
    research_status: "requires_archival_review",
    other_pre_oss_affiliations: [],
    claims: [],
  });
});

test("Batch 503 withholds Michael Cucinotta's post-OSS occupation", () => {
  const michael = profile("c761718b-f471-5e3c-a170-c70cad41522f");
  expect(michael).toMatchObject({
    identity_status: "confirmed",
    personnel_category: "enlisted_army_personnel",
    commissioned_officer: false,
    research_status: "requires_archival_review",
    immediate_pre_oss_affiliations: [],
    last_civilian_pre_service: [],
    other_pre_oss_affiliations: [],
  });
  expect(michael.claims).toContainEqual(
    expect.objectContaining({
      claim_type: "identity",
      claim_confidence: "confirmed",
      claim_text: expect.stringContaining("cannot establish a pre-OSS affiliation"),
    }),
  );
  expect(JSON.stringify(michael.other_pre_oss_affiliations)).not.toContain("Shipping and receiving");
});

test("Batch 503 public totals preserve confidence-aware analytics", () => {
  expect(stats.research_attempted_people).toBe(4798);
  expect(stats.verified_affiliation_people).toBe(547);
  expect(stats.verified_employer_people).toBe(244);
  expect(stats.archival_review_assessed_people).toBe(4753);
});

test("Batch 503 direct routes expose qualified evidence and archival guidance", async ({ page }) => {
  await page.goto("./people/82f178fe-ccca-55cf-a628-a8775292094c/");
  await expect(page.getByRole("heading", { name: "Malcolm A Crusius", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("Assistant United States Attorney");
  await expect(page.locator("main")).toContainText("First Bombardment Division");
  await expect(page.locator("main")).toContainText("needs identity review");

  await page.goto("./people/b3b3d8c2-c8c5-54f3-a2b2-621597c304e5/");
  await expect(page.getByRole("heading", { name: "Manuel P Cruz Jr.", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("canning and preserving of foods");
  await expect(page.locator("main")).toContainText("no employer");

  await page.goto("./people/40e70d9b-f075-5714-b4e2-3cc167d9b549/");
  await expect(page.getByRole("heading", { name: "Charles J Csar", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("Student; institution not recorded");

  await page.goto("./people/c761718b-f471-5e3c-a170-c70cad41522f/");
  await expect(page.getByRole("heading", { name: "Michael A Cucinotta", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("16 October 1945");
  await expect(page.locator("main")).toContainText("cannot establish a pre-OSS affiliation");

  await page.goto("./people/18ee63ce-db20-5b1c-9f8f-98b7591d4bd2/");
  await expect(page.getByRole("heading", { name: "Sophie B Crystal", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("No reliable pre-OSS employer has yet been identified");
});
