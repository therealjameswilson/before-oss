import fs from "node:fs";
import { expect, test } from "@playwright/test";
import type { APIRequestContext } from "@playwright/test";

const evidence = fs.readFileSync(
  new URL(
    "../../research/evidence-page512-william-wolverton-to-william-wood-review_batch-1022_2026-11-04.json",
    import.meta.url,
  ),
  "utf8",
);

const profiles = {
  pakHoyWong: ["52eadd18-6063-5dd3-aaf1-82fbde9d6243", "Pak Hoy Wong"],
  raymondWong: ["a0f8c55f-c8c4-5e3b-8b45-33cb34318f30", "Raymond T Wong"],
  shenWong: ["59e7eeb9-6bc4-516d-b4f2-4e98bee6508e", "Shen T Wong"],
  shewWong: ["51f077a2-c1d2-5504-9917-8b4448140944", "Shew T Wong"],
  williamWood: ["a699fb3f-fdb2-5f46-b13f-787bda39291e", "William D Wood"],
} as const;

async function publicPerson(request: APIRequestContext, [id, name]: readonly [string, string]) {
  const response = await request.get(`./data/people/${name[0].toLowerCase()}.json`);
  expect(response.ok()).toBeTruthy();
  return (await response.json()).find((item: { person_id: string }) => item.person_id === id);
}

test("Batch 1022 publishes every page 512 row with a terminal outcome", async ({ request }) => {
  let sourceRows = 0;
  let people = 0;
  for (const letter of [..."abcdefghijklmnopqrstuvw", "y", "z", "other"]) {
    const response = await request.get(`./data/people/${letter}.json`);
    expect(response.ok()).toBeTruthy();
    for (const person of await response.json()) {
      const rows = person.source_records.filter((row: { pdf_page: number }) => row.pdf_page === 512);
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

test("qualified Army occupations stay separate from employers", async ({ request, page }) => {
  const pak = await publicPerson(request, profiles.pakHoyWong);
  expect(pak).toMatchObject({
    identity_status: "high_confidence",
    research_status: "occupation_only_found",
    personnel_category: "enlisted_army_personnel",
    commissioned_officer: false,
  });
  expect(pak.immediate_pre_oss_affiliations).toHaveLength(0);
  expect(pak.last_civilian_pre_service).toHaveLength(0);
  expect(pak.other_pre_oss_affiliations).toEqual([
    expect.objectContaining({ relationship_type: "student", occupation: "student" }),
  ]);

  const raymond = await publicPerson(request, profiles.raymondWong);
  expect(raymond.other_pre_oss_affiliations).toEqual([
    expect.objectContaining({ relationship_type: "unknown", occupation: "shipping and receiving clerk" }),
  ]);

  const william = await publicPerson(request, profiles.williamWood);
  expect(william.other_pre_oss_affiliations).toEqual([
    expect.objectContaining({ occupation: "salesman to consumers" }),
  ]);

  await page.goto(`./people/${profiles.pakHoyWong[0]}/`);
  await expect(page.getByRole("heading", { name: "Pak Hoy Wong", level: 1 })).toBeVisible();
  await expect(page.locator("main")).toContainText("student");
});

test("Shen and Shew Wong remain separate and visibly conflicting", async ({ request }) => {
  const shen = await publicPerson(request, profiles.shenWong);
  const shew = await publicPerson(request, profiles.shewWong);
  expect(shen.person_id).not.toBe(shew.person_id);
  for (const person of [shen, shew]) {
    expect(person).toMatchObject({
      identity_status: "conflicting",
      research_status: "conflicting_sources",
    });
    expect(person.possible_duplicate_group).toBeTruthy();
    expect(person.immediate_pre_oss_affiliations).toHaveLength(0);
    expect(person.last_civilian_pre_service).toHaveLength(0);
    expect(person.other_pre_oss_affiliations).toHaveLength(0);
  }
  expect(shen.possible_duplicate_group).toBe(shew.possible_duplicate_group);
});

test("Batch 1022 evidence excludes secrets, identifiers, and raw bulk records", () => {
  expect(evidence).not.toMatch(/"serial_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toMatch(/"service_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toContain("NARA_API_KEY");
  expect(evidence).not.toContain("x-api-key");
  expect(evidence).not.toContain("candidate_identifier");
  expect(evidence).not.toContain("bulk_record_ordinal");
});
