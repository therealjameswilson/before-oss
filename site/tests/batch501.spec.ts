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
  ["66f43b5e-8c87-5771-a901-af97b0c3c8db", "Sherman J Crough", "27d4b20b-eff2-5938-858c-f0592c96f2db", "156", true],
  ["ec53cbcd-995a-59d8-b5a5-f966f62b74c7", "Richard Crouse", "f06e493a-ac95-5c10-8992-07ea75996c97", "156", false],
  ["1d71ac7e-ae34-5431-a2d9-360cfd87eed8", "Harry L Crow", "4b04d99a-f85a-53a1-8e41-70b9efab55e4", "156", false],
  ["af1bdf07-60bb-509b-a52f-e01139ae5fbc", "Buford C Crowder", "9fc8bb94-d639-59b0-8554-1ad45a3761e6", "156", true],
  ["9921ec68-c23e-53ab-9b11-fc28cc276441", "Chester E Crowder", "1859a25f-8110-5722-8ded-d4a2d4b9eb35", "156", true],
  ["6ecd39c4-04a6-525b-bb1c-1bacbaf3532b", "Edwin W Crowe", "051e6b9d-5619-529b-8899-b476bfd76463", "157", true],
  ["86c8be42-ff6e-5688-b128-e985598e189d", "Joseph M Crowe", "b6571cd3-4f3a-510e-a11b-3055f3fdf722", "157", false],
  ["7798a07e-ac4c-5692-9955-3fa43c7d8381", "Phillip K Crowe", "440451cd-2fc6-5a3b-ba95-c3d58f03b860", "157", true],
  ["6ff917f3-681f-529d-847b-86dc54677a66", "John B Crowl", "c4b599b9-f725-5c0f-b52f-273131a50960", "157", true],
  ["1095e094-86b6-5247-904a-cb91685a04f2", "Anne T Crowley", "336316a0-fed1-5d98-b5d2-dad69239a1d7", "157", false],
] as const;

test("Batch 501 preserves all ten page 99 rows and masks every printed identifier", () => {
  for (const [id, name, sourceRecordId, box, hasPrivateIdentifier] of cohort) {
    const person = profile(id);
    expect(person).toMatchObject({ display_name: name });
    const sourceRecord = person.source_records.find(
      (record: { source_record_id: string }) => record.source_record_id === sourceRecordId,
    );
    expect(sourceRecord).toMatchObject({
      box,
      archive_location: "230/86/29/04",
      pdf_page: 99,
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

test("Batch 501 publishes Sherman Crough's student pathway without calling Dartmouth an employer", () => {
  const sherman = profile("66f43b5e-8c87-5771-a901-af97b0c3c8db");
  expect(sherman).toMatchObject({
    identity_status: "confirmed",
    personnel_category: "enlisted_army_personnel",
    commissioned_officer: false,
    research_status: "completed",
    immediate_pre_oss_affiliations: [],
    last_civilian_pre_service: [],
  });
  expect(sherman.other_pre_oss_affiliations).toContainEqual(
    expect.objectContaining({
      canonical_organization: "Dartmouth College",
      relationship_type: "student",
      occupation: "student",
      temporal_basis: "strongly_date_bounded",
      claim_confidence: "high",
    }),
  );
});

test("Batch 501 publishes two identifier-confirmed categories without inventing employers", () => {
  const expected = new Map([
    ["9921ec68-c23e-53ab-9b11-fc28cc276441", ["Actors and actresses", "unknown"]],
    ["6ecd39c4-04a6-525b-bb1c-1bacbaf3532b", ["student", "student"]],
  ]);
  for (const [id, [occupation, relationshipType]] of expected) {
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
        canonical_organization: null,
        occupation,
        relationship_type: relationshipType,
        temporal_basis: "strongly_date_bounded",
        claim_confidence: "medium",
        publication_status: "publish_qualified",
      }),
    );
  }
});

test("Batch 501 separates Philip Crowe's immediate, last-civilian and earlier affiliations", () => {
  const philip = profile("7798a07e-ac4c-5692-9955-3fa43c7d8381");
  expect(philip).toMatchObject({
    display_name: "Phillip K Crowe",
    identity_status: "high_confidence",
    personnel_category: "unknown_or_indeterminate",
    commissioned_officer: null,
    research_status: "verified_employer_found",
  });
  expect(philip.name_variants).toEqual(
    expect.arrayContaining(["Philip K. Crowe", "Philip Kingsland Crowe"]),
  );
  expect(philip.immediate_pre_oss_affiliations).toContainEqual(
    expect.objectContaining({
      canonical_organization: "Fortune magazine",
      relationship_type: "employment",
      immediate_pre_oss: true,
      last_civilian_pre_service: true,
      claim_confidence: "high",
    }),
  );
  expect(philip.last_civilian_pre_service).toContainEqual(
    expect.objectContaining({ canonical_organization: "Fortune magazine" }),
  );
  expect(philip.other_pre_oss_affiliations).toEqual(
    expect.arrayContaining([
      expect.objectContaining({ canonical_organization: "Life magazine", relationship_type: "employment" }),
      expect.objectContaining({ canonical_organization: "New York Evening Post", role_title: "reporter" }),
      expect.objectContaining({ canonical_organization: "University of Virginia", relationship_type: "student" }),
    ]),
  );
});

test("Batch 501 separates John Crowl's Army, self-employment and earlier clerkship", () => {
  const john = profile("6ff917f3-681f-529d-847b-86dc54677a66");
  expect(john).toMatchObject({
    identity_status: "confirmed",
    personnel_category: "enlisted_army_personnel",
    commissioned_officer: false,
    research_status: "verified_employer_found",
  });
  expect(john.immediate_pre_oss_affiliations).toContainEqual(
    expect.objectContaining({
      canonical_organization: "United States Army",
      relationship_type: "military_assignment",
      temporal_basis: "explicit_immediate",
      claim_confidence: "confirmed",
    }),
  );
  expect(john.last_civilian_pre_service).toContainEqual(
    expect.objectContaining({
      organization_name_as_found: "his own printing business",
      relationship_type: "self_employment",
      claim_confidence: "confirmed",
    }),
  );
  expect(john.other_pre_oss_affiliations).toContainEqual(
    expect.objectContaining({
      canonical_organization: "American Steel and Wire Company",
      role_title: "clerk",
      temporal_basis: "documented_prewar",
    }),
  );
});

test("Batch 501 keeps five unresolved or ambiguous names free of public claims", () => {
  for (const id of [
    "ec53cbcd-995a-59d8-b5a5-f966f62b74c7",
    "1d71ac7e-ae34-5431-a2d9-360cfd87eed8",
    "af1bdf07-60bb-509b-a52f-e01139ae5fbc",
    "86c8be42-ff6e-5688-b128-e985598e189d",
    "1095e094-86b6-5247-904a-cb91685a04f2",
  ]) {
    const person = profile(id);
    expect(["unresolved", "ambiguous"]).toContain(person.identity_status);
    expect(person).toMatchObject({
      personnel_category: "unknown_or_indeterminate",
      commissioned_officer: null,
      immediate_pre_oss_affiliations: [],
      last_civilian_pre_service: [],
      other_pre_oss_affiliations: [],
      claims: [],
    });
  }
});

test("Batch 501 direct routes expose the new evidence and current coverage", async ({ page }) => {
  expect(stats.research_attempted_people).toBeGreaterThanOrEqual(4778);
  expect(stats.verified_affiliation_people).toBeGreaterThanOrEqual(547);
  expect(stats.verified_employer_people).toBeGreaterThanOrEqual(244);
  expect(stats.archival_review_assessed_people).toBeGreaterThanOrEqual(4733);

  await page.goto("./people/7798a07e-ac4c-5692-9955-3fa43c7d8381/");
  await expect(page.getByRole("heading", { name: "Phillip K Crowe", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("Philip Kingsland Crowe");
  await expect(page.locator("main")).toContainText("Fortune magazine");
  await expect(page.locator("main")).toContainText("University of Virginia");

  await page.goto("./people/6ff917f3-681f-529d-847b-86dc54677a66/");
  await expect(page.getByRole("heading", { name: "John B Crowl", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("replacement depot in North Africa");
  await expect(page.locator("main")).toContainText("his own printing business");
  await expect(page.locator("main")).toContainText("American Steel and Wire Company");

  await page.goto("./people/66f43b5e-8c87-5771-a901-af97b0c3c8db/");
  await expect(page.getByRole("heading", { name: "Sherman J Crough", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("Dartmouth College");

  await page.goto("./people/1095e094-86b6-5247-904a-cb91685a04f2/");
  await expect(page.getByRole("heading", { name: "Anne T Crowley", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("No reliable pre-OSS employer has yet been identified");
});
