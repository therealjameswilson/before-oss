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
  ["8c31d2d3-10ad-5cc8-abb5-8e85d63be34b", "Compton N Crook", "3d292bfe-9091-515d-a0d0-4068fd548bea", "155", true],
  ["cc177b95-a0ed-5eb0-b689-6227bb04f401", "George Crook", "9b407530-28be-580f-883e-381e95467063", "155", false],
  ["558951b5-9d1c-5e0b-8a78-0bb458cbd1f6", "Robert L Croop", "81c092ca-6e34-5561-a8ad-e17e95c5ae47", "155", true],
  ["3f0dbb5d-feb2-5e11-a29d-8c36159daf83", "Hazel Cropsey", "4fdddc6a-a855-5531-af54-1e7181e9769f", "155", false],
  ["57243fa4-32de-52a2-9b5a-87760ed5741c", "Rene Cros", "395a8024-3cf9-5f74-a5cd-1a52e9b7afe8", "156", false],
  ["7708e5e6-ccb2-56c6-8627-aadf8796fce3", "Caleb P Crosby", "dcd2eead-65ec-5b7f-b849-3a10c3ff0883", "156", true],
  ["bf6cc08d-d2f6-58d6-bcac-8e841c846389", "Cushing M Crosby", "bde69b61-7ff2-54b1-bc4d-56180b5bd7fe", "156", true],
  ["e1d65ca0-fd88-533a-9c0f-756ce9dc1202", "Helen P Crosby", "5a0a56cc-2743-50c0-9efd-7be78bfb4f2f", "156", false],
  ["c2dfc4d8-1832-5620-8f04-c19f28bb6771", "Isiah Crosby", "4407662a-d81e-5026-ae16-93838541ce78", "156", true],
  ["835fb815-dfe9-5873-a484-258feb224c72", "Margaret Crosby", "41afa29c-969c-5c05-a99b-748f226e98cb", "156", false],
] as const;

test("Batch 499 preserves all ten page 99 rows and masks every printed identifier", () => {
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
      expect(sourceRecord.serial_masked).toMatch(/^••(?:••)?\d{4}$/);
    } else {
      expect(sourceRecord.serial_masked).toBeNull();
    }
    expect(JSON.stringify(person)).not.toMatch(
      /"serial_number"|"serial_number_raw"|"serial_number_normalized"/,
    );
  }
});

test("Batch 499 preserves Compton Crook's two qualified pathways and date conflict", () => {
  const compton = profile("8c31d2d3-10ad-5cc8-abb5-8e85d63be34b");
  expect(compton).toMatchObject({
    identity_status: "high_confidence",
    personnel_category: "unknown_or_indeterminate",
    commissioned_officer: null,
    research_status: "documented_prewar_employer_found",
    immediate_pre_oss_affiliations: [],
    last_civilian_pre_service: [],
  });
  expect(compton.name_variants).toEqual(
    expect.arrayContaining(["Compton N. Crook", "Compton Newby Crook", "Stephen Tall"]),
  );
  expect(compton.other_pre_oss_affiliations).toContainEqual(
    expect.objectContaining({
      canonical_organization: "Yellowstone National Park",
      role_title: "national park ranger",
      relationship_type: "government_assignment",
      temporal_basis: "documented_prewar",
      claim_confidence: "medium",
    }),
  );
  expect(compton.other_pre_oss_affiliations).toContainEqual(
    expect.objectContaining({
      canonical_organization: "Towson University",
      role_title: "biology faculty member",
      relationship_type: "employment",
      temporal_basis: "documented_prewar",
      claim_confidence: "medium",
    }),
  );
  expect(JSON.stringify(compton)).toContain("1939-versus-1940s");
});

test("Batch 499 publishes two confirmed Army occupations without employers", () => {
  const occupations = new Map([
    ["558951b5-9d1c-5e0b-8a78-0bb458cbd1f6", "Attendants, filling stations and parking lots"],
    ["c2dfc4d8-1832-5620-8f04-c19f28bb6771", "Chauffeurs and drivers, bus, taxi, truck, and tractor"],
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
        temporal_basis: "documented_prewar",
        claim_confidence: "medium",
        publication_status: "publish_qualified",
      }),
    );
  }
  expect(profile("c2dfc4d8-1832-5620-8f04-c19f28bb6771").name_variants).toContain(
    "Isaiah Crosby",
  );
});

test("Batch 499 publishes the French dossier identity without inventing employment", () => {
  const rene = profile("57243fa4-32de-52a2-9b5a-87760ed5741c");
  expect(rene).toMatchObject({
    identity_status: "high_confidence",
    personnel_category: "foreign_or_allied_military_personnel",
    commissioned_officer: true,
    research_status: "requires_archival_review",
    immediate_pre_oss_affiliations: [],
    last_civilian_pre_service: [],
    other_pre_oss_affiliations: [],
  });
  expect(rene.name_variants).toContain("René Cros");
  expect(rene.claims).toContainEqual(
    expect.objectContaining({ claim_type: "identity", claim_confidence: "high" }),
  );
  expect(JSON.stringify(rene)).toContain("GR 28 P 4 175/188");
});

test("Batch 499 keeps Margaret Crosby's fellowship distinct from employment", () => {
  const margaret = profile("835fb815-dfe9-5873-a484-258feb224c72");
  expect(margaret).toMatchObject({
    identity_status: "high_confidence",
    personnel_category: "civilian_professional_or_administrative_grade",
    commissioned_officer: false,
    research_status: "requires_archival_review",
    immediate_pre_oss_affiliations: [],
    last_civilian_pre_service: [],
  });
  expect(margaret.other_pre_oss_affiliations).toContainEqual(
    expect.objectContaining({
      canonical_organization: "American School of Classical Studies at Athens",
      role_title: "Fellow of the Agora; Fellow in charge of Section BB",
      relationship_type: "professional_affiliation",
      start_date: "1935",
      end_date: "1939",
      claim_confidence: "high",
    }),
  );
  expect(margaret.claims).toEqual(
    expect.arrayContaining([
      expect.objectContaining({ claim_type: "identity", claim_confidence: "high" }),
      expect.objectContaining({ claim_type: "other_pre_oss_affiliation", claim_confidence: "high" }),
    ]),
  );
});

test("Batch 499 retains one ambiguous and four unresolved archival profiles", () => {
  expect(profile("cc177b95-a0ed-5eb0-b689-6227bb04f401")).toMatchObject({
    identity_status: "ambiguous",
    personnel_category: "unknown_or_indeterminate",
    commissioned_officer: null,
    research_status: "needs_identity_review",
    claims: [],
  });
  for (const id of [
    "3f0dbb5d-feb2-5e11-a29d-8c36159daf83",
    "7708e5e6-ccb2-56c6-8627-aadf8796fce3",
    "bf6cc08d-d2f6-58d6-bcac-8e841c846389",
    "e1d65ca0-fd88-533a-9c0f-756ce9dc1202",
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
});

test("Batch 499 direct routes show evidence, uncertainty and current coverage", async ({ page }) => {
  expect(stats.research_attempted_people).toBeGreaterThanOrEqual(4758);
  expect(stats.verified_affiliation_people).toBeGreaterThanOrEqual(544);
  expect(stats.verified_employer_people).toBeGreaterThanOrEqual(242);
  expect(stats.archival_review_assessed_people).toBeGreaterThanOrEqual(4713);

  await page.goto("./people/8c31d2d3-10ad-5cc8-abb5-8e85d63be34b/");
  await expect(page.getByRole("heading", { name: "Compton N Crook", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("Yellowstone National Park");
  await expect(page.locator("main")).toContainText("Towson University");
  await expect(page.locator("main")).toContainText("1939-versus-1940s");

  await page.goto("./people/57243fa4-32de-52a2-9b5a-87760ed5741c/");
  await expect(page.getByRole("heading", { name: "Rene Cros", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("Dossier individuel de René CROS");
  await expect(page.locator("main")).toContainText("GR 28 P 4 175/188");

  await page.goto("./people/835fb815-dfe9-5873-a484-258feb224c72/");
  await expect(page.getByRole("heading", { name: "Margaret Crosby", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("American School of Classical Studies at Athens");
  await expect(page.locator("main")).toContainText("Fellow in charge of Section BB");

  await page.goto("./people/c2dfc4d8-1832-5620-8f04-c19f28bb6771/");
  await expect(page.getByRole("heading", { name: "Isiah Crosby", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("Chauffeurs and drivers, bus, taxi, truck, and tractor");

  expect(profile("62a6316b-a612-5d6e-baa6-d4ee8673673a")).toMatchObject({
    display_name: "Paul L Crosby",
    research_status: "not_started",
  });
});
