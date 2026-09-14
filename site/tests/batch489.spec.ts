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
  ["1247422d-36ba-5230-8bb1-02f82fd609b0", "Mary J Craig", "8dec8d5b-fdd3-5a2e-a032-4aa6f7cdcba8", "151", false],
  ["e6fd6469-f6a7-5cea-90c0-a3b50bb58c1f", "Nelson Craig", "3bc5c5b9-ed57-52b5-b40a-4376893b0c14", "151", true],
  ["424db092-142e-5233-a946-607358c39d04", "Robert B Craig", "671cd94d-dbee-589f-ae27-3037299874f3", "152", false],
  ["be38446c-5707-55f2-a991-0525a1a2dd5e", "Robert B Craig", "1d4e6e59-819f-5286-b02b-30ce5e3c983c", "151", true],
  ["b79c9a99-7bc9-51d3-84ff-4113e13fbfc0", "Roger P Craig", "87a5bdc4-ad39-586b-97ed-460ae6de49e9", "151", true],
  ["dca47f1b-4a54-5422-b5c3-627e3e71842a", "William C Craig", "326c22d5-9251-5ddc-ab30-5b86eaccbee9", "151", true],
  ["8c31616c-f212-5f38-8cdb-38cbef29f4fa", "Richard J Craigo", "52df9616-3d69-5727-b045-c3b8fd6b9c62", "151", true],
  ["6d084d0a-a719-5acf-af6c-7eefe11028d9", "Richard Craigue", "36a58159-6bfc-5d94-8c0b-2a7016690d1d", "151", false],
  ["f661f7b1-56ed-537b-b647-cede4101ef2f", "Mary L Crain", "e0921ece-878e-5929-959f-4af73fc672e7", "151", false],
  ["6b7d0736-f74a-5585-8e09-54a794681eb6", "Arvid H Craker", "19907670-de12-50f9-90e0-3363936dda83", "151", true],
] as const;

test("Batch 489 preserves all ten page 97 rows and masks every printed identifier", () => {
  for (const [id, name, sourceRecordId, box, hasPrivateIdentifier] of cohort) {
    const person = profile(id);
    expect(person).toMatchObject({ display_name: name });
    const sourceRecord = person.source_records.find(
      (record: { source_record_id: string }) => record.source_record_id === sourceRecordId,
    );
    expect(sourceRecord).toMatchObject({
      box,
      archive_location: "230/86/29/03",
      pdf_page: 97,
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

test("Batch 489 publishes only identifier-supported Army-entry occupations", () => {
  const expected = [
    ["be38446c-5707-55f2-a991-0525a1a2dd5e", "confirmed", "Mechanical engineers", "1943-09-13"],
    ["b79c9a99-7bc9-51d3-84ff-4113e13fbfc0", "confirmed", "Authors, editors, and reporters", "1944-03-18"],
    ["dca47f1b-4a54-5422-b5c3-627e3e71842a", "confirmed", "Photoengravers", "1943-04-05"],
    ["8c31616c-f212-5f38-8cdb-38cbef29f4fa", "high_confidence", "Managers and officials, not elsewhere classified", "1941-12-08"],
  ] as const;

  for (const [id, identityStatus, occupation, endDate] of expected) {
    const person = profile(id);
    expect(person).toMatchObject({
      identity_status: identityStatus,
      personnel_category: "enlisted_army_personnel",
      commissioned_officer: false,
      research_status: "occupation_only_found",
      immediate_pre_oss_affiliations: [],
      last_civilian_pre_service: [],
    });
    expect(person.other_pre_oss_affiliations).toContainEqual(
      expect.objectContaining({
        occupation,
        end_date: endDate,
        relationship_type: "unknown",
        temporal_basis: "strongly_date_bounded",
        claim_confidence: "medium",
      }),
    );
    expect(person.claims).toContainEqual(
      expect.objectContaining({
        claim_type: "occupation",
        claim_confidence: "medium",
        publication_status: "publish_qualified",
      }),
    );
  }
});

test("Batch 489 keeps unsupported identities unresolved and does not infer officer status", () => {
  for (const id of [
    "1247422d-36ba-5230-8bb1-02f82fd609b0",
    "e6fd6469-f6a7-5cea-90c0-a3b50bb58c1f",
    "424db092-142e-5233-a946-607358c39d04",
    "6d084d0a-a719-5acf-af6c-7eefe11028d9",
    "f661f7b1-56ed-537b-b647-cede4101ef2f",
    "6b7d0736-f74a-5585-8e09-54a794681eb6",
  ]) {
    const person = profile(id);
    expect(person).toMatchObject({
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

test("Batch 489 exposes but never merges both plausible duplicate pairs", () => {
  const robertBox152 = profile("424db092-142e-5233-a946-607358c39d04");
  const robertBox151 = profile("be38446c-5707-55f2-a991-0525a1a2dd5e");
  expect(robertBox152.possible_duplicate_group).toBeTruthy();
  expect(robertBox152.possible_duplicate_group).toBe(robertBox151.possible_duplicate_group);
  expect(robertBox152.person_id).not.toBe(robertBox151.person_id);

  const craigo = profile("8c31616c-f212-5f38-8cdb-38cbef29f4fa");
  const craigue = profile("6d084d0a-a719-5acf-af6c-7eefe11028d9");
  expect(craigo.possible_duplicate_group).toBeTruthy();
  expect(craigo.possible_duplicate_group).toBe(craigue.possible_duplicate_group);
  expect(craigo.person_id).not.toBe(craigue.person_id);
});

test("Batch 489 profiles render qualified evidence and updated coverage", async ({ page }) => {
  expect(stats.research_attempted_people).toBeGreaterThanOrEqual(4658);
  expect(stats.verified_affiliation_people).toBeGreaterThanOrEqual(533);
  expect(stats.verified_employer_people).toBeGreaterThanOrEqual(236);
  expect(stats.archival_review_assessed_people).toBeGreaterThanOrEqual(4613);

  await page.goto("./people/be38446c-5707-55f2-a991-0525a1a2dd5e/");
  await expect(page.getByRole("heading", { name: "Robert B Craig", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("Mechanical engineers");
  await expect(page.locator("main")).toContainText("no employer is named");
  await expect(page.locator("main")).toContainText("Keep the Box 152 namesake separate");

  await page.goto("./people/8c31616c-f212-5f38-8cdb-38cbef29f4fa/");
  await expect(page.getByRole("heading", { name: "Richard J Craigo", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("Managers and officials");
  await expect(page.locator("main")).toContainText("CRA GO RICHARD J");

  await page.goto("./people/6d084d0a-a719-5acf-af6c-7eefe11028d9/");
  await expect(page.getByRole("heading", { name: "Richard Craigue", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("No reliable pre-OSS employer has yet been identified");
});
