import { expect, test } from "@playwright/test";
import fs from "node:fs";

const people = JSON.parse(
  fs.readFileSync(new URL("../src/data/generated/people.json", import.meta.url), "utf8"),
);
const profile = (id: string) =>
  people.find((person: { person_id: string }) => person.person_id === id);

test("Batch 441 preserves identifier-supported spelling differences", async ({ page }) => {
  const expected = [
    [
      "ddf5f6bf-1d31-5711-8c78-cfa49ec4b04f",
      "Leoonard A Colavita",
      "Leonard A Colavita",
      "Student",
      "student",
      "1943-07-03",
    ],
    [
      "84574c3a-c295-5080-8ac3-a561091c306a",
      "Calvin Colding",
      "Calvin H Colding",
      "Chauffeurs and drivers, bus, taxi, truck, and tractor",
      "unknown",
      "1943-05-07",
    ],
    [
      "615ffde0-76c6-591a-aac2-b9538ac7a473",
      "Charles H Cole Jr.",
      "Charles H Coles Jr",
      "Student",
      "student",
      "1942-10-03",
    ],
    [
      "91b9e358-fdb7-5220-89dd-c19e84463406",
      "Francis J Cole",
      "Francis J Cole",
      "Student",
      "student",
      "1942-12-15",
    ],
  ];

  for (const [id, indexedName, documentedVariant, label, relationship, endDate] of expected) {
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
        relationship_type: relationship,
        end_date: endDate,
        temporal_basis: "strongly_date_bounded",
        identity_confidence: "confirmed",
        claim_confidence: "medium",
      }),
    );
    expect(
      person.other_pre_oss_affiliations.some(
        (item: { role_title: string | null; occupation: string | null }) =>
          item.role_title === label || item.occupation === label,
      ),
    ).toBe(true);
  }

  const leoonard = profile("ddf5f6bf-1d31-5711-8c78-cfa49ec4b04f");
  await page.goto(`./people/${leoonard.person_id}/`);
  await expect(page.getByRole("heading", { name: "Leoonard A Colavita", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("Leonard A Colavita");
  await expect(page.locator("main")).toContainText("Students");
  await expect(page.locator("main")).toContainText("No reliable pre-OSS employer has yet been identified");
});

test("Batch 441 qualifies the John A Colborn OSS-context identity lead", async ({ page }) => {
  const john = profile("bcc8249f-ffa2-5c56-8cb5-863d6fa0ae9a");
  expect(john).toMatchObject({
    display_name: "John A Colborn",
    identity_status: "probable",
    personnel_category: "unknown_or_indeterminate",
    commissioned_officer: null,
    research_status: "requires_archival_review",
  });
  expect(john.name_variants).toContain("John A. Colborn, Jr.");
  expect(john.immediate_pre_oss_affiliations).toEqual([]);
  expect(john.last_civilian_pre_service).toEqual([]);
  expect(john.other_pre_oss_affiliations).toEqual([]);
  expect(john.claims).toContainEqual(
    expect.objectContaining({
      claim_type: "identity",
      claim_confidence: "medium",
      publication_status: "publish_qualified",
      temporal_assessment:
        "The 1943 directory documents an OSS administrative role, not an employer or affiliation before OSS.",
    }),
  );
  expect(
    john.claims[0].sources.some(
      (link: { source: { stable_url: string } }) =>
        link.source.stable_url.includes("govinfo.gov/content/pkg/GOVPUB-PR32_4200"),
    ),
  ).toBe(true);

  await page.goto(`./people/${john.person_id}/`);
  await expect(page.getByRole("heading", { name: "John A Colborn", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("John A. Colborn, Jr.");
  await expect(page.locator("main")).toContainText("federal mileage administrator");
  await expect(page.locator("main")).toContainText("No publishable pre-OSS affiliation is recorded yet");
  await expect(page.locator("main")).toContainText("Review Box 133");
});

test("Batch 441 corrects William E Colby's employer-status semantics", async ({ page }) => {
  const william = profile("7a26fb60-b1e2-5377-9092-f16406580dfd");
  expect(william).toMatchObject({
    display_name: "William E Colby",
    identity_status: "high_confidence",
    personnel_category: "commissioned_army_officer",
    commissioned_officer: true,
    research_status: "requires_archival_review",
    research_attempt_count: 2,
  });
  expect(william.immediate_pre_oss_affiliations).toContainEqual(
    expect.objectContaining({
      canonical_organization: "United States Army",
      relationship_type: "military_assignment",
      immediate_pre_oss: true,
      claim_confidence: "high",
    }),
  );
  expect(william.last_civilian_pre_service).toEqual([]);

  await page.goto(`./people/${william.person_id}/`);
  await expect(page.getByRole("heading", { name: "William E Colby", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("U.S. Army");
  await expect(page.locator("main")).toContainText("is not itself a verified employer");
  await expect(page.locator("main")).toContainText("No reliable pre-OSS employer has yet been identified");
});

test("Batch 441 preserves every row, masks identifiers and keeps unresolved people visible", async ({ page }) => {
  const expected = [
    ["ddf5f6bf-1d31-5711-8c78-cfa49ec4b04f", "Leoonard A Colavita", "3ac6bb10-ce6c-5038-b9dd-c03ce4ddb18e", "133", "230/86/28/07", true],
    ["bcc8249f-ffa2-5c56-8cb5-863d6fa0ae9a", "John A Colborn", "a6d5bbcd-343c-5cec-8705-8fd33f7b9781", "133", "230/86/28/07", false],
    ["a4a480af-8f3c-55cb-83ce-a9f278ee11ed", "John H Colby", "01d47dfb-e715-5ae6-8c02-fc169903bfc9", "133", "230/86/28/07", true],
    ["7a26fb60-b1e2-5377-9092-f16406580dfd", "William E Colby", "6e31ad8f-6ee2-5f0a-badb-92a59c172418", "133", "230/86/28/07", true],
    ["84574c3a-c295-5080-8ac3-a561091c306a", "Calvin Colding", "3ef03d42-4cb6-5adf-9bdb-195d5188b305", "133", "230/86/28/07", true],
    ["abc3b33f-404c-59a0-86fd-6c18c9bf39e4", "Anita B Cole", "e0e91b56-b552-5a52-81ae-a638db10d90a", "133", "230/86/28/07", false],
    ["c3fa940f-9819-50b1-9045-08dbb927aa1e", "Betina Cole", "59c80d51-4e08-54a5-b211-531a9d9952ed", "134", "230/86/29/01", false],
    ["615ffde0-76c6-591a-aac2-b9538ac7a473", "Charles H Cole Jr.", "a3943803-2ef2-5ca8-a99d-5feda504d7e9", "135", "230/86/29/01", true],
    ["91b9e358-fdb7-5220-89dd-c19e84463406", "Francis J Cole", "3bdb077c-6813-53b1-a15f-67936af91b68", "134", "230/86/29/01", true],
    ["5aa7ab5a-7ff1-5470-87a2-709b885b4b24", "Frank Cole", "d17a90cf-12d5-5dec-a3dc-7e299be8b60e", "134", "230/86/29/01", false],
  ];

  for (const [id, name, sourceRecordId, box, location, hasSerial] of expected) {
    const person = profile(String(id));
    expect(person).toMatchObject({ display_name: name });
    expect(person.source_records[0]).toMatchObject({
      source_record_id: sourceRecordId,
      pdf_page: 86,
      rank_as_indexed: null,
      box,
      archive_location: location,
    });
    if (hasSerial) {
      expect(person.source_records[0].serial_masked).toMatch(/^••••.{4}$/u);
    } else {
      expect(person.source_records[0].serial_masked).toBeNull();
    }
    expect(JSON.stringify(person)).not.toMatch(
      /"serial_number"|"serial_number_raw"|"serial_number_normalized"/,
    );
  }

  for (const id of [
    "a4a480af-8f3c-55cb-83ce-a9f278ee11ed",
    "abc3b33f-404c-59a0-86fd-6c18c9bf39e4",
    "c3fa940f-9819-50b1-9045-08dbb927aa1e",
    "5aa7ab5a-7ff1-5470-87a2-709b885b4b24",
  ]) {
    const person = profile(id);
    expect(person.identity_status).toBe("unresolved");
    expect(person.research_status).toBe("requires_archival_review");
    expect(person.immediate_pre_oss_affiliations).toEqual([]);
    expect(person.last_civilian_pre_service).toEqual([]);
    expect(person.other_pre_oss_affiliations).toEqual([]);
    expect(person.claims).toEqual([]);
  }

  const john = profile("a4a480af-8f3c-55cb-83ce-a9f278ee11ed");
  await page.goto(`./people/${john.person_id}/`);
  await expect(page.getByRole("heading", { name: "John H Colby", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("short six-digit identifier");
  await expect(page.locator("main")).toContainText("was not padded or altered");
  await expect(page.locator("main")).toContainText("Review Box 133");
  await expect(page.locator("main")).toContainText("No reliable pre-OSS employer has yet been identified");
});
