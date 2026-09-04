import { expect, test } from "@playwright/test";
import fs from "node:fs";

const people = JSON.parse(fs.readFileSync(new URL("../src/data/generated/people.json", import.meta.url), "utf8"));
const profile = (id: string) => people.find((p: { person_id: string }) => p.person_id === id);

test("Batch 409 publishes Chittick's 1940 Pure Oil affiliation without promoting it to employer or immediate status", async ({ page }) => {
  const p = profile("51732786-8509-5906-a4b4-66fd6bff7cac");
  expect(p.identity_status).toBe("high_confidence");
  expect(p.personnel_category).toBe("commissioned_army_officer");
  expect(p.commissioned_officer).toBe(true);
  expect(p.research_status).toBe("requires_archival_review");
  expect(p.source_records[0]).toMatchObject({ pdf_page: 79, box: "122", rank_as_indexed: "Col", serial_masked: "••••0258" });
  expect(p.immediate_pre_oss_affiliations).toEqual([]);
  expect(p.last_civilian_pre_service).toEqual([]);
  expect(p.other_pre_oss_affiliations).toHaveLength(1);
  expect(p.other_pre_oss_affiliations[0]).toMatchObject({
    canonical_organization: "The Pure Oil Company",
    historical_organization: "The Pure Oil Co.",
    relationship_type: "professional_affiliation",
    temporal_basis: "documented_prewar",
    claim_confidence: "high",
    immediate_pre_oss: false,
    last_civilian_pre_service: false,
  });
  await page.goto(`./people/${p.person_id}/`);
  await expect(page.getByRole("heading", { name: "Martin B Chittick", exact: true })).toBeVisible();
  await expect(page.locator('section[aria-labelledby="earlier-affiliations"]')).toContainText("The Pure Oil Company");
  await expect(page.locator('section[aria-labelledby="earlier-affiliations"]')).toContainText("professional affiliation");
  await expect(page.locator('section[aria-labelledby="civilian-employer"]')).toContainText("No reliable pre-OSS employer");
  await expect(page.locator("main")).toContainText("American Society for Testing Materials");
  await expect(page.locator("main")).toContainText("United States Civil Service Commission");
});

test("Batch 409 publishes Choha's bounded Army occupation without inventing an employer", async ({ page }) => {
  const p = profile("f160b3e8-0b1d-5abd-ac05-f07ffe541999");
  expect(p.identity_status).toBe("high_confidence");
  expect(p.personnel_category).toBe("enlisted_army_personnel");
  expect(p.commissioned_officer).toBe(false);
  expect(p.research_status).toBe("occupation_only_found");
  expect(p.source_records[0]).toMatchObject({ pdf_page: 79, box: "122", rank_as_indexed: null, serial_masked: "••••9283" });
  expect(p.immediate_pre_oss_affiliations).toEqual([]);
  expect(p.last_civilian_pre_service).toEqual([]);
  expect(p.other_pre_oss_affiliations).toHaveLength(1);
  expect(p.other_pre_oss_affiliations[0]).toMatchObject({
    occupation: "Mechanics and repairmen, airplane",
    organization_id: null,
    relationship_type: "unknown",
    temporal_basis: "temporal_relation_uncertain",
    claim_confidence: "medium",
  });
  expect(p.other_pre_oss_affiliations[0].date_precision).toContain("1944-02-08");
  await page.goto(`./people/${p.person_id}/`);
  await expect(page.getByRole("heading", { name: "DeForest D Choha", exact: true })).toBeVisible();
  await expect(page.locator('section[aria-labelledby="earlier-affiliations"]')).toContainText("Mechanics and repairmen, airplane");
  await expect(page.locator('section[aria-labelledby="civilian-employer"]')).toContainText("No reliable pre-OSS employer");
});

test("Batch 409 qualifies two Yugoslavia identity leads and leaves their pre-OSS histories unresolved", async ({ page }) => {
  for (const [id, name] of [
    ["ebd9f337-9fc5-5b5e-a22f-1b2020ff091c", "Ernest L Chmieleski"],
    ["f7ca36b2-9b93-5558-a6d1-40fd78fe0dc1", "Joseph F Chochola"],
  ]) {
    const p = profile(id);
    expect(p.identity_status).toBe("probable");
    expect(p.research_status).toBe("requires_archival_review");
    expect(p.immediate_pre_oss_affiliations).toEqual([]);
    expect(p.last_civilian_pre_service).toEqual([]);
    expect(p.other_pre_oss_affiliations).toEqual([]);
    expect(p.claims).toHaveLength(1);
    expect(p.claims[0]).toMatchObject({ claim_type: "identity", claim_confidence: "medium", publication_status: "publish_qualified" });
    await page.goto(`./people/${id}/`);
    await expect(page.getByRole("heading", { name, exact: true })).toBeVisible();
    await expect(page.locator("main")).toContainText("probable");
    await expect(page.locator("main")).toContainText("Waldemar Grabowski");
    await expect(page.locator("main")).toContainText("No reliable pre-OSS employer has yet been identified in the accessible sources reviewed.");
  }
});

test("Batch 409 keeps six unresolved people archive-routed and makes all ten exact names searchable", async ({ page }) => {
  for (const id of [
    "b837a209-4178-58ee-81b5-3f08eca2044b",
    "28875606-e837-5579-a6a2-4978bba482ef",
    "8e8ab02f-80d9-5c28-bbef-1f3abfbefb93",
    "667ecc9e-66f0-526d-a8a0-259242f0ea8f",
    "d7d32abf-05c1-55b3-8e8e-17a7efe1a0b3",
    "937f3bee-20bf-5379-9541-ad720f2347ef",
  ]) {
    const p = profile(id);
    expect(p.identity_status).toBe("unresolved");
    expect(p.research_status).toBe("requires_archival_review");
    expect(p.claims).toEqual([]);
    expect(p.other_pre_oss_affiliations).toEqual([]);
  }
  expect(profile("8e8ab02f-80d9-5c28-bbef-1f3abfbefb93").source_records[0].serial_masked).toBe("••••0402");
  for (const name of [
    "Herbert G Chissell",
    "Martin B Chittick",
    "C Chittinandhan",
    "Charles E Chitwood",
    "Churchill T Chiu",
    "Ernest L Chmieleski",
    "Charles Choate",
    "Wade T Choate",
    "Joseph F Chochola",
    "DeForest D Choha",
  ]) {
    await page.goto(`./people/?q=${encodeURIComponent(name)}`);
    await expect(page.getByRole("link", { name, exact: true })).toBeVisible();
  }
});
