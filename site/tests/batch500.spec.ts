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
  ["62a6316b-a612-5d6e-baa6-d4ee8673673a", "Paul L Crosby", "5c55dab0-7a35-5692-94af-996471372256", true],
  ["d29d09eb-caf5-56bb-98e3-383f542ee39e", "Richard Crosby", "7487084b-680b-54fc-b842-15a4e84238d2", true],
  ["44229cf5-f9c6-5547-a640-c999cc95ba33", "Vernon R Crosby", "58291f47-faf6-5e6e-b523-55f0feeb6eae", true],
  ["e984ea64-f5cc-5691-902d-8d1ac1672d4b", "Allan B Cross", "9c158ae3-b745-50a5-8c27-762418808de3", true],
  ["774bcf91-44a4-58a6-9e51-0a5bb687a683", "J A Cross", "d94b9c5c-f0e3-5821-85c8-824e9e7d106c", true],
  ["a89936c7-8775-53f2-b0fb-b0c6d17f960d", "James E Cross", "21658f8c-6887-5e75-b89b-bf59bbc01227", false],
  ["f1b41fee-b483-5aa2-bcc1-8237c625cab3", "Arthur W Crossley", "0dd1040e-e1af-52ac-ba4b-21b5c5636a0d", true],
  ["5bf50f1c-5a7b-5310-83a8-a38baed557b1", "Phyllis R Croswell", "b899a988-81b4-5900-8719-b3656df72afc", false],
  ["262bac81-d2be-5b79-8012-54eceb89ec80", "Gregg E Crouch", "d99f766c-cfbf-5455-b1ad-5faf471afd7e", true],
  ["1af8322e-3d2b-5657-a6bb-582901396464", "Paul W Crouch", "7fbd8fc4-7a74-5182-bfa8-4ebca301caaa", false],
] as const;

test("Batch 500 preserves all ten page 99 rows and masks every printed identifier", () => {
  for (const [id, name, sourceRecordId, hasPrivateIdentifier] of cohort) {
    const person = profile(id);
    expect(person).toMatchObject({ display_name: name });
    const sourceRecord = person.source_records.find(
      (record: { source_record_id: string }) => record.source_record_id === sourceRecordId,
    );
    expect(sourceRecord).toMatchObject({
      box: "156",
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

test("Batch 500 publishes three identifier-confirmed occupations without employers", () => {
  const occupations = new Map([
    ["62a6316b-a612-5d6e-baa6-d4ee8673673a", "Warehousing, storekeeping, handling, loading, unloading, or related occupation, n.e.c."],
    ["44229cf5-f9c6-5547-a640-c999cc95ba33", "Railroad clerks, not elsewhere classified"],
    ["e984ea64-f5cc-5691-902d-8d1ac1672d4b", "Semiskilled occupation in manufacture of radios and phonographs"],
  ]);
  for (const [id, occupation] of occupations) {
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
        relationship_type: "unknown",
        temporal_basis: "strongly_date_bounded",
        claim_confidence: "medium",
        publication_status: "publish_qualified",
      }),
    );
  }
  expect(JSON.stringify(profile("e984ea64-f5cc-5691-902d-8d1ac1672d4b"))).toContain(
    "data anomaly",
  );
});

test("Batch 500 preserves Gregg Crouch's evidence and identifier conflict", () => {
  const gregg = profile("262bac81-d2be-5b79-8012-54eceb89ec80");
  expect(gregg).toMatchObject({
    identity_status: "high_confidence",
    personnel_category: "enlisted_army_personnel",
    commissioned_officer: false,
    research_status: "conflicting_sources",
    immediate_pre_oss_affiliations: [],
    last_civilian_pre_service: [],
  });
  expect(gregg.name_variants).toContain("Gregg Elwyn Crouch");
  expect(gregg.other_pre_oss_affiliations).toEqual(
    expect.arrayContaining([
      expect.objectContaining({
        canonical_organization: "Washta High School",
        relationship_type: "student",
        end_date: "1943",
        claim_confidence: "high",
      }),
      expect.objectContaining({
        canonical_organization: "United States Army Air Corps",
        relationship_type: "military_assignment",
        temporal_basis: "temporal_relation_uncertain",
        claim_confidence: "medium",
      }),
      expect.objectContaining({
        occupation: "Tinsmiths, coppersmiths, and sheet metal workers",
        canonical_organization: null,
        claim_confidence: "medium",
      }),
    ]),
  );
  expect(gregg.claims).toEqual(
    expect.arrayContaining([
      expect.objectContaining({ claim_type: "identity", claim_confidence: "high" }),
      expect.objectContaining({ claim_type: "other_pre_oss_affiliation", claim_confidence: "high" }),
    ]),
  );
  expect(JSON.stringify(gregg)).toContain("identifier");
  expect(JSON.stringify(gregg)).toContain("differs by one");
});

test("Batch 500 withholds Arthur Crossley's different-identifier occupation candidate", () => {
  const arthur = profile("f1b41fee-b483-5aa2-bcc1-8237c625cab3");
  expect(arthur).toMatchObject({
    identity_status: "ambiguous",
    personnel_category: "unknown_or_indeterminate",
    commissioned_officer: null,
    research_status: "needs_identity_review",
    immediate_pre_oss_affiliations: [],
    last_civilian_pre_service: [],
    other_pre_oss_affiliations: [],
    claims: [],
  });
  expect(JSON.stringify(arthur)).toContain("W-prefixed");
});

test("Batch 500 retains five unresolved or ambiguous archival profiles", () => {
  for (const id of [
    "d29d09eb-caf5-56bb-98e3-383f542ee39e",
    "774bcf91-44a4-58a6-9e51-0a5bb687a683",
    "a89936c7-8775-53f2-b0fb-b0c6d17f960d",
    "5bf50f1c-5a7b-5310-83a8-a38baed557b1",
    "1af8322e-3d2b-5657-a6bb-582901396464",
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

test("Batch 500 corrects every previously identified code 699 profile", () => {
  for (const id of [
    "3f59d5a5-1e4b-57f6-936d-75e5d3fe354b",
    "e3d3ebd1-3c70-535d-a092-f52630dcce15",
    "d9ee343c-50ab-5db4-b059-1b6dffa9b3a3",
  ]) {
    const person = profile(id);
    expect(person.other_pre_oss_affiliations).toContainEqual(
      expect.objectContaining({
        occupation: "Semiskilled occupation in manufacture of radios and phonographs",
      }),
    );
    expect(JSON.stringify(person)).not.toContain("electrical-machinery manufacturing");
  }
});

test("Batch 500 direct routes show evidence, qualification and current coverage", async ({ page }) => {
  expect(stats.research_attempted_people).toBeGreaterThanOrEqual(4768);
  expect(stats.verified_affiliation_people).toBeGreaterThanOrEqual(544);
  expect(stats.verified_employer_people).toBeGreaterThanOrEqual(242);
  expect(stats.archival_review_assessed_people).toBeGreaterThanOrEqual(4723);

  await page.goto("./people/262bac81-d2be-5b79-8012-54eceb89ec80/");
  await expect(page.getByRole("heading", { name: "Gregg E Crouch", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("Gregg Elwyn Crouch");
  await expect(page.locator("main")).toContainText("Washta High School");
  await expect(page.locator("main")).toContainText("United States Army Air Corps");
  await expect(page.locator("main")).toContainText("identifier");

  await page.goto("./people/44229cf5-f9c6-5547-a640-c999cc95ba33/");
  await expect(page.getByRole("heading", { name: "Vernon R Crosby", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("Railroad clerks, not elsewhere classified");

  await page.goto("./people/f1b41fee-b483-5aa2-bcc1-8237c625cab3/");
  await expect(page.getByRole("heading", { name: "Arthur W Crossley", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("No reliable pre-OSS employer has yet been identified");

  expect(profile("66f43b5e-8c87-5771-a901-af97b0c3c8db")).toMatchObject({
    display_name: "Sherman J Crough",
    research_status: "not_started",
  });
});
