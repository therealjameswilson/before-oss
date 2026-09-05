import { expect, test } from "@playwright/test";
import fs from "node:fs";

const people = JSON.parse(fs.readFileSync(new URL("../src/data/generated/people.json", import.meta.url), "utf8"));
const profile = (id: string) => people.find((p: { person_id: string }) => p.person_id === id);

test("Batch 414 publishes George Chrysostomas's explicit Army-to-OSS pathway without inventing an employer", async ({ page }) => {
  const p = profile("17587760-1571-58d0-abab-ab1eda891e15");
  expect(p.identity_status).toBe("confirmed");
  expect(p.personnel_category).toBe("commissioned_army_officer");
  expect(p.commissioned_officer).toBe(true);
  expect(p.source_records[0]).toMatchObject({ pdf_page: 80, box: "124", rank_as_indexed: null, serial_masked: "••••5041" });
  expect(p.name_variants).toContain("George Christy Chrysostomas");
  expect(p.immediate_pre_oss_affiliations).toHaveLength(1);
  expect(p.last_civilian_pre_service).toEqual([]);
  expect(p.immediate_pre_oss_affiliations[0]).toMatchObject({
    canonical_organization: "19th Communications Squadron",
    relationship_type: "military_assignment",
    role_title: "Communications soldier",
    occupation: "Radio communications",
    end_date: "1943-07",
    immediate_pre_oss: true,
    last_civilian_pre_service: false,
    temporal_basis: "explicit_immediate",
    identity_confidence: "confirmed",
    claim_confidence: "confirmed",
  });
  expect(p.other_pre_oss_affiliations).toHaveLength(2);
  expect(p.other_pre_oss_affiliations).toEqual(expect.arrayContaining([
    expect.objectContaining({ relationship_type: "student", organization_name_as_found: "a radio communications school in New York", claim_confidence: "high" }),
    expect.objectContaining({ relationship_type: "unknown", occupation: "Musicians and teachers of music", organization_id: null, claim_confidence: "medium" }),
  ]));

  await page.goto(`./people/${p.person_id}/`);
  await expect(page.getByRole("heading", { name: "George Chrysostomas", exact: true })).toBeVisible();
  await expect(page.locator('section[aria-labelledby="immediate-affiliation"]')).toContainText("19th Communications Squadron");
  await expect(page.locator('section[aria-labelledby="immediate-affiliation"]')).toContainText("military assignment");
  await expect(page.locator('section[aria-labelledby="civilian-employer"]')).toContainText("No reliable pre-OSS employer");
  await expect(page.locator('section[aria-labelledby="earlier-affiliations"]')).toContainText("radio communications school in New York");
  await expect(page.locator('section[aria-labelledby="earlier-affiliations"]')).toContainText("Musicians and teachers of music");
  await expect(page.locator("main")).toContainText("Proceedings of the board appointed by director of OSS");
  await expect(page.locator("main")).toContainText("The Waterbury Democrat");

  const unit = p.immediate_pre_oss_affiliations[0];
  await page.goto(`./organizations/${unit.organization_id}/`);
  await expect(page.getByRole("heading", { name: "19th Communications Squadron", exact: true })).toBeVisible();
  await expect(page.getByRole("link", { name: "George Chrysostomas", exact: true })).toBeVisible();
});

test("Batch 414 publishes three identifier-backed occupation or student observations without employers", async ({ page }) => {
  for (const [id, name, relationship, occupation, date] of [
    ["d60c4476-a60e-5505-bcf7-43dcd7075eca", "John B Christopher", "unknown", "Teachers (secondary school) and principals", "22 August 1942"],
    ["4e1a4af5-4002-553a-9f2e-9eaffdb41950", "Paul P Christopher", "unknown", "Stenographers and typists", "7 May 1943"],
    ["aae3cf9d-f551-5260-82ad-2cb06d163ec2", "James H Chu", "student", "Student", "26 August 1943"],
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
      relationship_type: relationship,
      temporal_basis: "temporal_relation_uncertain",
      claim_confidence: "medium",
    });
    expect(p.other_pre_oss_affiliations[0].date_precision).toContain(date);
    await page.goto(`./people/${id}/`);
    await expect(page.getByRole("heading", { name, exact: true })).toBeVisible();
    await expect(page.locator('section[aria-labelledby="earlier-affiliations"]')).toContainText(occupation);
    await expect(page.locator('section[aria-labelledby="civilian-employer"]')).toContainText("No reliable pre-OSS employer");
  }
});

test("Batch 414 exposes Walter Chuckro's chronology problem and withholds the post-dissolution occupation", async ({ page }) => {
  const p = profile("49b02131-eb96-5862-bb2e-4f8937c7184f");
  expect(p.identity_status).toBe("high_confidence");
  expect(p.personnel_category).toBe("enlisted_army_personnel");
  expect(p.commissioned_officer).toBe(false);
  expect(p.research_status).toBe("needs_temporal_review");
  expect(p.archival_file.review_priority).toBe("critical");
  expect(p.immediate_pre_oss_affiliations).toEqual([]);
  expect(p.last_civilian_pre_service).toEqual([]);
  expect(p.other_pre_oss_affiliations).toEqual([]);
  expect(p.claims).toHaveLength(1);
  expect(p.claims[0].temporal_assessment).toContain("3 October 1945");

  await page.goto(`./people/${p.person_id}/`);
  await expect(page.getByRole("heading", { name: "Walter J Chuckro", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("20 September 1945");
  await expect(page.locator("main")).toContainText("OSS Records");
  await expect(page.locator("main")).not.toContainText("Sales clerks");
  await expect(page.locator("main")).not.toContainText("Westinghouse");
});

test("Batch 414 archive-routes five unresolved people and makes the full cohort searchable", async ({ page }) => {
  const unresolved = [
    ["3ef10c02-8817-524c-b40e-926d7062715a", null],
    ["615c3148-9819-53ed-89f1-6f758420a8e5", "••••3466"],
    ["4bc1f8f2-8a28-5071-900d-f10d8996e839", null],
    ["6c70ef83-5d5c-544d-9181-e5560d177460", null],
    ["b0e4df11-b504-5a1b-b5f5-5c101bcd9791", null],
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
    "John B Christopher",
    "Paul P Christopher",
    "Irma Christy",
    "Johnny E Christy",
    "Julia U Chromicz",
    "George Chrysostomas",
    "Evelyn S Chu",
    "James H Chu",
    "Thomas C Chubb",
    "Walter J Chuckro",
  ]) {
    await page.goto(`./people/?q=${encodeURIComponent(name)}`);
    await expect(page.getByRole("link", { name, exact: true })).toBeVisible();
  }
});
