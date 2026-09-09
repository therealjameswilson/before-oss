import { expect, test } from "@playwright/test";
import fs from "node:fs";

const people = JSON.parse(
  fs.readFileSync(new URL("../src/data/generated/people.json", import.meta.url), "utf8"),
);
const profile = (id: string) =>
  people.find((person: { person_id: string }) => person.person_id === id);

test("Batch 444 publishes identifier-supported occupations without inventing employers", async ({ page }) => {
  const expected = [
    [
      "07924cc1-de97-5013-a93f-8682c6b4a245",
      "Thomas J Coleman",
      "Thomas J Coleman",
      "Office machine operator",
      "1941-03-31",
    ],
    [
      "e87e2976-99e7-5966-93bb-92e4b46329f5",
      "Loannis N Collaros",
      "Ioannis N Collaros",
      "Radio operator",
      "1942-04-03",
    ],
  ];

  for (const [id, indexedName, documentedVariant, occupation, endDate] of expected) {
    const person = profile(id);
    expect(person).toMatchObject({
      display_name: indexedName,
      identity_status: "confirmed",
      personnel_category: "enlisted_army_personnel",
      commissioned_officer: false,
      research_status: "occupation_only_found",
    });
    expect(person.name_variants).toContain(documentedVariant);
    expect(person.immediate_pre_oss_affiliations).toEqual([]);
    expect(person.last_civilian_pre_service).toEqual([]);
    expect(person.other_pre_oss_affiliations).toContainEqual(
      expect.objectContaining({
        organization_id: null,
        occupation,
        relationship_type: "unknown",
        end_date: endDate,
        temporal_basis: "strongly_date_bounded",
        identity_confidence: "confirmed",
        claim_confidence: "medium",
      }),
    );
  }

  const thomas = profile("07924cc1-de97-5013-a93f-8682c6b4a245");
  await page.goto(`./people/${thomas.person_id}/`);
  await expect(page.getByRole("heading", { name: "Thomas J Coleman", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("Office machine operator");
  await expect(page.locator("main")).toContainText("no employer or machine is identified");
  await expect(page.locator("main")).toContainText("No reliable pre-OSS employer has yet been identified");

  const collaros = profile("e87e2976-99e7-5966-93bb-92e4b46329f5");
  await page.goto(`./people/${collaros.person_id}/`);
  await expect(page.getByRole("heading", { name: "Loannis N Collaros", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("Ioannis N Collaros");
  await expect(page.locator("main")).toContainText("Radio operator");
  await expect(page.locator("main")).toContainText("no employer or station is identified");
});

test("Batch 444 retains Joseph Collart's officer identity while keeping education distinct from employment", async ({ page }) => {
  const joseph = profile("832d939e-cbb0-5979-9c57-bb0c0e27113d");
  expect(joseph).toMatchObject({
    display_name: "Joseph Collart",
    identity_status: "high_confidence",
    personnel_category: "commissioned_army_officer",
    commissioned_officer: true,
    research_status: "requires_archival_review",
  });
  expect(joseph.immediate_pre_oss_affiliations).toEqual([]);
  expect(joseph.last_civilian_pre_service).toEqual([]);
  expect(joseph.other_pre_oss_affiliations).toContainEqual(
    expect.objectContaining({
      canonical_organization: "Washington State University",
      relationship_type: "student",
      immediate_pre_oss: false,
      last_civilian_pre_service: false,
      temporal_basis: "documented_prewar",
    }),
  );

  await page.goto(`./people/${joseph.person_id}/`);
  await expect(page.getByRole("heading", { name: "Joseph Collart", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("commissioned army officer");
  await expect(page.locator("main")).toContainText("Student athlete");
  await expect(page.locator("main")).toContainText("No reliable pre-OSS employer has yet been identified");
});

test("Batch 444 preserves all ten printed rows, masks identifiers and publishes unresolved profiles", async ({ page }) => {
  const expected = [
    ["d7a1e18a-fb4e-5204-a539-d37a6ec6f460", "Lawrence A Coleman", "d16761f6-e598-5dc0-b46c-5c526c49bf55", "134", true],
    ["4fb29d2a-e303-5603-8364-0c610bda18bf", "Marion E Coleman", "e2b07550-890e-5274-8449-096d8a57242d", "134", false],
    ["fcab0617-5054-50e8-a8d6-d67d6fbb2736", "Robert C Coleman", "759558fd-7b1f-5871-bab4-70ada0b965a9", "135", true],
    ["07924cc1-de97-5013-a93f-8682c6b4a245", "Thomas J Coleman", "10ddd5f2-047d-5916-a494-059379a6dc3b", "135", true],
    ["30df5791-746c-585b-b53c-634c7e258bf2", "William S Coleman", "2c31f0a6-e7e1-57db-8675-dea864633c32", "135", false],
    ["c7a539bd-e958-5d38-8439-d35930d88aba", "Aline J Colgate", "2eb3ad79-3c4e-5218-97fd-f57d3cb4da86", "135", false],
    ["294c9621-5b8f-5224-b6f3-d29945325f1a", "Orrin K Coligan", "068208a0-4b93-56b4-9364-873edb6a8592", "135", false],
    ["e87e2976-99e7-5966-93bb-92e4b46329f5", "Loannis N Collaros", "f1b456ff-d368-5b42-bd2b-45d39a12dfda", "135", true],
    ["832d939e-cbb0-5979-9c57-bb0c0e27113d", "Joseph Collart", "635b7118-e2fb-5376-bde0-efdff4769cf4", "135", true],
    ["11351235-a2b1-5c84-8c9a-37d60fc1ea87", "Norman T Collett", "30c34d0a-5ffc-5f1c-959d-25c3e926df8c", "135", false],
  ];

  for (const [id, name, sourceRecordId, box, hasSerial] of expected) {
    const person = profile(String(id));
    expect(person).toMatchObject({ display_name: name });
    expect(person.source_records[0]).toMatchObject({
      source_record_id: sourceRecordId,
      box,
      archive_location: "230/86/29/01",
      pdf_page: 87,
    });
    if (hasSerial) {
      expect(person.source_records[0].serial_masked).toMatch(/^••••.{3,4}$/u);
    } else {
      expect(person.source_records[0].serial_masked).toBeNull();
    }
    expect(JSON.stringify(person)).not.toMatch(
      /"serial_number"|"serial_number_raw"|"serial_number_normalized"/,
    );
  }

  for (const id of [
    "d7a1e18a-fb4e-5204-a539-d37a6ec6f460",
    "4fb29d2a-e303-5603-8364-0c610bda18bf",
    "fcab0617-5054-50e8-a8d6-d67d6fbb2736",
    "30df5791-746c-585b-b53c-634c7e258bf2",
    "c7a539bd-e958-5d38-8439-d35930d88aba",
    "294c9621-5b8f-5224-b6f3-d29945325f1a",
    "11351235-a2b1-5c84-8c9a-37d60fc1ea87",
  ]) {
    const person = profile(id);
    expect(person.identity_status).toBe("unresolved");
    expect(person.research_status).toBe("requires_archival_review");
    expect(person.immediate_pre_oss_affiliations).toEqual([]);
    expect(person.last_civilian_pre_service).toEqual([]);
    expect(person.other_pre_oss_affiliations).toEqual([]);
    expect(person.claims).toEqual([]);
  }

  const lawrence = profile("d7a1e18a-fb4e-5204-a539-d37a6ec6f460");
  await page.goto(`./people/${lawrence.person_id}/`);
  await expect(page.getByRole("heading", { name: "Lawrence A Coleman", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("six-digit identifier");
  await expect(page.locator("main")).toContainText("not padded or assigned to that candidate");
  await expect(page.locator("main")).toContainText("Review Box 134");
  await expect(page.locator("main")).toContainText("No reliable pre-OSS employer has yet been identified");
});
