import { expect, test } from "@playwright/test";
import fs from "node:fs";

const people = JSON.parse(
  fs.readFileSync(new URL("../src/data/generated/people.json", import.meta.url), "utf8"),
);
const profile = (id: string) =>
  people.find((person: { person_id: string }) => person.person_id === id);

test("Batch 478 preserves page 94 rows and masks private identifiers", () => {
  const expected = [
    ["508c6632-281f-562d-a2d4-db7764f854a9", "Georges Cotton", "f7cf007c-cb66-506b-808d-f2fed6cd5e42", null],
    ["94b2995b-adf1-50f7-bf8c-235cfdbfca9d", "James B Cotton", "baac8629-f619-59ba-b389-0c69822319ab", "••••4024"],
    ["85692df3-176c-5515-917f-823718c8f51b", "Mary M Cotton", "c69289c3-79b7-561a-87ca-8293859c17a1", null],
    ["b0312c6a-f288-545b-92f9-bcd2e84d7b28", "Cassandra P Cottone", "38dd50f6-4a7f-5896-9680-d968462fd046", null],
    ["94900781-c4ac-54f5-bdd0-12c0807af51a", "D T Cottone", "cf601570-4b03-5fae-930e-f90fb1ac21c7", null],
    ["8c44fae9-6747-5f3d-a87c-ccd222b8536a", "George W Cottrell Jr.", "2fffd0ec-4cdf-5383-97d8-25c95b4d4517", null],
    ["06d4f4cb-d292-5960-9b7b-34243ca2d27a", "Dale R Cottrill", "97517024-0eb2-5b64-a10f-accf2274afea", "••••4136"],
    ["eda60fc7-97fe-54e9-b2b4-2c4420315316", "Elec A Couch", "96b36522-14e3-5b09-beca-3c4d7513c44a", "••••9067"],
    ["66dc98d8-164a-546a-9218-02cd49b5132e", "Beverly T Couchman", "e6ad2ec3-2109-56a5-81b9-34456d782951", null],
    ["d1d4928e-3a36-5c29-a1fd-1776e663e0b2", "Panagiotis D Coucoulis", "4191cd1f-7317-5af0-b954-a3141cf6b023", null],
  ];

  for (const [id, name, sourceRecordId, serial] of expected) {
    const person = profile(String(id));
    expect(person).toMatchObject({ display_name: name });
    expect(person.source_records).toContainEqual(
      expect.objectContaining({
        source_record_id: sourceRecordId,
        serial_masked: serial,
        box: "147",
        archive_location: "230/86/29/02",
        pdf_page: 94,
      }),
    );
    expect(JSON.stringify(person)).not.toMatch(
      /"serial_number"|"serial_number_raw"|"serial_number_normalized"/,
    );
  }
});

test("Batch 478 publishes Elec Couch's separated military and civilian pathway", async ({ page }) => {
  const person = profile("eda60fc7-97fe-54e9-b2b4-2c4420315316");
  expect(person).toMatchObject({
    display_name: "Elec A Couch",
    identity_status: "confirmed",
    personnel_category: "enlisted_army_personnel",
    commissioned_officer: false,
    research_status: "verified_employer_found",
    manual_review_required: true,
  });
  expect(person.immediate_pre_oss_affiliations).toContainEqual(
    expect.objectContaining({
      organization_name_as_found: "Ninth Air Force",
      canonical_organization: "United States Army Air Forces, Ninth Air Force",
      relationship_type: "military_assignment",
      end_date: "1943-05",
      temporal_basis: "strongly_date_bounded",
      claim_confidence: "high",
    }),
  );
  expect(person.last_civilian_pre_service).toContainEqual(
    expect.objectContaining({
      organization_name_as_found: "Sears, Roebuck",
      canonical_organization: "Sears, Roebuck and Company",
      role_title: "Auditor and trainee",
      occupation: "Auditor and trainee",
      relationship_type: "employment",
      end_date: "1942",
      temporal_basis: "strongly_date_bounded",
      claim_confidence: "high",
    }),
  );

  await page.goto("./people/eda60fc7-97fe-54e9-b2b4-2c4420315316/");
  await expect(page.getByRole("heading", { name: "Elec A Couch", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("Ninth Air Force");
  await expect(page.locator("main")).toContainText("Sears, Roebuck");
  await expect(page.locator("main")).toContainText("Auditor and trainee");
  await expect(page.locator("main")).toContainText("Verbatim interviews of OSS personnel in Cairo");
  await expect(page.locator("main")).toContainText("high strongly date bounded");
});

test("Batch 478 confirms James Cotton without decoding an unsupported occupation", async ({ page }) => {
  const person = profile("94b2995b-adf1-50f7-bf8c-235cfdbfca9d");
  expect(person).toMatchObject({
    display_name: "James B Cotton",
    identity_status: "confirmed",
    personnel_category: "enlisted_army_personnel",
    commissioned_officer: false,
    research_status: "requires_archival_review",
    immediate_pre_oss_affiliations: [],
    last_civilian_pre_service: [],
    other_pre_oss_affiliations: [],
  });

  await page.goto("./people/94b2995b-adf1-50f7-bf8c-235cfdbfca9d/");
  await expect(page.getByRole("heading", { name: "James B Cotton", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("28 September 1942");
  await expect(page.locator("main")).toContainText("No reliable pre-OSS employer has yet been identified");
});

test("Batch 478 identifies Panagiotis Coucoulis without treating an OSS assignment as pre-OSS", async ({ page }) => {
  const person = profile("d1d4928e-3a36-5c29-a1fd-1776e663e0b2");
  expect(person).toMatchObject({
    display_name: "Panagiotis D Coucoulis",
    identity_status: "high_confidence",
    personnel_category: "enlisted_army_personnel",
    commissioned_officer: false,
    allied_or_foreign_personnel: false,
    research_status: "requires_archival_review",
    immediate_pre_oss_affiliations: [],
    last_civilian_pre_service: [],
    other_pre_oss_affiliations: [],
  });

  await page.goto("./people/d1d4928e-3a36-5c29-a1fd-1776e663e0b2/");
  await expect(page.getByRole("heading", { name: "Panagiotis D Coucoulis", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("communications in Athens");
  await expect(page.locator("main")).toContainText("Athens personnel list of 1 January 1945");
  await expect(page.locator("main")).toContainText("No reliable pre-OSS employer has yet been identified");
});

test("Batch 478 leaves seven identities unresolved with archival routing", async ({ page }) => {
  for (const id of [
    "508c6632-281f-562d-a2d4-db7764f854a9",
    "85692df3-176c-5515-917f-823718c8f51b",
    "b0312c6a-f288-545b-92f9-bcd2e84d7b28",
    "94900781-c4ac-54f5-bdd0-12c0807af51a",
    "8c44fae9-6747-5f3d-a87c-ccd222b8536a",
    "06d4f4cb-d292-5960-9b7b-34243ca2d27a",
    "66dc98d8-164a-546a-9218-02cd49b5132e",
  ]) {
    expect(profile(id)).toMatchObject({
      identity_status: "unresolved",
      research_status: "requires_archival_review",
      manual_review_required: true,
      immediate_pre_oss_affiliations: [],
      last_civilian_pre_service: [],
      other_pre_oss_affiliations: [],
      claims: [],
    });
  }
  expect(profile("508c6632-281f-562d-a2d4-db7764f854a9")).toMatchObject({
    personnel_category: "unknown_or_indeterminate",
    commissioned_officer: null,
  });

  await page.goto("./people/94900781-c4ac-54f5-bdd0-12c0807af51a/");
  await expect(page.getByRole("heading", { name: "D T Cottone", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("expand the initials");
});
