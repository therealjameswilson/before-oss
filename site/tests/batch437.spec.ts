import { expect, test } from "@playwright/test";
import fs from "node:fs";

const people = JSON.parse(
  fs.readFileSync(new URL("../src/data/generated/people.json", import.meta.url), "utf8"),
);
const profile = (id: string) =>
  people.find((person: { person_id: string }) => person.person_id === id);

test("Batch 437 keeps Army occupations separate from employers", async ({ page }) => {
  const expected = [
    ["de2b5e47-ce8d-5802-9f14-a779c2628ca1", "Robert W Coe", "Accountants and auditors", "1942-02-20"],
    ["05cc0f23-fee1-5294-8b81-f3eb675f51f8", "Henry G Coffee", "Farm hands, general farms", "1942-11-04"],
  ];

  for (const [id, name, occupation, endDate] of expected) {
    const person = profile(id);
    expect(person).toMatchObject({
      display_name: name,
      identity_status: "confirmed",
      personnel_category: "enlisted_army_personnel",
      commissioned_officer: false,
      research_status: "occupation_only_found",
    });
    expect(person.immediate_pre_oss_affiliations).toEqual([]);
    expect(person.last_civilian_pre_service).toEqual([]);
    expect(person.other_pre_oss_affiliations).toContainEqual(
      expect.objectContaining({
        organization_id: null,
        occupation,
        relationship_type: "unknown",
        end_date: endDate,
        temporal_basis: "temporal_relation_uncertain",
        claim_confidence: "medium",
      }),
    );
  }

  const robert = profile("de2b5e47-ce8d-5802-9f14-a779c2628ca1");
  await page.goto(`./people/${robert.person_id}/`);
  await expect(page.getByRole("heading", { name: "Robert W Coe", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("Accountants and auditors");
  await expect(page.locator("main")).toContainText("no employer is identified");
  await expect(page.locator("main")).toContainText("No reliable pre-OSS employer has yet been identified");
});

test("Batch 437 qualifies Frederic Coenen's last civilian employer without calling it immediate", async ({ page }) => {
  const frederic = profile("e92d5f6e-18aa-55b7-9334-eb83986b097c");
  expect(frederic).toMatchObject({
    display_name: "Frederic E Coenen",
    identity_status: "high_confidence",
    personnel_category: "civilian_professional_or_administrative_grade",
    commissioned_officer: false,
    research_status: "documented_prewar_employer_found",
  });
  expect(frederic.immediate_pre_oss_affiliations).toEqual([]);
  expect(frederic.last_civilian_pre_service).toContainEqual(
    expect.objectContaining({
      canonical_organization: "University of North Carolina at Chapel Hill",
      organization_name_as_found: "University of North Carolina",
      role_title: "Assistant Professor of German and Adviser in the General College",
      relationship_type: "employment",
      start_date: "1944",
      end_date: "1945",
      temporal_basis: "probable_immediate",
      claim_confidence: "medium",
      publication_status: "publish_qualified",
    }),
  );

  await page.goto(`./people/${frederic.person_id}/`);
  await expect(page.getByRole("heading", { name: "Frederic E Coenen", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("University of North Carolina");
  await expect(page.locator("main")).toContainText("last civilian employer");
  await expect(page.locator("main")).toContainText("direct OSS transition is not proven");
});

test("Batch 437 publishes Robert Coffin's explicit Ohio State to OSS pathway", async ({ page }) => {
  const robert = profile("6c4cd3e0-9bb8-5467-9635-f149da3ec837");
  expect(robert).toMatchObject({
    display_name: "Robert M Coffin",
    identity_status: "high_confidence",
    personnel_category: "civilian_professional_or_administrative_grade",
    commissioned_officer: false,
    research_status: "verified_employer_found",
  });
  for (const affiliations of [
    robert.immediate_pre_oss_affiliations,
    robert.last_civilian_pre_service,
  ]) {
    expect(affiliations).toContainEqual(
      expect.objectContaining({
        canonical_organization: "The Ohio State University",
        organization_name_as_found: "Ohio State University",
        role_title: "member of the teaching staff",
        occupation: "professor",
        relationship_type: "employment",
        end_date: "1942-11",
        temporal_basis: "explicit_immediate",
        claim_confidence: "high",
        publication_status: "published",
      }),
    );
  }

  await page.goto(`./people/${robert.person_id}/`);
  await expect(page.getByRole("heading", { name: "Robert M Coffin", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("Ohio State University");
  await expect(page.locator("main")).toContainText("immediate pre-OSS affiliation");
  await expect(page.locator("main")).toContainText("Cartographic Division");
  await expect(page.locator("main")).toContainText("artist-designer");
});

test("Batch 437 preserves all ten rows, masks identifiers and withholds Cyril Coggins's weak lead", async ({ page }) => {
  const expected = [
    ["de2b5e47-ce8d-5802-9f14-a779c2628ca1", "Robert W Coe", "0d2edc52-e702-5ea3-8b56-25be702f844a", 85, true],
    ["3f85da20-e83b-5d7b-9ce6-4fec9d01d22a", "Catherine R Coenen", "417a6523-3454-52eb-a2fc-3ed2df31cd7d", 85, false],
    ["e92d5f6e-18aa-55b7-9334-eb83986b097c", "Frederic E Coenen", "6d426a81-8294-5e07-bcc6-8b9687b0bd2f", 85, false],
    ["05cc0f23-fee1-5294-8b81-f3eb675f51f8", "Henry G Coffee", "03b06538-205b-5c4e-a6e7-fcce6bc69235", 85, true],
    ["8a931413-6109-5bd4-ae0a-0adb18e651ed", "Charles M Coffey", "506f5eec-6ef6-5aab-aa25-b0153bd9b9b5", 85, false],
    ["a7dbb8ce-6b1d-5299-9ead-44679401b9ce", "John W Coffey", "ccd39fd8-286e-57ec-80df-a1a49cd3469d", 85, false],
    ["6c4cd3e0-9bb8-5467-9635-f149da3ec837", "Robert M Coffin", "eb018cef-8a83-56c1-8cbe-f8d9ee6e414d", 85, false],
    ["dc978e23-967b-53b6-9440-2f4c8a3faf22", "Humbert Cofrances", "52e13b8c-cced-59ce-8ab6-18702b914766", 86, false],
    ["c271b82c-b8e9-57b9-944b-fc056a561595", "Cyril M Coggins", "2d113a71-7409-5dfd-a9fc-bfac0f808256", 86, true],
    ["49ecd517-4045-5808-935b-5c361cd5f925", "Dorothy P Coggins", "d813d5ac-ccb5-5657-b8c4-2b1016267128", 86, false],
  ];

  for (const [id, name, sourceRecordId, pdfPage, hasSerial] of expected) {
    const person = profile(String(id));
    expect(person).toMatchObject({ display_name: name });
    expect(person.source_records[0]).toMatchObject({
      source_record_id: sourceRecordId,
      pdf_page: pdfPage,
      rank_as_indexed: null,
      box: "132",
      archive_location: "230/86/28/07",
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

  const cyril = profile("c271b82c-b8e9-57b9-944b-fc056a561595");
  expect(cyril).toMatchObject({
    display_name: "Cyril M Coggins",
    identity_status: "probable",
    research_status: "requires_archival_review",
  });
  expect(cyril.immediate_pre_oss_affiliations).toEqual([]);
  expect(cyril.last_civilian_pre_service).toEqual([]);
  expect(cyril.other_pre_oss_affiliations).toEqual([]);
  expect(cyril.claims).toEqual([]);

  await page.goto(`./people/${cyril.person_id}/`);
  await expect(page.getByRole("heading", { name: "Cyril M Coggins", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("different eight-digit exact-name Army row");
  await expect(page.locator("main")).toContainText("No reliable pre-OSS employer has yet been identified");
  await expect(page.locator("main")).not.toContainText("mortar-training mission");
});
