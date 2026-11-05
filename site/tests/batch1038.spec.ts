import fs from "node:fs";
import { expect, test } from "@playwright/test";
import type { APIRequestContext } from "@playwright/test";

const evidence = JSON.parse(
  fs.readFileSync(
    new URL(
      "../../research/evidence-page293-james-p-mann-to-kenneth-mar-review_batch-1038_2026-11-04.json",
      import.meta.url,
    ),
    "utf8",
  ),
);

const profiles = {
  jacques: ["5cd35483-b9f5-554f-928b-9bce1cf63709", "Jacques Mansion"],
  max: ["4dde52b0-59f6-5901-912f-6dee1395b614", "Max Manus"],
  michael: ["5ddf4d80-7af1-5078-9b50-06a9e0705a8d", "Michael Manno"],
  marcus: ["e39610c5-3508-5326-b6e8-7bc7f5844670", "Marcus Manoloe"],
  emile: ["eb3e155b-ef45-5aee-a023-198f1d69f4b1", "Emile Manuello"],
  nevio: ["e4018ad8-7c06-53df-8436-dbc98b4bd1c1", "Nevio J Manzani"],
} as const;

async function publicPerson(request: APIRequestContext, [id, name]: readonly [string, string]) {
  const response = await request.get(`./data/people/${name[0].toLowerCase()}.json`);
  expect(response.ok()).toBeTruthy();
  return (await response.json()).find((item: { person_id: string }) => item.person_id === id);
}

test("Batch 1038 publishes all page 293 rows with terminal outcomes", async ({ request }) => {
  const people = [];
  for (const shard of [..."abcdefghijklmnopqrstuvw", "y", "z", "other"]) {
    const response = await request.get(`./data/people/${shard}.json`);
    expect(response.ok()).toBeTruthy();
    people.push(...(await response.json()).filter((person: { source_records: { pdf_page: number }[] }) =>
      person.source_records.some((row) => row.pdf_page === 293),
    ));
  }
  expect(people).toHaveLength(46);
  expect(people.flatMap((person: { source_records: { pdf_page: number }[] }) =>
    person.source_records.filter((row) => row.pdf_page === 293))).toHaveLength(46);
  for (const person of people) {
    expect(person.research_status).not.toBe("not_started");
    expect(person.research_status).not.toBe("in_progress");
  }
});

test("Jacques Mansion publishes Renault only as last civilian employer", async ({ request, page }) => {
  const jacques = await publicPerson(request, profiles.jacques);
  expect(jacques).toMatchObject({ identity_status: "high_confidence", research_status: "verified_employer_found" });
  expect(jacques.immediate_pre_oss_affiliations).toHaveLength(0);
  expect(jacques.last_civilian_pre_service).toEqual([
    expect.objectContaining({
      organization_name_as_found: "Service Vente de Renault à Paris",
      canonical_organization: "Renault",
      relationship_type: "employment",
    }),
  ]);
  await page.goto(`./people/${profiles.jacques[0]}/`);
  await expect(page.locator("main")).toContainText("Service Vente de Renault à Paris");
  await expect(page.locator("main")).toContainText("last civilian employer");
});

test("Max Manus preserves the unnamed family flower business", async ({ request, page }) => {
  const max = await publicPerson(request, profiles.max);
  expect(max).toMatchObject({ identity_status: "high_confidence", research_status: "documented_prewar_employer_found" });
  expect(max.immediate_pre_oss_affiliations).toHaveLength(0);
  expect(max.last_civilian_pre_service).toEqual([
    expect.objectContaining({
      organization_id: null,
      organization_name_as_found: "his father's flower business",
      relationship_type: "employment",
    }),
  ]);
  await page.goto(`./people/${profiles.max[0]}/`);
  await expect(page.locator("main")).toContainText("his father's flower business");
  await expect(page.locator("main")).toContainText("firm's name is not supplied");
});

test("Manzani identity is strong while Manuello remains qualified", async ({ request, page }) => {
  const nevio = await publicPerson(request, profiles.nevio);
  expect(nevio).toMatchObject({ identity_status: "high_confidence", research_status: "requires_archival_review" });
  expect(nevio.claims).toEqual([
    expect.objectContaining({ claim_type: "identity", claim_confidence: "high" }),
  ]);
  const emile = await publicPerson(request, profiles.emile);
  expect(emile).toMatchObject({ identity_status: "probable", research_status: "needs_identity_review" });
  expect(emile.last_civilian_pre_service).toHaveLength(0);
  expect(emile.claims).toEqual([
    expect.objectContaining({ claim_type: "identity", claim_confidence: "medium" }),
  ]);
  await page.goto(`./people/${profiles.emile[0]}/`);
  await expect(page.locator("main")).toContainText("qualified identity lead");
  await expect(page.locator("main")).toContainText("not conclusive");
});

test("duplicate Army rows produce one qualified Michael Manno occupation", async ({ request }) => {
  const michael = await publicPerson(request, profiles.michael);
  expect(michael).toMatchObject({ identity_status: "confirmed", research_status: "occupation_only_found" });
  expect(michael.other_pre_oss_affiliations).toEqual([
    expect.objectContaining({ occupation: "compositor or typesetter", organization_id: null }),
  ]);
  expect(michael.claims).toHaveLength(1);
  expect(michael.claims[0].identity_match_assessment).toContain("Two duplicate official Army rows");
});

test("conflicting Marcus Manoloe candidates transfer no evidence", async ({ request, page }) => {
  const marcus = await publicPerson(request, profiles.marcus);
  expect(marcus).toMatchObject({ identity_status: "conflicting", research_status: "conflicting_sources" });
  expect(marcus.immediate_pre_oss_affiliations).toHaveLength(0);
  expect(marcus.last_civilian_pre_service).toHaveLength(0);
  expect(marcus.other_pre_oss_affiliations).toHaveLength(0);
  expect(marcus.claims).toHaveLength(0);
  await page.goto(`./people/${profiles.marcus[0]}/`);
  await expect(page.locator("main")).toContainText("shared");
  await expect(page.locator("main")).toContainText("No reliable pre-OSS employer");
});

test("Batch 1038 public assets omit protected identifiers", async ({ request }) => {
  const batchIds = new Set(evidence.person_updates.map((item: { person_id: string }) => item.person_id));
  const people = [];
  for (const shard of [..."abcdefghijklmnopqrstuvw", "y", "z", "other"]) {
    const response = await request.get(`./data/people/${shard}.json`);
    people.push(...(await response.json()).filter((person: { person_id: string }) => batchIds.has(person.person_id)));
  }
  expect(people).toHaveLength(45);
  const serialized = JSON.stringify(people);
  expect(serialized).not.toContain("candidate_identifier");
  expect(serialized).not.toContain("serial_number");
  expect(serialized).not.toContain("service_number");
  expect(serialized).not.toContain("bulk_record_ordinal");
});
