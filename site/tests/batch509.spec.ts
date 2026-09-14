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
  ["de448054-0021-5fc6-94fa-a312c9908aef", "Mary Cunningham", "e77dd03a-7b94-5342-8125-86c294e587db", "159", false],
  ["4a75e2bd-9dab-55fc-b563-55f42ae7a51c", "Murray O Cunningham", "861d047f-32f9-5101-8a8a-9f975b6088e7", "159", true],
  ["92db86fe-1c64-552f-970f-949bc27f0fe8", "Richard H Cunningham", "fb829a6a-e331-52a0-b0d6-183ed2a0ac74", "159", false],
  ["859aebb1-c063-5dec-b2d5-1a27dd7cada9", "Robert H Cunningham", "28d696c4-d1eb-536d-88a6-7cdef8f5cdd0", "159", false],
  ["058b87e4-831c-5e8c-9adc-2d5e5e1722a5", "Robert J Cunningham", "6672399d-5365-5fda-bfd0-a10a11416a6a", "159", false],
  ["9dc73e3e-13ee-53c5-995c-8678b61c7099", "Robert A Cunningham", "7f72bb03-9284-57ba-968f-cf2bb17e2019", "159", true],
  ["d9295ea7-bce5-5ccf-9400-29626e637b36", "Roy H Cunningham", "12af01ac-cf67-58b2-916b-e7c4dabd6317", "160", false],
  ["7ec0bc66-f6bf-579d-ba9f-f1e5baac1b38", "Walter W Cunningham", "1f48946e-e88a-5f3f-bfc5-791b85b89c6d", "160", false],
  ["335eeb04-1eb1-5853-91ca-48805b83ff33", "Alberto Cupelli", "85ba5687-014d-5782-9022-9c91cf375b48", "160", false],
  ["b382f404-d7c8-54f5-8114-65733013cfb2", "Sanford C Curcie", "13cfdd8d-7d5b-5b2f-82d6-aea40100ee99", "160", false],
] as const;

test("Batch 509 preserves the audited page 101 sequence, box boundary, and private-field masking", () => {
  for (const [id, name, sourceRecordId, box, hasPrivateIdentifier] of cohort) {
    const person = profile(id);
    expect(person).toMatchObject({ display_name: name });
    const sourceRecord = person.source_records.find(
      (record: { source_record_id: string }) => record.source_record_id === sourceRecordId,
    );
    expect(sourceRecord).toMatchObject({
      box,
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

test("Batch 509 publishes Murray Cunningham's qualified occupation without inventing an employer", () => {
  const murray = profile("4a75e2bd-9dab-55fc-b563-55f42ae7a51c");
  expect(murray).toMatchObject({
    identity_status: "confirmed",
    personnel_category: "enlisted_army_personnel",
    commissioned_officer: false,
    research_status: "occupation_only_found",
    immediate_pre_oss_affiliations: [],
    last_civilian_pre_service: [],
  });
  expect(murray.other_pre_oss_affiliations).toHaveLength(1);
  expect(murray.other_pre_oss_affiliations[0]).toMatchObject({
    occupation: "Photographers",
    relationship_type: "unknown",
    end_date: "1942-09-15",
    temporal_basis: "strongly_date_bounded",
    claim_confidence: "medium",
    publication_status: "publish_qualified",
  });
  expect(murray.other_pre_oss_affiliations[0]).toMatchObject({
    organization_id: null,
    canonical_organization: null,
    historical_organization: null,
    organization_name_as_found: null,
  });
  expect(murray.claims.map((claim: { claim_type: string }) => claim.claim_type)).toEqual([
    "identity",
    "occupation",
  ]);
});

test("Batch 509 retains six common-name or rank-dependent identities as unmerged alternatives", () => {
  for (const id of [
    "92db86fe-1c64-552f-970f-949bc27f0fe8",
    "859aebb1-c063-5dec-b2d5-1a27dd7cada9",
    "058b87e4-831c-5e8c-9adc-2d5e5e1722a5",
    "9dc73e3e-13ee-53c5-995c-8678b61c7099",
    "d9295ea7-bce5-5ccf-9400-29626e637b36",
    "7ec0bc66-f6bf-579d-ba9f-f1e5baac1b38",
  ]) {
    expect(profile(id)).toMatchObject({
      identity_status: "ambiguous",
      research_status: "needs_identity_review",
      immediate_pre_oss_affiliations: [],
      last_civilian_pre_service: [],
      other_pre_oss_affiliations: [],
      claims: [],
    });
  }
  expect(profile("d9295ea7-bce5-5ccf-9400-29626e637b36")).toMatchObject({
    personnel_category: "commissioned_army_officer",
    commissioned_officer: true,
  });
  expect(profile("9dc73e3e-13ee-53c5-995c-8678b61c7099").next_action).toContain(
    "converted-file non-hit is not negative proof",
  );
});

test("Batch 509 leaves three unsupported identities unresolved and without affiliations", () => {
  for (const id of [
    "de448054-0021-5fc6-94fa-a312c9908aef",
    "335eeb04-1eb1-5853-91ca-48805b83ff33",
    "b382f404-d7c8-54f5-8114-65733013cfb2",
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

test("Batch 509 exact coverage and direct routes expose the supported occupation and uncertainty", async ({ page }) => {
  expect(stats.research_attempted_people).toBe(4858);
  expect(stats.verified_affiliation_people).toBe(553);
  expect(stats.verified_employer_people).toBe(246);
  expect(stats.archival_review_assessed_people).toBe(4813);

  await page.goto("./people/4a75e2bd-9dab-55fc-b563-55f42ae7a51c/");
  await expect(page.getByRole("heading", { name: "Murray O Cunningham", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("Photographers");
  await expect(page.locator("main")).toContainText("September 15, 1942");
  await expect(page.locator("main")).toContainText("medium strongly date bounded");
  await expect(page.locator("main")).not.toContainText("Studio:");

  await page.goto("./people/d9295ea7-bce5-5ccf-9400-29626e637b36/");
  await expect(page.getByRole("heading", { name: "Roy H Cunningham", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("commissioned army officer");
  await expect(page.locator("main")).toContainText("needs identity review");
  await expect(page.locator("main")).toContainText("Box 160");

  await page.goto("./people/335eeb04-1eb1-5853-91ca-48805b83ff33/");
  await expect(page.getByRole("heading", { name: "Alberto Cupelli", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("requires archival review");
  await expect(page.locator("main")).not.toContainText("Il Mondo");
});
