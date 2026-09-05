import { expect, test } from "@playwright/test";
import fs from "node:fs";

const people = JSON.parse(fs.readFileSync(new URL("../src/data/generated/people.json", import.meta.url), "utf8"));
const profile = (id: string) => people.find((p: { person_id: string }) => p.person_id === id);

test("Batch 425 publishes two qualified observations without inventing employers", async ({ page }) => {
  for (const [id, name, occupation, relationship] of [
    ["8b2caa9b-cd02-5ed8-92e3-55bc98b51592", "Thomas B Clark", "Teachers (secondary school) and principals", "unknown"],
    ["691bddc7-42a8-5fc8-95b8-95fb6c0a0ffa", "William F Clark", "Student", "student"],
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
      relationship_type: relationship,
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

test("Batch 425 keeps occupation, student status, and commissioned rank distinct", async ({ page }) => {
  const thomas = profile("8b2caa9b-cd02-5ed8-92e3-55bc98b51592");
  expect(thomas.claims).toContainEqual(expect.objectContaining({
    claim_type: "occupation",
    claim_confidence: "medium",
  }));
  await page.goto(`./people/${thomas.person_id}/`);
  await expect(page.locator("main")).toContainText("standard-card civilian-occupation field");
  await expect(page.locator("main")).toContainText("no school or employer is identified");

  const william = profile("691bddc7-42a8-5fc8-95b8-95fb6c0a0ffa");
  expect(william.claims).toContainEqual(expect.objectContaining({
    claim_type: "other_pre_oss_affiliation",
    claim_confidence: "medium",
  }));
  await page.goto(`./people/${william.person_id}/`);
  await expect(page.locator("main")).toContainText("Dates not established · student");
  await expect(page.locator("main")).toContainText("no school or employer is identified");

  const walter = profile("c140f7ad-9ab0-5736-9a24-e1b2a095291a");
  expect(walter).toMatchObject({
    display_name: "Walter R Clark",
    identity_status: "unresolved",
    personnel_category: "commissioned_army_officer",
    commissioned_officer: true,
    research_status: "requires_archival_review",
  });
  expect(walter.claims).toEqual([]);
  await page.goto(`./people/${walter.person_id}/`);
  await expect(page.locator("main")).toContainText("Rank or grade");
  await expect(page.locator("main")).toContainText("Capt");
  await expect(page.locator("main")).toContainText("Twelve exact-name Walter R Clark Army rows carry other identifiers");
});

test("Batch 425 keeps identifier non-hits and name-only candidates out of public claims", async ({ page }) => {
  for (const [id, name, identityStatus, researchStatus, evidence] of [
    ["06035c12-8422-557a-afe0-94a03e982154", "Vernon S Clark", "ambiguous", "needs_identity_review", "Two exact-name Vernon S Clark Army rows carry other identifiers"],
    ["7c27b55e-85b8-5525-ba5e-eece7ad001b4", "William R Clark", "unresolved", "requires_archival_review", "Sixty-two exact-name William R Clark Army rows carry other identifiers"],
    ["7b7255e8-3129-5c82-8e05-ae524b1cb86b", "Edward Clarke", "ambiguous", "needs_identity_review", "two exact-name Edward Clarke rows"],
    ["603d27f9-ebbe-5350-9106-8e24c7e311f4", "Frederick C Clarke", "ambiguous", "needs_identity_review", "sole exact-name Frederick C Clarke Army row"],
    ["a8a374fe-22fd-5573-b951-ca95ea706537", "Grace M Clarke", "unresolved", "requires_archival_review", "no exact-name Grace M Clarke row"],
    ["feb323df-2ba4-5414-8be3-46281841ba2b", "James F Clarke", "ambiguous", "needs_identity_review", "eleven exact-name James F Clarke rows"],
    ["d4aba826-d746-5aec-b438-d926bd3c281c", "Josephine Clarke", "unresolved", "requires_archival_review", "no exact-name Josephine Clarke row"],
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
    await expect(page.locator("main")).toContainText("Review Box 127");
    await expect(page.locator("main")).not.toContainText(/\b\d{8}\b/);
  }
});

test("Batch 425 preserves page 83, Box 127, rank, and exact-name search", async ({ page }) => {
  const expected = [
    ["8b2caa9b-cd02-5ed8-92e3-55bc98b51592", "Thomas B Clark", "e48b1524-6873-5ba1-be95-797a70cac954", null],
    ["06035c12-8422-557a-afe0-94a03e982154", "Vernon S Clark", "3f8eb1b5-4b7c-5332-ac04-17e4066f7cc1", null],
    ["c140f7ad-9ab0-5736-9a24-e1b2a095291a", "Walter R Clark", "88495bb9-77bd-5d41-b176-628396d6bc83", "Capt"],
    ["691bddc7-42a8-5fc8-95b8-95fb6c0a0ffa", "William F Clark", "fc837e14-6ca0-59c0-87b2-dc4369c2953b", null],
    ["7c27b55e-85b8-5525-ba5e-eece7ad001b4", "William R Clark", "5736e024-6da8-5d8f-bd59-32f72c568ae3", null],
    ["7b7255e8-3129-5c82-8e05-ae524b1cb86b", "Edward Clarke", "6c63c585-b1d2-57ac-80ff-e46c207cb6e5", null],
    ["603d27f9-ebbe-5350-9106-8e24c7e311f4", "Frederick C Clarke", "d8e2849e-6329-53f3-87de-fadb78c3f026", null],
    ["a8a374fe-22fd-5573-b951-ca95ea706537", "Grace M Clarke", "e372f2a2-6926-5f55-a72a-be75d91b5022", null],
    ["feb323df-2ba4-5414-8be3-46281841ba2b", "James F Clarke", "d4b7ea36-462c-58f8-a3a9-1f9ad94f2dfb", null],
    ["d4aba826-d746-5aec-b438-d926bd3c281c", "Josephine Clarke", "387c07c9-5693-5a69-9ca8-537d2e847a7d", null],
  ];

  for (const [id, name, sourceRecordId, rank] of expected) {
    const p = profile(String(id));
    expect(p.source_records[0]).toMatchObject({
      source_record_id: sourceRecordId,
      pdf_page: 83,
      box: "127",
      archive_location: "230/86/28/07",
      rank_as_indexed: rank,
    });

    await page.goto(`./people/?q=${encodeURIComponent(String(name))}`);
    await expect(page.getByRole("link", { name: String(name), exact: true })).toBeVisible();
  }
});

test("Batch 425 evidence is cited and public projections retain only masked identifiers", async ({ page }) => {
  for (const id of [
    "8b2caa9b-cd02-5ed8-92e3-55bc98b51592",
    "691bddc7-42a8-5fc8-95b8-95fb6c0a0ffa",
  ]) {
    const p = profile(id);
    expect(p.claims).toHaveLength(2);
    expect(p.source_records[0].serial_masked).toMatch(/^••••\d{4}$/);
    expect(JSON.stringify(p)).not.toMatch(/"serial_number"|"serial_number_raw"|"serial_number_normalized"/);

    await page.goto(`./people/${id}/`);
    await expect(page.getByRole("link", { name: "Electronic Army Serial Number Merged File, ca. 1938-1946" }).first()).toBeVisible();
    await expect(page.getByRole("link", { name: "NARA Compiled Code Lists for the Electronic Army Serial Number Merged File" })).toBeVisible();
    await expect(page.locator("main")).not.toContainText(/\b\d{8}\b/);
  }
});
