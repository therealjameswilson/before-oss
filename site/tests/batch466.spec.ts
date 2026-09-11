import { expect, test } from "@playwright/test";
import fs from "node:fs";

const people = JSON.parse(
  fs.readFileSync(new URL("../src/data/generated/people.json", import.meta.url), "utf8"),
);
const profile = (id: string) =>
  people.find((person: { person_id: string }) => person.person_id === id);

test("Batch 466 preserves all ten printed rows and masks private identifiers", () => {
  const expected = [
    ["84779f42-f02c-5d62-861f-dde0905ac594", "Eli M Cooper", "0a677489-3fd1-5eb3-9322-362626155006", "••••4182", "142"],
    ["d13fe5d3-0d6a-50c4-bbc3-9982be785237", "Elizabeth J Cooper", "e7894b54-a57e-5434-b658-76c1e06d17b6", null, "142"],
    ["14e06a51-042c-5f84-ac52-8776716e6979", "Felix Cooper", "a3734301-5508-5777-b752-50b374a9e173", null, "142"],
    ["7cbc08dd-c6b2-509b-85bc-d4546aded3b5", "Herbert W Cooper", "6694d56f-5e6b-5cf8-99bb-78b2a0e959b3", "••••6057", "142"],
    ["3eb6c58d-a758-5cfe-bf20-bd621fa5370a", "Howard E Cooper", "c0d89c53-d4d5-5415-9832-ac67cbd27417", "••••8456", "142"],
    ["b8f29223-b11a-55a3-8ba5-933bf34b0281", "Irvin E Cooper", "e6edf260-4be9-58c2-856f-7e819a879dec", "••••4212", "143"],
    ["ba8b5276-9d75-5f1b-a61f-0e42b0d017ad", "Irving Cooper", "171a6b54-9da7-5bf4-a8c5-de50710f8d96", "••••2011", "143"],
    ["46fc343b-db4d-5c83-95fb-9c965f42d52c", "John R Cooper", "5e785c14-16e9-5ee0-a8a5-e2da99a04be4", "••••4831", "143"],
    ["e554850e-f036-56f4-92c5-5b1a25b4c665", "Kenneth H Cooper", "ccb1c879-d91e-56f1-b85b-bce676ebc271", null, "143"],
    ["567f5127-667f-5d6f-9fc1-e5668235b48f", "Leslie T Cooper", "deebdf6a-9cf5-535f-88e5-28448486804a", "••••2320", "143"],
  ];

  for (const [id, name, sourceRecordId, serial, box] of expected) {
    const person = profile(String(id));
    expect(person).toMatchObject({ display_name: name });
    expect(person.source_records).toContainEqual(
      expect.objectContaining({
        source_record_id: sourceRecordId,
        rank_as_indexed: null,
        serial_masked: serial,
        box,
        archive_location: "230/86/29/02",
        pdf_page: 92,
      }),
    );
    expect(JSON.stringify(person)).not.toMatch(
      /"serial_number"|"serial_number_raw"|"serial_number_normalized"/,
    );
  }
});

test("Batch 466 keeps identifier matches and damaged personnel classifications distinct", () => {
  const enlisted = [
    "84779f42-f02c-5d62-861f-dde0905ac594",
    "3eb6c58d-a758-5cfe-bf20-bd621fa5370a",
    "b8f29223-b11a-55a3-8ba5-933bf34b0281",
    "ba8b5276-9d75-5f1b-a61f-0e42b0d017ad",
    "567f5127-667f-5d6f-9fc1-e5668235b48f",
  ];
  for (const id of enlisted) {
    expect(profile(id)).toMatchObject({
      identity_status: "confirmed",
      personnel_category: "enlisted_army_personnel",
      commissioned_officer: false,
    });
  }

  expect(profile("7cbc08dd-c6b2-509b-85bc-d4546aded3b5")).toMatchObject({
    identity_status: "high_confidence",
    personnel_category: "unknown_or_indeterminate",
    commissioned_officer: null,
    manual_review_required: true,
  });
  expect(profile("46fc343b-db4d-5c83-95fb-9c965f42d52c")).toMatchObject({
    identity_status: "confirmed",
    personnel_category: "unknown_or_indeterminate",
    commissioned_officer: null,
    manual_review_required: true,
  });
});

test("Batch 466 publishes six qualified occupations without inventing employers", async ({ page }) => {
  const expected = [
    ["84779f42-f02c-5d62-861f-dde0905ac594", "Accountant or auditor", "unknown", "1942-07-31"],
    ["7cbc08dd-c6b2-509b-85bc-d4546aded3b5", "Metal-products fabrication occupation, not elsewhere classified", "unknown", "1942-12-03"],
    ["3eb6c58d-a758-5cfe-bf20-bd621fa5370a", "Blaster or powderman", "unknown", "1941-08-21"],
    ["ba8b5276-9d75-5f1b-a61f-0e42b0d017ad", "Retail manager", "unknown", "1942-08-20"],
    ["46fc343b-db4d-5c83-95fb-9c965f42d52c", "Student", "student", "1943-03-22"],
    ["567f5127-667f-5d6f-9fc1-e5668235b48f", "Automobile-manufacturing occupation, not elsewhere classified", "unknown", "1941-05-08"],
  ];

  for (const [id, role, relationship, endDate] of expected) {
    const person = profile(String(id));
    expect(person.research_status).toBe("occupation_only_found");
    expect(person.immediate_pre_oss_affiliations).toEqual([]);
    expect(person.last_civilian_pre_service).toEqual([]);
    expect(person.other_pre_oss_affiliations).toContainEqual(
      expect.objectContaining({
        organization_id: null,
        role_title: role,
        relationship_type: relationship,
        end_date: endDate,
        temporal_basis: "strongly_date_bounded",
        claim_confidence: "medium",
      }),
    );
  }

  await page.goto("./people/46fc343b-db4d-5c83-95fb-9c965f42d52c/");
  await expect(page.getByRole("heading", { name: "John R Cooper", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("Student");
  await expect(page.locator("main")).toContainText("22 March 1943");
  await expect(page.locator("main")).toContainText("No reliable pre-OSS employer has yet been identified");
});

test("Batch 466 withholds name-only candidates and routes them to archival review", async ({ page }) => {
  for (const id of [
    "d13fe5d3-0d6a-50c4-bbc3-9982be785237",
    "14e06a51-042c-5f84-ac52-8776716e6979",
    "e554850e-f036-56f4-92c5-5b1a25b4c665",
  ]) {
    const person = profile(id);
    expect(person).toMatchObject({
      identity_status: "ambiguous",
      personnel_category: "unknown_or_indeterminate",
      research_status: "needs_identity_review",
      manual_review_required: true,
    });
    expect(person.immediate_pre_oss_affiliations).toEqual([]);
    expect(person.last_civilian_pre_service).toEqual([]);
    expect(person.other_pre_oss_affiliations).toEqual([]);
    expect(person.claims).toEqual([]);
  }

  const john = profile("46fc343b-db4d-5c83-95fb-9c965f42d52c");
  expect(john.claims.some((claim: { claim_text: string }) => claim.claim_text.includes("Miami Shipbuilding"))).toBe(false);

  const irvin = profile("b8f29223-b11a-55a3-8ba5-933bf34b0281");
  expect(irvin).toMatchObject({
    identity_status: "confirmed",
    research_status: "requires_archival_review",
    manual_review_required: true,
  });
  expect(irvin.other_pre_oss_affiliations).toEqual([]);

  await page.goto("./people/14e06a51-042c-5f84-ac52-8776716e6979/");
  await expect(page.getByRole("heading", { name: "Felix Cooper", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("No publishable pre-OSS affiliation is recorded yet");
  await expect(page.locator("main")).toContainText("Review Box 142");
});
