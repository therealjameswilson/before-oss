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
  ["c96c4f51-63e9-5282-9aae-e138ab0503fe", "Dante Crifasi", "2a68e36f-1209-5092-9bf6-9ce67b09412a", "153", true],
  ["c8af03ef-46af-592a-8694-82538fb44792", "Joseph Crisafulli", "e92e2d1b-384d-5faf-8e90-430169103cb9", "154", false],
  ["db8cac4c-5899-58df-9c73-88ab53816670", "James J Crisalli", "1d0dc017-a0c7-5b1f-8336-2a1ed886f022", "154", true],
  ["ed2c2c0d-16a0-5659-af03-273598068cc3", "Charles B Crisman", "6bbc4058-7ee9-5732-a503-13e9a4e1a945", "154", true],
  ["935c865f-b647-5f14-81f6-83ebc8ce8821", "Robert J Crisman", "9c7839cc-e136-508c-8898-1a005e21c369", "154", false],
  ["0fc7ce09-3a9a-5c0b-bcb6-320baef5a15d", "Donald Crisp", "5b9ff919-d455-52db-9a5c-7be24d958bed", "154", false],
  ["9f7f4ce8-3f43-5c77-b207-61e773384214", "Violet L Crisp", "fb1b4aff-6837-59be-9533-2b9552aa23fc", "154", false],
  ["2a167b88-7d70-5b17-92c7-ba54c2d40c03", "Milo Crissman", "9f8e6393-1e94-52ad-b696-10c5e45376d9", "154", false],
  ["147c9649-4837-502c-b73c-f46a42aff499", "Clyde E Criswell", "eae802ab-ba2b-5e3f-b7f9-7376126810ed", "154", false],
  ["dde7c1c0-fefa-5195-876f-73bd683a1cf8", "Elberta G Crites", "cb06b138-1d2d-51eb-82f7-005a2cdf1df4", "154", false],
] as const;

test("Batch 495 preserves all ten page 98 rows and masks every printed identifier", () => {
  for (const [id, name, sourceRecordId, box, hasPrivateIdentifier] of cohort) {
    const person = profile(id);
    expect(person).toMatchObject({ display_name: name });
    const sourceRecord = person.source_records.find(
      (record: { source_record_id: string }) => record.source_record_id === sourceRecordId,
    );
    expect(sourceRecord).toMatchObject({
      box,
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

test("Batch 495 separates the Chronicle employer from occupation-only findings", () => {
  const crifasi = profile("c96c4f51-63e9-5282-9aae-e138ab0503fe");
  expect(crifasi).toMatchObject({
    identity_status: "high_confidence",
    personnel_category: "commissioned_army_officer",
    commissioned_officer: true,
    research_status: "occupation_only_found",
    immediate_pre_oss_affiliations: [],
    last_civilian_pre_service: [],
  });
  expect(crifasi.name_variants).toContain("Dante D. Crifasi");
  expect(crifasi.other_pre_oss_affiliations).toContainEqual(
    expect.objectContaining({
      occupation: "Telegraph operators",
      temporal_basis: "documented_prewar",
      claim_confidence: "medium",
    }),
  );

  const crisalli = profile("db8cac4c-5899-58df-9c73-88ab53816670");
  expect(crisalli).toMatchObject({
    identity_status: "confirmed",
    personnel_category: "enlisted_army_personnel",
    commissioned_officer: false,
    research_status: "occupation_only_found",
    immediate_pre_oss_affiliations: [],
    last_civilian_pre_service: [],
  });
  expect(crisalli.other_pre_oss_affiliations).toContainEqual(
    expect.objectContaining({
      occupation: "Amusement, recreation, and motion picture occupations, n.e.c.",
      temporal_basis: "documented_prewar",
      claim_confidence: "medium",
    }),
  );

  const crisman = profile("ed2c2c0d-16a0-5659-af03-273598068cc3");
  expect(crisman).toMatchObject({
    identity_status: "confirmed",
    personnel_category: "enlisted_army_personnel",
    commissioned_officer: false,
    research_status: "verified_employer_found",
    immediate_pre_oss_affiliations: [],
  });
  expect(crisman.name_variants).toEqual(
    expect.arrayContaining(["Charles \"Ben\" Crisman", "Ben Crisman"]),
  );
  expect(crisman.last_civilian_pre_service).toContainEqual(
    expect.objectContaining({
      canonical_organization: "San Francisco Chronicle",
      role_title: "editor and reporter; worked on the financial page",
      relationship_type: "employment",
      temporal_basis: "strongly_date_bounded",
      claim_confidence: "high",
    }),
  );
});

test("Batch 495 publishes Donald Crisp as an officer and actor without inventing a studio employer", () => {
  const crisp = profile("0fc7ce09-3a9a-5c0b-bcb6-320baef5a15d");
  expect(crisp).toMatchObject({
    identity_status: "high_confidence",
    personnel_category: "commissioned_army_officer",
    commissioned_officer: true,
    research_status: "occupation_only_found",
    immediate_pre_oss_affiliations: [],
    last_civilian_pre_service: [],
  });
  expect(crisp.other_pre_oss_affiliations).toContainEqual(
    expect.objectContaining({
      canonical_organization: null,
      occupation: "motion-picture actor",
      end_date: "1941-12-26",
      temporal_basis: "documented_prewar",
      claim_confidence: "high",
    }),
  );
  expect(JSON.stringify(crisp)).not.toContain("Twentieth Century-Fox Film Corp.");
});

test("Batch 495 retains unresolved and ambiguous people as archival-review profiles", () => {
  for (const id of [
    "935c865f-b647-5f14-81f6-83ebc8ce8821",
    "9f7f4ce8-3f43-5c77-b207-61e773384214",
    "dde7c1c0-fefa-5195-876f-73bd683a1cf8",
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
  for (const id of [
    "c8af03ef-46af-592a-8694-82538fb44792",
    "2a167b88-7d70-5b17-92c7-ba54c2d40c03",
    "147c9649-4837-502c-b73c-f46a42aff499",
  ]) {
    expect(profile(id)).toMatchObject({
      identity_status: "ambiguous",
      personnel_category: "unknown_or_indeterminate",
      commissioned_officer: null,
      research_status: "needs_identity_review",
      immediate_pre_oss_affiliations: [],
      last_civilian_pre_service: [],
      other_pre_oss_affiliations: [],
      claims: [],
    });
  }
});

test("Batch 495 direct routes show evidence qualifications and current coverage", async ({ page }) => {
  expect(stats.research_attempted_people).toBeGreaterThanOrEqual(4718);
  expect(stats.verified_affiliation_people).toBeGreaterThanOrEqual(538);
  expect(stats.verified_employer_people).toBeGreaterThanOrEqual(240);
  expect(stats.archival_review_assessed_people).toBeGreaterThanOrEqual(4673);

  await page.goto("./people/ed2c2c0d-16a0-5659-af03-273598068cc3/");
  await expect(page.getByRole("heading", { name: "Charles B Crisman", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("San Francisco Chronicle");
  await expect(page.locator("main")).toContainText("not proved to be the immediate pre-OSS affiliation");
  await expect(page.locator("main")).toContainText("another R&A colleague, newspaperman Ben Crisman");

  await page.goto("./people/0fc7ce09-3a9a-5c0b-bcb6-320baef5a15d/");
  await expect(page.getByRole("heading", { name: "Donald Crisp", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("motion-picture actor");
  await expect(page.locator("main")).toContainText("no specific studio is treated as his employer");
  await expect(page.locator("main")).toContainText("OSS colonel");

  await page.goto("./people/c8af03ef-46af-592a-8694-82538fb44792/");
  await expect(page.getByRole("heading", { name: "Joseph Crisafulli", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("multiple exact-name Army candidates");
  await expect(page.locator("main")).toContainText("No reliable pre-OSS employer has yet been identified");

  expect(profile("43fab178-1410-51d7-bd62-630dec3fd025")).toMatchObject({
    display_name: "Charles Crittenden",
    research_status: "not_started",
  });
});
