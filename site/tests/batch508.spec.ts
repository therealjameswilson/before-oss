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
  ["dd734ae4-ed0e-51df-bf2b-1e5759024729", "Ramon C Cunill", "2ca476a4-9389-56f3-b44b-7810b553275e", false],
  ["fd011bc3-c3af-5547-8641-6f36ccd25e3e", "Riuth M Cunniff", "1b2a3efd-b27b-55ca-ad89-e54f690fa342", false],
  ["46d54464-8581-521e-b94c-239018415abb", "Anvilla P Cunningham", "17396b55-6ed8-56fb-a530-52b54297b340", false],
  ["05fc645a-dae3-5ada-8b8f-d1a681ecdf80", "Clotilde Cunningham", "c0567fcd-76a8-5172-9e4c-7013a56736ff", false],
  ["73315998-3b98-55c0-854d-afe2ab43132f", "Harry G Cunningham", "5a8d2d52-65fe-5efd-a3e1-05f7f760ef76", false],
  ["2939af6b-c9d2-5e74-9515-de0e7c3424f2", "Helen M Cunningham", "f0a94557-b814-584c-be95-6eef33ffcb34", false],
  ["a2e4f241-c7b2-5fe7-ae82-e8645ad37600", "Hugh T Cunningham", "62d4efcd-e5e0-5d7b-82ca-7e281bba3a75", true],
  ["b5311c26-27c0-5c05-a4d1-664b14feb224", "Jane Cunningham", "1e2d275b-09c0-513f-bbe2-1be749623ceb", false],
  ["abb39e42-7be1-5506-8442-6883fc00a626", "Joan Cunningham", "974d9d91-5869-5120-859a-b577fa8858f5", false],
  ["74e34291-be64-5d97-8d0b-7331c2e24fd6", "Lou Cunningham", "ee30d12f-ed1a-56f2-9fbc-f6f123d270ae", false],
] as const;

test("Batch 508 preserves the audited page 101 sequence and masks the private identifier", () => {
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

test("Batch 508 leaves seven unsupported identities unresolved and without affiliations", () => {
  for (const id of [
    "dd734ae4-ed0e-51df-bf2b-1e5759024729",
    "fd011bc3-c3af-5547-8641-6f36ccd25e3e",
    "46d54464-8581-521e-b94c-239018415abb",
    "05fc645a-dae3-5ada-8b8f-d1a681ecdf80",
    "b5311c26-27c0-5c05-a4d1-664b14feb224",
    "abb39e42-7be1-5506-8442-6883fc00a626",
    "74e34291-be64-5d97-8d0b-7331c2e24fd6",
  ]) {
    expect(profile(id)).toMatchObject({
      identity_status: "unresolved",
      research_status: "requires_archival_review",
      commissioned_officer: null,
      immediate_pre_oss_affiliations: [],
      last_civilian_pre_service: [],
      other_pre_oss_affiliations: [],
      claims: [],
    });
  }
});

test("Batch 508 retains Harry, Helen, and Hugh Cunningham as unmerged identity alternatives", () => {
  for (const id of [
    "73315998-3b98-55c0-854d-afe2ab43132f",
    "2939af6b-c9d2-5e74-9515-de0e7c3424f2",
    "a2e4f241-c7b2-5fe7-ae82-e8645ad37600",
  ]) {
    expect(profile(id)).toMatchObject({
      identity_status: "ambiguous",
      research_status: "needs_identity_review",
      personnel_category: "unknown_or_indeterminate",
      commissioned_officer: null,
      immediate_pre_oss_affiliations: [],
      last_civilian_pre_service: [],
      other_pre_oss_affiliations: [],
      claims: [],
    });
  }
  expect(profile("73315998-3b98-55c0-854d-afe2ab43132f").next_action).toContain(
    "before selecting an Army or technical-career namesake",
  );
  expect(profile("2939af6b-c9d2-5e74-9515-de0e7c3424f2").next_action).toContain(
    "before choosing either WAC candidate",
  );
  expect(profile("a2e4f241-c7b2-5fe7-ae82-e8645ad37600").next_action).toContain(
    "before accepting the exact-name Army row or any postwar CIA namesake",
  );
});

test("Batch 508 preserves Riuth as indexed and marks Ruth only as a searchable variant", () => {
  const cunniff = profile("fd011bc3-c3af-5547-8641-6f36ccd25e3e");
  expect(cunniff.display_name).toBe("Riuth M Cunniff");
  expect(cunniff.name_variants).toEqual(
    expect.arrayContaining(["Cunniff, Riuth M", "Riuth M. Cunniff", "Ruth M. Cunniff"]),
  );
  expect(cunniff.source_records[0]).toMatchObject({
    indexed_first_name: "Riuth",
    indexed_middle: "M",
  });
  expect(cunniff.next_action).toContain("whether Riuth is the intended spelling");
});

test("Batch 508 exact coverage and direct routes expose uncertainty and archival next actions", async ({ page }) => {
  expect(stats.research_attempted_people).toBe(4848);
  expect(stats.verified_affiliation_people).toBe(553);
  expect(stats.verified_employer_people).toBe(246);
  expect(stats.archival_review_assessed_people).toBe(4803);

  await page.goto("./people/73315998-3b98-55c0-854d-afe2ab43132f/");
  await expect(page.getByRole("heading", { name: "Harry G Cunningham", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("needs identity review");
  await expect(page.locator("main")).toContainText("technical-career namesake");
  await expect(page.locator("main")).toContainText("Box 159");

  await page.goto("./people/fd011bc3-c3af-5547-8641-6f36ccd25e3e/");
  await expect(page.getByRole("heading", { name: "Riuth M Cunniff", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("Ruth M. Cunniff");
  await expect(page.locator("main")).toContainText("requires archival review");

  await page.goto("./people/a2e4f241-c7b2-5fe7-ae82-e8645ad37600/");
  await expect(page.getByRole("heading", { name: "Hugh T Cunningham", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("••••3096");
  await expect(page.locator("main")).not.toContainText("Director of Training");
});
