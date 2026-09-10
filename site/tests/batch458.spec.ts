import { expect, test } from "@playwright/test";
import fs from "node:fs";

const people = JSON.parse(
  fs.readFileSync(new URL("../src/data/generated/people.json", import.meta.url), "utf8"),
);
const profile = (id: string) =>
  people.find((person: { person_id: string }) => person.person_id === id);

test("Batch 458 preserves all ten printed rows and masks every private identifier", () => {
  const expected = [
    ["b90f6b4f-1fa7-5f2b-b108-a0d507819fde", "Irving Connors", "3cca1fd2-4bf4-510d-8802-32caca0e6078", "139", null],
    ["e71e2add-0ed0-5b5a-b681-52427ef1d3f9", "Allen J Conover", "823b06ae-0390-5e00-b2e3-26ec196311d8", "139", null],
    ["945494f6-580c-59cf-a191-dd40908da929", "Denzil L Conrad", "90a4e1d7-5f12-56bb-ab1d-24d18697d855", "139", "••••5438"],
    ["552ea93d-e41e-5976-a107-c7162eb319ce", "Doda Conrad", "6bc3408f-40da-5c4a-8733-e7a3a58cd87c", "140", "••••1533"],
    ["efdf9ac3-f2ef-547f-95e5-fdd50ab67f20", "Henry Conrad", "98d0f949-017f-543d-b9d2-ec56ebb82c13", "140", null],
    ["6123e5c8-4193-5924-b119-928ce8972216", "Louise W Conrad", "fa2fce4c-2a41-5c2f-87e9-dbdd29a92656", "140", "••••0238"],
    ["4deec738-4af6-5f71-b379-559d1be78196", "Owen M Conrad", "3d8a221b-a792-534b-a06b-8570d035715a", "140", null],
    ["8aa50bf2-4c63-5ad7-a946-5767bf03ac54", "Robert J Conrad", "190e49f7-81d4-517c-aa0e-d74920993418", "140", "••••7255"],
    ["02798f6a-192a-5d35-87df-0d8dacabe18f", "Margaret E Conroy", "6914f255-2ec6-55de-8723-7927b079c728", "140", null],
    ["218e213c-c62e-5f34-a468-ebe49f21458e", "Marion C Conroy", "67d0f287-6948-50e1-aed2-206edea8049f", "140", null],
  ];

  for (const [id, name, sourceRecordId, box, serial] of expected) {
    const person = profile(String(id));
    expect(person).toMatchObject({ display_name: name });
    expect(person.source_records).toContainEqual(
      expect.objectContaining({
        source_record_id: sourceRecordId,
        rank_as_indexed: null,
        serial_masked: serial,
        box,
        archive_location: "230/86/29/01",
        pdf_page: 90,
      }),
    );
    expect(JSON.stringify(person)).not.toMatch(
      /"serial_number"|"serial_number_raw"|"serial_number_normalized"/,
    );
  }
});

test("Batch 458 publishes Doda Conrad's musical career without inventing an employer", async ({ page }) => {
  const doda = profile("552ea93d-e41e-5976-a107-c7162eb319ce");
  expect(doda).toMatchObject({
    display_name: "Doda Conrad",
    identity_status: "high_confidence",
    research_status: "occupation_only_found",
    personnel_category: "enlisted_army_personnel",
    commissioned_officer: false,
  });
  expect(doda.immediate_pre_oss_affiliations).toEqual([]);
  expect(doda.last_civilian_pre_service).toEqual([]);
  expect(doda.other_pre_oss_affiliations).toContainEqual(
    expect.objectContaining({
      role_title: "Baritone and bass singer",
      occupation: "Musicians and teachers of music",
      relationship_type: "unknown",
      end_date: "1942-07-13",
      temporal_basis: "strongly_date_bounded",
      identity_confidence: "high_confidence",
      claim_confidence: "high",
    }),
  );

  await page.goto("./people/" + doda.person_id + "/");
  await expect(page.getByRole("heading", { name: "Doda Conrad", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("Baritone and bass singer");
  await expect(page.locator("main")).toContainText("Musicians and teachers of music");
  await expect(page.locator("main")).toContainText(
    "Last civilian employer before serviceNo reliable pre-OSS employer has yet been identified",
  );
});

test("Batch 458 qualifies Owen Conrad's occupation and leaves commissioned status indeterminate", async ({ page }) => {
  const owen = profile("4deec738-4af6-5f71-b379-559d1be78196");
  expect(owen).toMatchObject({
    display_name: "Owen M Conrad",
    identity_status: "high_confidence",
    research_status: "occupation_only_found",
    personnel_category: "unknown_or_indeterminate",
    commissioned_officer: null,
  });
  expect(owen.other_pre_oss_affiliations).toContainEqual(
    expect.objectContaining({
      occupation: "Salespersons",
      end_date: "1942-10-30",
      identity_confidence: "high_confidence",
      claim_confidence: "medium",
    }),
  );

  await page.goto("./people/" + owen.person_id + "/");
  await expect(page.getByRole("heading", { name: "Owen M Conrad", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("Salespersons");
  await expect(page.locator("main")).toContainText("no employer is identified");
});

test("Batch 458 publishes Robert Conrad's confirmed motorman finding and Louise Conrad's conflict", async ({ page }) => {
  const robert = profile("8aa50bf2-4c63-5ad7-a946-5767bf03ac54");
  expect(robert).toMatchObject({
    identity_status: "confirmed",
    research_status: "occupation_only_found",
    personnel_category: "enlisted_army_personnel",
    commissioned_officer: false,
  });
  expect(robert.other_pre_oss_affiliations).toContainEqual(
    expect.objectContaining({
      occupation: "Motormen, street, subway, and elevated railway",
      end_date: "1943-02-16",
      claim_confidence: "medium",
    }),
  );

  const louise = profile("6123e5c8-4193-5924-b119-928ce8972216");
  expect(louise).toMatchObject({
    identity_status: "conflicting",
    research_status: "conflicting_sources",
    personnel_category: "unknown_or_indeterminate",
    commissioned_officer: null,
    manual_review_required: true,
  });
  expect(louise.other_pre_oss_affiliations).toEqual([]);
  expect(louise.claims).toContainEqual(
    expect.objectContaining({
      claim_type: "identity",
      claim_confidence: "conflicting",
      publication_status: "conflicting",
    }),
  );
  expect(JSON.stringify(louise)).not.toContain("15120238");

  await page.goto("./people/" + louise.person_id + "/");
  await expect(page.getByRole("heading", { name: "Louise W Conrad", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("first-name conflict");
  await expect(page.locator("main")).toContainText("Box 140");
});

test("Batch 458 keeps the six unresolved or ambiguous records claim-free", () => {
  const expected = [
    ["b90f6b4f-1fa7-5f2b-b108-a0d507819fde", "unresolved", "requires_archival_review"],
    ["e71e2add-0ed0-5b5a-b681-52427ef1d3f9", "unresolved", "requires_archival_review"],
    ["945494f6-580c-59cf-a191-dd40908da929", "ambiguous", "needs_identity_review"],
    ["efdf9ac3-f2ef-547f-95e5-fdd50ab67f20", "ambiguous", "needs_identity_review"],
    ["02798f6a-192a-5d35-87df-0d8dacabe18f", "unresolved", "requires_archival_review"],
    ["218e213c-c62e-5f34-a468-ebe49f21458e", "unresolved", "requires_archival_review"],
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
    expect(person.next_action).toMatch(/Box 139|Box 140/);
  }
});
