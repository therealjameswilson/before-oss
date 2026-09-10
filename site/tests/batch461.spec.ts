import { expect, test } from "@playwright/test";
import fs from "node:fs";

const people = JSON.parse(
  fs.readFileSync(new URL("../src/data/generated/people.json", import.meta.url), "utf8"),
);
const profile = (id: string) =>
  people.find((person: { person_id: string }) => person.person_id === id);

test("Batch 461 preserves all ten printed rows and masks every private identifier", () => {
  const expected = [
    ["796f0bfd-732d-5449-be84-8ae51f1b4caf", "Charles O Cook", "0193fabc-512d-555c-8f71-1959f0df4d41", null],
    ["e4aee293-5bc4-5739-9e4d-735b207b0328", "Dale F Cook", "4b912118-96cc-58de-9b00-ccc4109ecc60", "••••1568"],
    ["256a16fd-e610-5e66-ac19-24e9b1c1a84f", "Davis L Cook", "e297e69a-75c9-59b5-80d2-a1db8facd5cd", "••••4520"],
    ["b6d62d28-903d-53ec-a922-da32c886debb", "Elizabeth H Cook", "5d88f73a-775d-55b8-9c2b-870cd4b85e74", null],
    ["2c03ea7a-e55c-5348-87a3-15541613c6ca", "Eva C Cook", "8ee19062-62c4-5223-909f-01a377c69e59", null],
    ["7d58331c-6419-5913-bac6-93aad2ccc35e", "Francis Cook", "f2f05119-eb7a-5a1a-828c-61402d882d46", "••••6788"],
    ["6c7befb4-94af-5ff0-8ecb-605fa3f9bb81", "Fred H Cook", "1459ee11-3016-550a-a2b7-8da0061aab1f", "••••4435"],
    ["c5ca3947-b204-5a4b-b533-5ac65a3450ed", "Harl Cook", "ee680036-7de3-5d85-983b-5fb5747dc27f", null],
    ["0cb5cf08-851f-5071-a678-5bcf93f74e01", "Harry E Cook", "20711b32-b84b-534a-a0c7-2b268e66700a", null],
    ["05fae687-d82f-5b9d-8434-0087d4fb44ca", "Hughes M Cook", "26aa9303-449c-543d-b156-6813ad522643", "••••9099"],
  ];

  for (const [id, name, sourceRecordId, serial] of expected) {
    const person = profile(String(id));
    expect(person).toMatchObject({ display_name: name });
    expect(person.source_records).toContainEqual(
      expect.objectContaining({
        source_record_id: sourceRecordId,
        rank_as_indexed: null,
        serial_masked: serial,
        box: "140",
        archive_location: "230/86/29/01",
        pdf_page: 91,
      }),
    );
    expect(JSON.stringify(person)).not.toMatch(
      /"serial_number"|"serial_number_raw"|"serial_number_normalized"/,
    );
  }
});

test("Batch 461 publishes Dale Cook's broad occupation without inventing an employer", async ({ page }) => {
  const dale = profile("e4aee293-5bc4-5739-9e4d-735b207b0328");
  expect(dale).toMatchObject({
    display_name: "Dale F Cook",
    identity_status: "confirmed",
    research_status: "occupation_only_found",
    personnel_category: "enlisted_army_personnel",
    commissioned_officer: false,
  });
  expect(dale.immediate_pre_oss_affiliations).toEqual([]);
  expect(dale.last_civilian_pre_service).toEqual([]);
  expect(dale.other_pre_oss_affiliations).toContainEqual(
    expect.objectContaining({
      occupation: "Unskilled occupations in canning and preserving of foods",
      end_date: "1942-10-08",
      temporal_basis: "strongly_date_bounded",
      claim_confidence: "medium",
      organization_id: null,
    }),
  );

  await page.goto("./people/" + dale.person_id + "/");
  await expect(page.getByRole("heading", { name: "Dale F Cook", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("canning and preserving of foods");
  await expect(page.locator("main")).toContainText(
    "Last civilian employer before serviceNo reliable pre-OSS employer has yet been identified",
  );
});

test("Batch 461 publishes Fred Cook's clerk category without naming an office", async ({ page }) => {
  const fred = profile("6c7befb4-94af-5ff0-8ecb-605fa3f9bb81");
  expect(fred).toMatchObject({
    display_name: "Fred H Cook",
    identity_status: "confirmed",
    research_status: "occupation_only_found",
    personnel_category: "enlisted_army_personnel",
    commissioned_officer: false,
  });
  expect(fred.last_civilian_pre_service).toEqual([]);
  expect(fred.other_pre_oss_affiliations).toContainEqual(
    expect.objectContaining({
      occupation: "Clerk, general office",
      end_date: "1944-01-29",
      claim_confidence: "medium",
      organization_id: null,
    }),
  );

  await page.goto("./people/" + fred.person_id + "/");
  await expect(page.getByRole("heading", { name: "Fred H Cook", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("Clerk, general office");
  await expect(page.locator("main")).toContainText("no employer or office is identified");
});

test("Batch 461 exposes Davis Cook's identifier conflict without transferring Army facts", async ({ page }) => {
  const davis = profile("256a16fd-e610-5e66-ac19-24e9b1c1a84f");
  expect(davis).toMatchObject({
    display_name: "Davis L Cook",
    identity_status: "conflicting",
    research_status: "conflicting_sources",
    personnel_category: "unknown_or_indeterminate",
    commissioned_officer: null,
    manual_review_required: true,
  });
  expect(davis.immediate_pre_oss_affiliations).toEqual([]);
  expect(davis.last_civilian_pre_service).toEqual([]);
  expect(davis.other_pre_oss_affiliations).toEqual([]);
  expect(davis.claims).toContainEqual(
    expect.objectContaining({
      claim_type: "identity",
      claim_confidence: "conflicting",
      publication_status: "conflicting",
    }),
  );

  await page.goto("./people/" + davis.person_id + "/");
  await expect(page.getByRole("heading", { name: "Davis L Cook", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("differs by one digit");
  await expect(page.locator("main")).toContainText("Review Box 140");
});

test("Batch 461 keeps missing-range and unresolved cases explicit and claim-safe", async ({ page }) => {
  const francis = profile("7d58331c-6419-5913-bac6-93aad2ccc35e");
  expect(francis).toMatchObject({
    display_name: "Francis Cook",
    identity_status: "unresolved",
    research_status: "requires_archival_review",
  });
  expect(francis.immediate_pre_oss_affiliations).toEqual([]);
  expect(francis.last_civilian_pre_service).toEqual([]);
  expect(francis.other_pre_oss_affiliations).toEqual([]);
  expect(francis.claims).toContainEqual(
    expect.objectContaining({
      claim_type: "archival_file_status",
      claim_confidence: "confirmed",
      publication_status: "published",
    }),
  );

  await page.goto("./people/" + francis.person_id + "/");
  await expect(page.getByRole("heading", { name: "Francis Cook", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("documented missing serial-number range");
  await expect(page.locator("main")).toContainText("absence from the merged Army file is inconclusive");

  for (const [id, identityStatus, researchStatus] of [
    ["796f0bfd-732d-5449-be84-8ae51f1b4caf", "ambiguous", "needs_identity_review"],
    ["b6d62d28-903d-53ec-a922-da32c886debb", "unresolved", "requires_archival_review"],
    ["2c03ea7a-e55c-5348-87a3-15541613c6ca", "unresolved", "requires_archival_review"],
    ["c5ca3947-b204-5a4b-b533-5ac65a3450ed", "ambiguous", "needs_identity_review"],
    ["0cb5cf08-851f-5071-a678-5bcf93f74e01", "ambiguous", "needs_identity_review"],
  ]) {
    const person = profile(id);
    expect(person).toMatchObject({
      identity_status: identityStatus,
      research_status: researchStatus,
      manual_review_required: true,
    });
    expect(person.claims).toEqual([]);
    expect(person.immediate_pre_oss_affiliations).toEqual([]);
    expect(person.last_civilian_pre_service).toEqual([]);
    expect(person.other_pre_oss_affiliations).toEqual([]);
  }

  const hughes = profile("05fae687-d82f-5b9d-8434-0087d4fb44ca");
  expect(hughes).toMatchObject({
    identity_status: "confirmed",
    research_status: "requires_archival_review",
    personnel_category: "enlisted_army_personnel",
    commissioned_officer: false,
  });
  expect(hughes.other_pre_oss_affiliations).toEqual([]);
  expect(hughes.next_action).toContain("occupation value 999 is not used");
});
