import { expect, test } from "@playwright/test";
import fs from "node:fs";

const people = JSON.parse(fs.readFileSync(new URL("../src/data/generated/people.json", import.meta.url), "utf8"));
const profile = (id: string) => people.find((person: { person_id: string }) => person.person_id === id);
const occupations = [
  ["2ecdbc80-de30-5429-9cbf-9aea2e9ccbec", "Routemen", "1943-07-15"],
  ["88b3ba8a-9796-50b6-b74d-02eb8adfa16a", "Cooks, except private family", "1942-09-16"],
  ["4091f765-1f01-50d1-9a5e-94625d28073e", "Meatcutters, except in slaughtering and packing houses", "1942-09-05"],
  ["a3a8b61e-e34c-570b-9895-8a6faa99e355", "Attendants, filling stations and parking lots", "1943-10-07"],
  ["ede3fe35-7b17-5d18-a6f1-2ff194986020", "Clerks, general", "1944-01-17"],
  ["faa58812-da75-5ee3-9dbe-b7150b0cc660", "Painters, construction and maintenance", "1942-05-09"],
];

test("Batch 403 qualifies six Army occupations without inventing employers, work dates, locations or OSS ranks", async ({ page }) => {
  for (const [id, occupation, date] of occupations) {
    const p = profile(id);
    expect(p.identity_status).toBe("high_confidence");
    expect(p.commissioned_officer).toBeNull();
    expect(p.source_records[0]).toMatchObject({ pdf_page: 78, box: "120", archive_location: "230/86/28/06", rank_as_indexed: null });
    expect(p.research_status).toBe("occupation_only_found");
    expect(p.research_attempt_count).toBeGreaterThan(0);
    expect(p.immediate_pre_oss_affiliations).toEqual([]);
    expect(p.last_civilian_pre_service).toEqual([]);
    expect(p.other_pre_oss_affiliations).toHaveLength(1);
    expect(p.other_pre_oss_affiliations[0]).toMatchObject({ occupation, organization_id: null, relationship_type: "unknown", start_date: null, end_date: null, country: null, temporal_basis: "temporal_relation_uncertain", claim_confidence: "medium", publication_status: "publish_qualified" });
    expect(p.other_pre_oss_affiliations[0].date_precision).toContain(date);
    expect(p.claims).toHaveLength(2);
    const claim = p.claims.find((claim: { claim_type: string }) => claim.claim_type === "occupation");
    expect(claim.sources).toHaveLength(3);
    await page.goto(`./people/${id}/`);
    await expect(page.getByRole("heading", { name: p.display_name, exact: true })).toBeVisible();
    const earlier = page.locator('section[aria-labelledby="earlier-affiliations"]');
    await expect(earlier).toContainText(occupation);
    await expect(earlier).toContainText(date);
    await expect(earlier).toContainText("temporal relation uncertain");
    await expect(page.locator('section[aria-labelledby="civilian-employer"]')).toContainText("No reliable pre-OSS employer");
  }
});

test("Batch 403 keeps Chekrezi and Vung candidates private and preserves their indexed spellings", async ({ page }) => {
  for (const [id, identity, name] of [
    ["b4eb9569-3207-5ea7-a556-a107e4ed6f0b", "probable", "C A Chekrezi"],
    ["96c810da-5f93-590f-9532-e3c3f8ae8d96", "ambiguous", "Vung T Chen"],
  ]) {
    const p = profile(id);
    expect(p.identity_status).toBe(identity);
    expect(p.claims).toEqual([]);
    expect(p.other_pre_oss_affiliations).toEqual([]);
    expect(p.research_status).toBe("requires_archival_review");
    expect(p.name_variants).not.toContain("Yung T Chen");
    expect(p.name_variants).not.toContain("Constantine A. Chekrezi");
    await page.goto(`./people/${id}/`);
    await expect(page.getByRole("heading", { name, exact: true })).toBeVisible();
    await expect(page.locator('section[aria-labelledby="earlier-affiliations"] .affiliation-card')).toHaveCount(0);
    await expect(page.locator("main")).toContainText("requires archival review");
  }
  expect(profile("96c810da-5f93-590f-9532-e3c3f8ae8d96").identity_evidence).toContain("1946");
});

test("Batch 403 gives Tung-Yu Chen and Jane P Chennault substantive unresolved pages", async ({ page }) => {
  for (const id of ["937d8ad6-6821-54df-80f8-2bcb699625d6", "0655ba1e-8528-52f0-9db4-f250406cc1e2"]) {
    const p = profile(id);
    expect(p.identity_status).toBe("unresolved");
    expect(p.claims).toEqual([]);
    expect(p.research_status).toBe("requires_archival_review");
    expect(p.research_attempt_count).toBeGreaterThan(0);
    await page.goto(`./people/${id}/`);
    await expect(page.getByRole("heading", { name: p.display_name, exact: true })).toBeVisible();
    await expect(page.locator("main")).toContainText("Box 120");
    await expect(page.locator("main")).toContainText("No reliable pre-OSS employer has yet been identified in the accessible sources reviewed.");
  }
});

test("Batch 403 search finds the indexed people and does not promote a speculative Guard assignment", async ({ page }) => {
  const p = profile("faa58812-da75-5ee3-9dbe-b7150b0cc660");
  expect(p.name_variants).not.toContain("George N. Chenoweth");
  expect(p.claims.map((claim: { claim_type: string }) => claim.claim_type).sort()).toEqual(["identity", "occupation"]);
  await page.goto("./people/");
  await page.getByRole("searchbox", { name: "Search", exact: true }).fill("Chemsak");
  await expect(page.getByRole("link", { name: "Michael C Chemsak", exact: true })).toBeVisible();
  await page.getByRole("searchbox", { name: "Search", exact: true }).fill("Tung-Yu Chen");
  await expect(page.getByRole("link", { name: "Tung-Yu Chen", exact: true })).toBeVisible();
});
