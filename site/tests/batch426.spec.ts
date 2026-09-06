import { expect, test } from "@playwright/test";
import fs from "node:fs";

const people = JSON.parse(fs.readFileSync(new URL("../src/data/generated/people.json", import.meta.url), "utf8"));
const profile = (id: string) => people.find((p: { person_id: string }) => p.person_id === id);

test("Batch 426 publishes two qualified observations without inventing employers", async ({ page }) => {
  for (const [id, name, occupation, relationship] of [
    ["51ad2418-5d75-5f18-9548-8bfbe4b26388", "Norman F Clarke", "Engineers, electrical", "unknown"],
    ["fb3a1629-f724-56c3-ba56-5e5c3c0783ae", "William W Clarke", "Student", "student"],
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

test("Batch 426 keeps occupation, student status, and Navy rank distinct", async ({ page }) => {
  const norman = profile("51ad2418-5d75-5f18-9548-8bfbe4b26388");
  expect(norman.claims).toContainEqual(expect.objectContaining({
    claim_type: "occupation",
    claim_confidence: "medium",
  }));
  await page.goto(`./people/${norman.person_id}/`);
  await expect(page.locator("main")).toContainText("Enlisted Reserve Corps occupation field");
  await expect(page.locator("main")).toContainText("no employer is identified");

  const william = profile("fb3a1629-f724-56c3-ba56-5e5c3c0783ae");
  expect(william.claims).toContainEqual(expect.objectContaining({
    claim_type: "other_pre_oss_affiliation",
    claim_confidence: "medium",
  }));
  await page.goto(`./people/${william.person_id}/`);
  await expect(page.locator("main")).toContainText("Dates not established · student");
  await expect(page.locator("main")).toContainText("no school or employer is identified");

  const paul = profile("a2bf698b-9594-5006-a7fa-940527f7cdf5");
  expect(paul).toMatchObject({
    display_name: "Paul W Clarke",
    identity_status: "ambiguous",
    personnel_category: "enlisted_naval_personnel",
    commissioned_officer: false,
    research_status: "needs_identity_review",
  });
  expect(paul.claims).toEqual([]);
  await page.goto(`./people/${paul.person_id}/`);
  await expect(page.locator("main")).toContainText("Rank or grade");
  await expect(page.locator("main")).toContainText("S 2/c");
  await expect(page.locator("main")).toContainText("sole exact-name Army row carries a different identifier");
});

test("Batch 426 keeps unbridged identity candidates out of public claims", async ({ page }) => {
  for (const [id, name, identityStatus, researchStatus, evidence, box] of [
    ["346cd1cc-591a-52aa-a42e-9097eb036d7d", "Kathleen M Clarke", "unresolved", "requires_archival_review", "no exact-name Kathleen M Clarke row", "127"],
    ["e7fc210e-05c7-5f7a-889b-150f11240159", "Marianne Clarke", "ambiguous", "needs_identity_review", "Special Funds Branch", "127"],
    ["f198235d-0875-5a6a-8612-84a144dc2e58", "Mildred A Clarke", "unresolved", "requires_archival_review", "no exact-name Mildred A Clarke row", "128"],
    ["8ef8c631-d21b-5ded-b37f-75a9a611090d", "Ruby M Clarke", "unresolved", "requires_archival_review", "no exact-name Ruby M Clarke row", "128"],
    ["09e7fb81-4196-537f-89ca-499b219a8559", "Harold W Classen", "ambiguous", "needs_identity_review", "seven-digit identifier cannot be silently padded", "125"],
    ["a5ba614e-3a6f-5888-b9aa-3d1c5e30dd62", "Henri L Claudel", "ambiguous", "needs_identity_review", "writing to Franklin Roosevelt in 1941", "128"],
    ["c14f5faa-ad3f-555a-aa15-b8b1e869b251", "Frederick Claudy", "ambiguous", "needs_identity_review", "1912-1997 genealogy lead", "128"],
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
    await expect(page.locator("main")).toContainText(`Review Box ${box}`);
    await expect(page.locator("main")).not.toContainText(/\b\d{8}\b/);
  }
});

test("Batch 426 preserves page 83, boxes, rank, and exact-name search", async ({ page }) => {
  const expected = [
    ["346cd1cc-591a-52aa-a42e-9097eb036d7d", "Kathleen M Clarke", "45afa421-6bb2-5c9b-be70-00266838bdf4", "127", "230/86/28/07", null],
    ["e7fc210e-05c7-5f7a-889b-150f11240159", "Marianne Clarke", "2834cfcd-6913-5244-883c-6dbbb0b43d20", "127", "230/86/28/07", null],
    ["f198235d-0875-5a6a-8612-84a144dc2e58", "Mildred A Clarke", "4f26fdab-cdb3-518b-89de-4ff88b2e2cb0", "128", "230/86/28/07", null],
    ["51ad2418-5d75-5f18-9548-8bfbe4b26388", "Norman F Clarke", "ba10c42a-3c80-5c44-b87b-622b4b941bb4", "128", "230/86/28/07", null],
    ["a2bf698b-9594-5006-a7fa-940527f7cdf5", "Paul W Clarke", "88075372-d75d-5b4b-8309-5391a6ee2458", "128", "230/86/28/07", "S 2/c"],
    ["8ef8c631-d21b-5ded-b37f-75a9a611090d", "Ruby M Clarke", "041013c1-3df6-5b8a-afa9-f004029ebe2d", "128", "230/86/28/07", null],
    ["fb3a1629-f724-56c3-ba56-5e5c3c0783ae", "William W Clarke", "5da59369-3654-56b7-8eec-c10860b99c9b", "128", "230/86/28/07", null],
    ["09e7fb81-4196-537f-89ca-499b219a8559", "Harold W Classen", "3b7776c4-eef8-599b-91cf-b6ffb8a46bc2", "125", "230/86/28/06", null],
    ["a5ba614e-3a6f-5888-b9aa-3d1c5e30dd62", "Henri L Claudel", "a7437309-b6a4-566f-9761-f5aa191840ec", "128", "230/86/28/07", null],
    ["c14f5faa-ad3f-555a-aa15-b8b1e869b251", "Frederick Claudy", "9a7a82b9-a63b-5793-9be7-656b25906d97", "128", "230/86/28/07", null],
  ];

  for (const [id, name, sourceRecordId, box, location, rank] of expected) {
    const p = profile(String(id));
    expect(p.source_records[0]).toMatchObject({
      source_record_id: sourceRecordId,
      pdf_page: 83,
      box,
      archive_location: location,
      rank_as_indexed: rank,
    });

    await page.goto(`./people/?q=${encodeURIComponent(String(name))}`);
    await expect(page.getByRole("link", { name: String(name), exact: true })).toBeVisible();
  }
});

test("Batch 426 evidence is cited and public projections retain only masked identifiers", async ({ page }) => {
  for (const id of [
    "51ad2418-5d75-5f18-9548-8bfbe4b26388",
    "fb3a1629-f724-56c3-ba56-5e5c3c0783ae",
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
