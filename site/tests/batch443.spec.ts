import { expect, test } from "@playwright/test";
import fs from "node:fs";

const people = JSON.parse(
  fs.readFileSync(new URL("../src/data/generated/people.json", import.meta.url), "utf8"),
);
const profile = (id: string) =>
  people.find((person: { person_id: string }) => person.person_id === id);

test("Batch 443 preserves identifier-supported Army categories without inventing employers", async ({ page }) => {
  const expected = [
    [
      "fe72ac0a-d567-592d-a2e8-e29e1cb02209",
      "William J Cole",
      "William J Cole",
      "Plumber, gas fitter, or steam fitter",
      "unknown",
      "1943-02-17",
    ],
    [
      "15980cb0-b607-59c1-a065-cfcadec3586e",
      "George W Cole Jr.",
      "George W Cole",
      "Chauffeur or driver (bus, taxi, truck, or tractor)",
      "unknown",
      "1942-07-11",
    ],
    [
      "986c01c8-d170-5ce4-8060-6b3032c515d4",
      "Francis G Coleman",
      "Francis G Coleman",
      "Student",
      "student",
      "1943-02-13",
    ],
  ];

  for (const [id, indexedName, documentedVariant, occupation, relationship, endDate] of expected) {
    const person = profile(id);
    expect(person).toMatchObject({
      display_name: indexedName,
      identity_status: "confirmed",
      personnel_category: "enlisted_army_personnel",
      commissioned_officer: false,
      research_status: "occupation_only_found",
    });
    expect(person.name_variants).toContain(documentedVariant);
    expect(person.immediate_pre_oss_affiliations).toEqual([]);
    expect(person.last_civilian_pre_service).toEqual([]);
    expect(person.other_pre_oss_affiliations).toContainEqual(
      expect.objectContaining({
        organization_id: null,
        occupation,
        relationship_type: relationship,
        end_date: endDate,
        temporal_basis: "strongly_date_bounded",
        identity_confidence: "confirmed",
        claim_confidence: "medium",
      }),
    );
  }

  const francis = profile("986c01c8-d170-5ce4-8060-6b3032c515d4");
  await page.goto(`./people/${francis.person_id}/`);
  await expect(page.getByRole("heading", { name: "Francis G Coleman", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("Student");
  await expect(page.locator("main")).toContainText("no institution or employer is identified");
  await expect(page.locator("main")).toContainText("No reliable pre-OSS employer has yet been identified");
});

test("Batch 443 publishes Kenneth Colegrove's continuing Northwestern employment with temporal qualification", async ({ page }) => {
  const kenneth = profile("b12044bb-e310-5e2c-8d8f-44ca6e32a01c");
  expect(kenneth).toMatchObject({
    display_name: "Kenneth Colegrove",
    identity_status: "high_confidence",
    personnel_category: "civilian_professional_or_administrative_grade",
    commissioned_officer: false,
    research_status: "verified_employer_found",
  });
  expect(kenneth.name_variants).toContain("Kenneth Wallace Colegrove");
  expect(kenneth.immediate_pre_oss_affiliations).toContainEqual(
    expect.objectContaining({
      canonical_organization: "Northwestern University",
      role_title: "Professor of political science; department chair, 1940-1948",
      relationship_type: "employment",
      start_date: "1919",
      end_date: "1952",
      temporal_basis: "strongly_date_bounded",
      identity_confidence: "high_confidence",
      claim_confidence: "high",
      sector: "academia_and_research",
    }),
  );
  expect(kenneth.last_civilian_pre_service).toContainEqual(
    expect.objectContaining({
      canonical_organization: "Northwestern University",
      relationship_type: "employment",
      temporal_basis: "strongly_date_bounded",
      claim_confidence: "high",
    }),
  );

  const immediateClaim = kenneth.claims.find(
    (claim: { claim_type: string }) => claim.claim_type === "immediate_pre_oss_affiliation",
  );
  expect(immediateClaim).toMatchObject({
    claim_confidence: "high",
    publication_status: "published",
  });
  expect(
    immediateClaim.sources.some(
      (link: { source: { stable_url: string } }) =>
        link.source.stable_url === "https://findingaids.library.northwestern.edu/agents/people/2097",
    ),
  ).toBe(true);

  await page.goto(`./people/${kenneth.person_id}/`);
  await expect(page.getByRole("heading", { name: "Kenneth Colegrove", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("Kenneth Wallace Colegrove");
  await expect(page.locator("main")).toContainText("Northwestern University");
  await expect(page.locator("main")).toContainText("Professor of political science");
  await expect(page.locator("main")).toContainText("strongly date bounded");
  await expect(page.locator("main")).toContainText("continuously on its faculty from 1919 to 1952");
});

test("Batch 443 preserves every source row, masks identifiers and keeps unresolved people visible", async ({ page }) => {
  const expected = [
    ["207fcecc-c11a-5b37-b4b3-dcb4331251d8", "Thelma M Cole", "ddaa02fb-1535-53d0-91a8-29f708ef62a4", false],
    ["fe72ac0a-d567-592d-a2e8-e29e1cb02209", "William J Cole", "cb76070a-e72c-522e-ab5d-67bdb96846cd", true],
    ["15980cb0-b607-59c1-a065-cfcadec3586e", "George W Cole Jr.", "774eb1e8-21fe-5787-8933-5c13edeffbbb", true],
    ["7a771ae7-d50e-5034-a5c2-2a04b48bc840", "Albert M Colegrove", "7e1b843f-cb87-54ad-a806-445af7ad9522", true],
    ["b12044bb-e310-5e2c-8d8f-44ca6e32a01c", "Kenneth Colegrove", "87f88cc5-85c2-5b2f-8908-ad901503f8f3", false],
    ["6aafc6d3-b300-5b48-a70d-2aac3c65005d", "Albert Coleman", "b2c956bc-1146-5164-866f-1ec407952601", false],
    ["ab0c07b8-c2cb-54be-b953-1366a1ee0ebd", "Archie F Coleman", "cee4dc2f-c930-5c90-b8de-d76575560cc0", false],
    ["986c01c8-d170-5ce4-8060-6b3032c515d4", "Francis G Coleman", "072dae92-7582-5518-a1b6-fb028b1c761d", true],
    ["dbbed73f-2962-51d7-92d0-6d05f052a3d4", "Frederick S Coleman", "2abd144a-e1cf-5889-a546-f7d305ea16c1", false],
    ["c0a54c1e-2e3d-5a94-b179-2612873a6fa0", "James E Coleman", "7e5688af-f633-5372-9dab-b7e79ac3b23b", false],
  ];

  for (const [id, name, sourceRecordId, hasSerial] of expected) {
    const person = profile(String(id));
    expect(person).toMatchObject({ display_name: name });
    expect(person.source_records[0]).toMatchObject({
      source_record_id: sourceRecordId,
      pdf_page: 87,
      rank_as_indexed: null,
      box: "134",
      archive_location: "230/86/29/01",
    });
    if (hasSerial) {
      expect(person.source_records[0].serial_masked).toMatch(/^••••.{3,4}$/u);
    } else {
      expect(person.source_records[0].serial_masked).toBeNull();
    }
    expect(JSON.stringify(person)).not.toMatch(
      /"serial_number"|"serial_number_raw"|"serial_number_normalized"/,
    );
  }

  for (const id of [
    "207fcecc-c11a-5b37-b4b3-dcb4331251d8",
    "7a771ae7-d50e-5034-a5c2-2a04b48bc840",
    "6aafc6d3-b300-5b48-a70d-2aac3c65005d",
    "ab0c07b8-c2cb-54be-b953-1366a1ee0ebd",
    "dbbed73f-2962-51d7-92d0-6d05f052a3d4",
    "c0a54c1e-2e3d-5a94-b179-2612873a6fa0",
  ]) {
    const person = profile(id);
    expect(person.identity_status).toBe("unresolved");
    expect(person.research_status).toBe("requires_archival_review");
    expect(person.immediate_pre_oss_affiliations).toEqual([]);
    expect(person.last_civilian_pre_service).toEqual([]);
    expect(person.other_pre_oss_affiliations).toEqual([]);
    expect(person.claims).toEqual([]);
  }

  const albert = profile("7a771ae7-d50e-5034-a5c2-2a04b48bc840");
  await page.goto(`./people/${albert.person_id}/`);
  await expect(page.getByRole("heading", { name: "Albert M Colegrove", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("seven-digit identifier");
  await expect(page.locator("main")).toContainText("not padded, corrected or assigned");
  await expect(page.locator("main")).toContainText("Review Box 134");
  await expect(page.locator("main")).toContainText("No reliable pre-OSS employer has yet been identified");
});
