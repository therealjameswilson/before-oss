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
  ["3a514f10-226d-5ca6-a485-4a04c7bdc861", "Harriet Crowley", "b416f265-cb27-5f57-8c52-fadc8cfccc07", 99, false],
  ["78414b5f-4476-504c-a355-092968173818", "Leo F Crowley", "c698b309-8165-528f-9da6-9e5b92c75a6c", 100, false],
  ["d0a6c46f-bee3-545f-a9c4-497a17a5ae98", "Mary H Crowley", "3617c09a-d539-5a91-90b6-a7fc8cf24d87", 100, false],
  ["b8f3a4d8-1d30-5c90-8c3b-4ddfcec64a05", "Robert D Crowley", "c323ea8f-1432-5ae5-92fe-2a29c2b28fd9", 100, true],
  ["831d914e-bb63-5cf1-8bcd-886520e07beb", "John R Croze", "acaa94a8-b87c-547f-93ee-a1e0b92d5559", 100, true],
  ["a22e226c-18a9-5850-8b61-d476658edbdd", "Harold L Cruikshank", "2726923f-06ad-536d-a663-715416980c63", 100, false],
  ["ca34a2fe-6e6c-5f8e-abda-746f198721a9", "Scott L Crull", "093c06b7-c9f7-5fda-8cf0-ba8ddfaa2628", 100, true],
  ["1ce078a3-716d-5ebb-be74-784e88350481", "Ida M Crumlin", "bcddb152-8e71-56c6-95eb-f46270df3766", 100, false],
  ["eb679c22-fbb5-584b-b086-2f686e8dab94", "James I Crump Jr.", "ad773a9c-9bfd-5496-ab34-40125c41c084", 100, true],
  ["eddf771b-3bff-5f56-8a00-f9d5d38a5865", "Nancy W Cruse", "3d587134-8381-53ef-b3d5-bcc06ad953e8", 100, false],
] as const;

test("Batch 502 preserves all ten page 99-100 rows and masks every printed identifier", () => {
  for (const [id, name, sourceRecordId, page, hasPrivateIdentifier] of cohort) {
    const person = profile(id);
    expect(person).toMatchObject({ display_name: name });
    const sourceRecord = person.source_records.find(
      (record: { source_record_id: string }) => record.source_record_id === sourceRecordId,
    );
    expect(sourceRecord).toMatchObject({
      box: "157",
      archive_location: "230/86/29/04",
      pdf_page: page,
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
  expect(profile("3a514f10-226d-5ca6-a485-4a04c7bdc861").source_records[0]).toMatchObject({
    notes_as_indexed: "docume",
  });
});

test("Batch 502 keeps Robert Crowley's printed captain status but rejects enlisted namesakes", () => {
  const robert = profile("b8f3a4d8-1d30-5c90-8c3b-4ddfcec64a05");
  expect(robert).toMatchObject({
    identity_status: "ambiguous",
    personnel_category: "commissioned_army_officer",
    commissioned_officer: true,
    research_status: "needs_identity_review",
    immediate_pre_oss_affiliations: [],
    last_civilian_pre_service: [],
    other_pre_oss_affiliations: [],
    claims: [],
  });
});

test("Batch 502 confirms John Croze without inventing an occupation or employer", () => {
  const john = profile("831d914e-bb63-5cf1-8bcd-886520e07beb");
  expect(john).toMatchObject({
    identity_status: "confirmed",
    personnel_category: "enlisted_army_personnel",
    commissioned_officer: false,
    research_status: "requires_archival_review",
    immediate_pre_oss_affiliations: [],
    last_civilian_pre_service: [],
    other_pre_oss_affiliations: [],
  });
  expect(john.claims).toContainEqual(
    expect.objectContaining({
      claim_type: "identity",
      claim_confidence: "confirmed",
      claim_text: expect.stringContaining("no civilian occupation or employer"),
    }),
  );
});

test("Batch 502 publishes Scott Crull's broad occupation without a named employer", () => {
  const scott = profile("ca34a2fe-6e6c-5f8e-abda-746f198721a9");
  expect(scott).toMatchObject({
    identity_status: "confirmed",
    personnel_category: "enlisted_army_personnel",
    commissioned_officer: false,
    research_status: "occupation_only_found",
    immediate_pre_oss_affiliations: [],
    last_civilian_pre_service: [],
  });
  expect(scott.other_pre_oss_affiliations).toContainEqual(
    expect.objectContaining({
      canonical_organization: null,
      occupation: "Warehousing, storekeeping, handling, loading, unloading, or related occupation, n.e.c.",
      relationship_type: "unknown",
      temporal_basis: "strongly_date_bounded",
      claim_confidence: "medium",
      publication_status: "publish_qualified",
    }),
  );
});

test("Batch 502 qualifies James Crump's Army training and never calls Harvard an employer", () => {
  const james = profile("eb679c22-fbb5-584b-b086-2f686e8dab94");
  expect(james).toMatchObject({
    identity_status: "probable",
    personnel_category: "enlisted_army_personnel",
    commissioned_officer: false,
    research_status: "needs_identity_review",
    immediate_pre_oss_affiliations: [],
    last_civilian_pre_service: [],
  });
  expect(james.name_variants).toEqual(
    expect.arrayContaining(["James I. Crump Jr.", "James Irving Crump Jr."]),
  );
  expect(james.other_pre_oss_affiliations).toContainEqual(
    expect.objectContaining({
      canonical_organization: "U.S. Army Specialized Training Program at Harvard University",
      role_title: "Chinese-language interpreter trainee",
      relationship_type: "military_assignment",
      temporal_basis: "temporal_relation_uncertain",
      claim_confidence: "medium",
      publication_status: "publish_qualified",
    }),
  );
});

test("Batch 502 keeps the remaining unresolved or ambiguous names free of public claims", () => {
  for (const id of [
    "3a514f10-226d-5ca6-a485-4a04c7bdc861",
    "78414b5f-4476-504c-a355-092968173818",
    "d0a6c46f-bee3-545f-a9c4-497a17a5ae98",
    "a22e226c-18a9-5850-8b61-d476658edbdd",
    "1ce078a3-716d-5ebb-be74-784e88350481",
    "eddf771b-3bff-5f56-8a00-f9d5d38a5865",
  ]) {
    const person = profile(id);
    expect(["unresolved", "ambiguous"]).toContain(person.identity_status);
    expect(person).toMatchObject({
      personnel_category: "unknown_or_indeterminate",
      commissioned_officer: null,
      immediate_pre_oss_affiliations: [],
      last_civilian_pre_service: [],
      other_pre_oss_affiliations: [],
      claims: [],
    });
  }
});

test("Batch 502 direct routes expose the qualified evidence and current coverage", async ({ page }) => {
  expect(stats.research_attempted_people).toBeGreaterThanOrEqual(4788);
  expect(stats.verified_affiliation_people).toBeGreaterThanOrEqual(547);
  expect(stats.verified_employer_people).toBeGreaterThanOrEqual(244);
  expect(stats.archival_review_assessed_people).toBeGreaterThanOrEqual(4743);

  await page.goto("./people/ca34a2fe-6e6c-5f8e-abda-746f198721a9/");
  await expect(page.getByRole("heading", { name: "Scott L Crull", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("Warehousing, storekeeping");
  await expect(page.locator("main")).toContainText("no employer is named");

  await page.goto("./people/eb679c22-fbb5-584b-b086-2f686e8dab94/");
  await expect(page.getByRole("heading", { name: "James I Crump Jr.", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("James Irving Crump Jr.");
  await expect(page.locator("main")).toContainText("Army Specialized Training Program at Harvard");
  await expect(page.locator("main")).toContainText("needs identity review");

  await page.goto("./people/831d914e-bb63-5cf1-8bcd-886520e07beb/");
  await expect(page.getByRole("heading", { name: "John R Croze", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("no civilian occupation or employer");

  await page.goto("./people/3a514f10-226d-5ca6-a485-4a04c7bdc861/");
  await expect(page.getByRole("heading", { name: "Harriet Crowley", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("No reliable pre-OSS employer has yet been identified");
  await expect(page.locator("main")).toContainText("docume");
});
