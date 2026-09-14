import { expect, test } from "@playwright/test";
import fs from "node:fs";

const people = JSON.parse(
  fs.readFileSync(new URL("../src/data/generated/people.json", import.meta.url), "utf8"),
);
const profile = (id: string) =>
  people.find((person: { person_id: string }) => person.person_id === id);

test("Batch 457 preserves all ten printed rows and masks every private identifier", async () => {
  const expected = [
    ["2a5ef16e-0be2-5751-8398-ed7d3446290e", "Thomas B Connole", "1ad9cdfc-2282-575f-8564-a6191b45914b", 10, null, null],
    ["f6a86233-c565-564c-b0b6-65091c35cb47", "James R Connolly", "364765a0-7692-5d0a-b244-72c38694b507", 11, null, "••••8634"],
    ["b97a57d2-1fbb-5257-9266-f88eb688261e", "Martin J Connolly", "f4a9d7e7-9bff-50c8-98ed-6f02abb7eb87", 12, null, "••••0157"],
    ["2ca30944-aa95-5f4f-8e66-98a2b69d3efc", "Mary E Connolly", "f0cdf2b1-0db6-5ac3-bb20-f3f118ed74a6", 13, null, null],
    ["bc0e629f-cb56-59c8-ada2-88a178d8b65a", "Thomas J Connolly", "18e1b101-4995-559d-8c5c-4fd1cfc6d9a6", 14, null, "••••8669"],
    ["59fb93c0-6b88-5956-8189-8ad16099e522", "Matthew F Connoly", "1a6a2d14-6770-5f0c-892e-827ee682c0e0", 15, null, null],
    ["eede5fb0-0d79-5082-a193-872e989ce57a", "Duncan Connor", "1a680e03-a443-52f3-bb5f-abde8bba1fd2", 16, null, "••••0381"],
    ["3f131d29-fcca-5a93-a374-453c46439837", "William E Connor", "26f0d5d9-a2c2-5798-9e48-e0992ffd4410", 19, null, "••••4740"],
  ];

  for (const [id, name, sourceRecordId, _rowNumber, rank, serial] of expected) {
    const person = profile(String(id));
    expect(person).toMatchObject({ display_name: name });
    expect(person.source_records).toContainEqual(
      expect.objectContaining({
        source_record_id: sourceRecordId,
        rank_as_indexed: rank,
        serial_masked: serial,
        box: "139",
        archive_location: "230/86/29/01",
        pdf_page: 90,
      }),
    );
    expect(JSON.stringify(person)).not.toMatch(
      /"serial_number"|"serial_number_raw"|"serial_number_normalized"/,
    );
  }

  const robert = profile("e9584e7d-9bd8-54a7-9c54-418c9dc421a9");
  expect(robert.source_records).toHaveLength(2);
  expect(robert.source_records).toEqual(
    expect.arrayContaining([
      expect.objectContaining({
        source_record_id: "09c4b480-a98f-5345-b5c0-c971794ce1c6",
        rank_as_indexed: "Pvt",
        serial_masked: "••••3330",
      }),
      expect.objectContaining({
        source_record_id: "05586049-0fb0-5352-9a7b-2d5ee1188375",
        rank_as_indexed: null,
        serial_masked: "••••3330",
      }),
    ]),
  );
});

test("Batch 457 publishes three exact-identifier Army findings without inventing employers", async ({ page }) => {
  const expected = [
    ["b97a57d2-1fbb-5257-9266-f88eb688261e", "Martin J Connolly", "Occupations in fabrication of textile products, n.e.c.", "unknown", "1942-08-12"],
    ["eede5fb0-0d79-5082-a193-872e989ce57a", "Duncan Connor", "Chauffeurs and drivers, bus, taxi, truck, and tractor", "unknown", "1943-02-10"],
    ["3f131d29-fcca-5a93-a374-453c46439837", "William E Connor", "Students", "student", "1943-06-29"],
  ];

  for (const [id, name, occupation, relationshipType, endDate] of expected) {
    const person = profile(id);
    expect(person).toMatchObject({
      display_name: name,
      identity_status: "confirmed",
      research_status: "occupation_only_found",
      personnel_category: "enlisted_army_personnel",
      commissioned_officer: false,
    });
    expect(person.immediate_pre_oss_affiliations).toEqual([]);
    expect(person.last_civilian_pre_service).toEqual([]);
    expect(person.other_pre_oss_affiliations).toContainEqual(
      expect.objectContaining({
        canonical_organization: null,
        occupation,
        relationship_type: relationshipType,
        end_date: endDate,
        temporal_basis: "strongly_date_bounded",
        identity_confidence: "confirmed",
        claim_confidence: "medium",
      }),
    );
    expect(person.claims).toContainEqual(
      expect.objectContaining({
        claim_type: "identity",
        claim_confidence: "confirmed",
        publication_status: "published",
      }),
    );
    expect(person.claims).toContainEqual(
      expect.objectContaining({
        claim_type: "occupation",
        claim_confidence: "medium",
        publication_status: "publish_qualified",
      }),
    );

    await page.goto("./people/" + person.person_id + "/");
    await expect(page.getByRole("heading", { name, exact: true })).toBeVisible();
    await expect(page.locator("main")).toContainText(occupation);
    await expect(page.locator("main")).toContainText(
      "Last civilian employer before serviceNo reliable pre-OSS employer has yet been identified",
    );
  }
});

test("Batch 457 keeps William Connor's student status out of employer fields", async ({ page }) => {
  const william = profile("3f131d29-fcca-5a93-a374-453c46439837");
  expect(william.immediate_pre_oss_affiliations).toEqual([]);
  expect(william.last_civilian_pre_service).toEqual([]);
  expect(william.other_pre_oss_affiliations[0]).toMatchObject({
    role_title: "Student",
    relationship_type: "student",
    occupation: "Students",
  });

  await page.goto("./people/" + william.person_id + "/");
  await expect(page.locator("main")).toContainText("Student status");
  await expect(page.locator("main")).toContainText("no school or employer");
});

test("Batch 457 publishes the Robert Connor identifier conflict and preserves both source rows", async ({ page }) => {
  const robert = profile("e9584e7d-9bd8-54a7-9c54-418c9dc421a9");
  expect(robert).toMatchObject({
    display_name: "Robert B Connor",
    identity_status: "conflicting",
    research_status: "conflicting_sources",
    personnel_category: "enlisted_army_personnel",
    commissioned_officer: false,
    manual_review_required: true,
    archival_file: expect.objectContaining({ review_priority: "critical" }),
  });
  expect(robert.source_records).toHaveLength(2);
  expect(robert.immediate_pre_oss_affiliations).toEqual([]);
  expect(robert.last_civilian_pre_service).toEqual([]);
  expect(robert.other_pre_oss_affiliations).toEqual([]);
  expect(robert.claims).toContainEqual(
    expect.objectContaining({
      claim_type: "identity",
      claim_confidence: "conflicting",
      publication_status: "conflicting",
    }),
  );
  expect(JSON.stringify(robert)).not.toContain("/LBZETHL");

  await page.goto("./people/" + robert.person_id + "/");
  await expect(page.getByRole("heading", { name: "Robert B Connor", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("conflicting");
  await expect(page.locator("main")).toContainText("different name");
  await expect(page.getByRole("heading", { name: "Index row 1" })).toBeVisible();
  await expect(page.getByRole("heading", { name: "Index row 2" })).toBeVisible();
  await expect(page.locator("main")).toContainText("09c4b480-a98f-5345-b5c0-c971794ce1c6");
  await expect(page.locator("main")).toContainText("05586049-0fb0-5352-9a7b-2d5ee1188375");
});

test("Batch 457 leaves the five unresolved or ambiguous cases claim-free", async () => {
  const expected = [
    ["2a5ef16e-0be2-5751-8398-ed7d3446290e", "unresolved", "requires_archival_review"],
    ["f6a86233-c565-564c-b0b6-65091c35cb47", "ambiguous", "needs_identity_review"],
    ["2ca30944-aa95-5f4f-8e66-98a2b69d3efc", "ambiguous", "needs_identity_review"],
    ["bc0e629f-cb56-59c8-ada2-88a178d8b65a", "ambiguous", "needs_identity_review"],
    ["59fb93c0-6b88-5956-8189-8ad16099e522", "unresolved", "requires_archival_review"],
  ];

  for (const [id, identityStatus, researchStatus] of expected) {
    const person = profile(id);
    expect(person).toMatchObject({
      identity_status: identityStatus,
      research_status: researchStatus,
    });
    expect(person.claims).toEqual([]);
    expect(person.immediate_pre_oss_affiliations).toEqual([]);
    expect(person.last_civilian_pre_service).toEqual([]);
    expect(person.other_pre_oss_affiliations).toEqual([]);
    expect(person.next_action).toContain("Box 139");
  }
});
