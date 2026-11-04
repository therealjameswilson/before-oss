import fs from "node:fs";
import { expect, test } from "@playwright/test";
import type { APIRequestContext } from "@playwright/test";

const evidence = fs.readFileSync(
  new URL(
    "../../research/evidence-page288-sylvia-macdonald-to-roderick-maclennan-review_batch-1033_2026-11-04.json",
    import.meta.url,
  ),
  "utf8",
);

const profiles = {
  macFarland: ["2a6b3d58-409a-5abf-9a55-f4086aabfb65", "Lanning MacFarland"],
  macGregorRanked: ["a5987bdb-67ab-54b3-980c-908b6fefea23", "Clark MacGregor"],
  macGregorUnranked: ["438a3e9f-1de4-50de-980e-b68f2d9b8e98", "Clark MacGregor"],
  gerstleMack: ["d5d3a163-d899-5c02-912c-5a8fceecd039", "Gerstle Mack"],
  macKinnon: ["b12f7b98-15a6-5fed-bb0a-1c7ae661c1ad", "Donald W MacKinnon"],
  malcolmCivilian: ["90b1746e-8188-5d8b-8e60-62a6f1f2e066", "Malcolm S MacKenzie"],
  malcolmOfficer: ["7f796d25-c694-5f0c-be35-f649c24e5c82", "Malcolm S MacKenzie"],
} as const;

async function publicPerson(request: APIRequestContext, [id, name]: readonly [string, string]) {
  const response = await request.get(`./data/people/${name[0].toLowerCase()}.json`);
  expect(response.ok()).toBeTruthy();
  return (await response.json()).find((item: { person_id: string }) => item.person_id === id);
}

test("Batch 1033 publishes every page 288 row with a terminal outcome", async ({ request }) => {
  let people = 0;
  let sourceRows = 0;
  for (const letter of [..."abcdefghijklmnopqrstuvw", "y", "z", "other"]) {
    const response = await request.get(`./data/people/${letter}.json`);
    expect(response.ok()).toBeTruthy();
    for (const person of await response.json()) {
      const rows = person.source_records.filter((row: { pdf_page: number }) => row.pdf_page === 288);
      if (rows.length) {
        people += 1;
        sourceRows += rows.length;
        expect(person.research_status).not.toBe("not_started");
        expect(person.research_status).not.toBe("in_progress");
      }
    }
  }
  expect(people).toBe(46);
  expect(sourceRows).toBe(46);
});

test("Lanning MacFarland is qualified as last civilian employer, not immediate", async ({ request, page }) => {
  const person = await publicPerson(request, profiles.macFarland);
  expect(person).toMatchObject({ identity_status: "high_confidence", research_status: "verified_employer_found" });
  expect(person.immediate_pre_oss_affiliations).toHaveLength(0);
  expect(person.last_civilian_pre_service).toEqual([
    expect.objectContaining({ canonical_organization: "Northern Trust Company", temporal_basis: "strongly_date_bounded" }),
  ]);
  await page.goto(`./people/${profiles.macFarland[0]}/`);
  await expect(page.locator("main")).toContainText("Northern Trust Company");
  await expect(page.locator("main")).toContainText("vice president");
});

test("the two Clark MacGregor rows remain separate", async ({ request, page }) => {
  const ranked = await publicPerson(request, profiles.macGregorRanked);
  const unranked = await publicPerson(request, profiles.macGregorUnranked);
  expect(ranked).toMatchObject({
    identity_status: "confirmed",
    personnel_category: "enlisted_army_personnel",
    commissioned_officer: true,
    research_status: "completed",
  });
  expect(unranked).toMatchObject({ identity_status: "ambiguous", research_status: "needs_identity_review" });
  expect(ranked.possible_duplicate_group).toBe(unranked.possible_duplicate_group);
  expect(ranked.immediate_pre_oss_affiliations).toEqual([
    expect.objectContaining({ canonical_organization: "United States Army", relationship_type: "military_assignment" }),
  ]);
  expect(ranked.other_pre_oss_affiliations).toEqual([
    expect.objectContaining({ canonical_organization: "Dartmouth College", relationship_type: "student" }),
  ]);
  expect(unranked.immediate_pre_oss_affiliations).toHaveLength(0);
  expect(unranked.other_pre_oss_affiliations).toHaveLength(0);
  await page.goto(`./people/${profiles.macGregorRanked[0]}/`);
  await expect(page.locator("main")).toContainText("Dartmouth College");
  await expect(page.locator("main")).toContainText("U.S. Army");
});

test("Gerstle Mack remains occupation-only without a self-employment inference", async ({ request }) => {
  const person = await publicPerson(request, profiles.gerstleMack);
  expect(person).toMatchObject({ identity_status: "high_confidence", research_status: "occupation_only_found" });
  expect(person.immediate_pre_oss_affiliations).toHaveLength(0);
  expect(person.last_civilian_pre_service).toHaveLength(0);
  expect(person.other_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      canonical_organization: null,
      relationship_type: "unknown",
      occupation: "writer and biographer",
    }),
  ]);
});

test("Donald MacKinnon has an explicit Bryn Mawr predecessor", async ({ request, page }) => {
  const person = await publicPerson(request, profiles.macKinnon);
  expect(person).toMatchObject({ identity_status: "high_confidence", research_status: "verified_employer_found" });
  expect(person.immediate_pre_oss_affiliations).toEqual([
    expect.objectContaining({ canonical_organization: "Bryn Mawr College", temporal_basis: "explicit_immediate" }),
  ]);
  expect(person.last_civilian_pre_service).toEqual([
    expect.objectContaining({ canonical_organization: "Bryn Mawr College", temporal_basis: "explicit_immediate" }),
  ]);
  await page.goto(`./people/${profiles.macKinnon[0]}/`);
  await expect(page.locator("main")).toContainText("Bryn Mawr College");
  await expect(page.locator("main")).toContainText("professor of psychology");
});

test("the two Malcolm MacKenzie rows remain separate", async ({ request }) => {
  const civilian = await publicPerson(request, profiles.malcolmCivilian);
  const officer = await publicPerson(request, profiles.malcolmOfficer);
  expect(civilian).toMatchObject({
    identity_status: "ambiguous",
    personnel_category: "civilian_professional_or_administrative_grade",
    commissioned_officer: false,
  });
  expect(officer).toMatchObject({
    identity_status: "ambiguous",
    personnel_category: "commissioned_army_officer",
    commissioned_officer: true,
  });
  expect(civilian.possible_duplicate_group).toBe(officer.possible_duplicate_group);
  expect(civilian.other_pre_oss_affiliations).toHaveLength(0);
  expect(officer.other_pre_oss_affiliations).toHaveLength(0);
});

test("Batch 1033 public assets do not expose protected identifiers", async ({ request }) => {
  const batch = JSON.parse(evidence);
  const batchIds = new Set(batch.person_updates.map((item: { person_id: string }) => item.person_id));
  const protectedNameVariants = new Set(
    batch.person_updates
      .flatMap((item: { name_variants?: string[] }) => item.name_variants ?? [])
      .filter((value: string) => /^\d{7,9}$/.test(value)),
  );
  expect(protectedNameVariants.size).toBe(0);

  const keys = new Set<string>();
  function collectKeys(value: unknown): void {
    if (Array.isArray(value)) {
      value.forEach(collectKeys);
    } else if (value && typeof value === "object") {
      for (const [key, child] of Object.entries(value)) {
        keys.add(key);
        collectKeys(child);
      }
    }
  }

  for (const shard of ["c", "d", "g", "l", "m"]) {
    const response = await request.get(`./data/people/${shard}.json`);
    const people = (await response.json()).filter((person: { person_id: string }) => batchIds.has(person.person_id));
    people.forEach(collectKeys);
  }
  expect(keys).not.toContain("candidate_identifier");
  expect(keys).not.toContain("serial_number");
  expect(keys).not.toContain("service_number");
});
