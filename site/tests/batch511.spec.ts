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
  ["634b1256-6156-5c31-9763-ffb67d9584f2", "Richard Currier", "fe560492-ebde-5b85-a817-657cbb88add0", 101, false],
  ["ccf0b958-6266-5c86-9e0b-928318610e0a", "William B Curry", "a865fe9e-37c8-59e8-b75c-5eda12c5e55e", 101, true],
  ["f72df5d4-aa75-5032-ac4f-db9328f34c76", "Anne Curtis", "c7939adf-cfdc-5a2f-8fc2-2d328ed4b2d7", 101, false],
  ["3628c760-0d99-5d5d-bfb2-06f40ce3927f", "Charles C Curtis", "184b5dbe-4410-51a9-bde8-ecebb47d4abb", 102, false],
  ["ca2cb0ce-f476-5d6a-9751-244fc2b6ab23", "Earle J Curtis", "83ff08a7-7c8e-51ba-a7fe-efe197abe8b4", 102, true],
  ["f4790153-aba0-5d42-9ad8-c838961f9391", "Eleanor R Curtis", "d04b9b57-3ce8-5c62-bfa4-34a0be338d06", 102, true],
  ["9eff3d20-51d4-5247-996e-cf56690ca4a9", "Floyd J Curtis", "47aa9554-064c-584d-aa83-9ec860cb16b2", 102, true],
  ["baffad97-4ee9-5934-ad3f-1f8c22a6979c", "Helen D Curtis", "7c1e4068-4da2-5247-b7fe-a9d9e3722d15", 102, false],
  ["60c3fdb9-7015-5928-890a-e220539789ff", "Horace M Curtis", "cea2f126-87aa-5181-80ce-baf2dff49c7e", 102, true],
  ["999b2bba-c94b-51a2-88d3-2583e1b6f9d1", "John N Curtis", "510930fe-c018-5e06-9e48-a0e2db7483b0", 102, false],
] as const;

test("Batch 511 preserves the two-page cohort and masks every private field", () => {
  for (const [id, name, sourceRecordId, pdfPage, hasPrivateIdentifier] of cohort) {
    const person = profile(id);
    expect(person).toMatchObject({ display_name: name });
    const sourceRecord = person.source_records.find(
      (record: { source_record_id: string }) => record.source_record_id === sourceRecordId,
    );
    expect(sourceRecord).toMatchObject({
      box: "160",
      archive_location: "230/86/29/04",
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
  expect(profile("60c3fdb9-7015-5928-890a-e220539789ff").source_records[0].rank_as_indexed).toBe("T/Sgt");
});

test("Batch 511 publishes three qualified occupations without inventing employers", () => {
  for (const [id, occupation, endDate] of [
    ["ca2cb0ce-f476-5d6a-9751-244fc2b6ab23", "General farmer", "1942-07-09"],
    ["9eff3d20-51d4-5247-996e-cf56690ca4a9", "Policemen and detectives, public service", "1945-02-13"],
    ["60c3fdb9-7015-5928-890a-e220539789ff", "Draftsman", "1942-09-16"],
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

test("Batch 511 keeps unsupported identities and value 999 unresolved", () => {
  for (const id of [
    "634b1256-6156-5c31-9763-ffb67d9584f2",
    "f72df5d4-aa75-5032-ac4f-db9328f34c76",
    "f4790153-aba0-5d42-9ad8-c838961f9391",
    "baffad97-4ee9-5934-ad3f-1f8c22a6979c",
    "999b2bba-c94b-51a2-88d3-2583e1b6f9d1",
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
  const william = profile("ccf0b958-6266-5c86-9e0b-928318610e0a");
  expect(william).toMatchObject({
    identity_status: "confirmed",
    personnel_category: "enlisted_army_personnel",
    commissioned_officer: false,
    research_status: "requires_archival_review",
    immediate_pre_oss_affiliations: [],
    last_civilian_pre_service: [],
    other_pre_oss_affiliations: [],
  });
  expect(JSON.stringify(william)).not.toContain('"occupation":"999"');
});

test("Batch 511 retains the Charles Curtis lead without publishing it as fact", () => {
  const charles = profile("3628c760-0d99-5d5d-bfb2-06f40ce3927f");
  expect(charles).toMatchObject({
    identity_status: "unresolved",
    personnel_category: "unknown_or_indeterminate",
    commissioned_officer: null,
    research_status: "needs_identity_review",
    immediate_pre_oss_affiliations: [],
    last_civilian_pre_service: [],
    other_pre_oss_affiliations: [],
    claims: [],
  });
  expect(charles.identity_evidence).toContain("213th Coast Artillery");
  expect(charles.next_action).toContain("plausible");
});

test("Batch 511 coverage and direct routes expose the supported findings and qualifications", async ({ page }) => {
  expect(stats.research_attempted_people).toBe(4878);
  expect(stats.verified_affiliation_people).toBe(554);
  expect(stats.verified_employer_people).toBe(246);
  expect(stats.archival_review_assessed_people).toBe(4833);

  await page.goto("./people/ca2cb0ce-f476-5d6a-9751-244fc2b6ab23/");
  await expect(page.getByRole("heading", { name: "Earle J Curtis", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("General farmer");

  await page.goto("./people/9eff3d20-51d4-5247-996e-cf56690ca4a9/");
  await expect(page.getByRole("heading", { name: "Floyd J Curtis", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("Policemen and detectives, public service");

  await page.goto("./people/60c3fdb9-7015-5928-890a-e220539789ff/");
  await expect(page.getByRole("heading", { name: "Horace M Curtis", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("Draftsman");

  await page.goto("./people/3628c760-0d99-5d5d-bfb2-06f40ce3927f/");
  await expect(page.getByRole("heading", { name: "Charles C Curtis", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("plausible 213th Coast Artillery colonel");
  await expect(page.locator("main")).toContainText("needs identity review");
});
