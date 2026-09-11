import { expect, test } from "@playwright/test";
import fs from "node:fs";

const people = JSON.parse(
  fs.readFileSync(new URL("../src/data/generated/people.json", import.meta.url), "utf8"),
);
const profile = (id: string) =>
  people.find((person: { person_id: string }) => person.person_id === id);

test("Batch 471 preserves all ten page 93 source rows and masks every printed identifier", () => {
  const expected = [
    ["e2475a96-97a5-53b0-b063-416f3fb48709", "Ismael Cordero", "a3ee04d4-d365-5664-8a26-1216a4b8f0ae", "••••1377"],
    ["64de3d81-d381-57b1-a2c9-0dedb86c4d96", "Robert Cordes", "cdea1ae7-07e4-5517-a381-5b718ff0fc45", null],
    ["0071d033-32cd-5bf1-b149-e55605bebc95", "Frances A Cordle", "ac499556-b53e-510e-89f2-479fd54374dc", null],
    ["362f257a-489e-56d9-a311-d2e888388ddd", "Victor Cordovi", "107c9dee-f7d7-5cf5-86a1-de0303e778e3", "••••4676"],
    ["c67152c3-c1dd-5075-91a2-28ba2e20f63d", "Donald L Coriell", "89ab044d-c416-5d06-aa67-fa315a618aa0", "••••7173"],
    ["ed445d13-d943-5c35-b079-bcebe108bf41", "John W Corley", "c74f0653-0a69-53a0-bba8-64bbf6dcaf4a", "••••9692"],
    ["e6deade4-0ba0-5d6c-990c-767e5668e4b5", "Helen E Corliss", "91cc664c-b3af-5124-98b8-52c8f8ce19ff", null],
    ["2f216eaf-def2-528d-866e-4f3782b7f42f", "Margaret L Corman", "20bdcd44-9ef9-5f72-810e-719bf12532ea", "••••1613"],
    ["708df59b-c828-52fe-ac9b-44cb448ea538", "Alton P Cormier", "3e7b9ddc-1f4d-50fb-a7dd-65c363722b47", "••••4224"],
    ["2e92f331-5371-5051-9b7a-0407d062cdb6", "Robert A Cormier", "d68cd2ec-f5fc-59a3-b2e3-de881a5a958a", "••••5133"],
  ];

  for (const [id, name, sourceRecordId, serial] of expected) {
    const person = profile(String(id));
    expect(person).toMatchObject({ display_name: name });
    expect(person.source_records).toContainEqual(
      expect.objectContaining({
        source_record_id: sourceRecordId,
        rank_as_indexed: null,
        serial_masked: serial,
        notes_as_indexed: null,
        box: "144",
        archive_location: "230/86/29/02",
        pdf_page: 93,
      }),
    );
    expect(JSON.stringify(person)).not.toMatch(
      /"serial_number"|"serial_number_raw"|"serial_number_normalized"/,
    );
  }
});

test("Batch 471 publishes only qualified Army-entry occupations for Ismael Cordero and Donald Coriell", async ({ page }) => {
  const expected = [
    [
      "e2475a96-97a5-53b0-b063-416f3fb48709",
      "Ismael Cordero",
      "Kitchen workers in hotels, restaurants, railroads, steamships, etc., n.e.c.",
      "1942-03-02",
    ],
    [
      "c67152c3-c1dd-5075-91a2-28ba2e20f63d",
      "Donald L Coriell",
      "Occupations in manufacture of boots and shoes",
      "1943-03-26",
    ],
  ];

  for (const [id, name, occupation, endDate] of expected) {
    const person = profile(String(id));
    expect(person).toMatchObject({
      display_name: name,
      identity_status: "confirmed",
      personnel_category: "enlisted_army_personnel",
      commissioned_officer: false,
      research_status: "occupation_only_found",
    });
    expect(person.immediate_pre_oss_affiliations).toEqual([]);
    expect(person.last_civilian_pre_service).toEqual([]);
    expect(person.other_pre_oss_affiliations).toContainEqual(
      expect.objectContaining({
        organization_id: null,
        occupation,
        relationship_type: "unknown",
        end_date: endDate,
        temporal_basis: "temporal_relation_uncertain",
        claim_confidence: "medium",
      }),
    );

    await page.goto(`./people/${id}/`);
    await expect(page.getByRole("heading", { name: String(name), exact: true })).toBeVisible();
    await expect(page.locator("main")).toContainText(String(occupation));
    await expect(page.locator("main")).toContainText("No reliable pre-OSS employer has yet been identified");
  }
});

test("Batch 471 confirms Victor Cordovi while preserving the chronology conflict and withholding a predecessor", async ({ page }) => {
  const victor = profile("362f257a-489e-56d9-a311-d2e888388ddd");
  expect(victor).toMatchObject({
    display_name: "Victor Cordovi",
    identity_status: "confirmed",
    personnel_category: "enlisted_army_personnel",
    commissioned_officer: false,
    manual_review_required: false,
    research_status: "requires_archival_review",
  });
  expect(victor.name_variants).toEqual(expect.arrayContaining(["Victor A Cordovi", "Victor A. Cordovi"]));
  expect(victor.immediate_pre_oss_affiliations).toEqual([]);
  expect(victor.last_civilian_pre_service).toEqual([]);
  expect(victor.other_pre_oss_affiliations).toEqual([]);
  expect(victor.claims).toContainEqual(
    expect.objectContaining({
      claim_type: "identity",
      claim_confidence: "confirmed",
      publication_status: "published",
      match_notes: expect.stringContaining("1941/1943 arrival-date disagreement"),
    }),
  );

  await page.goto("./people/362f257a-489e-56d9-a311-d2e888388ddd/");
  await expect(page.getByRole("heading", { name: "Victor Cordovi", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("Cable-Victor Cordovi");
  await expect(page.locator("main")).toContainText("1941-versus-1943 U.S.-arrival disagreement");
  await expect(page.locator("main")).toContainText("No reliable pre-OSS employer has yet been identified");
});

test("Batch 471 separates confirmed post-OSS Army identity from unresolved and ambiguous namesakes", async ({ page }) => {
  const john = profile("ed445d13-d943-5c35-b079-bcebe108bf41");
  expect(john).toMatchObject({
    display_name: "John W Corley",
    identity_status: "confirmed",
    personnel_category: "enlisted_army_personnel",
    commissioned_officer: false,
    research_status: "requires_archival_review",
  });
  expect(john.immediate_pre_oss_affiliations).toEqual([]);
  expect(john.last_civilian_pre_service).toEqual([]);
  expect(john.other_pre_oss_affiliations).toEqual([]);
  expect(john.claims[0].temporal_assessment).toContain("postdates OSS dissolution");

  for (const id of [
    "64de3d81-d381-57b1-a2c9-0dedb86c4d96",
    "0071d033-32cd-5bf1-b149-e55605bebc95",
    "e6deade4-0ba0-5d6c-990c-767e5668e4b5",
  ]) {
    const person = profile(id);
    expect(person).toMatchObject({
      identity_status: "unresolved",
      research_status: "requires_archival_review",
      manual_review_required: true,
    });
    expect(person.claims).toEqual([]);
    expect(person.other_pre_oss_affiliations).toEqual([]);
  }

  for (const id of [
    "2f216eaf-def2-528d-866e-4f3782b7f42f",
    "708df59b-c828-52fe-ac9b-44cb448ea538",
    "2e92f331-5371-5051-9b7a-0407d062cdb6",
  ]) {
    const person = profile(id);
    expect(person).toMatchObject({
      identity_status: "ambiguous",
      personnel_category: "unknown_or_indeterminate",
      commissioned_officer: null,
      research_status: "requires_archival_review",
      manual_review_required: true,
    });
    expect(person.claims).toEqual([]);
    expect(person.other_pre_oss_affiliations).toEqual([]);
  }

  await page.goto("./people/ed445d13-d943-5c35-b079-bcebe108bf41/");
  await expect(page.getByRole("heading", { name: "John W Corley", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("postdates OSS dissolution");
  await expect(page.locator("main")).toContainText("No reliable pre-OSS employer has yet been identified");
});
