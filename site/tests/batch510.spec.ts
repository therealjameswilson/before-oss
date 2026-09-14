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
  ["dc313941-998d-5374-a44d-fbeee19d0c30", "Mary T Curio", "cd041525-ad10-5e23-8ea5-e8c2825de3e5", false],
  ["14be82c7-e568-5a66-85bb-5a50f8381e33", "Anton Curl", "b863805f-d13c-5078-a39b-3048ccac7dbe", true],
  ["1b86a070-f3ca-53ae-a5a1-d0d48b7ea198", "Vincent L Curl", "59711689-c32c-5e0d-a0c3-9d7076e285c8", true],
  ["f69e5acd-de93-584c-9a1b-effa8ec8f841", "Michael J Curley", "17aca550-e5ee-5ea8-bc23-4aac0cb6beae", true],
  ["549b20e7-8d5d-557d-ab60-19a600754c0f", "Charley Curo", "3624c56a-be6f-5412-950e-74ffa4790282", true],
  ["6576bf37-173b-5b27-aa16-a3f00e77918a", "Elinor Curran", "20e9fc22-feb2-5aba-9504-d6c86d162a30", false],
  ["e8673f48-b0f1-5a8b-93c1-a026154cfb8a", "Phillip D Curran", "b6885927-623c-5899-9ffc-4e824da22b4e", false],
  ["f6646c9b-d11d-52e1-a8ce-55c4fa0d4f8a", "Robert R Curran", "4ee41666-fe6a-5d21-9007-f09bc1ee9fab", true],
  ["700555ed-5c90-5d2c-b7ca-5bf0b7bc16f4", "Louise P Currie", "ea900373-b0e6-5d1d-a7f8-b19e1de54166", true],
  ["46cfb425-ef2d-51c2-93f2-299f52c644de", "Teresita Currie", "f61eb153-d24b-543c-a181-bf5b62d02722", false],
] as const;

test("Batch 510 preserves the audited page 101 cohort and masks every private field", () => {
  for (const [id, name, sourceRecordId, hasPrivateIdentifier] of cohort) {
    const person = profile(id);
    expect(person).toMatchObject({ display_name: name });
    const sourceRecord = person.source_records.find(
      (record: { source_record_id: string }) => record.source_record_id === sourceRecordId,
    );
    expect(sourceRecord).toMatchObject({
      box: "160",
      archive_location: "230/86/29/04",
      pdf_page: 101,
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

test("Batch 510 publishes two qualified occupations without inventing employers", () => {
  for (const [id, occupation, endDate] of [
    ["14be82c7-e568-5a66-85bb-5a50f8381e33", "Electricians' apprentice", "1941-03-25"],
    ["f69e5acd-de93-584c-9a1b-effa8ec8f841", "Boilermaker", "1942-02-03"],
  ] as const) {
    const person = profile(id);
    expect(person).toMatchObject({
      identity_status: "confirmed",
      personnel_category: "enlisted_army_personnel",
      commissioned_officer: false,
      research_status: "occupation_only_found",
      immediate_pre_oss_affiliations: [],
      last_civilian_pre_service: [],
    });
    expect(person.other_pre_oss_affiliations).toHaveLength(1);
    expect(person.other_pre_oss_affiliations[0]).toMatchObject({
      occupation,
      relationship_type: "unknown",
      end_date: endDate,
      temporal_basis: "strongly_date_bounded",
      claim_confidence: "medium",
      publication_status: "publish_qualified",
      organization_id: null,
      canonical_organization: null,
      historical_organization: null,
      organization_name_as_found: null,
    });
  }
});

test("Batch 510 publishes Vincent Curl's immediate Army assignment, not a civilian employer", () => {
  const vincent = profile("1b86a070-f3ca-53ae-a5a1-d0d48b7ea198");
  expect(vincent).toMatchObject({
    identity_status: "high_confidence",
    personnel_category: "commissioned_army_officer",
    commissioned_officer: true,
    research_status: "requires_archival_review",
    last_civilian_pre_service: [],
    other_pre_oss_affiliations: [],
  });
  expect(vincent.immediate_pre_oss_affiliations).toHaveLength(1);
  expect(vincent.immediate_pre_oss_affiliations[0]).toMatchObject({
    canonical_organization: "United States Army, 35th Infantry Regiment",
    organization_name_as_found: "35th Regiment",
    relationship_type: "military_assignment",
    immediate_pre_oss: true,
    last_civilian_pre_service: false,
    temporal_basis: "explicit_immediate",
    claim_confidence: "high",
  });
});

test("Batch 510 leaves unsupported identities unresolved and value 999 uninterpreted", () => {
  for (const id of [
    "dc313941-998d-5374-a44d-fbeee19d0c30",
    "6576bf37-173b-5b27-aa16-a3f00e77918a",
    "e8673f48-b0f1-5a8b-93c1-a026154cfb8a",
    "f6646c9b-d11d-52e1-a8ce-55c4fa0d4f8a",
    "700555ed-5c90-5d2c-b7ca-5bf0b7bc16f4",
    "46cfb425-ef2d-51c2-93f2-299f52c644de",
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
  const charley = profile("549b20e7-8d5d-557d-ab60-19a600754c0f");
  expect(charley).toMatchObject({
    identity_status: "confirmed",
    personnel_category: "enlisted_army_personnel",
    commissioned_officer: false,
    research_status: "requires_archival_review",
    immediate_pre_oss_affiliations: [],
    last_civilian_pre_service: [],
    other_pre_oss_affiliations: [],
  });
  expect(JSON.stringify(charley)).not.toContain('"occupation":"999"');
});

test("Batch 510 coverage and direct routes expose the supported findings and qualifications", async ({ page }) => {
  expect(stats.research_attempted_people).toBe(4868);
  expect(stats.verified_affiliation_people).toBe(554);
  expect(stats.verified_employer_people).toBe(246);
  expect(stats.archival_review_assessed_people).toBe(4823);

  await page.goto("./people/14be82c7-e568-5a66-85bb-5a50f8381e33/");
  await expect(page.getByRole("heading", { name: "Anton Curl", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("Electricians' apprentice");
  await expect(page.locator("main")).not.toContainText("Apprenticeship employer:");

  await page.goto("./people/f69e5acd-de93-584c-9a1b-effa8ec8f841/");
  await expect(page.getByRole("heading", { name: "Michael J Curley", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("Boilermaker");
  await expect(page.locator("main")).not.toContainText("Archbishop");

  await page.goto("./people/1b86a070-f3ca-53ae-a5a1-d0d48b7ea198/");
  await expect(page.getByRole("heading", { name: "Vincent L Curl", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("United States Army, 35th Infantry Regiment");
  await expect(page.locator("main")).toContainText("military assignment");
  await expect(page.locator("main")).toContainText("explicit immediate");
  await expect(page.locator("main")).toContainText("commissioned army officer");
});
