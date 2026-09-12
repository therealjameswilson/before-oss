import { expect, test } from "@playwright/test";
import fs from "node:fs";

const people = JSON.parse(
  fs.readFileSync(new URL("../src/data/generated/people.json", import.meta.url), "utf8"),
);
const profile = (id: string) =>
  people.find((person: { person_id: string }) => person.person_id === id);

test("Batch 474 preserves page 93-94 rows and masks private identifiers", () => {
  const expected = [
    ["bf272f97-ede5-5edc-a083-fedda34b9f67", "John F Corrigan", "86176af8-9f59-5ce8-a550-10004cb0a39a", "••••5214", null, 93, "145"],
    ["d822b77d-95a9-5807-9d23-542182d4b9bd", "Catherine T Corson", "4a1f0580-e131-5d5d-b614-fc9f3039e51d", null, null, 93, "145"],
    ["856cdb6d-6397-522b-8073-bec696892033", "William H Corson", "553f6808-8c5f-5200-8947-d2e9598804d5", "••••0772", null, 93, "145"],
    ["44f3c943-47ee-5868-8b6e-2d670d16b950", "Richard D Cortright", "abaef052-891b-5cd4-a7dd-8bb0cd569bc1", "••••7080", "Lt Cmdr", 93, "145"],
    ["f4bd1796-a781-5db0-8b99-d16023380c09", "Joseph V Corvaia", "f82d721d-9f71-55e2-9285-64cbfa8fdca3", "••••4334", null, 93, "146"],
    ["c0712d8a-84e1-5588-82d6-ebf7a6094d71", "Henry J Corven", "ba43084a-420c-5aaa-bebc-b96b3752a517", null, null, 94, "146"],
    ["98c3c478-3380-5141-83ae-9cd6b8ddfe33", "Melvin Corvin", "a48e81a1-70d9-5980-892b-94fdd966c451", "••••8209", null, 94, "146"],
    ["92c52128-31c7-5980-842c-eb2071d060a5", "Biagio M Corvio", "43aeff4e-31a0-5b02-973b-e389b9510eab", "••••9968", null, 94, "146"],
    ["33999a88-57d6-5564-8258-10816fd55d3c", "Archie B Cory", "1df90aea-ca97-5e0b-9945-06885ae68b8e", "••••1462", null, 94, "146"],
    ["1d72ab48-d68b-539f-a79f-320085c7b7b0", "Carolyn F Cory", "72227d87-62ed-54b8-8072-eb44357e1a41", null, null, 94, "146"],
  ];

  for (const [id, name, sourceRecordId, serial, rank, pdfPage, box] of expected) {
    const person = profile(String(id));
    expect(person).toMatchObject({ display_name: name });
    expect(person.source_records).toContainEqual(
      expect.objectContaining({
        source_record_id: sourceRecordId,
        serial_masked: serial,
        rank_as_indexed: rank,
        box,
        archive_location: "230/86/29/02",
        pdf_page: pdfPage,
      }),
    );
    expect(JSON.stringify(person)).not.toMatch(
      /"serial_number"|"serial_number_raw"|"serial_number_normalized"/,
    );
  }
});

test("Batch 474 publishes four bounded Army categories without inventing employers", async ({ page }) => {
  const cases = [
    ["bf272f97-ede5-5edc-a083-fedda34b9f67", "John F Corrigan", "Student", "1942-12-11", "student"],
    ["856cdb6d-6397-522b-8073-bec696892033", "William H Corson", "Statistical clerks and compilers", "1942-12-30", "unknown"],
    ["f4bd1796-a781-5db0-8b99-d16023380c09", "Joseph V Corvaia", "Clerks, general office", "1941-04-07", "unknown"],
    ["98c3c478-3380-5141-83ae-9cd6b8ddfe33", "Melvin Corvin", "Student", "1942-10-02", "student"],
  ];
  for (const [id, name, occupation, endDate, relationship] of cases) {
    const person = profile(id);
    expect(person).toMatchObject({
      display_name: name,
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
        occupation,
        relationship_type: relationship,
        end_date: endDate,
        temporal_basis: "temporal_relation_uncertain",
        claim_confidence: "medium",
      }),
    );
    await page.goto("./people/" + id + "/");
    await expect(page.getByRole("heading", { name, exact: true })).toBeVisible();
    await expect(page.locator("main")).toContainText(occupation);
    await expect(page.locator("main")).toContainText("No reliable pre-OSS employer has yet been identified");
  }
});

test("Batch 474 publishes Cortright's explicit Bureau of Ships pathway", async ({ page }) => {
  const person = profile("44f3c943-47ee-5868-8b6e-2d670d16b950");
  expect(person).toMatchObject({
    identity_status: "high_confidence",
    personnel_category: "commissioned_naval_officer",
    commissioned_officer: true,
    research_status: "verified_employer_found",
    manual_review_required: true,
  });
  expect(person.immediate_pre_oss_affiliations).toContainEqual(
    expect.objectContaining({
      organization_name_as_found: "U.S. Navy - BuShips",
      role_title: "Radio engineer",
      occupation: "Engineer, radio",
      relationship_type: "government_assignment",
      end_date: "1942-09",
      temporal_basis: "explicit_immediate",
      claim_confidence: "high",
    }),
  );
  expect(person.last_civilian_pre_service).toHaveLength(1);
  expect(person.last_civilian_pre_service[0].affiliation_id).toBe(
    person.immediate_pre_oss_affiliations[0].affiliation_id,
  );

  await page.goto("./people/44f3c943-47ee-5868-8b6e-2d670d16b950/");
  await expect(page.getByRole("heading", { name: "Richard D Cortright", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("U.S. Navy Bureau of Ships");
  await expect(page.locator("main")).toContainText("Radio engineer");
  await expect(page.locator("main")).toContainText("one digit");
});

test("Batch 474 qualifies Corven and keeps unresolved candidates out of affiliations", async ({ page }) => {
  const henry = profile("c0712d8a-84e1-5588-82d6-ebf7a6094d71");
  expect(henry).toMatchObject({
    identity_status: "probable",
    personnel_category: "enlisted_army_personnel",
    commissioned_officer: false,
    research_status: "requires_archival_review",
    immediate_pre_oss_affiliations: [],
    last_civilian_pre_service: [],
    other_pre_oss_affiliations: [],
  });
  await page.goto("./people/c0712d8a-84e1-5588-82d6-ebf7a6094d71/");
  await expect(page.locator("main")).toContainText("Army Rangers");
  await expect(page.locator("main")).toContainText("does not establish");

  for (const id of [
    "d822b77d-95a9-5807-9d23-542182d4b9bd",
    "92c52128-31c7-5980-842c-eb2071d060a5",
    "33999a88-57d6-5564-8258-10816fd55d3c",
    "1d72ab48-d68b-539f-a79f-320085c7b7b0",
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

  expect(profile("98c3c478-3380-5141-83ae-9cd6b8ddfe33")).toMatchObject({
    manual_review_required: true,
  });
  expect(profile("98c3c478-3380-5141-83ae-9cd6b8ddfe33").possible_duplicate_group).toBeTruthy();
});
