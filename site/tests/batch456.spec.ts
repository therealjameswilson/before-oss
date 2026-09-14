import { expect, test } from "@playwright/test";
import fs from "node:fs";

const people = JSON.parse(
  fs.readFileSync(new URL("../src/data/generated/people.json", import.meta.url), "utf8"),
);
const profile = (id: string) =>
  people.find((person: { person_id: string }) => person.person_id === id);

test("Batch 456 preserves all ten printed rows across the page boundary and masks every private identifier", async () => {
  const expected = [
    ["09aec63c-a6aa-5eaa-ae07-32c3af733abd", "Marguerite Connelly", "74b67e59-63b5-5616-8377-955d466d50d7", 89, null],
    ["1fd48899-11a6-5e00-a087-56e37b10ed42", "Ralph H Connelly", "b58b52cc-24b8-5393-bb71-2e61e28ba452", 90, "••••8731"],
    ["bf2948c4-2c7c-5b04-b618-3ba9d4db8cff", "Richard D Connelly", "d0f61c25-9b33-5a4e-80fd-17050f70f549", 90, "••••1859"],
    ["58a44c1b-1087-5969-aef4-aa0886e11001", "Annie G Conner", "23dc4a2a-c0ae-5354-bde2-474be571799f", 90, "••••6003"],
    ["671acd70-8bc2-5a36-92c7-bbf63339dcc6", "Fred N Conner", "afdac921-d2b2-5d82-989d-f39535971d9c", 90, "••••4812"],
    ["88df8890-41da-573b-bb54-f90433a4a681", "John J Conner", "d1d8c4e3-8c73-550e-9cb6-d26538e6d66e", 90, "••••9712"],
    ["7be0d583-1595-5980-a27d-547023a04c30", "Margaret L Conner", "6130702c-b899-523f-9cad-8b4b7307f607", 90, null],
    ["137b8dd1-343e-54e7-b4dd-8a8330a12429", "Melvin E Conner", "6487b2e0-57a3-5101-a445-6594d54affa1", 90, null],
    ["441e28de-b94f-5c05-8737-8d71d3cd4cfc", "Willie M Connick", "05ec8eff-c586-5ff2-8561-0893d9289031", 90, null],
    ["9dc7223f-9679-5325-b4bf-43c2ccb409cd", "Thomas Conniff", "c87747b3-05a6-5294-b41b-cffaab9f3f76", 90, null],
  ];

  for (const [id, name, sourceRecordId, pageNumber, serial] of expected) {
    const person = profile(String(id));
    expect(person).toMatchObject({ display_name: name });
    expect(person.source_records[0]).toMatchObject({
      source_record_id: sourceRecordId,
      rank_as_indexed: null,
      serial_masked: serial,
      box: "139",
      archive_location: "230/86/29/01",
      pdf_page: pageNumber,
    });
    expect(JSON.stringify(person)).not.toMatch(
      /"serial_number"|"serial_number_raw"|"serial_number_normalized"/,
    );
  }
});

test("Batch 456 publishes five exact-identifier Army findings without inventing employers", async ({ page }) => {
  const expected = [
    ["1fd48899-11a6-5e00-a087-56e37b10ed42", "Ralph H Connelly", "Engravers", "unknown", "1943-05-18"],
    ["bf2948c4-2c7c-5b04-b618-3ba9d4db8cff", "Richard D Connelly", "Students", "student", "1944-02-14"],
    ["58a44c1b-1087-5969-aef4-aa0886e11001", "Annie G Conner", "Stenographers and typists", "unknown", "1943-01-13"],
    ["671acd70-8bc2-5a36-92c7-bbf63339dcc6", "Fred N Conner", "Machinists' apprentices", "unknown", "1943-03-11"],
    ["88df8890-41da-573b-bb54-f90433a4a681", "John J Conner", "Miscellaneous products manufacturing occupations, n.e.c.", "unknown", "1943-05-08"],
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

test("Batch 456 preserves Richard Connely as a documented variant and keeps student status out of employer fields", async ({ page }) => {
  const richard = profile("bf2948c4-2c7c-5b04-b618-3ba9d4db8cff");
  expect(richard.name_variants).toEqual(
    expect.arrayContaining(["Richard D Connelly", "Richard D Connely", "CONNELY RICHARD D"]),
  );
  expect(richard.immediate_pre_oss_affiliations).toEqual([]);
  expect(richard.last_civilian_pre_service).toEqual([]);
  expect(richard.other_pre_oss_affiliations[0]).toMatchObject({
    role_title: "Student",
    relationship_type: "student",
  });

  await page.goto("./people/" + richard.person_id + "/");
  await expect(page.locator("main")).toContainText("Richard D Connely");
  await expect(page.locator("main")).toContainText("Student status");
  await expect(page.locator("main")).toContainText("no school or employer");
});

test("Batch 456 preserves Annie Conner as noncommissioned women's Army personnel", async ({ page }) => {
  const annie = profile("58a44c1b-1087-5969-aef4-aa0886e11001");
  expect(annie).toMatchObject({
    display_name: "Annie G Conner",
    identity_status: "confirmed",
    personnel_category: "enlisted_army_personnel",
    commissioned_officer: false,
  });

  await page.goto("./people/" + annie.person_id + "/");
  await expect(page.locator("main")).toContainText("Auxiliary");
  await expect(page.locator("main")).toContainText("WAC");
  await expect(page.locator("main")).toContainText("Stenographers and typists");
});

test("Batch 456 leaves the five unresolved or ambiguous cases claim-free", async () => {
  const expected = [
    ["09aec63c-a6aa-5eaa-ae07-32c3af733abd", "unresolved", "requires_archival_review"],
    ["7be0d583-1595-5980-a27d-547023a04c30", "unresolved", "requires_archival_review"],
    ["137b8dd1-343e-54e7-b4dd-8a8330a12429", "ambiguous", "needs_identity_review"],
    ["441e28de-b94f-5c05-8737-8d71d3cd4cfc", "unresolved", "requires_archival_review"],
    ["9dc7223f-9679-5325-b4bf-43c2ccb409cd", "unresolved", "requires_archival_review"],
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
