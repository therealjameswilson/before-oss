import fs from "node:fs";
import { expect, test } from "@playwright/test";
import type { APIRequestContext } from "@playwright/test";

const evidence = JSON.parse(
  fs.readFileSync(
    new URL(
      "../../research/evidence-page295-laura-margulas-to-richard-s-marnocaa-review_batch-1040_2026-11-05.json",
      import.meta.url,
    ),
    "utf8",
  ),
);

const profiles = {
  maritz: ["58effa7e-349b-5864-be24-3568512448d8", "Raymond E Maritz"],
  markotny: ["9bc573d5-c28f-575b-8290-35f6802cd70a", "Antoni Markotny"],
  markoutsas: ["929854ef-6184-51c7-9c61-1910d009b617", "George C Markoutsas"],
  marlin: ["d2b1e446-e325-5ef6-b740-65e7ee92d2f1", "Ervin R Marlin"],
  marmande: ["3e7ecf52-360f-5ed5-9776-788d6e229496", "Raymond-Jea Marmande"],
  marketos: ["2156cb61-8bc8-5755-a2bb-73727da4d659", "Dennis A Marketos"],
  marnocaa: ["5f2ac5f3-3165-5f9a-8773-de9beda50d77", "Richard S Marnocaa"],
  marinelli: ["730e0d7f-d180-5bbe-ac72-d71f79439be9", "Carmel C Marinelli"],
  marks: ["dd2784b6-c932-5e2d-853b-f3ac1692f014", "Robert B Marks"],
} as const;

async function publicPerson(request: APIRequestContext, [id, name]: readonly [string, string]) {
  const response = await request.get(`./data/people/${name[0].toLowerCase()}.json`);
  expect(response.ok()).toBeTruthy();
  return (await response.json()).find((item: { person_id: string }) => item.person_id === id);
}

test("Batch 1040 publishes all page 295 rows with terminal outcomes", async ({ request }) => {
  const people = [];
  for (const shard of [..."abcdefghijklmnopqrstuvw", "y", "z", "other"]) {
    const response = await request.get(`./data/people/${shard}.json`);
    expect(response.ok()).toBeTruthy();
    people.push(...(await response.json()).filter((person: { source_records: { pdf_page: number }[] }) =>
      person.source_records.some((row) => row.pdf_page === 295),
    ));
  }
  expect(people).toHaveLength(46);
  expect(people.flatMap((person: { source_records: { pdf_page: number }[] }) =>
    person.source_records.filter((row) => row.pdf_page === 295))).toHaveLength(46);
  for (const person of people) {
    expect(person.research_status).not.toBe("not_started");
    expect(person.research_status).not.toBe("in_progress");
  }
});

test("Raymond Maritz publishes the explicit firm-to-OSS transition", async ({ request, page }) => {
  const maritz = await publicPerson(request, profiles.maritz);
  expect(maritz).toMatchObject({ identity_status: "high_confidence", research_status: "verified_employer_found" });
  expect(maritz.immediate_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      canonical_organization: "Maritz, Young and Dusard",
      relationship_type: "employment",
      immediate_pre_oss: true,
      last_civilian_pre_service: true,
      temporal_basis: "explicit_immediate",
    }),
  ]);
  await page.goto(`./people/${profiles.maritz[0]}/`);
  await expect(page.locator("main")).toContainText("Maritz, Young and Dusard");
  await expect(page.locator("main")).toContainText("left the firm in 1942 to join OSS");
});

test("George Markoutsas remains an Army pathway, not a civilian employer", async ({ request, page }) => {
  const person = await publicPerson(request, profiles.markoutsas);
  expect(person).toMatchObject({ identity_status: "confirmed", research_status: "completed" });
  expect(person.immediate_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      canonical_organization: "United States Army",
      relationship_type: "military_assignment",
      last_civilian_pre_service: false,
    }),
  ]);
  expect(person.last_civilian_pre_service).toHaveLength(0);
  await page.goto(`./people/${profiles.markoutsas[0]}/`);
  await expect(page.locator("main")).toContainText("September 1942");
  await expect(page.locator("main")).toContainText("October 1943");
});

test("Ervin Marlin separates FSA employment from Trinity student status", async ({ request, page }) => {
  const marlin = await publicPerson(request, profiles.marlin);
  expect(marlin).toMatchObject({ identity_status: "confirmed", research_status: "verified_employer_found" });
  expect(marlin.last_civilian_pre_service).toEqual([
    expect.objectContaining({
      canonical_organization: "United States Federal Security Agency",
      relationship_type: "government_assignment",
    }),
  ]);
  expect(marlin.other_pre_oss_affiliations).toEqual([
    expect.objectContaining({ canonical_organization: "Trinity College Dublin", relationship_type: "student" }),
  ]);
  await page.goto(`./people/${profiles.marlin[0]}/`);
  await expect(page.locator("main")).toContainText("Federal Security Agency");
  await expect(page.locator("main")).toContainText("Student status remains separate from employment");
});

test("identity-only mission evidence does not invent employers", async ({ request }) => {
  const markotny = await publicPerson(request, profiles.markotny);
  const marmande = await publicPerson(request, profiles.marmande);
  for (const person of [markotny, marmande]) {
    expect(person.immediate_pre_oss_affiliations).toHaveLength(0);
    expect(person.last_civilian_pre_service).toHaveLength(0);
    expect(person.other_pre_oss_affiliations).toHaveLength(0);
    expect(person.claims).toEqual([expect.objectContaining({ claim_type: "identity" })]);
  }
  expect(marmande.name_variants).toEqual(expect.arrayContaining(["Raymond Marmande", "Jacques Larcy"]));
});

test("undefined and late Army codes remain identity-only", async ({ request }) => {
  const undefinedCode = await publicPerson(request, profiles.marinelli);
  const lateEntry = await publicPerson(request, profiles.marks);
  for (const person of [undefinedCode, lateEntry]) {
    expect(person.other_pre_oss_affiliations).toHaveLength(0);
    expect(person.claims).toEqual([expect.objectContaining({ claim_type: "identity" })]);
  }
  expect(undefinedCode.claims[0].evidence_paraphrase).toContain("code 999");
  expect(lateEntry.claims[0].evidence_paraphrase).toContain("1945");
});

test("Marketos and Marnocaa conflicts remain visible and unmerged", async ({ request, page }) => {
  const marketos = await publicPerson(request, profiles.marketos);
  expect(marketos).toMatchObject({ identity_status: "conflicting", research_status: "conflicting_sources" });
  expect(marketos.claims).toHaveLength(0);
  const marnocaa = await publicPerson(request, profiles.marnocaa);
  expect(marnocaa).toMatchObject({ identity_status: "ambiguous", research_status: "needs_identity_review" });
  expect(marnocaa.possible_duplicate_group).toBeTruthy();
  await page.goto(`./people/${profiles.marnocaa[0]}/`);
  await expect(page.locator("main")).toContainText("Marnocaa");
  await expect(page.locator("main")).toContainText("No merge was made");
});

test("Batch 1040 public assets omit protected identifiers", async ({ request }) => {
  const batchIds = new Set(evidence.person_updates.map((item: { person_id: string }) => item.person_id));
  const people = [];
  for (const shard of [..."abcdefghijklmnopqrstuvw", "y", "z", "other"]) {
    const response = await request.get(`./data/people/${shard}.json`);
    people.push(...(await response.json()).filter((person: { person_id: string }) => batchIds.has(person.person_id)));
  }
  expect(people).toHaveLength(46);
  const serialized = JSON.stringify(people);
  expect(serialized).not.toContain("candidate_identifier");
  expect(serialized).not.toContain("serial_number");
  expect(serialized).not.toContain("service_number");
  expect(serialized).not.toContain("bulk_record_ordinal");
});
