import { expect, test } from "@playwright/test";
import fs from "node:fs";

const people = JSON.parse(
  fs.readFileSync(new URL("../src/data/generated/people.json", import.meta.url), "utf8"),
);
const organizations = JSON.parse(
  fs.readFileSync(new URL("../src/data/generated/organizations.json", import.meta.url), "utf8"),
);
const profile = (id: string) =>
  people.find((person: { person_id: string }) => person.person_id === id);

test("Batch 433 keeps Rhea Clyman's three work relationships separate and non-immediate", async ({ page }) => {
  const rhea = profile("1c980bed-f447-5d32-ae33-f33cb9aab085");
  expect(rhea).toMatchObject({
    display_name: "Rhea G Clyman",
    identity_status: "high_confidence",
    research_status: "documented_prewar_employer_found",
  });
  expect(rhea.immediate_pre_oss_affiliations).toEqual([]);
  expect(rhea.last_civilian_pre_service).toEqual([]);
  expect(rhea.other_pre_oss_affiliations).toContainEqual(
    expect.objectContaining({
      canonical_organization: null,
      role_title: "secretary and assistant to Walter Duranty",
      relationship_type: "employment",
      temporal_basis: "documented_prewar",
      claim_confidence: "high",
    }),
  );
  expect(rhea.other_pre_oss_affiliations).toContainEqual(
    expect.objectContaining({
      role_title: "freelance journalist",
      relationship_type: "self_employment",
      temporal_basis: "documented_prewar",
      claim_confidence: "high",
    }),
  );
  expect(rhea.other_pre_oss_affiliations).toContainEqual(
    expect.objectContaining({
      canonical_organization: "The Daily Telegraph",
      organization_name_as_found: "Daily Telegraph",
      role_title: "Munich correspondent; later Canadian correspondent",
      relationship_type: "employment",
      temporal_basis: "documented_prewar",
      claim_confidence: "high",
    }),
  );

  const telegraph = organizations.find(
    (organization: { canonical_name: string }) =>
      organization.canonical_name === "The Daily Telegraph",
  );
  expect(telegraph).toMatchObject({
    historical_name: "Daily Telegraph",
    organization_type: "newspaper",
    sector: "journalism_and_media",
    country: "United Kingdom",
  });

  await page.goto(`./people/${rhea.person_id}/`);
  await expect(page.getByRole("heading", { name: "Rhea G Clyman", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("Walter Duranty");
  await expect(page.locator("main")).toContainText("freelance journalist");
  await expect(page.locator("main")).toContainText("Daily Telegraph");
  await expect(page.locator("main")).toContainText("No reviewed claim currently meets the publication threshold");
  await expect(page.getByRole("link", { name: "Rhea Clyman: A Forgotten Canadian Eyewitness to the Hunger of 1932" }).first()).toBeVisible();
});

test("Batch 433 publishes Army observations without inventing employers or ranks", async ({ page }) => {
  const lawrence = profile("b534123d-3fcb-5372-80bd-2adad61cec1f");
  expect(lawrence).toMatchObject({
    display_name: "Lawrence W Cloutier",
    identity_status: "confirmed",
    personnel_category: "enlisted_army_personnel",
    commissioned_officer: false,
    research_status: "requires_archival_review",
  });
  expect(lawrence.immediate_pre_oss_affiliations).toEqual([]);
  expect(lawrence.last_civilian_pre_service).toEqual([]);
  expect(lawrence.other_pre_oss_affiliations).toEqual([]);

  const wilbert = profile("d9a56a54-7416-585c-9088-c40d9d0f85af");
  expect(wilbert).toMatchObject({
    display_name: "Wilbert A Clower",
    identity_status: "confirmed",
    personnel_category: "enlisted_army_personnel",
    commissioned_officer: false,
    research_status: "occupation_only_found",
  });
  expect(wilbert.last_civilian_pre_service).toEqual([]);
  expect(wilbert.other_pre_oss_affiliations).toContainEqual(
    expect.objectContaining({
      occupation: "Student",
      relationship_type: "student",
      temporal_basis: "temporal_relation_uncertain",
      claim_confidence: "medium",
    }),
  );

  const william = profile("596a616a-89f6-5d52-873e-07bc88bbb05d");
  expect(william).toMatchObject({
    display_name: "William Clugston",
    identity_status: "confirmed",
    personnel_category: "unknown_or_indeterminate",
    commissioned_officer: null,
    research_status: "occupation_only_found",
  });
  expect(william.last_civilian_pre_service).toEqual([]);
  expect(william.other_pre_oss_affiliations).toContainEqual(
    expect.objectContaining({
      occupation: "Mechanics and repairmen, n.e.c.",
      relationship_type: "unknown",
      temporal_basis: "temporal_relation_uncertain",
      claim_confidence: "medium",
    }),
  );

  await page.goto(`./people/${william.person_id}/`);
  await expect(page.getByRole("heading", { name: "William Clugston", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("Mechanics and repairmen, n.e.c.");
  await expect(page.locator("main")).toContainText("No reliable pre-OSS employer has yet been identified");
});

test("Batch 433 qualifies Bartine Coady's identity and student status without retrojecting rank", async ({ page }) => {
  const bartine = profile("955f0289-9d0b-5f80-893f-74dc76a3d1f1");
  expect(bartine).toMatchObject({
    display_name: "Bartine H Coady",
    identity_status: "high_confidence",
    personnel_category: "unknown_or_indeterminate",
    commissioned_officer: null,
    research_status: "occupation_only_found",
  });
  expect(bartine.immediate_pre_oss_affiliations).toEqual([]);
  expect(bartine.last_civilian_pre_service).toEqual([]);
  expect(bartine.other_pre_oss_affiliations).toContainEqual(
    expect.objectContaining({
      occupation: "Student",
      relationship_type: "student",
      temporal_basis: "temporal_relation_uncertain",
      claim_confidence: "medium",
    }),
  );
  expect(bartine.claims).toContainEqual(
    expect.objectContaining({
      claim_type: "identity",
      claim_confidence: "high",
      publication_status: "published",
      match_notes: expect.stringContaining("postwar Special Forces roster"),
    }),
  );

  await page.goto(`./people/${bartine.person_id}/`);
  await expect(page.getByRole("heading", { name: "Bartine H Coady", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("Students");
  await expect(page.locator("main")).toContainText("No reliable pre-OSS employer has yet been identified");
  await expect(page.getByRole("link", { name: "The Office of Strategic Services (OSS) Influence on Special Forces" }).first()).toBeVisible();
});

test("Batch 433 preserves every source row and masks all private identifiers", async ({ page }) => {
  const expected = [
    ["c7b61b71-69a4-5b9e-b518-19741399ab28", "John Closson", "779a2789-0cc8-5cc8-a36d-0a61d418859f", 84, "unresolved", "requires_archival_review", false],
    ["330b9ef2-f9aa-518e-8de2-1776426907ca", "Elinor Cloutier", "e1f9b401-037b-50bd-af72-3bca4a9c5e45", 85, "unresolved", "requires_archival_review", false],
    ["b534123d-3fcb-5372-80bd-2adad61cec1f", "Lawrence W Cloutier", "254fe2e8-13dc-50d2-a962-825ad52a5982", 85, "confirmed", "requires_archival_review", true],
    ["d9a56a54-7416-585c-9088-c40d9d0f85af", "Wilbert A Clower", "209aa510-6393-57fb-a4f6-41d5b2996207", 85, "confirmed", "occupation_only_found", true],
    ["a61f35f8-91ec-5ece-b601-04e564352910", "James C Cloyd", "4cbf6444-6f2f-53a9-a5a0-703aed34ff68", 85, "unresolved", "requires_archival_review", false],
    ["596a616a-89f6-5d52-873e-07bc88bbb05d", "William Clugston", "3e43e916-453c-5d31-9c46-ecd0f519f814", 85, "confirmed", "occupation_only_found", true],
    ["1c980bed-f447-5d32-ae33-f33cb9aab085", "Rhea G Clyman", "21bdccd5-aa46-5ab9-9b8e-59247a46c758", 85, "high_confidence", "documented_prewar_employer_found", false],
    ["955f0289-9d0b-5f80-893f-74dc76a3d1f1", "Bartine H Coady", "09d3a5b6-79f0-577e-baff-186a47c2cc74", 85, "high_confidence", "occupation_only_found", false],
    ["ea74ad80-e073-5462-b04b-f7d8e5c381ff", "Helen I Coakley", "a27f3952-a529-5b96-b3ba-9be555d03581", 85, "unresolved", "requires_archival_review", false],
    ["d9b40381-d084-5697-97f3-fd5c7f124472", "Howard R Coan", "a82a7695-34fb-562f-a307-b7bf55cacf86", 85, "unresolved", "requires_archival_review", false],
  ];

  for (const [id, name, sourceRecordId, pdfPage, identityStatus, researchStatus, hasSerial] of expected) {
    const person = profile(String(id));
    expect(person).toMatchObject({
      display_name: name,
      identity_status: identityStatus,
      research_status: researchStatus,
    });
    expect(person.source_records[0]).toMatchObject({
      source_record_id: sourceRecordId,
      pdf_page: pdfPage,
      box: "130",
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

  await page.goto("./people/?q=Rhea%20G%20Clyman");
  await expect(page.getByRole("link", { name: "Rhea G Clyman", exact: true })).toBeVisible();
});
