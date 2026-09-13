import { expect, test } from "@playwright/test";
import fs from "node:fs";

const people = JSON.parse(
  fs.readFileSync(new URL("../src/data/generated/people.json", import.meta.url), "utf8"),
);
const profile = (id: string) =>
  people.find((person: { person_id: string }) => person.person_id === id);

test("Batch 481 preserves page 95 rows 20-29 and masks private identifiers", () => {
  const expected = [
    ["6cb343a8-c2ff-5649-b3a4-e307603d04cd", "Frank L Coursen Jr.", "08ddd267-749a-5310-a7d5-2c3a9cc38a42", "••••4055", "148"],
    ["36c18618-6871-562f-8a20-088d7ea462ec", "Canby Courtlandt", "42f1799b-83f2-50ba-bab9-d21f0f98c764", null, "148"],
    ["086cd59e-01e4-5085-bfe6-8478a7c4ead6", "Anna S Courtney", "61d77314-d4aa-5bc7-8b50-a1f7d83a2910", null, "148"],
    ["be8c16f6-0275-509e-bbe8-c87a09594205", "Rosemarie C Courtney", "f27b3ce5-994a-51fe-9373-5c7613c6364e", null, "148"],
    ["dc2b29c1-b8aa-5317-a035-c3b1e9a2e3b2", "Armand H Courtot", "5edfb968-8474-5569-a1da-fbcbc01b1d5f", "••••7160", "148"],
    ["07a58874-e735-5340-9877-5c9d245ea39a", "William F Courtright", "fa24721e-6791-538c-a814-2011c6f33deb", "••••9522", "148"],
    ["0a506119-e6ae-5a48-806d-27859833aee6", "Forrest Courtwright", "659a6a0b-7c65-50c0-b776-4fe02243efbb", null, "148"],
    ["ed87ea70-0fcb-532e-b7ac-6b6aba54d446", "Walter J Cousins", "786e96bb-c2af-5268-99d3-0d99f3784fe3", null, "149"],
    ["bbe41c8b-f906-5ce4-ba3f-f351f5526053", "William S Cousins", "db454eb5-d948-5092-b3d2-8e98fe2b74bc", null, "148"],
    ["82212ca6-e815-57ca-b4ea-3caf8025c31d", "William S Cousins", "71e217bc-4c81-51b8-9429-1e83ff6adce8", null, "149"],
  ];

  for (const [id, name, sourceRecordId, serial, box] of expected) {
    const person = profile(String(id));
    expect(person).toMatchObject({ display_name: name });
    expect(person.source_records).toContainEqual(
      expect.objectContaining({
        source_record_id: sourceRecordId,
        serial_masked: serial,
        box,
        archive_location: "230/86/29/03",
        pdf_page: 95,
      }),
    );
    expect(JSON.stringify(person)).not.toMatch(
      /"serial_number"|"serial_number_raw"|"serial_number_normalized"/,
    );
  }
});

test("Batch 481 records Armand Courtot as a student without inventing an employer", () => {
  const person = profile("dc2b29c1-b8aa-5317-a035-c3b1e9a2e3b2");
  expect(person).toMatchObject({
    display_name: "Armand H Courtot",
    identity_status: "confirmed",
    personnel_category: "enlisted_army_personnel",
    commissioned_officer: false,
    research_status: "occupation_only_found",
    immediate_pre_oss_affiliations: [],
    last_civilian_pre_service: [],
  });
  expect(person.other_pre_oss_affiliations).toContainEqual(
    expect.objectContaining({
      occupation: "Student",
      relationship_type: "student",
      temporal_basis: "strongly_date_bounded",
      claim_confidence: "medium",
      end_date: "1943-03-12",
    }),
  );
  expect(person.claims).toContainEqual(
    expect.objectContaining({
      claim_type: "occupation",
      claim_confidence: "medium",
      publication_status: "publish_qualified",
    }),
  );
});

test("Batch 481 renders the qualified Courtot student-status evidence", async ({ page }) => {
  await page.goto("./people/dc2b29c1-b8aa-5317-a035-c3b1e9a2e3b2/");
  await expect(page.getByRole("heading", { name: "Armand H Courtot", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("Student");
  await expect(page.locator("main")).toContainText("12 March 1943");
  await expect(page.locator("main")).toContainText("No school, employer");
  await expect(page.locator("main")).toContainText(
    "No reliable pre-OSS employer has yet been identified",
  );
});

test("Batch 481 keeps the two William S Cousins rows separate in one review group", async ({ page }) => {
  const box148 = profile("bbe41c8b-f906-5ce4-ba3f-f351f5526053");
  const box149 = profile("82212ca6-e815-57ca-b4ea-3caf8025c31d");
  expect(box148.person_id).not.toBe(box149.person_id);
  expect(box148.possible_duplicate_group).toBe(box149.possible_duplicate_group);
  for (const person of [box148, box149]) {
    expect(person).toMatchObject({
      display_name: "William S Cousins",
      identity_status: "ambiguous",
      research_status: "needs_identity_review",
      manual_review_required: true,
      immediate_pre_oss_affiliations: [],
      last_civilian_pre_service: [],
      other_pre_oss_affiliations: [],
    });
  }

  await page.goto("./people/bbe41c8b-f906-5ce4-ba3f-f351f5526053/");
  await expect(page.locator("main")).toContainText("different boxes, 148 and 149");
  await expect(page.locator("main")).toContainText("Compare the Box 148 and Box 149 files");
});

test("Batch 481 preserves the Canby Courtlandt transposition as a probable duplicate", () => {
  const transposed = profile("36c18618-6871-562f-8a20-088d7ea462ec");
  const conventional = profile("e08147c7-73c7-5a7d-9e00-16b7f764b3bc");
  expect(transposed.person_id).not.toBe(conventional.person_id);
  expect(transposed).toMatchObject({
    display_name: "Canby Courtlandt",
    identity_status: "probable",
    research_status: "needs_identity_review",
    manual_review_required: true,
    immediate_pre_oss_affiliations: [],
    last_civilian_pre_service: [],
    other_pre_oss_affiliations: [],
  });
  expect(transposed.possible_duplicate_group).toBe(conventional.possible_duplicate_group);
});

test("Batch 481 leaves six unsupported identities unresolved with archival actions", () => {
  for (const id of [
    "6cb343a8-c2ff-5649-b3a4-e307603d04cd",
    "086cd59e-01e4-5085-bfe6-8478a7c4ead6",
    "be8c16f6-0275-509e-bbe8-c87a09594205",
    "07a58874-e735-5340-9877-5c9d245ea39a",
    "0a506119-e6ae-5a48-806d-27859833aee6",
    "ed87ea70-0fcb-532e-b7ac-6b6aba54d446",
  ]) {
    expect(profile(id)).toMatchObject({
      identity_status: "unresolved",
      research_status: "requires_archival_review",
      manual_review_required: true,
      immediate_pre_oss_affiliations: [],
      last_civilian_pre_service: [],
      other_pre_oss_affiliations: [],
      claims: [],
    });
  }
});
