import fs from "node:fs";
import { expect, test } from "@playwright/test";
import type { APIRequestContext } from "@playwright/test";

const evidence = JSON.parse(
  fs.readFileSync(
    new URL(
      "../../research/evidence-page303-luigi-mazzone-to-richard-j-mccann-review_batch-1048_2026-11-05.json",
      import.meta.url,
    ),
    "utf8",
  ),
);

const profiles = {
  luigi: ["36ddd41c-6c05-5bbc-ba32-e447e6705bf3", "Luigi Mazzone"],
  frederica: ["a75f2bdc-68ba-546c-9dde-d06899a32354", "Frederica McAfee"],
  williamMcAfee: ["d55bc229-2189-53f8-a66e-422b32f4c203", "William McAfee"],
  mcAragle: ["5925506f-0976-5138-9c6a-794f152a31d9", "William C McAragle"],
  turner: ["c5d22196-a119-55fd-8591-5d902531e84e", "Turner H McBaine"],
  mcAnolish: ["e497610e-712f-5f2d-941f-e559411bf199", "Nancy M McAnolish"],
  mcCandlish: ["5a051b4f-2624-52b8-adb9-9e2e50201832", "Nancy McCandlish"],
  dale: ["dc968a4e-3508-597e-a8db-67a84f1dbbb7", "Dale McAdoo"],
} as const;

async function publicPerson(request: APIRequestContext, [id, name]: readonly [string, string]) {
  const response = await request.get(`./data/people/${name[0].toLowerCase()}.json`);
  expect(response.ok()).toBeTruthy();
  return (await response.json()).find((item: { person_id: string }) => item.person_id === id);
}

test("Batch 1048 publishes all page 303 rows with terminal outcomes", async ({ request }) => {
  const people = [];
  for (const shard of [..."abcdefghijklmnopqrstuvw", "y", "z", "other"]) {
    const response = await request.get(`./data/people/${shard}.json`);
    expect(response.ok()).toBeTruthy();
    people.push(...(await response.json()).filter((person: { source_records: { pdf_page: number }[] }) =>
      person.source_records.some((row) => row.pdf_page === 303),
    ));
  }
  expect(people).toHaveLength(46);
  expect(people.flatMap((person: { source_records: { pdf_page: number }[] }) =>
    person.source_records.filter((row) => row.pdf_page === 303))).toHaveLength(46);
  for (const person of people) {
    expect(person.research_status).not.toBe("not_started");
    expect(person.research_status).not.toBe("in_progress");
  }
});

test("Luigi Mazzone separates a confirmed Navy pathway from his unnamed civilian employer", async ({ request, page }) => {
  const person = await publicPerson(request, profiles.luigi);
  expect(person).toMatchObject({
    identity_status: "confirmed",
    personnel_category: "enlisted_naval_personnel",
    research_status: "occupation_only_found",
  });
  expect(person.immediate_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      canonical_organization: "United States Navy",
      relationship_type: "military_assignment",
      temporal_basis: "explicit_immediate",
    }),
  ]);
  expect(person.last_civilian_pre_service).toEqual([
    expect.objectContaining({ canonical_organization: null, occupation: "truck driver" }),
  ]);
  await page.goto(`./people/${profiles.luigi[0]}/`);
  await expect(page.locator("main")).toContainText("truck driver");
});

test("Turner McBaine preserves immediate, last-civilian, and earlier law affiliations", async ({ request, page }) => {
  const person = await publicPerson(request, profiles.turner);
  expect(person).toMatchObject({
    identity_status: "confirmed",
    personnel_category: "commissioned_naval_officer",
    commissioned_officer: true,
    research_status: "verified_employer_found",
  });
  expect(person.immediate_pre_oss_affiliations).toEqual([
    expect.objectContaining({ canonical_organization: "United States Navy", relationship_type: "military_assignment" }),
  ]);
  expect(person.last_civilian_pre_service).toEqual([
    expect.objectContaining({ canonical_organization: "Law Office of John Francis Neylan", occupation: "attorney" }),
  ]);
  expect(person.other_pre_oss_affiliations).toEqual([
    expect.objectContaining({ canonical_organization: "Orrick, Palmer & Dahlquist", temporal_basis: "documented_prewar" }),
  ]);
  await page.goto(`./people/${profiles.turner[0]}/`);
  await expect(page.locator("main")).toContainText("Law Office of John Francis Neylan");
});

test("William McAfee separates China Theater, his unnamed last school, and earlier teaching", async ({ request, page }) => {
  const person = await publicPerson(request, profiles.williamMcAfee);
  expect(person).toMatchObject({ commissioned_officer: true, research_status: "documented_prewar_employer_found" });
  expect(person.immediate_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      organization_name_as_found: "China Theater headquarters",
      relationship_type: "military_assignment",
      temporal_basis: "explicit_immediate",
    }),
  ]);
  expect(person.last_civilian_pre_service).toEqual([
    expect.objectContaining({ organization_name_as_found: "local high school", occupation: "high-school teacher" }),
  ]);
  expect(person.other_pre_oss_affiliations).toEqual(expect.arrayContaining([
    expect.objectContaining({ canonical_organization: "Ewing Christian College", start_date: "1932", end_date: "1935" }),
  ]));
  await page.goto(`./people/${profiles.williamMcAfee[0]}/`);
  await expect(page.locator("main")).toContainText("Ewing Christian College");
});

test("Nancy McCandlish has a Smithsonian predecessor without transferring it to McAnolish", async ({ request, page }) => {
  const mcCandlish = await publicPerson(request, profiles.mcCandlish);
  expect(mcCandlish).toMatchObject({ identity_status: "high_confidence", research_status: "verified_employer_found" });
  expect(mcCandlish.immediate_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      canonical_organization: "Smithsonian Astrophysical Observatory",
      role_title: "Special Assistant to the Meteorologist",
      temporal_basis: "explicit_immediate",
    }),
  ]);
  expect(mcCandlish.last_civilian_pre_service).toHaveLength(1);

  const mcAnolish = await publicPerson(request, profiles.mcAnolish);
  expect(mcAnolish).toMatchObject({ identity_status: "ambiguous", research_status: "needs_identity_review" });
  expect(mcAnolish.immediate_pre_oss_affiliations).toHaveLength(0);
  expect(mcAnolish.last_civilian_pre_service).toHaveLength(0);
  expect(mcAnolish.other_pre_oss_affiliations).toHaveLength(0);
  await page.goto(`./people/${profiles.mcCandlish[0]}/`);
  await expect(page.locator("main")).toContainText("Smithsonian Astrophysical Observatory");
});

test("Frederica McAfee keeps WASP as qualified civilian government service", async ({ request, page }) => {
  const person = await publicPerson(request, profiles.frederica);
  expect(person).toMatchObject({
    commissioned_officer: false,
    personnel_category: "civilian_professional_or_administrative_grade",
    research_status: "needs_temporal_review",
  });
  expect(person.immediate_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      canonical_organization: "Women Airforce Service Pilots",
      relationship_type: "government_assignment",
      temporal_basis: "probable_immediate",
      claim_confidence: "medium",
    }),
  ]);
  await page.goto(`./people/${profiles.frederica[0]}/`);
  await expect(page.locator("main")).toContainText("Women Airforce Service Pilots");
});

test("McAragle conflict and Dale McAdoo identity-only evidence do not create affiliations", async ({ request }) => {
  for (const profile of [profiles.mcAragle, profiles.dale]) {
    const person = await publicPerson(request, profile);
    expect(person.immediate_pre_oss_affiliations).toHaveLength(0);
    expect(person.last_civilian_pre_service).toHaveLength(0);
    expect(person.other_pre_oss_affiliations).toHaveLength(0);
  }
  const mcAragle = await publicPerson(request, profiles.mcAragle);
  expect(mcAragle).toMatchObject({ identity_status: "ambiguous", research_status: "needs_identity_review" });
  const dale = await publicPerson(request, profiles.dale);
  expect(dale).toMatchObject({ identity_status: "probable", research_status: "requires_archival_review" });
});

test("Batch 1048 public assets omit protected identifiers", async ({ request }) => {
  const batchIds = new Set(evidence.person_updates.map((item: { person_id: string }) => item.person_id));
  const people = [];
  for (const shard of [..."abcdefghijklmnopqrstuvw", "y", "z", "other"]) {
    const response = await request.get(`./data/people/${shard}.json`);
    people.push(...(await response.json()).filter((person: { person_id: string }) => batchIds.has(person.person_id)));
  }
  expect(people).toHaveLength(43);
  const serialized = JSON.stringify(people);
  expect(serialized).not.toContain("candidate_identifier");
  expect(serialized).not.toContain("serial_number");
  expect(serialized).not.toContain("service_number");
  expect(serialized).not.toContain("bulk_record_ordinal");
});
