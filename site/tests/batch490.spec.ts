import { expect, test } from "@playwright/test";
import fs from "node:fs";

const people = JSON.parse(
  fs.readFileSync(new URL("../src/data/generated/people.json", import.meta.url), "utf8"),
);
const organizations = JSON.parse(
  fs.readFileSync(new URL("../src/data/generated/organizations.json", import.meta.url), "utf8"),
);
const stats = JSON.parse(
  fs.readFileSync(new URL("../src/data/generated/stats.json", import.meta.url), "utf8"),
);
const profile = (id: string) =>
  people.find((person: { person_id: string }) => person.person_id === id);

const cohort = [
  ["da4dfe5c-22d3-5b67-8f7c-0375a5ec9dcd", "Robert E Cramer", "7b66c951-d545-5607-bf65-1e5b69998f0e", "151", false],
  ["61917fef-ca77-5346-a638-2ecae50cb5af", "Joseph Crampes", "5543532d-f6e6-58cc-ba3d-ac9b2264533b", "152", true],
  ["10ab749d-8f12-56b5-a94a-c1125aa02701", "Burton Crane", "37ad2f3c-6f31-5f2a-b67d-7063f9bc8149", "152", false],
  ["1e569e97-758d-5ce7-a2b0-d7a062fe81bb", "Donald J Crane", "294c895a-ef50-57ff-a8c6-9441f830a9c0", "152", false],
  ["83211d34-6b53-5b18-a0f3-0cd6b1ca330b", "Elizabeth J Crane", "5ede8adb-7891-5b6c-bfa7-6c8e0c884847", "152", false],
  ["b9bc8f09-be2a-5e00-9d1e-3381de354ebb", "Gordon Crane", "ce86499e-f711-51cf-b74c-e653c343b960", "152", true],
  ["5ca1c0c7-4f2e-5bdb-ad48-8f966335cc9e", "Milton Crane", "ad984e4a-9d77-577c-bd55-954eccb33544", "152", false],
  ["013ad579-90cc-59a9-8730-176c39ec83a1", "Robert Crane", "33198b56-3e7f-5f4d-baf7-30de9fa877bd", "152", false],
  ["15e9302b-486b-5828-835b-d0fa419a11f7", "Rufus S Crane Jr.", "b3082fc9-3840-57b2-9d01-f0157e1a54da", "152", true],
  ["51677744-32cc-5e49-bd53-54451ff13c2c", "Wallen L Crane", "6fdc0c82-8bf9-58fb-9338-4493a4afc3e4", "152", true],
] as const;

test("Batch 490 preserves all ten page 97 rows and masks every printed identifier", () => {
  for (const [id, name, sourceRecordId, box, hasPrivateIdentifier] of cohort) {
    const person = profile(id);
    expect(person).toMatchObject({ display_name: name });
    const sourceRecord = person.source_records.find(
      (record: { source_record_id: string }) => record.source_record_id === sourceRecordId,
    );
    expect(sourceRecord).toMatchObject({
      box,
      archive_location: "230/86/29/03",
      pdf_page: 97,
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

test("Batch 490 publishes three identifier-supported Army-entry occupations", () => {
  const expected = [
    ["61917fef-ca77-5346-a638-2ecae50cb5af", "Cooks, except private family", "1942-06-30"],
    ["15e9302b-486b-5828-835b-d0fa419a11f7", "Actors and actresses", "1942-02-12"],
    ["51677744-32cc-5e49-bd53-54451ff13c2c", "Managers and officials, not elsewhere classified", "1944-04-26"],
  ] as const;

  for (const [id, occupation, endDate] of expected) {
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
        occupation,
        end_date: endDate,
        relationship_type: "unknown",
        temporal_basis: "strongly_date_bounded",
        claim_confidence: "medium",
      }),
    );
    expect(person.claims).toContainEqual(
      expect.objectContaining({
        claim_type: "occupation",
        claim_confidence: "medium",
        publication_status: "publish_qualified",
      }),
    );
  }
});

test("Batch 490 distinguishes Burton Crane's last civilian employer from earlier work", () => {
  const burton = profile("10ab749d-8f12-56b5-a94a-c1125aa02701");
  expect(burton).toMatchObject({
    identity_status: "high_confidence",
    personnel_category: "unknown_or_indeterminate",
    commissioned_officer: null,
    research_status: "verified_employer_found",
    immediate_pre_oss_affiliations: [],
  });
  expect(burton.name_variants).toContain("Louis Burton Crane Jr.");
  expect(burton.last_civilian_pre_service).toContainEqual(
    expect.objectContaining({
      canonical_organization: "The New York Times",
      role_title: "financial writer",
      start_date: "1937",
      temporal_basis: "probable_immediate",
      claim_confidence: "high",
    }),
  );
  expect(burton.other_pre_oss_affiliations).toContainEqual(
    expect.objectContaining({
      canonical_organization: "The Japan Advertiser",
      role_title: "financial editor",
      start_date: "1925",
      end_date: "1936",
      temporal_basis: "documented_prewar",
      claim_confidence: "high",
    }),
  );
  expect(burton.claims).toHaveLength(2);
  for (const claim of burton.claims) {
    expect(claim.sources.length).toBeGreaterThanOrEqual(2);
  }
});

test("Batch 490 leaves unsupported identities and officer status unresolved", () => {
  for (const id of [
    "da4dfe5c-22d3-5b67-8f7c-0375a5ec9dcd",
    "1e569e97-758d-5ce7-a2b0-d7a062fe81bb",
    "83211d34-6b53-5b18-a0f3-0cd6b1ca330b",
    "b9bc8f09-be2a-5e00-9d1e-3381de354ebb",
    "5ca1c0c7-4f2e-5bdb-ad48-8f966335cc9e",
    "013ad579-90cc-59a9-8730-176c39ec83a1",
  ]) {
    const person = profile(id);
    expect(person).toMatchObject({
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

test("Batch 490 data and direct routes expose qualified evidence", async ({ page }) => {
  expect(stats.research_attempted_people).toBeGreaterThanOrEqual(4668);
  expect(stats.verified_affiliation_people).toBeGreaterThanOrEqual(534);
  expect(stats.verified_employer_people).toBeGreaterThanOrEqual(237);
  expect(stats.archival_review_assessed_people).toBeGreaterThanOrEqual(4623);

  const newYorkTimes = organizations.find(
    (organization: { canonical_name: string }) =>
      organization.canonical_name === "The New York Times",
  );
  const japanAdvertiser = organizations.find(
    (organization: { canonical_name: string }) =>
      organization.canonical_name === "The Japan Advertiser",
  );
  expect(newYorkTimes.organization_id).toBe("9904e836-9d45-5ba0-ba26-035a375d8d6f");
  expect(japanAdvertiser.organization_id).toBe("ee9be0ee-9cd1-54ac-baea-878e7d7f7105");

  await page.goto("./people/10ab749d-8f12-56b5-a94a-c1125aa02701/");
  await expect(page.getByRole("heading", { name: "Burton Crane", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("Louis Burton Crane Jr.");
  await expect(page.locator("main")).toContainText("The New York Times");
  await expect(page.locator("main")).toContainText("The Japan Advertiser");
  await expect(page.locator("main")).toContainText("Probable immediate");
  await expect(page.locator("main")).toContainText("The Historical and Interpretive Collections of The Franklin Institute");

  await page.goto("./organizations/9904e836-9d45-5ba0-ba26-035a375d8d6f/");
  await expect(page.getByRole("heading", { name: "The New York Times", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("Burton Crane");

  await page.goto("./people/15e9302b-486b-5828-835b-d0fa419a11f7/");
  await expect(page.getByRole("heading", { name: "Rufus S Crane Jr.", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("Actors and actresses");
  await expect(page.locator("main")).toContainText("no employer is named");

  await page.goto("./people/013ad579-90cc-59a9-8730-176c39ec83a1/");
  await expect(page.getByRole("heading", { name: "Robert Crane", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("No reliable pre-OSS employer has yet been identified");
});
