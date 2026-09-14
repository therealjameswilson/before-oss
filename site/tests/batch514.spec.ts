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
  ["aca39de9-9bd3-5017-ac3d-d48189651ed1", "Arline Custer", "542da2ab-4dc1-539e-9066-99cc1c317838", null, false],
  ["e70b7f19-40fa-532a-87e2-7a7ee03e2f5a", "Dolly V Custer", "1e57a185-ab8b-5190-a62e-257d7ee6d0a4", null, false],
  ["d40d54cd-6550-5c97-83f0-e03e68438cc5", "Edward A Custer", "8e27b830-5b29-5c37-82ca-841fe0ec0759", "Capt", false],
  ["3b483ba6-7065-5bb2-bba4-a2d183b87252", "Maud E Custer", "9c920f1c-973e-5cf0-b567-09fd59410777", null, false],
  ["33b23f34-a94b-55c3-8309-b8880441149b", "Frank J Custode", "778c70ee-5705-5473-a094-06f64dc8f9df", null, false],
  ["d2487f3a-1b18-5a9a-b5d0-7baee1b4becd", "Joseph Cusumano", "5b8d2469-a2cb-5305-af38-cfe58e4e8570", null, true],
  ["05f5e203-d517-5d45-8d1c-4cb37594007c", "Helen M Cuthbertson", "148865d7-1e5e-56c3-b289-d6d3ffd63814", null, false],
  ["931e64e9-70f6-54bd-8a6f-f098e79aa6b7", "Cecile F Cutler", "508a3698-fb02-5a18-84c3-c95d18d928e1", null, false],
  ["18292e40-73fd-5ed3-a410-9bb19389cf24", "Judith B Cutler", "b6fde7d3-d8b9-52cb-80aa-b4bf69888c82", null, false],
  ["9abe9b1c-1da0-565b-b86a-2ef2300dd2fa", "Levern W Cutler", "ab4187ea-597c-579e-aa3d-e3d24d9e1143", null, true],
] as const;

test("Batch 514 preserves page 102 rows 28-37, Captain, and two masked private fields", () => {
  for (const [id, name, sourceRecordId, rank, hasPrivateIdentifier] of cohort) {
    const person = profile(id);
    expect(person).toMatchObject({ display_name: name });
    const sourceRecord = person.source_records.find(
      (record: { source_record_id: string }) => record.source_record_id === sourceRecordId,
    );
    expect(sourceRecord).toMatchObject({
      box: "161",
      archive_location: "230/86/29/04",
      pdf_page: 102,
      rank_as_indexed: rank,
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

test("Batch 514 keeps Edward Custer's printed Captain classification but rejects the name-only Army row", () => {
  const edward = profile("d40d54cd-6550-5c97-83f0-e03e68438cc5");
  expect(edward).toMatchObject({
    identity_status: "ambiguous",
    personnel_category: "commissioned_army_officer",
    commissioned_officer: true,
    research_status: "needs_identity_review",
    immediate_pre_oss_affiliations: [],
    last_civilian_pre_service: [],
    other_pre_oss_affiliations: [],
    claims: [],
  });
  expect(edward.next_action).toContain("name-only row");
});

test("Batch 514 publishes Joseph Cusumano only as an identifier-backed occupation", () => {
  const joseph = profile("d2487f3a-1b18-5a9a-b5d0-7baee1b4becd");
  expect(joseph).toMatchObject({
    identity_status: "confirmed",
    personnel_category: "enlisted_army_personnel",
    commissioned_officer: false,
    research_status: "occupation_only_found",
    immediate_pre_oss_affiliations: [],
    last_civilian_pre_service: [],
  });
  expect(joseph.other_pre_oss_affiliations).toHaveLength(1);
  expect(joseph.other_pre_oss_affiliations[0]).toMatchObject({
    occupation: "Welder or flame cutter",
    relationship_type: "unknown",
    end_date: "1942-10-26",
    temporal_basis: "strongly_date_bounded",
    identity_confidence: "confirmed",
    claim_confidence: "medium",
    organization_id: null,
  });
  expect(joseph.claims).toHaveLength(2);
});

test("Batch 514 publishes Levern Cutler's spaced variant and occupation without inventing a library", () => {
  const levern = profile("9abe9b1c-1da0-565b-b86a-2ef2300dd2fa");
  expect(levern).toMatchObject({
    display_name: "Levern W Cutler",
    identity_status: "confirmed",
    personnel_category: "enlisted_army_personnel",
    commissioned_officer: false,
    research_status: "occupation_only_found",
    immediate_pre_oss_affiliations: [],
    last_civilian_pre_service: [],
  });
  expect(levern.name_variants).toContain("Le Vern W Cutler");
  expect(levern.other_pre_oss_affiliations).toHaveLength(1);
  expect(levern.other_pre_oss_affiliations[0]).toMatchObject({
    occupation: "Library assistant or attendant",
    relationship_type: "unknown",
    end_date: "1943-03-27",
    temporal_basis: "strongly_date_bounded",
    identity_confidence: "confirmed",
    claim_confidence: "medium",
    organization_id: null,
  });
  expect(levern.claims).toHaveLength(2);
});

test("Batch 514 exposes three identity-review profiles without speculative claims", () => {
  for (const id of [
    "aca39de9-9bd3-5017-ac3d-d48189651ed1",
    "d40d54cd-6550-5c97-83f0-e03e68438cc5",
    "33b23f34-a94b-55c3-8309-b8880441149b",
  ]) {
    expect(profile(id)).toMatchObject({
      identity_status: "ambiguous",
      research_status: "needs_identity_review",
      claims: [],
    });
  }
});

test("Batch 514 exposes five unresolved archival-review profiles", () => {
  for (const id of [
    "e70b7f19-40fa-532a-87e2-7a7ee03e2f5a",
    "3b483ba6-7065-5bb2-bba4-a2d183b87252",
    "05f5e203-d517-5d45-8d1c-4cb37594007c",
    "931e64e9-70f6-54bd-8a6f-f098e79aa6b7",
    "18292e40-73fd-5ed3-a410-9bb19389cf24",
  ]) {
    expect(profile(id)).toMatchObject({
      identity_status: "unresolved",
      research_status: "requires_archival_review",
      claims: [],
    });
  }
});

test("Batch 514 coverage advances attempted and archival review without changing verified employer counts", () => {
  expect(stats.research_attempted_people).toBe(4908);
  expect(stats.verified_affiliation_people).toBe(557);
  expect(stats.verified_employer_people).toBe(248);
  expect(stats.archival_review_assessed_people).toBe(4863);
});

test("Batch 514 direct routes expose qualified occupation evidence and unresolved guidance", async ({ page }) => {
  await page.goto("./people/d2487f3a-1b18-5a9a-b5d0-7baee1b4becd/");
  await expect(page.getByRole("heading", { name: "Joseph Cusumano", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("Welder or flame cutter");
  await expect(page.locator("main")).toContainText("occupation");
  await expect(page.locator("main")).not.toContainText("Immediate pre-OSS affiliation\nWelder");

  await page.goto("./people/9abe9b1c-1da0-565b-b86a-2ef2300dd2fa/");
  await expect(page.getByRole("heading", { name: "Levern W Cutler", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("Le Vern W Cutler");
  await expect(page.locator("main")).toContainText("Library assistant or attendant");

  await page.goto("./people/aca39de9-9bd3-5017-ac3d-d48189651ed1/");
  await expect(page.getByRole("heading", { name: "Arline Custer", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("Smithsonian-documented librarian");
  await expect(page.locator("main")).toContainText("No reliable pre-OSS employer");
});
