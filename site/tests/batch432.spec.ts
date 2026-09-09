import { expect, test } from "@playwright/test";
import fs from "node:fs";

const people = JSON.parse(
  fs.readFileSync(new URL("../src/data/generated/people.json", import.meta.url), "utf8"),
);
const organizations = JSON.parse(
  fs.readFileSync(new URL("../src/data/generated/organizations.json", import.meta.url), "utf8"),
);
const profile = (id: string) =>
  people.find((person: { person_id: string }) => person.person_id === id);

test("Batch 432 publishes Joseph Clinton's Army occupation without inventing an employer", async ({ page }) => {
  const joseph = profile("7948c9c5-d39a-5124-a6e3-ad760e41425d");
  expect(joseph).toMatchObject({
    display_name: "Joseph F Clinton",
    identity_status: "confirmed",
    personnel_category: "enlisted_army_personnel",
    commissioned_officer: false,
    research_status: "occupation_only_found",
  });
  expect(joseph.immediate_pre_oss_affiliations).toEqual([]);
  expect(joseph.last_civilian_pre_service).toEqual([]);
  expect(joseph.other_pre_oss_affiliations).toContainEqual(
    expect.objectContaining({
      organization_id: null,
      occupation: "Embalmers and undertakers",
      relationship_type: "unknown",
      temporal_basis: "temporal_relation_uncertain",
      claim_confidence: "medium",
    }),
  );

  await page.goto(`./people/${joseph.person_id}/`);
  await expect(page.getByRole("heading", { name: "Joseph F Clinton", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("Embalmers and undertakers");
  await expect(page.locator("main")).toContainText("No reliable pre-OSS employer has yet been identified");
});

test("Batch 432 keeps Evelyne Clopet's Allied pathway distinct from civilian employment", async ({ page }) => {
  const evelyne = profile("7b9e0915-bb24-5fbf-9b0e-8402cba906e1");
  expect(evelyne).toMatchObject({
    display_name: "Evelyne Clopet",
    identity_status: "confirmed",
    personnel_category: "foreign_or_allied_military_personnel",
    commissioned_officer: true,
    allied_or_foreign_personnel: true,
    research_status: "completed",
  });
  expect(evelyne.last_civilian_pre_service).toEqual([]);
  expect(evelyne.immediate_pre_oss_affiliations).toContainEqual(
    expect.objectContaining({
      canonical_organization: "Bureau central de renseignements et d'action",
      organization_name_as_found: "BCRA",
      role_title: "radio operator",
      relationship_type: "military_assignment",
      start_date: "1944-02",
      temporal_basis: "strongly_date_bounded",
      claim_confidence: "high",
    }),
  );
  expect(evelyne.other_pre_oss_affiliations).toContainEqual(
    expect.objectContaining({
      canonical_organization: "Corps féminin des transmissions",
      role_title: "volunteer",
      relationship_type: "military_assignment",
      end_date: "1944-02",
      temporal_basis: "documented_prewar",
      claim_confidence: "high",
    }),
  );
  expect(evelyne.claims).toContainEqual(
    expect.objectContaining({
      claim_type: "archival_file_status",
      claim_confidence: "high",
      publication_status: "published",
    }),
  );

  const bcra = organizations.find(
    (organization: { canonical_name: string }) =>
      organization.canonical_name === "Bureau central de renseignements et d'action",
  );
  expect(bcra).toMatchObject({
    historical_name: "Bureau central de renseignements et d'actions",
    organization_type: "Free French intelligence service",
    sector: "military",
    country: "France",
  });

  await page.goto(`./people/${evelyne.person_id}/`);
  await expect(page.getByRole("heading", { name: "Evelyne Clopet", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("BCRA");
  await expect(page.locator("main")).toContainText("radio operator");
  await expect(page.locator("main")).toContainText("Corps féminin des transmissions");
  await expect(page.locator("main")).toContainText("No reliable pre-OSS employer has yet been identified");
  await expect(page.getByRole("link", { name: "Évelyne Clopet (1922-1944), profile in Aux combattantes" }).first()).toBeVisible();
});

test("Batch 432 qualifies Charles Cloninger and retains John Clive's existing chronology", async ({ page }) => {
  const charles = profile("1158e305-2053-5200-874b-af517be22013");
  expect(charles).toMatchObject({
    display_name: "Charles K Cloninger",
    identity_status: "probable",
    personnel_category: "commissioned_army_officer",
    commissioned_officer: true,
    research_status: "requires_archival_review",
  });
  expect(charles.immediate_pre_oss_affiliations).toEqual([]);
  expect(charles.last_civilian_pre_service).toEqual([]);
  expect(charles.other_pre_oss_affiliations).toEqual([]);
  expect(charles.claims).toContainEqual(
    expect.objectContaining({
      claim_type: "identity",
      claim_confidence: "medium",
      publication_status: "publish_qualified",
      match_notes: expect.stringContaining("same-name 1942 Army merged-file row"),
    }),
  );

  await page.goto(`./people/${charles.person_id}/`);
  await expect(page.getByRole("heading", { name: "Charles K Cloninger", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("probably corresponds");
  await expect(page.getByRole("link", { name: "Artillery Officer Candidate School Graduates, 1941-1973: Alphabetical List" }).first()).toBeVisible();

  const john = profile("bc1757bd-9946-593f-8575-8c470dd6c61f");
  expect(john).toMatchObject({
    display_name: "John L Clive",
    identity_status: "high_confidence",
    research_status: "requires_archival_review",
    research_attempt_count: 2,
  });
  expect(john.immediate_pre_oss_affiliations).toContainEqual(
    expect.objectContaining({
      canonical_organization: "United States Army",
      relationship_type: "military_assignment",
      temporal_basis: "explicit_immediate",
      claim_confidence: "high",
    }),
  );
  expect(john.other_pre_oss_affiliations).toContainEqual(
    expect.objectContaining({
      canonical_organization: "University of North Carolina at Chapel Hill",
      organization_name_as_found: "University of North Carolina",
      relationship_type: "student",
      temporal_basis: "documented_prewar",
      claim_confidence: "high",
    }),
  );
  expect(john.last_civilian_pre_service).toEqual([]);
});

test("Batch 432 preserves every page 84 source row and masks private identifiers", async ({ page }) => {
  const expected = [
    ["dd2bc6f0-4f73-530b-9945-907f7b321b05", "Edward J Clinton", "0f2e183d-e19f-5368-8d9d-69cd8219f6d1", "unresolved", "requires_archival_review", null],
    ["7948c9c5-d39a-5124-a6e3-ad760e41425d", "Joseph F Clinton", "b94b8359-05cb-5e7e-8817-632c8e610995", "confirmed", "occupation_only_found", null],
    ["dc9ac8f5-9605-53de-adc8-1dfb2483d915", "Margery T Clinton", "8e1b39a4-78a9-5bb3-917d-44cf61951458", "unresolved", "requires_archival_review", null],
    ["bc1757bd-9946-593f-8575-8c470dd6c61f", "John L Clive", "d1913b10-ab2d-56b3-a508-99e5264a7645", "high_confidence", "requires_archival_review", null],
    ["0587c1e5-d84f-52a4-b0d8-e9e305b68b50", "Frank T Cloak", "13566c19-417a-59ef-942c-54ccc3a0be16", "unresolved", "requires_archival_review", null],
    ["9e856539-1226-5c69-a0ab-c8017e6ac38b", "Jan Cloesmeyer", "f77d3143-5380-5030-b08b-f8d0a36593a0", "ambiguous", "requires_archival_review", null],
    ["c159da7c-8829-5c17-838f-11163cf1aa88", "Ida M Clohan", "4dbe9b1a-e0f1-50da-a840-f99af480da80", "unresolved", "requires_archival_review", null],
    ["9cbd4a53-b220-59dc-a9c8-b6650d1511f8", "Elton Clohecy", "6ed67bca-1e5a-50ce-a389-4822785c96e8", "ambiguous", "requires_archival_review", null],
    ["1158e305-2053-5200-874b-af517be22013", "Charles K Cloninger", "6fcf697e-8a17-5075-82f5-6d94d1bafe4c", "probable", "requires_archival_review", "Lt"],
    ["7b9e0915-bb24-5fbf-9b0e-8402cba906e1", "Evelyne Clopet", "7ce71ba7-e5e3-5166-92d3-f76d201c3510", "confirmed", "completed", "Lt"],
  ];

  for (const [id, name, sourceRecordId, identityStatus, researchStatus, rank] of expected) {
    const person = profile(String(id));
    expect(person).toMatchObject({
      display_name: name,
      identity_status: identityStatus,
      research_status: researchStatus,
    });
    expect(person.source_records[0]).toMatchObject({
      source_record_id: sourceRecordId,
      pdf_page: 84,
      box: "130",
      archive_location: "230/86/28/07",
      rank_as_indexed: rank,
    });
    expect(JSON.stringify(person)).not.toMatch(
      /"serial_number"|"serial_number_raw"|"serial_number_normalized"/,
    );
  }

  for (const id of [
    "dd2bc6f0-4f73-530b-9945-907f7b321b05",
    "7948c9c5-d39a-5124-a6e3-ad760e41425d",
    "bc1757bd-9946-593f-8575-8c470dd6c61f",
    "1158e305-2053-5200-874b-af517be22013",
  ]) {
    expect(profile(id).source_records[0].serial_masked).toMatch(/^••••.{4}$/u);
  }

  await page.goto("./people/?q=Evelyne%20Clopet");
  await expect(page.getByRole("link", { name: "Evelyne Clopet", exact: true })).toBeVisible();
});
