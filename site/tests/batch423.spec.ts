import { expect, test } from "@playwright/test";
import fs from "node:fs";

const people = JSON.parse(fs.readFileSync(new URL("../src/data/generated/people.json", import.meta.url), "utf8"));
const profile = (id: string) => people.find((p: { person_id: string }) => p.person_id === id);

test("Batch 423 publishes only John M Clark's identifier-backed occupation", async ({ page }) => {
  const p = profile("6648b6f7-0043-5018-98da-8d0087a41f69");
  expect(p).toMatchObject({
    display_name: "John M Clark",
    identity_status: "confirmed",
    personnel_category: "enlisted_army_personnel",
    commissioned_officer: false,
    research_status: "occupation_only_found",
  });
  expect(p.immediate_pre_oss_affiliations).toEqual([]);
  expect(p.last_civilian_pre_service).toEqual([]);
  expect(p.other_pre_oss_affiliations).toContainEqual(expect.objectContaining({
    occupation: "Policemen and detectives, public service",
    relationship_type: "unknown",
    temporal_basis: "temporal_relation_uncertain",
    claim_confidence: "medium",
    organization_id: null,
  }));

  await page.goto(`./people/${p.person_id}/`);
  await expect(page.getByRole("heading", { name: "John M Clark", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("thirty exact-name John M Clark records");
  await expect(page.locator("main")).toContainText("Policemen and detectives, public service");
  await expect(page.locator("main")).toContainText("No reliable pre-OSS employer");
  await expect(page.locator("main")).not.toContainText(/\b\d{8}\b/);
});

test("Batch 423 keeps John N Clark's indexed Major status separate from outside identities", async ({ page }) => {
  const p = profile("c5adb1fa-b411-50cc-bd88-c096fd60705e");
  expect(p).toMatchObject({
    display_name: "John N Clark",
    identity_status: "ambiguous",
    personnel_category: "commissioned_army_officer",
    commissioned_officer: true,
    research_status: "needs_identity_review",
  });
  expect(p.source_records[0]).toMatchObject({ rank_as_indexed: "Maj", box: "127", pdf_page: 82 });
  expect(p.claims).toEqual([]);
  expect(p.other_pre_oss_affiliations).toEqual([]);

  await page.goto(`./people/${p.person_id}/`);
  await expect(page.getByRole("heading", { name: "John N Clark", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("thirteen exact-name John N Clark Army rows");
  await expect(page.locator("main")).toContainText("Major");
  await expect(page.locator("main")).toContainText("No publishable pre-OSS affiliation is recorded yet");
});

test("Batch 423 leaves Hoyt, James, and Leonard Clark Army candidates unmerged", async ({ page }) => {
  for (const [id, name, expected] of [
    ["7931e78a-3718-5854-a528-9dbdb2190b9c", "Hoyt B Clark", "one exact-name Hoyt B Clark row"],
    ["0e0ce8ab-0ea3-567a-a265-c4693bde228d", "James E Clark", "111 exact-name James E Clark rows"],
    ["101632b5-950b-5e2f-8fa0-2ba405a797f6", "Leonard F Clark", "sole exact-name Leonard F Clark Army row"],
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
    await expect(page.locator("main")).toContainText(/Review Box 12[67]/);
    await expect(page.locator("main")).toContainText("No reviewed claim currently meets the publication threshold");
  }
});

test("Batch 423 gives four no-hit names complete archival-review profiles", async ({ page }) => {
  for (const [id, name, box, pdfPage] of [
    ["7245b71c-645e-578e-9180-9fa880db85a1", "Helen H Clark", "126", 82],
    ["01f8e373-a84a-5da9-9e06-6492b02f265c", "Janie K Clark", "126", 82],
    ["cee38083-52de-5ff3-9035-89079ef39004", "Julia A Clark", "127", 82],
    ["714f2320-668d-58f1-9367-8d129e00544f", "Percy E Clark", "127", 83],
  ]) {
    const idString = String(id);
    const nameString = String(name);
    const p = profile(idString);
    expect(p).toMatchObject({
      display_name: nameString,
      identity_status: "unresolved",
      personnel_category: "unknown_or_indeterminate",
      commissioned_officer: null,
      research_status: "requires_archival_review",
    });
    expect(p.claims).toEqual([]);
    expect(p.source_records[0]).toMatchObject({ pdf_page: pdfPage, box, rank_as_indexed: null });

    await page.goto(`./people/${idString}/`);
    await expect(page.getByRole("heading", { name: nameString, exact: true })).toBeVisible();
    await expect(page.locator("main")).toContainText(`Review Box ${box}`);
    await expect(page.locator("main")).toContainText("no exact-name Army row was found");
    await expect(page.locator("main")).toContainText("No reliable pre-OSS employer");
  }
});

test("Batch 423 rejects Leslie Clark's other-identifier Army namesakes", async ({ page }) => {
  const p = profile("5d2b8485-58df-5f8f-8649-553f1b4aa280");
  expect(p).toMatchObject({
    display_name: "Leslie A Clark",
    identity_status: "unresolved",
    personnel_category: "unknown_or_indeterminate",
    commissioned_officer: null,
    research_status: "requires_archival_review",
  });
  expect(p.claims).toEqual([]);
  expect(p.other_pre_oss_affiliations).toEqual([]);

  await page.goto(`./people/${p.person_id}/`);
  await expect(page.locator("main")).toContainText("Four exact-name Leslie A Clark Army rows carry other identifiers");
  await expect(page.locator("main")).toContainText("Review Box 127");
  await expect(page.locator("main")).not.toContainText(/\b\d{8}\b/);
});

test("Batch 423 preserves the page and location boundary", async ({ page }) => {
  const helen = profile("7245b71c-645e-578e-9180-9fa880db85a1");
  const percy = profile("714f2320-668d-58f1-9367-8d129e00544f");
  expect(helen.source_records[0]).toMatchObject({
    source_record_id: "786b6ee9-1512-5ad6-8256-fcd30da93c55",
    pdf_page: 82,
    box: "126",
    archive_location: "230/86/28/06",
  });
  expect(percy.source_records[0]).toMatchObject({
    source_record_id: "86c9cafe-0659-53b4-aea0-e90605e2296a",
    pdf_page: 83,
    box: "127",
    archive_location: "230/86/28/07",
  });

  await page.goto(`./people/${helen.person_id}/`);
  await expect(page.locator("main")).toContainText("230/86/28/06");
  await page.goto(`./people/${percy.person_id}/`);
  await expect(page.locator("main")).toContainText("230/86/28/07");
});

test("Batch 423 cohort is searchable by every exact indexed name", async ({ page }) => {
  for (const name of [
    "Helen H Clark",
    "Hoyt B Clark",
    "James E Clark",
    "Janie K Clark",
    "John M Clark",
    "John N Clark",
    "Julia A Clark",
    "Leonard F Clark",
    "Leslie A Clark",
    "Percy E Clark",
  ]) {
    await page.goto(`./people/?q=${encodeURIComponent(name)}`);
    await expect(page.getByRole("link", { name, exact: true })).toBeVisible();
  }
});
