import { expect, test } from "@playwright/test";
import fs from "node:fs";

const people = JSON.parse(
  fs.readFileSync(new URL("../src/data/generated/people.json", import.meta.url), "utf8"),
);
const profile = (id: string) =>
  people.find((person: { person_id: string }) => person.person_id === id);

test("Batch 473 preserves page 93 rows 32-41 and masks private identifiers", () => {
  const expected = [
    ["5c4ccadb-8b8a-50e0-8e71-8fae0cff6c3f", "Tully R Cornick Jr.", "30d600cd-6e0a-5f54-95da-4a50a2346917", "••••1779", null, null],
    ["66969e0a-fbe9-5585-b23e-a42d32a0e659", "George H Cornish", "a61979f8-0883-528b-9b90-b7f9e3c39a5e", "••••9697", null, null],
    ["846a5268-845f-57c7-b6a8-163e9246b300", "Andre Cornut", "ad1fa1b0-8d37-599f-ba4a-c65f6e75e419", null, "Capt", "French"],
    ["21ca6b99-0cf9-5fc4-926d-02463a24b05f", "Beatrice L Corr", "43de920c-d10c-59b9-9ceb-6781bb2aee3a", null, null, null],
    ["89491a94-b0da-5edf-bcd6-76316e01f4c1", "Margaret M Corragio", "f5dbca15-35bd-5bba-a84a-24f6367aefcd", "••••6333", null, null],
    ["3525173e-a159-573d-ad9f-10e4889e028c", "William I Correa", "d7d49e0f-04f6-5243-b3a2-cf07cd01d630", "••••7113", null, null],
    ["717ce632-7dd4-5519-99f1-f138e180c085", "Louise J Correri", "00c1c12d-1a46-588e-9e7c-7b79f42bd771", null, "Pvt", null],
    ["fa649630-9bf9-5c87-acdf-bb5e3a5b77ae", "Bruce Corrick", "e9d0a601-7d1b-52f3-9336-54bb56d69de4", "••••0905", null, null],
    ["c4c8394a-c3c6-52f9-9cce-eed2d158edb1", "John H Corridon", "9ae887cb-f0e4-5ab6-9be2-61be456e09b9", "••••0063", null, null],
    ["bbbc2fac-83f2-5f77-8aac-65bf979c87c6", "John P Corriera", "a19674e3-42ac-5933-b779-a9419122b464", "••••5251", null, null],
  ];

  for (const [id, name, sourceRecordId, serial, rank, notes] of expected) {
    const person = profile(String(id));
    expect(person).toMatchObject({ display_name: name });
    expect(person.source_records).toContainEqual(
      expect.objectContaining({
        source_record_id: sourceRecordId,
        serial_masked: serial,
        rank_as_indexed: rank,
        notes_as_indexed: notes,
        box: "145",
        archive_location: "230/86/29/02",
        pdf_page: 93,
      }),
    );
    expect(JSON.stringify(person)).not.toMatch(
      /"serial_number"|"serial_number_raw"|"serial_number_normalized"/,
    );
  }
});

test("Batch 473 publishes only bounded occupations for Cornick and Correa", async ({ page }) => {
  const cases = [
    ["5c4ccadb-8b8a-50e0-8e71-8fae0cff6c3f", "Tully R Cornick Jr.", "Sales clerks", "1942-02-12"],
    ["3525173e-a159-573d-ad9f-10e4889e028c", "William I Correa", "Stenographers and typists", "1941-08-20"],
  ];
  for (const [id, name, occupation, endDate] of cases) {
    const person = profile(id);
    expect(person).toMatchObject({
      display_name: name,
      identity_status: "confirmed",
      personnel_category: "enlisted_army_personnel",
      commissioned_officer: false,
      research_status: "occupation_only_found",
      immediate_pre_oss_affiliations: [],
      last_civilian_pre_service: [],
    });
    expect(person.other_pre_oss_affiliations).toContainEqual(
      expect.objectContaining({
        organization_id: null,
        occupation,
        end_date: endDate,
        temporal_basis: "temporal_relation_uncertain",
        claim_confidence: "medium",
      }),
    );
    await page.goto("./people/" + id + "/");
    await expect(page.getByRole("heading", { name, exact: true })).toBeVisible();
    await expect(page.locator("main")).toContainText(occupation);
    await expect(page.locator("main")).toContainText("No reliable pre-OSS employer has yet been identified");
  }
});

test("Batch 473 qualifies Cornut and Corriera identity evidence without employer claims", async ({ page }) => {
  const andre = profile("846a5268-845f-57c7-b6a8-163e9246b300");
  expect(andre).toMatchObject({
    identity_status: "high_confidence",
    personnel_category: "foreign_or_allied_military_personnel",
    commissioned_officer: true,
    allied_or_foreign_personnel: true,
    research_status: "requires_archival_review",
    immediate_pre_oss_affiliations: [],
    last_civilian_pre_service: [],
    other_pre_oss_affiliations: [],
  });
  expect(andre.name_variants).toContain("Guermantes");

  const john = profile("bbbc2fac-83f2-5f77-8aac-65bf979c87c6");
  expect(john).toMatchObject({
    identity_status: "high_confidence",
    personnel_category: "enlisted_army_personnel",
    commissioned_officer: false,
    research_status: "requires_archival_review",
    manual_review_required: true,
    immediate_pre_oss_affiliations: [],
    last_civilian_pre_service: [],
    other_pre_oss_affiliations: [],
  });

  await page.goto("./people/846a5268-845f-57c7-b6a8-163e9246b300/");
  await expect(page.locator("main")).toContainText("Guermantes");
  await page.goto("./people/bbbc2fac-83f2-5f77-8aac-65bf979c87c6/");
  await expect(page.locator("main")).toContainText("leading zero");
  await expect(page.locator("main")).not.toContainText("occupation code 373");
});

test("Batch 473 withholds unbridged candidate facts", () => {
  const unresolved = [
    "21ca6b99-0cf9-5fc4-926d-02463a24b05f",
    "89491a94-b0da-5edf-bcd6-76316e01f4c1",
    "717ce632-7dd4-5519-99f1-f138e180c085",
    "fa649630-9bf9-5c87-acdf-bb5e3a5b77ae",
    "c4c8394a-c3c6-52f9-9cce-eed2d158edb1",
  ];
  for (const id of unresolved) {
    expect(profile(id)).toMatchObject({
      identity_status: "unresolved",
      research_status: "requires_archival_review",
      manual_review_required: true,
      other_pre_oss_affiliations: [],
      claims: [],
    });
  }
  expect(profile("66969e0a-fbe9-5585-b23e-a42d32a0e659")).toMatchObject({
    identity_status: "ambiguous",
    research_status: "requires_archival_review",
    other_pre_oss_affiliations: [],
    claims: [],
  });
});
