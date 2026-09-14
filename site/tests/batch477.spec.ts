import { expect, test } from "@playwright/test";
import fs from "node:fs";

const people = JSON.parse(
  fs.readFileSync(new URL("../src/data/generated/people.json", import.meta.url), "utf8"),
);
const profile = (id: string) =>
  people.find((person: { person_id: string }) => person.person_id === id);

test("Batch 477 preserves page 94 rows and masks private identifiers", () => {
  const expected = [
    ["1b224fd6-fc49-51ff-86aa-c22ade2ada01", "Armand J Cote", "d18b1584-43e7-5217-b9a9-007894a0e0ed", "••••7176"],
    ["3a8adf2a-99f0-57fa-8180-bb65416675f9", "Gerard W Cote", "a0b452d4-7f66-5e1c-ab9f-dd5eda7633bd", "••••7028"],
    ["76b38e7b-52e4-580f-bdad-aeb7e70c5062", "Roger E Cote", "341be105-e954-50a8-ac54-cc120f6ede50", "••••4219"],
    ["d70d4a1b-1879-5a8d-ae76-cdabfa30e11d", "Roland E Cote", "a5bb326d-3e8a-5f04-b97b-91723189bf38", "••••1819"],
    ["a32d158c-e006-5a15-9597-3f4c7d87e5dc", "Florence M Cotes", "4a0a006a-f76d-5e6b-9d48-40a4bbd31ddb", null],
    ["e3de9c0a-74d7-54e5-a558-5a3a6d7db0ff", "Olen Cothron", "6d1870d5-d14d-58be-a4fb-3dff11a5a002", "••••7650"],
    ["42017296-cdee-51fb-a626-a7201e4bfc6c", "Robert L Cotnoir", "2afdc0c6-e891-50c7-91b5-e44ac2efd5c4", "••••1253"],
    ["c094a40b-111e-54a0-8320-9dd6aa661968", "George C Cotte", "d31b6ebe-1db2-5eb1-b9aa-2f01478170fd", null],
    ["bb4e1a85-eb07-5de2-a673-05a9e9a2fc15", "Charles R Cotton", "4733c8b7-0361-55e8-b097-ff5a7772ab37", "••••1828"],
    ["616d1c75-104d-55ed-9c8e-a23d62628e0f", "Christine Cotton", "6f36bc8f-07a1-5931-ada3-40360f88f264", null],
  ];

  for (const [id, name, sourceRecordId, serial] of expected) {
    const person = profile(String(id));
    expect(person).toMatchObject({ display_name: name });
    expect(person.source_records).toContainEqual(
      expect.objectContaining({
        source_record_id: sourceRecordId,
        serial_masked: serial,
        box: "147",
        archive_location: "230/86/29/02",
        pdf_page: 94,
      }),
    );
    expect(JSON.stringify(person)).not.toMatch(
      /"serial_number"|"serial_number_raw"|"serial_number_normalized"/,
    );
  }
});

test("Batch 477 confirms four exact Army-record identities while separating broad occupations", async ({ page }) => {
  const expected = [
    ["3a8adf2a-99f0-57fa-8180-bb65416675f9", "Gerard W Cote", "Cooks, except private family", "1940-09-09"],
    ["76b38e7b-52e4-580f-bdad-aeb7e70c5062", "Roger E Cote", "Clerks, general office", "1942-11-09"],
    ["d70d4a1b-1879-5a8d-ae76-cdabfa30e11d", "Roland E Cote", "Meatcutters, except in slaughtering and packing houses", "1942-03-05"],
  ];

  for (const [id, name, occupation, endDate] of expected) {
    const person = profile(String(id));
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
        relationship_type: "unknown",
        end_date: endDate,
        temporal_basis: "temporal_relation_uncertain",
        claim_confidence: "medium",
      }),
    );
  }

  await page.goto("./people/3a8adf2a-99f0-57fa-8180-bb65416675f9/");
  await expect(page.getByRole("heading", { name: "Gerard W Cote", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("Cooks, except private family");
  await expect(page.locator("main")).toContainText("No reliable pre-OSS employer has yet been identified");
});

test("Batch 477 does not publish Armand Cote's post-OSS occupation as pre-OSS evidence", async ({ page }) => {
  const person = profile("1b224fd6-fc49-51ff-86aa-c22ade2ada01");
  expect(person).toMatchObject({
    display_name: "Armand J Cote",
    identity_status: "confirmed",
    personnel_category: "enlisted_army_personnel",
    commissioned_officer: false,
    research_status: "requires_archival_review",
    immediate_pre_oss_affiliations: [],
    last_civilian_pre_service: [],
    other_pre_oss_affiliations: [],
  });

  await page.goto("./people/1b224fd6-fc49-51ff-86aa-c22ade2ada01/");
  await expect(page.getByRole("heading", { name: "Armand J Cote", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("30 January 1946");
  await expect(page.locator("main")).not.toContainText("Ore dressing occupations");
  await expect(page.locator("main")).toContainText("No reliable pre-OSS employer has yet been identified");
});

test("Batch 477 publishes Olen Cothron's qualified 1942 locksmith employment", async ({ page }) => {
  const person = profile("e3de9c0a-74d7-54e5-a558-5a3a6d7db0ff");
  expect(person).toMatchObject({
    display_name: "Olen Cothron",
    identity_status: "high_confidence",
    personnel_category: "unknown_or_indeterminate",
    commissioned_officer: null,
    research_status: "documented_prewar_employer_found",
    manual_review_required: true,
    immediate_pre_oss_affiliations: [],
  });
  expect(person.last_civilian_pre_service).toContainEqual(
    expect.objectContaining({
      organization_name_as_found: "L B Cothron",
      canonical_organization: "L. B. Cothron locksmith business",
      role_title: "Locksmith",
      occupation: "Locksmith",
      relationship_type: "employment",
      end_date: "1942",
      temporal_basis: "probable_immediate",
      identity_confidence: "high_confidence",
      claim_confidence: "medium",
    }),
  );

  await page.goto("./people/e3de9c0a-74d7-54e5-a558-5a3a6d7db0ff/");
  await expect(page.getByRole("heading", { name: "Olen Cothron", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("L B Cothron");
  await expect(page.locator("main")).toContainText("Locksmith");
  await expect(page.locator("main")).toContainText("San Diego Directory Co.'s San Diego City Directory 1942");
  await expect(page.locator("main")).toContainText("Longest-standing Austin locksmith");
  await expect(page.locator("main")).toContainText("medium probable immediate");
});

test("Batch 477 leaves five names unresolved with archival routing", async ({ page }) => {
  for (const id of [
    "a32d158c-e006-5a15-9597-3f4c7d87e5dc",
    "42017296-cdee-51fb-a626-a7201e4bfc6c",
    "c094a40b-111e-54a0-8320-9dd6aa661968",
    "bb4e1a85-eb07-5de2-a673-05a9e9a2fc15",
    "616d1c75-104d-55ed-9c8e-a23d62628e0f",
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

  await page.goto("./people/bb4e1a85-eb07-5de2-a673-05a9e9a2fc15/");
  await expect(page.getByRole("heading", { name: "Charles R Cotton", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("No reliable pre-OSS employer has yet been identified");
});
