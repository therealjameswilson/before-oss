import { expect, test } from "@playwright/test";
import fs from "node:fs";

const people = JSON.parse(fs.readFileSync(new URL("../src/data/generated/people.json", import.meta.url), "utf8"));
const profile = (id: string) => people.find((p: { person_id: string }) => p.person_id === id);

test("Batch 408 publishes Robert Chin's immediate Columbia student pathway without calling it employment", async ({ page }) => {
  const p = profile("f861478f-8c0a-5bbb-8d23-fa26bfc7b07f");
  expect(p.identity_status).toBe("confirmed");
  expect(p.personnel_category).toBe("commissioned_army_officer");
  expect(p.commissioned_officer).toBe(true);
  expect(p.source_records[0]).toMatchObject({ pdf_page: 79, box: "122", rank_as_indexed: null });
  expect(p.immediate_pre_oss_affiliations).toHaveLength(1);
  expect(p.last_civilian_pre_service).toEqual([]);
  expect(p.other_pre_oss_affiliations).toEqual([]);
  expect(p.immediate_pre_oss_affiliations[0]).toMatchObject({
    canonical_organization: "Columbia University",
    relationship_type: "student",
    occupation: "psychology student",
    end_date: "1943",
    immediate_pre_oss: true,
    last_civilian_pre_service: false,
    temporal_basis: "strongly_date_bounded",
    claim_confidence: "high",
  });
  await page.goto(`./people/${p.person_id}/`);
  await expect(page.getByRole("heading", { name: "Robert Chin", exact: true })).toBeVisible();
  await expect(page.locator('section[aria-labelledby="immediate-affiliation"]')).toContainText("Columbia University");
  await expect(page.locator('section[aria-labelledby="immediate-affiliation"]')).toContainText("student");
  await expect(page.locator('section[aria-labelledby="civilian-employer"]')).toContainText("No reliable pre-OSS employer");
  await expect(page.locator("main")).toContainText("Leonard Saxe");
});

test("Batch 408 publishes four bounded occupation groups without inventing employers", async ({ page }) => {
  for (const [id, occupation, date, identity] of [
    ["f791bece-13d7-5dd7-99e5-61e5e0e86382", "Linemen and servicemen, telegraph, telephone, and power", "1943-01-12", "confirmed"],
    ["7e4f7593-f52e-5896-95f1-b0fb1740301c", "Occupations in manufacture of electrical machinery and accessories, n. e. c.", "1942-07-21", "high_confidence"],
    ["810d573f-3092-55de-8a5e-bb768c1a067c", "Salespersons", "1942-11-09", "high_confidence"],
    ["d6c42508-1010-59bc-ad79-e451738e274b", "Occupations in manufacture of furniture, n. e. c.", "1942-12-28", "high_confidence"],
  ]) {
    const p = profile(id);
    expect(p.identity_status).toBe(identity);
    expect(p.research_status).toBe("occupation_only_found");
    expect(p.immediate_pre_oss_affiliations).toEqual([]);
    expect(p.last_civilian_pre_service).toEqual([]);
    expect(p.other_pre_oss_affiliations).toHaveLength(1);
    expect(p.other_pre_oss_affiliations[0]).toMatchObject({ occupation, organization_id: null, relationship_type: "unknown", start_date: null, end_date: null, country: null, temporal_basis: "temporal_relation_uncertain", claim_confidence: "medium" });
    expect(p.other_pre_oss_affiliations[0].date_precision).toContain(date);
    await page.goto(`./people/${id}/`);
    await expect(page.getByRole("heading", { name: p.display_name, exact: true })).toBeVisible();
    await expect(page.locator('section[aria-labelledby="earlier-affiliations"]')).toContainText(occupation);
    await expect(page.locator('section[aria-labelledby="civilian-employer"]')).toContainText("No reliable pre-OSS employer");
  }
  expect(profile("f791bece-13d7-5dd7-99e5-61e5e0e86382").commissioned_officer).toBe(false);
});

test("Batch 408 keeps one identifier-only and four unresolved outcomes archive-routed", async ({ page }) => {
  const william = profile("8d8e06da-63d3-59c9-94d0-bb5711e77155");
  expect(william.identity_status).toBe("high_confidence");
  expect(william.research_status).toBe("requires_archival_review");
  expect(william.claims).toHaveLength(1);
  expect(william.other_pre_oss_affiliations).toEqual([]);
  for (const id of ["8a587635-8627-5fd5-955e-0f164744d6a1", "99730e97-d728-56ba-aeb8-a0946170a4a4", "2a4f4a75-e6a2-557b-bcf5-92666aeb1af7", "1c643481-b325-5214-ab44-c851e826dcbe"]) {
    const p = profile(id);
    expect(p.identity_status).toBe("unresolved");
    expect(p.research_status).toBe("requires_archival_review");
    expect(p.claims).toEqual([]);
    expect(p.other_pre_oss_affiliations).toEqual([]);
    await page.goto(`./people/${id}/`);
    await expect(page.getByRole("heading", { name: p.display_name, exact: true })).toBeVisible();
    await expect(page.locator("main")).toContainText("No reliable pre-OSS employer has yet been identified in the accessible sources reviewed.");
    await expect(page.locator("main")).not.toContainText("China Cab Company");
    await expect(page.locator("main")).not.toContainText("New York Daily News");
  }
  expect(profile("8a587635-8627-5fd5-955e-0f164744d6a1").source_records[0].rank_as_indexed).toBe("Pvt");
  expect(profile("99730e97-d728-56ba-aeb8-a0946170a4a4").source_records[0].rank_as_indexed).toBe("Lt");
});

test("Batch 408 exact-name searches surface all ten independently reviewed records", async ({ page }) => {
  for (const name of ["Durwood W Chiles", "William H Chilton", "Henry S Chin", "Robert Chin", "Walter Chinn", "James E Chippendale", "Charles L Chiriako", "Joseph J Chirichillo", "Frank J Chisari", "Corning Chisolm"]) {
    await page.goto(`./people/?q=${encodeURIComponent(name)}`);
    await expect(page.getByRole("link", { name, exact: true })).toBeVisible();
  }
});
