import fs from "node:fs";
import { expect, test } from "@playwright/test";
import type { APIRequestContext } from "@playwright/test";

const evidence = JSON.parse(
  fs.readFileSync(
    new URL(
      "../../research/evidence-page308-robert-h-mcdowell-to-william-m-mcghee-review_batch-1053_2026-11-11.json",
      import.meta.url,
    ),
    "utf8",
  ),
);

const profiles = {
  charlesMcFadden: ["43e65fcd-5b93-58f7-b693-51f0f5541fcc", "Charles W McFadden"],
  lawrenceMcFaddin: ["c7305cd7-23c2-54f5-989e-7a2156333733", "Lawerence B McFaddin"],
  dallasMcFarland: ["6b8e782a-5b29-5d33-a730-501bf048dbc7", "Dallas A McFarland"],
  darelMcFerren: ["1aee67a4-b38b-5ebd-84ec-086909f10cad", "Darel D McFerren"],
  williamMcGaragle: ["4d6eb7f9-83b2-567a-aa76-25683a32d761", "William C McGaragle"],
  edwardMcGaughyA: ["806e928a-6bb1-5935-a8cc-258cb69cbdf6", "Edward A McGaughy"],
  edwardMcGaughy: ["73bc3437-460f-5c09-9903-82b581914e1e", "Edward McGaughy"],
  edwardMcElroy: ["7ab9338b-1ec0-5e60-88e6-d9d123907b4d", "Edward C McElroy"],
  robertMcFadden: ["b2850942-a685-52d7-bb47-43a368d1b665", "Robert D McFadden"],
  stuartMcFadden: ["bc76141a-950f-5e91-8578-a9b74be39d47", "Stuart P McFadden"],
} as const;

async function publicPerson(
  request: APIRequestContext,
  [id, name]: readonly [string, string],
) {
  const response = await request.get(`./data/people/${name[0].toLowerCase()}.json`);
  expect(response.ok()).toBeTruthy();
  return (await response.json()).find(
    (item: { person_id: string }) => item.person_id === id,
  );
}

test("Batch 1053 publishes 46 page-308 rows as 44 researched people", async ({ request }) => {
  const people = [];
  for (const shard of [..."abcdefghijklmnopqrstuvw", "y", "z", "other"]) {
    const response = await request.get(`./data/people/${shard}.json`);
    expect(response.ok()).toBeTruthy();
    people.push(
      ...(await response.json()).filter(
        (person: { source_records: { pdf_page: number }[] }) =>
          person.source_records.some((row) => row.pdf_page === 308),
      ),
    );
  }
  expect(people).toHaveLength(44);
  expect(
    people.flatMap((person: { source_records: { pdf_page: number }[] }) =>
      person.source_records.filter((row) => row.pdf_page === 308),
    ),
  ).toHaveLength(46);
  for (const person of people) {
    expect(["not_started", "in_progress", "candidate_found"]).not.toContain(
      person.research_status,
    );
  }
});

test("Lawrence McFaddin is a documented student and fraternity pledge, not an employee", async ({ request, page }) => {
  const person = await publicPerson(request, profiles.lawrenceMcFaddin);
  expect(person).toMatchObject({
    display_name: "Lawerence B McFaddin",
    identity_status: "high_confidence",
    research_status: "occupation_only_found",
  });
  expect(person.name_variants).toEqual(
    expect.arrayContaining(["Lawrence B McFaddin", "Lawrence McFaddin"]),
  );
  expect(person.immediate_pre_oss_affiliations).toHaveLength(0);
  expect(person.last_civilian_pre_service).toHaveLength(0);
  expect(person.other_pre_oss_affiliations).toEqual(
    expect.arrayContaining([
      expect.objectContaining({
        canonical_organization: "Indiana University",
        relationship_type: "student",
        claim_confidence: "high",
      }),
      expect.objectContaining({
        canonical_organization: "Phi Kappa Psi, Indiana Beta chapter",
        relationship_type: "professional_affiliation",
        role_title: "pledgee",
      }),
    ]),
  );
  await page.goto(`./people/${profiles.lawrenceMcFaddin[0]}/`);
  await expect(page.locator("main")).toContainText("Indiana University");
  await expect(page.locator("main")).toContainText("Phi Kappa Psi");
  await expect(page.locator("main")).toContainText("Lawrence B McFaddin");
});

test("Darel McFerren separates the earlier school job from the qualified last civilian role", async ({ request, page }) => {
  const person = await publicPerson(request, profiles.darelMcFerren);
  expect(person).toMatchObject({
    identity_status: "high_confidence",
    research_status: "documented_prewar_employer_found",
  });
  expect(person.immediate_pre_oss_affiliations).toHaveLength(0);
  expect(person.last_civilian_pre_service).toEqual([
    expect.objectContaining({
      canonical_organization: "Methodist Mission School, Medan",
      role_title: "teacher and administrator",
      relationship_type: "employment",
      temporal_basis: "strongly_date_bounded",
      claim_confidence: "medium",
    }),
  ]);
  expect(person.other_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      canonical_organization: "Gordon High School",
      role_title: "history and economics teacher",
      relationship_type: "employment",
      temporal_basis: "documented_prewar",
      claim_confidence: "high",
    }),
  ]);
  await page.goto(`./people/${profiles.darelMcFerren[0]}/`);
  await expect(page.locator("main")).toContainText("Methodist Mission School");
  await expect(page.locator("main")).toContainText("Gordon High School");
  await expect(page.locator("main")).toContainText("medium");
});

test("Page-308 Army category remains qualified and unnamed", async ({ request, page }) => {
  const person = await publicPerson(request, profiles.charlesMcFadden);
  expect(person).toMatchObject({
    identity_status: "high_confidence",
    research_status: "occupation_only_found",
  });
  expect(person.immediate_pre_oss_affiliations).toHaveLength(0);
  expect(person.last_civilian_pre_service).toHaveLength(0);
  expect(person.other_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      canonical_organization: null,
      organization_id: null,
      occupation: "sales agent, except to consumers",
      relationship_type: "unknown",
      temporal_basis: "temporal_relation_uncertain",
      claim_confidence: "medium",
    }),
  ]);
  await page.goto(`./people/${profiles.charlesMcFadden[0]}/`);
  await expect(page.locator("main")).toContainText("sales agent, except to consumers");
  await expect(page.locator("main")).toContainText(
    "No reliable pre-OSS employer has yet been identified",
  );
});

test("Undefined Army code 999 produces no Dallas McFarland occupation claim", async ({ request, page }) => {
  const person = await publicPerson(request, profiles.dallasMcFarland);
  expect(person).toMatchObject({
    identity_status: "high_confidence",
    research_status: "requires_archival_review",
  });
  expect(person.immediate_pre_oss_affiliations).toHaveLength(0);
  expect(person.last_civilian_pre_service).toHaveLength(0);
  expect(person.other_pre_oss_affiliations).toHaveLength(0);
  expect(person.claims).not.toEqual(
    expect.arrayContaining([expect.objectContaining({ claim_type: "occupation" })]),
  );
  await page.goto(`./people/${profiles.dallasMcFarland[0]}/`);
  await expect(page.locator("main")).toContainText("undefined code 999");
});

test("Page-308 conflict clusters remain separate and visible", async ({ request, page }) => {
  const william = await publicPerson(request, profiles.williamMcGaragle);
  expect(william).toMatchObject({
    identity_status: "ambiguous",
    research_status: "needs_identity_review",
  });
  const edwardA = await publicPerson(request, profiles.edwardMcGaughyA);
  const edward = await publicPerson(request, profiles.edwardMcGaughy);
  expect(edwardA.person_id).not.toBe(edward.person_id);
  expect(edwardA.possible_duplicate_group).toBe(edward.possible_duplicate_group);
  expect(edwardA.identity_status).toBe("ambiguous");
  expect(edward.identity_status).toBe("ambiguous");
  const mcElroy = await publicPerson(request, profiles.edwardMcElroy);
  expect(mcElroy).toMatchObject({
    identity_status: "conflicting",
    research_status: "conflicting_sources",
  });
  await page.goto(`./people/${profiles.williamMcGaragle[0]}/`);
  await expect(page.locator("main")).toContainText("William C McAragle");
  await page.goto(`./people/${profiles.edwardMcGaughyA[0]}/`);
  await expect(page.locator("main")).toContainText("Edward McGaughy");
});

test("Two duplicated source-row pairs remain visible on their single profiles", async ({ request, page }) => {
  for (const profile of [profiles.robertMcFadden, profiles.stuartMcFadden]) {
    const person = await publicPerson(request, profile);
    expect(
      person.source_records.filter((row: { pdf_page: number }) => row.pdf_page === 308),
    ).toHaveLength(2);
    expect(person.possible_duplicate_group).toBeTruthy();
  }
  await page.goto(`./people/${profiles.robertMcFadden[0]}/`);
  await expect(page.locator("main")).toContainText("Index row 2");
  await page.goto(`./people/${profiles.stuartMcFadden[0]}/`);
  await expect(page.locator("main")).toContainText("Index row 2");
});

test("Batch 1053 public assets omit private identifiers", async ({ request }) => {
  const batchIds = new Set(
    evidence.person_updates.map((item: { person_id: string }) => item.person_id),
  );
  const people = [];
  for (const shard of [..."abcdefghijklmnopqrstuvw", "y", "z", "other"]) {
    const response = await request.get(`./data/people/${shard}.json`);
    people.push(
      ...(await response.json()).filter((person: { person_id: string }) =>
        batchIds.has(person.person_id),
      ),
    );
  }
  expect(people).toHaveLength(44);
  const serialized = JSON.stringify(people);
  expect(serialized).not.toContain("candidate_identifier");
  expect(serialized).not.toContain("serial_number");
  expect(serialized).not.toContain("service_number");
  expect(serialized).not.toContain("raw_api_response");
});
