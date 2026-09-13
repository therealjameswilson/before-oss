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
  ["43fab178-1410-51d7-bd62-630dec3fd025", "Charles Crittenden", "0f6dd4d2-ebc6-50d1-aaa0-70253d1c2539", false],
  ["273cedbc-1189-5733-bc0d-9f5dc560bd56", "James E Crittenden", "cb56b3c5-d3f9-5547-8e03-d0c7abea6b14", true],
  ["88bb0bd3-c32f-5197-9caf-266da2389595", "Constantine J Critzaz", "eb4c54fa-91ca-55be-b595-711194aec27f", false],
  ["e46e6266-11d2-5bfb-8d50-219543f5f126", "Philip F Crocheron", "a1f501f3-bba3-5e64-96b2-ebe2fb3a7295", true],
  ["1aa702fc-b2af-52b7-8bf0-3b7dde120107", "Ernest Crocker", "8c792671-6e29-565f-b582-517479586f73", true],
  ["0aa260cd-b576-5d48-ab9b-539eeb7dcebd", "Charis Crockett", "361fd093-4e90-51ed-84ef-dd5be2619a39", false],
  ["1d95ccc8-5f65-5864-b243-946c005d00ac", "Charles D Crockett", "12b54ef0-6cba-5400-9782-2d5c8050ed6a", false],
  ["d715759e-aef5-5af9-b76c-7a0c0e9fcffd", "David C Crockett", "2d62bd38-b7d8-53eb-94a1-580b9a3bef65", false],
  ["826344d5-ed31-5f11-8b43-60527ef25bb5", "Frederick E Crockett", "7e8eaf26-5cf3-5c78-866a-d700bb4c1649", false],
  ["7df287b2-8a5f-5a21-8be5-bfd788f4b277", "Aristide Crocq", "82693a86-f07e-52a3-a101-2d337693fed6", false],
] as const;

test("Batch 496 preserves all ten page 98 rows and masks every printed identifier", () => {
  for (const [id, name, sourceRecordId, hasPrivateIdentifier] of cohort) {
    const person = profile(id);
    expect(person).toMatchObject({ display_name: name });
    const sourceRecord = person.source_records.find(
      (record: { source_record_id: string }) => record.source_record_id === sourceRecordId,
    );
    expect(sourceRecord).toMatchObject({
      box: "154",
      archive_location: "230/86/29/03",
      pdf_page: 98,
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

test("Batch 496 separates an occupation, an employer, and sponsored expeditions", () => {
  const james = profile("273cedbc-1189-5733-bc0d-9f5dc560bd56");
  expect(james).toMatchObject({
    identity_status: "confirmed",
    personnel_category: "enlisted_army_personnel",
    commissioned_officer: false,
    research_status: "occupation_only_found",
    immediate_pre_oss_affiliations: [],
    last_civilian_pre_service: [],
  });
  expect(james.other_pre_oss_affiliations).toContainEqual(
    expect.objectContaining({
      canonical_organization: null,
      occupation: "Occupations in production of chemical products, n.e.c.",
      temporal_basis: "documented_prewar",
      claim_confidence: "medium",
    }),
  );

  const ernest = profile("1aa702fc-b2af-52b7-8bf0-3b7dde120107");
  expect(ernest).toMatchObject({
    identity_status: "high_confidence",
    research_status: "documented_prewar_employer_found",
    immediate_pre_oss_affiliations: [],
    last_civilian_pre_service: [],
  });
  expect(ernest.other_pre_oss_affiliations).toContainEqual(
    expect.objectContaining({
      canonical_organization: "Arthur D. Little, Inc.",
      relationship_type: "employment",
      temporal_basis: "documented_prewar",
      claim_confidence: "high",
    }),
  );

  for (const id of [
    "0aa260cd-b576-5d48-ab9b-539eeb7dcebd",
    "826344d5-ed31-5f11-8b43-60527ef25bb5",
  ]) {
    const person = profile(id);
    expect(person.immediate_pre_oss_affiliations).toEqual([]);
    expect(person.last_civilian_pre_service).toEqual([]);
    expect(person.other_pre_oss_affiliations).toContainEqual(
      expect.objectContaining({
        canonical_organization: "Academy of Natural Sciences of Philadelphia",
        relationship_type: "professional_affiliation",
        start_date: "1937",
        end_date: "1938",
      }),
    );
  }
});

test("Batch 496 publishes qualified identity and service findings without inventing employers", () => {
  const critzaz = profile("88bb0bd3-c32f-5197-9caf-266da2389595");
  expect(critzaz).toMatchObject({
    identity_status: "probable",
    research_status: "needs_identity_review",
    immediate_pre_oss_affiliations: [],
    last_civilian_pre_service: [],
  });
  expect(critzaz.name_variants).toContain("Constantine J. Critzas");
  expect(critzaz.other_pre_oss_affiliations).toContainEqual(
    expect.objectContaining({
      canonical_organization: "Order of AHEPA",
      relationship_type: "professional_affiliation",
      claim_confidence: "medium",
      publication_status: "publish_qualified",
    }),
  );

  const david = profile("d715759e-aef5-5af9-b76c-7a0c0e9fcffd");
  expect(david).toMatchObject({
    identity_status: "high_confidence",
    personnel_category: "commissioned_army_officer",
    commissioned_officer: true,
    research_status: "requires_archival_review",
    immediate_pre_oss_affiliations: [],
    last_civilian_pre_service: [],
    other_pre_oss_affiliations: [],
  });

  const frederick = profile("826344d5-ed31-5f11-8b43-60527ef25bb5");
  expect(frederick).toMatchObject({
    identity_status: "high_confidence",
    personnel_category: "commissioned_army_officer",
    commissioned_officer: true,
  });

  const crocq = profile("7df287b2-8a5f-5a21-8be5-bfd788f4b277");
  expect(crocq).toMatchObject({
    identity_status: "high_confidence",
    personnel_category: "foreign_or_allied_military_personnel",
    commissioned_officer: true,
    allied_or_foreign_personnel: true,
    research_status: "requires_archival_review",
    other_pre_oss_affiliations: [],
  });
});

test("Batch 496 retains unresolved and ambiguous profiles for archival review", () => {
  for (const id of [
    "43fab178-1410-51d7-bd62-630dec3fd025",
    "e46e6266-11d2-5bfb-8d50-219543f5f126",
  ]) {
    expect(profile(id)).toMatchObject({
      identity_status: "unresolved",
      personnel_category: "unknown_or_indeterminate",
      commissioned_officer: null,
      research_status: "requires_archival_review",
      immediate_pre_oss_affiliations: [],
      last_civilian_pre_service: [],
      other_pre_oss_affiliations: [],
      claims: [],
    });
  }
  expect(profile("1d95ccc8-5f65-5864-b243-946c005d00ac")).toMatchObject({
    identity_status: "ambiguous",
    personnel_category: "unknown_or_indeterminate",
    commissioned_officer: null,
    research_status: "needs_identity_review",
    immediate_pre_oss_affiliations: [],
    last_civilian_pre_service: [],
    other_pre_oss_affiliations: [],
    claims: [],
  });
});

test("Batch 496 direct routes show evidence qualifications and current coverage", async ({ page }) => {
  expect(stats.research_attempted_people).toBeGreaterThanOrEqual(4728);
  expect(stats.verified_affiliation_people).toBeGreaterThanOrEqual(541);
  expect(stats.verified_employer_people).toBeGreaterThanOrEqual(241);
  expect(stats.archival_review_assessed_people).toBeGreaterThanOrEqual(4683);

  await page.goto("./people/1aa702fc-b2af-52b7-8bf0-3b7dde120107/");
  await expect(page.getByRole("heading", { name: "Ernest Crocker", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("Arthur D. Little");
  await expect(page.locator("main")).toContainText("mid-1920s");
  await expect(page.locator("main")).toContainText("does not make it his immediate pre-OSS employer");

  await page.goto("./people/88bb0bd3-c32f-5197-9caf-266da2389595/");
  await expect(page.getByRole("heading", { name: "Constantine J Critzaz", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("Constantine J. Critzas");
  await expect(page.locator("main")).toContainText("probable");
  await expect(page.locator("main")).toContainText("Order of AHEPA");

  await page.goto("./people/d715759e-aef5-5af9-b76c-7a0c0e9fcffd/");
  await expect(page.getByRole("heading", { name: "David C Crockett", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("1st Lt. David C. Crockett");
  await expect(page.locator("main")).toContainText("No reliable pre-OSS employer has yet been identified");

  await page.goto("./people/7df287b2-8a5f-5a21-8be5-bfd788f4b277/");
  await expect(page.getByRole("heading", { name: "Aristide Crocq", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("Aristide Joseph Crocq");
  await expect(page.locator("main")).toContainText("French");

  expect(profile("315f8f64-6115-50b6-8f07-4fafd29a70a1")).toMatchObject({
    display_name: "Diana I Croft",
    research_status: "not_started",
  });
});
