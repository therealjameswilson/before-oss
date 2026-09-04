import { expect, test } from "@playwright/test";
import fs from "node:fs";

const people = JSON.parse(fs.readFileSync(new URL("../src/data/generated/people.json", import.meta.url), "utf8"));
const profile = (id: string) => people.find((p: { person_id: string }) => p.person_id === id);
const milan = "b76027c3-b5ec-5375-a98b-39090501e29c";
const anthony = "2cd76c71-88f0-5d6b-9449-9271ec96b599";

test("Batch 406 corrects Paul Child's citation and withdraws unsupported employment boundaries", async ({ page }) => {
  const p = profile("a9b1ec13-509a-57f2-bb04-d2453d49e908");
  expect(p.immediate_pre_oss_affiliations).toEqual([]);
  expect(p.last_civilian_pre_service).toEqual([]);
  expect(p.other_pre_oss_affiliations).toHaveLength(1);
  expect(p.other_pre_oss_affiliations[0]).toMatchObject({ start_date: null, end_date: null, immediate_pre_oss: false, last_civilian_pre_service: false, temporal_basis: "documented_prewar", occupation: "art and French teacher", claim_confidence: "medium" });
  expect(p.claims).toHaveLength(2);
  expect(p.claims.some((c: { claim_type: string }) => c.claim_type === "last_civilian_pre_service")).toBe(false);
  const sources = JSON.parse(fs.readFileSync(new URL("../src/data/generated/sources.json", import.meta.url), "utf8"));
  const source = sources.find((s: { stable_url: string }) => s.stable_url?.includes("paul-childs-shimmering-photographs"));
  expect(source).toMatchObject({ author_creator: "Cynthia Zarin", publication_record_date: "2017-12-02" });
  await page.goto(`./people/${p.person_id}/`);
  await expect(page.locator('section[aria-labelledby="earlier-affiliations"]')).toContainText("Avon Old Farms School");
  await expect(page.locator('section[aria-labelledby="immediate-affiliation"]')).not.toContainText("Avon Old Farms School");
  await expect(page.locator('section[aria-labelledby="civilian-employer"]')).not.toContainText("Avon Old Farms School");
  await expect(page.locator("main")).toContainText("Cynthia Zarin");
  await expect(page.getByRole("link", { name: "Cooking with Julia Child", exact: true }).first()).toBeVisible();
});

test("Batch 406 publishes Cheyovich's explicit military training transfer without inventing employment dates", async ({ page }) => {
  const p = profile(milan);
  expect(p.identity_status).toBe("confirmed");
  expect(p.personnel_category).toBe("enlisted_army_personnel");
  expect(p.commissioned_officer).toBe(false);
  expect(p.source_records[0]).toMatchObject({ pdf_page: 79, box: "121", rank_as_indexed: null });
  expect(p.immediate_pre_oss_affiliations).toHaveLength(1);
  expect(p.last_civilian_pre_service).toEqual([]);
  expect(p.other_pre_oss_affiliations).toEqual([]);
  const a = p.immediate_pre_oss_affiliations[0];
  expect(a).toMatchObject({ relationship_type: "military_assignment", organization_name_as_found: "Signal Corps Training School in Chicago", start_date: null, end_date: null, immediate_pre_oss: true, last_civilian_pre_service: false, temporal_basis: "explicit_immediate", claim_confidence: "confirmed", city: "Chicago" });
  expect(a.date_precision).toContain("1943-07-02");
  expect(p.claims).toHaveLength(2);
  await page.goto(`./people/${milan}/`);
  await expect(page.getByRole("heading", { name: "Milan Cheyovich", exact: true })).toBeVisible();
  await expect(page.locator('section[aria-labelledby="immediate-affiliation"]')).toContainText("Signal Corps Training School, Chicago");
  await expect(page.locator("main")).toContainText("1943-07-02");
  await expect(page.locator('section[aria-labelledby="civilian-employer"]')).toContainText("No reliable pre-OSS employer");
  await page.goto(`./organizations/${a.organization_id}/`);
  await expect(page.getByRole("heading", { name: "Signal Corps Training School, Chicago", exact: true })).toBeVisible();
  await expect(page.getByRole("link", { name: "Milan Cheyovich", exact: true })).toBeVisible();
});

test("Batch 406 publishes five bounded occupation observations with no employer or OSS-rank inference", async ({ page }) => {
  for (const [id, occupation, date] of [
    ["964b6111-afab-5802-ae6e-2f87b48ebfd6", "Mechanics and repairmen, n. e. c.", "1943-02-09"],
    [anthony, "Lithographers", "1943-04-02"],
    ["95dea97c-22da-5e0e-95ae-9c4c5967ec84", "Occupations in fabrication of textile products, n. e. c.", "1942-10-30"],
    ["7edeb440-5998-5d5a-bfa4-ceda4e17c2fd", "Locomotive firemen", "1942-01-10"],
    ["0b62f542-2caf-5bc1-9e19-17edb44ef381", "Occupations in manufacture of paper goods", "1942-12-10"],
  ]) {
    const p = profile(id);
    expect(p.identity_status).toBe("high_confidence");
    expect(p.commissioned_officer).toBeNull();
    expect(p.research_status).toBe("occupation_only_found");
    expect(p.source_records[0].rank_as_indexed).toBeNull();
    expect(p.immediate_pre_oss_affiliations).toEqual([]);
    expect(p.last_civilian_pre_service).toEqual([]);
    expect(p.other_pre_oss_affiliations).toHaveLength(1);
    expect(p.other_pre_oss_affiliations[0]).toMatchObject({ occupation, organization_id: null, relationship_type: "unknown", claim_confidence: "medium", temporal_basis: "temporal_relation_uncertain", start_date: null, end_date: null, country: null });
    expect(p.other_pre_oss_affiliations[0].date_precision).toContain(date);
    await page.goto(`./people/${id}/`);
    await expect(page.getByRole("heading", { name: p.display_name, exact: true })).toBeVisible();
    await expect(page.locator('section[aria-labelledby="earlier-affiliations"]')).toContainText(occupation);
    await expect(page.locator('section[aria-labelledby="civilian-employer"]')).toContainText("No reliable pre-OSS employer");
  }
});

test("Batch 406 keeps four unresolved profiles dignified and unlinked candidate employers private", async ({ page }) => {
  for (const id of ["3c10b2cb-2ef4-53ed-8a46-3bda2c063269", "ac670b83-898f-540f-a496-a80442b7d0d8", "ae5c303e-a026-58e5-ba2e-0bf6498418c4", "d3b5d8ef-bade-5d50-b5fb-0a502e40a875"]) {
    const p = profile(id);
    expect(p.research_status).toBe("requires_archival_review");
    expect(p.research_attempt_count).toBeGreaterThan(0);
    expect(p.commissioned_officer).toBeNull();
    expect(p.claims).toEqual([]);
    expect(p.other_pre_oss_affiliations).toEqual([]);
    await page.goto(`./people/${id}/`);
    await expect(page.getByRole("heading", { name: p.display_name, exact: true })).toBeVisible();
    await expect(page.locator("main")).toContainText("No reliable pre-OSS employer has yet been identified in the accessible sources reviewed.");
    await expect(page.locator("main")).not.toContainText("F. J. Lisman Company");
    await expect(page.locator("main")).not.toContainText("Love Hardware");
  }
  expect(profile("964b6111-afab-5802-ae6e-2f87b48ebfd6").name_variants).not.toContain("Wellington Lum Chew");
});

test("Batch 406 surname variants are searchable without overwriting the source spelling", async ({ page }) => {
  const p = profile(anthony);
  expect(p.display_name).toBe("Anthony C Chiapetta");
  expect(p.name_variants).toContain("Anthony C Chiapatta");
  expect(p.claims).toHaveLength(2);
  await page.goto("./people/?q=Anthony+Chiapatta");
  await expect(page.getByRole("link", { name: "Anthony C Chiapetta", exact: true })).toBeVisible();
  await page.goto(`./people/${anthony}/`);
  await expect(page.locator(".index-record").first()).toContainText("Chiapetta | Anthony | C");
  await expect(page.locator("main")).toContainText("Anthony C Chiapatta");
});
