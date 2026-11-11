import fs from "node:fs";
import { expect, test } from "@playwright/test";
import type { APIRequestContext } from "@playwright/test";

const evidence = JSON.parse(
  fs.readFileSync(
    new URL(
      "../../research/evidence-page306-howard-p-mccormick-to-william-c-mccutcheon-review_batch-1051_2026-11-11.json",
      import.meta.url,
    ),
    "utf8",
  ),
);

const profiles = {
  frankMcCoy: ["adbb1da1-14ea-5d70-9445-9b429be33320", "Frank R McCoy"],
  thomasMcCoy: ["14fd8141-1e60-5dc7-8822-fb74feedfc23", "Thomas F McCoy"],
  josephMcCrindleCpl: ["4c8522f4-9712-584a-924e-ba55ee072e88", "Joseph F McCrindle"],
  josephMcCrindleLt: ["9c68dd21-4877-5709-b14a-e757abb377f9", "Joseph F McCrindle"],
  georgeMcCune: ["c69ef820-17f0-5460-83df-d717087725f5", "George M McCune"],
  marshallMcCune: ["b035428e-2bc2-5a6c-b645-7e5671b55de0", "Marshall L McCune"],
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

test("Batch 1051 publishes all page 306 rows with terminal outcomes", async ({ request }) => {
  const people = [];
  for (const shard of [..."abcdefghijklmnopqrstuvw", "y", "z", "other"]) {
    const response = await request.get(`./data/people/${shard}.json`);
    expect(response.ok()).toBeTruthy();
    people.push(
      ...(await response.json()).filter(
        (person: { source_records: { pdf_page: number }[] }) =>
          person.source_records.some((row) => row.pdf_page === 306),
      ),
    );
  }
  expect(people).toHaveLength(46);
  expect(
    people.flatMap((person: { source_records: { pdf_page: number }[] }) =>
      person.source_records.filter((row) => row.pdf_page === 306),
    ),
  ).toHaveLength(46);
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

test("George McCune publishes Occidental as both immediate and last civilian employment", async ({ request, page }) => {
  const person = await publicPerson(request, profiles.georgeMcCune);
  expect(person).toMatchObject({
    identity_status: "confirmed",
    research_status: "verified_employer_found",
  });
  expect(person.name_variants).toContain("George McAfee McCune");
  expect(person.immediate_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      canonical_organization: "Occidental College",
      relationship_type: "employment",
      temporal_basis: "explicit_immediate",
      claim_confidence: "confirmed",
    }),
  ]);
  expect(person.last_civilian_pre_service).toEqual([
    expect.objectContaining({
      canonical_organization: "Occidental College",
      relationship_type: "employment",
    }),
  ]);
  await page.goto(`./people/${profiles.georgeMcCune[0]}/`);
  await expect(page.locator("main")).toContainText("Occidental College");
  await expect(page.locator("main")).toContainText("University of California");
});

test("Thomas McCoy keeps the immediate Army pathway separate from an unknown civilian employer", async ({ request, page }) => {
  const person = await publicPerson(request, profiles.thomasMcCoy);
  expect(person).toMatchObject({
    identity_status: "high_confidence",
    personnel_category: "commissioned_army_officer",
    commissioned_officer: true,
    research_status: "requires_archival_review",
  });
  expect(person.name_variants).toContain("Thomas Frederick McCoy");
  expect(person.immediate_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      canonical_organization: "United States Army",
      relationship_type: "military_assignment",
      temporal_basis: "explicit_immediate",
    }),
  ]);
  expect(person.last_civilian_pre_service).toHaveLength(0);
  await page.goto(`./people/${profiles.thomasMcCoy[0]}/`);
  await expect(page.locator("main")).toContainText("United States Army");
  await expect(page.locator("main")).toContainText("The Washington Post");
});

test("The two Joseph McCrindle rows remain separate and receive row-specific evidence", async ({ request, page }) => {
  const corporal = await publicPerson(request, profiles.josephMcCrindleCpl);
  const lieutenant = await publicPerson(request, profiles.josephMcCrindleLt);
  expect(corporal.person_id).not.toBe(lieutenant.person_id);
  expect(corporal.possible_duplicate_group).toBe(lieutenant.possible_duplicate_group);
  expect(corporal).toMatchObject({
    identity_status: "high_confidence",
    personnel_category: "enlisted_army_personnel",
    research_status: "occupation_only_found",
  });
  expect(corporal.other_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      canonical_organization: null,
      occupation: "student",
      end_date: "1943-05-25",
    }),
  ]);
  expect(lieutenant).toMatchObject({
    identity_status: "confirmed",
    personnel_category: "commissioned_army_officer",
    research_status: "requires_archival_review",
  });
  expect(lieutenant.name_variants).toContain("Joseph Feder McCrindle");
  expect(lieutenant.other_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      canonical_organization: "Harvard University",
      relationship_type: "student",
    }),
  ]);
  await page.goto(`./people/${profiles.josephMcCrindleLt[0]}/`);
  await expect(page.locator("main")).toContainText("Harvard University");
  await expect(page.locator("main")).toContainText("Smithsonian Institution");
});

test("Frank McCoy and Marshall McCune affiliations remain temporally qualified", async ({ request, page }) => {
  const frank = await publicPerson(request, profiles.frankMcCoy);
  expect(frank.other_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      canonical_organization: "Foreign Policy Association",
      relationship_type: "professional_affiliation",
      temporal_basis: "documented_prewar",
    }),
  ]);
  expect(frank.immediate_pre_oss_affiliations).toHaveLength(0);

  const marshall = await publicPerson(request, profiles.marshallMcCune);
  expect(marshall.other_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      canonical_organization: "U.S. Army Special Services",
      relationship_type: "military_assignment",
      temporal_basis: "temporal_relation_uncertain",
      claim_confidence: "medium",
    }),
  ]);
  expect(marshall.immediate_pre_oss_affiliations).toHaveLength(0);
  await page.goto(`./people/${profiles.marshallMcCune[0]}/`);
  await expect(page.locator("main")).toContainText("U.S. Army Special Services");
  await expect(page.locator("main")).toContainText("relation to OSS is uncertain");
});

test("Batch 1051 public assets omit private identifiers", async ({ request }) => {
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
  expect(people).toHaveLength(46);
  const serialized = JSON.stringify(people);
  expect(serialized).not.toContain("candidate_identifier");
  expect(serialized).not.toContain("serial_number");
  expect(serialized).not.toContain("service_number");
  expect(serialized).not.toContain("bulk_record_ordinal");
});
