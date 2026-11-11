import fs from "node:fs";
import { expect, test } from "@playwright/test";
import type { APIRequestContext } from "@playwright/test";

const evidence = JSON.parse(
  fs.readFileSync(
    new URL(
      "../../research/evidence-page305-margaret-j-mcclellan-to-charles-h-mccormick-review_batch-1050_2026-11-11.json",
      import.meta.url,
    ),
    "utf8",
  ),
);

const profiles = {
  stewartMcClintic: ["a6911402-9f5f-5a47-ae11-6a42509d5368", "Stewart McClintic"],
  haroldMcCollom: ["51b951af-5498-5e4a-8fad-f116c358817a", "Harold C McCollom"],
  jamesMcConaughy: ["3bf3ecc1-9b6d-5c69-96ed-7ac97d10c1f3", "James L Dr. McConaughy"],
  oscarMcCollum: ["24491f3b-b7bd-5973-94fd-2a0a38b14cf1", "Oscar D McCollum"],
  elmerMcCollum: ["3b715d57-6fcc-58f1-8da6-b8438bf52f62", "Elmer L McCollum"],
  elmerMcCcollum: ["b66a5fc2-3989-5316-a346-82a0bf0162a1", "Elmer L McCcollum"],
} as const;

async function publicPerson(request: APIRequestContext, [id, name]: readonly [string, string]) {
  const response = await request.get(`./data/people/${name[0].toLowerCase()}.json`);
  expect(response.ok()).toBeTruthy();
  return (await response.json()).find((item: { person_id: string }) => item.person_id === id);
}

test("Batch 1050 publishes all page 305 rows with terminal outcomes", async ({ request }) => {
  const people = [];
  for (const shard of [..."abcdefghijklmnopqrstuvw", "y", "z", "other"]) {
    const response = await request.get(`./data/people/${shard}.json`);
    expect(response.ok()).toBeTruthy();
    people.push(...(await response.json()).filter((person: { source_records: { pdf_page: number }[] }) =>
      person.source_records.some((row) => row.pdf_page === 305),
    ));
  }
  expect(people).toHaveLength(46);
  expect(people.flatMap((person: { source_records: { pdf_page: number }[] }) =>
    person.source_records.filter((row) => row.pdf_page === 305))).toHaveLength(46);
  for (const person of people) {
    expect([
      "not_started",
      "in_progress",
      "candidate_found",
      "needs_identity_review",
      "needs_temporal_review",
    ]).not.toContain(person.research_status);
  }
});

test("Stewart McClintic separates his bank employer from the Army Air Forces pathway", async ({ request, page }) => {
  const person = await publicPerson(request, profiles.stewartMcClintic);
  expect(person).toMatchObject({
    identity_status: "high_confidence",
    personnel_category: "commissioned_army_officer",
    commissioned_officer: true,
    research_status: "verified_employer_found",
  });
  expect(person.immediate_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      canonical_organization: "VIII Bomber Command",
      organization_name_as_found: "U.S. VIII Bomber Command",
      relationship_type: "military_assignment",
      temporal_basis: "strongly_date_bounded",
    }),
  ]);
  expect(person.last_civilian_pre_service).toEqual([
    expect.objectContaining({
      canonical_organization: "Mellon National Bank",
      organization_name_as_found: "Mellon National Bank and Trust Company",
      relationship_type: "employment",
      claim_confidence: "high",
    }),
  ]);
  await page.goto(`./people/${profiles.stewartMcClintic[0]}/`);
  await expect(page.locator("main")).toContainText("U.S. VIII Bomber Command");
  await expect(page.locator("main")).toContainText("Mellon National Bank and Trust Company");
  await expect(page.locator("main")).toContainText("Carnegie Hero Fund Commission");
});

test("Harold McCollom publishes Benton & Bowles and keeps the Army category qualified", async ({ request, page }) => {
  const person = await publicPerson(request, profiles.haroldMcCollom);
  expect(person).toMatchObject({
    identity_status: "high_confidence",
    research_status: "verified_employer_found",
  });
  expect(person.name_variants).toContain("Harold C McCollom Jr.");
  expect(person.last_civilian_pre_service).toEqual([
    expect.objectContaining({
      canonical_organization: "Benton & Bowles",
      role_title: "account executive",
      relationship_type: "employment",
      claim_confidence: "high",
    }),
  ]);
  expect(person.other_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      canonical_organization: null,
      occupation: "author, editor, or reporter",
      temporal_basis: "temporal_relation_uncertain",
      claim_confidence: "medium",
    }),
  ]);
  await page.goto(`./people/${profiles.haroldMcCollom[0]}/`);
  await expect(page.locator("main")).toContainText("Benton & Bowles");
  await expect(page.locator("main")).toContainText("Broadcasting: The Weekly Newsmagazine of Radio");
});

test("James McConaughy distinguishes immediate affiliation, employer, and earlier roles", async ({ request, page }) => {
  const person = await publicPerson(request, profiles.jamesMcConaughy);
  expect(person).toMatchObject({
    identity_status: "confirmed",
    personnel_category: "civilian_professional_or_administrative_grade",
    commissioned_officer: false,
    research_status: "verified_employer_found",
  });
  expect(person.name_variants).toEqual(expect.arrayContaining(["James L. McConaughy", "James Lukens McConaughy"]));
  expect(person.immediate_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      canonical_organization: "United China Relief",
      relationship_type: "professional_affiliation",
      temporal_basis: "explicit_immediate",
    }),
  ]);
  expect(person.last_civilian_pre_service).toEqual([
    expect.objectContaining({
      canonical_organization: "Wesleyan University",
      relationship_type: "employment",
      temporal_basis: "probable_immediate",
    }),
  ]);
  expect(person.other_pre_oss_affiliations.map((item: { canonical_organization: string }) => item.canonical_organization)).toEqual(
    expect.arrayContaining(["Bowdoin College", "Dartmouth College", "Knox College"]),
  );
  await page.goto(`./people/${profiles.jamesMcConaughy[0]}/`);
  await expect(page.locator("main")).toContainText("United China Relief");
  await expect(page.locator("main")).toContainText("Wesleyan University");
  await expect(page.locator("main")).toContainText("National Governors Association");
  await expect(page.locator("main")).toContainText("Connecticut History");
});

test("Postwar Army code and repeated-row conflicts remain archival", async ({ request }) => {
  const oscar = await publicPerson(request, profiles.oscarMcCollum);
  expect(oscar).toMatchObject({
    identity_status: "high_confidence",
    research_status: "requires_archival_review",
  });
  expect(oscar.immediate_pre_oss_affiliations).toHaveLength(0);
  expect(oscar.last_civilian_pre_service).toHaveLength(0);
  expect(oscar.other_pre_oss_affiliations).toHaveLength(0);

  const elmer = await publicPerson(request, profiles.elmerMcCollum);
  expect(elmer).toMatchObject({
    identity_status: "conflicting",
    research_status: "conflicting_sources",
  });
  const adjacentElmer = await publicPerson(request, profiles.elmerMcCcollum);
  expect(elmer.possible_duplicate_group).toMatch(/^duplicate-/);
  expect(elmer.possible_duplicate_group).toBe(adjacentElmer.possible_duplicate_group);
});

test("Batch 1050 public assets omit protected identifiers", async ({ request }) => {
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
