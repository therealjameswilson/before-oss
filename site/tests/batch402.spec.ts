import { expect, test } from "@playwright/test";
import fs from "node:fs";

const people = JSON.parse(fs.readFileSync(new URL("../src/data/generated/people.json", import.meta.url), "utf8"));
const profile = (id: string) => people.find((person: { person_id: string }) => person.person_id === id);
const unresolved = [
  ["83fbb728-78d5-5937-8bff-05a2e9d52d71", "Catherine L Chaudet"],
  ["f0f65160-fc7a-5a54-a723-7aea9ae853a1", "Aaron H Chayes"],
  ["a93259a6-252b-5580-b01d-d84a5f4a43c1", "Louis C Cheatham"],
  ["ba6b4769-c7f1-5ad4-a540-1186602077e8", "Walter W Chechot"],
  ["adccb97e-8d3e-5f93-a783-f4f200f35e8a", "Abraham Checkoway"],
];

test("Batch 402 keeps uncorroborated identities public without namesake employment", async ({ page }) => {
  for (const [id, name] of unresolved) {
    const p = profile(id);
    expect(p.identity_status).toBe("unresolved");
    expect(p.claims).toEqual([]);
    expect(p.research_status).toBe("requires_archival_review");
    expect(p.research_attempt_count).toBeGreaterThan(0);
    expect(p.source_records[0]).toMatchObject({ pdf_page: 78, box: "120", archive_location: "230/86/28/06" });
    await page.goto(`./people/${id}/`);
    await expect(page.getByRole("heading", { name, exact: true })).toBeVisible();
    await expect(page.locator("main")).toContainText("No reliable pre-OSS employer has yet been identified in the accessible sources reviewed.");
    await expect(page.locator('section[aria-labelledby="earlier-affiliations"] .affiliation-card')).toHaveCount(0);
  }
});

test("Batch 402 Army identifiers resolve identity without decoding missing occupation codes or projecting postwar grades", async ({ page }) => {
  for (const id of ["ab682014-4481-5aeb-82da-5f97fe88b403", "5ed618ea-3fd5-59e9-ae65-19e324758389", "d183b618-59e9-5a78-a55c-e4ff5292df3f"]) {
    const p = profile(id);
    expect(p.identity_status).toBe("high_confidence");
    expect(p.commissioned_officer).toBeNull();
    expect(p.source_records[0].rank_as_indexed).toBeNull();
    expect(p.immediate_pre_oss_affiliations).toEqual([]);
    expect(p.last_civilian_pre_service).toEqual([]);
    expect(p.other_pre_oss_affiliations).toEqual([]);
    expect(p.claims).toHaveLength(1);
    expect(p.claims[0].claim_type).toBe("identity");
    expect(p.claims[0].sources.length).toBeGreaterThan(0);
    await page.goto(`./people/${id}/`);
    await expect(page.locator("main")).toContainText("Box 120");
    await expect(page.locator('section[aria-labelledby="earlier-affiliations"] .affiliation-card')).toHaveCount(0);
  }
  expect(profile("ab682014-4481-5aeb-82da-5f97fe88b403").claims[0].temporal_assessment).toContain("1946");
  expect(profile("d183b618-59e9-5a78-a55c-e4ff5292df3f").name_variants).toContain("Lloyd J. Cheek");
});

test("Batch 402 separates Cheek's museum employment from Army-school work and preserves both printed suffixes", async ({ page }) => {
  const id = "46cc3ed9-c738-5649-93c1-48994390bd94";
  const p = profile(id);
  expect(p.display_name).toBe("Leslie Cheek Jr.");
  expect(p.name_variants).toContain("Leslie, Jr. Cheek Jr.");
  expect(p.source_records[0]).toMatchObject({ indexed_last_name: "Cheek, Jr.", indexed_first_name: "Leslie, Jr.", rank_as_indexed: null });
  expect(p.commissioned_officer).toBeNull();
  expect(p.immediate_pre_oss_affiliations).toEqual([]);
  expect(p.last_civilian_pre_service).toHaveLength(1);
  expect(p.last_civilian_pre_service[0]).toMatchObject({ canonical_organization: "Baltimore Museum of Art", relationship_type: "employment", start_date: "1939-09-01", end_date: "1942", immediate_pre_oss: false });
  expect(p.other_pre_oss_affiliations.map((a: { relationship_type: string }) => a.relationship_type).sort()).toEqual(["employment", "government_assignment"]);
  for (const claim of p.claims) expect(claim.sources.length).toBeGreaterThan(0);
  await page.goto(`./people/${id}/`);
  await expect(page.getByRole("heading", { name: "Leslie Cheek Jr.", exact: true })).toBeVisible();
  await expect(page.locator('section[aria-labelledby="civilian-employer"]')).toContainText("Baltimore Museum of Art");
  await expect(page.locator('section[aria-labelledby="civilian-employer"]')).toContainText("End in spring 1942; no exact day established.");
  await expect(page.locator('section[aria-labelledby="civilian-employer"] .badge')).toContainText(["high", "documented pre-OSS"]);
  const museum = p.last_civilian_pre_service[0].organization_id;
  await page.goto(`./organizations/${museum}/`);
  await expect(page.getByRole("heading", { name: "Baltimore Museum of Art", exact: true })).toBeVisible();
  await expect(page.getByRole("link", { name: "Leslie Cheek Jr.", exact: true })).toBeVisible();
  await page.goto("./people/");
  await page.getByRole("searchbox", { name: "Search", exact: true }).fill("Leslie Cheek Jr");
  await expect(page.getByRole("link", { name: "Leslie Cheek Jr.", exact: true })).toBeVisible();
});

test("Batch 402 dates Cheever's intermittent command without inventing an OSS transfer or civilian employer", async ({ page }) => {
  const id = "eaf8432d-7c3b-5e66-b131-2c2c0c7d9f7f";
  const p = profile(id);
  expect(p.commissioned_officer).toBe(true);
  expect(p.personnel_category).toBe("commissioned_marine_corps_officer");
  expect(p.source_records[0].rank_as_indexed).toBeNull();
  expect(p.last_civilian_pre_service).toEqual([]);
  expect(p.immediate_pre_oss_affiliations).toEqual([]);
  expect(p.other_pre_oss_affiliations).toHaveLength(1);
  expect(p.other_pre_oss_affiliations[0]).toMatchObject({ relationship_type: "military_assignment", temporal_basis: "temporal_relation_uncertain", claim_confidence: "medium", immediate_pre_oss: false });
  expect(p.other_pre_oss_affiliations[0].date_precision).toContain("not continuous");
  await page.goto(`./people/${id}/`);
  await expect(page.getByRole("heading", { name: "Bruce B Cheever", exact: true })).toBeVisible();
  await expect(page.locator('section[aria-labelledby="earlier-affiliations"] .affiliation-card')).toContainText("Intermittent commanding officer");
  await expect(page.locator("main")).toContainText("timing relative to the beginning of his OSS service remains uncertain");
});
