import { expect, test } from "@playwright/test";
import fs from "node:fs";

const people = JSON.parse(
  fs.readFileSync(new URL("../src/data/generated/people.json", import.meta.url), "utf8"),
);
const stats = JSON.parse(
  fs.readFileSync(new URL("../src/data/generated/stats.json", import.meta.url), "utf8"),
);
const organizations = JSON.parse(
  fs.readFileSync(new URL("../src/data/generated/organizations.json", import.meta.url), "utf8"),
);
const profile = (id: string) =>
  people.find((person: { person_id: string }) => person.person_id === id);

const cohort = [
  ["d804ae6f-f0dd-5512-98ec-1919b885f18a", "Roger Cummings", "a732f1cb-c2a3-5b46-a49f-e182a71d868f", false],
  ["ee9351ea-3d6d-57e7-9468-e71249aa8cc9", "William H Cummings", "b8e9e542-a05c-5a8d-9ca0-655fd3ca1e17", true],
  ["cc79d27f-746b-551a-b4d5-35c1abfb484c", "Elizabeth J Cummins", "7f0bb752-8587-5ef9-9add-5dba7931a919", false],
  ["13b0628a-0bd0-57c2-bbd7-a40b5e6a470d", "Henry C Cummins", "8ee95722-b294-548e-a142-a5a54fb92b2e", true],
  ["d8444a72-72b4-54c5-b131-15a637811455", "Melvin F Cummins", "12af4733-cafc-5b7c-b2a8-bc1bb3f13195", true],
  ["d1c5122a-7c7d-5237-9b65-cc3ffb4aab66", "Sidney S Cummins", "11b02412-64ca-5e30-9e4c-393eb7976f8c", true],
  ["381d5a12-46ea-5ec4-aed9-9fc4a8d09031", "Herman L Cundiff", "fc0c5bc1-6713-5365-8de6-905bc53f7b85", true],
  ["6410db31-25ff-5a9e-aa28-6fc568dedc13", "Ernest Cuneo", "541e94b8-2776-5d5b-83db-62c6bc12339e", false],
  ["13862ee6-458b-5f90-a0d1-410c6c63059b", "Julia Cuniberti", "875d1db4-9f58-5a19-ada9-0842c7ddd2d8", false],
  ["1b443cad-8daf-5025-bd02-166dc33aaca4", "Matthew J Cunic", "baa7977d-4d7c-5bc7-91cf-8d9d627d922d", true],
] as const;

test("Batch 507 preserves the audited page 101 sequence and masks every private identifier", () => {
  for (const [id, name, sourceRecordId, hasPrivateIdentifier] of cohort) {
    const person = profile(id);
    expect(person).toMatchObject({ display_name: name });
    const sourceRecord = person.source_records.find(
      (record: { source_record_id: string }) => record.source_record_id === sourceRecordId,
    );
    expect(sourceRecord).toMatchObject({
      box: "159",
      archive_location: "230/86/29/04",
      pdf_page: 101,
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

test("Batch 507 leaves unresolved and common-name alternatives unmerged", () => {
  for (const id of [
    "d804ae6f-f0dd-5512-98ec-1919b885f18a",
    "cc79d27f-746b-551a-b4d5-35c1abfb484c",
    "d1c5122a-7c7d-5237-9b65-cc3ffb4aab66",
  ]) {
    expect(profile(id)).toMatchObject({
      identity_status: "unresolved",
      research_status: "requires_archival_review",
      immediate_pre_oss_affiliations: [],
      last_civilian_pre_service: [],
      other_pre_oss_affiliations: [],
      claims: [],
    });
  }
  for (const id of [
    "ee9351ea-3d6d-57e7-9468-e71249aa8cc9",
    "13b0628a-0bd0-57c2-bbd7-a40b5e6a470d",
  ]) {
    expect(profile(id)).toMatchObject({
      identity_status: "ambiguous",
      research_status: "needs_identity_review",
      commissioned_officer: null,
      immediate_pre_oss_affiliations: [],
      last_civilian_pre_service: [],
      other_pre_oss_affiliations: [],
      claims: [],
    });
  }
});

test("Batch 507 confirms Melvin Cummins but does not project a post-OSS Army row backward", () => {
  const person = profile("d8444a72-72b4-54c5-b131-15a637811455");
  expect(person).toMatchObject({
    identity_status: "confirmed",
    personnel_category: "enlisted_army_personnel",
    commissioned_officer: false,
    research_status: "needs_temporal_review",
    immediate_pre_oss_affiliations: [],
    last_civilian_pre_service: [],
    other_pre_oss_affiliations: [],
  });
  expect(person.claims).toContainEqual(
    expect.objectContaining({
      claim_type: "identity",
      claim_confidence: "confirmed",
      temporal_assessment: expect.stringContaining("after OSS dissolution"),
    }),
  );
});

test("Batch 507 exposes Herman Cundiff's identifier-name conflict without selecting either row", () => {
  const person = profile("381d5a12-46ea-5ec4-aed9-9fc4a8d09031");
  expect(person).toMatchObject({
    identity_status: "conflicting",
    personnel_category: "unknown_or_indeterminate",
    commissioned_officer: null,
    research_status: "conflicting_sources",
    immediate_pre_oss_affiliations: [],
    last_civilian_pre_service: [],
    other_pre_oss_affiliations: [],
  });
  expect(person.claims).toContainEqual(
    expect.objectContaining({
      claim_type: "identity",
      claim_confidence: "conflicting",
      publication_status: "conflicting",
    }),
  );
});

test("Batch 507 keeps Cuneo's qualified DNC bridge separate from earlier work", () => {
  const cuneo = profile("6410db31-25ff-5a9e-aa28-6fc568dedc13");
  expect(cuneo).toMatchObject({
    identity_status: "confirmed",
    commissioned_officer: null,
    research_status: "documented_prewar_employer_found",
  });
  expect(cuneo.immediate_pre_oss_affiliations).toContainEqual(
    expect.objectContaining({
      canonical_organization: "Democratic National Committee",
      role_title: "Associate general counsel",
      start_date: "1936",
      end_date: "1940",
      temporal_basis: "probable_immediate",
      claim_confidence: "medium",
    }),
  );
  expect(cuneo.last_civilian_pre_service).toContainEqual(
    expect.objectContaining({ canonical_organization: "Democratic National Committee" }),
  );
  expect(cuneo.other_pre_oss_affiliations).toEqual(
    expect.arrayContaining([
      expect.objectContaining({
        canonical_organization: "New York Daily News",
        relationship_type: "employment",
      }),
      expect.objectContaining({
        canonical_organization: "Office of U.S. Representative Fiorello H. LaGuardia",
        relationship_type: "government_assignment",
      }),
    ]),
  );
});

test("Batch 507 models Cuniberti's Vassar path as student status, never employment", () => {
  const cuniberti = profile("13862ee6-458b-5f90-a0d1-410c6c63059b");
  expect(cuniberti).toMatchObject({
    identity_status: "confirmed",
    commissioned_officer: null,
    research_status: "completed",
    last_civilian_pre_service: [],
  });
  expect(cuniberti.immediate_pre_oss_affiliations).toContainEqual(
    expect.objectContaining({
      canonical_organization: "Vassar College",
      relationship_type: "student",
      end_date: "1944",
      temporal_basis: "strongly_date_bounded",
      claim_confidence: "high",
    }),
  );
  expect(cuniberti.immediate_pre_oss_affiliations).not.toContainEqual(
    expect.objectContaining({ relationship_type: "employment" }),
  );
});

test("Batch 507 publishes Cunic's exact occupation without inventing an employer", () => {
  const cunic = profile("1b443cad-8daf-5025-bd02-166dc33aaca4");
  expect(cunic).toMatchObject({
    identity_status: "confirmed",
    personnel_category: "enlisted_army_personnel",
    commissioned_officer: false,
    research_status: "occupation_only_found",
    immediate_pre_oss_affiliations: [],
    last_civilian_pre_service: [],
  });
  expect(cunic.other_pre_oss_affiliations).toContainEqual(
    expect.objectContaining({
      canonical_organization: null,
      relationship_type: "unknown",
      occupation: "Unskilled occupation in the manufacture of textiles, not elsewhere classified",
      end_date: "1942-10-09",
      claim_confidence: "high",
    }),
  );
});

test("Batch 507 exact coverage and direct routes expose evidence and uncertainty", async ({ page }) => {
  expect(stats.research_attempted_people).toBe(4838);
  expect(stats.verified_affiliation_people).toBe(553);
  expect(stats.verified_employer_people).toBe(246);
  expect(stats.archival_review_assessed_people).toBe(4793);

  await page.goto("./people/6410db31-25ff-5a9e-aa28-6fc568dedc13/");
  await expect(page.getByRole("heading", { name: "Ernest Cuneo", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("Democratic National Committee");
  await expect(page.locator("main")).toContainText("probable immediate");
  await expect(page.locator("main")).toContainText("New York Daily News");
  await expect(page.locator("main")).toContainText("A Tribute to Ernest L. Cuneo");

  await page.goto("./people/13862ee6-458b-5f90-a0d1-410c6c63059b/");
  await expect(page.getByRole("heading", { name: "Julia Cuniberti", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("Vassar College");
  await expect(page.locator("main")).toContainText("Student");
  await expect(page.locator("main")).toContainText("not as an employer");

  await page.goto("./people/381d5a12-46ea-5ec4-aed9-9fc4a8d09031/");
  await expect(page.getByRole("heading", { name: "Herman L Cundiff", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("evidence conflict");
  await expect(page.locator("main")).toContainText("Box 159");

  const dnc = organizations.find(
    (organization: { canonical_name: string }) =>
      organization.canonical_name === "Democratic National Committee",
  );
  await page.goto(`./organizations/${dnc.organization_id}/`);
  await expect(page.getByRole("heading", { name: "Democratic National Committee", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("Ernest Cuneo");
});
