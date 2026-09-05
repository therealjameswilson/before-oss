import { expect, test } from "@playwright/test";
import fs from "node:fs";

const people = JSON.parse(fs.readFileSync(new URL("../src/data/generated/people.json", import.meta.url), "utf8"));
const profile = (id: string) => people.find((p: { person_id: string }) => p.person_id === id);

test("Batch 421 publishes only identifier-backed occupation evidence for Creston Clark", async ({ page }) => {
  const p = profile("c220073a-8a31-5885-9159-2ddfa138718d");
  expect(p).toMatchObject({
    display_name: "Creston P Clark",
    identity_status: "confirmed",
    personnel_category: "enlisted_army_personnel",
    commissioned_officer: false,
    research_status: "occupation_only_found",
  });
  expect(p.source_records[0]).toMatchObject({ pdf_page: 82, box: "126", serial_masked: "••••9744" });
  expect(p.immediate_pre_oss_affiliations).toEqual([]);
  expect(p.last_civilian_pre_service).toEqual([]);
  expect(p.other_pre_oss_affiliations).toContainEqual(expect.objectContaining({
    occupation: "Accountants and auditors",
    relationship_type: "unknown",
    temporal_basis: "temporal_relation_uncertain",
    claim_confidence: "medium",
    organization_id: null,
  }));

  await page.goto(`./people/${p.person_id}/`);
  await expect(page.getByRole("heading", { name: "Creston P Clark", exact: true })).toBeVisible();
  await expect(page.locator('section[aria-labelledby="earlier-affiliations"]')).toContainText("Accountants and auditors");
  await expect(page.locator('section[aria-labelledby="civilian-employer"]')).toContainText(/No (?:reviewed claim|reliable pre-OSS employer)/);
  await expect(page.locator("main")).toContainText("15 December 1944");
});

test("Batch 421 keeps Calvin Clark's identifier conflict visible without candidate transfer", async ({ page }) => {
  const p = profile("fe57eba0-5439-5a46-b6b6-4c5bdf7943e4");
  expect(p).toMatchObject({
    display_name: "Calvin L Clark",
    identity_status: "conflicting",
    personnel_category: "unknown_or_indeterminate",
    commissioned_officer: null,
    research_status: "conflicting_sources",
  });
  expect(p.immediate_pre_oss_affiliations).toEqual([]);
  expect(p.last_civilian_pre_service).toEqual([]);
  expect(p.other_pre_oss_affiliations).toEqual([]);
  expect(p.claims).toHaveLength(1);
  expect(p.claims[0]).toMatchObject({ claim_type: "identity", claim_confidence: "conflicting", publication_status: "conflicting" });

  await page.goto(`./people/${p.person_id}/`);
  await expect(page.getByRole("heading", { name: "Calvin L Clark", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("different private identifier");
  await expect(page.locator("main")).toContainText("records remain unmerged");
  await expect(page.locator("main")).not.toContainText(/\b\d{8}\b/);
  await expect(page.locator("main")).toContainText("No publishable pre-OSS affiliation is recorded yet");
});

test("Batch 421 leaves sole name-only Army candidates unmerged", async ({ page }) => {
  for (const [id, name] of [
    ["3700b8b4-3bdb-5881-a320-08969e8b9f9a", "Andrew H Clark"],
    ["3652949d-ece6-5814-a995-93e6badc6287", "Clayton E Clark"],
    ["930b3378-060d-5eda-a782-6591284d6486", "Douglas M Clark"],
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
    await expect(page.locator("main")).toContainText("one exact-name");
    await expect(page.locator("main")).toContainText("Review Box 126");
    await expect(page.locator("main")).toContainText("No publishable pre-OSS affiliation is recorded yet");
  }
});

test("Batch 421 does not transfer Dorothy Clark's name-only WAC candidate", async ({ page }) => {
  const p = profile("d9a433cc-e540-5b78-a530-2bf103bcfc1e");
  expect(p).toMatchObject({
    display_name: "Dorothy P Clark",
    identity_status: "ambiguous",
    personnel_category: "unknown_or_indeterminate",
    commissioned_officer: null,
    research_status: "needs_identity_review",
  });
  expect(p.claims).toEqual([]);
  expect(p.immediate_pre_oss_affiliations).toEqual([]);
  expect(p.last_civilian_pre_service).toEqual([]);
  expect(p.other_pre_oss_affiliations).toEqual([]);

  await page.goto(`./people/${p.person_id}/`);
  await expect(page.getByRole("heading", { name: "Dorothy P Clark", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("WAC row");
  await expect(page.locator("main")).toContainText("candidate is not merged from name alone");
  await expect(page.locator("main")).toContainText("No publishable pre-OSS affiliation is recorded yet");
});

test("Batch 421 keeps all six Clyde Clark candidates separate", async ({ page }) => {
  const p = profile("bfa217f3-34f7-5afe-8d17-32c3d26539a5");
  expect(p).toMatchObject({
    display_name: "Clyde Clark",
    identity_status: "ambiguous",
    personnel_category: "unknown_or_indeterminate",
    commissioned_officer: null,
    research_status: "needs_identity_review",
  });
  expect(p.claims).toEqual([]);
  expect(p.other_pre_oss_affiliations).toEqual([]);

  await page.goto(`./people/${p.person_id}/`);
  await expect(page.locator("main")).toContainText("Six exact-name Clyde Clark rows");
  await expect(page.locator("main")).toContainText("at least two corroborating identifiers");
  await expect(page.locator("main")).toContainText("Box 126");
});

test("Batch 421 withholds the unconfirmed Eleanor Clark writer candidate", async ({ page }) => {
  const p = profile("b02f11d5-469a-5b25-9f8a-a1de271a54b2");
  expect(p).toMatchObject({
    display_name: "Eleanor Clark",
    identity_status: "unresolved",
    personnel_category: "unknown_or_indeterminate",
    commissioned_officer: null,
    research_status: "candidate_found",
  });
  expect(p.claims).toEqual([]);
  expect(p.immediate_pre_oss_affiliations).toEqual([]);
  expect(p.last_civilian_pre_service).toEqual([]);
  expect(p.other_pre_oss_affiliations).toEqual([]);

  await page.goto(`./people/${p.person_id}/`);
  await expect(page.getByRole("heading", { name: "Eleanor Clark", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("Research is in progress");
  await expect(page.locator("main")).toContainText("Discovery candidates are not presented as established facts");
  await expect(page.locator("main")).toContainText("No publishable pre-OSS affiliation is recorded yet");
});

test("Batch 421 gives Anna and Cecelia Clark complete unresolved archival profiles", async ({ page }) => {
  for (const [id, name] of [
    ["dcd4e73c-7405-56b6-ab1c-6296b1a44f49", "Anna H Clark"],
    ["4d7f8ed1-3b83-5b31-932e-dffc8a15e355", "Cecelia Clark"],
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

test("Batch 421 cohort is searchable by exact indexed name", async ({ page }) => {
  for (const name of [
    "Andrew H Clark",
    "Anna H Clark",
    "Calvin L Clark",
    "Cecelia Clark",
    "Clayton E Clark",
    "Clyde Clark",
    "Creston P Clark",
    "Dorothy P Clark",
    "Douglas M Clark",
    "Eleanor Clark",
  ]) {
    await page.goto(`./people/?q=${encodeURIComponent(name)}`);
    await expect(page.getByRole("link", { name, exact: true })).toBeVisible();
  }
});
