import { expect, test } from "@playwright/test";
import fs from "node:fs";

const people = JSON.parse(
  fs.readFileSync(new URL("../src/data/generated/people.json", import.meta.url), "utf8"),
);
const stats = JSON.parse(
  fs.readFileSync(new URL("../src/data/generated/stats.json", import.meta.url), "utf8"),
);
const analytics = JSON.parse(
  fs.readFileSync(new URL("../src/data/generated/analytics.json", import.meta.url), "utf8"),
);
const profile = (id: string) =>
  people.find((person: { person_id: string }) => person.person_id === id);

const cohort = [
  ["2dbfa59b-f026-5aed-9456-1f9f853bada3", "Walter M Cuddy Jr.", "38dc8981-5225-57a1-88bd-86c0ae54ea68", "157", true],
  ["3d16196a-e9d8-5c6d-8389-c213c16ba5f6", "John H Cudmore", "cfaf0ccc-c35d-5778-bfa4-ea9489e88300", "157", true],
  ["4bc2de73-077f-5f07-a1b5-a13874dc02ff", "Frank Cuellar", "f916c548-9f87-5ca3-aff3-80f1d5e5a989", "157", true],
  ["40bd9b2d-264e-5842-9499-10ae6eaf98d3", "Rodolfo E Cueva", "3123eb9a-bbe4-551d-a507-931d16515eaf", "157", false],
  ["bc53e536-8919-59cb-b760-64d9928a0847", "Domingo Cuevas", "27f8ff5c-9aa3-5556-b30d-1d01df8a40ea", "157", true],
  ["8d9ac81b-e576-5636-9f1c-cbababa88946", "Mario J Cugia", "4e004a2c-5b93-513c-a138-92ddae585ac9", "157", true],
  ["18dff061-47dd-532d-aed9-95e1affef495", "Saburo Cujow", "17a2489c-426c-55c0-9d3e-10460fa48ab3", "158", false],
  ["4301edb6-d672-55ee-8659-abad726ee17d", "Frederick C Culbert", "98cc8133-e34d-54a2-be1c-48914802e555", "158", false],
  ["2434a0ca-c538-572c-be3b-dde55a2b03dd", "Frederick P Culbert", "55d24655-ea8b-5a39-ab4a-27fca9c15183", "158", false],
  ["aaf1d806-5ddb-580b-af22-e83861cd2c09", "Jane Culbertson", "2f865da8-a7a7-59fc-b392-38b901bf4cf7", "158", false],
] as const;

test("Batch 504 preserves all ten page 100 rows and masks every printed identifier", () => {
  for (const [id, name, sourceRecordId, box, hasPrivateIdentifier] of cohort) {
    const person = profile(id);
    expect(person).toMatchObject({ display_name: name });
    const sourceRecord = person.source_records.find(
      (record: { source_record_id: string }) => record.source_record_id === sourceRecordId,
    );
    expect(sourceRecord).toMatchObject({
      box,
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

test("Batch 504 publishes two exact-identifier occupations without employers", () => {
  const expectations = [
    ["2dbfa59b-f026-5aed-9456-1f9f853bada3", "Pressman or plate printer in printing"],
    ["8d9ac81b-e576-5636-9f1c-cbababa88946", "Unskilled occupation in printing and publishing, not elsewhere classified"],
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

test("Batch 504 publishes Culbert's government pathway and preserves the location conflict", () => {
  const culbert = profile("2434a0ca-c538-572c-be3b-dde55a2b03dd");
  expect(culbert).toMatchObject({
    identity_status: "high_confidence",
    personnel_category: "civilian_professional_or_administrative_grade",
    commissioned_officer: null,
    research_status: "completed",
    last_civilian_pre_service: [],
  });
  expect(culbert.immediate_pre_oss_affiliations).toContainEqual(
    expect.objectContaining({
      canonical_organization: "United States Department of State",
      role_title: "Vice Consul and control officer in North Africa",
      relationship_type: "government_assignment",
      temporal_basis: "explicit_immediate",
      claim_confidence: "high",
    }),
  );
  expect(culbert.other_pre_oss_affiliations).toEqual(
    expect.arrayContaining([
      expect.objectContaining({
        canonical_organization: "United States Navy",
        relationship_type: "military_assignment",
      }),
      expect.objectContaining({
        canonical_organization: null,
        role_title: "Business executive",
        relationship_type: "employment",
      }),
    ]),
  );
  const immediateClaim = culbert.claims.find(
    (claim: { claim_type: string }) => claim.claim_type === "immediate_pre_oss_affiliation",
  );
  expect(immediateClaim.claim_text).toContain("disagree between Casablanca and Dakar");
  expect(immediateClaim.sources).toEqual(
    expect.arrayContaining([
      expect.objectContaining({ support_type: "contradicts", excerpt_override: "control officer at Dakar" }),
    ]),
  );
});

test("Batch 504 leaves weak identities and false newspaper hits out of public facts", () => {
  const expected = [
    ["3d16196a-e9d8-5c6d-8389-c213c16ba5f6", "unresolved", "requires_archival_review"],
    ["4bc2de73-077f-5f07-a1b5-a13874dc02ff", "ambiguous", "needs_identity_review"],
    ["40bd9b2d-264e-5842-9499-10ae6eaf98d3", "ambiguous", "needs_identity_review"],
    ["bc53e536-8919-59cb-b760-64d9928a0847", "unresolved", "requires_archival_review"],
    ["18dff061-47dd-532d-aed9-95e1affef495", "unresolved", "requires_archival_review"],
    ["4301edb6-d672-55ee-8659-abad726ee17d", "unresolved", "requires_archival_review"],
    ["aaf1d806-5ddb-580b-af22-e83861cd2c09", "unresolved", "requires_archival_review"],
  ] as const;

  for (const [id, identityStatus, researchStatus] of expected) {
    expect(profile(id)).toMatchObject({
      identity_status: identityStatus,
      research_status: researchStatus,
      immediate_pre_oss_affiliations: [],
      last_civilian_pre_service: [],
      other_pre_oss_affiliations: [],
      claims: [],
    });
  }
});

test("Batch 504 coverage excludes unnamed employment from verified-employer analytics", () => {
  expect(stats.research_attempted_people).toBe(4808);
  expect(stats.verified_affiliation_people).toBe(548);
  expect(stats.verified_employer_people).toBe(243);
  expect(stats.archival_review_assessed_people).toBe(4763);
  expect(stats.analytics_policy).toContain("employment at a named organization");
  const sectorChart = analytics.charts.find((chart: { key: string }) => chart.key === "sectors");
  expect(sectorChart.denominator).toBe(243);
  expect(JSON.stringify(sectorChart)).not.toContain("2434a0ca-c538-572c-be3b-dde55a2b03dd");
});

test("Batch 504 direct routes show evidence, qualification and archival guidance", async ({ page }) => {
  await page.goto("./people/2434a0ca-c538-572c-be3b-dde55a2b03dd/");
  await expect(page.getByRole("heading", { name: "Frederick P Culbert", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("United States Department of State");
  await expect(page.locator("main")).toContainText("Casablanca versus Dakar");
  await expect(page.locator("main")).toContainText("Plan for North Africa");
  await expect(page.locator("main")).toContainText("control officer at Dakar");
  await expect(page.locator("main")).toContainText("business executive");

  await page.goto("./people/2dbfa59b-f026-5aed-9456-1f9f853bada3/");
  await expect(page.getByRole("heading", { name: "Walter M Cuddy Jr.", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("Pressman or plate printer in printing");
  await expect(page.locator("main")).toContainText("does not name an employer");

  await page.goto("./people/aaf1d806-5ddb-580b-af22-e83861cd2c09/");
  await expect(page.getByRole("heading", { name: "Jane Culbertson", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("No reliable pre-OSS employer has yet been identified");
  await expect(page.locator("main")).toContainText("Box 158");
});
