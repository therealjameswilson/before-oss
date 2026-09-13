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
  ["315f8f64-6115-50b6-8f07-4fafd29a70a1", "Diana I Croft", "6db1fe0c-079f-5786-98f9-360c099dfbf9", 98, "154", "230/86/29/03", false],
  ["3d601abe-c984-570f-84bd-bd36cd9ca85b", "Eddie L Croft", "2784c98a-4dc4-5361-8e96-82c40e536506", 98, "154", "230/86/29/03", true],
  ["18c20146-0957-5946-9b1d-d114c65f0524", "Diana Crofts", "efe75554-95e6-5352-9ce1-0f0a86d6c162", 98, "154", "230/86/29/03", false],
  ["22582e41-dd9e-549c-896a-132367459329", "Robert J Croken", "7947358a-708c-5150-aa19-318cb4afc4f7", 98, "155", "230/86/29/04", true],
  ["d98e0f3f-5bf2-5b5d-ab73-2065675b2b94", "Ann Crolius", "93143305-1c5e-5e74-99c6-e7c76d1fb30b", 98, "155", "230/86/29/04", false],
  ["3dd2078c-b1ea-5887-b1eb-1013dbf33f67", "Jeannette P Crolius", "3857ac05-70be-5c6d-8fd1-40761a6cb75e", 99, "155", "230/86/29/04", false],
  ["c41cec88-865a-543f-8c82-c7ea5fb65323", "Anne B Croliuus", "d8d67b75-3b33-550e-9257-ad4792e1ec72", 99, "155", "230/86/29/04", false],
  ["e2e60763-e561-568d-88be-53e09dd4584c", "Joseph D Croll", "487353a3-04df-500a-82e5-52aae0151980", 99, "155", "230/86/29/04", false],
  ["dfbc4fd2-abb7-5389-a684-91a648b71e43", "Flavus Cromeans", "2b658e49-3c1f-5fca-81c5-5ff6ed9c472d", 99, "155", "230/86/29/04", true],
  ["9756f9b4-ba4f-56d7-b2d6-2a0ba73e5ed5", "Russell H Cromes", "542d7621-6138-57d2-9642-78f106f77bc1", 99, "155", "230/86/29/04", true],
] as const;

test("Batch 497 preserves all ten page 98-99 rows and masks every printed identifier", () => {
  for (const [id, name, sourceRecordId, page, box, location, hasPrivateIdentifier] of cohort) {
    const person = profile(id);
    expect(person).toMatchObject({ display_name: name });
    const sourceRecord = person.source_records.find(
      (record: { source_record_id: string }) => record.source_record_id === sourceRecordId,
    );
    expect(sourceRecord).toMatchObject({ box, archive_location: location, pdf_page: page });
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

test("Batch 497 publishes four qualified occupations without inventing employers", () => {
  const occupations = new Map([
    ["3d601abe-c984-570f-84bd-bd36cd9ca85b", "Roofers and slaters"],
    ["22582e41-dd9e-549c-896a-132367459329", "Metallurgists, assayers, and chemists"],
    ["dfbc4fd2-abb7-5389-a684-91a648b71e43", "General farmers"],
    ["9756f9b4-ba4f-56d7-b2d6-2a0ba73e5ed5", "Pressmen and plate printers, printing"],
  ]);

  for (const [id, occupation] of occupations) {
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
        canonical_organization: null,
        occupation,
        relationship_type: "unknown",
        temporal_basis: "documented_prewar",
        claim_confidence: "medium",
        publication_status: "publish_qualified",
      }),
    );
  }
});

test("Batch 497 keeps duplicate and spelling conflicts visible", () => {
  const dianaCroft = profile("315f8f64-6115-50b6-8f07-4fafd29a70a1");
  const dianaCrofts = profile("18c20146-0957-5946-9b1d-d114c65f0524");
  for (const person of [dianaCroft, dianaCrofts]) {
    expect(person).toMatchObject({
      identity_status: "ambiguous",
      research_status: "needs_identity_review",
      claims: [],
      immediate_pre_oss_affiliations: [],
      last_civilian_pre_service: [],
      other_pre_oss_affiliations: [],
    });
    expect(person.possible_duplicate_group).toBeTruthy();
  }
  expect(dianaCroft.person_id).not.toBe(dianaCrofts.person_id);
  expect(dianaCroft.possible_duplicate_group).toBe(dianaCrofts.possible_duplicate_group);

  const russell = profile("9756f9b4-ba4f-56d7-b2d6-2a0ba73e5ed5");
  expect(russell.name_variants).toContain("Russell H. Cromez");
  expect(russell.identity_evidence).toContain("Cromez");

  const anne = profile("c41cec88-865a-543f-8c82-c7ea5fb65323");
  expect(anne).toMatchObject({
    display_name: "Anne B Croliuus",
    identity_status: "unresolved",
    research_status: "needs_identity_review",
    claims: [],
  });
  expect(anne.name_variants).not.toContain("Anne B. Crolius");
});

test("Batch 497 retains clean unresolved profiles for archival review", () => {
  for (const id of [
    "d98e0f3f-5bf2-5b5d-ab73-2065675b2b94",
    "3dd2078c-b1ea-5887-b1eb-1013dbf33f67",
    "e2e60763-e561-568d-88be-53e09dd4584c",
  ]) {
    expect(profile(id)).toMatchObject({
      identity_status: "unresolved",
      personnel_category: "unknown_or_indeterminate",
      commissioned_officer: null,
      research_status: "requires_archival_review",
      immediate_pre_oss_affiliations: [],
      last_civilian_pre_service: [],
      other_pre_oss_affiliations: [],
      claims: [],
    });
  }
});

test("Batch 497 direct routes show evidence qualifications and current coverage", async ({ page }) => {
  expect(stats.research_attempted_people).toBeGreaterThanOrEqual(4738);
  expect(stats.verified_affiliation_people).toBeGreaterThanOrEqual(541);
  expect(stats.verified_employer_people).toBeGreaterThanOrEqual(241);
  expect(stats.archival_review_assessed_people).toBeGreaterThanOrEqual(4693);

  await page.goto("./people/3d601abe-c984-570f-84bd-bd36cd9ca85b/");
  await expect(page.getByRole("heading", { name: "Eddie L Croft", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("Roofers and slaters");
  await expect(page.locator("main")).toContainText("no employer");

  await page.goto("./people/22582e41-dd9e-549c-896a-132367459329/");
  await expect(page.getByRole("heading", { name: "Robert J Croken", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("Metallurgists, assayers, and chemists");

  await page.goto("./people/9756f9b4-ba4f-56d7-b2d6-2a0ba73e5ed5/");
  await expect(page.getByRole("heading", { name: "Russell H Cromes", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("Russell H. Cromez");
  await expect(page.locator("main")).toContainText("Pressmen and plate printers, printing");

  await page.goto("./people/315f8f64-6115-50b6-8f07-4fafd29a70a1/");
  await expect(page.getByRole("heading", { name: "Diana I Croft", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("Duplicate group");
  await expect(page.locator("main")).toContainText("No publishable pre-OSS affiliation is recorded yet");

  expect(profile("777d3cb7-f27d-59ee-95f9-10f447f4f70a")).toMatchObject({
    display_name: "Raymond A Cromley",
    research_status: "not_started",
  });
});
