import { expect, test } from "@playwright/test";
import fs from "node:fs";

const people = JSON.parse(
  fs.readFileSync(new URL("../src/data/generated/people.json", import.meta.url), "utf8"),
);
const stats = JSON.parse(
  fs.readFileSync(new URL("../src/data/generated/stats.json", import.meta.url), "utf8"),
);
const organizations = JSON.parse(
  fs.readFileSync(new URL("../src/data/generated/organizations.json", import.meta.url), "utf8"),
);
const analytics = JSON.parse(
  fs.readFileSync(new URL("../src/data/generated/analytics.json", import.meta.url), "utf8"),
);
const profile = (id: string) =>
  people.find((person: { person_id: string }) => person.person_id === id);

const cohort = [
  ["d5ab2677-e4e5-5ae3-92bc-402aa146f1a8", "Ruth B Culbertson", "f898d193-be1d-5317-bcce-dc502f16a3ee", false],
  ["e264bb1d-1b97-5b50-b31f-bd349e60220d", "William S Culbertson", "3c5d1910-4185-5842-9dcc-a046f0fab160", true],
  ["58c59371-4b84-5aa7-b579-177fbc5c5d14", "William D Culbertson", "70175a23-718d-536d-a546-5af933b1f12e", true],
  ["236ffd5a-0963-5cc2-89be-f0f23fa3bb48", "Helen M Culgen", "6f03f888-8173-5c07-bc1d-fb3eac8c173e", false],
  ["164e7ced-dccf-52b4-a5a8-5ad511223453", "Thomas M Cullens", "c6a75d1c-fdf6-5bd2-9ce1-b429db21c090", true],
  ["c0f013c3-c59c-5e10-8f88-b9861131dfca", "Augustine Cullinan", "0682bc43-c6dc-5983-b985-86b9f66fa403", false],
  ["3b83a566-7eed-5b87-b1f1-ab411cc887d7", "Charles H Cullinan", "bb847826-74d6-5dde-9781-81bef80ffdde", false],
  ["1a34a633-a046-58e7-8c7c-a088cb82a6c8", "Caroline E Cullings", "8410df88-42dc-58d5-9b4a-7fcf9595ca99", false],
  ["c62ad924-7552-571c-81de-d64b0278240e", "James S Cullison", "fc67468f-c7d8-516c-a29e-426d50c75bfb", true],
  ["f6116d9f-08fb-5b05-bffa-b92b4da219cd", "Carson W Culp", "a9f284e5-2838-5eb2-8585-23b3a03a47fe", true],
] as const;

test("Batch 505 preserves all ten page 100 rows and masks every printed identifier", () => {
  for (const [id, name, sourceRecordId, hasPrivateIdentifier] of cohort) {
    const person = profile(id);
    expect(person).toMatchObject({ display_name: name });
    const sourceRecord = person.source_records.find(
      (record: { source_record_id: string }) => record.source_record_id === sourceRecordId,
    );
    expect(sourceRecord).toMatchObject({
      box: "158",
      archive_location: "230/86/29/04",
      pdf_page: 100,
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

test("Batch 505 publishes two exact-identifier occupations without employers", () => {
  const expectations = [
    ["58c59371-4b84-5aa7-b579-177fbc5c5d14", "Checker"],
    ["164e7ced-dccf-52b4-a5a8-5ad511223453", "Garage laborer, car washer, or car greaser"],
  ] as const;

  for (const [id, occupation] of expectations) {
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
        organization_name_as_found: null,
        occupation,
        relationship_type: "unknown",
        temporal_basis: "strongly_date_bounded",
        claim_confidence: "medium",
        publication_status: "publish_qualified",
      }),
    );
  }
});

test("Batch 505 separates Culbertson's military, university, legal and diplomatic pathways", () => {
  const culbertson = profile("e264bb1d-1b97-5b50-b31f-bd349e60220d");
  expect(culbertson).toMatchObject({
    identity_status: "high_confidence",
    personnel_category: "commissioned_army_officer",
    commissioned_officer: true,
    research_status: "verified_employer_found",
    last_civilian_pre_service: [],
  });
  expect(culbertson.name_variants).toContain("William Smith Culbertson");
  expect(culbertson.immediate_pre_oss_affiliations).toContainEqual(
    expect.objectContaining({
      canonical_organization: "United States War Department",
      role_title: "Chief of the Military Intelligence Service",
      relationship_type: "military_assignment",
      temporal_basis: "probable_immediate",
      claim_confidence: "medium",
    }),
  );
  expect(culbertson.other_pre_oss_affiliations).toEqual(
    expect.arrayContaining([
      expect.objectContaining({ canonical_organization: "Georgetown University", relationship_type: "employment" }),
      expect.objectContaining({ canonical_organization: null, relationship_type: "self_employment" }),
      expect.objectContaining({ canonical_organization: "United States Tariff Commission", relationship_type: "government_assignment" }),
      expect.objectContaining({ canonical_organization: "United States Department of State", relationship_type: "government_assignment" }),
    ]),
  );
  expect(culbertson.claims.some((claim: { claim_text: string }) =>
    claim.claim_text.includes("exact sequence or overlap remains uncertain"),
  )).toBe(true);
});

test("Batch 505 keeps Cullison probable and out of default employer analytics", () => {
  const cullison = profile("c62ad924-7552-571c-81de-d64b0278240e");
  expect(cullison).toMatchObject({
    identity_status: "probable",
    personnel_category: "unknown_or_indeterminate",
    commissioned_officer: null,
    research_status: "documented_prewar_employer_found",
    immediate_pre_oss_affiliations: [],
    last_civilian_pre_service: [],
  });
  expect(cullison.other_pre_oss_affiliations).toEqual(
    expect.arrayContaining([
      expect.objectContaining({
        canonical_organization: "Missouri School of Mines",
        relationship_type: "employment",
        temporal_basis: "documented_prewar",
        identity_confidence: "probable",
        claim_confidence: "medium",
      }),
      expect.objectContaining({
        canonical_organization: "Missouri Geological Survey",
        relationship_type: "government_assignment",
        temporal_basis: "temporal_relation_uncertain",
      }),
    ]),
  );
  expect(organizations.find(
    (organization: { canonical_name: string }) => organization.canonical_name === "Missouri School of Mines",
  ).documented_person_count).toBe(1);
  expect(JSON.stringify(analytics)).not.toContain("Missouri School of Mines");
});

test("Batch 505 leaves six unresolved identities without public affiliations", () => {
  const unresolvedIds = [
    "d5ab2677-e4e5-5ae3-92bc-402aa146f1a8",
    "236ffd5a-0963-5cc2-89be-f0f23fa3bb48",
    "c0f013c3-c59c-5e10-8f88-b9861131dfca",
    "3b83a566-7eed-5b87-b1f1-ab411cc887d7",
    "1a34a633-a046-58e7-8c7c-a088cb82a6c8",
    "f6116d9f-08fb-5b05-bffa-b92b4da219cd",
  ];
  for (const id of unresolvedIds) {
    expect(profile(id)).toMatchObject({
      identity_status: "unresolved",
      research_status: "requires_archival_review",
      immediate_pre_oss_affiliations: [],
      last_civilian_pre_service: [],
      other_pre_oss_affiliations: [],
      claims: [],
    });
  }
});

test("Batch 505 exact coverage reflects ten terminal outcomes and one verified employer", () => {
  expect(stats.research_attempted_people).toBe(4818);
  expect(stats.verified_affiliation_people).toBe(549);
  expect(stats.verified_employer_people).toBe(244);
  expect(stats.archival_review_assessed_people).toBe(4773);
  expect(stats.analytics_policy).toContain("employment at a named organization");
});

test("Batch 505 direct routes show citations, qualification and archival guidance", async ({ page }) => {
  await page.goto("./people/e264bb1d-1b97-5b50-b31f-bd349e60220d/");
  await expect(page.getByRole("heading", { name: "William S Culbertson", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("United States War Department");
  await expect(page.locator("main")).toContainText("Chief of the Military Intelligence Service");
  await expect(page.locator("main")).toContainText("William Smith Culbertson Papers");
  await expect(page.locator("main")).toContainText("probable immediate");

  await page.goto("./people/c62ad924-7552-571c-81de-d64b0278240e/");
  await expect(page.getByRole("heading", { name: "James S Cullison", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("Missouri School of Mines");
  await expect(page.locator("main")).toContainText("probable identity match");
  await expect(page.locator("main")).toContainText("does not link him directly to OSS");

  await page.goto("./people/f6116d9f-08fb-5b05-bffa-b92b4da219cd/");
  await expect(page.getByRole("heading", { name: "Carson W Culp", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("No reliable pre-OSS employer has yet been identified");
  await expect(page.locator("main")).toContainText("Box 158");
});
