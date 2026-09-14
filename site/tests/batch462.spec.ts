import { expect, test } from "@playwright/test";
import fs from "node:fs";

const people = JSON.parse(
  fs.readFileSync(new URL("../src/data/generated/people.json", import.meta.url), "utf8"),
);
const profile = (id: string) =>
  people.find((person: { person_id: string }) => person.person_id === id);

test("Batch 462 preserves all ten printed rows and masks every private identifier", () => {
  const expected = [
    ["7e6d5d65-afec-5e35-a90f-b582392b1ca8", "John E Cook", "894c13d6-33e8-5c60-b1ce-e3f0bd322527", null, "••••6642", "140"],
    ["4982a3aa-6e98-5f69-894d-40c84ad41c24", "Kenneth Cook", "f29aa274-c65d-5a9c-9d2f-b46f61065095", null, "••••9664", "140"],
    ["4c76083a-e31f-5b6a-843a-aa6ba37013f9", "Martha B Cook", "65b65e92-ded1-5203-ae82-594b3f3656dd", null, null, "140"],
    ["a6f7b473-69ef-595c-9e53-f90344c3a2f5", "Maurice W Cook", "7f8eed83-b685-5223-8a5d-64ffb35a786e", null, "••••5734", "140"],
    ["5a69205d-dc58-5458-9e14-6dd2cf5b63d5", "Richard C Cook", "a38405d1-5888-5bc0-b7c6-4935b900efd9", "Pvt", "••••0768", "141"],
    ["542d8d71-45a9-517e-a7d1-89fb73c9b2e7", "Thomas G Cook", "fa3f0dce-1bcc-5a42-a1ad-8ace00a61be5", null, null, "141"],
    ["2c9399a9-3a97-5121-93a5-789fe49d2d75", "Vernon J Cook", "384d9336-e41a-5a1f-b6fe-d18c27ca3753", null, "••••9345", "141"],
    ["09adaeb3-af39-5cc3-889e-ec3a80a8969f", "William R Cook", "1211695e-8601-5233-9de1-bea08ac5173d", null, "••••1489", "141"],
    ["a633c17b-9880-5302-92e3-33c6611d677b", "Wilmer J Cook", "872f2a6e-f624-5b20-afe8-faea600689ba", null, "••••6359", "141"],
    ["dcd6d6f2-13df-5e08-8fa8-da5378ce336b", "Adelaide L Cooke", "523b15a5-b4a8-5db3-a1e6-d86d2f1d8a8f", null, null, "141"],
  ];

  for (const [id, name, sourceRecordId, rank, serial, box] of expected) {
    const person = profile(String(id));
    expect(person).toMatchObject({ display_name: name });
    expect(person.source_records).toContainEqual(
      expect.objectContaining({
        source_record_id: sourceRecordId,
        rank_as_indexed: rank,
        serial_masked: serial,
        box,
        archive_location: "230/86/29/01",
        pdf_page: 91,
      }),
    );
    expect(JSON.stringify(person)).not.toMatch(
      /"serial_number"|"serial_number_raw"|"serial_number_normalized"/,
    );
  }
});

test("Batch 462 keeps both student findings separate from employers", async ({ page }) => {
  for (const [id, name, date] of [
    ["4982a3aa-6e98-5f69-894d-40c84ad41c24", "Kenneth Cook", "1942-10-01"],
    ["5a69205d-dc58-5458-9e14-6dd2cf5b63d5", "Richard C Cook", "1942-11-27"],
  ]) {
    const person = profile(id);
    expect(person).toMatchObject({
      display_name: name,
      identity_status: "confirmed",
      research_status: "occupation_only_found",
      personnel_category: "enlisted_army_personnel",
      commissioned_officer: false,
    });
    expect(person.immediate_pre_oss_affiliations).toEqual([]);
    expect(person.last_civilian_pre_service).toEqual([]);
    expect(person.other_pre_oss_affiliations).toContainEqual(
      expect.objectContaining({
        role_title: "Student",
        occupation: "Students",
        relationship_type: "student",
        end_date: date,
        claim_confidence: "medium",
        organization_id: null,
      }),
    );
  }

  await page.goto("./people/4982a3aa-6e98-5f69-894d-40c84ad41c24/");
  await expect(page.getByRole("heading", { name: "Kenneth Cook", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("classifies Kenneth Cook as a student");
  await expect(page.locator("main")).toContainText(
    "Last civilian employer before serviceNo reliable pre-OSS employer has yet been identified",
  );
});

test("Batch 462 publishes two broad occupations without inventing organizations", async ({ page }) => {
  const expected = [
    ["a6f7b473-69ef-595c-9e53-f90344c3a2f5", "Maurice W Cook", "Chauffeurs and drivers, bus, taxi, truck, and tractor", "1942-09-15"],
    ["a633c17b-9880-5302-92e3-33c6611d677b", "Wilmer J Cook", "Farm hands, general farms", "1943-10-02"],
  ];
  for (const [id, name, occupation, date] of expected) {
    const person = profile(id);
    expect(person).toMatchObject({
      display_name: name,
      identity_status: "confirmed",
      research_status: "occupation_only_found",
      personnel_category: "enlisted_army_personnel",
      commissioned_officer: false,
    });
    expect(person.last_civilian_pre_service).toEqual([]);
    expect(person.other_pre_oss_affiliations).toContainEqual(
      expect.objectContaining({
        occupation,
        end_date: date,
        claim_confidence: "medium",
        organization_id: null,
      }),
    );
  }

  await page.goto("./people/a633c17b-9880-5302-92e3-33c6611d677b/");
  await expect(page.getByRole("heading", { name: "Wilmer J Cook", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("Farm hands, general farms");
  await expect(page.locator("main")).toContainText("no farm or employer is identified");
});

test("Batch 462 exposes the William Cook conflict and Vernon Cook missing range", async ({ page }) => {
  const william = profile("09adaeb3-af39-5cc3-889e-ec3a80a8969f");
  expect(william).toMatchObject({
    display_name: "William R Cook",
    identity_status: "conflicting",
    research_status: "conflicting_sources",
    personnel_category: "unknown_or_indeterminate",
    commissioned_officer: null,
    manual_review_required: true,
  });
  expect(william.other_pre_oss_affiliations).toEqual([]);
  expect(william.claims).toContainEqual(
    expect.objectContaining({
      claim_type: "identity",
      claim_confidence: "conflicting",
      publication_status: "conflicting",
    }),
  );

  await page.goto("./people/09adaeb3-af39-5cc3-889e-ec3a80a8969f/");
  await expect(page.locator("main")).toContainText("selects William B Cook");
  await expect(page.locator("main")).toContainText("Review Box 141");

  const vernon = profile("2c9399a9-3a97-5121-93a5-789fe49d2d75");
  expect(vernon).toMatchObject({
    identity_status: "unresolved",
    research_status: "requires_archival_review",
  });
  expect(vernon.other_pre_oss_affiliations).toEqual([]);
  expect(vernon.claims).toContainEqual(
    expect.objectContaining({
      claim_type: "archival_file_status",
      claim_confidence: "confirmed",
      publication_status: "published",
    }),
  );
});

test("Batch 462 preserves every unresolved or ambiguous profile as an archival task", async ({ page }) => {
  for (const [id, identityStatus, researchStatus] of [
    ["7e6d5d65-afec-5e35-a90f-b582392b1ca8", "ambiguous", "needs_identity_review"],
    ["4c76083a-e31f-5b6a-843a-aa6ba37013f9", "unresolved", "requires_archival_review"],
    ["542d8d71-45a9-517e-a7d1-89fb73c9b2e7", "ambiguous", "needs_identity_review"],
    ["dcd6d6f2-13df-5e08-8fa8-da5378ce336b", "unresolved", "requires_archival_review"],
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

  await page.goto("./people/dcd6d6f2-13df-5e08-8fa8-da5378ce336b/");
  await expect(page.getByRole("heading", { name: "Adelaide L Cooke", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("No reliable pre-OSS employer has yet been identified");
  await expect(page.locator("main")).toContainText("Review Box 141");
});
