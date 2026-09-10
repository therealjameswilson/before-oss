import { expect, test } from "@playwright/test";
import fs from "node:fs";

const people = JSON.parse(
  fs.readFileSync(new URL("../src/data/generated/people.json", import.meta.url), "utf8"),
);
const profile = (id: string) =>
  people.find((person: { person_id: string }) => person.person_id === id);

test("Batch 455 preserves all ten printed rows and masks every private identifier", async () => {
  const expected = [
    ["6aea02bb-61e2-5d97-bb85-5f557d46edc6", "Leroy G Conn", "a7a10663-8353-57ea-82ed-3c4d267c6c18", "138", null],
    ["e435f1a4-b968-522a-9176-5fced06db9f7", "Rebecca Connally", "41da6004-8961-5b31-94d5-b705149f1662", "138", null],
    ["68c1eaaa-237a-5e35-b9a1-f6401aa066b8", "Jacques M Connaughton", "d51063d2-d5e9-5bfb-97b6-599e128f1642", "139", "••••5006"],
    ["7ea4e4ac-d953-5662-bd78-1cd3b9fbef1c", "George J Connell", "054286ee-61f7-51cc-9414-022e301a57eb", "139", "••••3811"],
    ["b1ba7b13-1d2f-57d7-8944-14c1b893a141", "John G Connell", "711ffc9e-a823-517f-9029-c92f117c5167", "139", "••••6013"],
    ["aa488229-e09e-5d02-8bc9-ed2c96dfe4ea", "Oswald C Connell", "7e0235d2-3cfc-5a61-b8a2-bbf9ec97c65f", "139", "••••4632"],
    ["33aa623b-bd1c-5a12-8a4b-76e51eb786f2", "Richard A Connell", "8cb7da4c-018b-5173-baaa-4de87c8f40d4", "139", "••••8495"],
    ["a52e755d-b842-58e6-93e6-8fc147ad510a", "Bernard M Connelly", "e5578e30-89c5-5bfe-ba7c-541291866df0", "139", "••••1854"],
    ["25db4b90-8100-5f34-8090-6e9a9e602fbb", "David L Connelly", "8e0c3d80-90c1-5baa-8c3d-8c8967644a34", "139", null],
    ["bfe66780-626e-5662-8a9c-41cbc9e8efb6", "Emmett F Connelly", "a386c221-d6d4-5504-b393-5a679ae5b5d0", "139", "••••7648"],
  ];

  for (const [id, name, sourceRecordId, box, serial] of expected) {
    const person = profile(String(id));
    expect(person).toMatchObject({ display_name: name });
    expect(person.source_records[0]).toMatchObject({
      source_record_id: sourceRecordId,
      rank_as_indexed: null,
      serial_masked: serial,
      box,
      archive_location: "230/86/29/01",
      pdf_page: 89,
    });
    expect(JSON.stringify(person)).not.toMatch(
      /"serial_number"|"serial_number_raw"|"serial_number_normalized"/,
    );
  }
});

test("Batch 455 publishes George and Oswald occupations without inventing employers", async ({ page }) => {
  const expected = [
    ["7ea4e4ac-d953-5662-bd78-1cd3b9fbef1c", "George J Connell", "Machine shop and related occupations, n.e.c.", "1943-05-20"],
    ["aa488229-e09e-5d02-8bc9-ed2c96dfe4ea", "Oswald C Connell", "Accountants and auditors", "1942-10-20"],
  ];

  for (const [id, name, occupation, endDate] of expected) {
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
        relationship_type: "unknown",
        end_date: endDate,
        temporal_basis: "strongly_date_bounded",
        identity_confidence: "confirmed",
        claim_confidence: "medium",
      }),
    );

    await page.goto(`./people/${person.person_id}/`);
    await expect(page.getByRole("heading", { name, exact: true })).toBeVisible();
    await expect(page.locator("main")).toContainText(occupation);
    await expect(page.locator("main")).toContainText(
      "Last civilian employer before serviceNo reliable pre-OSS employer has yet been identified",
    );
  }
});

test("Batch 455 qualifies Emmett F Connelly's identity and last civilian employer", async ({ page }) => {
  const emmett = profile("bfe66780-626e-5662-8a9c-41cbc9e8efb6");
  expect(emmett).toMatchObject({
    display_name: "Emmett F Connelly",
    identity_status: "high_confidence",
    research_status: "documented_prewar_employer_found",
    personnel_category: "commissioned_army_officer",
    commissioned_officer: true,
  });
  expect(emmett.name_variants).toEqual(expect.arrayContaining(["Emmett F. Connely"]));
  expect(emmett.immediate_pre_oss_affiliations).toEqual([]);
  expect(emmett.last_civilian_pre_service).toContainEqual(
    expect.objectContaining({
      canonical_organization: "First of Michigan Corporation",
      role_title: "President",
      occupation: "Investment banker",
      relationship_type: "employment",
      temporal_basis: "probable_immediate",
      identity_confidence: "high_confidence",
      claim_confidence: "medium",
      immediate_pre_oss: false,
      last_civilian_pre_service: true,
    }),
  );
  expect(emmett.claims).toContainEqual(
    expect.objectContaining({
      claim_type: "identity",
      claim_confidence: "high",
      publication_status: "published",
    }),
  );
  expect(emmett.claims).toContainEqual(
    expect.objectContaining({
      claim_type: "last_civilian_pre_service",
      claim_confidence: "medium",
      publication_status: "publish_qualified",
    }),
  );

  await page.goto(`./people/${emmett.person_id}/`);
  await expect(page.getByRole("heading", { name: "Emmett F Connelly", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("Emmett F. Connely");
  await expect(page.locator("main")).toContainText("commissioned army officer");
  await expect(page.locator("main")).toContainText("First of Michigan Corporation");
  await expect(page.locator("main")).toContainText(/do not explicitly exclude an intervening role/i);
  await expect(page.locator("main")).toContainText(/not labeled immediate pre-OSS/i);
});

test("Batch 455 leaves unresolved and ambiguous names claim-free", async () => {
  const expected = [
    ["6aea02bb-61e2-5d97-bb85-5f557d46edc6", "unresolved", "needs_identity_review", "Box 138"],
    ["e435f1a4-b968-522a-9176-5fced06db9f7", "unresolved", "requires_archival_review", "Box 138"],
    ["68c1eaaa-237a-5e35-b9a1-f6401aa066b8", "ambiguous", "needs_identity_review", "Box 139"],
    ["b1ba7b13-1d2f-57d7-8944-14c1b893a141", "ambiguous", "needs_identity_review", "Box 139"],
    ["33aa623b-bd1c-5a12-8a4b-76e51eb786f2", "ambiguous", "needs_identity_review", "Box 139"],
    ["a52e755d-b842-58e6-93e6-8fc147ad510a", "ambiguous", "needs_identity_review", "Box 139"],
    ["25db4b90-8100-5f34-8090-6e9a9e602fbb", "unresolved", "requires_archival_review", "Box 139"],
  ];

  for (const [id, identityStatus, researchStatus, box] of expected) {
    const person = profile(id);
    expect(person).toMatchObject({
      identity_status: identityStatus,
      research_status: researchStatus,
    });
    expect(person.claims).toEqual([]);
    expect(person.immediate_pre_oss_affiliations).toEqual([]);
    expect(person.last_civilian_pre_service).toEqual([]);
    expect(person.other_pre_oss_affiliations).toEqual([]);
    expect(person.next_action).toContain(box);
  }
});

test("Batch 455 organization page carries historical scope and qualified counts", async ({ page }) => {
  const organization = JSON.parse(
    fs.readFileSync(new URL("../src/data/generated/organizations.json", import.meta.url), "utf8"),
  ).find((item: { organization_id: string }) =>
    item.organization_id === "3effebd6-c7a7-5683-9003-1a79d67c137f"
  );
  expect(organization).toMatchObject({
    canonical_name: "First of Michigan Corporation",
    historical_name: "First of Michigan Corporation",
    organization_type: "investment banking firm",
    sector: "finance_and_banking",
    city: "Detroit",
    country: "United States",
    documented_person_count: 1,
  });
  expect(organization.linked_people).toContainEqual(
    expect.objectContaining({
      person_id: "bfe66780-626e-5662-8a9c-41cbc9e8efb6",
      display_name: "Emmett F Connelly",
    }),
  );

  await page.goto(`./organizations/${organization.organization_id}/`);
  await expect(page.getByRole("heading", { name: "First of Michigan Corporation", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("Emmett F Connelly");
  await expect(page.locator("main")).toContainText("last civilian employer before service");
  await expect(page.getByText("medium", { exact: true }).first()).toBeVisible();
});
