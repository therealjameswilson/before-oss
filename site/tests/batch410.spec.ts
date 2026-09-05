import { expect, test } from "@playwright/test";
import fs from "node:fs";

const people = JSON.parse(fs.readFileSync(new URL("../src/data/generated/people.json", import.meta.url), "utf8"));
const profile = (id: string) => people.find((p: { person_id: string }) => p.person_id === id);

test("Batch 410 publishes Choukas's Dartmouth-to-OSS pathway with separate immediate and last-civilian claims", async ({ page }) => {
  const p = profile("286cbf50-c5be-5404-b433-33584b7c9a1e");
  expect(p.identity_status).toBe("high_confidence");
  expect(p.research_status).toBe("verified_employer_found");
  expect(p.source_records[0]).toMatchObject({ pdf_page: 80, box: "122", serial_masked: null });
  expect(p.immediate_pre_oss_affiliations).toHaveLength(1);
  expect(p.last_civilian_pre_service).toHaveLength(1);
  expect(p.immediate_pre_oss_affiliations[0]).toMatchObject({
    canonical_organization: "Dartmouth College",
    role_title: "Professor of Sociology",
    relationship_type: "employment",
    start_date: "1929",
    end_date: null,
    temporal_basis: "strongly_date_bounded",
    claim_confidence: "high",
  });
  expect(p.claims.map((claim: { claim_type: string }) => claim.claim_type).sort()).toEqual([
    "identity",
    "immediate_pre_oss_affiliation",
    "last_civilian_pre_service",
  ]);

  await page.goto(`./people/${p.person_id}/`);
  await expect(page.getByRole("heading", { name: "Michael E Choukas", exact: true })).toBeVisible();
  await expect(page.locator('section[aria-labelledby="immediate-affiliation"]')).toContainText("Dartmouth College");
  await expect(page.locator('section[aria-labelledby="civilian-employer"]')).toContainText("Dartmouth College");
  await expect(page.locator("main")).toContainText("Retiring Faculty");
  await expect(page.locator("main")).toContainText("Michael Choukas, Jr. '51: An Interview Conducted by Jane Carroll");
  await expect(page.locator("main")).toContainText("strongly date bounded");
});

test("Batch 410 qualifies Chopela's unnamed government pathway without inventing an agency or school employer", async ({ page }) => {
  const p = profile("9259225a-2f15-589e-ba5d-fe40f44baba4");
  expect(p.identity_status).toBe("probable");
  expect(p.research_status).toBe("requires_archival_review");
  expect(p.name_variants).toEqual(expect.arrayContaining(["Nancy Andrews", "Nancy Tsopelas"]));
  expect(p.immediate_pre_oss_affiliations).toHaveLength(1);
  expect(p.last_civilian_pre_service).toHaveLength(1);
  expect(p.immediate_pre_oss_affiliations[0]).toMatchObject({
    canonical_organization: "Unspecified United States federal agency",
    organization_name_as_found: "U.S. Government",
    relationship_type: "government_assignment",
    role_title: null,
    occupation: null,
    temporal_basis: "probable_immediate",
    identity_confidence: "probable",
    claim_confidence: "medium",
  });

  await page.goto(`./people/${p.person_id}/`);
  await expect(page.getByRole("heading", { name: "Nancy Chopela", exact: true })).toBeVisible();
  await expect(page.locator('section[aria-labelledby="immediate-affiliation"]')).toContainText("Unspecified United States federal agency");
  await expect(page.locator('section[aria-labelledby="civilian-employer"]')).toContainText("Unspecified United States federal agency");
  await expect(page.locator("main")).toContainText("probable immediate");
  await expect(page.locator("main")).toContainText("Nancy Andrews Obituary");
  await expect(page.locator("main")).not.toContainText("business college as employer");
});

test("Batch 410 distinguishes Stanley Choy's probable OSS identity from Chojnicki's unresolved Allied-military index record", async ({ page }) => {
  const stanley = profile("2e8e8232-d0ce-5c39-9319-4c9ecff60bf2");
  expect(stanley.identity_status).toBe("probable");
  expect(stanley.research_status).toBe("requires_archival_review");
  expect(stanley.immediate_pre_oss_affiliations).toEqual([]);
  expect(stanley.last_civilian_pre_service).toEqual([]);
  expect(stanley.claims).toHaveLength(1);
  expect(stanley.claims[0]).toMatchObject({ claim_type: "identity", claim_confidence: "medium", publication_status: "publish_qualified" });

  const waclaw = profile("309bceb3-860f-5ed0-98c3-667d46b24e7d");
  expect(waclaw.identity_status).toBe("unresolved");
  expect(waclaw.personnel_category).toBe("foreign_or_allied_military_personnel");
  expect(waclaw.commissioned_officer).toBe(false);
  expect(waclaw.allied_or_foreign_personnel).toBe(true);
  expect(waclaw.source_records[0]).toMatchObject({ pdf_page: 79, box: "122", rank_as_indexed: "Sgt", notes_as_indexed: "Polish Ar" });
  expect(waclaw.claims).toEqual([]);

  await page.goto(`./people/${stanley.person_id}/`);
  await expect(page.getByRole("heading", { name: "Stanley Choy", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("probable");
  await expect(page.locator("main")).toContainText("Independence Hall of Korea");
  await expect(page.locator('section[aria-labelledby="civilian-employer"]')).toContainText("No reliable pre-OSS employer");

  await page.goto(`./people/${waclaw.person_id}/`);
  await expect(page.getByRole("heading", { name: "Waclaw Chojnicki", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("foreign or allied military personnel");
  await expect(page.locator("main")).toContainText("Polish Ar");
});

test("Batch 410 archive-routes the six no-result identities and makes the complete cohort searchable", async ({ page }) => {
  const unresolved = [
    ["9ffc15bd-72c2-5e42-9465-a0ed8874ef47", "••••9767"],
    ["3ce9a3d9-2931-54e1-98c9-02660f290020", null],
    ["995adb69-a654-5165-9539-62747ba289ea", "••••2589"],
    ["2663104c-b24d-5f9b-8f99-1e03069d69f7", null],
    ["8cdf8f9f-b6fa-5590-8af0-54411b403936", "••••0014"],
    ["f9b5c7d6-c2cd-54b9-95eb-0af098f1db1f", null],
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
    "Waclaw Chojnicki",
    "Roger R Cholin",
    "Michael G Choma",
    "Bay Y Chong",
    "Nancy Chopela",
    "John Choptowich",
    "Michael E Choukas",
    "Alma H Choy",
    "Chin H Choy",
    "Stanley Choy",
  ]) {
    await page.goto(`./people/?q=${encodeURIComponent(name)}`);
    await expect(page.getByRole("link", { name, exact: true })).toBeVisible();
  }
});
