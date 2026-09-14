import { expect, test } from "@playwright/test";
import fs from "node:fs";

const people = JSON.parse(
  fs.readFileSync(new URL("../src/data/generated/people.json", import.meta.url), "utf8"),
);
const profile = (id: string) =>
  people.find((person: { person_id: string }) => person.person_id === id);

test("Batch 460 preserves all ten printed rows and masks every private identifier", () => {
  const expected = [
    ["26898233-77ca-5222-9b77-28aeb5368fa1", "Edmund C Converse", "d21fe580-8f7f-59c0-ab5f-61be391252cf", 90, null],
    ["76bb294f-1132-53db-a462-07c088810f96", "George M Converse", "2328f20e-ab59-5716-81c7-76732655aaae", 90, null],
    ["d9c4a63e-585a-59ed-81b9-94cc6dbf4a89", "Alan C Conway", "2857d598-bcd2-570e-864c-b6718ecdcfdf", 90, "••••1873"],
    ["1e7dfe61-3d8a-50cf-b8e1-9028c8a79596", "Alice E Conway", "68640ce8-771b-5a48-8dbe-52ae78b4158d", 90, null],
    ["d09a1713-bc08-5a4d-8575-0589fce6fbfe", "William E Conway", "e7976f07-6ade-5ed7-bb8b-5afc46e8f82d", 90, "••••6792"],
    ["5753ff75-30a8-520d-8137-5b504919cb68", "William F Conway", "a944b9f4-bb0c-5f4e-a037-5342ab1ccd22", 90, null],
    ["d6668b18-b675-54fb-9849-1a50659a0228", "William H Conway", "a5691523-dbae-5330-8bfd-242a5fee807e", 90, "••••5814"],
    ["f0584b53-43be-5eea-98b4-ef284bdd137a", "Harry G Coogias", "d997a972-dd67-583e-9543-2b42f4af9cad", 91, "••••3394"],
    ["a06e5d1b-d12b-52aa-b2de-04ef9971989d", "Cecilia M Cook", "9b034418-c5fa-5128-8c68-f464f502971b", 91, null],
    ["9605be11-3df7-500f-bf6e-14edfc8ffd3c", "Charles W Cook", "d1642746-1af5-5943-ac1c-b12eff0b6ba7", 91, "••••4661"],
  ];

  for (const [id, name, sourceRecordId, pdfPage, serial] of expected) {
    const person = profile(String(id));
    expect(person).toMatchObject({ display_name: name });
    expect(person.source_records).toContainEqual(
      expect.objectContaining({
        source_record_id: sourceRecordId,
        rank_as_indexed: null,
        serial_masked: serial,
        box: "140",
        archive_location: "230/86/29/01",
        pdf_page: pdfPage,
      }),
    );
    expect(JSON.stringify(person)).not.toMatch(
      /"serial_number"|"serial_number_raw"|"serial_number_normalized"/,
    );
  }
});

test("Batch 460 publishes Edmund Converse's three distinct pre-OSS relationships", async ({ page }) => {
  const edmund = profile("26898233-77ca-5222-9b77-28aeb5368fa1");
  expect(edmund).toMatchObject({
    display_name: "Edmund C Converse",
    identity_status: "high_confidence",
    research_status: "verified_employer_found",
    personnel_category: "unknown_or_indeterminate",
    commissioned_officer: null,
  });
  expect(edmund.immediate_pre_oss_affiliations).toContainEqual(
    expect.objectContaining({
      canonical_organization: "United States Navy",
      relationship_type: "military_assignment",
      temporal_basis: "probable_immediate",
      claim_confidence: "high",
    }),
  );
  expect(edmund.last_civilian_pre_service).toContainEqual(
    expect.objectContaining({
      canonical_organization: "Office of U.S. Senator Styles Bridges",
      role_title: "Staff member",
      relationship_type: "employment",
      start_date: "1937",
      end_date: "1941",
      temporal_basis: "strongly_date_bounded",
    }),
  );
  expect(edmund.other_pre_oss_affiliations).toContainEqual(
    expect.objectContaining({
      canonical_organization: "Stanford University",
      relationship_type: "student",
      end_date: "1934",
      temporal_basis: "documented_prewar",
    }),
  );

  await page.goto("./people/" + edmund.person_id + "/");
  await expect(page.getByRole("heading", { name: "Edmund C Converse", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("United States Navy");
  await expect(page.locator("main")).toContainText("Office of U.S. Senator Styles Bridges");
  await expect(page.locator("main")).toContainText("Stanford University");
  await expect(page.locator("main")).toContainText("probable immediate");
});

test("Batch 460 publishes William Conway's student observation without inventing an employer", async ({ page }) => {
  const william = profile("d09a1713-bc08-5a4d-8575-0589fce6fbfe");
  expect(william).toMatchObject({
    display_name: "William E Conway",
    identity_status: "confirmed",
    research_status: "occupation_only_found",
    personnel_category: "enlisted_army_personnel",
    commissioned_officer: false,
  });
  expect(william.immediate_pre_oss_affiliations).toEqual([]);
  expect(william.last_civilian_pre_service).toEqual([]);
  expect(william.other_pre_oss_affiliations).toContainEqual(
    expect.objectContaining({
      role_title: "Student",
      occupation: "Students",
      relationship_type: "student",
      end_date: "1945-07-30",
      temporal_basis: "temporal_relation_uncertain",
      claim_confidence: "medium",
    }),
  );

  await page.goto("./people/" + william.person_id + "/");
  await expect(page.getByRole("heading", { name: "William E Conway", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("Students");
  await expect(page.locator("main")).toContainText("temporal relation uncertain");
  await expect(page.locator("main")).toContainText(
    "Last civilian employer before serviceNo reliable pre-OSS employer has yet been identified",
  );
});

test("Batch 460 exposes Harry Coogias's middle-initial conflict without transferring Army facts", async ({ page }) => {
  const harry = profile("f0584b53-43be-5eea-98b4-ef284bdd137a");
  expect(harry).toMatchObject({
    display_name: "Harry G Coogias",
    identity_status: "conflicting",
    research_status: "conflicting_sources",
    personnel_category: "unknown_or_indeterminate",
    commissioned_officer: null,
    manual_review_required: true,
  });
  expect(harry.immediate_pre_oss_affiliations).toEqual([]);
  expect(harry.last_civilian_pre_service).toEqual([]);
  expect(harry.other_pre_oss_affiliations).toEqual([]);
  expect(harry.claims).toContainEqual(
    expect.objectContaining({
      claim_type: "identity",
      claim_confidence: "conflicting",
      publication_status: "conflicting",
    }),
  );
  expect(JSON.stringify(harry)).not.toContain("31233394");

  await page.goto("./people/" + harry.person_id + "/");
  await expect(page.getByRole("heading", { name: "Harry G Coogias", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("middle initial");
  await expect(page.locator("main")).toContainText("Box 140");
});

test("Batch 460 keeps ambiguous and unresolved people claim-free", () => {
  const expected = [
    ["76bb294f-1132-53db-a462-07c088810f96", "ambiguous", "needs_identity_review"],
    ["d9c4a63e-585a-59ed-81b9-94cc6dbf4a89", "ambiguous", "needs_identity_review"],
    ["1e7dfe61-3d8a-50cf-b8e1-9028c8a79596", "unresolved", "requires_archival_review"],
    ["5753ff75-30a8-520d-8137-5b504919cb68", "ambiguous", "needs_identity_review"],
    ["d6668b18-b675-54fb-9849-1a50659a0228", "ambiguous", "needs_identity_review"],
    ["a06e5d1b-d12b-52aa-b2de-04ef9971989d", "unresolved", "requires_archival_review"],
    ["9605be11-3df7-500f-bf6e-14edfc8ffd3c", "ambiguous", "needs_identity_review"],
  ];

  for (const [id, identityStatus, researchStatus] of expected) {
    const person = profile(id);
    expect(person).toMatchObject({
      identity_status: identityStatus,
      research_status: researchStatus,
      manual_review_required: true,
    });
    expect(person.claims).toEqual([]);
    expect(person.immediate_pre_oss_affiliations).toEqual([]);
    expect(person.last_civilian_pre_service).toEqual([]);
    expect(person.other_pre_oss_affiliations).toEqual([]);
    expect(person.next_action).toContain("Box 140");
  }
});
