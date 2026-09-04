import { expect, test } from "@playwright/test";
import fs from "node:fs";

const people = JSON.parse(fs.readFileSync(new URL("../src/data/generated/people.json", import.meta.url), "utf8"));
const profile = (id: string) => people.find((p: { person_id: string }) => p.person_id === id);
const charles = "ec8bf7e8-3975-57c4-b303-8fedc319fac3";
const john = "4511e9ad-538a-5352-9f17-0a4df04b2c5e";

test("Batch 405 separates Cheston's banking affiliation from the civilian Army Specialist Corps", async ({ page }) => {
  const p = profile(charles);
  expect(p.identity_status).toBe("high_confidence");
  expect(p.commissioned_officer).toBeNull();
  expect(p.personnel_category).toBe("unknown_or_indeterminate");
  expect(p.source_records[0]).toMatchObject({ pdf_page: 78, box: "121", rank_as_indexed: null });
  expect(p.name_variants).toContain("Charles Steele Cheston");
  expect(p.research_status).toBe("documented_prewar_employer_found");
  expect(p.immediate_pre_oss_affiliations).toEqual([]);
  expect(p.last_civilian_pre_service).toEqual([]);
  expect(p.other_pre_oss_affiliations).toHaveLength(2);
  const bank = p.other_pre_oss_affiliations.find((a: { relationship_type: string }) => a.relationship_type === "employment");
  const government = p.other_pre_oss_affiliations.find((a: { relationship_type: string }) => a.relationship_type === "government_assignment");
  for (const a of [bank, government]) {
    expect(a).toMatchObject({ start_date: null, end_date: null, city: null, country: null, immediate_pre_oss: false, last_civilian_pre_service: false, claim_confidence: "high" });
  }
  expect(bank.organization_name_as_found).toBe("Smith, Barney & Co.");
  expect(bank.date_precision).toContain("1942-07-23");
  expect(government.organization_name_as_found).toBe("Army Specialist Corps");
  expect(government.date_precision).toContain("1942-06-11");
  expect(p.claims).toHaveLength(3);
  for (const c of p.claims) expect(c.sources.length).toBeGreaterThanOrEqual(3);
  await page.goto(`./people/${charles}/`);
  await expect(page.getByRole("heading", { name: "Charles S Cheston", exact: true })).toBeVisible();
  const earlier = page.locator('section[aria-labelledby="earlier-affiliations"]');
  await expect(earlier).toContainText("Smith, Barney & Co.");
  await expect(earlier).toContainText("Army Specialist Corps");
  await expect(earlier).toContainText("1942-06-11");
  await expect(page.locator("main")).toContainText("civilian");
});

test("Batch 405 publishes only the bounded Chevalier occupation observation", async ({ page }) => {
  const p = profile(john);
  expect(p.identity_status).toBe("high_confidence");
  expect(p.commissioned_officer).toBeNull();
  expect(p.source_records[0]).toMatchObject({ pdf_page: 79, box: "121", rank_as_indexed: null });
  expect(p.immediate_pre_oss_affiliations).toEqual([]);
  expect(p.last_civilian_pre_service).toEqual([]);
  expect(p.other_pre_oss_affiliations).toHaveLength(1);
  expect(p.other_pre_oss_affiliations[0]).toMatchObject({ occupation: "Managers and officials, n. e. c.", organization_id: null, relationship_type: "unknown", start_date: null, end_date: null, country: null, claim_confidence: "medium", temporal_basis: "temporal_relation_uncertain" });
  expect(p.other_pre_oss_affiliations[0].date_precision).toContain("1942-06-30");
  await page.goto(`./people/${john}/`);
  await expect(page.getByRole("heading", { name: "John H Chevalier", exact: true })).toBeVisible();
  await expect(page.locator('section[aria-labelledby="civilian-employer"]')).toContainText("No reliable pre-OSS employer");
  await expect(page.locator('section[aria-labelledby="earlier-affiliations"]')).toContainText("Managers and officials, n. e. c.");
});

test("Batch 405 keeps eight archival cases public but their unlinked candidates private", async ({ page }) => {
  for (const id of [
    "e863af1b-ed3f-5470-b4e9-af1d996fe523", "913f7b38-487e-5736-835e-fcd033d0d867",
    "86ceb140-46b8-5617-aafa-4230945c0576", "5e7594a6-04a7-5c90-a7d1-883aa5560bd3",
    "5c99045f-2bb9-504e-bd12-03e807e6dd5d", "ab517139-dd52-5980-a3ea-42752d91446e",
    "f8b5e43e-f62b-5e7d-bc9f-83ffa2f8f855", "08b1acfc-0d3f-5815-a247-228a6d44eb25",
  ]) {
    const p = profile(id);
    expect(p.research_status).toBe("requires_archival_review");
    expect(p.research_attempt_count).toBeGreaterThan(0);
    expect(p.commissioned_officer).toBeNull();
    expect(p.claims).toEqual([]);
    expect(p.other_pre_oss_affiliations).toEqual([]);
    expect(p.name_variants).not.toContain("Harriet Klosson");
    await page.goto(`./people/${id}/`);
    await expect(page.getByRole("heading", { name: p.display_name, exact: true })).toBeVisible();
    await expect(page.locator("main")).toContainText("No reliable pre-OSS employer has yet been identified in the accessible sources reviewed.");
  }
});

test("Batch 405 direct organization URLs and surname-first search retain the evidence distinctions", async ({ page }) => {
  for (const a of profile(charles).other_pre_oss_affiliations) {
    await page.goto(`./organizations/${a.organization_id}/`);
    await expect(page.getByRole("heading", { name: a.canonical_organization, exact: true })).toBeVisible();
    await expect(page.getByRole("link", { name: "Charles S Cheston", exact: true })).toBeVisible();
    if (a.relationship_type === "government_assignment") {
      await expect(page.locator("main")).toContainText("uniformed civilian");
      await expect(page.locator("main")).toContainText("Executive Order 9078");
    }
  }
  await page.goto("./people/?q=Cheston+Charles");
  await expect(page.getByRole("link", { name: "Charles S Cheston", exact: true })).toBeVisible();
  await page.getByRole("searchbox", { name: "Search", exact: true }).fill("John R Chevalier");
  await expect(page.getByRole("link", { name: "John R Chevalier", exact: true })).toBeVisible();
});
