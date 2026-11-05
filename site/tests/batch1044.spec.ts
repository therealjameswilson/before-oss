import fs from "node:fs";
import { expect, test } from "@playwright/test";
import type { APIRequestContext } from "@playwright/test";

const evidence = JSON.parse(
  fs.readFileSync(
    new URL(
      "../../research/evidence-page299-nicholas-g-maslikosa-to-william-a-mathewson-review_batch-1044_2026-11-05.json",
      import.meta.url,
    ),
    "utf8",
  ),
);

const profiles = {
  nicholas: ["29c9d876-b149-5a52-8a77-8704e9398b73", "Nicholas G Maslikosa"],
  edwardMaslowsky: ["2bd2124f-a3c2-541e-be6d-1ce03721b3f1", "Edward S Maslowsky"],
  raymond: ["e6aaa1ce-31ca-5603-9321-0946e71ffaee", "Raymond K Masnaghetti"],
  edwardMason: ["e3b15c03-9d62-5a59-8ac0-117fe8e68bef", "Edward S Mason"],
  fred: ["21ac50fe-047a-5640-a78c-51f9ddfe35d4", "Fred M Mast Jr."],
  steve: ["699dc478-5ee2-5d00-a097-83b0b547ca48", "Steve J Mastros"],
  thomas: ["12186952-87d5-5b15-ab27-d16fbdb6494a", "Thomas Masuda"],
  brunislaw: ["1c51a5e9-b1f8-527e-8416-2f4ecb1c926a", "Brunislaw J Matejcak"],
  albert: ["94583f40-5aa1-5ff8-89cc-69b0a1cd96e2", "Albert R Materazzi"],
  elwood: ["0b1b7345-f31f-5c45-b270-9d9a6f27e151", "Elwood K Mathews"],
  eugene: ["5ae134b6-03a7-56fa-9a37-a6077ed848fe", "Eugene K Mathews"],
} as const;

async function publicPerson(request: APIRequestContext, [id, name]: readonly [string, string]) {
  const response = await request.get(`./data/people/${name[0].toLowerCase()}.json`);
  expect(response.ok()).toBeTruthy();
  return (await response.json()).find((item: { person_id: string }) => item.person_id === id);
}

test("Batch 1044 publishes all page 299 rows with terminal outcomes", async ({ request }) => {
  const people = [];
  for (const shard of [..."abcdefghijklmnopqrstuvw", "y", "z", "other"]) {
    const response = await request.get(`./data/people/${shard}.json`);
    expect(response.ok()).toBeTruthy();
    people.push(...(await response.json()).filter((person: { source_records: { pdf_page: number }[] }) =>
      person.source_records.some((row) => row.pdf_page === 299),
    ));
  }
  expect(people).toHaveLength(46);
  expect(people.flatMap((person: { source_records: { pdf_page: number }[] }) =>
    person.source_records.filter((row) => row.pdf_page === 299))).toHaveLength(46);
  for (const person of people) {
    expect(person.research_status).not.toBe("not_started");
    expect(person.research_status).not.toBe("in_progress");
  }
});

test("Materazzi separates his immediate Army pathway from qualified civilian employment", async ({ request, page }) => {
  const person = await publicPerson(request, profiles.albert);
  expect(person).toMatchObject({ identity_status: "confirmed", research_status: "verified_employer_found" });
  expect(person.immediate_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      canonical_organization: "United States Army Corps of Engineers",
      relationship_type: "military_assignment",
      temporal_basis: "strongly_date_bounded",
      claim_confidence: "high",
    }),
  ]);
  expect(person.last_civilian_pre_service).toEqual([
    expect.objectContaining({
      canonical_organization: "United States Army Map Service",
      role_title: "chemist",
      relationship_type: "employment",
      temporal_basis: "documented_prewar",
      claim_confidence: "medium",
    }),
  ]);
  await page.goto(`./people/${profiles.albert[0]}/`);
  await expect(page.locator("main")).toContainText("United States Army Corps of Engineers");
  await expect(page.locator("main")).toContainText("United States Army Map Service");
  await expect(page.locator("main")).toContainText("documented pre-OSS");
});

test("Army categories remain qualified and preserve reviewed name variants", async ({ request, page }) => {
  const raymond = await publicPerson(request, profiles.raymond);
  expect(raymond).toMatchObject({ identity_status: "confirmed", research_status: "occupation_only_found" });
  expect(raymond.other_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      canonical_organization: null,
      occupation: "semiskilled automobile-manufacturing worker, not elsewhere classified",
      claim_confidence: "medium",
    }),
  ]);

  const fred = await publicPerson(request, profiles.fred);
  expect(fred.other_pre_oss_affiliations).toEqual([
    expect.objectContaining({ canonical_organization: null, role_title: "student", relationship_type: "student" }),
  ]);

  const brunislaw = await publicPerson(request, profiles.brunislaw);
  expect(brunislaw.display_name).toBe("Brunislaw J Matejcak");
  expect(brunislaw.name_variants).toContain("Bronislaw J Matejczak");

  const elwood = await publicPerson(request, profiles.elwood);
  expect(elwood.name_variants).toContain("Elwood K Mathew");
  await page.goto(`./people/${profiles.elwood[0]}/`);
  await expect(page.locator("main")).toContainText("no employer, institution, or workplace is identified");
});

test("distinctive wartime identities do not invent pre-OSS employers", async ({ request, page }) => {
  for (const profile of [profiles.nicholas, profiles.edwardMaslowsky, profiles.steve]) {
    const person = await publicPerson(request, profile);
    expect(person).toMatchObject({ identity_status: "high_confidence", research_status: "requires_archival_review" });
    expect(person.immediate_pre_oss_affiliations).toHaveLength(0);
    expect(person.last_civilian_pre_service).toHaveLength(0);
    expect(person.other_pre_oss_affiliations).toHaveLength(0);
    await page.goto(`./people/${profile[0]}/`);
    await expect(page.locator("main")).toContainText("No reliable pre-OSS employer has yet been identified");
  }
});

test("ambiguous Thomas Masuda and rejected Eugene Mathews candidates transfer no affiliations", async ({ request, page }) => {
  const thomas = await publicPerson(request, profiles.thomas);
  expect(thomas).toMatchObject({ identity_status: "ambiguous", research_status: "needs_identity_review" });
  expect(thomas.immediate_pre_oss_affiliations).toHaveLength(0);
  expect(thomas.last_civilian_pre_service).toHaveLength(0);
  expect(thomas.other_pre_oss_affiliations).toHaveLength(0);

  const eugene = await publicPerson(request, profiles.eugene);
  expect(eugene).toMatchObject({ identity_status: "ambiguous", research_status: "needs_identity_review" });
  expect(eugene.other_pre_oss_affiliations).toHaveLength(0);
  await page.goto(`./people/${profiles.eugene[0]}/`);
  await expect(page.locator("main")).toContainText("Evidence conflicts");
  await expect(page.locator("main")).toContainText("protected identifiers conflict");
});

test("Edward Mason keeps previously verified evidence without duplicate affiliations", async ({ request, page }) => {
  const person = await publicPerson(request, profiles.edwardMason);
  expect(person).toMatchObject({ identity_status: "high_confidence", research_status: "verified_employer_found" });
  expect(person.immediate_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      canonical_organization: "U.S. Office of Production Management",
      historical_organization: "Office of Production Management",
    }),
  ]);
  expect(person.last_civilian_pre_service).toEqual([
    expect.objectContaining({ canonical_organization: "Harvard University" }),
  ]);
  expect(person.immediate_pre_oss_affiliations).toHaveLength(1);
  expect(person.last_civilian_pre_service).toHaveLength(1);
  await page.goto(`./people/${profiles.edwardMason[0]}/`);
  await expect(page.locator("main")).toContainText("Office of Production Management");
  await expect(page.locator("main")).toContainText("Harvard University");
});

test("Batch 1044 public assets omit protected identifiers", async ({ request }) => {
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
