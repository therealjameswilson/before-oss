import { expect, test } from "@playwright/test";
import fs from "node:fs";

const people = JSON.parse(fs.readFileSync(new URL("../src/data/generated/people.json", import.meta.url), "utf8"));
const profile = (id: string) => people.find((p: { person_id: string }) => p.person_id === id);

test("Batch 418 publishes four bounded occupations without inventing employers", async ({ page }) => {
  for (const [id, name, category, officer, occupation, date, serial] of [
    ["75752b0f-b19b-5d16-825a-8654383b0771", "Henry F Ciezak", "commissioned_army_officer", true, "Mechanics and repairmen, motor vehicle", "17 December 1941", "••••4667"],
    ["918cb60a-78c6-5b24-bec4-c4f93ff58228", "Jouis C Ciminera", "enlisted_army_personnel", false, "Shipping and receiving clerks", "21 September 1942", "••••0808"],
    ["17d18f0f-77c9-53ff-87fc-b1bd627e8ea6", "Chester Cimochowski", "enlisted_army_personnel", false, "Filers, grinders, buffers, and polishers (metal)", "11 July 1942", "••••1430"],
    ["cd5bb943-df3d-557a-98b3-7e303bc8af42", "Walter T Cini", "enlisted_army_personnel", false, "Public officials, n.e.c.", "22 June 1942", "••••8032"],
  ] as const) {
    const p = profile(id);
    expect(p.identity_status).toBe("high_confidence");
    expect(p.personnel_category).toBe(category);
    expect(p.commissioned_officer).toBe(officer);
    expect(p.research_status).toBe("occupation_only_found");
    expect(p.source_records[0]).toMatchObject({ pdf_page: 81, box: "125", serial_masked: serial });
    expect(p.immediate_pre_oss_affiliations).toEqual([]);
    expect(p.last_civilian_pre_service).toEqual([]);
    expect(p.other_pre_oss_affiliations).toHaveLength(1);
    expect(p.other_pre_oss_affiliations[0]).toMatchObject({
      occupation,
      organization_id: null,
      relationship_type: "unknown",
      temporal_basis: "temporal_relation_uncertain",
      claim_confidence: "medium",
    });
    expect(p.other_pre_oss_affiliations[0].date_precision).toContain(date);

    await page.goto(`./people/${id}/`);
    await expect(page.getByRole("heading", { name, exact: true })).toBeVisible();
    await expect(page.locator('section[aria-labelledby="earlier-affiliations"]')).toContainText(occupation);
    await expect(page.locator('section[aria-labelledby="civilian-employer"]')).toContainText("No reliable pre-OSS employer");
    await expect(page.locator("main")).toContainText("NARA Compiled Code Lists");
  }
});

test("Batch 418 publishes Ralph Ciluzzi's explicit Marine Corps Reserve pathway", async ({ page }) => {
  const p = profile("5d8b3ae5-ea98-51eb-b4e0-fce85c3c0564");
  expect(p).toMatchObject({
    display_name: "Ralph J Ciluzzi",
    identity_status: "high_confidence",
    personnel_category: "enlisted_marine_corps_personnel",
    commissioned_officer: false,
    research_status: "completed",
  });
  expect(p.source_records[0]).toMatchObject({ pdf_page: 81, box: "125", serial_masked: null });
  expect(p.immediate_pre_oss_affiliations).toHaveLength(1);
  expect(p.immediate_pre_oss_affiliations[0]).toMatchObject({
    canonical_organization: "United States Marine Corps Reserve",
    organization_name_as_found: "U.S.M.C.R.",
    role_title: "Sergeant",
    relationship_type: "military_assignment",
    temporal_basis: "explicit_immediate",
    claim_confidence: "high",
  });
  expect(p.last_civilian_pre_service).toEqual([]);

  await page.goto(`./people/${p.person_id}/`);
  await expect(page.getByRole("heading", { name: "Ralph J Ciluzzi", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("United States Marine Corps Reserve");
  await expect(page.locator("main")).toContainText("assigned to OSS in July 1943");
  await expect(page.locator("main")).toContainText("Hoover ID 69085.147");
  await expect(page.locator('section[aria-labelledby="civilian-employer"]')).toContainText("No reliable pre-OSS employer");
});

test("Batch 418 preserves Jouis Ciminera's indexed spelling and searches the documented Louis variant", async ({ page }) => {
  const p = profile("918cb60a-78c6-5b24-bec4-c4f93ff58228");
  expect(p.display_name).toBe("Jouis C Ciminera");
  expect(p.name_variants).toContain("Louis C Ciminera");
  expect(p.name_variants).toContain("Louis C. Ciminera");
  expect(p.source_records[0].indexed_first_name).toBe("Jouis");
  expect(p.source_records[0].serial_masked).toBe("••••0808");

  await page.goto(`./people/${p.person_id}/`);
  await expect(page.getByRole("heading", { name: "Jouis C Ciminera", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("Louis C Ciminera");
  await expect(page.locator("main")).toContainText("preserving Jouis as the indexed spelling");
  await expect(page.locator("main")).not.toContainText(/\b\d{8}\b/);

  await page.goto(`./people/?q=${encodeURIComponent("Louis C Ciminera")}`);
  await expect(page.getByRole("link", { name: "Jouis C Ciminera", exact: true })).toBeVisible();
});

test("Batch 418 keeps identity-only evidence bounded for Joseph Ciezadlo", async ({ page }) => {
  const p = profile("4e2f6904-e573-5b58-a9fa-856bfb3db131");
  expect(p).toMatchObject({
    display_name: "Joseph V Ciezadlo",
    identity_status: "high_confidence",
    personnel_category: "enlisted_army_personnel",
    commissioned_officer: false,
    research_status: "requires_archival_review",
  });
  expect(p.source_records[0]).toMatchObject({ serial_masked: "••••1846", pdf_page: 81, box: "125" });
  expect(p.immediate_pre_oss_affiliations).toEqual([]);
  expect(p.last_civilian_pre_service).toEqual([]);
  expect(p.other_pre_oss_affiliations).toEqual([]);
  expect(p.claims.map((claim: { claim_type: string }) => claim.claim_type)).toEqual(["identity"]);

  await page.goto(`./people/${p.person_id}/`);
  await expect(page.getByRole("heading", { name: "Joseph V Ciezadlo", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("enlisted men's recommendations approved");
  await expect(page.locator("main")).toContainText("Detachment 101");
  await expect(page.locator('section[aria-labelledby="civilian-employer"]')).toContainText("No reliable pre-OSS employer");
});

test("Batch 418 withholds unbridged Army candidates for Joseph Cilcius and Michael Cimino", async ({ page }) => {
  const joseph = profile("7ca8b995-9892-5291-a0ae-76a47d761141");
  expect(joseph).toMatchObject({
    display_name: "Joseph Cilcius",
    identity_status: "unresolved",
    personnel_category: "unknown_or_indeterminate",
    commissioned_officer: null,
    research_status: "candidate_found",
  });
  expect(joseph.claims).toEqual([]);
  expect(joseph.other_pre_oss_affiliations).toEqual([]);
  expect(joseph.identity_evidence).toContain("no private identifier");

  const michael = profile("2e91eab8-03cb-5c5b-8fec-364de6af64cd");
  expect(michael).toMatchObject({
    display_name: "Michael Cimino",
    identity_status: "ambiguous",
    personnel_category: "unknown_or_indeterminate",
    commissioned_officer: null,
    research_status: "needs_identity_review",
  });
  expect(michael.claims).toEqual([]);
  expect(michael.other_pre_oss_affiliations).toEqual([]);
  expect(michael.identity_evidence).toContain("Four Army rows expand the common name Michael Cimino");

  for (const [id, name] of [[joseph.person_id, joseph.display_name], [michael.person_id, michael.display_name]]) {
    await page.goto(`./people/${id}/`);
    await expect(page.getByRole("heading", { name, exact: true })).toBeVisible();
    await expect(page.locator("main")).toContainText("No publishable pre-OSS affiliation is recorded yet");
    await expect(page.locator('section[aria-labelledby="civilian-employer"]')).toContainText("No reviewed claim currently meets the publication threshold");
  }
});

test("Batch 418 gives unresolved Angel Cinza and Alfred Ciocca complete archival-review profiles", async ({ page }) => {
  for (const [id, name] of [
    ["5d29ee1e-d441-51e1-a8fd-13a0bee080c6", "Angel L Cinza"],
    ["dee82392-d2c7-5713-aaa9-fca62c2d1968", "Alfred H Ciocca"],
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
    expect(p.immediate_pre_oss_affiliations).toEqual([]);
    expect(p.last_civilian_pre_service).toEqual([]);
    expect(p.other_pre_oss_affiliations).toEqual([]);

    await page.goto(`./people/${id}/`);
    await expect(page.getByRole("heading", { name, exact: true })).toBeVisible();
    await expect(page.locator("main")).toContainText("requires archival review");
    await expect(page.locator("main")).toContainText("Box 125");
    await expect(page.locator("main")).toContainText("230/86/28/06");
    await expect(page.locator("main")).toContainText("No reliable pre-OSS employer");
  }
});

test("Batch 418 cohort is searchable by exact indexed name", async ({ page }) => {
  for (const name of [
    "Joseph V Ciezadlo",
    "Henry F Ciezak",
    "Joseph Cilcius",
    "Ralph J Ciluzzi",
    "Jouis C Ciminera",
    "Michael Cimino",
    "Chester Cimochowski",
    "Walter T Cini",
    "Angel L Cinza",
    "Alfred H Ciocca",
  ]) {
    await page.goto(`./people/?q=${encodeURIComponent(name)}`);
    await expect(page.getByRole("link", { name, exact: true })).toBeVisible();
  }
});
