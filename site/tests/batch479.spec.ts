import { expect, test } from "@playwright/test";
import fs from "node:fs";

const people = JSON.parse(
  fs.readFileSync(new URL("../src/data/generated/people.json", import.meta.url), "utf8"),
);
const profile = (id: string) =>
  people.find((person: { person_id: string }) => person.person_id === id);

test("Batch 479 preserves pages 94-95 rows and masks private identifiers", () => {
  const expected = [
    ["3e6993ac-d49d-59d4-849e-9bdd6cebf337", "Mary P Couden", "5c341a1f-96de-52cf-8c7e-b55a57b61109", null, "147", "230/86/29/02", 94],
    ["1b3a302e-e10a-57e4-9143-e144f7919a82", "Louise P Coufos", "3a2ea308-9610-5d68-b1e7-30c82252999e", "••••3306", "147", "230/86/29/02", 95],
    ["3950d7cb-7507-50d0-ac89-2bf63e7e495c", "Eva A Coughlin", "8b497f3e-bc6c-536a-b4c3-1d8b2b5deea4", null, "147", "230/86/29/02", 95],
    ["8f649739-f4de-5151-8be5-68d38810f730", "Francis X Coughlin", "33f6fe62-d0f7-5add-a835-e98637641a28", "••••6090", "147", "230/86/29/02", 95],
    ["0d91343b-decd-5968-98d2-216581e607c7", "John G Coughlin", "384ea594-053c-5d46-a1c2-804324754caf", "••••8898", "147", "230/86/29/02", 95],
    ["ff3fdf0f-abdb-5be6-ac9b-11c8d353d671", "Richard J Coughlin", "35525a71-729b-5afe-9b9c-016cf407014d", "••••7722", "148", "230/86/29/03", 95],
    ["449b58fd-bdf4-5972-a7ca-461ae08c4ddb", "John L Coukos", "f4df24de-f94a-5e7c-a0ad-0ee21b4ffbf0", "••••8414", "148", "230/86/29/03", 95],
    ["561f2a6f-290c-5d27-9d44-69675b61875f", "William L Coulehan", "43b3008b-b03a-5e57-8a5a-c18e08699dcc", "••••7378", "148", "230/86/29/03", 95],
    ["26190080-de5a-5832-b39a-cebaab2f1e22", "Alfred J Coulombre", "0289d248-eaab-5328-977e-50b6e4319e79", "••••5747", "148", "230/86/29/03", 95],
    ["c2828388-db19-58d8-a471-301a9145e329", "Jacques Coulon", "e48f70d2-4d67-583c-930e-6dc8c12670b1", null, "148", "230/86/29/03", 95],
  ];

  for (const [id, name, sourceRecordId, serial, box, location, pdfPage] of expected) {
    const person = profile(String(id));
    expect(person).toMatchObject({ display_name: name });
    expect(person.source_records).toContainEqual(
      expect.objectContaining({
        source_record_id: sourceRecordId,
        serial_masked: serial,
        box,
        archive_location: location,
        pdf_page: pdfPage,
      }),
    );
    expect(JSON.stringify(person)).not.toMatch(
      /"serial_number"|"serial_number_raw"|"serial_number_normalized"/,
    );
  }
});

test("Batch 479 publishes John Coughlin's regiment as military, not civilian employment", async ({ page }) => {
  const person = profile("0d91343b-decd-5968-98d2-216581e607c7");
  expect(person).toMatchObject({
    display_name: "John G Coughlin",
    identity_status: "high_confidence",
    personnel_category: "commissioned_army_officer",
    commissioned_officer: true,
    research_status: "requires_archival_review",
    last_civilian_pre_service: [],
  });
  expect(person.immediate_pre_oss_affiliations).toContainEqual(
    expect.objectContaining({
      organization_name_as_found: "35th Regiment",
      canonical_organization: "United States Army, 35th Infantry Regiment",
      relationship_type: "military_assignment",
      temporal_basis: "explicit_immediate",
      claim_confidence: "high",
    }),
  );

  await page.goto("./people/0d91343b-decd-5968-98d2-216581e607c7/");
  await expect(page.getByRole("heading", { name: "John G Coughlin", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("35th Infantry Regiment");
  await expect(page.locator("main")).toContainText("OSS in Action: The Pacific and the Far East");
  await expect(page.locator("main")).toContainText("explicit immediate");
});

test("Batch 479 keeps William Coulehan's Army and Foreign Service pathways separate and qualified", async ({ page }) => {
  const person = profile("561f2a6f-290c-5d27-9d44-69675b61875f");
  expect(person).toMatchObject({
    display_name: "William L Coulehan",
    identity_status: "high_confidence",
    personnel_category: "commissioned_army_officer",
    commissioned_officer: true,
    research_status: "needs_temporal_review",
  });
  expect(person.immediate_pre_oss_affiliations).toContainEqual(
    expect.objectContaining({
      canonical_organization: "United States Army",
      relationship_type: "military_assignment",
      temporal_basis: "probable_immediate",
      claim_confidence: "medium",
    }),
  );
  expect(person.last_civilian_pre_service).toContainEqual(
    expect.objectContaining({
      organization_name_as_found: "Foreign Service",
      canonical_organization: "United States Department of State",
      relationship_type: "government_assignment",
      temporal_basis: "strongly_date_bounded",
      claim_confidence: "medium",
    }),
  );

  await page.goto("./people/561f2a6f-290c-5d27-9d44-69675b61875f/");
  await expect(page.getByRole("heading", { name: "William L Coulehan", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("Foreign Service");
  await expect(page.locator("main")).toContainText("United States Army");
  await expect(page.locator("main")).toContainText("medium");
});

test("Batch 479 publishes three occupations without converting them into employers", async ({ page }) => {
  const expected = [
    ["1b3a302e-e10a-57e4-9143-e144f7919a82", "Animal and livestock farmer"],
    ["ff3fdf0f-abdb-5be6-ac9b-11c8d353d671", "Salesman or sales agent, except to consumers"],
    ["26190080-de5a-5832-b39a-cebaab2f1e22", "Apprentice to an unspecified trade"],
  ];
  for (const [id, occupation] of expected) {
    const person = profile(id);
    expect(person.last_civilian_pre_service).toEqual([]);
    expect(person.other_pre_oss_affiliations).toContainEqual(
      expect.objectContaining({
        occupation,
        relationship_type: "unknown",
        claim_confidence: "medium",
      }),
    );
  }

  await page.goto("./people/26190080-de5a-5832-b39a-cebaab2f1e22/");
  await expect(page.locator("main")).toContainText("Apprentice to an unspecified trade");
  await expect(page.locator("main")).toContainText("No reliable pre-OSS employer has yet been identified");
});

test("Batch 479 identifies Jacques Coulon but does not create a pre-OSS affiliation", async ({ page }) => {
  const person = profile("c2828388-db19-58d8-a471-301a9145e329");
  expect(person).toMatchObject({
    display_name: "Jacques Coulon",
    identity_status: "high_confidence",
    personnel_category: "foreign_or_allied_military_personnel",
    commissioned_officer: true,
    allied_or_foreign_personnel: true,
    research_status: "requires_archival_review",
    immediate_pre_oss_affiliations: [],
    last_civilian_pre_service: [],
    other_pre_oss_affiliations: [],
  });

  await page.goto("./people/c2828388-db19-58d8-a471-301a9145e329/");
  await expect(page.getByRole("heading", { name: "Jacques Coulon", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("Jacques Olivier");
  await expect(page.locator("main")).toContainText("History of WWII Infiltrations into/from France");
  await expect(page.locator("main")).toContainText("No reliable pre-OSS employer has yet been identified");
});

test("Batch 479 leaves the three unsupported identities unresolved", () => {
  for (const id of [
    "3e6993ac-d49d-59d4-849e-9bdd6cebf337",
    "3950d7cb-7507-50d0-ac89-2bf63e7e495c",
    "8f649739-f4de-5151-8be5-68d38810f730",
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
