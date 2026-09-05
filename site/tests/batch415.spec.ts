import { expect, test } from "@playwright/test";
import fs from "node:fs";

const people = JSON.parse(fs.readFileSync(new URL("../src/data/generated/people.json", import.meta.url), "utf8"));
const profile = (id: string) => people.find((p: { person_id: string }) => p.person_id === id);

test("Batch 415 publishes two bounded Army occupations without inventing employers", async ({ page }) => {
  for (const [id, name, occupation, date, serial] of [
    ["16e04c43-c477-574f-8f47-ab51f1914b49", "Jerome H Chudej", "Farm hands, general farms", "20 April 1942", "••••0637"],
    ["3c0feb4f-c51b-562d-a678-91c5aebb8619", "Constantine W Chuleas", "Stamping occupations in mechanical treatment of metals", "20 November 1942", "••••0854"],
  ]) {
    const p = profile(id);
    expect(p.identity_status).toBe("high_confidence");
    expect(p.personnel_category).toBe("enlisted_army_personnel");
    expect(p.commissioned_officer).toBe(false);
    expect(p.research_status).toBe("occupation_only_found");
    expect(p.source_records[0]).toMatchObject({ pdf_page: 81, box: "124", serial_masked: serial });
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
  expect(profile("16e04c43-c477-574f-8f47-ab51f1914b49").name_variants).toContain("Jero H Chudej");
  expect(profile("3c0feb4f-c51b-562d-a678-91c5aebb8619").name_variants).toContain('Constantine W. "Gus" Chuleas');
  expect(profile("3c0feb4f-c51b-562d-a678-91c5aebb8619").source_records[0].rank_as_indexed).toBe("Pvt");
});

test("Batch 415 exposes Chin Chung's complete-name identifier conflict without transferring an Army occupation", async ({ page }) => {
  const p = profile("471aa9c5-0899-54a7-91d1-160ade15dcfc");
  expect(p.identity_status).toBe("conflicting");
  expect(p.research_status).toBe("conflicting_sources");
  expect(p.archival_file.review_priority).toBe("critical");
  expect(p.claims).toHaveLength(1);
  expect(p.claims[0].claim_confidence).toBe("conflicting");
  expect(p.immediate_pre_oss_affiliations).toEqual([]);
  expect(p.last_civilian_pre_service).toEqual([]);
  expect(p.other_pre_oss_affiliations).toEqual([]);

  await page.goto(`./people/${p.person_id}/`);
  await expect(page.getByRole("heading", { name: "Chin H Chung", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("Edward F Foster");
  await expect(page.locator("main")).toContainText("conflicting sources");
});

test("Batch 415 qualifies the George Chumas Greek Group lead without publishing it as an affiliation", async ({ page }) => {
  const p = profile("6e8ef3e4-41ae-5e38-9a7b-a129e1ba0d7d");
  expect(p.identity_status).toBe("unresolved");
  expect(p.research_status).toBe("needs_identity_review");
  expect(p.personnel_category).toBe("unknown_or_indeterminate");
  expect(p.commissioned_officer).toBeNull();
  expect(p.claims).toEqual([]);
  expect(p.immediate_pre_oss_affiliations).toEqual([]);
  expect(p.last_civilian_pre_service).toEqual([]);
  expect(p.other_pre_oss_affiliations).toEqual([]);

  await page.goto(`./people/${p.person_id}/`);
  await expect(page.getByRole("heading", { name: "George Chumas", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("lists a 1st Lt. George Chumas in OSS Greek Group VI");
  await expect(page.locator("main")).toContainText("supplies no index number or second identifying datum");
  await expect(page.locator("main")).toContainText("Commissioned officerUnknown");
  await expect(page.locator('section[aria-labelledby="immediate-affiliation"]')).toContainText("No reviewed claim currently meets the publication threshold");
  await expect(page.locator('section[aria-labelledby="civilian-employer"]')).toContainText("No reviewed claim currently meets the publication threshold");
});

test("Batch 415 archive-routes six unresolved people and makes the full cohort searchable", async ({ page }) => {
  const unresolved = [
    ["73f5f637-3a2b-5851-a47e-daaea7b81fb2", "••••6860"],
    ["99a32b71-d20c-5e91-872f-a8262b30444f", "••••7901"],
    ["e806fa99-e940-52c2-b617-a8e986a6458e", null],
    ["eefdabd4-d4b8-589e-8460-452693535f96", null],
    ["4f0d5826-94bf-5da5-9faf-c0258038ef9b", null],
    ["162f178d-0651-5261-ad6a-6e635111c8fb", null],
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
    "Jerome H Chudej",
    "Raymond A Chuipek",
    "Constantine W Chuleas",
    "George Chumas",
    "Raymond L Chumbley",
    "William B Chun",
    "Chin H Chung",
    "John Chung",
    "Kei W Chung",
    "Lois W Chung",
  ]) {
    await page.goto(`./people/?q=${encodeURIComponent(name)}`);
    await expect(page.getByRole("link", { name, exact: true })).toBeVisible();
  }
});
