import { expect, test } from "@playwright/test";
import fs from "node:fs";

const people = JSON.parse(
  fs.readFileSync(new URL("../src/data/generated/people.json", import.meta.url), "utf8"),
);
const profile = (id: string) =>
  people.find((person: { person_id: string }) => person.person_id === id);

test("Batch 438 keeps four Army occupations separate from employers", async ({ page }) => {
  const expected = [
    ["81ffc7a3-009c-59fd-a598-3bd8c12cd725", "Thomas B Cogley", "Electrical machinery and accessories manufacturing occupations, n.e.c.", "1943-08-13"],
    ["0e4eec76-476d-5ee2-a4a3-ea0155c70fb6", "Albert Cohen", "Warehousing, storekeeping, handling, loading, unloading, and related occupations, n.e.c.", "1942-02-09"],
    ["3ae9f27a-3991-5252-859a-669796c211e1", "Arthur A Cohen", "Foremen, n.e.c.", "1942-11-03"],
    ["f90dba80-db4f-586f-acce-d1a071bebec2", "Harry Cohen", "Managers and officials, n.e.c.", "1941-04-30"],
  ];

  for (const [id, name, occupation, endDate] of expected) {
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
        relationship_type: "unknown",
        end_date: endDate,
        temporal_basis: "temporal_relation_uncertain",
        claim_confidence: "medium",
      }),
    );
  }

  const thomas = profile("81ffc7a3-009c-59fd-a598-3bd8c12cd725");
  await page.goto(`./people/${thomas.person_id}/`);
  await expect(page.getByRole("heading", { name: "Thomas B Cogley", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("Electrical machinery and accessories manufacturing occupations");
  await expect(page.locator("main")).toContainText("no employer or exact job is identified");
  await expect(page.locator("main")).toContainText("No reliable pre-OSS employer has yet been identified");
});

test("Batch 438 qualifies Cogswell's last civilian employer without calling it immediate", async ({ page }) => {
  const cogswell = profile("c6efa644-bcad-5e64-9cdd-6eeeb80982b2");
  expect(cogswell).toMatchObject({
    display_name: "Colby A Cogswell",
    identity_status: "confirmed",
    personnel_category: "enlisted_army_personnel",
    commissioned_officer: false,
    research_status: "documented_prewar_employer_found",
  });
  expect(cogswell.immediate_pre_oss_affiliations).toEqual([]);
  expect(cogswell.last_civilian_pre_service).toContainEqual(
    expect.objectContaining({
      canonical_organization: "The First Boston Corporation",
      organization_name_as_found: "the First Boston Corporation",
      relationship_type: "employment",
      start_date: "1939",
      end_date: "1943-06",
      temporal_basis: "probable_immediate",
      claim_confidence: "medium",
      publication_status: "publish_qualified",
    }),
  );
  expect(cogswell.last_civilian_pre_service[0]).toMatchObject({
    role_title: null,
    occupation: null,
    city: null,
    state_or_region: null,
    country: null,
  });

  await page.goto(`./people/${cogswell.person_id}/`);
  await expect(page.getByRole("heading", { name: "Colby A Cogswell", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("First Boston Corporation");
  await expect(page.locator("main")).toContainText("best-supported last civilian employer");
  await expect(page.locator("main")).toContainText("precise interruption date is inferred rather than stated");
});

test("Batch 438 separates Cogswell's student, Army and occupation evidence", async ({ page }) => {
  const cogswell = profile("c6efa644-bcad-5e64-9cdd-6eeeb80982b2");
  expect(cogswell.other_pre_oss_affiliations).toContainEqual(
    expect.objectContaining({
      canonical_organization: "Dartmouth College",
      relationship_type: "student",
      temporal_basis: "documented_prewar",
      claim_confidence: "high",
    }),
  );
  expect(cogswell.other_pre_oss_affiliations).toContainEqual(
    expect.objectContaining({
      canonical_organization: "United States Army",
      organization_name_as_found: "AUS",
      role_title: "private at Army entry; later rank not established",
      relationship_type: "military_assignment",
      start_date: "1943-06-07",
      claim_confidence: "high",
    }),
  );
  expect(cogswell.other_pre_oss_affiliations).toContainEqual(
    expect.objectContaining({
      organization_id: null,
      occupation: "Salesmen, stock and bond",
      relationship_type: "unknown",
      end_date: "1943-06-07",
      claim_confidence: "medium",
    }),
  );

  await page.goto(`./people/${cogswell.person_id}/`);
  await expect(page.locator("main")).toContainText("Dartmouth College");
  await expect(page.locator("main")).toContainText("student");
  await expect(page.locator("main")).toContainText("United States Army");
  await expect(page.locator("main")).toContainText("military assignment");
  await expect(page.locator("main")).toContainText("private at Army entry; later rank not established");
  await expect(page.locator("main")).toContainText("Salesmen, stock and bond");
});

test("Batch 438 preserves all ten rows, masks identifiers and withholds rejected namesakes", async ({ page }) => {
  const expected = [
    ["4952a2ca-a59a-5e72-bd1f-7f2793aede75", "Mary M Coghlan", "516c26af-4ed5-59c6-894b-3b4940c6a560", "132", false],
    ["81ffc7a3-009c-59fd-a598-3bd8c12cd725", "Thomas B Cogley", "0e92d1c3-4fa0-595e-aaa4-ce74ae4ef976", "132", true],
    ["c6efa644-bcad-5e64-9cdd-6eeeb80982b2", "Colby A Cogswell", "5b6feb15-0199-5d1e-98d7-f8820abc8b35", "132", true],
    ["0e4eec76-476d-5ee2-a4a3-ea0155c70fb6", "Albert Cohen", "0f7d5f4f-06ab-54e8-adc6-4410ce8846ab", "132", true],
    ["3ae9f27a-3991-5252-859a-669796c211e1", "Arthur A Cohen", "0f26a87c-6042-550e-a721-208fffbef45a", "132", true],
    ["bb8b859b-5926-579f-af1a-29c1f11e2534", "David C Cohen", "1b687013-5360-57fe-b1e8-3c9acc9801a4", "132", false],
    ["66ce9e06-1af7-587e-91a5-ed10f5c1c9a0", "Harold Cohen", "bc855740-5fcf-5d3a-99c5-43353bf6905f", "132", true],
    ["f90dba80-db4f-586f-acce-d1a071bebec2", "Harry Cohen", "6e54dd04-24ed-528f-9006-2969ae2f6190", "132", true],
    ["a077b353-8c89-5bd9-8a50-8343f7aedd91", "Jean Cohen", "c35dfdee-90f4-5d04-853e-7bb771fc51cd", "132", false],
    ["bf2ab088-e74c-5f81-ad77-b69368c06b94", "Leonard Cohen", "51e919f7-65cb-51f9-a6d7-56ce33551ee3", "133", true],
  ];

  for (const [id, name, sourceRecordId, box, hasSerial] of expected) {
    const person = profile(String(id));
    expect(person).toMatchObject({ display_name: name });
    expect(person.source_records[0]).toMatchObject({
      source_record_id: sourceRecordId,
      pdf_page: 86,
      rank_as_indexed: null,
      box,
      archive_location: "230/86/28/07",
    });
    if (hasSerial) {
      expect(person.source_records[0].serial_masked).toMatch(/^••••.{4}$/u);
    } else {
      expect(person.source_records[0].serial_masked).toBeNull();
    }
    expect(JSON.stringify(person)).not.toMatch(
      /"serial_number"|"serial_number_raw"|"serial_number_normalized"/,
    );
  }

  for (const id of [
    "4952a2ca-a59a-5e72-bd1f-7f2793aede75",
    "bb8b859b-5926-579f-af1a-29c1f11e2534",
    "66ce9e06-1af7-587e-91a5-ed10f5c1c9a0",
    "a077b353-8c89-5bd9-8a50-8343f7aedd91",
    "bf2ab088-e74c-5f81-ad77-b69368c06b94",
  ]) {
    const person = profile(id);
    expect(person).toMatchObject({
      identity_status: "unresolved",
      research_status: "requires_archival_review",
    });
    expect(person.immediate_pre_oss_affiliations).toEqual([]);
    expect(person.last_civilian_pre_service).toEqual([]);
    expect(person.other_pre_oss_affiliations).toEqual([]);
    expect(person.claims).toEqual([]);
  }

  const leonard = profile("bf2ab088-e74c-5f81-ad77-b69368c06b94");
  await page.goto(`./people/${leonard.person_id}/`);
  await expect(page.getByRole("heading", { name: "Leonard Cohen", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("Canadian singer");
  await expect(page.locator("main")).toContainText("No reliable pre-OSS employer has yet been identified");
  await expect(page.locator("main")).not.toContainText("Hallelujah");
});
