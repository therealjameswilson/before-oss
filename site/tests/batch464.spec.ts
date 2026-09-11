import { expect, test } from "@playwright/test";
import fs from "node:fs";

const people = JSON.parse(
  fs.readFileSync(new URL("../src/data/generated/people.json", import.meta.url), "utf8"),
);
const profile = (id: string) =>
  people.find((person: { person_id: string }) => person.person_id === id);

test("Batch 464 preserves all ten printed rows and masks private identifiers", () => {
  const expected = [
    ["2bf3d9ad-d19b-55f7-8172-a4336b418051", "Pauline M Cooley", "5b1b2d94-e39c-5e17-9721-ba2392447b32", null, null, "141", "230/86/29/01"],
    ["9958e5f7-9493-5398-b484-953c5a9b860d", "Francis L Coolidge", "f6cf9fa4-d2dd-5ec6-8404-2c7b68ee142e", null, "••••5905", "141", "230/86/29/01"],
    ["8ea2275b-bbd5-5d86-be36-873def48b8fd", "Harold J Coolidge", "e129a64e-36b8-5e06-9474-38b923fb91fe", null, "••••5143", "141", "230/86/29/01"],
    ["5a549178-e64b-5fdb-ad77-622cc94c6dba", "Joseph R Coolidge", "91209d5b-821f-5356-a0d5-cb0f3d2e7c61", null, "••••4932", "141", "230/86/29/01"],
    ["75f816e0-cb7a-5049-b14f-2fb74f468201", "Randolph Coolidge", "c0d0595b-06f1-5c12-bde0-dd5d8bbd61e2", null, null, "141", "230/86/29/01"],
    ["19b4f006-b072-5123-ae6f-313addddabd8", "Frederick A Coombs", "617e4586-049d-5f6b-a4fa-af63c5723b74", null, null, "142", "230/86/29/02"],
    ["e04e5f14-a900-5e38-b071-e1bd77d4185d", "Philip H Coombs", "cbf290d3-b76e-51ee-9323-e9ef89a77b1a", null, "••••3323", "142", "230/86/29/02"],
    ["928871ef-6c5b-54dd-8967-08e8afcd7efc", "Carleton S Coon", "185919a6-a8f3-5c48-9c8f-494f9d0d761f", "Maj", null, "142", "230/86/29/02"],
    ["bc52d78c-9507-59da-825f-baf52d099771", "Edith M Coon", "fe1fd731-715c-5aca-9fc1-6e133039d801", null, null, "142", "230/86/29/02"],
    ["c1f8f54a-ac58-5885-b052-d6c6a069186f", "Maurice P Coon", "ea8f5a65-fb13-5c4c-8aff-35168f93fd02", null, null, "142", "230/86/29/02"],
  ];

  for (const [id, name, sourceRecordId, rank, serial, box, location] of expected) {
    const person = profile(String(id));
    expect(person).toMatchObject({ display_name: name });
    expect(person.source_records).toContainEqual(
      expect.objectContaining({
        source_record_id: sourceRecordId,
        rank_as_indexed: rank,
        serial_masked: serial,
        box,
        archive_location: location,
        pdf_page: 91,
      }),
    );
    expect(JSON.stringify(person)).not.toMatch(
      /"serial_number"|"serial_number_raw"|"serial_number_normalized"/,
    );
  }
});

test("Batch 464 publishes Francis Coolidge's military path without inventing an employer", async ({ page }) => {
  const francis = profile("9958e5f7-9493-5398-b484-953c5a9b860d");
  expect(francis).toMatchObject({
    display_name: "Francis L Coolidge",
    identity_status: "high_confidence",
    personnel_category: "commissioned_army_officer",
    commissioned_officer: true,
    research_status: "completed",
  });
  expect(francis.name_variants).toContain("Francis Lowell Coolidge");
  expect(francis.immediate_pre_oss_affiliations).toContainEqual(
    expect.objectContaining({
      canonical_organization: "United States Army Air Forces",
      role_title: "Captain",
      relationship_type: "military_assignment",
      temporal_basis: "explicit_immediate",
      claim_confidence: "high",
    }),
  );
  expect(francis.last_civilian_pre_service).toEqual([]);
  expect(francis.other_pre_oss_affiliations).toEqual(
    expect.arrayContaining([
      expect.objectContaining({ canonical_organization: "French Foreign Legion", start_date: "1931", end_date: "1936" }),
      expect.objectContaining({ occupation: "Stockbroker", organization_id: null, claim_confidence: "medium" }),
    ]),
  );

  await page.goto("./people/9958e5f7-9493-5398-b484-953c5a9b860d/");
  await expect(page.getByRole("heading", { name: "Francis L Coolidge", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("United States Army Air Forces");
  await expect(page.locator("main")).toContainText("French Foreign Legion");
  await expect(page.locator("main")).toContainText("Stockbroker");
  await expect(page.locator("main")).toContainText("No reliable pre-OSS employer has yet been identified");
});

test("Batch 464 publishes Harold Coolidge's museum role as immediate and last civilian", async ({ page }) => {
  const harold = profile("8ea2275b-bbd5-5d86-be36-873def48b8fd");
  expect(harold).toMatchObject({
    display_name: "Harold J Coolidge",
    identity_status: "high_confidence",
    personnel_category: "unknown_or_indeterminate",
    commissioned_officer: null,
    research_status: "verified_employer_found",
  });
  expect(harold.name_variants).toContain("Harold Jefferson Coolidge Jr.");
  expect(harold.immediate_pre_oss_affiliations).toContainEqual(
    expect.objectContaining({
      canonical_organization: "Museum of Comparative Zoology at Harvard University",
      role_title: "Curator of mammals; museum staff member",
      start_date: "1929",
      end_date: "1940",
      immediate_pre_oss: true,
      last_civilian_pre_service: true,
      temporal_basis: "explicit_immediate",
      claim_confidence: "high",
    }),
  );
  expect(harold.last_civilian_pre_service).toHaveLength(1);

  await page.goto("./people/8ea2275b-bbd5-5d86-be36-873def48b8fd/");
  await expect(page.getByRole("heading", { name: "Harold J Coolidge", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("Museum of Comparative Zoology");
  await expect(page.locator("main")).toContainText("appointment continued through 1946");
});

test("Batch 464 keeps Philip Coombs's OPA assignment distinct from Williams employment", async ({ page }) => {
  const philip = profile("e04e5f14-a900-5e38-b071-e1bd77d4185d");
  expect(philip).toMatchObject({
    display_name: "Philip H Coombs",
    identity_status: "high_confidence",
    personnel_category: "unknown_or_indeterminate",
    commissioned_officer: null,
    research_status: "documented_prewar_employer_found",
  });
  expect(philip.immediate_pre_oss_affiliations).toContainEqual(
    expect.objectContaining({
      canonical_organization: "United States Office of Price Administration",
      relationship_type: "government_assignment",
      temporal_basis: "probable_immediate",
      claim_confidence: "medium",
    }),
  );
  expect(philip.last_civilian_pre_service).toContainEqual(
    expect.objectContaining({
      canonical_organization: "Williams College",
      relationship_type: "employment",
      claim_confidence: "medium",
    }),
  );

  await page.goto("./people/e04e5f14-a900-5e38-b071-e1bd77d4185d/");
  await expect(page.getByRole("heading", { name: "Philip H Coombs", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("Office of Price Administration");
  await expect(page.locator("main")).toContainText("Williams College");
  await expect(page.locator("main .badge--medium")).toHaveCount(4);
});

test("Batch 464 retains Carleton Coon and exposes six unresolved archival profiles", async ({ page }) => {
  const carleton = profile("928871ef-6c5b-54dd-8967-08e8afcd7efc");
  expect(carleton).toMatchObject({
    identity_status: "high_confidence",
    personnel_category: "commissioned_army_officer",
    commissioned_officer: true,
    research_status: "verified_employer_found",
  });
  expect(carleton.immediate_pre_oss_affiliations).toEqual(
    expect.arrayContaining([
      expect.objectContaining({ canonical_organization: "Harvard University", claim_confidence: "high" }),
      expect.objectContaining({ canonical_organization: "Peabody Museum of Archaeology and Ethnology", claim_confidence: "high" }),
    ]),
  );

  for (const id of [
    "2bf3d9ad-d19b-55f7-8172-a4336b418051",
    "5a549178-e64b-5fdb-ad77-622cc94c6dba",
    "75f816e0-cb7a-5049-b14f-2fb74f468201",
    "19b4f006-b072-5123-ae6f-313addddabd8",
    "bc52d78c-9507-59da-825f-baf52d099771",
    "c1f8f54a-ac58-5885-b052-d6c6a069186f",
  ]) {
    const person = profile(id);
    expect(person).toMatchObject({
      identity_status: "unresolved",
      research_status: "requires_archival_review",
      manual_review_required: true,
    });
    expect(person.immediate_pre_oss_affiliations).toEqual([]);
    expect(person.last_civilian_pre_service).toEqual([]);
    expect(person.other_pre_oss_affiliations).toEqual([]);
  }

  await page.goto("./people/2bf3d9ad-d19b-55f7-8172-a4336b418051/");
  await expect(page.getByRole("heading", { name: "Pauline M Cooley", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("No reliable pre-OSS employer has yet been identified");
  await expect(page.locator("main")).toContainText("Review Box 141");
});
