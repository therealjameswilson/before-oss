import { expect, test } from "@playwright/test";
import fs from "node:fs";

const people = JSON.parse(
  fs.readFileSync(new URL("../src/data/generated/people.json", import.meta.url), "utf8"),
);
const profile = (id: string) =>
  people.find((person: { person_id: string }) => person.person_id === id);

const cohort = [
  ["a816e383-3c0f-548e-ba60-e2e30d344b52", "Theodore R Coverly", "8e94765b-4a2a-54ba-b7a3-c7b057f19309", 95, null],
  ["37e471b0-163d-53f8-a466-557d6a23730f", "Floyd R Covey", "7ad88d8e-27ec-57e4-9bcb-6d95c1c908ef", 95, "••••0832"],
  ["c94599de-c27e-506c-8ee1-ad643fa67ae9", "Albert P Coviello", "c94c78e4-2031-59a2-8a3b-e7ef72e5a056", 95, null],
  ["d9445583-30ad-50b4-b861-1e1a2a04ac3c", "John W Covill", "677c25ec-6e5e-58c1-ba8d-fa7082a9d832", 95, null],
  ["e00994e0-ec89-5096-a4e8-c4750cf859ef", "Richard L Covington", "0c735d6d-7f25-5700-a390-d39374196cd2", 95, null],
  ["5eb89e4f-84ed-5140-80c8-505ff8f5f6bd", "Richard O Covington", "8f1b3abe-7ad5-5f0e-b815-241aa491a80f", 95, null],
  ["d9e30e09-a093-5985-9aba-d2d10326c6e9", "Catherine Cowan", "30d4094c-e2c9-5aab-bcf7-07d49027a4cf", 95, null],
  ["d7f2dbb1-77f4-5b52-aaa6-502bb511489a", "George L Cowan", "bf19842d-b866-5fe5-a3a1-0a21776a63c1", 96, "••••4363"],
  ["91b1a11b-76b9-5993-a69c-419fa5e5e5aa", "John K Cowan", "9d8307a0-f661-57a2-ad85-1315d221e8e4", 96, "••••1532"],
  ["464aeb77-6009-5a6e-a25e-9ef7e6f462d3", "Joseph G Cowel", "36f5ddaf-d119-5f6d-bd26-801c9bb41c4e", 96, null],
] as const;

test("Batch 483 preserves the ten page 95-96 rows and masks private identifiers", () => {
  for (const [id, name, sourceRecordId, page, serial] of cohort) {
    const person = profile(id);
    expect(person).toMatchObject({ display_name: name });
    expect(person.source_records).toContainEqual(
      expect.objectContaining({
        source_record_id: sourceRecordId,
        serial_masked: serial,
        box: "149",
        archive_location: "230/86/29/03",
        pdf_page: page,
      }),
    );
    expect(JSON.stringify(person)).not.toMatch(
      /"serial_number"|"serial_number_raw"|"serial_number_normalized"/,
    );
  }
});

test("Batch 483 leaves all ten identities and affiliations unresolved", () => {
  for (const [id] of cohort) {
    expect(profile(id)).toMatchObject({
      identity_status: "unresolved",
      research_status: "requires_archival_review",
      personnel_category: "unknown_or_indeterminate",
      commissioned_officer: null,
      manual_review_required: true,
      immediate_pre_oss_affiliations: [],
      last_civilian_pre_service: [],
      other_pre_oss_affiliations: [],
      claims: [],
    });
  }
});

test("Batch 483 does not transfer name-only Army or institutional candidates", () => {
  for (const id of [
    "a816e383-3c0f-548e-ba60-e2e30d344b52",
    "e00994e0-ec89-5096-a4e8-c4750cf859ef",
    "d7f2dbb1-77f4-5b52-aaa6-502bb511489a",
    "91b1a11b-76b9-5993-a69c-419fa5e5e5aa",
    "5eb89e4f-84ed-5140-80c8-505ff8f5f6bd",
    "d9e30e09-a093-5985-9aba-d2d10326c6e9",
  ]) {
    const person = profile(id);
    expect(person.other_pre_oss_affiliations).toEqual([]);
    expect(person.personnel_category).toBe("unknown_or_indeterminate");
    expect(person.commissioned_officer).toBeNull();
  }
});

test("Batch 483 renders John W Covill as a critical archival-review case", async ({ page }) => {
  await page.goto("./people/d9445583-30ad-50b4-b861-1e1a2a04ac3c/");
  await expect(page.getByRole("heading", { name: "John W Covill", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("No reliable pre-OSS employer has yet been identified");
  await expect(page.locator("main")).toContainText("Box 149");
  await expect(page.locator("main")).toContainText("USAAF prisoner-of-war namesake");
  await expect(page.locator("main")).toContainText("critical");
});
