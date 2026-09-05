import { expect, test } from "@playwright/test";
import fs from "node:fs";

const people = JSON.parse(fs.readFileSync(new URL("../src/data/generated/people.json", import.meta.url), "utf8"));
const profile = (id: string) => people.find((p: { person_id: string }) => p.person_id === id);

test("Batch 412 publishes Chester Christian's bounded Army occupation without inventing an employer", async ({ page }) => {
  const p = profile("7085f9b3-3619-5a74-9cc1-7f257d556eb5");
  expect(p.identity_status).toBe("high_confidence");
  expect(p.personnel_category).toBe("enlisted_army_personnel");
  expect(p.commissioned_officer).toBe(false);
  expect(p.research_status).toBe("occupation_only_found");
  expect(p.source_records[0]).toMatchObject({ pdf_page: 80, box: "123", rank_as_indexed: null, serial_masked: "••••8994" });
  expect(p.immediate_pre_oss_affiliations).toEqual([]);
  expect(p.last_civilian_pre_service).toEqual([]);
  expect(p.other_pre_oss_affiliations).toHaveLength(1);
  expect(p.other_pre_oss_affiliations[0]).toMatchObject({
    occupation: "Mechanics and repairmen, motor vehicle",
    organization_id: null,
    relationship_type: "unknown",
    temporal_basis: "temporal_relation_uncertain",
    claim_confidence: "medium",
  });
  expect(p.other_pre_oss_affiliations[0].date_precision).toContain("18 August 1942");

  await page.goto(`./people/${p.person_id}/`);
  await expect(page.getByRole("heading", { name: "Chester Christian", exact: true })).toBeVisible();
  await expect(page.locator('section[aria-labelledby="earlier-affiliations"]')).toContainText("Mechanics and repairmen, motor vehicle");
  await expect(page.locator('section[aria-labelledby="civilian-employer"]')).toContainText("No reliable pre-OSS employer");
  await expect(page.locator("main")).toContainText("NARA Compiled Code Lists");
});

test("Batch 412 archive-routes nine unresolved people and makes the full cohort searchable", async ({ page }) => {
  const unresolved = [
    ["296b8c7b-39f5-5f9e-b466-6ede25dd65bb", null],
    ["42ec43a6-4500-5f8b-93b2-193505e89373", "••••6365"],
    ["a98a7125-36d5-5b8e-a1f2-08af0df985a7", null],
    ["d62bea84-9927-56eb-bea3-85bcaacb8a56", "••••6276"],
    ["3ee6de4e-28a6-5233-8f76-e8db9dc7d05e", "••••6330"],
    ["6d832286-c55f-5be6-9f99-26e8409064a2", "••••5268"],
    ["ff62a50d-8c0d-557d-834d-83c4754c58da", null],
    ["2542fe23-2730-5b14-9537-7bb5c27de4a0", null],
    ["938d5933-875c-546d-8aac-112acda1ac2b", null],
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
    "Geoffrey Christensen",
    "Hal S Christensen",
    "Lillian D Christensen",
    "Norris A Christensen",
    "Robert J Christensen",
    "Sverre H Christensen",
    "Christian R Christenson",
    "Chester Christian",
    "Louise E Christian",
    "Mary W Christian",
  ]) {
    await page.goto(`./people/?q=${encodeURIComponent(name)}`);
    await expect(page.getByRole("link", { name, exact: true })).toBeVisible();
  }
});
