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
  ["e9eb8245-a802-57d7-906d-6c7e54302031", "Jean L Coyat", "f04d5fc1-6966-577e-92ef-4d8042601ee0", true],
  ["59ebafd3-8d0e-521d-9815-190f9aa7b109", "Hubert E Coyer", "ec3dd401-2155-51d9-bc0a-e274b2dfa34e", true],
  ["aa6c0357-7257-53ea-ac48-55cb961fd661", "William R Coyle", "3511bffb-894c-51fb-a1ee-1db86fb07703", false],
  ["65ee1ab7-c8f8-5d5c-a257-ede513b20455", "Joseph Coyne", "f98bbf7a-1b83-54b8-b0a6-f7d87e45d9fb", false],
  ["238d5430-0efc-55d9-a96e-d84cb37d0bbb", "Terence A Coyne", "6b834735-0079-5ce8-adb6-d36eccb7ae0a", false],
  ["f521034b-dfe0-5e2d-a07f-9b78b3dac4e9", "Yves J Cozic", "d39bd6e5-eadf-5ce1-bc28-2d3193f41fc0", true],
  ["0e7f7cad-745a-5e37-a9bf-b1b794b38576", "Arthur B Cozzens", "771fa3ea-20a7-521a-b66c-7665b0035389", false],
  ["4ebf7afb-3681-5b2b-b0f8-c84394053469", "James W Cozzens", "873663d5-4a57-5f44-8697-5be7f22fc46f", false],
  ["9764229d-fe04-5278-bea7-bf9c5d26af2a", "Nicholas A Cozzone", "6f4e3c0a-3628-5fb3-b0b2-1891abfdd7a9", true],
  ["8ea59ef4-9bd1-5eab-9b35-2f886ae390dd", "Lillian E Crabbe", "cdc40de5-c5dd-5fc1-8902-64cfd4b31ee3", false],
] as const;

test("Batch 487 preserves all ten page 96 rows and masks private identifiers", () => {
  for (const [id, name, sourceRecordId, hasPrivateIdentifier] of cohort) {
    const person = profile(id);
    expect(person).toMatchObject({ display_name: name });
    const sourceRecord = person.source_records.find(
      (record: { source_record_id: string }) => record.source_record_id === sourceRecordId,
    );
    expect(sourceRecord).toMatchObject({
      box: "151",
      archive_location: "230/86/29/03",
      pdf_page: 96,
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

test("Batch 487 keeps Hubert Coyer's earlier school and state-guard records qualified", () => {
  const hubert = profile("59ebafd3-8d0e-521d-9815-190f9aa7b109");
  expect(hubert).toMatchObject({
    display_name: "Hubert E Coyer",
    identity_status: "high_confidence",
    personnel_category: "commissioned_army_officer",
    commissioned_officer: true,
    research_status: "documented_prewar_employer_found",
    immediate_pre_oss_affiliations: [],
    last_civilian_pre_service: [],
  });
  expect(hubert.other_pre_oss_affiliations).toEqual(
    expect.arrayContaining([
      expect.objectContaining({
        canonical_organization: "John Marshall High School",
        role_title: "Teacher",
        relationship_type: "employment",
        temporal_basis: "documented_prewar",
        claim_confidence: "medium",
        publication_status: "publish_qualified",
      }),
      expect.objectContaining({
        canonical_organization: "74th Regiment, New York Guard",
        role_title: "Captain",
        relationship_type: "military_assignment",
        temporal_basis: "documented_prewar",
        claim_confidence: "high",
      }),
    ]),
  );
});

test("Batch 487 separates Terence Coyne's immediate naval assignment from his last civilian employer", () => {
  const terence = profile("238d5430-0efc-55d9-a96e-d84cb37d0bbb");
  expect(terence).toMatchObject({
    display_name: "Terence A Coyne",
    identity_status: "confirmed",
    personnel_category: "enlisted_naval_personnel",
    commissioned_officer: false,
    research_status: "verified_employer_found",
  });
  expect(terence.immediate_pre_oss_affiliations).toContainEqual(
    expect.objectContaining({
      canonical_organization: "U.S. Naval Hospital Great Lakes",
      role_title: "Yeoman first class on temporary duty",
      relationship_type: "military_assignment",
      end_date: "1945-03-17",
      temporal_basis: "explicit_immediate",
      claim_confidence: "confirmed",
    }),
  );
  expect(terence.last_civilian_pre_service).toContainEqual(
    expect.objectContaining({
      canonical_organization: "U.S. Railway Mail Service",
      role_title: "Railway mail clerk",
      relationship_type: "employment",
      start_date: "1939-07",
      end_date: "1942-11",
      claim_confidence: "confirmed",
    }),
  );
  expect(terence.other_pre_oss_affiliations).toEqual(
    expect.arrayContaining([
      expect.objectContaining({ canonical_organization: "Works Progress Administration" }),
      expect.objectContaining({ canonical_organization: "Civil Works Administration" }),
    ]),
  );
  expect(terence.archival_file).toMatchObject({
    nara_catalog_id: "2170299",
    review_priority: "low",
  });
});

test("Batch 487 publishes only broad Army-entry occupations for Coyat and Cozzone", () => {
  for (const [id, role] of [
    ["e9eb8245-a802-57d7-906d-6c7e54302031", "Cook (except private family)"],
    [
      "9764229d-fe04-5278-bea7-bf9c5d26af2a",
      "Chauffeur or vehicle driver (broad occupational group)",
    ],
  ]) {
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
        role_title: role,
        organization_id: null,
        relationship_type: "unknown",
        temporal_basis: "strongly_date_bounded",
        claim_confidence: "medium",
        publication_status: "publish_qualified",
      }),
    );
  }
});

test("Batch 487 keeps the six unsupported identities unresolved", () => {
  for (const id of [
    "aa6c0357-7257-53ea-ac48-55cb961fd661",
    "65ee1ab7-c8f8-5d5c-a257-ede513b20455",
    "f521034b-dfe0-5e2d-a07f-9b78b3dac4e9",
    "0e7f7cad-745a-5e37-a9bf-b1b794b38576",
    "4ebf7afb-3681-5b2b-b0f8-c84394053469",
    "8ea59ef4-9bd1-5eab-9b35-2f886ae390dd",
  ]) {
    const person = profile(id);
    expect(person.identity_status).toBe("unresolved");
    expect(person.research_status).toBe("requires_archival_review");
    expect(person.immediate_pre_oss_affiliations).toEqual([]);
    expect(person.last_civilian_pre_service).toEqual([]);
    expect(person.other_pre_oss_affiliations).toEqual([]);
    expect(person.claims).toEqual([]);
  }
});

test("Batch 487 profiles and coverage render the reviewed outcomes", async ({ page }) => {
  expect(stats.research_attempted_people).toBeGreaterThanOrEqual(4639);
  expect(stats.verified_affiliation_people).toBeGreaterThanOrEqual(532);
  expect(stats.verified_employer_people).toBeGreaterThanOrEqual(236);
  expect(stats.archival_review_assessed_people).toBeGreaterThanOrEqual(4594);

  await page.goto("./people/238d5430-0efc-55d9-a96e-d84cb37d0bbb/");
  await expect(page.getByRole("heading", { name: "Terence A Coyne", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("U.S. Naval Hospital Great Lakes");
  await expect(page.locator("main")).toContainText("U.S. Railway Mail Service");
  await expect(page.locator("main")).toContainText("Works Progress Administration");
  await expect(page.locator("main")).toContainText("Terence Coyne Personnel File, NAID 2170299");

  await page.goto("./people/59ebafd3-8d0e-521d-9815-190f9aa7b109/");
  await expect(page.getByRole("heading", { name: "Hubert E Coyer", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("John Marshall High School");
  await expect(page.locator("main")).toContainText("74th Regiment, New York Guard");
  await expect(page.locator("main")).toContainText(
    "No publishable immediate affiliation or civilian employer is recorded yet",
  );
});
