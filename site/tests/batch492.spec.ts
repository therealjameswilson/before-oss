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
  ["6e2f2941-0dad-5363-91ad-5afd66b3f4d7", "Hilary Crawford", "4bbd96c2-4d10-5f23-bd1b-9a22dfd0edf5", 97, "152", true],
  ["a1f07e88-1d63-580c-8aa6-09290f707b6e", "Jack B Crawford", "ab6d1364-4d19-50f7-901e-6711323bf160", 97, "152", true],
  ["b6df8604-a52b-58ad-94f6-3c02b57615bb", "John E Crawford Jr.", "332bda4f-f4b4-5fc1-9f58-65e902ea483a", 97, "152", true],
  ["7963d00d-25f1-581e-bf60-5de659d93ba0", "Ruth E Crawford", "797ee5d7-fb33-5313-a2bc-3ba9a63efc72", 97, "152", false],
  ["3c9f0d39-40c8-5c50-a09b-6fa35743b539", "Samuel J Crawford", "07fb6ca2-024b-578b-8e10-eb19b6c7d906", 97, "152", true],
  ["e4ab74b0-c118-5a2d-93cb-5b26ea19eedb", "William E Crawford", "a6275ab6-c98a-55e6-a5d4-9f25d282c238", 97, "152", true],
  ["71b3c835-7d1e-563d-8207-5000e34842f5", "William S Crawford Jr.", "b4a231d8-4ade-5e88-a7d2-ed11dc09f3cc", 97, "152", false],
  ["54b07c9d-fbcc-5d67-b7c5-abf51761e15d", "Alton O Crawley", "52dcd087-4e1f-5221-9cfc-9429c9859430", 97, "152", true],
  ["d7e21c57-6d30-588a-9e45-22483a598526", "Carlotta B Crawley", "96411817-f74f-5a97-b8ed-7b90e421fed3", 97, "153", false],
  ["2027bd17-62fb-51a8-90ee-785b6c079cae", "James W Crayhon", "3de0661a-fef9-510c-a989-5cb6fc13bf4d", 98, "153", false],
] as const;

test("Batch 492 preserves all ten source rows across pages 97 and 98 and masks printed identifiers", () => {
  for (const [id, name, sourceRecordId, pdfPage, box, hasPrivateIdentifier] of cohort) {
    const person = profile(id);
    expect(person).toMatchObject({ display_name: name });
    const sourceRecord = person.source_records.find(
      (record: { source_record_id: string }) => record.source_record_id === sourceRecordId,
    );
    expect(sourceRecord).toMatchObject({
      box,
      archive_location: "230/86/29/03",
      pdf_page: pdfPage,
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

test("Batch 492 publishes three qualified identifier-supported occupations", () => {
  const expected = [
    ["a1f07e88-1d63-580c-8aa6-09290f707b6e", "Tool sharpeners and dressers", "1943-07-26"],
    ["b6df8604-a52b-58ad-94f6-3c02b57615bb", "Clerks, general office", "1942-07-22"],
    ["3c9f0d39-40c8-5c50-a09b-6fa35743b539", "Carpenters", "1942-07-15"],
  ] as const;

  for (const [id, occupation, endDate] of expected) {
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
        occupation,
        end_date: endDate,
        relationship_type: "unknown",
        temporal_basis: "strongly_date_bounded",
        claim_confidence: "medium",
      }),
    );
  }
});

test("Batch 492 does not project William E Crawford's post-OSS Army record backward", () => {
  const person = profile("e4ab74b0-c118-5a2d-93cb-5b26ea19eedb");
  expect(person).toMatchObject({
    identity_status: "confirmed",
    personnel_category: "unknown_or_indeterminate",
    commissioned_officer: null,
    research_status: "needs_temporal_review",
    immediate_pre_oss_affiliations: [],
    last_civilian_pre_service: [],
    other_pre_oss_affiliations: [],
  });
  expect(person.claims).toContainEqual(
    expect.objectContaining({
      claim_type: "identity",
      claim_confidence: "confirmed",
      temporal_assessment: expect.stringContaining("post-OSS Army-entry date"),
      match_notes: expect.stringContaining("deliberately withheld"),
    }),
  );
});

test("Batch 492 qualifies the probable Crayhon Associated Press role", () => {
  const person = profile("2027bd17-62fb-51a8-90ee-785b6c079cae");
  expect(person).toMatchObject({
    identity_status: "probable",
    personnel_category: "unknown_or_indeterminate",
    commissioned_officer: null,
    research_status: "documented_prewar_employer_found",
    immediate_pre_oss_affiliations: [],
    last_civilian_pre_service: [],
  });
  expect(person.other_pre_oss_affiliations).toContainEqual(
    expect.objectContaining({
      canonical_organization: "Associated Press",
      role_title: "Photo city assignment editor",
      relationship_type: "employment",
      temporal_basis: "documented_prewar",
      identity_confidence: "probable",
      claim_confidence: "medium",
      publication_status: "publish_qualified",
    }),
  );
  expect(person.claims).toContainEqual(
    expect.objectContaining({
      claim_type: "other_pre_oss_affiliation",
      claim_confidence: "medium",
      match_notes: expect.stringContaining("excluded from default employer analytics"),
    }),
  );
});

test("Batch 492 preserves unresolved and ambiguous short-identifier cases", () => {
  for (const id of [
    "7963d00d-25f1-581e-bf60-5de659d93ba0",
    "d7e21c57-6d30-588a-9e45-22483a598526",
  ]) {
    expect(profile(id)).toMatchObject({
      identity_status: "unresolved",
      personnel_category: "unknown_or_indeterminate",
      commissioned_officer: null,
      research_status: "requires_archival_review",
      immediate_pre_oss_affiliations: [],
      last_civilian_pre_service: [],
      other_pre_oss_affiliations: [],
      claims: [],
    });
  }
  for (const id of [
    "6e2f2941-0dad-5363-91ad-5afd66b3f4d7",
    "71b3c835-7d1e-563d-8207-5000e34842f5",
    "54b07c9d-fbcc-5d67-b7c5-abf51761e15d",
  ]) {
    expect(profile(id)).toMatchObject({
      identity_status: "ambiguous",
      personnel_category: "unknown_or_indeterminate",
      commissioned_officer: null,
      research_status: "needs_identity_review",
      immediate_pre_oss_affiliations: [],
      last_civilian_pre_service: [],
      other_pre_oss_affiliations: [],
      claims: [],
    });
  }
});

test("Batch 492 direct routes expose qualifications, citations, and archival guidance", async ({ page }) => {
  expect(stats.research_attempted_people).toBeGreaterThanOrEqual(4688);
  expect(stats.verified_affiliation_people).toBeGreaterThanOrEqual(534);
  expect(stats.verified_employer_people).toBeGreaterThanOrEqual(237);
  expect(stats.archival_review_assessed_people).toBeGreaterThanOrEqual(4643);

  await page.goto("./people/a1f07e88-1d63-580c-8aa6-09290f707b6e/");
  await expect(page.getByRole("heading", { name: "Jack B Crawford", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("Tool sharpeners and dressers");
  await expect(page.locator("main")).toContainText("no employer is named");

  await page.goto("./people/e4ab74b0-c118-5a2d-93cb-5b26ea19eedb/");
  await expect(page.getByRole("heading", { name: "William E Crawford", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("after OSS dissolution");
  await expect(page.locator("main")).toContainText("do not project the post-OSS Army occupation backward");

  await page.goto("./people/2027bd17-62fb-51a8-90ee-785b6c079cae/");
  await expect(page.getByRole("heading", { name: "James W Crayhon", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("Associated Press");
  await expect(page.locator("main")).toContainText("Photo city assignment editor");
  await expect(page.locator("main")).toContainText("Probable");
  await expect(page.locator("main")).toContainText("not shown to be the immediate pre-OSS affiliation");

  await page.goto("./people/6e2f2941-0dad-5363-91ad-5afd66b3f4d7/");
  await expect(page.getByRole("heading", { name: "Hilary Crawford", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("literal identifier");
  await expect(page.locator("main")).toContainText("No reliable pre-OSS employer has yet been identified");
});
