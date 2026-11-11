import fs from "node:fs";
import { expect, test } from "@playwright/test";
import type { APIRequestContext } from "@playwright/test";

const evidence = JSON.parse(
  fs.readFileSync(
    new URL(
      "../../research/evidence-page304-thomas-a-mccann-to-grant-s-mcclelian-review_batch-1049_2026-11-06.json",
      import.meta.url,
    ),
    "utf8",
  ),
);

const profiles = {
  thomasMcCart: ["ed6f557f-5d4d-5668-9f8d-10db4a9851d7", "Thomas A McCart"],
  elderMcCarter: ["d14f21e3-d3df-596d-b041-3a7879d15de4", "Elder McCarter"],
  rexMcCauley: ["22ad5999-7308-5fb9-bba2-018ae671ceac", "Rex H McCauley"],
} as const;

async function publicPerson(request: APIRequestContext, [id, name]: readonly [string, string]) {
  const response = await request.get(`./data/people/${name[0].toLowerCase()}.json`);
  expect(response.ok()).toBeTruthy();
  return (await response.json()).find((item: { person_id: string }) => item.person_id === id);
}

test("Batch 1049 publishes all page 304 rows with terminal outcomes", async ({ request }) => {
  const people = [];
  for (const shard of [..."abcdefghijklmnopqrstuvw", "y", "z", "other"]) {
    const response = await request.get(`./data/people/${shard}.json`);
    expect(response.ok()).toBeTruthy();
    people.push(...(await response.json()).filter((person: { source_records: { pdf_page: number }[] }) =>
      person.source_records.some((row) => row.pdf_page === 304),
    ));
  }
  expect(people).toHaveLength(46);
  expect(people.flatMap((person: { source_records: { pdf_page: number }[] }) =>
    person.source_records.filter((row) => row.pdf_page === 304))).toHaveLength(46);
  for (const person of people) {
    expect(person.research_status).not.toBe("not_started");
    expect(person.research_status).not.toBe("in_progress");
  }
});

test("Thomas McCart separates his immediate Army pathway from documented RCA work", async ({ request, page }) => {
  const person = await publicPerson(request, profiles.thomasMcCart);
  expect(person).toMatchObject({
    identity_status: "confirmed",
    personnel_category: "enlisted_army_personnel",
    commissioned_officer: false,
    research_status: "documented_prewar_employer_found",
  });
  expect(person.immediate_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      canonical_organization: "United States Army",
      organization_name_as_found: "Vth Army Replacement Center",
      relationship_type: "military_assignment",
      temporal_basis: "explicit_immediate",
    }),
  ]);
  expect(person.last_civilian_pre_service).toHaveLength(0);
  expect(person.other_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      canonical_organization: "Radio Corporation of America",
      organization_name_as_found: "RCA",
      relationship_type: "employment",
      temporal_basis: "documented_prewar",
      claim_confidence: "high",
    }),
  ]);
  await page.goto(`./people/${profiles.thomasMcCart[0]}/`);
  await expect(page.locator("main")).toContainText("Vth Army Replacement Center");
  await expect(page.locator("main")).toContainText("RCA");
  await expect(page.locator("main")).toContainText("OSS board of officers report on arrival at Naples");
});

test("Army-entry categories remain qualified and conflicts create no affiliation", async ({ request }) => {
  const elder = await publicPerson(request, profiles.elderMcCarter);
  expect(elder).toMatchObject({ identity_status: "high_confidence", research_status: "occupation_only_found" });
  expect(elder.immediate_pre_oss_affiliations).toHaveLength(0);
  expect(elder.last_civilian_pre_service).toHaveLength(0);
  expect(elder.other_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      canonical_organization: null,
      occupation: "student",
      relationship_type: "student",
      claim_confidence: "medium",
    }),
  ]);

  const rex = await publicPerson(request, profiles.rexMcCauley);
  expect(rex).toMatchObject({ identity_status: "conflicting", research_status: "conflicting_sources" });
  expect(rex.immediate_pre_oss_affiliations).toHaveLength(0);
  expect(rex.last_civilian_pre_service).toHaveLength(0);
  expect(rex.other_pre_oss_affiliations).toHaveLength(0);
});

test("Batch 1049 public assets omit protected identifiers", async ({ request }) => {
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
