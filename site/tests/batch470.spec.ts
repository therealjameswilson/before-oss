import { expect, test } from "@playwright/test";
import fs from "node:fs";

const people = JSON.parse(
  fs.readFileSync(new URL("../src/data/generated/people.json", import.meta.url), "utf8"),
);
const profile = (id: string) =>
  people.find((person: { person_id: string }) => person.person_id === id);

test("Batch 470 preserves all ten page 93 source rows and masks every printed identifier", () => {
  const expected = [
    ["72e197b6-b791-5901-9ecc-048c8bdd93e7", "Pauline Corbitt", "3f5deb9a-a24b-577b-bc52-3046e6a809f4", null, "••••9004", null],
    ["700a1c8f-81b5-5c1c-b154-2e0330284da4", "Roy E Corbitt", "448a7452-a4a9-5625-8b60-ff4193dc74bd", null, "••••5292", null],
    ["44dd444b-535d-5841-883c-c91816cb0eb5", "Charles R Corcoran", "35181e50-5abf-5cc7-b5f0-4150df17d4e2", null, "••••2607", null],
    ["5dbfeaaa-e870-55dd-97a4-a9f1ecdacced", "Herman L Corcoran", "464c0e20-b6e6-5240-b895-b49a0a172eeb", null, "••••2218", null],
    ["f34c37af-0401-59e5-981f-e11029289933", "Nicholas Cordas", "85bef506-e2dd-5aa5-8d29-25b69280c617", null, "••••6188", null],
    ["82810e22-1b1b-5b87-93f0-e8b8523d3de3", "Georges Cordeau", "169b470a-92cf-5245-a247-49251ed45d9a", "S/Lt", null, "French"],
    ["fc9962ab-4cbb-54d4-b2c9-ed5fc974d0f9", "Janet E Cordell", "6a65a0c7-6461-59ec-8af0-d09a223b8f77", null, null, null],
    ["df8a65b2-022e-5dac-af42-9212cdaa1b80", "Robert W Cordell", "f6152251-bbd4-5f68-9c83-c7fa959ca6c7", null, "••••9870", null],
    ["4dc8ed31-ebb9-582e-9be6-cb8f9dcd8c01", "Sidney Corderman", "50384bfb-6109-56e8-809e-ea34d6d52ac2", null, null, null],
    ["d5fcdbd6-11bd-527c-8776-61771b179684", "Sidney A Corderman", "420b9b99-4c30-5f94-b7ad-53dec7c20e3c", null, "••••3101", null],
  ];

  for (const [id, name, sourceRecordId, rank, serial, notes] of expected) {
    const person = profile(String(id));
    expect(person).toMatchObject({ display_name: name });
    expect(person.source_records).toContainEqual(
      expect.objectContaining({
        source_record_id: sourceRecordId,
        rank_as_indexed: rank,
        serial_masked: serial,
        notes_as_indexed: notes,
        box: "144",
        archive_location: "230/86/29/02",
        pdf_page: 93,
      }),
    );
    expect(JSON.stringify(person)).not.toMatch(
      /"serial_number"|"serial_number_raw"|"serial_number_normalized"/,
    );
  }
});

test("Batch 470 publishes only bounded Army evidence for Herman Corcoran and Nicholas Cordas", async ({ page }) => {
  const herman = profile("5dbfeaaa-e870-55dd-97a4-a9f1ecdacced");
  expect(herman).toMatchObject({
    display_name: "Herman L Corcoran",
    identity_status: "confirmed",
    personnel_category: "enlisted_army_personnel",
    commissioned_officer: false,
    research_status: "requires_archival_review",
  });
  expect(herman.immediate_pre_oss_affiliations).toEqual([]);
  expect(herman.last_civilian_pre_service).toEqual([]);
  expect(herman.other_pre_oss_affiliations).toEqual([]);

  const nicholas = profile("f34c37af-0401-59e5-981f-e11029289933");
  expect(nicholas).toMatchObject({
    display_name: "Nicholas Cordas",
    identity_status: "confirmed",
    personnel_category: "enlisted_army_personnel",
    commissioned_officer: false,
    research_status: "occupation_only_found",
  });
  expect(nicholas.immediate_pre_oss_affiliations).toEqual([]);
  expect(nicholas.last_civilian_pre_service).toEqual([]);
  expect(nicholas.other_pre_oss_affiliations).toContainEqual(
    expect.objectContaining({
      organization_id: null,
      occupation: "Occupations in manufacture of tobacco products",
      relationship_type: "unknown",
      end_date: "1942-12-09",
      temporal_basis: "strongly_date_bounded",
      claim_confidence: "medium",
    }),
  );

  await page.goto("./people/f34c37af-0401-59e5-981f-e11029289933/");
  await expect(page.getByRole("heading", { name: "Nicholas Cordas", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("Occupations in manufacture of tobacco products");
  await expect(page.locator("main")).toContainText("No reliable pre-OSS employer has yet been identified");
});

test("Batch 470 qualifies Georges Cordeau without expanding S/Lt or inventing a pre-OSS role", async ({ page }) => {
  const georges = profile("82810e22-1b1b-5b87-93f0-e8b8523d3de3");
  expect(georges).toMatchObject({
    display_name: "Georges Cordeau",
    identity_status: "high_confidence",
    personnel_category: "foreign_or_allied_military_personnel",
    commissioned_officer: null,
    allied_or_foreign_personnel: true,
    manual_review_required: false,
    research_status: "requires_archival_review",
  });
  expect(georges.name_variants).toEqual(expect.arrayContaining(["George Courtois", "Cottard"]));
  expect(georges.source_records[0]).toMatchObject({ rank_as_indexed: "S/Lt", notes_as_indexed: "French" });
  expect(georges.immediate_pre_oss_affiliations).toEqual([]);
  expect(georges.last_civilian_pre_service).toEqual([]);
  expect(georges.other_pre_oss_affiliations).toEqual([]);
  expect(georges.claims).toContainEqual(
    expect.objectContaining({
      claim_type: "identity",
      claim_confidence: "high",
      publication_status: "publish_qualified",
    }),
  );

  await page.goto("./people/82810e22-1b1b-5b87-93f0-e8b8523d3de3/");
  await expect(page.getByRole("heading", { name: "Georges Cordeau", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("S/Lt");
  await expect(page.locator("main")).toContainText("GR 28 P 4 175/187");
  await expect(page.locator("main")).toContainText("No reliable pre-OSS employer has yet been identified");
});

test("Batch 470 keeps the two Sidney Corderman rows separate while publishing student status only for Sidney A", async ({ page }) => {
  const plain = profile("4dc8ed31-ebb9-582e-9be6-cb8f9dcd8c01");
  const initialed = profile("d5fcdbd6-11bd-527c-8776-61771b179684");
  expect(plain).toMatchObject({
    display_name: "Sidney Corderman",
    identity_status: "ambiguous",
    manual_review_required: true,
    research_status: "requires_archival_review",
  });
  expect(initialed).toMatchObject({
    display_name: "Sidney A Corderman",
    identity_status: "confirmed",
    personnel_category: "enlisted_army_personnel",
    commissioned_officer: false,
    manual_review_required: true,
    research_status: "completed",
  });
  expect(plain.possible_duplicate_group).toMatch(/^duplicate-[a-f0-9]{12}$/);
  expect(initialed.possible_duplicate_group).toBe(plain.possible_duplicate_group);
  expect(plain.immediate_pre_oss_affiliations).toEqual([]);
  expect(plain.claims).toEqual([]);
  expect(initialed.immediate_pre_oss_affiliations).toContainEqual(
    expect.objectContaining({
      role_title: "High-school student",
      occupation: "Students",
      relationship_type: "student",
      immediate_pre_oss: true,
      last_civilian_pre_service: false,
      temporal_basis: "explicit_immediate",
      claim_confidence: "high",
    }),
  );
  expect(initialed.last_civilian_pre_service).toEqual([]);

  await page.goto("./people/d5fcdbd6-11bd-527c-8776-61771b179684/");
  await expect(page.getByRole("heading", { name: "Sidney A Corderman", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("High-school student");
  await expect(page.locator("main")).toContainText("student status is not employment");
  await expect(page.locator("main")).toContainText("Duplicate group");

  await page.goto("./people/4dc8ed31-ebb9-582e-9be6-cb8f9dcd8c01/");
  await expect(page.getByRole("heading", { name: "Sidney Corderman", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("do not transfer Sidney A Corderman's Army or student facts");
  await expect(page.locator("main")).toContainText("No reliable pre-OSS employer has yet been identified");
});
