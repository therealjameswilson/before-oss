import { expect, test } from "@playwright/test";
import fs from "node:fs";

const people = JSON.parse(fs.readFileSync(new URL("../src/data/generated/people.json", import.meta.url), "utf8"));
const profile = (id: string) => people.find((p: { person_id: string }) => p.person_id === id);

test("Batch 407 distinguishes apprenticeship and student observations from named employers", async ({ page }) => {
  for (const [id, occupation, relationship, date] of [
    ["76efa2b4-2b39-5eb6-98cf-b5903c236e17", "Apprentices to other trades", "unknown", "1942-12-04"],
    ["dbe6b387-60ca-59e1-96cd-f92b7fbe21db", "Student", "student", "1942-11-17"],
  ]) {
    const p = profile(id);
    expect(p.identity_status).toBe("high_confidence");
    expect(p.research_status).toBe("occupation_only_found");
    expect(p.commissioned_officer).toBeNull();
    expect(p.immediate_pre_oss_affiliations).toEqual([]);
    expect(p.last_civilian_pre_service).toEqual([]);
    expect(p.other_pre_oss_affiliations).toHaveLength(1);
    expect(p.other_pre_oss_affiliations[0]).toMatchObject({ occupation, relationship_type: relationship, organization_id: null, start_date: null, end_date: null, city: null, country: null, temporal_basis: "temporal_relation_uncertain", claim_confidence: "medium" });
    expect(p.other_pre_oss_affiliations[0].date_precision).toContain(date);
    await page.goto(`./people/${id}/`);
    await expect(page.getByRole("heading", { name: p.display_name, exact: true })).toBeVisible();
    await expect(page.locator('section[aria-labelledby="earlier-affiliations"]')).toContainText(occupation);
    await expect(page.locator('section[aria-labelledby="civilian-employer"]')).toContainText("No reliable pre-OSS employer");
    await expect(page.locator('section[aria-labelledby="earlier-affiliations"]')).not.toContainText("New York University");
  }
});

test("Batch 407 keeps the Chiella and Childs identifier conflicts public without assigning candidate occupations", async ({ page }) => {
  for (const id of ["297bde5b-cc65-51a6-8b54-9a1bee9db55a", "156581f1-85c9-5c65-8384-fe9d33fb837a"]) {
    const p = profile(id);
    expect(p.identity_status).toBe("conflicting");
    expect(p.research_status).toBe("conflicting_sources");
    expect(p.claims).toHaveLength(1);
    expect(p.claims[0].claim_confidence).toBe("conflicting");
    expect(p.immediate_pre_oss_affiliations).toEqual([]);
    expect(p.last_civilian_pre_service).toEqual([]);
    expect(p.other_pre_oss_affiliations).toEqual([]);
    await page.goto(`./people/${id}/`);
    await expect(page.getByRole("heading", { name: p.display_name, exact: true })).toBeVisible();
    await expect(page.locator("main")).toContainText("conflicting sources");
    await expect(page.locator("main")).not.toContainText("Sheet metal workers");
  }
  const harold = profile("156581f1-85c9-5c65-8384-fe9d33fb837a");
  expect(harold.source_records[0].rank_as_indexed).toBe("T/Sgt");
  expect(harold.commissioned_officer).toBe(false);
  expect(profile("297bde5b-cc65-51a6-8b54-9a1bee9db55a").name_variants).not.toContain("Frank Ralph Chiella");
});

test("Batch 407 preserves five archival-review profiles and withholds the Chidsey identity candidate", async ({ page }) => {
  for (const id of ["3a873e55-894a-5cd9-bc99-8e78cdc12151", "17e29ca0-9e0d-5b35-aee9-f987cd3690b4", "2ca01d01-7dc4-53cb-8a07-43e177095fa4", "954caa3f-c9c1-51c9-869a-b0fa13a967f7", "ccb15857-8a09-5750-9e32-94e884a05dca"]) {
    const p = profile(id);
    expect(p.research_status).toBe("requires_archival_review");
    expect(p.research_attempt_count).toBeGreaterThan(0);
    expect(p.claims).toEqual([]);
    expect(p.other_pre_oss_affiliations).toEqual([]);
    await page.goto(`./people/${id}/`);
    await expect(page.getByRole("heading", { name: p.display_name, exact: true })).toBeVisible();
    await expect(page.locator("main")).toContainText("No reliable pre-OSS employer has yet been identified in the accessible sources reviewed.");
    await expect(page.locator("main")).not.toContainText("Charles Nordhoff");
  }
});

test("Batch 407 exact-name searches surface the new reviewed records", async ({ page }) => {
  for (const name of ["William Chidekel", "Shirley A Chidsey", "Frank R Chiella", "Harold A Childs", "Dawson W Chiles"]) {
    await page.goto(`./people/?q=${encodeURIComponent(name)}`);
    await expect(page.getByRole("link", { name, exact: true })).toBeVisible();
  }
});
