import { expect, test } from "@playwright/test";
import fs from "node:fs";

const people = JSON.parse(
  fs.readFileSync(new URL("../src/data/generated/people.json", import.meta.url), "utf8"),
);
const profile = (id: string) =>
  people.find((person: { person_id: string }) => person.person_id === id);

test("Batch 467 preserves all ten printed rows and masks private identifiers", () => {
  const expected = [
    ["b132e054-84fd-5a3f-8956-c5288539fe1c", "Nolan R Cooper", "ed2ab845-633a-5a7e-9260-cc477a47fcd9", "••••7739"],
    ["e5c4c4ab-5004-57f5-ba4b-5584bac0452d", "Pauline F Cooper", "f4659263-4040-5126-98ac-63a8e69ee578", null],
    ["ceadd268-724f-5efd-977f-553262221b4c", "Rollo W Cooper", "8faa8429-fc8e-5789-bf02-13bdaf8886d7", null],
    ["17f2e6d5-1e8e-5934-954e-81e526b5b52c", "Sidney H Cooper", "66ee9e21-7878-552f-8e59-49f5e54a51ff", "••••5142"],
    ["416c6f4e-cc4f-59b7-9267-b7fa7bb933f5", "William H Cooper Jr.", "9da1abdf-3969-5df4-8f6c-704d88710c20", "••••3062"],
    ["c636e039-e9a5-5eff-9a56-a966d57148ec", "Steven V Cope", "84dd187e-381d-5660-8314-6218c3fafd07", "••••3945"],
    ["48ec3d94-3806-5556-9cf8-92f1febc59f0", "A C Copeland", "2261df3c-3e1f-58c9-a4ea-bb7b065befb7", null],
    ["918854bc-a1d6-5699-aeb5-a18a66ab2d25", "Arthur S Copeland", "982ee8d5-1168-5bbf-949e-e321464643ad", "••••4534"],
    ["2d84d529-4375-59c8-b43c-589d51d23afc", "Charles H Copeland", "24f71854-fdb4-5ffc-aeab-0b8f48e94a74", "••••2720"],
    ["19358879-499d-53d2-be9d-0d920b11cd0a", "Elizabeth Copeland", "9ee9f130-57b7-5391-adc4-86595113a248", null],
  ];

  for (const [id, name, sourceRecordId, serial] of expected) {
    const person = profile(String(id));
    expect(person).toMatchObject({ display_name: name });
    expect(person.source_records).toContainEqual(
      expect.objectContaining({
        source_record_id: sourceRecordId,
        rank_as_indexed: null,
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

test("Batch 467 publishes three date-bounded occupations without inventing employers", async ({ page }) => {
  const expected = [
    ["b132e054-84fd-5a3f-8956-c5288539fe1c", "General farm hand", "1941-02-03"],
    ["17f2e6d5-1e8e-5934-954e-81e526b5b52c", "Photographic-process occupation", "1942-08-17"],
    ["416c6f4e-cc4f-59b7-9267-b7fa7bb933f5", "Chauffeur or driver", "1941-04-04"],
  ];

  for (const [id, role, endDate] of expected) {
    const person = profile(String(id));
    expect(person).toMatchObject({
      identity_status: "confirmed",
      personnel_category: "enlisted_army_personnel",
      commissioned_officer: false,
      research_status: "occupation_only_found",
    });
    expect(person.immediate_pre_oss_affiliations).toEqual([]);
    expect(person.last_civilian_pre_service).toEqual([]);
    expect(person.other_pre_oss_affiliations).toContainEqual(
      expect.objectContaining({
        organization_id: null,
        role_title: role,
        relationship_type: "unknown",
        end_date: endDate,
        temporal_basis: "strongly_date_bounded",
        claim_confidence: "medium",
      }),
    );
  }

  await page.goto("./people/b132e054-84fd-5a3f-8956-c5288539fe1c/");
  await expect(page.getByRole("heading", { name: "Nolan R Cooper", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("Farm hands, general farms");
  await expect(page.locator("main")).toContainText("3 February 1941");
  await expect(page.locator("main")).toContainText("No reliable pre-OSS employer has yet been identified");
});

test("Batch 467 confirms William Cooper with the official OSS roster but does not recast it as pre-OSS employment", async ({ page }) => {
  const william = profile("416c6f4e-cc4f-59b7-9267-b7fa7bb933f5");
  expect(william.claims).toContainEqual(
    expect.objectContaining({
      claim_type: "identity",
      claim_confidence: "confirmed",
      evidence_excerpt: "Tec 3 William H. Cooper, Jr.",
    }),
  );
  expect(william.immediate_pre_oss_affiliations).toEqual([]);
  expect(william.last_civilian_pre_service).toEqual([]);
  expect(JSON.stringify(william.claims)).toContain("104-10165-10120.pdf");

  await page.goto("./people/416c6f4e-cc4f-59b7-9267-b7fa7bb933f5/");
  await expect(page.getByRole("heading", { name: "William H Cooper Jr.", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("Tec 3 William H. Cooper, Jr.");
  await expect(page.locator("main")).toContainText("Battle Participation Awards");
  await expect(page.locator("main")).toContainText("No reliable pre-OSS employer has yet been identified");
});

test("Batch 467 keeps the Arthur Copeland identifier conflict visible and routes unresolved people to Box 143", async ({ page }) => {
  const unresolved = [
    "e5c4c4ab-5004-57f5-ba4b-5584bac0452d",
    "ceadd268-724f-5efd-977f-553262221b4c",
    "c636e039-e9a5-5eff-9a56-a966d57148ec",
    "48ec3d94-3806-5556-9cf8-92f1febc59f0",
    "2d84d529-4375-59c8-b43c-589d51d23afc",
    "19358879-499d-53d2-be9d-0d920b11cd0a",
  ];
  for (const id of unresolved) {
    const person = profile(id);
    expect(person).toMatchObject({
      identity_status: "unresolved",
      personnel_category: "unknown_or_indeterminate",
      research_status: "requires_archival_review",
      manual_review_required: true,
    });
    expect(person.immediate_pre_oss_affiliations).toEqual([]);
    expect(person.last_civilian_pre_service).toEqual([]);
    expect(person.other_pre_oss_affiliations).toEqual([]);
    expect(person.claims).toEqual([]);
  }

  const arthur = profile("918854bc-a1d6-5699-aeb5-a18a66ab2d25");
  expect(arthur).toMatchObject({
    identity_status: "conflicting",
    personnel_category: "unknown_or_indeterminate",
    commissioned_officer: null,
    research_status: "conflicting_sources",
    manual_review_required: true,
  });
  expect(arthur.other_pre_oss_affiliations).toEqual([]);

  await page.goto("./people/918854bc-a1d6-5699-aeb5-a18a66ab2d25/");
  await expect(page.getByRole("heading", { name: "Arthur S Copeland", exact: true })).toBeVisible();
  await expect(page.getByText("conflicting", { exact: true }).first()).toBeVisible();
  await expect(page.getByText("conflicting sources", { exact: true }).first()).toBeVisible();
  await expect(page.locator("main")).toContainText("selects a different name");
  await expect(page.locator("main")).toContainText("Review Box 143");
});
