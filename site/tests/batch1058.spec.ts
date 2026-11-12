import { expect, test } from "@playwright/test";
import type { APIRequestContext } from "@playwright/test";

const profiles = {
  thomasMcNamara: ["6cd113ce-3751-5a09-b1e2-ac656e2a578c", "Thomas J McNamara"],
  williamMcNeely: ["fad5c77b-2530-5e2a-8492-11170f289b77", "William D McNeely"],
  coyMcNeil: ["2df2c498-74e4-588e-9d85-43e2fdf7a147", "Coy I McNeil"],
  edwardMcNeil: ["494364ee-0148-5275-b1c7-c7d9d4c4ef82", "Edward F McNeil"],
  jamesMcNearnry: ["cae1845d-65c0-5bfb-ba5a-1e3494d35551", "James E McNearnry"],
  jamesMcNerney: ["86bbdb79-84c5-5ce5-81aa-58de02c2d582", "James E McNerney"],
  thomasMcParland: ["baf6c6b1-c49b-5ffd-b858-514918dfce35", "Thomas E McParland"],
  thomasMcPharland: ["5a7c2989-51bc-5df9-a02c-644959675d47", "Thomas E McPharland"],
  joannMcQuiston: ["79e0abb6-1bc6-5caa-b381-a51a3a54a4a8", "Joann W McQuiston"],
  joanneMcquiston: ["1af9856d-8712-5210-b55b-c11c6b2d64b1", "Joanne W Mcquiston"],
  donaldMcVannel: ["c8c087ec-782f-56cd-a71f-a8d7da152c27", "Donald S McVannel"],
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

test("Batch 1058 publishes all 46 page-313 rows as separate terminal profiles", async ({ request }) => {
  const people = [];
  for (const shard of [..."abcdefghijklmnopqrstuvw", "y", "z", "other"]) {
    const response = await request.get(`./data/people/${shard}.json`);
    expect(response.ok()).toBeTruthy();
    people.push(
      ...(await response.json()).filter(
        (person: { source_records: { pdf_page: number }[] }) =>
          person.source_records.some((row) => row.pdf_page === 313),
      ),
    );
  }
  expect(people).toHaveLength(46);
  expect(
    people.flatMap((person: { source_records: { pdf_page: number }[] }) =>
      person.source_records.filter((row) => row.pdf_page === 313),
    ),
  ).toHaveLength(46);
  for (const person of people) {
    expect(["not_started", "in_progress", "candidate_found"]).not.toContain(
      person.research_status,
    );
  }
});

test("Batch 1058 Army-entry occupations remain qualified and organization-free", async ({ request, page }) => {
  for (const [profile, occupation] of [
    [profiles.thomasMcNamara, "occupation in mechanical treatment of metals, n.e.c."],
    [profiles.williamMcNeely, "student"],
    [profiles.edwardMcNeil, "sales clerk"],
    [profiles.donaldMcVannel, "foundry occupation, n.e.c."],
  ] as const) {
    const person = await publicPerson(request, profile);
    expect(person).toMatchObject({
      identity_status: "high_confidence",
      research_status: "occupation_only_found",
    });
    expect(person.immediate_pre_oss_affiliations).toHaveLength(0);
    expect(person.last_civilian_pre_service).toHaveLength(0);
    expect(person.other_pre_oss_affiliations).toEqual([
      expect.objectContaining({
        canonical_organization: null,
        occupation,
        temporal_basis: "temporal_relation_uncertain",
        claim_confidence: "medium",
      }),
    ]);
  }
  await page.goto(`./people/${profiles.donaldMcVannel[0]}/`);
  await expect(page.locator("main")).toContainText("foundry occupation, n.e.c.");
  await expect(page.locator("main")).toContainText("medium");
  await expect(page.locator("main")).toContainText("temporal relation uncertain");
});

test("Page-313 duplicate-name boundaries remain separate and visible", async ({ request }) => {
  for (const [leftProfile, rightProfile] of [
    [profiles.jamesMcNearnry, profiles.jamesMcNerney],
    [profiles.thomasMcParland, profiles.thomasMcPharland],
    [profiles.joannMcQuiston, profiles.joanneMcquiston],
  ] as const) {
    const left = await publicPerson(request, leftProfile);
    const right = await publicPerson(request, rightProfile);
    expect(left.person_id).not.toBe(right.person_id);
    for (const person of [left, right]) {
      expect(person).toMatchObject({
        identity_status: "probable",
        research_status: "needs_identity_review",
      });
      expect(person.possible_duplicate_group).toBeTruthy();
      expect(person.other_pre_oss_affiliations).toHaveLength(0);
    }
  }
});

test("Coy McNeil's protected-identifier conflict is visible and unpromoted", async ({ request, page }) => {
  const person = await publicPerson(request, profiles.coyMcNeil);
  expect(person).toMatchObject({
    identity_status: "conflicting",
    research_status: "conflicting_sources",
  });
  expect(person.immediate_pre_oss_affiliations).toHaveLength(0);
  expect(person.last_civilian_pre_service).toHaveLength(0);
  expect(person.other_pre_oss_affiliations).toHaveLength(0);
  await page.goto(`./people/${profiles.coyMcNeil[0]}/`);
  await expect(page.locator("main")).toContainText("conflicting");
});

test("Batch 1058 public data omits private identity-crosswalk fields", async ({ request }) => {
  for (const profile of Object.values(profiles)) {
    const person = await publicPerson(request, profile);
    const serialized = JSON.stringify(person);
    expect(serialized).not.toContain("candidate_identifier");
    expect(serialized).not.toContain("bulk_record_ordinal");
    expect(serialized).not.toContain("private_identifier");
    expect(serialized).not.toContain("service_number_normalized");
  }
});
