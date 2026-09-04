import { expect, test } from "@playwright/test";
import fs from "node:fs";

const people = JSON.parse(fs.readFileSync(new URL("../src/data/generated/people.json", import.meta.url), "utf8"));
const profile = (id: string) => people.find((person: { person_id: string }) => person.person_id === id);
const unresolved = [
  ["5faa9147-8024-5d4d-b519-68c70e183dfb", "Margaret I Chase", "119"],
  ["98a32940-848a-5a1d-b700-e294ac13867e", "William D Chase", "119"],
  ["160a50c5-4861-56c7-9423-8b8c4457c645", "Fred A Chastain", "119"],
  ["8e320ce1-8b48-5dbf-a2e5-38c9ff971f87", "John P Chastain", "119"],
  ["9f0e80b1-b3e4-5c23-b592-e6969921dcb1", "Ruth Chastain", "119"],
  ["44114aef-c7b3-594a-963b-30d772df8e5d", "Clothilde Chatelan", "119"],
  ["85beeed9-070e-5fc6-b6b2-a00ba5d82873", "Diane L Chatelan", "119"],
  ["d9d46acc-02eb-5517-a3ad-e0079a305145", "Charles W Chattaway", "120"],
  ["2616ca43-44b8-5063-98de-cc06c7e7f6f7", "Arthur A Chattillion", "120"],
];

test("Batch 401 preserves nine unresolved identities and the Box 119 to 120 boundary", async ({ page }) => {
  for (const [id, name, box] of unresolved) {
    const person = profile(id);
    expect(person.display_name).toBe(name);
    expect(person.identity_status).toBe("unresolved");
    expect(person.research_status).toBe("requires_archival_review");
    expect(person.research_attempt_count).toBeGreaterThan(0);
    expect(person.claims).toEqual([]);
    expect(person.source_records[0]).toMatchObject({
      pdf_page: 78, box, archive_location: box === "119" ? "230/86/28/05" : "230/86/28/06",
    });
    await page.goto(`./people/${id}/`);
    await expect(page.getByRole("heading", { name, exact: true })).toBeVisible();
    await expect(page.locator("main")).toContainText(`Box ${box}`);
    await expect(page.locator("main")).toContainText("No reliable pre-OSS employer has yet been identified in the accessible sources reviewed.");
    await expect(page.locator(".affiliation-card")).toHaveCount(0);
  }
  expect(profile("160a50c5-4861-56c7-9423-8b8c4457c645").commissioned_officer).toBe(true);
});

test("Batch 401 dates Chatellier's occupational observation without inventing an employer or OSS rank", async ({ page }) => {
  const id = "839ae1ff-71f1-577e-b54b-21c572f61f9c";
  const person = profile(id);
  expect(person.display_name).toBe("Rene Chatellier");
  expect(person.name_variants).toContain("Rene A. Chatellier");
  expect(person.identity_status).toBe("high_confidence");
  expect(person.commissioned_officer).toBeNull();
  expect(person.source_records[0].rank_as_indexed).toBeNull();
  expect(person.source_records[0].indexed_middle).toBeNull();
  expect(person.source_records[0].serial_masked).toMatch(/^••••[A-Z0-9]{4}$/);
  expect(person.immediate_pre_oss_affiliations).toEqual([]);
  expect(person.last_civilian_pre_service).toEqual([]);
  expect(person.other_pre_oss_affiliations).toHaveLength(1);
  expect(person.other_pre_oss_affiliations[0]).toMatchObject({
    occupation: "Bartenders", relationship_type: "unknown", organization_id: null,
    temporal_basis: "temporal_relation_uncertain", claim_confidence: "medium",
  });
  expect(person.claims).toHaveLength(2);
  for (const claim of person.claims) expect(claim.sources.length).toBeGreaterThan(0);
  await page.goto(`./people/${id}/`);
  const occupation = page.locator('section[aria-labelledby="earlier-affiliations"] .affiliation-card');
  await expect(occupation).toContainText("Bartenders");
  await expect(occupation).toContainText("Recorded at 1944-03-21");
  await expect(occupation).not.toContainText("Through 1944-03-21");
  await expect(page.locator('section[aria-labelledby="civilian-employer"]')).toContainText("No reliable pre-OSS employer has yet been identified");
});

test("Batch 401 searches the documented Army initial without rewriting the indexed name", async ({ page }) => {
  await page.goto("./people/");
  await page.getByRole("searchbox", { name: "Search", exact: true }).fill("Rene A Chatellier");
  await expect(page.getByRole("link", { name: "Rene Chatellier", exact: true })).toBeVisible();
});
