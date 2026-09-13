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
  ["777d3cb7-f27d-59ee-95f9-10f447f4f70a", "Raymond A Cromley", "5040987a-1d74-5f09-a37f-1b0dc480f68b", true],
  ["e2bb5270-6121-5fbd-81ed-dff1eedec629", "Doris D Cromwell", "7f12435c-e242-583f-8ba3-639b245c1b2a", false],
  ["0b58b9ee-0a8b-57bd-bd23-21f4762c194b", "Frederick Cromwell", "08cbeec0-4fb2-5314-9b0f-22d1248dd34d", true],
  ["01f26507-def8-5d0a-b921-a9ccfa644079", "Howard L Cromwell", "94fe874e-1d0f-5afe-b9e2-d7c52ef63503", true],
  ["30a01709-504c-51bf-9dcc-21d5e0d8339c", "Dorothea Cronin", "37fcbd2f-3a53-5d32-bd6a-d4706c9128fa", false],
  ["58dee0d5-c3fd-5bc2-8ee2-167c5c1aa76c", "Edward R Cronin", "d41dd3fe-b636-55ff-bf7b-8e5f6182a032", true],
  ["a215dd72-b842-5e15-9d74-cf8ff37d1f69", "William H Cronin Jr.", "9ab8e940-927b-5592-bba8-2648510e3f23", false],
  ["89b26907-3029-5305-b3be-a5a014fa9aa7", "John L Cronkrite", "9de7b756-b8ab-5645-abf7-882b9df64cd0", true],
  ["366d3665-7f61-5fa6-9a88-5d39924cb917", "Joseph J Crooch", "91383267-632e-53ca-a91a-ebc505ee62a0", true],
  ["c62b8f12-f85a-5819-873c-af89d840ed1a", "Claire F Crook", "1a20b4fb-9e33-5484-80be-ae690eb7b24b", false],
] as const;

test("Batch 498 preserves all ten page 99 rows and masks every printed identifier", () => {
  for (const [id, name, sourceRecordId, hasPrivateIdentifier] of cohort) {
    const person = profile(id);
    expect(person).toMatchObject({ display_name: name });
    const sourceRecord = person.source_records.find(
      (record: { source_record_id: string }) => record.source_record_id === sourceRecordId,
    );
    expect(sourceRecord).toMatchObject({
      box: "155",
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

test("Batch 498 separates Raymond Cromley's last civilian employer from earlier work", () => {
  const raymond = profile("777d3cb7-f27d-59ee-95f9-10f447f4f70a");
  expect(raymond).toMatchObject({
    identity_status: "high_confidence",
    personnel_category: "commissioned_army_officer",
    commissioned_officer: true,
    research_status: "verified_employer_found",
    immediate_pre_oss_affiliations: [],
  });
  expect(raymond.last_civilian_pre_service).toContainEqual(
    expect.objectContaining({
      canonical_organization: "The Wall Street Journal",
      role_title: "correspondent",
      country: "Japan",
      temporal_basis: "strongly_date_bounded",
      claim_confidence: "high",
    }),
  );
  expect(raymond.other_pre_oss_affiliations).toContainEqual(
    expect.objectContaining({
      canonical_organization: "The Japan Advertiser",
      role_title: "financial editor",
      temporal_basis: "documented_prewar",
      claim_confidence: "high",
    }),
  );
});

test("Batch 498 keeps Doris Cromwell's role, trusteeship and timing distinct", () => {
  const doris = profile("e2bb5270-6121-5fbd-81ed-dff1eedec629");
  expect(doris).toMatchObject({
    identity_status: "high_confidence",
    personnel_category: "civilian_professional_or_administrative_grade",
    commissioned_officer: false,
    research_status: "needs_temporal_review",
    immediate_pre_oss_affiliations: [],
    last_civilian_pre_service: [],
  });
  expect(doris.name_variants).toEqual(expect.arrayContaining(["Doris Duke", "Doris Duke Cromwell"]));
  expect(doris.other_pre_oss_affiliations).toContainEqual(
    expect.objectContaining({
      canonical_organization: "United Seamen's Service",
      relationship_type: "employment",
      temporal_basis: "temporal_relation_uncertain",
      claim_confidence: "medium",
      publication_status: "publish_qualified",
    }),
  );
  expect(doris.other_pre_oss_affiliations).toContainEqual(
    expect.objectContaining({
      canonical_organization: "The Duke Endowment",
      role_title: "trustee",
      relationship_type: "professional_affiliation",
      temporal_basis: "documented_prewar",
      claim_confidence: "high",
    }),
  );
});

test("Batch 498 publishes three qualified occupations without employers", () => {
  const occupations = new Map([
    ["01f26507-def8-5d0a-b921-a9ccfa644079", "Technicians, except laboratory"],
    ["89b26907-3029-5305-b3be-a5a014fa9aa7", "Managers and officials, n.e.c."],
    ["366d3665-7f61-5fa6-9a88-5d39924cb917", "Welders and flame cutters"],
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
});

test("Batch 498 retains ambiguity and unresolved archival profiles", () => {
  expect(profile("30a01709-504c-51bf-9dcc-21d5e0d8339c")).toMatchObject({
    identity_status: "high_confidence",
    research_status: "requires_archival_review",
    claims: [expect.objectContaining({ claim_type: "identity", claim_confidence: "high" })],
  });
  expect(profile("58dee0d5-c3fd-5bc2-8ee2-167c5c1aa76c")).toMatchObject({
    identity_status: "ambiguous",
    personnel_category: "unknown_or_indeterminate",
    commissioned_officer: null,
    research_status: "needs_identity_review",
    claims: [],
  });
  for (const id of [
    "0b58b9ee-0a8b-57bd-bd23-21f4762c194b",
    "a215dd72-b842-5e15-9d74-cf8ff37d1f69",
    "c62b8f12-f85a-5819-873c-af89d840ed1a",
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

test("Batch 498 direct routes show named evidence, timing limits and current coverage", async ({ page }) => {
  expect(stats.research_attempted_people).toBeGreaterThanOrEqual(4748);
  expect(stats.verified_affiliation_people).toBeGreaterThanOrEqual(543);
  expect(stats.verified_employer_people).toBeGreaterThanOrEqual(242);
  expect(stats.archival_review_assessed_people).toBeGreaterThanOrEqual(4703);

  await page.goto("./people/777d3cb7-f27d-59ee-95f9-10f447f4f70a/");
  await expect(page.getByRole("heading", { name: "Raymond A Cromley", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("The Wall Street Journal");
  await expect(page.locator("main")).toContainText("The Japan Advertiser");
  await expect(page.locator("main")).toContainText("Last civilian employer before service");

  await page.goto("./people/e2bb5270-6121-5fbd-81ed-dff1eedec629/");
  await expect(page.getByRole("heading", { name: "Doris D Cromwell", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("United Seamen's Service");
  await expect(page.locator("main")).toContainText("The Duke Endowment");
  await expect(page.locator("main")).toContainText("temporal relation uncertain");

  await page.goto("./people/89b26907-3029-5305-b3be-a5a014fa9aa7/");
  await expect(page.getByRole("heading", { name: "John L Cronkrite", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("Managers and officials, n.e.c.");
  await expect(page.locator("main")).toContainText("P0T");

  await page.goto("./people/58dee0d5-c3fd-5bc2-8ee2-167c5c1aa76c/");
  await expect(page.getByRole("heading", { name: "Edward R Cronin", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("Two different exact-name Edward R. Cronin Army rows");

  expect(profile("8c31d2d3-10ad-5cc8-abb5-8e85d63be34b")).toMatchObject({
    display_name: "Compton N Crook",
    research_status: "not_started",
  });
});
