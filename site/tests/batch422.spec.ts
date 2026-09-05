import { expect, test } from "@playwright/test";
import fs from "node:fs";

const people = JSON.parse(fs.readFileSync(new URL("../src/data/generated/people.json", import.meta.url), "utf8"));
const profile = (id: string) => people.find((p: { person_id: string }) => p.person_id === id);

test("Batch 422 keeps the two Ernest Clark source rows separate", async ({ page }) => {
  const first = profile("11ade8fa-be2b-53fb-8a7e-da039655576d");
  const second = profile("a5164ab7-aa58-5450-ac8c-0509ddcf14af");

  expect(first).toMatchObject({
    display_name: "Ernest D Clark",
    identity_status: "confirmed",
    personnel_category: "unknown_or_indeterminate",
    commissioned_officer: null,
    research_status: "occupation_only_found",
  });
  expect(second).toMatchObject({
    display_name: "Ernest D Clark",
    identity_status: "conflicting",
    personnel_category: "unknown_or_indeterminate",
    commissioned_officer: null,
    research_status: "conflicting_sources",
  });
  expect(first.person_id).not.toBe(second.person_id);
  expect(first.source_records[0].source_record_id).not.toBe(second.source_records[0].source_record_id);
  expect(first.source_records[0].serial_masked).not.toBe(second.source_records[0].serial_masked);
  expect(second.other_pre_oss_affiliations).toEqual([]);

  await page.goto(`./people/${first.person_id}/`);
  await expect(page.locator("main")).toContainText("Engineers, stationary");
  await expect(page.locator("main")).toContainText("first of two consecutive Ernest D Clark index rows");
  await expect(page.locator("main")).toContainText("grade field is malformed");

  await page.goto(`./people/${second.person_id}/`);
  await expect(page.locator("main")).toContainText("middle initial K");
  await expect(page.locator("main")).toContainText("records remain unmerged");
  await expect(page.locator("main")).not.toContainText("Engineers, stationary");
  await expect(page.locator("main")).not.toContainText(/\b\d{8}\b/);
});

test("Batch 422 publishes Frederick Clark only with the source anomaly warning", async ({ page }) => {
  const p = profile("eb20619c-7577-5165-bb02-7d50839b5c62");
  expect(p).toMatchObject({
    display_name: "Frederick L Clark",
    identity_status: "high_confidence",
    personnel_category: "unknown_or_indeterminate",
    commissioned_officer: null,
    research_status: "occupation_only_found",
  });
  expect(p.immediate_pre_oss_affiliations).toEqual([]);
  expect(p.last_civilian_pre_service).toEqual([]);
  expect(p.other_pre_oss_affiliations).toContainEqual(expect.objectContaining({
    occupation: "Furniture manufacturing occupations, n.e.c.",
    relationship_type: "unknown",
    temporal_basis: "temporal_relation_uncertain",
    claim_confidence: "medium",
    organization_id: null,
  }));

  await page.goto(`./people/${p.person_id}/`);
  await expect(page.getByRole("heading", { name: "Frederick L Clark", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("Furniture manufacturing occupations, n.e.c.");
  await expect(page.locator("main")).toContainText("internally anomalous birth-year data");
  await expect(page.locator("main")).toContainText("No reliable pre-OSS employer");
});

test("Batch 422 publishes George H Clark designer evidence without inventing an employer", async ({ page }) => {
  const p = profile("d23af960-e11e-528c-a032-a22178fbf1f7");
  expect(p).toMatchObject({
    display_name: "George H Clark",
    identity_status: "confirmed",
    personnel_category: "enlisted_army_personnel",
    commissioned_officer: false,
    research_status: "occupation_only_found",
  });
  expect(p.immediate_pre_oss_affiliations).toEqual([]);
  expect(p.last_civilian_pre_service).toEqual([]);
  expect(p.other_pre_oss_affiliations).toContainEqual(expect.objectContaining({
    occupation: "Designers",
    relationship_type: "unknown",
    temporal_basis: "temporal_relation_uncertain",
    claim_confidence: "medium",
    organization_id: null,
  }));

  await page.goto(`./people/${p.person_id}/`);
  await expect(page.getByRole("heading", { name: "George H Clark", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("forty-two George H Clark Army rows");
  await expect(page.locator("main")).toContainText("Designers");
  await expect(page.locator("main")).toContainText("No reliable pre-OSS employer");
});

test("Batch 422 withholds the wrong-middle-initial Ellery Clark naval candidate", async ({ page }) => {
  const p = profile("dab524bc-5bdd-5d3c-aebd-3a656d7f58e8");
  expect(p).toMatchObject({
    display_name: "Ellery D Clark",
    identity_status: "unresolved",
    personnel_category: "unknown_or_indeterminate",
    commissioned_officer: null,
    research_status: "candidate_found",
  });
  expect(p.claims).toEqual([]);
  expect(p.other_pre_oss_affiliations).toEqual([]);

  await page.goto(`./people/${p.person_id}/`);
  await expect(page.getByRole("heading", { name: "Ellery D Clark", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("conflicting middle initial");
  await expect(page.locator("main")).toContainText("Discovery candidates are not presented as established facts");
  await expect(page.locator("main")).not.toContainText("Harvard graduation");
});

test("Batch 422 leaves name-only Francis and George O Clark candidates unmerged", async ({ page }) => {
  for (const [id, name, expected] of [
    ["79a7e96d-0c22-5cb1-980a-6c436e19b167", "Francis V Clark", "one exact-name Francis V Clark row"],
    ["70a80998-2872-58dd-908d-d83d15f8a018", "George O Clark Jr.", "two exact-name-with-suffix George O Clark Jr. rows"],
  ]) {
    const p = profile(id);
    expect(p).toMatchObject({
      display_name: name,
      identity_status: "ambiguous",
      personnel_category: "unknown_or_indeterminate",
      commissioned_officer: null,
      research_status: "needs_identity_review",
    });
    expect(p.claims).toEqual([]);
    expect(p.other_pre_oss_affiliations).toEqual([]);

    await page.goto(`./people/${id}/`);
    await expect(page.getByRole("heading", { name, exact: true })).toBeVisible();
    await expect(page.locator("main")).toContainText(expected);
    await expect(page.locator("main")).toContainText("Review Box 126");
    await expect(page.locator("main")).toContainText("No publishable pre-OSS affiliation is recorded yet");
  }
});

test("Batch 422 gives unresolved Clark records complete archival profiles", async ({ page }) => {
  for (const [id, name] of [
    ["050ab3bc-a951-5346-a6d1-18f0030bfed6", "Elizabeth W Clark"],
    ["1fbcf5b2-25ed-5a9a-8bb5-cc53e5eec380", "Frank J Clark"],
    ["352f9c34-ce1e-57ce-a21a-f6446f443e92", "George E Clark"],
  ]) {
    const p = profile(id);
    expect(p).toMatchObject({
      display_name: name,
      identity_status: "unresolved",
      personnel_category: "unknown_or_indeterminate",
      commissioned_officer: null,
      research_status: "requires_archival_review",
    });
    expect(p.claims).toEqual([]);
    expect(p.source_records[0]).toMatchObject({ pdf_page: 82, box: "126", rank_as_indexed: null });

    await page.goto(`./people/${id}/`);
    await expect(page.getByRole("heading", { name, exact: true })).toBeVisible();
    await expect(page.locator("main")).toContainText("Review Box 126");
    await expect(page.locator("main")).toContainText("230/86/28/06");
    await expect(page.locator("main")).toContainText("No reliable pre-OSS employer");
  }
});

test("Batch 422 cohort is searchable and preserves both Ernest Clark rows", async ({ page }) => {
  for (const name of [
    "Elizabeth W Clark",
    "Ellery D Clark",
    "Francis V Clark",
    "Frank J Clark",
    "Frederick L Clark",
    "George H Clark",
    "George E Clark",
    "George O Clark Jr.",
  ]) {
    await page.goto(`./people/?q=${encodeURIComponent(name)}`);
    await expect(page.getByRole("link", { name, exact: true })).toBeVisible();
  }

  await page.goto(`./people/?q=${encodeURIComponent("Ernest D Clark")}`);
  await expect(page.getByRole("link", { name: "Ernest D Clark", exact: true })).toHaveCount(2);
});
