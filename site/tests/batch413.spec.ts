import { expect, test } from "@playwright/test";
import fs from "node:fs";

const people = JSON.parse(fs.readFileSync(new URL("../src/data/generated/people.json", import.meta.url), "utf8"));
const profile = (id: string) => people.find((p: { person_id: string }) => p.person_id === id);

test("Batch 413 publishes two bounded Army occupations without inventing employers", async ({ page }) => {
  for (const [id, name, occupation, date] of [
    ["1736c969-a322-5e9f-8229-c27ae6054dcb", "Gustave M Christianson", "Occupations in printing and publishing, n.e.c.", "8 September 1943"],
    ["81ec4047-d242-56fe-bd16-b2affead3366", "Richard A Christman", "Occupations in production of bakery products, n.e.c.", "12 May 1943"],
  ]) {
    const p = profile(id);
    expect(p.identity_status).toBe("high_confidence");
    expect(p.personnel_category).toBe("enlisted_army_personnel");
    expect(p.commissioned_officer).toBe(false);
    expect(p.research_status).toBe("occupation_only_found");
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
  expect(profile("1736c969-a322-5e9f-8229-c27ae6054dcb").name_variants).toContain("Gustav M Christianson");
  expect(profile("81ec4047-d242-56fe-bd16-b2affead3366").source_records[0].rank_as_indexed).toBe("T-5");
});

test("Batch 413 preserves two identifier conflicts without assigning their Army occupations", async ({ page }) => {
  for (const [id, name, rejectedOccupation] of [
    ["c2d682f4-0bb7-5931-9a87-4235d10b9f91", "Christian C Christis", "Construction occupations"],
    ["a40abcbd-0889-52c3-ac5c-4d62ed6ae3b8", "Peter A Christoff", "Managers and officials"],
  ]) {
    const p = profile(id);
    expect(p.identity_status).toBe("conflicting");
    expect(p.research_status).toBe("conflicting_sources");
    expect(p.claims).toHaveLength(1);
    expect(p.claims[0].claim_confidence).toBe("conflicting");
    expect(p.immediate_pre_oss_affiliations).toEqual([]);
    expect(p.last_civilian_pre_service).toEqual([]);
    expect(p.other_pre_oss_affiliations).toEqual([]);
    await page.goto(`./people/${id}/`);
    await expect(page.getByRole("heading", { name, exact: true })).toBeVisible();
    await expect(page.locator("main")).toContainText("conflicting sources");
    await expect(page.locator("main")).not.toContainText(rejectedOccupation);
  }
});

test("Batch 413 archive-routes six unresolved people and makes the full cohort searchable", async ({ page }) => {
  const unresolved = [
    ["f47ac5d8-331e-5867-868b-fc35915dbf4d", "••••4621"],
    ["45fa4044-208b-503b-b46a-aef52ab7a166", "••••4660"],
    ["fa7975d5-b4c3-5d3b-873b-ce5d5253adf5", null],
    ["235cb4c0-06a5-5831-82c6-55b08e00900a", null],
    ["3847bf8c-3f23-53db-9336-0acf281168cb", "••••9098"],
    ["703c7ac7-c148-54d8-8df0-38d919378a94", null],
  ];
  for (const [id, serial] of unresolved) {
    const p = profile(id as string);
    expect(p.identity_status).toBe("unresolved");
    expect(p.research_status).toBe("requires_archival_review");
    expect(p.claims).toEqual([]);
    expect(p.immediate_pre_oss_affiliations).toEqual([]);
    expect(p.last_civilian_pre_service).toEqual([]);
    expect(p.other_pre_oss_affiliations).toEqual([]);
    expect(p.source_records[0].serial_masked).toBe(serial);
  }

  for (const name of [
    "Roy P Christian",
    "Waldemar C Christian",
    "William B Christian",
    "William F Christians",
    "Herbert P Christiansen",
    "Gustave M Christianson",
    "Christian C Christis",
    "Richard A Christman",
    "William D Christman",
    "Peter A Christoff",
  ]) {
    await page.goto(`./people/?q=${encodeURIComponent(name)}`);
    await expect(page.getByRole("link", { name, exact: true })).toBeVisible();
  }
});
