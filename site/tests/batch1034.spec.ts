import fs from "node:fs";
import { expect, test } from "@playwright/test";
import type { APIRequestContext } from "@playwright/test";

const evidence = fs.readFileSync(
  new URL(
    "../../research/evidence-page289-cyril-macleod-to-tore-maehle-review_batch-1034_2026-11-04.json",
    import.meta.url,
  ),
  "utf8",
);

const profiles = {
  macomber: ["e45d7180-6117-5e6d-9fd0-39f45bc46a53", "William B Macomber"],
  madison: ["522fe604-4f7b-50a4-8d5f-19aa1ad725f0", "Louis E Madison"],
  madson: ["cac58b1f-5ff9-590c-b399-3d831493fd99", "Max T Madson"],
  robertBox510: ["ac210fe4-e532-5413-990b-fc09d1a4e1ef", "Robert B MacLeod"],
  robertP7: ["2c9c428b-91e7-5b97-a6e3-6176c1b5cd73", "Robert B MacLeod"],
  robertDr: ["94c14a7e-15b8-522c-b58f-dc6feb24f43d", "Robert B MacLeod"],
} as const;

const batchShards = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "r", "s", "t", "w", "z"];

async function publicPerson(request: APIRequestContext, [id, name]: readonly [string, string]) {
  const response = await request.get(`./data/people/${name[0].toLowerCase()}.json`);
  expect(response.ok()).toBeTruthy();
  return (await response.json()).find((item: { person_id: string }) => item.person_id === id);
}

test("Batch 1034 publishes every page 289 row with a terminal outcome", async ({ request }) => {
  let people = 0;
  let sourceRows = 0;
  for (const letter of [..."abcdefghijklmnopqrstuvw", "y", "z", "other"]) {
    const response = await request.get(`./data/people/${letter}.json`);
    expect(response.ok()).toBeTruthy();
    for (const person of await response.json()) {
      const rows = person.source_records.filter((row: { pdf_page: number }) => row.pdf_page === 289);
      if (rows.length) {
        people += 1;
        sourceRows += rows.length;
        expect(person.research_status).not.toBe("not_started");
        expect(person.research_status).not.toBe("in_progress");
      }
    }
  }
  expect(people).toBe(46);
  expect(sourceRows).toBe(46);
});

test("William Macomber has a Marine predecessor and a separate Yale student record", async ({ request, page }) => {
  const person = await publicPerson(request, profiles.macomber);
  expect(person).toMatchObject({
    identity_status: "high_confidence",
    research_status: "completed",
    personnel_category: "commissioned_marine_corps_officer",
    commissioned_officer: true,
  });
  expect(person.immediate_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      canonical_organization: "United States Marine Corps Reserve",
      relationship_type: "military_assignment",
      temporal_basis: "explicit_immediate",
    }),
  ]);
  expect(person.last_civilian_pre_service).toHaveLength(0);
  expect(person.other_pre_oss_affiliations).toEqual([
    expect.objectContaining({ canonical_organization: "Yale University", relationship_type: "student" }),
  ]);
  await page.goto(`./people/${profiles.macomber[0]}/`);
  await expect(page.locator("main")).toContainText("United States Marine Corps Reserve");
  await expect(page.locator("main")).toContainText("Yale University");
});

test("Louis Madison separates Army, Department of Labor, and university pathways", async ({ request, page }) => {
  const person = await publicPerson(request, profiles.madison);
  expect(person).toMatchObject({ identity_status: "high_confidence", research_status: "verified_employer_found" });
  expect(person.immediate_pre_oss_affiliations).toEqual([
    expect.objectContaining({ canonical_organization: "United States Army", relationship_type: "military_assignment" }),
  ]);
  expect(person.last_civilian_pre_service).toEqual([
    expect.objectContaining({ canonical_organization: "U.S. Department of Labor", role_title: "economist" }),
  ]);
  expect(person.other_pre_oss_affiliations).toEqual([
    expect.objectContaining({ canonical_organization: "George Washington University", relationship_type: "student" }),
  ]);
  await page.goto(`./people/${profiles.madison[0]}/`);
  await expect(page.locator("main")).toContainText("U.S. Department of Labor");
  await expect(page.locator("main")).toContainText("United States Army");
  await expect(page.locator("main")).toContainText("George Washington University");
});

test("Max Madson has a qualified Agriculture employer but no asserted immediate predecessor", async ({ request, page }) => {
  const person = await publicPerson(request, profiles.madson);
  expect(person).toMatchObject({ identity_status: "high_confidence", research_status: "verified_employer_found" });
  expect(person.name_variants).toContain("Max T Madsen");
  expect(person.immediate_pre_oss_affiliations).toHaveLength(0);
  expect(person.last_civilian_pre_service).toEqual([
    expect.objectContaining({
      canonical_organization: "United States Department of Agriculture",
      role_title: "motion-picture projectionist and sound technician",
      temporal_basis: "strongly_date_bounded",
    }),
  ]);
  await page.goto(`./people/${profiles.madson[0]}/`);
  await expect(page.locator("main")).toContainText("United States Department of Agriculture");
  await expect(page.locator("main")).toContainText("motion-picture projectionist");
});

test("the three Robert MacLeod rows remain separate and evidence-free", async ({ request }) => {
  const people = await Promise.all([
    publicPerson(request, profiles.robertBox510),
    publicPerson(request, profiles.robertP7),
    publicPerson(request, profiles.robertDr),
  ]);
  expect(new Set(people.map((person) => person.person_id)).size).toBe(3);
  expect(new Set(people.map((person) => person.possible_duplicate_group)).size).toBe(1);
  for (const person of people) {
    expect(person).toMatchObject({ identity_status: "ambiguous", research_status: "needs_identity_review" });
    expect(person.immediate_pre_oss_affiliations).toHaveLength(0);
    expect(person.last_civilian_pre_service).toHaveLength(0);
    expect(person.other_pre_oss_affiliations).toHaveLength(0);
  }
});

test("Batch 1034 public assets do not expose protected identifiers", async ({ request }) => {
  const batch = JSON.parse(evidence);
  const batchIds = new Set(batch.person_updates.map((item: { person_id: string }) => item.person_id));
  const keys = new Set<string>();

  function collectKeys(value: unknown): void {
    if (Array.isArray(value)) {
      value.forEach(collectKeys);
    } else if (value && typeof value === "object") {
      for (const [key, child] of Object.entries(value)) {
        keys.add(key);
        collectKeys(child);
      }
    }
  }

  let peopleFound = 0;
  for (const shard of batchShards) {
    const response = await request.get(`./data/people/${shard}.json`);
    const people = (await response.json()).filter((person: { person_id: string }) => batchIds.has(person.person_id));
    peopleFound += people.length;
    people.forEach(collectKeys);
  }
  expect(peopleFound).toBe(45);
  expect(keys).not.toContain("candidate_identifier");
  expect(keys).not.toContain("serial_number");
  expect(keys).not.toContain("service_number");
  expect(keys).not.toContain("bulk_record_ordinal");
});
