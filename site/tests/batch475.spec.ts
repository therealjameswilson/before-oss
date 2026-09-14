import { expect, test } from "@playwright/test";
import fs from "node:fs";

const people = JSON.parse(
  fs.readFileSync(new URL("../src/data/generated/people.json", import.meta.url), "utf8"),
);
const profile = (id: string) =>
  people.find((person: { person_id: string }) => person.person_id === id);

test("Batch 475 preserves page 94 rows and masks private identifiers", () => {
  const expected = [
    ["e72cc71f-1512-53dd-b1c5-b6ac47825601", "Charles F Corya", "dbfcca3b-e142-53a9-8ce8-92df7496901a", "••••1705", null],
    ["a9cae332-753e-5e30-b15d-4ce032ba3127", "Louise A Coser", "0d3dabad-8461-5a07-a104-316e05d966e5", null, null],
    ["521e3019-43b3-598a-9345-692e775d5cf6", "John O Cosgrave", "12dedeb9-305c-5288-96bc-2fc52b9c7178", "••••3863", null],
    ["f7382d8d-dc16-5521-824a-0a1c8511bf45", "Charles M Cosner", "d8b12f90-43c5-5f16-b8c5-749621be886b", "••••3808", "Pfc"],
    ["3655897f-afae-5e51-8136-04df35e75107", "William C Cossen", "de34c3c8-6761-5376-9fae-d239a80e4373", null, null],
    ["52e4f2d7-dc9a-5163-b70e-d30271b391d5", "Harmon Cossey", "0a10e8da-ee06-57fc-bb31-842e20379c75", null, null],
    ["3758b471-812c-51a2-8176-acac3190f59d", "Thomas P Cossuto", "d0ec8fc5-e152-5e38-9277-b3b41b3da899", "••••6944", null],
    ["eae034aa-ed00-5c61-b2f5-9910e0a20616", "Anette Costa", "bc5d449d-4d62-5476-a1a6-85758e776130", null, null],
    ["0aed0b45-539c-5bce-bcff-67bbe59c23b0", "Howard R Costa", "9c9ecf8e-4bc9-5aeb-a5f5-c8399b3ae715", "••••3980", null],
    ["a5048b62-3b5c-5bef-b116-9f502a309088", "Liberal Costa", "c6406b2c-f290-5a8e-b860-8912a0db900a", "••••8164", null],
  ];

  for (const [id, name, sourceRecordId, serial, rank] of expected) {
    const person = profile(String(id));
    expect(person).toMatchObject({ display_name: name });
    expect(person.source_records).toContainEqual(
      expect.objectContaining({
        source_record_id: sourceRecordId,
        serial_masked: serial,
        rank_as_indexed: rank,
        box: "146",
        archive_location: "230/86/29/02",
        pdf_page: 94,
      }),
    );
    expect(JSON.stringify(person)).not.toMatch(
      /"serial_number"|"serial_number_raw"|"serial_number_normalized"/,
    );
  }
  expect(profile("eae034aa-ed00-5c61-b2f5-9910e0a20616").source_records).toContainEqual(
    expect.objectContaining({ notes_as_indexed: "Italian Ci" }),
  );
});

test("Batch 475 publishes four broad Army categories without inventing employers", async ({ page }) => {
  const cases = [
    ["e72cc71f-1512-53dd-b1c5-b6ac47825601", "Charles F Corya", "Actors and actresses", "1941-01-17"],
    ["3758b471-812c-51a2-8176-acac3190f59d", "Thomas P Cossuto", "Construction occupations, n.e.c.", "1943-03-04"],
    ["0aed0b45-539c-5bce-bcff-67bbe59c23b0", "Howard R Costa", "Construction occupations, n.e.c.", "1943-02-12"],
    ["a5048b62-3b5c-5bef-b116-9f502a309088", "Liberal Costa", "Occupations in production of rubber goods", "1942-08-03"],
  ];
  for (const [id, name, occupation, endDate] of cases) {
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
        relationship_type: "unknown",
        end_date: endDate,
        temporal_basis: "temporal_relation_uncertain",
        claim_confidence: "medium",
      }),
    );
    await page.goto(`./people/${id}/`);
    await expect(page.getByRole("heading", { name, exact: true })).toBeVisible();
    await expect(page.locator("main")).toContainText(occupation);
    await expect(page.locator("main")).toContainText("No reliable pre-OSS employer has yet been identified");
  }
});

test("Batch 475 identifies John O'Hara Cosgrave II and keeps the chronology qualified", async ({ page }) => {
  const person = profile("521e3019-43b3-598a-9345-692e775d5cf6");
  expect(person).toMatchObject({
    display_name: "John O Cosgrave",
    identity_status: "high_confidence",
    personnel_category: "enlisted_army_personnel",
    commissioned_officer: false,
    research_status: "documented_prewar_employer_found",
    manual_review_required: true,
    immediate_pre_oss_affiliations: [],
    last_civilian_pre_service: [],
  });
  expect(person.name_variants).toEqual(expect.arrayContaining([
    "John O'Hara Cosgrave",
    "John O'Hara Cosgrave II",
    "J. O'H. Cosgrave II",
  ]));
  expect(person.other_pre_oss_affiliations).toContainEqual(
    expect.objectContaining({
      organization_id: null,
      role_title: "Book illustrator",
      occupation: "Freelance commercial artist and book illustrator",
      relationship_type: "self_employment",
      end_date: "1940",
      temporal_basis: "documented_prewar",
      claim_confidence: "high",
    }),
  );

  await page.goto("./people/521e3019-43b3-598a-9345-692e775d5cf6/");
  await expect(page.getByRole("heading", { name: "John O Cosgrave", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("John O'Hara Cosgrave II");
  await expect(page.locator("main")).toContainText("freelance commercial artist and book illustrator");
  await expect(page.locator("main")).toContainText("Springfield Weekly Republican");
  await expect(page.locator("main")).toContainText("no source reviewed establishes immediacy before OSS");
});

test("Batch 475 leaves five identities unresolved and preserves source classifications", async ({ page }) => {
  for (const id of [
    "a9cae332-753e-5e30-b15d-4ce032ba3127",
    "f7382d8d-dc16-5521-824a-0a1c8511bf45",
    "3655897f-afae-5e51-8136-04df35e75107",
    "52e4f2d7-dc9a-5163-b70e-d30271b391d5",
    "eae034aa-ed00-5c61-b2f5-9910e0a20616",
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
  expect(profile("f7382d8d-dc16-5521-824a-0a1c8511bf45")).toMatchObject({
    personnel_category: "enlisted_army_personnel",
    commissioned_officer: false,
  });
  expect(profile("eae034aa-ed00-5c61-b2f5-9910e0a20616")).toMatchObject({
    allied_or_foreign_personnel: true,
    personnel_category: "unknown_or_indeterminate",
  });

  await page.goto("./people/eae034aa-ed00-5c61-b2f5-9910e0a20616/");
  await expect(page.locator("main")).toContainText("Italian Ci");
  await expect(page.locator("main")).toContainText("No reliable pre-OSS employer has yet been identified");
});
