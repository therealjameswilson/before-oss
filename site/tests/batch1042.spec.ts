import fs from "node:fs";
import { expect, test } from "@playwright/test";
import type { APIRequestContext } from "@playwright/test";

const evidence = JSON.parse(
  fs.readFileSync(
    new URL(
      "../../research/evidence-page297-paul-p-martaus-to-maurice-martin-review_batch-1042_2026-11-05.json",
      import.meta.url,
    ),
    "utf8",
  ),
);

const profiles = {
  paulette: ["6e1c800f-7073-58d8-bcbb-1bb9025f81f3", "Paulette Marteliere"],
  garibaldi: ["3bfc4bdc-8f86-559b-9884-9efa72fdd50b", "Garibaldi Martellacci"],
  kaj: ["3fd6a1f7-cb2f-51fa-8559-2ab8092b1302", "Kaj Martens"],
  charlesH: ["23f24acd-cbd9-5652-bcb3-2ee847ee0481", "Charles H Martin"],
  edwin: ["ac722df1-5455-58ba-8abf-a5f8b0573e8b", "Edwin M Martin"],
  frank: ["55683b32-543b-51ff-b02b-c111cdcf95b3", "Frank J Martel"],
  maurice: ["60e23c0a-3f2d-543c-a035-e9b42a80eb6b", "Maurice Martin"],
} as const;

async function publicPerson(request: APIRequestContext, [id, name]: readonly [string, string]) {
  const response = await request.get(`./data/people/${name[0].toLowerCase()}.json`);
  expect(response.ok()).toBeTruthy();
  return (await response.json()).find((item: { person_id: string }) => item.person_id === id);
}

test("Batch 1042 publishes all page 297 rows with terminal outcomes", async ({ request }) => {
  const people = [];
  for (const shard of [..."abcdefghijklmnopqrstuvw", "y", "z", "other"]) {
    const response = await request.get(`./data/people/${shard}.json`);
    expect(response.ok()).toBeTruthy();
    people.push(...(await response.json()).filter((person: { source_records: { pdf_page: number }[] }) =>
      person.source_records.some((row) => row.pdf_page === 297),
    ));
  }
  expect(people).toHaveLength(46);
  expect(people.flatMap((person: { source_records: { pdf_page: number }[] }) =>
    person.source_records.filter((row) => row.pdf_page === 297))).toHaveLength(46);
  for (const person of people) {
    expect(person.research_status).not.toBe("not_started");
    expect(person.research_status).not.toBe("in_progress");
  }
});

test("Garibaldi Martellacci separates the named Mazzini affiliation from an unnamed shoe factory", async ({ request, page }) => {
  const person = await publicPerson(request, profiles.garibaldi);
  expect(person).toMatchObject({ identity_status: "confirmed", research_status: "occupation_only_found" });
  expect(person.immediate_pre_oss_affiliations).toHaveLength(0);
  expect(person.last_civilian_pre_service).toHaveLength(0);
  expect(person.other_pre_oss_affiliations).toEqual(expect.arrayContaining([
    expect.objectContaining({
      canonical_organization: "Mazzini Society",
      relationship_type: "professional_affiliation",
      claim_confidence: "high",
    }),
    expect.objectContaining({
      canonical_organization: null,
      occupation: "shoe-factory worker",
      relationship_type: "unknown",
      claim_confidence: "medium",
    }),
  ]));
  await page.goto(`./people/${profiles.garibaldi[0]}/`);
  await expect(page.locator("main")).toContainText("Mazzini Society");
  await expect(page.locator("main")).toContainText("shoe-factory worker");
  await expect(page.locator("main")).toContainText("professional affiliation, not employment");
});

test("Edwin Martin publishes the War Production Board as a civilian government pathway", async ({ request, page }) => {
  const person = await publicPerson(request, profiles.edwin);
  expect(person).toMatchObject({ identity_status: "high_confidence", research_status: "verified_employer_found" });
  expect(person.immediate_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      canonical_organization: "War Production Board",
      relationship_type: "government_assignment",
      temporal_basis: "explicit_immediate",
      claim_confidence: "high",
    }),
  ]);
  expect(person.last_civilian_pre_service).toEqual([
    expect.objectContaining({ canonical_organization: "War Production Board" }),
  ]);
  await page.goto(`./people/${profiles.edwin[0]}/`);
  await expect(page.locator("main")).toContainText("War Production Board");
  await expect(page.locator("main")).toContainText("Urgency Rating Commission");
  await expect(page.locator("main")).toContainText("civilian government assignment");
});

test("Paulette Marteliere and Kaj Martens expose identity evidence without invented employers", async ({ request, page }) => {
  for (const profile of [profiles.paulette, profiles.kaj]) {
    const person = await publicPerson(request, profile);
    expect(person).toMatchObject({ identity_status: "high_confidence", research_status: "requires_archival_review" });
    expect(person.immediate_pre_oss_affiliations).toHaveLength(0);
    expect(person.last_civilian_pre_service).toHaveLength(0);
    expect(person.other_pre_oss_affiliations).toHaveLength(0);
    await page.goto(`./people/${profile[0]}/`);
    await expect(page.locator("main")).toContainText("No reliable pre-OSS employer has yet been identified");
  }
  await page.goto(`./people/${profiles.kaj[0]}/`);
  await expect(page.locator("main")).toContainText("Postwar identity corroboration only");
});

test("page 297 rejected Army candidates and temporal exceptions stay visible", async ({ request, page }) => {
  const frank = await publicPerson(request, profiles.frank);
  expect(frank).toMatchObject({ identity_status: "conflicting", research_status: "needs_identity_review" });
  expect(frank.other_pre_oss_affiliations).toHaveLength(0);

  const charlesH = await publicPerson(request, profiles.charlesH);
  expect(charlesH).toMatchObject({ identity_status: "confirmed", research_status: "needs_temporal_review" });
  expect(charlesH.other_pre_oss_affiliations).toHaveLength(0);
  await page.goto(`./people/${profiles.charlesH[0]}/`);
  await expect(page.locator("main")).toContainText("post-OSS Army-entry date");
});

test("Maurice Martin publishes only Army-entry student status", async ({ request, page }) => {
  const person = await publicPerson(request, profiles.maurice);
  expect(person).toMatchObject({ identity_status: "confirmed", research_status: "occupation_only_found" });
  expect(person.other_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      canonical_organization: null,
      role_title: "student",
      relationship_type: "student",
      claim_confidence: "medium",
    }),
  ]);
  await page.goto(`./people/${profiles.maurice[0]}/`);
  await expect(page.locator("main")).toContainText("At Army entry");
  await expect(page.locator("main")).toContainText("no employer, institution, or workplace is identified");
});

test("Batch 1042 public assets omit protected identifiers", async ({ request }) => {
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
