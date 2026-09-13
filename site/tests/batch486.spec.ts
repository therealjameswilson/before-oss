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
  ["3bced88b-0fdb-5d68-9525-4ca6e7e5bf79", "Marjorie L Cox", "6523fffd-554b-5420-9285-7543d81095b5", false],
  ["c5150a19-e403-5a65-b5b3-baa56fd26e77", "Miriam Cox", "6d01b7f5-f65f-52e4-9cae-7675f8b244ab", false],
  ["6a2ce5ab-2a07-543f-afd7-a5f27472d1ff", "Nellie P Cox", "39066cc5-1cd3-5a51-897d-3641515c18fc", false],
  ["69ff6207-bfa9-5de2-909f-82bd98f7705f", "Norwood S Cox", "f8e59716-5ca5-5f8c-aa02-b5d3489d89fb", true],
  ["d88fb96d-9bd2-5638-b030-ee9283fcfa97", "Richard D Cox", "516748b0-4bd8-5dcd-a9e2-eb50b1adc9b7", true],
  ["963dd09a-fd52-5af1-90d5-beb13ffdf625", "Robin L Cox Jr.", "dd20b0bd-8e7d-5f65-9cc1-f1e1c525cbb1", false],
  ["6d05b244-4c1e-51b6-a6a7-3f56f70113bc", "Russell C Cox", "b8a22e19-7e28-59ce-b1fb-8c147a2f7944", true],
  ["2784afda-6cc4-5912-bc0e-46dd183ac0fa", "William N Cox", "4a03a384-bae2-5726-aabf-afd2a655e834", true],
  ["db8bb6b4-22a5-52b7-89d5-789ebbff94ad", "Henry B Coxe", "222b3de8-47cd-53c6-a92f-9055163a1f4a", true],
  ["64b54c82-341f-5a50-9e4c-187c2c9f3b2e", "Maryette A Coxe", "86cf8e91-7d41-5ea9-8a2b-8b43bd96aa78", false],
] as const;

test("Batch 486 preserves all ten page 96 rows and masks private identifiers", () => {
  for (const [id, name, sourceRecordId, hasPrivateIdentifier] of cohort) {
    const person = profile(id);
    expect(person).toMatchObject({ display_name: name });
    const sourceRecord = person.source_records.find(
      (record: { source_record_id: string }) => record.source_record_id === sourceRecordId,
    );
    expect(sourceRecord).toMatchObject({
      box: "150",
      archive_location: "230/86/29/03",
      pdf_page: 96,
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

test("Batch 486 distinguishes Russell Cox student status from employment", () => {
  const russell = profile("6d05b244-4c1e-51b6-a6a7-3f56f70113bc");
  expect(russell).toMatchObject({
    display_name: "Russell C Cox",
    identity_status: "confirmed",
    personnel_category: "enlisted_army_personnel",
    commissioned_officer: false,
    research_status: "occupation_only_found",
    immediate_pre_oss_affiliations: [],
    last_civilian_pre_service: [],
  });
  expect(russell.other_pre_oss_affiliations).toContainEqual(
    expect.objectContaining({
      role_title: "Student",
      organization_id: null,
      relationship_type: "student",
      end_date: "1943-03-19",
      temporal_basis: "strongly_date_bounded",
      claim_confidence: "medium",
      publication_status: "publish_qualified",
    }),
  );
});

test("Batch 486 publishes Henry Coxe's qualified 1939 law-firm affiliation", () => {
  const henry = profile("db8bb6b4-22a5-52b7-89d5-789ebbff94ad");
  expect(henry).toMatchObject({
    display_name: "Henry B Coxe",
    identity_status: "high_confidence",
    personnel_category: "commissioned_army_officer",
    commissioned_officer: true,
    research_status: "documented_prewar_employer_found",
    immediate_pre_oss_affiliations: [],
    last_civilian_pre_service: [],
  });
  expect(henry.name_variants).toEqual(
    expect.arrayContaining(["Henry B. Coxe, Jr.", "Coxe, Henry B., Jr."]),
  );
  expect(henry.other_pre_oss_affiliations).toContainEqual(
    expect.objectContaining({
      canonical_organization: "Barratt Coxe",
      role_title: "Attorney",
      relationship_type: "employment",
      temporal_basis: "documented_prewar",
      claim_confidence: "medium",
      publication_status: "publish_qualified",
    }),
  );
  expect(henry.claims).toEqual(
    expect.arrayContaining([
      expect.objectContaining({ claim_type: "identity", claim_confidence: "high" }),
      expect.objectContaining({
        claim_type: "other_pre_oss_affiliation",
        claim_confidence: "medium",
      }),
    ]),
  );
});

test("Batch 486 exposes Norwood Cox's conflict and keeps unresolved leads out of public facts", () => {
  const norwood = profile("69ff6207-bfa9-5de2-909f-82bd98f7705f");
  expect(norwood).toMatchObject({
    identity_status: "conflicting",
    personnel_category: "unknown_or_indeterminate",
    commissioned_officer: null,
    research_status: "conflicting_sources",
    immediate_pre_oss_affiliations: [],
    last_civilian_pre_service: [],
    other_pre_oss_affiliations: [],
  });
  expect(norwood.claims).toContainEqual(
    expect.objectContaining({
      claim_type: "identity",
      claim_confidence: "conflicting",
      publication_status: "conflicting",
    }),
  );

  for (const id of [
    "3bced88b-0fdb-5d68-9525-4ca6e7e5bf79",
    "c5150a19-e403-5a65-b5b3-baa56fd26e77",
    "6a2ce5ab-2a07-543f-afd7-a5f27472d1ff",
    "d88fb96d-9bd2-5638-b030-ee9283fcfa97",
    "963dd09a-fd52-5af1-90d5-beb13ffdf625",
    "2784afda-6cc4-5912-bc0e-46dd183ac0fa",
  ]) {
    const person = profile(id);
    expect(person.identity_status).toBe("unresolved");
    expect(person.research_status).toBe("requires_archival_review");
    expect(person.immediate_pre_oss_affiliations).toEqual([]);
    expect(person.last_civilian_pre_service).toEqual([]);
    expect(person.other_pre_oss_affiliations).toEqual([]);
    expect(person.claims).toEqual([]);
  }
});

test("Batch 486 profiles and coverage render the reviewed outcomes", async ({ page }) => {
  expect(stats.research_attempted_people).toBeGreaterThanOrEqual(4629);
  expect(stats.verified_affiliation_people).toBeGreaterThanOrEqual(530);
  expect(stats.verified_employer_people).toBeGreaterThanOrEqual(235);
  expect(stats.archival_review_assessed_people).toBeGreaterThanOrEqual(4584);

  await page.goto("./people/db8bb6b4-22a5-52b7-89d5-789ebbff94ad/");
  await expect(page.getByRole("heading", { name: "Henry B Coxe", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("Barratt Coxe");
  await expect(page.locator("main")).toContainText("documented prewar");
  await expect(page.locator("main")).toContainText(
    "CIA Operations Officer Lucien Conein: A Study in Contrasts and Controversy",
  );
  await expect(page.locator("main")).toContainText(
    "No publishable immediate affiliation or civilian employer is recorded yet",
  );

  await page.goto("./people/64b54c82-341f-5a50-9e4c-187c2c9f3b2e/");
  await expect(page.getByRole("heading", { name: "Maryette A Coxe", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("War Report, Office of Strategic Services");
  await expect(page.locator("main")).toContainText(
    "No reliable pre-OSS employer has yet been identified",
  );
});
