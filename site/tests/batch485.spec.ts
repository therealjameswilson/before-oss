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
  ["ffe64213-43bc-5b76-9577-4a45298443ce", "Dorotothy H Cox", "eb596f1d-3013-5d52-ae57-576fc8e8e709", null],
  ["e6db7e50-ba1d-5aae-93c4-9983d9e725bb", "Edward N Cox", "4637626b-91c6-5393-99ea-bd240e456cf9", "••••9751"],
  ["a73a235b-1eaf-51c2-841f-c98edcaed688", "Evelyn L Cox", "57fef7a7-1b01-5690-8a8b-6bad49c4e999", null],
  ["29788de7-9cce-5300-bbad-40fd4cfcc243", "Fred E Cox", "3f3e910d-c87d-572c-95fd-16e84f16a88b", "••••2067"],
  ["63981f0e-428e-5598-b03f-97b1b005b42f", "Frederic S Cox", "3e8e8a36-369e-525d-97b9-1224a29cea0b", null],
  ["3e64597f-14f0-5166-bdcd-fb99fe49dfb7", "Glenn L Cox", "42c538fb-a8c9-5f96-b849-826c7b030da6", "••••6880"],
  ["2dc77266-ba3b-5c58-bae6-73ba1e6fbd61", "Jane M Cox", "d1978248-cffd-5d8d-bef8-cb0fb2f5ed7b", null],
  ["5f1c5f46-5937-5595-bf3b-75c99e7231d9", "John H Cox", "67d17efd-f82a-5014-b806-ee0c303c9beb", null],
  ["5f9352e6-3dd4-5f38-a791-879a884281b4", "Johnie L Cox", "1888e277-2cc8-5745-8ef1-872bd4462930", "••••0713"],
  ["3f83f39a-9e81-52b8-8ba4-7eda1cfdc3ef", "Keith C Cox", "28ceb893-c8bb-51db-a31b-979f94692460", "••••5441"],
] as const;

test("Batch 485 preserves the ten page 96 rows and masks private identifiers", () => {
  for (const [id, name, sourceRecordId, serial] of cohort) {
    const person = profile(id);
    expect(person).toMatchObject({ display_name: name });
    expect(person.source_records).toContainEqual(
      expect.objectContaining({
        source_record_id: sourceRecordId,
        serial_masked: serial,
        box: "150",
        archive_location: "230/86/29/03",
        pdf_page: 96,
      }),
    );
    expect(JSON.stringify(person)).not.toMatch(
      /"serial_number"|"serial_number_raw"|"serial_number_normalized"/,
    );
  }
});

test("Batch 485 preserves Dorotothy while publishing the qualified Dorothy Hannah Cox pathway", () => {
  const dorothy = profile("ffe64213-43bc-5b76-9577-4a45298443ce");
  expect(dorothy).toMatchObject({
    display_name: "Dorotothy H Cox",
    identity_status: "high_confidence",
    personnel_category: "civilian_professional_or_administrative_grade",
    commissioned_officer: false,
    research_status: "occupation_only_found",
    last_civilian_pre_service: [],
  });
  expect(dorothy.name_variants).toEqual(
    expect.arrayContaining(["Dorothy H Cox", "Dorothy Hannah Cox", "Cox, Dorothy Hannah"]),
  );
  expect(dorothy.immediate_pre_oss_affiliations).toContainEqual(
    expect.objectContaining({
      canonical_organization: null,
      occupation: "Archaeologist, excavation architect, and numismatist",
      relationship_type: "unknown",
      immediate_pre_oss: true,
      temporal_basis: "probable_immediate",
      claim_confidence: "medium",
      publication_status: "publish_qualified",
    }),
  );
  expect(dorothy.claims).toEqual(
    expect.arrayContaining([
      expect.objectContaining({ claim_type: "identity", claim_confidence: "high" }),
      expect.objectContaining({ claim_type: "occupation", claim_confidence: "medium" }),
    ]),
  );
});

test("Batch 485 publishes only date-bounded exact-identifier Army occupations", () => {
  const cases = [
    ["e6db7e50-ba1d-5aae-93c4-9983d9e725bb", "Decorator or window dresser"],
    ["29788de7-9cce-5300-bbad-40fd4cfcc243", "Recreation or amusement attendant, not elsewhere classified"],
    ["5f9352e6-3dd4-5f38-a791-879a884281b4", "Farm hand, general farm"],
  ] as const;

  for (const [id, occupation] of cases) {
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
        occupation,
        relationship_type: "unknown",
        claim_confidence: "medium",
        publication_status: "publish_qualified",
      }),
    );
  }

  const keith = profile("3f83f39a-9e81-52b8-8ba4-7eda1cfdc3ef");
  expect(keith).toMatchObject({
    identity_status: "confirmed",
    personnel_category: "enlisted_army_personnel",
    commissioned_officer: false,
    research_status: "requires_archival_review",
    immediate_pre_oss_affiliations: [],
    last_civilian_pre_service: [],
    other_pre_oss_affiliations: [],
  });
  expect(keith.claims).toHaveLength(1);
  expect(keith.claims[0]).toMatchObject({ claim_type: "identity", claim_confidence: "confirmed" });
});

test("Batch 485 keeps unresolved and low-confidence namesake candidates out of public facts", () => {
  for (const id of [
    "a73a235b-1eaf-51c2-841f-c98edcaed688",
    "63981f0e-428e-5598-b03f-97b1b005b42f",
    "3e64597f-14f0-5166-bdcd-fb99fe49dfb7",
    "2dc77266-ba3b-5c58-bae6-73ba1e6fbd61",
  ]) {
    const person = profile(id);
    expect(person.identity_status).toBe("unresolved");
    expect(person.research_status).toBe("requires_archival_review");
    expect(person.immediate_pre_oss_affiliations).toEqual([]);
    expect(person.last_civilian_pre_service).toEqual([]);
    expect(person.other_pre_oss_affiliations).toEqual([]);
    expect(person.claims).toEqual([]);
  }

  const john = profile("5f1c5f46-5937-5595-bf3b-75c99e7231d9");
  expect(john).toMatchObject({
    identity_status: "ambiguous",
    research_status: "requires_archival_review",
    immediate_pre_oss_affiliations: [],
    last_civilian_pre_service: [],
    other_pre_oss_affiliations: [],
    claims: [],
  });
  expect(john.claims).toEqual([]);
  expect(john.next_action).toContain("compare only then with British Captain John H Cox and Team IVOR records");
});

test("Batch 485 profile and coverage data render the reviewed outcome", async ({ page }) => {
  expect(stats.research_attempted_people).toBeGreaterThanOrEqual(4619);
  expect(stats.verified_affiliation_people).toBeGreaterThanOrEqual(530);
  expect(stats.verified_employer_people).toBeGreaterThanOrEqual(235);

  await page.goto("./people/ffe64213-43bc-5b76-9577-4a45298443ce/");
  await expect(page.getByRole("heading", { name: "Dorotothy H Cox", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("Dorothy Hannah Cox");
  await expect(page.locator("main")).toContainText("Excavation architect and numismatist");
  await expect(page.locator("main")).toContainText("The Perfect Spy");
  await expect(page.locator("main")).toContainText("Records of the Office of Strategic Services (RG 226): Entry 215");
  await expect(page.locator("main")).toContainText("No reliable pre-OSS employer has yet been identified");
});
