import fs from "node:fs";
import { expect, test } from "@playwright/test";
import type { APIRequestContext } from "@playwright/test";

const evidence = JSON.parse(
  fs.readFileSync(
    new URL(
      "../../research/evidence-page291-sylvester-maiza-to-william-j-malone-review_batch-1036_2026-11-04.json",
      import.meta.url,
    ),
    "utf8",
  ),
);

const profiles = {
  majure: ["847ceb18-40df-5905-b976-c9870688169a", "Thomas B Majure"],
  maki: ["d945d0d2-91b0-5c58-b940-5167da988687", "Tovivo Maki"],
  makris: ["f8b31500-28c6-5a2b-b839-6d808405d511", "Lambros G Makris"],
  malenbaum: ["c075d283-bef5-5c80-a499-e8ae353455e0", "Wilfred Malenbaum"],
  malfettes: ["faee7841-6790-53dc-9b93-262fe20be144", "Maxime Malfettes"],
  malaspina: ["aa8aca81-09fa-55ba-a35b-d02680076044", "Victor Malaspina"],
  malispino: ["c99f9b22-6c95-5b97-9570-18b0e3a6a95f", "Victor Malispino"],
} as const;

async function publicPerson(request: APIRequestContext, [id, name]: readonly [string, string]) {
  const response = await request.get(`./data/people/${name[0].toLowerCase()}.json`);
  expect(response.ok()).toBeTruthy();
  return (await response.json()).find((item: { person_id: string }) => item.person_id === id);
}

test("Batch 1036 publishes every page 291 row with a terminal outcome", async ({ request }) => {
  const people = [];
  for (const shard of [..."abcdefghijklmnopqrstuvw", "y", "z", "other"]) {
    const response = await request.get(`./data/people/${shard}.json`);
    expect(response.ok()).toBeTruthy();
    people.push(...(await response.json()).filter((person: { source_records: { pdf_page: number }[] }) =>
      person.source_records.some((row) => row.pdf_page === 291),
    ));
  }
  expect(people).toHaveLength(46);
  expect(people.flatMap((person: { source_records: { pdf_page: number }[] }) =>
    person.source_records.filter((row) => row.pdf_page === 291))).toHaveLength(46);
  for (const person of people) {
    expect(person.research_status).not.toBe("not_started");
    expect(person.research_status).not.toBe("in_progress");
  }
});

test("accepted Army categories stay qualified and unsafe codes stay identity-only", async ({ request, page }) => {
  const malaspina = await publicPerson(request, profiles.malaspina);
  expect(malaspina).toMatchObject({ identity_status: "confirmed", research_status: "occupation_only_found" });
  expect(malaspina.immediate_pre_oss_affiliations).toHaveLength(0);
  expect(malaspina.last_civilian_pre_service).toHaveLength(0);
  expect(malaspina.other_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      occupation: "waiter or waitress outside private-family service",
      claim_confidence: "medium",
      temporal_basis: "strongly_date_bounded",
    }),
  ]);

  const maki = await publicPerson(request, profiles.maki);
  expect(maki).toMatchObject({ identity_status: "high_confidence", research_status: "requires_archival_review" });
  expect(maki.name_variants).toContain("Toivo W Maki");
  expect(maki.immediate_pre_oss_affiliations).toHaveLength(0);
  expect(maki.last_civilian_pre_service).toHaveLength(0);
  expect(maki.other_pre_oss_affiliations).toHaveLength(0);
  expect(maki.claims).toEqual([expect.objectContaining({ claim_type: "identity", claim_confidence: "high" })]);

  await page.goto(`./people/${profiles.maki[0]}/`);
  await expect(page.locator("main")).toContainText("Toivo W Maki");
  await expect(page.locator("main")).toContainText("identity only");
});

test("rejected Majure candidate transfers no Army evidence", async ({ request, page }) => {
  const majure = await publicPerson(request, profiles.majure);
  expect(majure).toMatchObject({ identity_status: "unresolved", research_status: "requires_archival_review" });
  expect(majure.immediate_pre_oss_affiliations).toHaveLength(0);
  expect(majure.last_civilian_pre_service).toHaveLength(0);
  expect(majure.other_pre_oss_affiliations).toHaveLength(0);
  expect(majure.claims).toHaveLength(0);
  await page.goto(`./people/${profiles.majure[0]}/`);
  await expect(page.locator("main")).toContainText("explicitly rejected");
  await expect(page.locator("main")).toContainText("No reliable pre-OSS employer");
});

test("Malenbaum separates immediate OPA service from Harvard student status", async ({ request, page }) => {
  const malenbaum = await publicPerson(request, profiles.malenbaum);
  expect(malenbaum).toMatchObject({
    identity_status: "high_confidence",
    research_status: "completed",
    personnel_category: "civilian_professional_or_administrative_grade",
    commissioned_officer: false,
  });
  expect(malenbaum.immediate_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      organization_name_as_found: "OPA",
      relationship_type: "government_assignment",
      role_title: "economist",
      temporal_basis: "probable_immediate",
    }),
  ]);
  expect(malenbaum.last_civilian_pre_service).toHaveLength(0);
  expect(malenbaum.other_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      organization_name_as_found: "Harvard",
      relationship_type: "student",
      role_title: "graduate student in economics",
    }),
  ]);
  await page.goto(`./people/${profiles.malenbaum[0]}/`);
  await expect(page.locator("main")).toContainText("Office of Price Administration");
  await expect(page.locator("main")).toContainText("graduate student in economics");
  await expect(page.locator("main")).toContainText("not employment");
});

test("Makris and Malfettes publish identity context without invented employers", async ({ request, page }) => {
  const makris = await publicPerson(request, profiles.makris);
  expect(makris).toMatchObject({ identity_status: "confirmed", research_status: "requires_archival_review" });
  expect(makris.other_pre_oss_affiliations).toHaveLength(0);
  expect(makris.claims).toEqual([expect.objectContaining({ claim_type: "identity", claim_confidence: "confirmed" })]);

  const malfettes = await publicPerson(request, profiles.malfettes);
  expect(malfettes).toMatchObject({
    identity_status: "high_confidence",
    research_status: "requires_archival_review",
    personnel_category: "foreign_or_allied_military_personnel",
  });
  expect(malfettes.name_variants).toEqual(expect.arrayContaining(["Tartuffe", "Maxime Brunet"]));
  expect(malfettes.other_pre_oss_affiliations).toHaveLength(0);
  expect(malfettes.claims).toEqual([expect.objectContaining({ claim_type: "identity", claim_confidence: "medium" })]);

  await page.goto(`./people/${profiles.makris[0]}/`);
  await expect(page.locator("main")).toContainText("Greek Operational Group");
  await expect(page.locator("main")).toContainText("No reliable pre-OSS employer");
});

test("possible duplicates remain separate public entities", async ({ request }) => {
  const malaspina = await publicPerson(request, profiles.malaspina);
  const malispino = await publicPerson(request, profiles.malispino);
  expect(malaspina.person_id).not.toBe(malispino.person_id);
  expect(malaspina.possible_duplicate_group).toBeTruthy();
  expect(malaspina.possible_duplicate_group).toBe(malispino.possible_duplicate_group);
  expect(malaspina.research_status).toBe("occupation_only_found");
  expect(malispino.research_status).toBe("needs_identity_review");
});

test("Batch 1036 public assets omit protected identifiers", async ({ request }) => {
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
