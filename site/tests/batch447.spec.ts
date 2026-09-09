import { expect, test } from "@playwright/test";
import fs from "node:fs";

const people = JSON.parse(
  fs.readFileSync(new URL("../src/data/generated/people.json", import.meta.url), "utf8"),
);
const profile = (id: string) =>
  people.find((person: { person_id: string }) => person.person_id === id);

test("Batch 447 publishes four identifier-supported status or occupation findings without inventing employers", async ({ page }) => {
  const expected = [
    [
      "7e53c938-aff6-5443-aa8f-2cabe3d98785",
      "Thomas M Collins",
      "Food products producing occupations, miscellaneous",
      "unknown",
      "1942-11-16",
    ],
    [
      "7762320c-5b2e-52be-8568-1ef76930e06c",
      "John E Colnon",
      "Students",
      "student",
      "1944-04-10",
    ],
    [
      "6e96c735-101e-58fd-a956-c49978ee025f",
      "Willard D Cologna",
      "Students",
      "student",
      "1944-01-04",
    ],
    [
      "7ff7214a-3d0e-554c-9f32-d041ce87b1f1",
      "Peter J Colombo",
      "Checkers",
      "unknown",
      "1942-09-07",
    ],
  ];

  for (const [id, name, occupation, relationshipType, endDate] of expected) {
    const person = profile(id);
    expect(person).toMatchObject({
      display_name: name,
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
        occupation,
        relationship_type: relationshipType,
        end_date: endDate,
        temporal_basis: "strongly_date_bounded",
        identity_confidence: "confirmed",
        claim_confidence: "medium",
      }),
    );
  }

  const thomas = profile("7e53c938-aff6-5443-aa8f-2cabe3d98785");
  await page.goto(`./people/${thomas.person_id}/`);
  await expect(page.getByRole("heading", { name: "Thomas M Collins", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("Food products producing occupations, miscellaneous");
  await expect(page.locator("main")).toContainText("no employer");
  await expect(page.locator("main")).toContainText("No reliable pre-OSS employer has yet been identified");

  const john = profile("7762320c-5b2e-52be-8568-1ef76930e06c");
  await page.goto(`./people/${john.person_id}/`);
  await expect(page.locator("main")).toContainText("Students");
  await expect(page.locator("main")).toContainText("no school or employer is identified");

  const willard = profile("6e96c735-101e-58fd-a956-c49978ee025f");
  await page.goto(`./people/${willard.person_id}/`);
  await expect(page.locator("main")).toContainText("Students");
  await expect(page.locator("main")).toContainText("no school or employer is identified");

  const peter = profile("7ff7214a-3d0e-554c-9f32-d041ce87b1f1");
  await page.goto(`./people/${peter.person_id}/`);
  await expect(page.locator("main")).toContainText("Checkers");
  await expect(page.locator("main")).toContainText("no employer, industry or checked material is identified");
});

test("Batch 447 keeps two identity leads qualified and employer-free", async ({ page }) => {
  const expected = [
    [
      "f8f138bb-7799-5463-84cd-c6a864525af6",
      "Yolande D Collins",
      "Yolande de Mauduit Collins",
      "Review Box 136",
    ],
    [
      "256daab4-061f-5974-8e82-f98f3b2445b1",
      "Clarence V Colmorgen",
      "Clarence Vernon Colmorgen",
      "Review Box 136",
    ],
  ];

  for (const [id, name, candidate, nextAction] of expected) {
    const person = profile(id);
    expect(person).toMatchObject({
      display_name: name,
      identity_status: "probable",
      personnel_category: "unknown_or_indeterminate",
      commissioned_officer: null,
      research_status: "requires_archival_review",
    });
    expect(person.name_variants).toContain(candidate);
    expect(person.immediate_pre_oss_affiliations).toEqual([]);
    expect(person.last_civilian_pre_service).toEqual([]);
    expect(person.other_pre_oss_affiliations).toEqual([]);
    expect(person.claims).toHaveLength(1);
    expect(person.claims[0]).toMatchObject({
      claim_type: "identity",
      claim_confidence: "medium",
    });

    await page.goto(`./people/${person.person_id}/`);
    await expect(page.getByRole("heading", { name, exact: true })).toBeVisible();
    await expect(page.locator("main")).toContainText("probably, but not conclusively");
    await expect(page.locator("main")).toContainText(nextAction);
    await expect(page.locator("main")).toContainText("No reliable pre-OSS employer has yet been identified");
  }
});

test("Batch 447 preserves all ten printed rows, masks identifiers and retains unresolved cases", async ({ page }) => {
  const expected = [
    ["dffa6165-09b9-5b3a-89cd-b73cee4cf27e", "Rose L Collins", "060ce843-d30f-5b42-9d5b-45cf0b5c22ca", "135", 0],
    ["7c840cfb-8fea-5f09-9aa1-60f42cc9b8a9", "Sara R Collins", "2be609e1-fded-556b-8fb9-58091678d280", "135", 0],
    ["7e53c938-aff6-5443-aa8f-2cabe3d98785", "Thomas M Collins", "e6651ddf-c85f-5a59-8332-7164ac4a591d", "135", 8],
    ["74726306-16fc-5807-8856-83ad9195bc62", "William L Collins", "b9e5161a-d189-547f-9d7a-28acd15d8ac9", "136", 6],
    ["f8f138bb-7799-5463-84cd-c6a864525af6", "Yolande D Collins", "5e0e4776-e65d-514e-9bfa-4b240a051cbb", "136", 0],
    ["fc4e66ca-0ecb-5f35-94b1-f4d7d32a5391", "Patsy Collitti", "101c4561-e0d4-5362-b61a-ce13816559b0", "135", 0],
    ["256daab4-061f-5974-8e82-f98f3b2445b1", "Clarence V Colmorgen", "91f2f2e5-f7de-5cab-b95e-751366954701", "136", 8],
    ["7762320c-5b2e-52be-8568-1ef76930e06c", "John E Colnon", "a312e636-ebde-57aa-a680-72635ee70383", "136", 8],
    ["6e96c735-101e-58fd-a956-c49978ee025f", "Willard D Cologna", "aaaa7092-4fa9-5899-83d1-81e30273afa5", "136", 8],
    ["7ff7214a-3d0e-554c-9f32-d041ce87b1f1", "Peter J Colombo", "4dca32c4-d823-5daf-bdff-11c92c14456b", "136", 8],
  ];

  for (const [id, name, sourceRecordId, box, serialLength] of expected) {
    const person = profile(String(id));
    expect(person).toMatchObject({ display_name: name });
    expect(person.source_records[0]).toMatchObject({
      source_record_id: sourceRecordId,
      box,
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
    "dffa6165-09b9-5b3a-89cd-b73cee4cf27e",
    "7c840cfb-8fea-5f09-9aa1-60f42cc9b8a9",
    "74726306-16fc-5807-8856-83ad9195bc62",
    "fc4e66ca-0ecb-5f35-94b1-f4d7d32a5391",
  ]) {
    const person = profile(id);
    expect(person.identity_status).toBe("unresolved");
    expect(person.research_status).toBe("requires_archival_review");
    expect(person.immediate_pre_oss_affiliations).toEqual([]);
    expect(person.last_civilian_pre_service).toEqual([]);
    expect(person.other_pre_oss_affiliations).toEqual([]);
    expect(person.claims).toEqual([]);
  }

  const william = profile("74726306-16fc-5807-8856-83ad9195bc62");
  await page.goto(`./people/${william.person_id}/`);
  await expect(page.locator("main")).toContainText("six-digit value");
  await expect(page.locator("main")).toContainText("Twenty-four exact-name");
  await expect(page.locator("main")).toContainText("Review Box 136");

  const patsy = profile("fc4e66ca-0ecb-5f35-94b1-f4d7d32a5391");
  await page.goto(`./people/${patsy.person_id}/`);
  await expect(page.locator("main")).toContainText("later Pat Collitti lead");
  await expect(page.locator("main")).toContainText("No reliable pre-OSS employer has yet been identified");
});
