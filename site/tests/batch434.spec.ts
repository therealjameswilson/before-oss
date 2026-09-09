import { expect, test } from "@playwright/test";
import fs from "node:fs";

const people = JSON.parse(
  fs.readFileSync(new URL("../src/data/generated/people.json", import.meta.url), "utf8"),
);
const profile = (id: string) =>
  people.find((person: { person_id: string }) => person.person_id === id);

test("Batch 434 publishes William Coates's Army occupation without inventing a school or employer", async ({ page }) => {
  const william = profile("da473cf8-e23e-5403-92df-edfd762e0027");
  expect(william).toMatchObject({
    display_name: "William A Coates",
    identity_status: "confirmed",
    personnel_category: "enlisted_army_personnel",
    commissioned_officer: false,
    research_status: "occupation_only_found",
  });
  expect(william.immediate_pre_oss_affiliations).toEqual([]);
  expect(william.last_civilian_pre_service).toEqual([]);
  expect(william.other_pre_oss_affiliations).toContainEqual(
    expect.objectContaining({
      organization_id: null,
      occupation: "Teachers (secondary school) and principals",
      relationship_type: "unknown",
      end_date: "1945-03-08",
      temporal_basis: "temporal_relation_uncertain",
      claim_confidence: "medium",
    }),
  );

  await page.goto(`./people/${william.person_id}/`);
  await expect(page.getByRole("heading", { name: "William A Coates", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("Teachers (secondary school) and principals");
  await expect(page.locator("main")).toContainText("no school or employer is identified");
  await expect(page.locator("main")).toContainText("No reliable pre-OSS employer has yet been identified");
});

test("Batch 434 publishes Howard Cobb's Army occupation without inventing a business or employer", async ({ page }) => {
  const howard = profile("a88ecca2-dceb-5dfb-ab7c-b82a6e16e4c2");
  expect(howard).toMatchObject({
    display_name: "Howard L Cobb",
    identity_status: "confirmed",
    personnel_category: "enlisted_army_personnel",
    commissioned_officer: false,
    research_status: "occupation_only_found",
  });
  expect(howard.immediate_pre_oss_affiliations).toEqual([]);
  expect(howard.last_civilian_pre_service).toEqual([]);
  expect(howard.other_pre_oss_affiliations).toContainEqual(
    expect.objectContaining({
      organization_id: null,
      occupation: "Wholesale managers",
      relationship_type: "unknown",
      end_date: "1943-05-21",
      temporal_basis: "temporal_relation_uncertain",
      claim_confidence: "medium",
    }),
  );

  await page.goto(`./people/${howard.person_id}/`);
  await expect(page.getByRole("heading", { name: "Howard L Cobb", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("Wholesale managers");
  await expect(page.locator("main")).toContainText("no business or employer is identified");
  await expect(page.locator("main")).toContainText("No reliable pre-OSS employer has yet been identified");
});

test("Batch 434 preserves John Coates's identifier conflict and Anne Coblean's printed spelling", async ({ page }) => {
  const john = profile("8703b998-21c1-5ca0-8667-ae21edb33720");
  expect(john).toMatchObject({
    display_name: "John G Coates",
    identity_status: "unresolved",
    personnel_category: "unknown_or_indeterminate",
    commissioned_officer: null,
    research_status: "requires_archival_review",
  });
  expect(john.immediate_pre_oss_affiliations).toEqual([]);
  expect(john.last_civilian_pre_service).toEqual([]);
  expect(john.other_pre_oss_affiliations).toEqual([]);

  await page.goto(`./people/${john.person_id}/`);
  await expect(page.getByRole("heading", { name: "John G Coates", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("its identifier differs");
  await expect(page.locator("main")).toContainText("a name match alone cannot override that conflict");

  const anne = profile("e402087d-9fd7-5d8e-a2ca-4949832df232");
  expect(anne).toMatchObject({
    display_name: "Anne M Coblean",
    identity_status: "unresolved",
    research_status: "requires_archival_review",
  });

  await page.goto("./people/?q=Anne%20M%20Coblean");
  await expect(page.getByRole("link", { name: "Anne M Coblean", exact: true })).toBeVisible();
});

test("Batch 434 preserves every source row and masks all private identifiers", async () => {
  const expected = [
    ["369d1b90-2be8-5bc6-b2cf-ce7cb3d3cc70", "Philip B Coan", "cb7352b5-bdea-57b1-8ca0-2cc9fd49e83e", "130", true],
    ["edaa828b-1811-59b5-a0c7-6fa9c1017858", "George H Coates", "6b7318d8-bf74-5e2a-b14e-301bcca141a2", "130", false],
    ["7233304c-df1e-54eb-9888-bd185dbfdd49", "Jane E Coates", "28bc02ca-dda9-5bb9-9f91-30a121e76e62", "130", false],
    ["8703b998-21c1-5ca0-8667-ae21edb33720", "John G Coates", "a9f601d0-7ab4-534e-b6da-5661375de9a0", "130", true],
    ["d3c9b735-a32f-50b0-9c15-331915c52430", "Lucille A Coates", "6e78583c-7c71-58aa-a254-8cf31dbf62a6", "131", false],
    ["a7adf86f-391a-5c7f-ad58-ce4b554528e3", "Robert B Coates", "22cf490e-cd1e-5778-8e0d-c219eef7a39a", "131", false],
    ["da473cf8-e23e-5403-92df-edfd762e0027", "William A Coates", "559a7178-28cc-5303-bf51-57af116d2195", "131", true],
    ["ddbfcbc9-c79e-5c1e-800b-94eb8201f094", "Eleanor Cobb", "2e289aa0-7275-5673-9caf-916a231e88bb", "131", false],
    ["a88ecca2-dceb-5dfb-ab7c-b82a6e16e4c2", "Howard L Cobb", "1a536088-47ac-5702-a964-89ce08d39e41", "131", true],
    ["e402087d-9fd7-5d8e-a2ca-4949832df232", "Anne M Coblean", "9f4b517f-c03a-5141-95b0-9dc018b62d2a", "131", false],
  ];

  for (const [id, name, sourceRecordId, box, hasSerial] of expected) {
    const person = profile(String(id));
    expect(person).toMatchObject({ display_name: name });
    expect(person.source_records[0]).toMatchObject({
      source_record_id: sourceRecordId,
      pdf_page: 85,
      box,
      archive_location: "230/86/28/07",
      rank_as_indexed: null,
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
