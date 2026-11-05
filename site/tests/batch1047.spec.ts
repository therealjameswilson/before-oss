import fs from "node:fs";
import { expect, test } from "@playwright/test";
import type { APIRequestContext } from "@playwright/test";

const evidence = JSON.parse(
  fs.readFileSync(
    new URL(
      "../../research/evidence-page302-philip-j-may-to-richard-mazzarini-review_batch-1047_2026-11-05.json",
      import.meta.url,
    ),
    "utf8",
  ),
);

const profiles = {
  ferdinand: ["0d58cfda-8870-5c0f-b2c7-99a365b7bf6f", "Ferdinand L Mayer"],
  gerald: ["c9d1224d-f4ac-5986-89d5-f6ee1298f16a", "Gerald Mayer"],
  wendell: ["e427752f-defe-51c2-b1dc-08d13ea506a4", "Wendell Mayfield"],
  bruce: ["04ebeaae-03df-5556-815a-3545177194e0", "Bruce H Mazlish"],
  jean: ["4a51ec7d-3141-5884-9773-c23e902857fa", "Jean Mazou"],
  chester: ["5a4777cc-80f6-5cab-92c1-41f3ea95184b", "Chester John Mazur"],
  riccardo: ["5688a930-b4d5-514a-a5f7-a48ada4c54dd", "Riccardo Mazzarini"],
  richard: ["383c4058-6918-5a5b-a35e-28dd71fd07bb", "Richard Mazzarini"],
} as const;

async function publicPerson(request: APIRequestContext, [id, name]: readonly [string, string]) {
  const response = await request.get(`./data/people/${name[0].toLowerCase()}.json`);
  expect(response.ok()).toBeTruthy();
  return (await response.json()).find((item: { person_id: string }) => item.person_id === id);
}

test("Batch 1047 publishes all page 302 rows with terminal outcomes", async ({ request }) => {
  const people = [];
  for (const shard of [..."abcdefghijklmnopqrstuvw", "y", "z", "other"]) {
    const response = await request.get(`./data/people/${shard}.json`);
    expect(response.ok()).toBeTruthy();
    people.push(...(await response.json()).filter((person: { source_records: { pdf_page: number }[] }) =>
      person.source_records.some((row) => row.pdf_page === 302),
    ));
  }
  expect(people).toHaveLength(46);
  expect(people.flatMap((person: { source_records: { pdf_page: number }[] }) =>
    person.source_records.filter((row) => row.pdf_page === 302))).toHaveLength(46);
  for (const person of people) {
    expect(person.research_status).not.toBe("not_started");
    expect(person.research_status).not.toBe("in_progress");
  }
});

test("Ferdinand Mayer keeps a dated government assignment separate from immediate affiliation", async ({ request, page }) => {
  const person = await publicPerson(request, profiles.ferdinand);
  expect(person).toMatchObject({ identity_status: "high_confidence", research_status: "documented_prewar_employer_found" });
  expect(person.immediate_pre_oss_affiliations).toHaveLength(0);
  expect(person.last_civilian_pre_service).toHaveLength(0);
  expect(person.other_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      canonical_organization: "United States Department of State",
      relationship_type: "government_assignment",
      temporal_basis: "documented_prewar",
    }),
  ]);
  await page.goto(`./people/${profiles.ferdinand[0]}/`);
  await expect(page.locator("main")).toContainText("Ferdinand Lathrop Mayer");
  await expect(page.locator("main")).toContainText("Ambassador to Haiti");
});

test("Bruce Mazlish shows Columbia as student status rather than employment", async ({ request, page }) => {
  const person = await publicPerson(request, profiles.bruce);
  expect(person).toMatchObject({ identity_status: "high_confidence", research_status: "completed" });
  expect(person.last_civilian_pre_service).toHaveLength(0);
  expect(person.other_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      canonical_organization: "Columbia University",
      relationship_type: "student",
    }),
  ]);
  await page.goto(`./people/${profiles.bruce[0]}/`);
  await expect(page.locator("main")).toContainText("student status, not employment");
});

test("Wendell Mayfield publishes direct naval identity evidence but no employer", async ({ request, page }) => {
  const person = await publicPerson(request, profiles.wendell);
  expect(person).toMatchObject({
    identity_status: "confirmed",
    personnel_category: "enlisted_naval_personnel",
    research_status: "requires_archival_review",
  });
  expect(person.immediate_pre_oss_affiliations).toHaveLength(0);
  expect(person.last_civilian_pre_service).toHaveLength(0);
  expect(person.other_pre_oss_affiliations).toHaveLength(0);
  await page.goto(`./people/${profiles.wendell[0]}/`);
  await expect(page.locator("main")).toContainText("Chief Yeoman Wendell Mayfield");
});

test("Richard Mazzarini has a qualified Pan American pathway without transfer to Riccardo", async ({ request, page }) => {
  const richard = await publicPerson(request, profiles.richard);
  expect(richard).toMatchObject({ identity_status: "high_confidence", research_status: "documented_prewar_employer_found" });
  expect(richard.immediate_pre_oss_affiliations).toHaveLength(0);
  expect(richard.last_civilian_pre_service).toEqual([
    expect.objectContaining({
      canonical_organization: "Pan American Airways",
      relationship_type: "employment",
      claim_confidence: "medium",
      temporal_basis: "probable_immediate",
    }),
  ]);

  const riccardo = await publicPerson(request, profiles.riccardo);
  expect(riccardo).toMatchObject({ identity_status: "ambiguous", research_status: "needs_identity_review" });
  expect(riccardo.immediate_pre_oss_affiliations).toHaveLength(0);
  expect(riccardo.last_civilian_pre_service).toHaveLength(0);
  expect(riccardo.other_pre_oss_affiliations).toHaveLength(0);
  await page.goto(`./people/${profiles.riccardo[0]}/`);
  await expect(page.locator("main")).toContainText("Evidence conflicts");
});

test("unbridged Gerald Mayer and Jean Mazou candidates remain unpublished", async ({ request }) => {
  for (const profile of [profiles.gerald, profiles.jean]) {
    const person = await publicPerson(request, profile);
    expect(person.research_status).toBe("needs_identity_review");
    expect(person.immediate_pre_oss_affiliations).toHaveLength(0);
    expect(person.last_civilian_pre_service).toHaveLength(0);
    expect(person.other_pre_oss_affiliations).toHaveLength(0);
  }
});

test("accepted Army bridge remains a qualified broad occupation", async ({ request, page }) => {
  const person = await publicPerson(request, profiles.chester);
  expect(person).toMatchObject({ identity_status: "high_confidence", research_status: "occupation_only_found" });
  expect(person.name_variants).toContain("Chester J Mazur");
  expect(person.other_pre_oss_affiliations).toEqual([
    expect.objectContaining({ canonical_organization: null, occupation: "machinist", claim_confidence: "medium" }),
  ]);
  await page.goto(`./people/${profiles.chester[0]}/`);
  await expect(page.locator("main")).toContainText("machinist");
});

test("Batch 1047 public assets omit protected identifiers", async ({ request }) => {
  const batchIds = new Set(evidence.person_updates.map((item: { person_id: string }) => item.person_id));
  const people = [];
  for (const shard of [..."abcdefghijklmnopqrstuvw", "y", "z", "other"]) {
    const response = await request.get(`./data/people/${shard}.json`);
    people.push(...(await response.json()).filter((person: { person_id: string }) => batchIds.has(person.person_id)));
  }
  expect(people).toHaveLength(44);
  const serialized = JSON.stringify(people);
  expect(serialized).not.toContain("candidate_identifier");
  expect(serialized).not.toContain("serial_number");
  expect(serialized).not.toContain("service_number");
  expect(serialized).not.toContain("bulk_record_ordinal");
});

