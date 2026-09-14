import { expect, test } from "@playwright/test";
import fs from "node:fs";

const people = JSON.parse(
  fs.readFileSync(new URL("../src/data/generated/people.json", import.meta.url), "utf8"),
);
const profile = (id: string) =>
  people.find((person: { person_id: string }) => person.person_id === id);

test("Batch 465 preserves all ten printed rows and masks private identifiers", () => {
  const expected = [
    ["394ac642-7026-5da3-8153-87f1ff3560d6", "Robert E Coon", "d7d136ec-4b0a-5633-ba8e-5e3422fe7709", null, 91, 44],
    ["b6a7c17b-e0af-56d2-beb9-fc6e131d728e", "John P Cooney", "acc41afd-6769-5795-aebd-ec3ab121d355", "••••6563", 91, 45],
    ["14021eff-848f-5894-bb24-1fd5d7d5061a", "Charles D Cooper", "741b66b4-c56a-53fa-9b47-8cc8c9044374", "••••1791", 91, 46],
    ["09badaa2-931e-5a0f-806d-36cc69f091c7", "Charles Cooper", "7eeaf593-1913-5214-8ba4-3922b9a1092d", null, 92, 1],
    ["e78c1717-7f75-57df-9b1d-6368f5542e26", "Charles L Cooper", "ed65c06e-73a8-5039-9a06-bdb3a2fd38da", null, 92, 2],
    ["d62072ee-b263-50a6-982c-b7d826115317", "Charles P Cooper", "33bace4c-986b-5bcd-a696-57eeb0a07d14", null, 92, 3],
    ["b79f33c3-4dcb-521d-af4e-d4d010b3e74b", "Chester L Cooper", "ecc262c2-b4c3-5cbf-ac84-86ca5925054f", "••••1133", 92, 4],
    ["b86e7f59-f6e7-58cb-bd75-3fe5c3a3dc8b", "Daisy F Cooper", "bbfa0eac-8590-5a00-ac41-9c71295153e4", null, 92, 5],
    ["261fdd65-1203-544c-a5e4-3cae6b03122a", "David C Cooper", "fd9a8364-5a3b-5faa-be99-21d31e917aad", null, 92, 6],
    ["2565c8ad-494c-5f06-bc6b-9b3782f77f97", "Delia A Cooper", "ab09c50e-5960-5fdb-a369-04d667cbb42b", null, 92, 7],
  ];

  for (const [id, name, sourceRecordId, serial, page, row] of expected) {
    const person = profile(String(id));
    expect(person).toMatchObject({ display_name: name });
    expect(person.source_records).toContainEqual(
      expect.objectContaining({
        source_record_id: sourceRecordId,
        rank_as_indexed: null,
        serial_masked: serial,
        box: "142",
        archive_location: "230/86/29/02",
        pdf_page: page,
      }),
    );
    expect(Number(row)).toBeGreaterThan(0);
    expect(JSON.stringify(person)).not.toMatch(
      /"serial_number"|"serial_number_raw"|"serial_number_normalized"/,
    );
  }
});

test("Batch 465 publishes Charles D Cooper's student status without inventing a school or employer", async ({ page }) => {
  const charles = profile("14021eff-848f-5894-bb24-1fd5d7d5061a");
  expect(charles).toMatchObject({
    display_name: "Charles D Cooper",
    identity_status: "confirmed",
    personnel_category: "enlisted_army_personnel",
    commissioned_officer: false,
    research_status: "occupation_only_found",
  });
  expect(charles.immediate_pre_oss_affiliations).toEqual([]);
  expect(charles.last_civilian_pre_service).toEqual([]);
  expect(charles.other_pre_oss_affiliations).toContainEqual(
    expect.objectContaining({
      organization_id: null,
      role_title: "Student",
      relationship_type: "student",
      end_date: "1945-04-11",
      temporal_basis: "strongly_date_bounded",
      claim_confidence: "medium",
    }),
  );

  await page.goto("./people/14021eff-848f-5894-bb24-1fd5d7d5061a/");
  await expect(page.getByRole("heading", { name: "Charles D Cooper", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("Student");
  await expect(page.locator("main")).toContainText("11 April 1945");
  await expect(page.locator("main")).toContainText("No reliable pre-OSS employer has yet been identified");
  await expect(page.locator("main")).not.toContainText("School:");
});

test("Batch 465 publishes Chester Cooper's Army pathway and keeps universities as student affiliations", async ({ page }) => {
  const chester = profile("b79f33c3-4dcb-521d-af4e-d4d010b3e74b");
  expect(chester).toMatchObject({
    display_name: "Chester L Cooper",
    identity_status: "high_confidence",
    personnel_category: "unknown_or_indeterminate",
    commissioned_officer: null,
    research_status: "completed",
    manual_review_required: true,
  });
  expect(chester.name_variants).toContain("Chester Lawrence Cooper");
  expect(chester.immediate_pre_oss_affiliations).toContainEqual(
    expect.objectContaining({
      canonical_organization: "United States Army",
      relationship_type: "military_assignment",
      country: "India",
      temporal_basis: "strongly_date_bounded",
      claim_confidence: "high",
    }),
  );
  expect(chester.last_civilian_pre_service).toEqual([]);
  expect(chester.other_pre_oss_affiliations).toEqual(
    expect.arrayContaining([
      expect.objectContaining({ canonical_organization: "Columbia University", relationship_type: "student" }),
      expect.objectContaining({ canonical_organization: "New York University", relationship_type: "student" }),
    ]),
  );
  const identityClaim = chester.claims.find((claim: { claim_type: string }) => claim.claim_type === "identity");
  expect(identityClaim.sources).toContainEqual(
    expect.objectContaining({ support_type: "contradicts" }),
  );

  await page.goto("./people/b79f33c3-4dcb-521d-af4e-d4d010b3e74b/");
  await expect(page.getByRole("heading", { name: "Chester L Cooper", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("United States Army");
  await expect(page.locator("main")).toContainText("Columbia University");
  await expect(page.locator("main")).toContainText("New York University");
  await expect(page.locator("main")).toContainText("identifier conflict");
  await expect(page.locator("main")).toContainText("No reliable pre-OSS employer has yet been identified");
});

test("Batch 465 keeps unresolved and ambiguous Cooper records visible for archival review", async ({ page }) => {
  const ambiguous = [
    "394ac642-7026-5da3-8153-87f1ff3560d6",
    "b6a7c17b-e0af-56d2-beb9-fc6e131d728e",
    "09badaa2-931e-5a0f-806d-36cc69f091c7",
    "e78c1717-7f75-57df-9b1d-6368f5542e26",
    "d62072ee-b263-50a6-982c-b7d826115317",
    "261fdd65-1203-544c-a5e4-3cae6b03122a",
  ];
  const unresolved = [
    "b86e7f59-f6e7-58cb-bd75-3fe5c3a3dc8b",
    "2565c8ad-494c-5f06-bc6b-9b3782f77f97",
  ];

  for (const id of ambiguous) {
    const person = profile(id);
    expect(person).toMatchObject({
      identity_status: "ambiguous",
      research_status: "needs_identity_review",
      manual_review_required: true,
    });
    expect(person.immediate_pre_oss_affiliations).toEqual([]);
    expect(person.last_civilian_pre_service).toEqual([]);
  }
  for (const id of unresolved) {
    const person = profile(id);
    expect(person).toMatchObject({
      identity_status: "unresolved",
      research_status: "requires_archival_review",
      manual_review_required: true,
    });
    expect(person.immediate_pre_oss_affiliations).toEqual([]);
    expect(person.last_civilian_pre_service).toEqual([]);
  }

  await page.goto("./people/09badaa2-931e-5a0f-806d-36cc69f091c7/");
  await expect(page.getByRole("heading", { name: "Charles Cooper", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("No publishable pre-OSS affiliation is recorded yet");
  await expect(page.locator("main")).toContainText("Review Box 142");
});
