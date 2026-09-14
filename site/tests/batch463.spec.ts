import { expect, test } from "@playwright/test";
import fs from "node:fs";

const people = JSON.parse(
  fs.readFileSync(new URL("../src/data/generated/people.json", import.meta.url), "utf8"),
);
const profile = (id: string) =>
  people.find((person: { person_id: string }) => person.person_id === id);

test("Batch 463 preserves all ten printed rows and masks private identifiers", () => {
  const expected = [
    ["ff57653b-2745-5eb9-a117-4868e638d64a", "Elizabeth M Cooke", "8648319a-6567-5794-9bac-3a5652105542", null, null],
    ["8f7e665f-6a69-59c8-9d95-df6c80e9d2f4", "Margauerite Cooke", "d89ba6c5-8c38-5faf-8340-b7f18f252249", null, null],
    ["9fcd8ee7-1330-52a8-86fa-fcac21e8f77d", "Mary Cooke", "93966d7b-d2f3-5fa4-8550-5626a695eb81", null, null],
    ["d7c66336-6454-513a-9c65-3e4dd83e7c9c", "Raymond F Cooke", "50827471-076c-58e8-91e3-b67a768a7c7a", null, "••••7497"],
    ["7be1c4e3-6b78-5d8e-9bc9-624c4c45d679", "Frederick Cookson", "1e73b7d8-a273-56f9-9543-70b1edb9c8a2", null, null],
    ["c3328cd1-5357-552b-9644-af1edd47843a", "Nick R Cooky", "fcf8f3e4-8e63-54a0-a6f8-3db9cbfa1f45", "Sgt", null],
    ["aaa43f71-fdfb-5e84-bdb0-05a76de23f45", "Francis J Cooley", "0a1bb3f4-7fd1-554d-bbdf-29d599747708", null, "••••7970"],
    ["83e835ed-907a-5aff-bc49-5d65a2c756ac", "James Cooley", "1f1e8049-4916-5d8a-bddf-44f32c991abe", null, null],
    ["bb585163-0244-5828-aad4-5e124d36a4c2", "Margaret A Cooley", "73e2c6d6-9c8a-5126-9ec7-f3ede841f885", null, null],
    ["8f1c158d-b716-518d-b755-c86f1d5fa0b9", "Marion L Cooley", "7dedc7cc-a922-5a92-b21e-08bd6dba1098", null, null],
  ];

  for (const [id, name, sourceRecordId, rank, serial] of expected) {
    const person = profile(String(id));
    expect(person).toMatchObject({ display_name: name });
    expect(person.source_records).toContainEqual(
      expect.objectContaining({
        source_record_id: sourceRecordId,
        rank_as_indexed: rank,
        serial_masked: serial,
        box: "141",
        archive_location: "230/86/29/01",
        pdf_page: 91,
      }),
    );
    expect(JSON.stringify(person)).not.toMatch(
      /"serial_number"|"serial_number_raw"|"serial_number_normalized"/,
    );
  }
});

test("Batch 463 preserves Cooky as printed and publishes Kukich as a sourced variant", async ({ page }) => {
  const nick = profile("c3328cd1-5357-552b-9644-af1edd47843a");
  expect(nick).toMatchObject({
    display_name: "Nick R Cooky",
    identity_status: "confirmed",
    personnel_category: "enlisted_marine_corps_personnel",
    commissioned_officer: false,
    research_status: "completed",
  });
  expect(nick.name_variants).toContain("Nick R. Kukich");
  expect(nick.source_records).toContainEqual(
    expect.objectContaining({ rank_as_indexed: "Sgt" }),
  );
  expect(nick.claims).toContainEqual(
    expect.objectContaining({
      claim_type: "identity",
      claim_confidence: "confirmed",
      claim_text: expect.stringContaining("Cooky was his documented nickname"),
    }),
  );

  await page.goto("./people/c3328cd1-5357-552b-9644-af1edd47843a/");
  await expect(page.getByRole("heading", { name: "Nick R Cooky", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("Nick R. Kukich");
  await expect(page.locator("main")).toContainText("nickname, not his surname");
});

test("Batch 463 keeps Nick Kukich's military pathway and civilian occupations distinct", async ({ page }) => {
  const nick = profile("c3328cd1-5357-552b-9644-af1edd47843a");
  expect(nick.immediate_pre_oss_affiliations).toContainEqual(
    expect.objectContaining({
      canonical_organization: "United States Marine Corps",
      relationship_type: "military_assignment",
      immediate_pre_oss: true,
      claim_confidence: "high",
    }),
  );
  expect(nick.last_civilian_pre_service).toEqual([]);
  expect(nick.other_pre_oss_affiliations).toEqual(
    expect.arrayContaining([
      expect.objectContaining({ occupation: "Coal miner", organization_id: null, claim_confidence: "high" }),
      expect.objectContaining({ occupation: "Truck driver", organization_id: null, claim_confidence: "medium" }),
    ]),
  );

  const sourceUrls = nick.claims.flatMap((claim: { sources: { source: { stable_url: string } }[] }) =>
    claim.sources.map((link) => link.source.stable_url),
  );
  expect(sourceUrls).toContain(
    "https://www.nps.gov/articles/oss-in-action-the-mediterranean-and-european-theaters.htm",
  );
  expect(sourceUrls).toContain(
    "https://www.govinfo.gov/content/pkg/GOVPUB-D214-PURL-gpo66817/pdf/GOVPUB-D214-PURL-gpo66817.pdf",
  );

  await page.goto("./people/c3328cd1-5357-552b-9644-af1edd47843a/");
  await expect(page.locator("main")).toContainText("United States Marine Corps");
  await expect(page.locator("main")).toContainText("Coal miner");
  await expect(page.locator("main")).toContainText("Truck driver");
  await expect(page.locator("main")).toContainText("No reliable pre-OSS employer has yet been identified");
});

test("Batch 463 publishes Francis Cooley's Army-linked occupation without an employer", async ({ page }) => {
  const francis = profile("aaa43f71-fdfb-5e84-bdb0-05a76de23f45");
  expect(francis).toMatchObject({
    display_name: "Francis J Cooley",
    identity_status: "confirmed",
    personnel_category: "enlisted_army_personnel",
    commissioned_officer: false,
    research_status: "occupation_only_found",
  });
  expect(francis.immediate_pre_oss_affiliations).toEqual([]);
  expect(francis.last_civilian_pre_service).toEqual([]);
  expect(francis.other_pre_oss_affiliations).toContainEqual(
    expect.objectContaining({
      occupation: "Mechanics and repairmen, n.e.c.",
      end_date: "1942-11-23",
      organization_id: null,
      claim_confidence: "medium",
    }),
  );

  await page.goto("./people/aaa43f71-fdfb-5e84-bdb0-05a76de23f45/");
  await expect(page.locator("main")).toContainText("Mechanics and repairmen, n.e.c.");
  await expect(page.locator("main")).toContainText("no employer or trade specialty is identified");
});

test("Batch 463 exposes the Raymond Cooke source gap and keeps unresolved profiles visible", async ({ page }) => {
  const raymond = profile("d7c66336-6454-513a-9c65-3e4dd83e7c9c");
  expect(raymond).toMatchObject({
    identity_status: "unresolved",
    research_status: "requires_archival_review",
    manual_review_required: true,
  });
  expect(raymond.claims).toContainEqual(
    expect.objectContaining({
      claim_type: "archival_file_status",
      claim_confidence: "confirmed",
      publication_status: "published",
    }),
  );

  for (const [id, identityStatus, researchStatus] of [
    ["ff57653b-2745-5eb9-a117-4868e638d64a", "ambiguous", "needs_identity_review"],
    ["8f7e665f-6a69-59c8-9d95-df6c80e9d2f4", "unresolved", "requires_archival_review"],
    ["9fcd8ee7-1330-52a8-86fa-fcac21e8f77d", "ambiguous", "needs_identity_review"],
    ["7be1c4e3-6b78-5d8e-9bc9-624c4c45d679", "ambiguous", "needs_identity_review"],
    ["83e835ed-907a-5aff-bc49-5d65a2c756ac", "ambiguous", "needs_identity_review"],
    ["bb585163-0244-5828-aad4-5e124d36a4c2", "unresolved", "requires_archival_review"],
    ["8f1c158d-b716-518d-b755-c86f1d5fa0b9", "ambiguous", "needs_identity_review"],
  ]) {
    const person = profile(id);
    expect(person).toMatchObject({
      identity_status: identityStatus,
      research_status: researchStatus,
      manual_review_required: true,
    });
    expect(person.immediate_pre_oss_affiliations).toEqual([]);
    expect(person.last_civilian_pre_service).toEqual([]);
    expect(person.other_pre_oss_affiliations).toEqual([]);
  }

  await page.goto("./people/8f7e665f-6a69-59c8-9d95-df6c80e9d2f4/");
  await expect(page.getByRole("heading", { name: "Margauerite Cooke", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("No reliable pre-OSS employer has yet been identified");
  await expect(page.locator("main")).toContainText("Review Box 141");
});
