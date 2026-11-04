import fs from "node:fs";
import { expect, test } from "@playwright/test";
import type { APIRequestContext } from "@playwright/test";

const evidence = fs.readFileSync(
  new URL(
    "../../research/evidence-page522-anthony-zucco-to-john-zwergel-review_batch-1032_2026-11-04.json",
    import.meta.url,
  ),
  "utf8",
);

const profiles = {
  anthonyZucco: ["a5c87af2-1156-568d-ab50-40ccdaa85d1d", "Anthony N Zucco"],
  zuckermanFirst: ["70602e22-738a-58a1-956f-45698184dc48", "John V Zuckerman"],
  zuckermanSecond: ["1f692e11-43bb-5e02-8699-d3d0ea2f9268", "John V Zuckerman"],
  zueker: ["7b03d9d4-3553-5331-8fc9-be947a9e4cfd", "John M Zueker"],
  zung: ["5243a4ea-5b4a-53c8-8c58-86aa9d7a1d82", "Cecilia S Zung"],
  zurfluh: ["ee85b027-0732-5308-a09d-9a47dfd86e53", "James R Zurfluh"],
  zurlo: ["eb71f275-786d-5245-b2dc-1f1eefb67f45", "Angelo A Zurlo"],
  zvolanek: ["4c5f05af-5ed3-5fd2-ab0f-05e9244f1731", "James V Zvolanek"],
  zwakhals: ["7de24aae-904f-5ac9-9a6a-5bd5c730ebab", "Francis J Zwakhals"],
  zweig: ["dd37b20f-054b-5f9f-97bd-485d8cf38477", "Stefan M Zweig"],
} as const;

async function publicPerson(request: APIRequestContext, [id, name]: readonly [string, string]) {
  const response = await request.get(`./data/people/${name[0].toLowerCase()}.json`);
  expect(response.ok()).toBeTruthy();
  return (await response.json()).find((item: { person_id: string }) => item.person_id === id);
}

test("Batch 1032 publishes every final-page row with a terminal outcome", async ({ request }) => {
  let people = 0;
  let sourceRows = 0;
  for (const letter of [..."abcdefghijklmnopqrstuvw", "y", "z", "other"]) {
    const response = await request.get(`./data/people/${letter}.json`);
    expect(response.ok()).toBeTruthy();
    for (const person of await response.json()) {
      const rows = person.source_records.filter((row: { pdf_page: number }) => row.pdf_page === 522);
      if (rows.length) {
        people += 1;
        sourceRows += rows.length;
        expect(person.research_status).not.toBe("not_started");
        expect(person.research_status).not.toBe("in_progress");
      }
    }
  }
  expect(people).toBe(12);
  expect(sourceRows).toBe(12);
});

test("Cecilia Zung keeps legal practice, study and government work distinct", async ({ request, page }) => {
  const person = await publicPerson(request, profiles.zung);
  expect(person).toMatchObject({
    identity_status: "high_confidence",
    personnel_category: "civilian_professional_or_administrative_grade",
    commissioned_officer: false,
    research_status: "documented_prewar_employer_found",
  });
  expect(person.immediate_pre_oss_affiliations).toHaveLength(0);
  expect(person.last_civilian_pre_service).toHaveLength(0);
  expect(person.other_pre_oss_affiliations).toEqual(
    expect.arrayContaining([
      expect.objectContaining({ relationship_type: "self_employment", occupation: "lawyer" }),
      expect.objectContaining({ canonical_organization: "New York University", relationship_type: "student" }),
      expect.objectContaining({ relationship_type: "government_assignment", temporal_basis: "temporal_relation_uncertain" }),
    ]),
  );
  await page.goto(`./people/${profiles.zung[0]}/`);
  await expect(page.locator("main")).toContainText("Cecilia Sieu-ling Zung");
  await expect(page.locator("main")).toContainText("New York University");
  await expect(page.locator("main")).toContainText("Postal Censor");
});

test("Angelo Zurlo is an officer without an invented pre-OSS affiliation", async ({ request, page }) => {
  const person = await publicPerson(request, profiles.zurlo);
  expect(person).toMatchObject({
    identity_status: "high_confidence",
    personnel_category: "commissioned_army_officer",
    commissioned_officer: true,
    research_status: "requires_archival_review",
  });
  expect(person.immediate_pre_oss_affiliations).toHaveLength(0);
  expect(person.last_civilian_pre_service).toHaveLength(0);
  expect(person.other_pre_oss_affiliations).toHaveLength(0);
  await page.goto(`./people/${profiles.zurlo[0]}/`);
  await expect(page.locator("main")).toContainText("first lieutenant");
  await expect(page.locator("main")).toContainText("Bari");
});

test("the two John Zuckerman rows remain separate", async ({ request }) => {
  const first = await publicPerson(request, profiles.zuckermanFirst);
  const second = await publicPerson(request, profiles.zuckermanSecond);
  expect(first).toMatchObject({ identity_status: "confirmed", research_status: "occupation_only_found" });
  expect(second).toMatchObject({ identity_status: "ambiguous", research_status: "needs_identity_review" });
  expect(first.possible_duplicate_group).toBe(second.possible_duplicate_group);
  expect(first.other_pre_oss_affiliations).toEqual([
    expect.objectContaining({ occupation: "salesperson or sales agent, except to consumers" }),
  ]);
  expect(second.other_pre_oss_affiliations).toHaveLength(0);
});

test("reviewed spelling variants and occupations are public but qualified", async ({ request }) => {
  const zueker = await publicPerson(request, profiles.zueker);
  expect(zueker.name_variants).toContain("John M Zucker");
  expect(zueker.other_pre_oss_affiliations).toEqual([
    expect.objectContaining({ occupation: "general office clerk", claim_confidence: "medium" }),
  ]);

  const zwakhals = await publicPerson(request, profiles.zwakhals);
  expect(zwakhals.name_variants).toContain("François J Zwakhals");
  expect(zwakhals.other_pre_oss_affiliations).toEqual([
    expect.objectContaining({ occupation: "ship captain, mate, pilot, or engineer" }),
  ]);

  const zucco = await publicPerson(request, profiles.anthonyZucco);
  expect(zucco.other_pre_oss_affiliations).toEqual([
    expect.objectContaining({ occupation: "cook, except private family" }),
  ]);
});

test("undefined and unresolved cases stay empty and archival", async ({ request }) => {
  for (const profile of [profiles.zurfluh, profiles.zvolanek, profiles.zweig]) {
    const person = await publicPerson(request, profile);
    expect(person.research_status).toBe("requires_archival_review");
    expect(person.immediate_pre_oss_affiliations).toHaveLength(0);
    expect(person.last_civilian_pre_service).toHaveLength(0);
    expect(person.other_pre_oss_affiliations).toHaveLength(0);
  }
});

test("Batch 1032 public assets do not expose protected identifiers", async ({ request }) => {
  const forbidden = new Set(
    JSON.parse(evidence)
      .person_updates.flatMap((item: { name_variants?: string[] }) => item.name_variants ?? [])
      .filter((value: string) => /^\d{7,9}$/.test(value)),
  );
  expect(forbidden.size).toBe(0);
  const response = await request.get("./data/people/z.json");
  const text = await response.text();
  expect(text).not.toContain("candidate_identifier");
  expect(text).not.toContain("serial_number");
  expect(text).not.toContain("service_number");
});
