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
  ["4636b761-fb3d-5dc9-9be4-22eea0d86674", "Edmund Czaplinski", "cc43cddb-01d0-571d-b99d-a11a0207b76a", "162", "Sgt", false],
  ["319f574c-ed85-5f9c-ac05-9da8ad929b47", "Wiktor Czarnecki", "b8d1c09f-ad20-5d50-95fe-9bac4d923a63", "162", "Sgt", false],
  ["afdcc764-546c-590e-b679-c3c779affbf0", "John Czebely", "d9eccbe9-5724-56ee-8779-5933d22bb8a5", "162", null, true],
  ["dce57294-738d-5a94-980d-df3821ed4b3e", "Stephanie Czech", "c535f6e8-61bc-59e0-bbb6-d75a525b7e14", "162", null, true],
  ["5973e9b9-4412-53fc-93d6-c9925bed1a90", "Joseph F Czechlewski", "ce0f6eae-fc44-5e51-8ea0-16b28dcd42d8", "162", null, true],
  ["485623fd-a49e-5288-816e-f2e2a378cdc5", "Jozef Czogowski", "db5f5250-2fe7-540e-9a3d-8aa7ffbc07dd", "162", "Sgt", false],
  ["9597340e-98ff-53e3-8a82-59cb7edd653d", "Edward J Czop", "bac89ffb-a3f9-5f48-83cd-7a44c79a7c19", "162", null, true],
  ["c2bd8fde-f390-5789-907e-6ad48256e8ce", "Fred C Czufin", "32220283-d648-5502-ba60-fca1b89f1f4f", "162", null, true],
  ["a1c5165e-750f-549e-b060-62fc8f65c2cc", "William S Czyzewski", "dd9b4f6f-36c4-526a-9468-6e07ecc6bd69", "162", null, true],
  ["a0801077-ae0f-5a72-9a69-a3e37257da2e", "Arnold Daane", "c01678bc-ee51-5f33-9f09-c1f95aaa18fb", "163", null, false],
] as const;

test("Batch 516 preserves page 103 rows 2-11 and masks six private fields", () => {
  for (const [id, name, sourceRecordId, box, rank, hasPrivateIdentifier] of cohort) {
    const person = profile(id);
    expect(person).toMatchObject({ display_name: name });
    const sourceRecord = person.source_records.find(
      (record: { source_record_id: string }) => record.source_record_id === sourceRecordId,
    );
    expect(sourceRecord).toMatchObject({
      box,
      archive_location: "230/86/29/05",
      pdf_page: 103,
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

test("Batch 516 publishes three distinct Project Eagle pathways without recasting them as civilian employment", () => {
  const projectEagle = [
    ["4636b761-fb3d-5dc9-9be4-22eea0d86674", "Edmund Czapliński"],
    ["319f574c-ed85-5f9c-ac05-9da8ad929b47", "Wiktor Szulik"],
    ["485623fd-a49e-5288-816e-f2e2a378cdc5", "Jan Czogowski"],
  ] as const;

  for (const [id, variant] of projectEagle) {
    const person = profile(id);
    expect(person).toMatchObject({
      identity_status: "high_confidence",
      personnel_category: "foreign_or_allied_military_personnel",
      commissioned_officer: false,
      research_status: "completed",
      last_civilian_pre_service: [],
    });
    expect(person.name_variants).toContain(variant);
    expect(person.immediate_pre_oss_affiliations).toHaveLength(1);
    expect(person.immediate_pre_oss_affiliations[0]).toMatchObject({
      canonical_organization: "Independent Grenadier Company, Polish Armed Forces in the West",
      relationship_type: "military_assignment",
      temporal_basis: "explicit_immediate",
      identity_confidence: "high_confidence",
      claim_confidence: "high",
      publication_status: "published",
    });
  }

  for (const id of [
    "4636b761-fb3d-5dc9-9be4-22eea0d86674",
    "319f574c-ed85-5f9c-ac05-9da8ad929b47",
  ]) {
    const person = profile(id);
    expect(person.other_pre_oss_affiliations).toHaveLength(1);
    expect(person.other_pre_oss_affiliations[0]).toMatchObject({
      canonical_organization: "German Army (Wehrmacht)",
      relationship_type: "military_assignment",
      temporal_basis: "documented_prewar",
      claim_confidence: "medium",
      publication_status: "publish_qualified",
    });
    expect(person.claims.some((claim: { match_notes: string }) =>
      claim.match_notes?.includes("rank forms differ"),
    )).toBe(true);
  }

  const jozef = profile("485623fd-a49e-5288-816e-f2e2a378cdc5");
  expect(jozef.other_pre_oss_affiliations).toHaveLength(2);
  expect(jozef.other_pre_oss_affiliations).toEqual(
    expect.arrayContaining([
      expect.objectContaining({ occupation: "Factory worker", organization_id: null }),
      expect.objectContaining({ canonical_organization: "German Army (Wehrmacht)" }),
    ]),
  );
});

test("Batch 516 separates Joseph Czechlewski's last civilian employer, earlier law practice, and occupation conflict", () => {
  const joseph = profile("5973e9b9-4412-53fc-93d6-c9925bed1a90");
  expect(joseph).toMatchObject({
    identity_status: "confirmed",
    personnel_category: "commissioned_army_officer",
    commissioned_officer: true,
    research_status: "verified_employer_found",
    immediate_pre_oss_affiliations: [],
  });
  expect(joseph.last_civilian_pre_service).toHaveLength(1);
  expect(joseph.last_civilian_pre_service[0]).toMatchObject({
    canonical_organization: "New York County District Attorney's Office",
    role_title: "Assistant district attorney",
    relationship_type: "government_assignment",
    temporal_basis: "strongly_date_bounded",
    claim_confidence: "high",
    publication_status: "published",
  });
  expect(joseph.other_pre_oss_affiliations).toHaveLength(1);
  expect(joseph.other_pre_oss_affiliations[0]).toMatchObject({
    role_title: "Attorney",
    relationship_type: "self_employment",
    temporal_basis: "documented_prewar",
    claim_confidence: "high",
  });
  expect(joseph.claims).toEqual(
    expect.arrayContaining([
      expect.objectContaining({
        claim_type: "occupation",
        claim_confidence: "conflicting",
        publication_status: "conflicting",
      }),
    ]),
  );
});

test("Batch 516 publishes bounded occupations while leaving employers and institutions unknown", () => {
  const occupationCases = [
    ["afdcc764-546c-590e-b679-c3c779affbf0", "General farmer", "unknown"],
    ["9597340e-98ff-53e3-8a82-59cb7edd653d", "Shipping and receiving clerk", "unknown"],
    ["c2bd8fde-f390-5789-907e-6ad48256e8ce", "Student", "student"],
  ] as const;

  for (const [id, occupation, relationship] of occupationCases) {
    const person = profile(id);
    expect(person).toMatchObject({
      identity_status: "confirmed",
      personnel_category: "enlisted_army_personnel",
      commissioned_officer: false,
      research_status: "occupation_only_found",
      immediate_pre_oss_affiliations: [],
      last_civilian_pre_service: [],
    });
    expect(person.other_pre_oss_affiliations).toHaveLength(1);
    expect(person.other_pre_oss_affiliations[0]).toMatchObject({
      organization_id: null,
      occupation,
      relationship_type: relationship,
      temporal_basis: "strongly_date_bounded",
      claim_confidence: "medium",
      publication_status: "publish_qualified",
    });
  }

  expect(profile("c2bd8fde-f390-5789-907e-6ad48256e8ce").name_variants).toContain(
    "Frederick Cutting Czufin",
  );
});

test("Batch 516 preserves Stephanie Czech's existing sequence and William Czyzewski's unresolved status", () => {
  const stephanie = profile("dce57294-738d-5a94-980d-df3821ed4b3e");
  expect(stephanie).toMatchObject({
    identity_status: "high_confidence",
    personnel_category: "commissioned_army_officer",
    commissioned_officer: true,
    research_status: "verified_employer_found",
  });
  expect(stephanie.immediate_pre_oss_affiliations[0]).toMatchObject({
    canonical_organization: "Women's Army Corps",
    relationship_type: "military_assignment",
    temporal_basis: "explicit_immediate",
    claim_confidence: "high",
  });
  expect(stephanie.last_civilian_pre_service[0]).toMatchObject({
    canonical_organization: "Texas Oil Company",
    role_title: "Librarian and researcher",
    relationship_type: "employment",
    claim_confidence: "high",
  });

  expect(profile("a1c5165e-750f-549e-b060-62fc8f65c2cc")).toMatchObject({
    identity_status: "unresolved",
    personnel_category: "unknown_or_indeterminate",
    commissioned_officer: null,
    research_status: "requires_archival_review",
    immediate_pre_oss_affiliations: [],
    last_civilian_pre_service: [],
    other_pre_oss_affiliations: [],
    claims: [],
  });
});

test("Batch 516 keeps Arnold Daane's name-only newspaper match conditional", () => {
  const arnold = profile("a0801077-ae0f-5a72-9a69-a3e37257da2e");
  expect(arnold).toMatchObject({
    identity_status: "probable",
    personnel_category: "unknown_or_indeterminate",
    commissioned_officer: null,
    research_status: "documented_prewar_employer_found",
    immediate_pre_oss_affiliations: [],
    last_civilian_pre_service: [],
  });
  expect(arnold.other_pre_oss_affiliations).toHaveLength(1);
  expect(arnold.other_pre_oss_affiliations[0]).toMatchObject({
    canonical_organization: "Daily Banner (Cambridge, Maryland)",
    role_title: "Owner and publisher",
    relationship_type: "self_employment",
    temporal_basis: "documented_prewar",
    identity_confidence: "probable",
    claim_confidence: "medium",
    publication_status: "publish_qualified",
  });
  expect(arnold.claims[0].claim_text).toContain("If the probable identity match is correct");
});

test("Batch 516 coverage and direct routes expose evidence, caveats, and unresolved guidance", async ({ page }) => {
  expect(stats.source_rows).toBe(23978);
  expect(stats.person_entities).toBe(23940);
  expect(stats.research_attempted_people).toBe(4927);
  expect(stats.verified_affiliation_people).toBe(562);
  expect(stats.verified_employer_people).toBe(250);
  expect(stats.archival_review_assessed_people).toBe(4882);

  await page.goto("./people/319f574c-ed85-5f9c-ac05-9da8ad929b47/");
  await expect(page.getByRole("heading", { name: "Wiktor Czarnecki", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("Wiktor Szulik");
  await expect(page.locator("main")).toContainText("Independent Grenadier Company");

  await page.goto("./people/5973e9b9-4412-53fc-93d6-c9925bed1a90/");
  await expect(page.getByRole("heading", { name: "Joseph F Czechlewski", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("New York County District Attorney's Office");
  await expect(page.locator("main")).toContainText("conflicting");

  await page.goto("./people/c2bd8fde-f390-5789-907e-6ad48256e8ce/");
  await expect(page.getByRole("heading", { name: "Fred C Czufin", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("Frederick Cutting Czufin");
  await expect(page.locator("main")).toContainText("Student");

  await page.goto("./people/a0801077-ae0f-5a72-9a69-a3e37257da2e/");
  await expect(page.getByRole("heading", { name: "Arnold Daane", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("If the probable identity match is correct");
  await expect(page.locator("main")).toContainText("Daily Banner");

  await page.goto("./people/a1c5165e-750f-549e-b060-62fc8f65c2cc/");
  await expect(page.getByRole("heading", { name: "William S Czyzewski", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("No reliable pre-OSS employer has yet been identified");
});
