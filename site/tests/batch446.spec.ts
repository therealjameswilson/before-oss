import { expect, test } from "@playwright/test";
import fs from "node:fs";

const people = JSON.parse(
  fs.readFileSync(new URL("../src/data/generated/people.json", import.meta.url), "utf8"),
);
const profile = (id: string) =>
  people.find((person: { person_id: string }) => person.person_id === id);

test("Batch 446 publishes four identifier-supported status or occupation findings without inventing employers", async ({ page }) => {
  const expected = [
    [
      "41d6b57f-b3de-5ad1-89df-f01733513dd0",
      "Gene Collins",
      "Students",
      "student",
      "1942-08-17",
    ],
    [
      "7da7d1c3-2c16-5ba1-9bbe-950fc7e84ddf",
      "Jerry Collins",
      "Authors, editors, and reporters",
      "unknown",
      "1941-04-30",
    ],
    [
      "09daac1e-9368-595d-a3f6-2a6c0e8f041b",
      "John H Collins",
      "Fruit and vegetable graders and packers",
      "unknown",
      "1942-01-27",
    ],
    [
      "8edb54b8-a539-51ee-bd72-1214c040b8a9",
      "Joseph G Collins",
      "Welders and flame cutters",
      "unknown",
      "1943-06-15",
    ],
  ];

  for (const [id, name, occupation, relationshipType, endDate] of expected) {
    const person = profile(id);
    expect(person).toMatchObject({
      display_name: name,
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
        occupation,
        relationship_type: relationshipType,
        end_date: endDate,
        temporal_basis: "strongly_date_bounded",
        identity_confidence: "confirmed",
        claim_confidence: "medium",
      }),
    );
  }

  const gene = profile("41d6b57f-b3de-5ad1-89df-f01733513dd0");
  await page.goto(`./people/${gene.person_id}/`);
  await expect(page.getByRole("heading", { name: "Gene Collins", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("Students");
  await expect(page.locator("main")).toContainText("no school or employer is identified");
  await expect(page.locator("main")).toContainText("No reliable pre-OSS employer has yet been identified");

  const jerry = profile("7da7d1c3-2c16-5ba1-9bbe-950fc7e84ddf");
  await page.goto(`./people/${jerry.person_id}/`);
  await expect(page.locator("main")).toContainText("Authors, editors, and reporters");
  await expect(page.locator("main")).toContainText("no employer or publication is identified");

  const john = profile("09daac1e-9368-595d-a3f6-2a6c0e8f041b");
  await page.goto(`./people/${john.person_id}/`);
  await expect(page.locator("main")).toContainText("Fruit and vegetable graders and packers");

  const joseph = profile("8edb54b8-a539-51ee-bd72-1214c040b8a9");
  await page.goto(`./people/${joseph.person_id}/`);
  await expect(page.locator("main")).toContainText("Welders and flame cutters");
});

test("Batch 446 confirms Charles J Collins Jr. but does not publish occupation value 999", async ({ page }) => {
  const charles = profile("f7c688a8-8d54-5d41-b7ab-30ae2aa07a48");
  expect(charles).toMatchObject({
    display_name: "Charles J Collins Jr.",
    identity_status: "confirmed",
    personnel_category: "enlisted_army_personnel",
    commissioned_officer: false,
    research_status: "requires_archival_review",
  });
  expect(charles.name_variants).toContain("Charles J Collins");
  expect(charles.immediate_pre_oss_affiliations).toEqual([]);
  expect(charles.last_civilian_pre_service).toEqual([]);
  expect(charles.other_pre_oss_affiliations).toEqual([]);
  expect(charles.claims).toHaveLength(1);
  expect(charles.claims[0]).toMatchObject({
    claim_type: "identity",
    claim_confidence: "confirmed",
  });

  await page.goto(`./people/${charles.person_id}/`);
  await expect(page.getByRole("heading", { name: "Charles J Collins Jr.", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("occupation value 999 is not used");
  await expect(page.locator("main")).toContainText("Review Box 135");
  await expect(page.locator("main")).toContainText("No reliable pre-OSS employer has yet been identified");
});

test("Batch 446 preserves all ten printed rows, masks identifiers and retains common-name uncertainty", async ({ page }) => {
  const expected = [
    ["f7c688a8-8d54-5d41-b7ab-30ae2aa07a48", "Charles J Collins Jr.", "307c33e5-050d-5bd0-b5c8-99f25df716d8", 87, true],
    ["41d6b57f-b3de-5ad1-89df-f01733513dd0", "Gene Collins", "877872d4-f18f-5076-88d3-c82b213e9716", 87, true],
    ["7e2ee329-1cc4-5a27-afe0-b3b303a1099a", "George E Collins", "8a9bd10c-4188-5fd7-a197-5512001a67d3", 87, false],
    ["75cb2a49-5ff1-5faf-9eff-4078f5b7ebd2", "Hugh R Collins", "2ac45d3d-d6fb-5f40-88e7-6517ff67a7bf", 87, false],
    ["725dc696-416e-58f3-9851-88a350a8b56e", "Jeremiah J Collins", "8b892af1-0062-5da0-8e42-b3ff5bc18361", 87, false],
    ["7da7d1c3-2c16-5ba1-9bbe-950fc7e84ddf", "Jerry Collins", "1262c141-979c-5ce0-82f1-ccdcb069809c", 87, true],
    ["bebae395-cd31-5149-8639-f9d5806111ef", "John F Collins", "4a759d39-ba0f-5397-950b-00bae620d557", 87, false],
    ["09daac1e-9368-595d-a3f6-2a6c0e8f041b", "John H Collins", "9cb7237e-8de2-5e52-9456-f1d2365d9fe7", 87, true],
    ["8edb54b8-a539-51ee-bd72-1214c040b8a9", "Joseph G Collins", "eaa7c2fb-f067-575c-ba8c-7331cc34bd9c", 87, true],
    ["1baaa662-e7c5-55f6-8849-4181b4ab8533", "Lucille G Collins", "0db3cd71-74c1-5ba1-a9fa-917d458d498b", 88, false],
  ];

  for (const [id, name, sourceRecordId, pdfPage, hasSerial] of expected) {
    const person = profile(String(id));
    expect(person).toMatchObject({ display_name: name });
    expect(person.source_records[0]).toMatchObject({
      source_record_id: sourceRecordId,
      box: "135",
      archive_location: "230/86/29/01",
      pdf_page: pdfPage,
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

  for (const id of [
    "7e2ee329-1cc4-5a27-afe0-b3b303a1099a",
    "75cb2a49-5ff1-5faf-9eff-4078f5b7ebd2",
    "725dc696-416e-58f3-9851-88a350a8b56e",
    "bebae395-cd31-5149-8639-f9d5806111ef",
    "1baaa662-e7c5-55f6-8849-4181b4ab8533",
  ]) {
    const person = profile(id);
    expect(person.identity_status).toBe("unresolved");
    expect(person.research_status).toBe("requires_archival_review");
    expect(person.immediate_pre_oss_affiliations).toEqual([]);
    expect(person.last_civilian_pre_service).toEqual([]);
    expect(person.other_pre_oss_affiliations).toEqual([]);
    expect(person.claims).toEqual([]);
  }

  const george = profile("7e2ee329-1cc4-5a27-afe0-b3b303a1099a");
  await page.goto(`./people/${george.person_id}/`);
  await expect(page.locator("main")).toContainText("twenty-four exact-name Army candidates");
  await expect(page.locator("main")).toContainText("No reliable pre-OSS employer has yet been identified");

  const hugh = profile("75cb2a49-5ff1-5faf-9eff-4078f5b7ebd2");
  await page.goto(`./people/${hugh.person_id}/`);
  await expect(page.locator("main")).toContainText("name-only match is insufficient");
  await expect(page.locator("main")).toContainText("Review Box 135");
});
