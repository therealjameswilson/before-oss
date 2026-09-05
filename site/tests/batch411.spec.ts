import { expect, test } from "@playwright/test";
import fs from "node:fs";

const people = JSON.parse(fs.readFileSync(new URL("../src/data/generated/people.json", import.meta.url), "utf8"));
const profile = (id: string) => people.find((p: { person_id: string }) => p.person_id === id);

test("Batch 411 qualifies Chretien's French intelligence pathway without inventing an OSS transfer", async ({ page }) => {
  const p = profile("86acb7be-f510-57a5-92a2-8dd2556fd316");
  expect(p.identity_status).toBe("high_confidence");
  expect(p.personnel_category).toBe("foreign_or_allied_military_personnel");
  expect(p.commissioned_officer).toBe(true);
  expect(p.allied_or_foreign_personnel).toBe(true);
  expect(p.research_status).toBe("completed");
  expect(p.source_records[0]).toMatchObject({ pdf_page: 80, box: "122", rank_as_indexed: "Col", notes_as_indexed: "French" });
  expect(p.immediate_pre_oss_affiliations).toHaveLength(1);
  expect(p.last_civilian_pre_service).toEqual([]);
  expect(p.immediate_pre_oss_affiliations[0]).toMatchObject({
    canonical_organization: "French Service de Renseignement (SR)",
    relationship_type: "military_assignment",
    temporal_basis: "probable_immediate",
    identity_confidence: "high_confidence",
    claim_confidence: "medium",
  });

  await page.goto(`./people/${p.person_id}/`);
  await expect(page.getByRole("heading", { name: "Jean Chretien", exact: true })).toBeVisible();
  await expect(page.locator('section[aria-labelledby="immediate-affiliation"]')).toContainText("French Service de Renseignement");
  await expect(page.locator('section[aria-labelledby="civilian-employer"]')).toContainText("No reliable pre-OSS employer");
  await expect(page.locator("main")).toContainText("The OSS in Algiers");
  await expect(page.locator("main")).toContainText("probable immediate");
});

test("Batch 411 links John Laurence Chrislow to a qualified Naval Reserve pathway while keeping education separate", async ({ page }) => {
  const p = profile("18b6fb4e-98c7-5805-9e26-ce9ac78a7048");
  expect(p.identity_status).toBe("high_confidence");
  expect(p.personnel_category).toBe("commissioned_naval_officer");
  expect(p.commissioned_officer).toBe(true);
  expect(p.name_variants).toEqual(expect.arrayContaining(["John Laurence Chrislow"]));
  expect(p.immediate_pre_oss_affiliations).toHaveLength(1);
  expect(p.last_civilian_pre_service).toEqual([]);
  expect(p.immediate_pre_oss_affiliations[0]).toMatchObject({
    canonical_organization: "United States Naval Reserve",
    role_title: "Ensign",
    relationship_type: "military_assignment",
    start_date: "1943-05-27",
    temporal_basis: "probable_immediate",
    claim_confidence: "medium",
  });

  await page.goto(`./people/${p.person_id}/`);
  await expect(page.getByRole("heading", { name: "John L Chrislow", exact: true })).toBeVisible();
  await expect(page.locator('section[aria-labelledby="immediate-affiliation"]')).toContainText("United States Naval Reserve");
  await expect(page.locator('section[aria-labelledby="civilian-employer"]')).toContainText("No reliable pre-OSS employer");
  await expect(page.locator("main")).toContainText("OSS: Headquarters and Headquarters Detachment Personnel Records");
  await expect(page.locator("main")).toContainText("Capstan");
});

test("Batch 411 withholds the postwar Anthony Chrisler identity lead from public facts", async ({ page }) => {
  const p = profile("919af5b7-2cd4-5a6b-8175-a9bafeafd6e1");
  expect(p.identity_status).toBe("unresolved");
  expect(p.research_status).toBe("requires_archival_review");
  expect(p.claims).toEqual([]);
  expect(p.immediate_pre_oss_affiliations).toEqual([]);
  expect(p.last_civilian_pre_service).toEqual([]);

  await page.goto(`./people/${p.person_id}/`);
  await expect(page.getByRole("heading", { name: "Anthony M Chrisler", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("archival review");
  await expect(page.locator('section[aria-labelledby="civilian-employer"]')).toContainText("No reliable pre-OSS employer");
  await expect(page.locator("main")).not.toContainText("CAP-5");
});

test("Batch 411 archive-routes eight unresolved people and makes the full cohort searchable", async ({ page }) => {
  const unresolved = [
    ["0f77fc28-499c-5824-a06e-da2e31dd33bb", null],
    ["919af5b7-2cd4-5a6b-8175-a9bafeafd6e1", null],
    ["02302f01-e515-58e5-af6f-c1d482f981ea", "••••7243"],
    ["9653f3c3-7536-5bdf-9087-be7781b8c46f", "••••6164"],
    ["e230b035-c192-5130-a278-69bea41b2da3", null],
    ["2e800c49-fda9-514f-99d9-e8c3ba072a05", "••••9350"],
    ["e6354ca1-561d-56b5-8b1e-c4a6e13d06ba", null],
    ["e28dcc23-aaf4-535d-87c2-8995cd2d1574", "••••9878"],
  ];
  for (const [id, serial] of unresolved) {
    const p = profile(id as string);
    expect(p.identity_status).toBe("unresolved");
    expect(p.research_status).toBe("requires_archival_review");
    expect(p.claims).toEqual([]);
    expect(p.immediate_pre_oss_affiliations).toEqual([]);
    expect(p.last_civilian_pre_service).toEqual([]);
    expect(p.source_records[0].serial_masked).toBe(serial);
  }

  for (const name of [
    "Jean Chretien",
    "John Chrislaw",
    "Anthony M Chrisler",
    "John L Chrislow",
    "Joseph D Chrisman",
    "David J Christ",
    "Mark J Christ",
    "Charles N Christensen",
    "Dale Christensen",
    "Emil E Christensen",
  ]) {
    await page.goto(`./people/?q=${encodeURIComponent(name)}`);
    await expect(page.getByRole("link", { name, exact: true })).toBeVisible();
  }
});
