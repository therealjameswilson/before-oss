import { expect, test } from "@playwright/test";
import fs from "node:fs";

const people = JSON.parse(
  fs.readFileSync(new URL("../src/data/generated/people.json", import.meta.url), "utf8"),
);
const profile = (id: string) =>
  people.find((person: { person_id: string }) => person.person_id === id);

test("Batch 449 publishes two Army-entry occupations without inventing employers", async ({ page }) => {
  const cases = [
    {
      id: "57cba9ec-d5d8-5aeb-8363-0da6fbaeb664",
      name: "Joseph F Comerford",
      occupation: "Actors and actresses",
      endDate: "1943-02-20",
    },
    {
      id: "58c34b81-440c-545a-bde8-24b50379cdd5",
      name: "Adolph Commodaro",
      occupation: "Tailors and tailoresses",
      endDate: "1943-05-10",
    },
  ];

  for (const item of cases) {
    const person = profile(item.id);
    expect(person).toMatchObject({
      display_name: item.name,
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
        occupation: item.occupation,
        relationship_type: "unknown",
        end_date: item.endDate,
        temporal_basis: "strongly_date_bounded",
        identity_confidence: "confirmed",
        claim_confidence: "medium",
      }),
    );

    await page.goto(`./people/${person.person_id}/`);
    await expect(page.getByRole("heading", { name: item.name, exact: true })).toBeVisible();
    await expect(page.locator("main")).toContainText(item.occupation);
    await expect(page.locator("main")).toContainText(
      "No reliable pre-OSS employer has yet been identified",
    );
  }
});

test("Batch 449 qualifies Cominos Hotel as a last-civilian candidate", async ({ page }) => {
  const nicholas = profile("9b00e31b-d4c5-5b15-bfd6-5af1038f4710");
  expect(nicholas).toMatchObject({
    display_name: "Nicholas H Cominos",
    identity_status: "high_confidence",
    personnel_category: "enlisted_army_personnel",
    commissioned_officer: false,
    research_status: "documented_prewar_employer_found",
  });
  expect(nicholas.immediate_pre_oss_affiliations).toEqual([]);
  expect(nicholas.last_civilian_pre_service).toContainEqual(
    expect.objectContaining({
      canonical_organization: "Cominos Hotel",
      organization_name_as_found: "Cominos Hotel",
      role_title: null,
      occupation: null,
      relationship_type: "employment",
      city: "Salinas",
      state_or_region: "California",
      last_civilian_pre_service: true,
      temporal_basis: "probable_immediate",
      identity_confidence: "high_confidence",
      claim_confidence: "medium",
    }),
  );

  await page.goto(`./people/${nicholas.person_id}/`);
  await expect(page.getByRole("heading", { name: "Nicholas H Cominos", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("Cominos Hotel");
  await expect(page.locator("main")).toContainText("best-supported candidate");
  await expect(page.locator("main")).toContainText("an intervening job cannot yet be excluded");
});

test("Batch 449 exposes Comfort's identifier conflict and Combs's temporal conflict", async ({ page }) => {
  const howard = profile("674a849d-f4d3-5f41-9e12-edc608d9ba71");
  expect(howard).toMatchObject({
    display_name: "Howard G Comfort",
    identity_status: "high_confidence",
    personnel_category: "commissioned_army_officer",
    commissioned_officer: true,
    research_status: "needs_identity_review",
  });
  expect(howard.immediate_pre_oss_affiliations).toEqual([]);
  expect(howard.last_civilian_pre_service).toEqual([]);
  expect(howard.other_pre_oss_affiliations).toEqual([]);
  await page.goto(`./people/${howard.person_id}/`);
  await expect(page.locator("main")).toContainText("unresolved identifier conflict");
  await expect(page.locator("main")).toContainText("transposes digits");
  await expect(page.locator("main")).toContainText("Review Box 136");

  const albert = profile("2ead8a89-e0f0-56c3-8de8-0f23c1045691");
  expect(albert).toMatchObject({
    display_name: "Albert R Combs",
    identity_status: "high_confidence",
    personnel_category: "enlisted_army_personnel",
    commissioned_officer: false,
    research_status: "needs_temporal_review",
  });
  expect(albert.other_pre_oss_affiliations).toEqual([]);
  await page.goto(`./people/${albert.person_id}/`);
  await expect(page.locator("main")).toContainText("unresolved post-OSS chronology");
  await expect(page.locator("main")).toContainText("1 February 1946");
  await expect(page.locator("main")).toContainText("value 000");
});

test("Batch 449 preserves all ten printed rows, foreign status and unresolved cases", async ({ page }) => {
  const expected = [
    ["2ead8a89-e0f0-56c3-8de8-0f23c1045691", "Albert R Combs", "4f3be055-e1cb-59a4-a133-b04b420f5b97", 8, null],
    ["aab31c89-345f-56ba-be59-3aa1d50b6aa9", "George I Combs", "c7c49a7e-7dc6-56ac-81d9-1f65328a03ec", 0, null],
    ["0a3ccd94-3eb1-5ee9-bdfb-d7d4f7ac1ec7", "Lorna M Combs", "84037087-4546-56ef-b405-fbb219217ce5", 0, null],
    ["57cba9ec-d5d8-5aeb-8363-0da6fbaeb664", "Joseph F Comerford", "41652cae-7fa3-59cc-9cc2-88d7b3607f72", 8, null],
    ["674a849d-f4d3-5f41-9e12-edc608d9ba71", "Howard G Comfort", "ead79339-43a0-5ef6-8048-37158e1ef87c", 7, null],
    ["9b00e31b-d4c5-5b15-bfd6-5af1038f4710", "Nicholas H Cominos", "d7d1fe45-8da6-5b26-b854-05f1efeaef18", 0, null],
    ["fb9895b1-1c66-5f31-8d59-117d9eb6147f", "Michael Commelin", "98d9e664-9852-5324-97c1-2db947ed9802", 0, null],
    ["58c34b81-440c-545a-bde8-24b50379cdd5", "Adolph Commodaro", "de93e9f4-e5f1-50c5-ba64-dee8bc0e5d5c", 8, null],
    ["4ddd4155-b001-5e35-9037-2d3a6fdea92c", "Mattiie H Commodore", "958111f8-a3ec-5fac-a02d-68dfe63e8d60", 0, null],
    ["a0b4bf98-5131-5b5d-9800-91eade00ed3d", "Raymond Compain", "86fd7960-125b-5db8-82e9-29e41e38b7b7", 0, "French"],
  ];

  for (const [id, name, sourceRecordId, serialLength, note] of expected) {
    const person = profile(String(id));
    expect(person).toMatchObject({ display_name: name });
    expect(person.source_records[0]).toMatchObject({
      source_record_id: sourceRecordId,
      box: "136",
      notes_as_indexed: note,
      archive_location: "230/86/29/01",
      pdf_page: 88,
    });
    if (serialLength) {
      expect(person.source_records[0].serial_masked).toMatch(/^••••.{4}$/u);
    } else {
      expect(person.source_records[0].serial_masked).toBeNull();
    }
    expect(JSON.stringify(person)).not.toMatch(
      /"serial_number"|"serial_number_raw"|"serial_number_normalized"/,
    );
  }

  for (const id of [
    "aab31c89-345f-56ba-be59-3aa1d50b6aa9",
    "0a3ccd94-3eb1-5ee9-bdfb-d7d4f7ac1ec7",
    "fb9895b1-1c66-5f31-8d59-117d9eb6147f",
    "4ddd4155-b001-5e35-9037-2d3a6fdea92c",
  ]) {
    const person = profile(id);
    expect(person.identity_status).toBe("unresolved");
    expect(person.research_status).toBe("requires_archival_review");
    expect(person.claims).toEqual([]);
    expect(person.immediate_pre_oss_affiliations).toEqual([]);
    expect(person.last_civilian_pre_service).toEqual([]);
    expect(person.other_pre_oss_affiliations).toEqual([]);
  }

  const mattiie = profile("4ddd4155-b001-5e35-9037-2d3a6fdea92c");
  expect(mattiie.name_variants).not.toContain("Mattie H Commodore");
  await page.goto(`./people/${mattiie.person_id}/`);
  await expect(page.getByRole("heading", { name: "Mattiie H Commodore", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("double-i given name");

  const raymond = profile("a0b4bf98-5131-5b5d-9800-91eade00ed3d");
  expect(raymond).toMatchObject({
    identity_status: "high_confidence",
    personnel_category: "temporary_contract_or_special_personnel",
    commissioned_officer: false,
    allied_or_foreign_personnel: true,
    research_status: "requires_archival_review",
  });
  expect(raymond.immediate_pre_oss_affiliations).toEqual([]);
  expect(raymond.last_civilian_pre_service).toEqual([]);
  expect(raymond.other_pre_oss_affiliations).toEqual([]);
  await page.goto(`./people/${raymond.person_id}/`);
  await expect(page.locator("main")).toContainText("OSS Team HERMIT bodyguard");
  await expect(page.locator("main")).toContainText(
    "No reliable pre-OSS employer has yet been identified",
  );
});
