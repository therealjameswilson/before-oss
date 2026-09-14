import { expect, test } from "@playwright/test";
import fs from "node:fs";

const people = JSON.parse(
  fs.readFileSync(new URL("../src/data/generated/people.json", import.meta.url), "utf8"),
);
const profile = (id: string) =>
  people.find((person: { person_id: string }) => person.person_id === id);

test("Batch 476 preserves page 94 rows and masks private identifiers", () => {
  const expected = [
    ["75f19532-0d30-5784-9c18-7146d146541e", "Marcello Costa", "2cf955ba-ce1b-531e-88e7-b044eeb1f473", null, "146"],
    ["a6aeab1a-ddd1-5064-87f1-23d23d004a2d", "Mary Costadina", "6804a709-7c25-53a6-8082-d0d8ab2a6c15", null, "146"],
    ["8554b2e9-dbb0-575d-9223-10a2e0d5c5e6", "Mary Costello", "22cbb3d0-63b8-587f-b4ec-0b62413d2415", null, "146"],
    ["26464c71-94c8-50b0-9124-d0e146e3e850", "Rita L Costello", "7462c75b-a3e0-5865-8189-d207e2dfc030", null, "146"],
    ["b463c8b7-30dd-5723-9dcd-ea41dc5395e1", "Robert E Costello", "f280cc0c-36b0-5dc7-8fbe-704b793417a8", "••••9502", "146"],
    ["a46a2163-11cd-53c5-b3cf-71285d5df5a6", "Donald Q Coster", "d064e498-451a-5b31-82b9-5631220bf401", "••••6786", "146"],
    ["bcdbcfab-e4a1-59c9-8b00-ed1bed5e42f6", "Harry J Coster", "b56a07e3-46d3-5c87-8b3c-ddf4a915d2f1", null, "147"],
    ["febd27ff-26a7-50a0-91a4-cd21eb59afdd", "Melvin Coster", "f2fdfce0-c96a-5895-8f92-da796628422e", null, "147"],
    ["7546cd85-f1e5-5f15-b033-5897f92d414a", "James H Costigan", "94e0e180-13ba-51e4-a508-57d30634a365", null, "147"],
    ["b060b3d9-824b-5ae6-adf6-219edd3358e8", "Andrew Costopoulos", "49c8a3a7-c217-5acc-8c83-8c9500b935b8", "••••1590", "147"],
  ];

  for (const [id, name, sourceRecordId, serial, box] of expected) {
    const person = profile(String(id));
    expect(person).toMatchObject({ display_name: name });
    expect(person.source_records).toContainEqual(
      expect.objectContaining({
        source_record_id: sourceRecordId,
        serial_masked: serial,
        box,
        archive_location: "230/86/29/02",
        pdf_page: 94,
      }),
    );
    expect(JSON.stringify(person)).not.toMatch(
      /"serial_number"|"serial_number_raw"|"serial_number_normalized"/,
    );
  }
  expect(profile("75f19532-0d30-5784-9c18-7146d146541e").source_records).toContainEqual(
    expect.objectContaining({ notes_as_indexed: "Italian Ci" }),
  );
});

test("Batch 476 publishes Donald Coster's separated pathway with source-level citations", async ({ page }) => {
  const person = profile("a46a2163-11cd-53c5-b3cf-71285d5df5a6");
  expect(person).toMatchObject({
    display_name: "Donald Q Coster",
    identity_status: "high_confidence",
    personnel_category: "commissioned_army_officer",
    commissioned_officer: true,
    research_status: "verified_employer_found",
    manual_review_required: true,
  });
  expect(person.immediate_pre_oss_affiliations).toContainEqual(
    expect.objectContaining({
      canonical_organization: "Office of Naval Intelligence",
      relationship_type: "military_assignment",
      temporal_basis: "explicit_immediate",
      claim_confidence: "high",
    }),
  );
  expect(person.last_civilian_pre_service).toContainEqual(
    expect.objectContaining({
      organization_id: null,
      organization_name_as_found: "an advertising firm in Montreal",
      role_title: "Sales manager",
      relationship_type: "employment",
      temporal_basis: "strongly_date_bounded",
      claim_confidence: "high",
    }),
  );
  expect(person.other_pre_oss_affiliations).toEqual(expect.arrayContaining([
    expect.objectContaining({
      canonical_organization: "American Field Service",
      relationship_type: "volunteer",
      start_date: "1940",
    }),
    expect.objectContaining({
      canonical_organization: "Princeton University",
      relationship_type: "student",
      end_date: "1929",
    }),
  ]));

  await page.goto("./people/a46a2163-11cd-53c5-b3cf-71285d5df5a6/");
  await expect(page.getByRole("heading", { name: "Donald Q Coster", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("Office of Naval Intelligence");
  await expect(page.locator("main")).toContainText("advertising firm in Montreal");
  await expect(page.locator("main")).toContainText("American Field Service");
  await expect(page.locator("main")).toContainText("Princeton University");
  await expect(page.locator("main")).toContainText("But We Expected You at Dakar");
  await expect(page.locator("main")).toContainText("Behind the German Lines");
  await expect(page.locator("main")).toContainText("high-confidence");
});

test("Batch 476 qualifies Andrew Costopoulos's broad Army occupation without inventing an employer", async ({ page }) => {
  const person = profile("b060b3d9-824b-5ae6-adf6-219edd3358e8");
  expect(person).toMatchObject({
    display_name: "Andrew Costopoulos",
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
      occupation: "Kitchen workers in hotels, restaurants, railroads, steamships, etc., n.e.c.",
      relationship_type: "unknown",
      end_date: "1942-08-05",
      temporal_basis: "temporal_relation_uncertain",
      claim_confidence: "medium",
    }),
  );

  await page.goto("./people/b060b3d9-824b-5ae6-adf6-219edd3358e8/");
  await expect(page.getByRole("heading", { name: "Andrew Costopoulos", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("Kitchen workers in hotels, restaurants, railroads, steamships, etc., n.e.c.");
  await expect(page.locator("main")).toContainText("No reliable pre-OSS employer has yet been identified");
});

test("Batch 476 leaves eight identities unresolved and preserves archival routing", async ({ page }) => {
  for (const id of [
    "75f19532-0d30-5784-9c18-7146d146541e",
    "a6aeab1a-ddd1-5064-87f1-23d23d004a2d",
    "8554b2e9-dbb0-575d-9223-10a2e0d5c5e6",
    "26464c71-94c8-50b0-9124-d0e146e3e850",
    "b463c8b7-30dd-5723-9dcd-ea41dc5395e1",
    "bcdbcfab-e4a1-59c9-8b00-ed1bed5e42f6",
    "febd27ff-26a7-50a0-91a4-cd21eb59afdd",
    "7546cd85-f1e5-5f15-b033-5897f92d414a",
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
  expect(profile("75f19532-0d30-5784-9c18-7146d146541e")).toMatchObject({
    allied_or_foreign_personnel: true,
    personnel_category: "unknown_or_indeterminate",
  });

  await page.goto("./people/75f19532-0d30-5784-9c18-7146d146541e/");
  await expect(page.locator("main")).toContainText("Italian Ci");
  await expect(page.locator("main")).toContainText("No reliable pre-OSS employer has yet been identified");
});
