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
  ["84b88ac0-c882-566b-bd62-65b0aa224892", "Thaddeus H Crenshaw", "dec34e74-ae23-5a8d-a2db-c4d72457d71a", false],
  ["660223ef-7a7f-5ce3-9279-e6c42d6883c0", "Clarence G Cress", "a936ad35-1936-50d1-8be5-8a626fa5f996", false],
  ["d98aeae7-2af1-56ad-991d-5d26d84f5cce", "John B Cress", "c12d77bc-f5f6-5cb2-a786-97b450576521", true],
  ["3da9e0bc-9be6-5214-86ce-3b088dfa1a25", "Richard Cressey", "cb7e1529-18c7-56b7-bc9a-de16b8ad649b", true],
  ["cce11ae8-4fc0-5791-b5e9-ea619a7232ff", "Luther F Cressman", "3ff36d97-16ae-56b4-a581-87e21b50bbe9", true],
  ["d81510b6-7af1-5f33-a7ef-cbc90a88ecf1", "Robert Cresswell", "f0f498d6-f1a9-59e6-beaa-dbd5f84e23de", true],
  ["65599afe-c36f-58d4-a134-c82a7402596e", "J C Crichton", "9e00d929-acbd-5bdb-9502-7ad4e0b3c4c5", false],
  ["b33700df-7c26-5160-9ea0-b3b17bc409a8", "Jack A Crichton", "97d29e78-5e32-5517-953b-865e40b8c99c", true],
  ["017814e5-1414-5ebe-9bc9-7f13a45a30dd", "Charles F Crider", "d9338165-aeb7-5fc3-a305-8a4fe3984e37", true],
  ["6eefb3bf-8a15-51cd-a50a-da8fa0adf805", "John W Crider", "885f15fc-cf30-594d-b141-57bce278d65d", true],
] as const;

test("Batch 494 preserves all ten page 98 rows and masks every printed identifier", () => {
  for (const [id, name, sourceRecordId, hasPrivateIdentifier] of cohort) {
    const person = profile(id);
    expect(person).toMatchObject({ display_name: name });
    const sourceRecord = person.source_records.find(
      (record: { source_record_id: string }) => record.source_record_id === sourceRecordId,
    );
    expect(sourceRecord).toMatchObject({
      box: "153",
      archive_location: "230/86/29/03",
      pdf_page: 98,
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
});

test("Batch 494 distinguishes the two officer pathways and their last civilian employers", () => {
  const cresswell = profile("d81510b6-7af1-5f33-a7ef-cbc90a88ecf1");
  expect(cresswell).toMatchObject({
    identity_status: "high_confidence",
    personnel_category: "commissioned_army_officer",
    commissioned_officer: true,
    research_status: "verified_employer_found",
    immediate_pre_oss_affiliations: [],
  });
  expect(cresswell.last_civilian_pre_service).toContainEqual(
    expect.objectContaining({
      canonical_organization: "Evening Public Ledger",
      role_title: "director and publisher",
      relationship_type: "employment",
      temporal_basis: "strongly_date_bounded",
      claim_confidence: "high",
    }),
  );
  expect(cresswell.other_pre_oss_affiliations).toContainEqual(
    expect.objectContaining({
      canonical_organization: "New York Herald Tribune",
      relationship_type: "employment",
      end_date: "1940",
    }),
  );

  const crichton = profile("b33700df-7c26-5160-9ea0-b3b17bc409a8");
  expect(crichton).toMatchObject({
    identity_status: "high_confidence",
    personnel_category: "commissioned_army_officer",
    commissioned_officer: true,
    research_status: "verified_employer_found",
    immediate_pre_oss_affiliations: [],
  });
  expect(crichton.name_variants).toEqual(
    expect.arrayContaining(["John Alston Crichton", "John A. 'Jack' Crichton"]),
  );
  expect(crichton.last_civilian_pre_service).toContainEqual(
    expect.objectContaining({
      canonical_organization: "Union Producing Company",
      role_title: "engineer and geologist",
      relationship_type: "employment",
      temporal_basis: "strongly_date_bounded",
      claim_confidence: "high",
    }),
  );
  expect(crichton.other_pre_oss_affiliations).toEqual(
    expect.arrayContaining([
      expect.objectContaining({
        canonical_organization: "Agricultural and Mechanical College of Texas",
        relationship_type: "student",
        end_date: "1937",
      }),
      expect.objectContaining({
        canonical_organization: "Massachusetts Institute of Technology",
        relationship_type: "student",
      }),
      expect.objectContaining({
        canonical_organization: "487th Bomb Group",
        relationship_type: "military_assignment",
        temporal_basis: "temporal_relation_uncertain",
      }),
    ]),
  );
});

test("Batch 494 publishes three exact-identifier statuses without inventing employers", () => {
  const cases = [
    ["3da9e0bc-9be6-5214-86ce-3b088dfa1a25", "Authors, editors, and reporters", "unknown"],
    ["cce11ae8-4fc0-5791-b5e9-ea619a7232ff", null, "student"],
    ["017814e5-1414-5ebe-9bc9-7f13a45a30dd", "General farmers", "unknown"],
  ] as const;
  for (const [id, occupation, relationshipType] of cases) {
    const person = profile(id);
    expect(person).toMatchObject({
      identity_status: "confirmed",
      personnel_category: "enlisted_army_personnel",
      commissioned_officer: false,
      research_status: "occupation_only_found",
      immediate_pre_oss_affiliations: [],
      last_civilian_pre_service: [],
    });
    expect(person.other_pre_oss_affiliations).toContainEqual(
      expect.objectContaining({
        occupation,
        relationship_type: relationshipType,
        temporal_basis: "documented_prewar",
        claim_confidence: "medium",
      }),
    );
  }
  const johnCrider = profile("6eefb3bf-8a15-51cd-a50a-da8fa0adf805");
  expect(johnCrider).toMatchObject({
    identity_status: "confirmed",
    personnel_category: "enlisted_army_personnel",
    commissioned_officer: false,
    research_status: "requires_archival_review",
    immediate_pre_oss_affiliations: [],
    last_civilian_pre_service: [],
    other_pre_oss_affiliations: [],
  });
  expect(JSON.stringify(johnCrider)).not.toContain("999");
});

test("Batch 494 retains unresolved and ambiguous people as archival-review profiles", () => {
  for (const id of [
    "84b88ac0-c882-566b-bd62-65b0aa224892",
    "660223ef-7a7f-5ce3-9279-e6c42d6883c0",
  ]) {
    expect(profile(id)).toMatchObject({
      identity_status: "unresolved",
      personnel_category: "unknown_or_indeterminate",
      commissioned_officer: null,
      research_status: "requires_archival_review",
      immediate_pre_oss_affiliations: [],
      last_civilian_pre_service: [],
      other_pre_oss_affiliations: [],
      claims: [],
    });
  }
  for (const id of [
    "d98aeae7-2af1-56ad-991d-5d26d84f5cce",
    "65599afe-c36f-58d4-a134-c82a7402596e",
  ]) {
    expect(profile(id)).toMatchObject({
      identity_status: "ambiguous",
      personnel_category: "unknown_or_indeterminate",
      commissioned_officer: null,
      research_status: "needs_identity_review",
      immediate_pre_oss_affiliations: [],
      last_civilian_pre_service: [],
      other_pre_oss_affiliations: [],
      claims: [],
    });
  }
});

test("Batch 494 direct routes show evidence qualifications and current coverage", async ({ page }) => {
  expect(stats.research_attempted_people).toBeGreaterThanOrEqual(4708);
  expect(stats.verified_affiliation_people).toBeGreaterThanOrEqual(536);
  expect(stats.verified_employer_people).toBeGreaterThanOrEqual(239);
  expect(stats.archival_review_assessed_people).toBeGreaterThanOrEqual(4663);

  await page.goto("./people/d81510b6-7af1-5f33-a7ef-cbc90a88ecf1/");
  await expect(page.getByRole("heading", { name: "Robert Cresswell", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("Evening Public Ledger");
  await expect(page.locator("main")).toContainText("New York Herald Tribune");
  await expect(page.locator("main")).toContainText("not proved to be the immediate OSS predecessor");

  await page.goto("./people/b33700df-7c26-5160-9ea0-b3b17bc409a8/");
  await expect(page.getByRole("heading", { name: "Jack A Crichton", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("Union Producing Company");
  await expect(page.locator("main")).toContainText("487th Bomb Group");
  await expect(page.locator("main")).toContainText("student status");

  await page.goto("./people/65599afe-c36f-58d4-a134-c82a7402596e/");
  await expect(page.getByRole("heading", { name: "J C Crichton", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("Five Library of Congress results");
  await expect(page.locator("main")).toContainText("No reliable pre-OSS employer has yet been identified");
});
