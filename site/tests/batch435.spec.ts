import { expect, test } from "@playwright/test";
import fs from "node:fs";

const people = JSON.parse(
  fs.readFileSync(new URL("../src/data/generated/people.json", import.meta.url), "utf8"),
);
const profile = (id: string) =>
  people.find((person: { person_id: string }) => person.person_id === id);

test("Batch 435 publishes Donald Cobleigh's Dartmouth employment without inventing an immediate OSS predecessor", async ({ page }) => {
  const donald = profile("4fe6b48a-fb59-5e5e-95e6-4a89c825e097");
  expect(donald).toMatchObject({
    display_name: "Donald E Cobleigh",
    identity_status: "high_confidence",
    personnel_category: "enlisted_marine_corps_personnel",
    commissioned_officer: false,
    research_status: "verified_employer_found",
  });
  expect(donald.immediate_pre_oss_affiliations).toEqual([]);
  expect(donald.last_civilian_pre_service).toContainEqual(
    expect.objectContaining({
      canonical_organization: "Dartmouth College",
      role_title: "music faculty member; assistant professor of music; Glee Club director",
      relationship_type: "employment",
      start_date: "1925",
      end_date: "1943",
      temporal_basis: "strongly_date_bounded",
      claim_confidence: "high",
    }),
  );

  await page.goto(`./people/${donald.person_id}/`);
  await expect(page.getByRole("heading", { name: "Donald E Cobleigh", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("Dartmouth College");
  await expect(page.locator("main")).toContainText("last documented civilian employer");
  await expect(page.locator("main")).toContainText("Marine Corps");
});

test("Batch 435 publishes Angelo Coccoli's Army occupation without inventing a workplace or employer", async ({ page }) => {
  const angelo = profile("65a0af85-d8fe-5cf7-a653-95d824e1b3c6");
  expect(angelo).toMatchObject({
    display_name: "Angelo Coccoli",
    identity_status: "confirmed",
    personnel_category: "enlisted_army_personnel",
    commissioned_officer: false,
    research_status: "occupation_only_found",
  });
  expect(angelo.immediate_pre_oss_affiliations).toEqual([]);
  expect(angelo.last_civilian_pre_service).toEqual([]);
  expect(angelo.other_pre_oss_affiliations).toContainEqual(
    expect.objectContaining({
      organization_id: null,
      occupation: "Packing, filling, labeling, marking, bottling, and related occupation, not elsewhere classified",
      relationship_type: "unknown",
      end_date: "1942-07-06",
      temporal_basis: "temporal_relation_uncertain",
      claim_confidence: "medium",
    }),
  );

  await page.goto(`./people/${angelo.person_id}/`);
  await expect(page.getByRole("heading", { name: "Angelo Coccoli", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("Packing, filling, labeling, marking, bottling");
  await expect(page.locator("main")).toContainText("no employer is identified");
  await expect(page.locator("main")).toContainText("No reliable pre-OSS employer has yet been identified");
});

test("Batch 435 preserves the rejected John Cochran candidate and Major Cochran's indexed first name", async ({ page }) => {
  const john = profile("ab8bc172-1b16-5d39-83eb-c14640bb53c0");
  expect(john).toMatchObject({
    display_name: "John M Cochran",
    identity_status: "unresolved",
    personnel_category: "unknown_or_indeterminate",
    commissioned_officer: null,
    research_status: "requires_archival_review",
  });
  expect(john.immediate_pre_oss_affiliations).toEqual([]);
  expect(john.last_civilian_pre_service).toEqual([]);
  expect(john.other_pre_oss_affiliations).toEqual([]);

  await page.goto(`./people/${john.person_id}/`);
  await expect(page.getByRole("heading", { name: "John M Cochran", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("one exact-name John M Cochran row");
  await expect(page.locator("main")).toContainText("name-only Army candidate");

  const major = profile("fa901b65-ab3f-5c27-b3dd-30bd12dbd7eb");
  expect(major).toMatchObject({
    display_name: "Major B Cochran",
    identity_status: "unresolved",
    commissioned_officer: null,
    research_status: "requires_archival_review",
  });

  await page.goto(`./people/${major.person_id}/`);
  await expect(page.getByRole("heading", { name: "Major B Cochran", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("Major is preserved as the printed first name");
  await expect(page.locator("main")).toContainText("not treated as a military grade");
});

test("Batch 435 preserves every source row and masks all private identifiers", async () => {
  const expected = [
    ["4fe6b48a-fb59-5e5e-95e6-4a89c825e097", "Donald E Cobleigh", "fe68b4f6-100e-56e6-abb7-cc5ec4bff176", "Sgt", true],
    ["325dbf24-89dc-541b-8573-5dad97be5a98", "Gwynne W Coburn", "7518a051-6bd4-5a28-9eeb-56e036dc4a10", null, true],
    ["3231b5e3-b52f-52c1-a17c-c1b349956922", "Sarah E Coburn", "3796ae21-fa73-544b-a83c-dadfaf63a237", null, false],
    ["65a0af85-d8fe-5cf7-a653-95d824e1b3c6", "Angelo Coccoli", "02ee8aa1-6167-5685-a3f7-9899de976d46", null, true],
    ["e04c533f-cc4b-56cc-bf70-fbb57e79aa3d", "Elizabeth Cochran", "b27eaac5-12e9-5e2e-8f25-75ef2c48de08", null, false],
    ["364f904b-9bfb-5f79-9178-5e6618fe1ee1", "Jefferson Cochran", "6991d94d-4d7c-59da-ac5e-07ced83cf643", null, false],
    ["ab8bc172-1b16-5d39-83eb-c14640bb53c0", "John M Cochran", "7bd5132f-70e0-54e8-8637-060d0ff0d9da", null, false],
    ["fa901b65-ab3f-5c27-b3dd-30bd12dbd7eb", "Major B Cochran", "35444aed-e85b-5389-8966-9f37ddc6310d", null, true],
    ["7bca18ce-25ba-5cba-981a-23829aaa989f", "Barbara L Cochrane", "dcb19194-31eb-5855-94b6-5500d4a3bf8c", null, false],
    ["ca57a781-8775-5946-bb69-22c563a7744a", "Lyle N Cockerille", "08104c03-cecc-59aa-b764-cd41b4989bf7", null, true],
  ];

  for (const [id, name, sourceRecordId, rank, hasSerial] of expected) {
    const person = profile(String(id));
    expect(person).toMatchObject({ display_name: name });
    expect(person.source_records[0]).toMatchObject({
      source_record_id: sourceRecordId,
      pdf_page: 85,
      box: "131",
      archive_location: "230/86/28/07",
      rank_as_indexed: rank,
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
