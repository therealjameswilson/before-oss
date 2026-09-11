import { expect, test } from "@playwright/test";
import fs from "node:fs";

const people = JSON.parse(
  fs.readFileSync(new URL("../src/data/generated/people.json", import.meta.url), "utf8"),
);
const profile = (id: string) =>
  people.find((person: { person_id: string }) => person.person_id === id);

test("Batch 468 preserves all ten printed rows and masks private identifiers", () => {
  const expected = [
    ["322b7b89-1422-5956-8c3a-13d4794bfa51", "James W Copeland", "3c95298f-9140-5d32-93fa-00c904ac8e4f", "1st Lt", null],
    ["c463ee18-73aa-5206-920b-8e2467214984", "Joe M Copeland", "3dacedb8-dcfd-59d1-ad2d-ee0cd90b53f7", null, "••••5158"],
    ["cde21206-1f2d-5241-82c6-7b30c8f95aa0", "Miles A Copeland", "8c659a26-63a1-5eb2-abd7-95ee67948f71", null, null],
    ["be18a8aa-49d3-5600-8d66-eae7b28afb78", "Millard A Copeland", "aa9b743b-70a6-5604-976c-db5eb88ce59b", null, "••••2318"],
    ["f59467d7-d1b6-5910-a5af-bdf88029c628", "Mortimemr Copeland", "f14ddb10-f516-5d77-9fd8-190025516914", null, null],
    ["8177c49f-4d61-5b3c-8120-cd1469aeacfe", "Oliver C Copeland", "4352f6eb-3851-5652-87a7-12cac3b1586a", null, null],
    ["af71bc77-f979-5ac8-809a-76ee6a73da1f", "Virginia Copeland", "035f86da-6435-51e3-a593-dcdd62da109a", null, null],
    ["4bcf1926-ed1a-5db4-878e-c8ac53a0beb7", "William Copeland", "03ca68bb-0e58-540f-91a2-f3a2089966f1", null, null],
    ["563d7809-de5d-5882-9a26-300f4273ca3c", "Ida L Coppa", "a8fa2086-cd46-50b6-aa72-f03c77492a48", null, null],
    ["7bb4f694-8286-5c6a-b1f9-6e583b3d3932", "John O Coppock", "6189b70a-abac-5e4a-b9af-96f872c95869", null, "••••6353"],
  ];

  for (const [id, name, sourceRecordId, rank, serial] of expected) {
    const person = profile(String(id));
    expect(person).toMatchObject({ display_name: name });
    expect(person.source_records).toContainEqual(
      expect.objectContaining({
        source_record_id: sourceRecordId,
        rank_as_indexed: rank,
        serial_masked: serial,
        box: "143",
        archive_location: "230/86/29/02",
        pdf_page: 92,
      }),
    );
    expect(JSON.stringify(person)).not.toMatch(
      /"serial_number"|"serial_number_raw"|"serial_number_normalized"/,
    );
  }
});

test("Batch 468 keeps the Joe Copeland conflict separate from Millard Copeland's confirmed Army match", async ({ page }) => {
  const joe = profile("c463ee18-73aa-5206-920b-8e2467214984");
  expect(joe).toMatchObject({
    identity_status: "conflicting",
    personnel_category: "unknown_or_indeterminate",
    commissioned_officer: null,
    research_status: "conflicting_sources",
    manual_review_required: true,
  });
  expect(joe.immediate_pre_oss_affiliations).toEqual([]);
  expect(joe.last_civilian_pre_service).toEqual([]);
  expect(joe.other_pre_oss_affiliations).toEqual([]);
  expect(joe.claims).toContainEqual(
    expect.objectContaining({ claim_type: "identity", claim_confidence: "conflicting" }),
  );

  const millard = profile("be18a8aa-49d3-5600-8d66-eae7b28afb78");
  expect(millard).toMatchObject({
    identity_status: "confirmed",
    personnel_category: "enlisted_army_personnel",
    commissioned_officer: false,
    research_status: "requires_archival_review",
  });
  expect(millard.immediate_pre_oss_affiliations).toEqual([]);
  expect(millard.last_civilian_pre_service).toEqual([]);
  expect(millard.other_pre_oss_affiliations).toEqual([]);

  await page.goto("./people/c463ee18-73aa-5206-920b-8e2467214984/");
  await expect(page.getByRole("heading", { name: "Joe M Copeland", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("selects a different full name");
  await expect(page.locator("main")).toContainText("Review Box 143");
});

test("Batch 468 publishes John Coppock's bounded occupation and earlier government assignment without inventing an immediate employer", async ({ page }) => {
  const john = profile("7bb4f694-8286-5c6a-b1f9-6e583b3d3932");
  expect(john).toMatchObject({
    identity_status: "confirmed",
    personnel_category: "enlisted_army_personnel",
    commissioned_officer: false,
    research_status: "requires_archival_review",
  });
  expect(john.immediate_pre_oss_affiliations).toEqual([]);
  expect(john.last_civilian_pre_service).toEqual([]);
  expect(john.other_pre_oss_affiliations).toContainEqual(
    expect.objectContaining({
      organization_id: null,
      occupation: "Professional occupations, n. e. c.",
      relationship_type: "unknown",
      end_date: "1943-08-10",
      temporal_basis: "strongly_date_bounded",
      claim_confidence: "medium",
    }),
  );
  expect(john.other_pre_oss_affiliations).toContainEqual(
    expect.objectContaining({
      canonical_organization: "War Production Board",
      role_title: "official",
      relationship_type: "government_assignment",
      start_date: "1942",
      end_date: "1942",
      temporal_basis: "documented_prewar",
      claim_confidence: "high",
    }),
  );

  await page.goto("./people/7bb4f694-8286-5c6a-b1f9-6e583b3d3932/");
  await expect(page.getByRole("heading", { name: "John O Coppock", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("War Production Board");
  await expect(page.locator("main")).toContainText("Professional occupations, n. e. c.");
  await expect(page.locator("main")).toContainText("No reliable pre-OSS employer has yet been identified");
});

test("Batch 468 preserves unresolved profiles while retaining Miles Copeland's established Army-to-OSS pathway", async ({ page }) => {
  const unresolved = [
    "322b7b89-1422-5956-8c3a-13d4794bfa51",
    "f59467d7-d1b6-5910-a5af-bdf88029c628",
    "8177c49f-4d61-5b3c-8120-cd1469aeacfe",
    "af71bc77-f979-5ac8-809a-76ee6a73da1f",
    "4bcf1926-ed1a-5db4-878e-c8ac53a0beb7",
    "563d7809-de5d-5882-9a26-300f4273ca3c",
  ];
  for (const id of unresolved) {
    const person = profile(id);
    expect(person).toMatchObject({
      identity_status: "unresolved",
      research_status: "requires_archival_review",
      manual_review_required: true,
    });
    expect(person.immediate_pre_oss_affiliations).toEqual([]);
    expect(person.last_civilian_pre_service).toEqual([]);
    expect(person.other_pre_oss_affiliations).toEqual([]);
    expect(person.claims).toEqual([]);
  }
  expect(profile("322b7b89-1422-5956-8c3a-13d4794bfa51")).toMatchObject({
    personnel_category: "commissioned_army_officer",
    commissioned_officer: true,
  });

  const miles = profile("cde21206-1f2d-5241-82c6-7b30c8f95aa0");
  expect(miles).toMatchObject({
    identity_status: "high_confidence",
    research_status: "occupation_only_found",
  });
  expect(miles.immediate_pre_oss_affiliations).toContainEqual(
    expect.objectContaining({
      canonical_organization: "United States Army",
      role_title: "Divisional Finance Office staff member",
      relationship_type: "military_assignment",
      temporal_basis: "explicit_immediate",
      claim_confidence: "high",
    }),
  );
  expect(miles.last_civilian_pre_service).toEqual([]);

  await page.goto("./people/f59467d7-d1b6-5910-a5af-bdf88029c628/");
  await expect(page.getByRole("heading", { name: "Mortimemr Copeland", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("Review Box 143");
  await expect(page.locator("main")).toContainText("No reliable pre-OSS employer has yet been identified");
});
