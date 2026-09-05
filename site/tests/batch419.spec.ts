import { expect, test } from "@playwright/test";
import fs from "node:fs";

const people = JSON.parse(fs.readFileSync(new URL("../src/data/generated/people.json", import.meta.url), "utf8"));
const profile = (id: string) => people.find((p: { person_id: string }) => p.person_id === id);

test("Batch 419 separates Caesar Civitella's Ford employment, Army pathway, and student affiliations", async ({ page }) => {
  const p = profile("96b61c3a-31ab-5107-84b4-92e1dc3feed0");
  expect(p).toMatchObject({
    display_name: "Caesar J Civitella",
    identity_status: "confirmed",
    personnel_category: "enlisted_army_personnel",
    commissioned_officer: false,
    research_status: "verified_employer_found",
  });
  expect(p.source_records[0]).toMatchObject({ pdf_page: 82, box: "125", serial_masked: "••••5424" });
  expect(p.immediate_pre_oss_affiliations).toHaveLength(1);
  expect(p.immediate_pre_oss_affiliations[0]).toMatchObject({
    canonical_organization: "United States Army",
    organization_name_as_found: "Army",
    relationship_type: "military_assignment",
    temporal_basis: "explicit_immediate",
    claim_confidence: "high",
  });
  expect(p.last_civilian_pre_service).toHaveLength(1);
  expect(p.last_civilian_pre_service[0]).toMatchObject({
    canonical_organization: "Ford Motor Company",
    organization_name_as_found: "Ford Motor Company",
    relationship_type: "employment",
    temporal_basis: "strongly_date_bounded",
    claim_confidence: "high",
    city: "Chester",
    state_or_region: "Pennsylvania",
  });
  const studentOrganizations = p.other_pre_oss_affiliations
    .filter((a: { relationship_type: string }) => a.relationship_type === "student")
    .map((a: { canonical_organization: string }) => a.canonical_organization)
    .sort();
  expect(studentOrganizations).toEqual(["Girard College", "Pennsylvania Maritime Academy"]);
  expect(p.other_pre_oss_affiliations).toContainEqual(expect.objectContaining({
    occupation: "Occupations in production of ferrous and nonferrous metals, n.e.c.",
    organization_id: null,
    temporal_basis: "temporal_relation_uncertain",
  }));

  await page.goto(`./people/${p.person_id}/`);
  await expect(page.getByRole("heading", { name: "Caesar J Civitella", exact: true })).toBeVisible();
  await expect(page.locator('section[aria-labelledby="immediate-affiliation"]')).toContainText("United States Army");
  await expect(page.locator('section[aria-labelledby="civilian-employer"]')).toContainText("Ford Motor Company");
  await expect(page.locator("main")).toContainText("Pennsylvania Maritime Academy");
  await expect(page.locator("main")).toContainText("Student");
  await expect(page.locator("main")).toContainText("United States Special Operations Command");
});

test("Batch 419 publishes only bounded occupation and military evidence for Joseph Ciras and George Clainos", async ({ page }) => {
  for (const [id, name, occupation, status, serial] of [
    ["e5baed2f-98a3-5cfa-8d36-143396fa333e", "Joseph C Ciras", "Structural and ornamental metal workers", "occupation_only_found", "••••6933"],
    ["40c32ac0-70d3-58f4-a60c-496c981e024f", "George V Clainos", "Waiters and waitresses, except private family", "needs_temporal_review", "••••7859"],
  ] as const) {
    const p = profile(id);
    expect(p.identity_status).toBe("confirmed");
    expect(p.personnel_category).toBe("enlisted_army_personnel");
    expect(p.commissioned_officer).toBe(false);
    expect(p.research_status).toBe(status);
    expect(p.source_records[0]).toMatchObject({ box: "125", serial_masked: serial });
    expect(p.immediate_pre_oss_affiliations).toEqual([]);
    expect(p.last_civilian_pre_service).toEqual([]);
    expect(p.other_pre_oss_affiliations).toContainEqual(expect.objectContaining({
      occupation,
      relationship_type: "unknown",
      temporal_basis: "temporal_relation_uncertain",
      claim_confidence: "medium",
      organization_id: null,
    }));

    await page.goto(`./people/${id}/`);
    await expect(page.getByRole("heading", { name, exact: true })).toBeVisible();
    await expect(page.locator('section[aria-labelledby="earlier-affiliations"]')).toContainText(occupation);
    await expect(page.locator('section[aria-labelledby="civilian-employer"]')).toContainText(/No (?:reviewed claim|reliable pre-OSS employer)/);
  }

  const george = profile("40c32ac0-70d3-58f4-a60c-496c981e024f");
  expect(george.other_pre_oss_affiliations).toContainEqual(expect.objectContaining({
    canonical_organization: "86th Infantry Regiment, United States Army",
    organization_name_as_found: "86TH INF",
    role_title: "Sergeant, Company A",
    relationship_type: "military_assignment",
    temporal_basis: "temporal_relation_uncertain",
  }));
});

test("Batch 419 keeps Nicholas Clainos's identifier conflict visible without merging the candidate", async ({ page }) => {
  const p = profile("619819c4-eb03-56a6-b255-41ce561d30a2");
  expect(p).toMatchObject({
    display_name: "Nicholas D Clainos",
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
  await expect(page.getByRole("heading", { name: "Nicholas D Clainos", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("different officer identifier");
  await expect(page.locator("main")).toContainText("records remain unmerged");
  await expect(page.locator("main")).not.toContainText(/\b\d{8}\b/);
});

test("Batch 419 publishes Peter Clainos as a commissioned Army officer while preserving OSS uncertainty", async ({ page }) => {
  const p = profile("812d7351-e167-568d-bc4d-d0ba2eecb2b3");
  expect(p).toMatchObject({
    display_name: "Peter D Clainos",
    identity_status: "high_confidence",
    personnel_category: "commissioned_army_officer",
    commissioned_officer: true,
    research_status: "needs_temporal_review",
  });
  expect(p.name_variants).toContain("Peter Demosthenes Clainos");
  expect(p.immediate_pre_oss_affiliations).toEqual([]);
  expect(p.last_civilian_pre_service).toEqual([]);
  expect(p.other_pre_oss_affiliations).toHaveLength(1);
  expect(p.other_pre_oss_affiliations[0]).toMatchObject({
    organization_name_as_found: "128 Infantry Greek battalion",
    role_title: "Major; commanding officer",
    relationship_type: "military_assignment",
    temporal_basis: "temporal_relation_uncertain",
    claim_confidence: "high",
  });

  await page.goto(`./people/${p.person_id}/`);
  await expect(page.getByRole("heading", { name: "Peter D Clainos", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("Peter Demosthenes Clainos");
  await expect(page.locator("main")).toContainText("128 Infantry Greek battalion");
  await expect(page.locator("main")).toContainText("whether he entered OSS or only supported its recruitment");
  await expect(page.locator("main")).toContainText("does not establish how it relates to the indexed OSS file");
  await expect(page.locator("main")).toContainText("Library of Congress");
});

test("Batch 419 withholds low-confidence Paul Cirillo and Iganazio Ciuppa candidates", async ({ page }) => {
  for (const [id, name, status] of [
    ["debd486f-0958-5784-bb61-f73ff6433de3", "Paul F Cirillo", "candidate_found"],
    ["358a48b3-af19-583d-8faf-e21a602f587c", "Iganazio Ciuppa", "needs_identity_review"],
  ] as const) {
    const p = profile(id);
    expect(p).toMatchObject({
      display_name: name,
      identity_status: "unresolved",
      personnel_category: "unknown_or_indeterminate",
      commissioned_officer: null,
      research_status: status,
    });
    expect(p.claims).toEqual([]);
    expect(p.immediate_pre_oss_affiliations).toEqual([]);
    expect(p.last_civilian_pre_service).toEqual([]);
    expect(p.other_pre_oss_affiliations).toEqual([]);

    await page.goto(`./people/${id}/`);
    await expect(page.getByRole("heading", { name, exact: true })).toBeVisible();
    await expect(page.locator("main")).toContainText("No publishable pre-OSS affiliation is recorded yet");
    await expect(page.locator('section[aria-labelledby="civilian-employer"]')).toContainText("No reviewed claim currently meets the publication threshold");
    await expect(page.locator("main")).not.toContainText("Garfield Police Department");
  }
});

test("Batch 419 preserves Stephan Claessens's incomplete source note without expansion", async ({ page }) => {
  const p = profile("04aa82a0-b97f-50ec-88f9-7eb237224d13");
  expect(p).toMatchObject({
    display_name: "Stephan M Claessens",
    identity_status: "unresolved",
    personnel_category: "foreign_or_allied_military_personnel",
    commissioned_officer: null,
    research_status: "requires_archival_review",
  });
  expect(p.source_records[0]).toMatchObject({ pdf_page: 82, box: "125", rank_as_indexed: "Sgt", notes_as_indexed: "Dutch Ar" });
  expect(p.claims).toEqual([]);

  await page.goto(`./people/${p.person_id}/`);
  await expect(page.getByRole("heading", { name: "Stephan M Claessens", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("Dutch Ar");
  await expect(page.locator("main")).toContainText("preserve the note verbatim");
  await expect(page.locator("main")).toContainText("No reliable pre-OSS employer");
});

test("Batch 419 gives unresolved John Cizauskas and Helen Clabby complete archival-review profiles", async ({ page }) => {
  for (const [id, name] of [
    ["022c8896-4e33-56ed-967c-71be8bee3e07", "John J Cizauskas Jr."],
    ["27b0ec9e-9959-5d14-8112-75d174aa5b02", "Helen V Clabby"],
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

    await page.goto(`./people/${id}/`);
    await expect(page.getByRole("heading", { name, exact: true })).toBeVisible();
    await expect(page.locator("main")).toContainText("requires archival review");
    await expect(page.locator("main")).toContainText("Box 125");
    await expect(page.locator("main")).toContainText("230/86/28/06");
  }
});

test("Batch 419 cohort is searchable by exact indexed name", async ({ page }) => {
  for (const name of [
    "Joseph C Ciras",
    "Paul F Cirillo",
    "Iganazio Ciuppa",
    "Caesar J Civitella",
    "John J Cizauskas Jr.",
    "Helen V Clabby",
    "Stephan M Claessens",
    "George V Clainos",
    "Nicholas D Clainos",
    "Peter D Clainos",
  ]) {
    await page.goto(`./people/?q=${encodeURIComponent(name)}`);
    await expect(page.getByRole("link", { name, exact: true })).toBeVisible();
  }
});
