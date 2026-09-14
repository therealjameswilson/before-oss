import { expect, test } from "@playwright/test";
import fs from "node:fs";

const people = JSON.parse(
  fs.readFileSync(new URL("../src/data/generated/people.json", import.meta.url), "utf8"),
);
const profile = (id: string) =>
  people.find((person: { person_id: string }) => person.person_id === id);

test("Batch 450 publishes Compton's 1917 cavalry appointment without calling it immediate", async ({ page }) => {
  const coalter = profile("20fcb61a-c46e-5f5c-a247-393d08102433");
  expect(coalter).toMatchObject({
    display_name: "Coalter B Compton",
    identity_status: "high_confidence",
    personnel_category: "commissioned_army_officer",
    commissioned_officer: true,
    research_status: "requires_archival_review",
  });
  expect(coalter.name_variants).toContain("Coalter Bates Compton");
  expect(coalter.immediate_pre_oss_affiliations).toEqual([]);
  expect(coalter.last_civilian_pre_service).toEqual([]);
  expect(coalter.other_pre_oss_affiliations).toContainEqual(
    expect.objectContaining({
      canonical_organization: "Cavalry Arm, U.S. Army",
      organization_name_as_found: "Cavalry Arm",
      role_title: "Second lieutenant",
      relationship_type: "military_assignment",
      start_date: "1917-04-20",
      immediate_pre_oss: false,
      last_civilian_pre_service: false,
      temporal_basis: "documented_prewar",
      identity_confidence: "high_confidence",
      claim_confidence: "high",
    }),
  );

  await page.goto(`./people/${coalter.person_id}/`);
  await expect(page.getByRole("heading", { name: "Coalter B Compton", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("Coalter Bates Compton");
  await expect(page.locator("main")).toContainText("Cavalry Arm");
  await expect(page.locator("main")).toContainText("20 April 1917");
  await expect(page.locator("main")).toContainText("Earlier pre-OSS affiliations");
  await expect(page.locator("main")).toContainText(
    "Immediate pre-OSS affiliationNo reviewed claim currently meets the publication threshold",
  );
  await expect(page.locator("main")).toContainText("Review Box 137");
});

test("Batch 450 qualifies Conard's last civilian employer and separates his occupation", async ({ page }) => {
  const alfred = profile("42664cee-1c0b-5ee3-9558-53813090de94");
  expect(alfred).toMatchObject({
    display_name: "Alfred F Conard",
    identity_status: "high_confidence",
    personnel_category: "enlisted_army_personnel",
    commissioned_officer: false,
    research_status: "documented_prewar_employer_found",
  });
  expect(alfred.name_variants).toContain("Alfred Fletcher Conard");
  expect(alfred.immediate_pre_oss_affiliations).toEqual([]);
  expect(alfred.last_civilian_pre_service).toContainEqual(
    expect.objectContaining({
      canonical_organization: "University of Kansas City School of Law",
      organization_name_as_found: "University of Kansas City School of Law",
      role_title: "Assistant Professor of Law",
      relationship_type: "employment",
      start_date: "1940",
      end_date: "1942",
      immediate_pre_oss: false,
      last_civilian_pre_service: true,
      temporal_basis: "probable_immediate",
      identity_confidence: "high_confidence",
      claim_confidence: "medium",
    }),
  );
  expect(alfred.other_pre_oss_affiliations).toContainEqual(
    expect.objectContaining({
      organization_id: null,
      occupation: "Lawyers and judges",
      relationship_type: "unknown",
      end_date: "1943-09-24",
      temporal_basis: "strongly_date_bounded",
      identity_confidence: "high_confidence",
      claim_confidence: "medium",
    }),
  );

  await page.goto(`./people/${alfred.person_id}/`);
  await expect(page.getByRole("heading", { name: "Alfred F Conard", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("University of Kansas City School of Law");
  await expect(page.locator("main")).toContainText("Assistant Professor of Law");
  await expect(page.locator("main")).toContainText("Lawyers and judges");
  await expect(page.locator("main")).toContainText("exclude an intervening civilian role");
  await expect(page.locator("main")).toContainText(
    "no private index identifier provides direct confirmation",
  );
});

test("Batch 450 preserves all ten printed rows and masks the two private identifier forms", async () => {
  const expected = [
    ["b60ca522-2780-5a20-8215-f4f6b23f8922", "Simone J Companardi", "ba469eff-1e63-5471-aa2d-8de608d80cd5", false],
    ["138fe9a4-1a24-5daa-bd4a-528c96c6d51e", "Charles R Compton", "dd1d5154-a5d7-5609-b5d9-f0e336b21a0e", true],
    ["20fcb61a-c46e-5f5c-a247-393d08102433", "Coalter B Compton", "d02f6ad1-ad81-517b-915f-5780fe6c3c70", false],
    ["9ac830f7-3386-577a-afb5-e04e8aa95f53", "James M Compton", "792a69c9-256d-5a1e-a430-921c0f1b3fe5", true],
    ["ee333cb9-2716-596d-a176-aa7dc442b033", "James R Compton", "0b8e93a1-bcf8-5cb4-a0cb-71c5daf290a9", false],
    ["e5599284-fe56-5481-8fda-ae595928779d", "William D Compton", "b48e566b-e71d-5b86-93d6-87350a29bb4b", false],
    ["f6b407a0-5388-5863-a826-058e09ea27c8", "Isabel L Comstedt", "d9aaeea4-f3c8-538a-aa18-b6ccd9d3d965", false],
    ["fa7e02e4-0f92-546c-b426-4856b7c32903", "Anne E Comstock", "07b17384-7ebe-5a0b-8b41-2cff9385e205", false],
    ["3ff7f332-7d6e-5f79-9a55-ed0f6ec846fe", "Dorothy D Comstock", "1d05815f-e8c9-5636-90fc-60e1201fd85a", false],
    ["42664cee-1c0b-5ee3-9558-53813090de94", "Alfred F Conard", "bca7f1c8-e5a6-5303-8e57-a05d30112b03", false],
  ];

  for (const [id, name, sourceRecordId, hasSerial] of expected) {
    const person = profile(String(id));
    expect(person).toMatchObject({ display_name: name });
    expect(person.source_records[0]).toMatchObject({
      source_record_id: sourceRecordId,
      box: "137",
      notes_as_indexed: null,
      archive_location: "230/86/29/01",
      pdf_page: 88,
    });
    if (hasSerial) {
      expect(person.source_records[0].serial_masked).toMatch(/^••••.{4}$/u);
    } else {
      expect(person.source_records[0].serial_masked).toBeNull();
    }
    expect(JSON.stringify(person)).not.toMatch(
      /"serial_number"|"serial_number_raw"|"serial_number_normalized"/,
    );
  }
});

test("Batch 450 keeps eight unresolved profiles empty of unsupported affiliations", async ({ page }) => {
  const unresolved = [
    ["b60ca522-2780-5a20-8215-f4f6b23f8922", "Simone J Companardi", "requires_archival_review"],
    ["138fe9a4-1a24-5daa-bd4a-528c96c6d51e", "Charles R Compton", "needs_identity_review"],
    ["9ac830f7-3386-577a-afb5-e04e8aa95f53", "James M Compton", "needs_identity_review"],
    ["ee333cb9-2716-596d-a176-aa7dc442b033", "James R Compton", "requires_archival_review"],
    ["e5599284-fe56-5481-8fda-ae595928779d", "William D Compton", "requires_archival_review"],
    ["f6b407a0-5388-5863-a826-058e09ea27c8", "Isabel L Comstedt", "requires_archival_review"],
    ["fa7e02e4-0f92-546c-b426-4856b7c32903", "Anne E Comstock", "requires_archival_review"],
    ["3ff7f332-7d6e-5f79-9a55-ed0f6ec846fe", "Dorothy D Comstock", "requires_archival_review"],
  ];

  for (const [id, name, status] of unresolved) {
    const person = profile(id);
    expect(person).toMatchObject({
      display_name: name,
      identity_status: "unresolved",
      personnel_category: "unknown_or_indeterminate",
      commissioned_officer: null,
      research_status: status,
    });
    expect(person.claims).toEqual([]);
    expect(person.immediate_pre_oss_affiliations).toEqual([]);
    expect(person.last_civilian_pre_service).toEqual([]);
    expect(person.other_pre_oss_affiliations).toEqual([]);
  }

  const charles = profile("138fe9a4-1a24-5daa-bd4a-528c96c6d51e");
  await page.goto(`./people/${charles.person_id}/`);
  await expect(page.getByRole("heading", { name: "Charles R Compton", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("six-digit private identifier");
  await expect(page.locator("main")).toContainText("not padded or silently repaired");
  await expect(page.locator("main")).toContainText("Review Box 137");
  await expect(page.locator("main")).toContainText(
    "Last civilian employer before serviceNo reviewed claim currently meets the publication threshold",
  );
});
