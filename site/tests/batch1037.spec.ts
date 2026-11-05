import fs from "node:fs";
import { expect, test } from "@playwright/test";
import type { APIRequestContext } from "@playwright/test";

const evidence = JSON.parse(
  fs.readFileSync(
    new URL(
      "../../research/evidence-page292-robert-maloof-to-gottfried-t-mann-review_batch-1037_2026-11-04.json",
      import.meta.url,
    ),
    "utf8",
  ),
);

const profiles = {
  marcus: ["e48018de-7e7c-55dd-9463-a85918f30847", "Marcus Manaloe"],
  david: ["8eebccc3-e7d0-5901-a4f0-805c905de555", "David G Mandelbaum"],
  erika: ["5ce229cf-2112-5804-b061-f47ff719e18c", "Erika Mann"],
  golo: ["5ab7f4a4-5341-5532-8a4f-db07d2bab3d8", "Gottfried T Mann"],
} as const;

async function publicPerson(request: APIRequestContext, [id, name]: readonly [string, string]) {
  const response = await request.get(`./data/people/${name[0].toLowerCase()}.json`);
  expect(response.ok()).toBeTruthy();
  return (await response.json()).find((item: { person_id: string }) => item.person_id === id);
}

test("Batch 1037 publishes every page 292 row with a terminal outcome", async ({ request }) => {
  const people = [];
  for (const shard of [..."abcdefghijklmnopqrstuvw", "y", "z", "other"]) {
    const response = await request.get(`./data/people/${shard}.json`);
    expect(response.ok()).toBeTruthy();
    people.push(...(await response.json()).filter((person: { source_records: { pdf_page: number }[] }) =>
      person.source_records.some((row) => row.pdf_page === 292),
    ));
  }
  expect(people).toHaveLength(46);
  expect(people.flatMap((person: { source_records: { pdf_page: number }[] }) =>
    person.source_records.filter((row) => row.pdf_page === 292))).toHaveLength(46);
  for (const person of people) {
    expect(person.research_status).not.toBe("not_started");
    expect(person.research_status).not.toBe("in_progress");
  }
});

test("Mandelbaum publishes Minnesota as both immediate and last civilian employer", async ({ request, page }) => {
  const david = await publicPerson(request, profiles.david);
  expect(david).toMatchObject({
    identity_status: "high_confidence",
    research_status: "verified_employer_found",
    commissioned_officer: true,
  });
  expect(david.immediate_pre_oss_affiliations).toEqual([
    expect.objectContaining({ organization_name_as_found: "University of Minnesota", relationship_type: "employment" }),
  ]);
  expect(david.last_civilian_pre_service).toEqual([
    expect.objectContaining({ organization_name_as_found: "University of Minnesota" }),
  ]);
  await page.goto(`./people/${profiles.david[0]}/`);
  await expect(page.locator("main")).toContainText("University of Minnesota");
  await expect(page.locator("main")).toContainText("while on leave");
});

test("Erika Mann keeps OWI qualified and separate from an immediate employer", async ({ request, page }) => {
  const erika = await publicPerson(request, profiles.erika);
  expect(erika).toMatchObject({ identity_status: "high_confidence", research_status: "completed" });
  expect(erika.immediate_pre_oss_affiliations).toHaveLength(0);
  expect(erika.last_civilian_pre_service).toHaveLength(0);
  expect(erika.other_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      organization_name_as_found: "Office of War Information",
      relationship_type: "government_assignment",
      claim_confidence: "medium",
    }),
  ]);
  await page.goto(`./people/${profiles.erika[0]}/`);
  await expect(page.locator("main")).toContainText("Office of War Information");
  await expect(page.locator("main")).toContainText("not proven to be the immediate predecessor");
});

test("Gottfried Mann publishes Golo alias and date-bounded Olivet employment", async ({ request, page }) => {
  const golo = await publicPerson(request, profiles.golo);
  expect(golo).toMatchObject({ identity_status: "high_confidence", research_status: "verified_employer_found" });
  expect(golo.name_variants).toEqual(expect.arrayContaining(["Golo Mann", "Angelus Gottfried Thomas Mann"]));
  expect(golo.immediate_pre_oss_affiliations).toEqual([
    expect.objectContaining({ organization_name_as_found: "Olivet College", role_title: "lecturer in history" }),
  ]);
  expect(golo.last_civilian_pre_service).toEqual([
    expect.objectContaining({ organization_name_as_found: "Olivet College" }),
  ]);
  await page.goto(`./people/${profiles.golo[0]}/`);
  await expect(page.locator("main")).toContainText("Golo Mann");
  await expect(page.locator("main")).toContainText("Olivet College");
});

test("shared and different-name Army candidates transfer no evidence", async ({ request, page }) => {
  const marcus = await publicPerson(request, profiles.marcus);
  expect(marcus).toMatchObject({ identity_status: "conflicting", research_status: "needs_identity_review" });
  expect(marcus.immediate_pre_oss_affiliations).toHaveLength(0);
  expect(marcus.last_civilian_pre_service).toHaveLength(0);
  expect(marcus.other_pre_oss_affiliations).toHaveLength(0);
  expect(marcus.claims).toHaveLength(0);
  await page.goto(`./people/${profiles.marcus[0]}/`);
  await expect(page.locator("main")).toContainText("shared");
  await expect(page.locator("main")).toContainText("No reliable pre-OSS employer");
});

test("Batch 1037 public assets omit protected identifiers", async ({ request }) => {
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
