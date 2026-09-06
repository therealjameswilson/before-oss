import { expect, test } from "@playwright/test";
import fs from "node:fs";

const people = JSON.parse(fs.readFileSync(new URL("../src/data/generated/people.json", import.meta.url), "utf8"));
const organizations = JSON.parse(fs.readFileSync(new URL("../src/data/generated/organizations.json", import.meta.url), "utf8"));
const profile = (id: string) => people.find((p: { person_id: string }) => p.person_id === id);

test("Batch 427 publishes two qualified occupations without inventing employers", async ({ page }) => {
  for (const [id, name, occupation] of [
    ["1363f4f6-0b47-5f2e-a690-6b942e65a415", "Gladys Claunch", "Clerks, general office"],
    ["68e2533a-824c-510d-bccc-9293695107bd", "Kenneth E Clawson", "Clerks and kindred occupations, n.e.c."],
  ]) {
    const p = profile(String(id));
    expect(p).toMatchObject({
      display_name: name,
      identity_status: "confirmed",
      personnel_category: "enlisted_army_personnel",
      commissioned_officer: false,
      research_status: "occupation_only_found",
    });
    expect(p.immediate_pre_oss_affiliations).toEqual([]);
    expect(p.last_civilian_pre_service).toEqual([]);
    expect(p.other_pre_oss_affiliations).toContainEqual(expect.objectContaining({
      organization_id: null,
      occupation,
      relationship_type: "unknown",
      temporal_basis: "temporal_relation_uncertain",
      claim_confidence: "medium",
    }));

    await page.goto(`./people/${id}/`);
    await expect(page.getByRole("heading", { name: String(name), exact: true })).toBeVisible();
    await expect(page.locator("main")).toContainText(String(occupation));
    await expect(page.locator("main")).toContainText("No reliable pre-OSS employer");
    await expect(page.locator("main")).not.toContainText(/\b\d{8}\b/);
  }
});

test("Batch 427 keeps Donald C Clayman's prewar Army pathway distinct from civilian employment", async ({ page }) => {
  const donald = profile("19bcd03f-a4b3-5c5c-8f50-5c99335042b3");
  expect(donald).toMatchObject({
    display_name: "Donald C Clayman",
    identity_status: "high_confidence",
    personnel_category: "commissioned_army_officer",
    commissioned_officer: true,
    research_status: "requires_archival_review",
  });
  expect(donald.immediate_pre_oss_affiliations).toEqual([]);
  expect(donald.last_civilian_pre_service).toEqual([]);
  expect(donald.other_pre_oss_affiliations).toContainEqual(expect.objectContaining({
    canonical_organization: "United States Army Infantry Reserve",
    organization_name_as_found: "Inf-Res.",
    relationship_type: "military_assignment",
    temporal_basis: "documented_prewar",
    claim_confidence: "high",
  }));
  expect(donald.claims).toContainEqual(expect.objectContaining({
    claim_type: "other_pre_oss_affiliation",
    claim_confidence: "high",
    publication_status: "publish_qualified",
  }));

  const armyReserve = organizations.find((o: { canonical_name: string }) => o.canonical_name === "United States Army Infantry Reserve");
  expect(armyReserve).toMatchObject({
    historical_name: "Infantry Reserve",
    sector: "military",
  });

  await page.goto(`./people/${donald.person_id}/`);
  await expect(page.getByRole("heading", { name: "Donald C Clayman", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("United States Army Infantry Reserve");
  await expect(page.locator("main")).toContainText("31 May 1935");
  await expect(page.locator("main")).toContainText("military assignment");
  await expect(page.locator("main")).toContainText("No reliable pre-OSS employer");
  await expect(page.locator("main")).not.toContainText(/\b\d{8}\b/);
});

test("Batch 427 keeps name-only and rejected candidates out of public facts", async ({ page }) => {
  for (const [id, name, identityStatus, researchStatus, evidence] of [
    ["145e89be-ebe0-5ded-992d-73168c91e5d2", "Clarence Clausen", "ambiguous", "needs_identity_review", "Jack George Clausen"],
    ["d4b8f632-fdf4-579f-a042-2eacac2ecb1b", "Paul Clavecilla", "unresolved", "requires_archival_review", "no exact-name Paul Clavecilla row"],
    ["e655b258-397b-5248-a17a-f2ffdbc5c124", "Arthur L Clawson", "ambiguous", "needs_identity_review", "19 April 1946"],
    ["3f9af7e4-514f-5d66-a135-b984190cc303", "Donald M Clawson", "unresolved", "requires_archival_review", "no exact-name Donald M Clawson row"],
    ["fe1837af-6d03-57f8-ab0d-f7fd40933171", "Alta T Clay", "ambiguous", "needs_identity_review", "one exact-name Alta T Clay WAC row"],
    ["d0b9752b-db40-5611-960c-51e5fd4dfa42", "Jeff Clay III", "unresolved", "requires_archival_review", "no exact-name Jeff Clay III row"],
    ["017c3992-1f2e-506c-a6c1-5cf2fa1b062e", "Lee H Clayman", "ambiguous", "needs_identity_review", "501st Parachute Infantry Regiment"],
  ]) {
    const p = profile(String(id));
    expect(p).toMatchObject({
      display_name: name,
      identity_status: identityStatus,
      research_status: researchStatus,
      personnel_category: "unknown_or_indeterminate",
      commissioned_officer: null,
    });
    expect(p.claims).toEqual([]);
    expect(p.other_pre_oss_affiliations).toEqual([]);

    await page.goto(`./people/${id}/`);
    await expect(page.getByRole("heading", { name: String(name), exact: true })).toBeVisible();
    await expect(page.locator("main")).toContainText(String(evidence));
    await expect(page.locator("main")).toContainText("Review Box 128");
    await expect(page.locator("main")).not.toContainText(/\b\d{8}\b/);
  }
});

test("Batch 427 preserves page 83 source rows and exact-name search", async ({ page }) => {
  const expected = [
    ["1363f4f6-0b47-5f2e-a690-6b942e65a415", "Gladys Claunch", "71007b26-9ecc-50d5-824c-b7d39b7e1c11"],
    ["145e89be-ebe0-5ded-992d-73168c91e5d2", "Clarence Clausen", "c94bfb6c-2b9b-558b-b1b0-cde9f30f8196"],
    ["d4b8f632-fdf4-579f-a042-2eacac2ecb1b", "Paul Clavecilla", "8165e30b-84c6-54c5-afa1-4be30951dfb1"],
    ["e655b258-397b-5248-a17a-f2ffdbc5c124", "Arthur L Clawson", "e80808b5-6bf2-52c1-9637-71192333bf71"],
    ["3f9af7e4-514f-5d66-a135-b984190cc303", "Donald M Clawson", "51d614a6-fc70-5fda-9ea5-974a1201a4d3"],
    ["68e2533a-824c-510d-bccc-9293695107bd", "Kenneth E Clawson", "e7963958-2350-5e28-b79e-05343ec1b1ac"],
    ["fe1837af-6d03-57f8-ab0d-f7fd40933171", "Alta T Clay", "588c9464-13ff-5c3e-b792-7ec841d19644"],
    ["d0b9752b-db40-5611-960c-51e5fd4dfa42", "Jeff Clay III", "c03eca5e-ed50-5ab2-a265-64b71ba50565"],
    ["19bcd03f-a4b3-5c5c-8f50-5c99335042b3", "Donald C Clayman", "1445f77e-382c-58aa-ae8b-d4c8adf53607"],
    ["017c3992-1f2e-506c-a6c1-5cf2fa1b062e", "Lee H Clayman", "23ac40e6-c1a6-53e8-bbdc-cd9896778698"],
  ];

  for (const [id, name, sourceRecordId] of expected) {
    const p = profile(String(id));
    expect(p.source_records[0]).toMatchObject({
      source_record_id: sourceRecordId,
      pdf_page: 83,
      box: "128",
      archive_location: "230/86/28/07",
      rank_as_indexed: null,
    });

    await page.goto(`./people/?q=${encodeURIComponent(String(name))}`);
    await expect(page.getByRole("link", { name: String(name), exact: true })).toBeVisible();
  }
});

test("Batch 427 evidence is cited and public projections retain only masked identifiers", async ({ page }) => {
  for (const id of [
    "1363f4f6-0b47-5f2e-a690-6b942e65a415",
    "68e2533a-824c-510d-bccc-9293695107bd",
    "19bcd03f-a4b3-5c5c-8f50-5c99335042b3",
  ]) {
    const p = profile(id);
    expect(p.claims).toHaveLength(2);
    expect(p.source_records[0].serial_masked).toMatch(/^••••\d{4}$/);
    expect(JSON.stringify(p)).not.toMatch(/"serial_number"|"serial_number_raw"|"serial_number_normalized"/);

    await page.goto(`./people/${id}/`);
    await expect(page.locator("main")).not.toContainText(/\b\d{8}\b/);
  }

  await page.goto("./people/1363f4f6-0b47-5f2e-a690-6b942e65a415/");
  await expect(page.getByRole("link", { name: "Electronic Army Serial Number Merged File, ca. 1938-1946" }).first()).toBeVisible();
  await expect(page.getByRole("link", { name: "NARA Compiled Code Lists for the Electronic Army Serial Number Merged File" })).toBeVisible();

  await page.goto("./people/19bcd03f-a4b3-5c5c-8f50-5c99335042b3/");
  await expect(page.getByRole("link", { name: "Official Army Register, 1946, Volume I" }).first()).toBeVisible();
  await expect(page.getByRole("link", { name: "World War II Master Card File Index" }).first()).toBeVisible();
});
