import fs from "node:fs";
import { expect, test } from "@playwright/test";
import type { APIRequestContext } from "@playwright/test";

const evidence = JSON.parse(
  fs.readFileSync(
    new URL(
      "../../research/evidence-page294-clarence-j-marah-to-norman-b-margolyes-review_batch-1039_2026-11-04.json",
      import.meta.url,
    ),
    "utf8",
  ),
);

const profiles = {
  paul: ["1b39ff16-f29b-588b-9f83-be63a822917f", "Paul Marchadier"],
  edward: ["04f9bd64-030a-54eb-83e9-97c40d3f1e0d", "Edward Marchigiani"],
  herbert: ["45a59ffc-eaac-581c-80ff-393af6e87fb4", "Herbert D Marcy"],
  greer: ["b8b22870-60ab-5c76-91ee-bf451d391956", "Greer M Marechal"],
  elwin: ["3718a624-ff8b-5ce0-ac0f-7fa4030586f5", "Elwin Marg"],
  danielP: ["acd47508-c324-503f-89d1-f5282323109c", "Daniel P Margolies"],
  danielF: ["9189a5cf-b440-53a6-b31a-50a40ac9692c", "Daniel F Margolies"],
  arnold: ["fc845180-4288-530b-a1ac-d9b7f70f97da", "Arnold D Margolin"],
} as const;

async function publicPerson(request: APIRequestContext, [id, name]: readonly [string, string]) {
  const response = await request.get(`./data/people/${name[0].toLowerCase()}.json`);
  expect(response.ok()).toBeTruthy();
  return (await response.json()).find((item: { person_id: string }) => item.person_id === id);
}

test("Batch 1039 publishes all page 294 rows with terminal outcomes", async ({ request }) => {
  const people = [];
  for (const shard of [..."abcdefghijklmnopqrstuvw", "y", "z", "other"]) {
    const response = await request.get(`./data/people/${shard}.json`);
    expect(response.ok()).toBeTruthy();
    people.push(...(await response.json()).filter((person: { source_records: { pdf_page: number }[] }) =>
      person.source_records.some((row) => row.pdf_page === 294),
    ));
  }
  expect(people).toHaveLength(44);
  expect(people.flatMap((person: { source_records: { pdf_page: number }[] }) =>
    person.source_records.filter((row) => row.pdf_page === 294))).toHaveLength(46);
  for (const person of people) {
    expect(person.research_status).not.toBe("not_started");
    expect(person.research_status).not.toBe("in_progress");
  }
});

test("Paul Marchadier remains a French BCRA officer, not an American OSS employee", async ({ request, page }) => {
  const paul = await publicPerson(request, profiles.paul);
  expect(paul).toMatchObject({ identity_status: "confirmed", research_status: "completed" });
  expect(paul.immediate_pre_oss_affiliations).toHaveLength(0);
  expect(paul.other_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      canonical_organization: "Bureau central de renseignements et d'action",
      relationship_type: "military_assignment",
    }),
  ]);
  await page.goto(`./people/${profiles.paul[0]}/`);
  await expect(page.locator("main")).toContainText("BCRA");
  await expect(page.locator("main")).toContainText("not labeled a civilian employer");
});

test("Daniel F Margolies publishes the RFC chronology while Daniel P stays separate", async ({ request, page }) => {
  const danielF = await publicPerson(request, profiles.danielF);
  expect(danielF).toMatchObject({ identity_status: "confirmed", research_status: "verified_employer_found" });
  expect(danielF.immediate_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      canonical_organization: "Reconstruction Finance Corporation",
      relationship_type: "government_assignment",
      immediate_pre_oss: true,
      last_civilian_pre_service: true,
    }),
  ]);
  const danielP = await publicPerson(request, profiles.danielP);
  expect(danielP).toMatchObject({ identity_status: "conflicting", research_status: "conflicting_sources" });
  expect(danielP.claims).toHaveLength(0);
  await page.goto(`./people/${profiles.danielF[0]}/`);
  await expect(page.locator("main")).toContainText("Reconstruction Finance Corp.");
  await expect(page.locator("main")).toContainText("government assignment");
});

test("Elwin Marg publishes faculty employment without converting student status", async ({ request, page }) => {
  const elwin = await publicPerson(request, profiles.elwin);
  expect(elwin).toMatchObject({ identity_status: "high_confidence", research_status: "documented_prewar_employer_found" });
  expect(elwin.last_civilian_pre_service).toEqual([
    expect.objectContaining({
      canonical_organization: "University of California, Berkeley School of Optometry",
      role_title: "faculty member",
      relationship_type: "employment",
    }),
  ]);
  await page.goto(`./people/${profiles.elwin[0]}/`);
  await expect(page.locator("main")).toContainText("faculty member");
  await expect(page.locator("main")).toContainText("Student attendance is not mislabeled as employment");
});

test("Arnold Margolin and Greer Marechal remain qualified documented-prewar claims", async ({ request }) => {
  const arnold = await publicPerson(request, profiles.arnold);
  expect(arnold).toMatchObject({ identity_status: "probable", research_status: "documented_prewar_employer_found" });
  expect(arnold.other_pre_oss_affiliations).toEqual([
    expect.objectContaining({ relationship_type: "self_employment", claim_confidence: "medium" }),
  ]);
  const greer = await publicPerson(request, profiles.greer);
  expect(greer).toMatchObject({ identity_status: "probable", research_status: "documented_prewar_employer_found" });
  expect(greer.other_pre_oss_affiliations).toEqual([
    expect.objectContaining({ canonical_organization: "Marechal & Noe", claim_confidence: "medium" }),
  ]);
});

test("duplicate Army rows produce one Edward Marchigiani occupation", async ({ request }) => {
  const edward = await publicPerson(request, profiles.edward);
  expect(edward).toMatchObject({ identity_status: "confirmed", research_status: "occupation_only_found" });
  expect(edward.other_pre_oss_affiliations).toEqual([
    expect.objectContaining({ occupation: "crane, derrick, hoist, or shovel operator", organization_id: null }),
  ]);
  expect(edward.claims).toHaveLength(1);
  expect(edward.claims[0].identity_match_assessment).toContain("Two duplicate official Army rows");
});

test("rejected Herbert Marcy candidate transfers no evidence", async ({ request, page }) => {
  const herbert = await publicPerson(request, profiles.herbert);
  expect(herbert).toMatchObject({ identity_status: "conflicting", research_status: "conflicting_sources" });
  expect(herbert.immediate_pre_oss_affiliations).toHaveLength(0);
  expect(herbert.last_civilian_pre_service).toHaveLength(0);
  expect(herbert.other_pre_oss_affiliations).toHaveLength(0);
  expect(herbert.claims).toHaveLength(0);
  await page.goto(`./people/${profiles.herbert[0]}/`);
  await expect(page.locator("main")).toContainText("different person");
});

test("Batch 1039 public assets omit protected identifiers", async ({ request }) => {
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
