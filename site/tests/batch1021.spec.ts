import fs from "node:fs";
import { expect, test } from "@playwright/test";
import type { APIRequestContext } from "@playwright/test";

const evidence = fs.readFileSync(
  new URL(
    "../../research/evidence-page511-ernest-wohlleben-to-joseph-wolverton-review_batch-1021_2026-11-04.json",
    import.meta.url,
  ),
  "utf8",
);

const profiles = {
  wolbarst: ["25aacc89-f678-5484-b3dd-9378a9e67bf3", "Roger K Wolbarst"],
  charlesWolf: ["ae2711c6-a74a-53ff-841d-17e8a30d621d", "Charles Wolf Jr."],
  miltonWolff: ["b41c09fd-d616-58cf-b2b6-f7a84ce66e1c", "Milton Wolff"],
  robertWolff: ["fe8ec29a-718c-56f3-af64-d619600f4f0d", "Robert L Wolff"],
  peterWolkonsky: ["f73382fa-fd80-500a-86e3-1bdcf682bb12", "Peter N Wolkonsky"],
  dorothyWolgamott: ["8884ab25-95d8-5ab1-a618-69fae44b77fd", "Dorothy E Wolgamott"],
  dimitriWolkonsky: ["f769ad45-d683-5fb7-b478-d32fa77c08a7", "Dimitri Wolkonsky"],
  anthonyWollner: ["d37e1eac-1b51-50b5-acb6-f0a703c330e8", "Anthony A Wollner"],
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

test("Batch 1021 publishes every page 511 row with a terminal outcome", async ({ request }) => {
  let sourceRows = 0;
  let people = 0;
  for (const letter of [
    ..."abcdefghijklmnopqrstuvw",
    "y",
    "z",
    "other",
  ]) {
    const response = await request.get(`./data/people/${letter}.json`);
    expect(response.ok()).toBeTruthy();
    for (const person of await response.json()) {
      const rows = person.source_records.filter(
        (row: { pdf_page: number }) => row.pdf_page === 511,
      );
      if (rows.length) {
        people += 1;
        sourceRows += rows.length;
        expect(person.research_status).not.toBe("not_started");
        expect(person.research_status).not.toBe("in_progress");
        expect(JSON.stringify(person)).not.toMatch(
          /"(?:serial|service)_number(?:_raw|_normalized)?"\s*:/,
        );
      }
    }
  }
  expect(people).toBe(46);
  expect(sourceRows).toBe(46);
});

test("Charles Wolf separates Harvard student status from the Army pathway", async ({ request, page }) => {
  const person = await publicPerson(request, profiles.charlesWolf);
  expect(person).toMatchObject({
    identity_status: "confirmed",
    research_status: "completed",
    personnel_category: "enlisted_army_personnel",
    commissioned_officer: false,
  });
  expect(person.immediate_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      canonical_organization: "United States Army",
      relationship_type: "military_assignment",
      temporal_basis: "strongly_date_bounded",
    }),
  ]);
  expect(person.last_civilian_pre_service).toHaveLength(0);
  expect(person.other_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      canonical_organization: "Harvard University",
      relationship_type: "student",
    }),
  ]);

  await page.goto(`./people/${profiles.charlesWolf[0]}/`);
  await expect(page.getByRole("heading", { name: "Charles Wolf Jr.", level: 1 })).toBeVisible();
  await expect(page.locator("main")).toContainText("United States Army");
  await expect(page.locator("main")).toContainText("Harvard University");
});

test("Milton Wolff publishes a military pathway, not a civilian employer", async ({ request }) => {
  const person = await publicPerson(request, profiles.miltonWolff);
  expect(person).toMatchObject({
    identity_status: "high_confidence",
    research_status: "completed",
    personnel_category: "enlisted_army_personnel",
  });
  expect(person.immediate_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      canonical_organization: "United States Army",
      relationship_type: "military_assignment",
      temporal_basis: "explicit_immediate",
    }),
  ]);
  expect(person.last_civilian_pre_service).toHaveLength(0);
});

test("Robert Wolff upgrades Harvard employment with explicit chronology", async ({ request }) => {
  const person = await publicPerson(request, profiles.robertWolff);
  expect(person).toMatchObject({
    identity_status: "high_confidence",
    research_status: "verified_employer_found",
  });
  expect(person.immediate_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      canonical_organization: "Harvard University",
      relationship_type: "employment",
      start_date: "1937",
      end_date: "1942",
      claim_confidence: "high",
    }),
  ]);
  expect(person.last_civilian_pre_service).toEqual(person.immediate_pre_oss_affiliations);
});

test("Peter Wolkonsky keeps a high-confidence Army path and qualified civilian employer", async ({ request }) => {
  const person = await publicPerson(request, profiles.peterWolkonsky);
  expect(person).toMatchObject({
    identity_status: "confirmed",
    research_status: "documented_prewar_employer_found",
  });
  expect(person.immediate_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      canonical_organization: "United States Army",
      relationship_type: "military_assignment",
      claim_confidence: "high",
      temporal_basis: "explicit_immediate",
    }),
  ]);
  expect(person.last_civilian_pre_service).toEqual([
    expect.objectContaining({
      canonical_organization: "Library of Congress",
      relationship_type: "employment",
      claim_confidence: "medium",
      temporal_basis: "probable_immediate",
      publication_status: "publish_qualified",
    }),
  ]);
});

test("Roger Wolbarst's Dartmouth relationship remains student status", async ({ request }) => {
  const person = await publicPerson(request, profiles.wolbarst);
  expect(person).toMatchObject({
    identity_status: "high_confidence",
    research_status: "requires_archival_review",
  });
  expect(person.immediate_pre_oss_affiliations).toHaveLength(0);
  expect(person.last_civilian_pre_service).toHaveLength(0);
  expect(person.other_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      canonical_organization: "Dartmouth College",
      relationship_type: "student",
    }),
  ]);
});

test("unbridged page 511 candidates remain unresolved", async ({ request }) => {
  for (const profile of [
    profiles.dorothyWolgamott,
    profiles.dimitriWolkonsky,
    profiles.anthonyWollner,
  ]) {
    const person = await publicPerson(request, profile);
    expect(person).toMatchObject({
      identity_status: "unresolved",
      research_status: "requires_archival_review",
    });
    expect(person.immediate_pre_oss_affiliations).toHaveLength(0);
    expect(person.last_civilian_pre_service).toHaveLength(0);
    expect(person.other_pre_oss_affiliations).toHaveLength(0);
    expect(person.claims).toHaveLength(0);
  }
});

test("Batch 1021 evidence excludes secrets and full identifiers", () => {
  expect(evidence).not.toMatch(/"serial_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toMatch(/"service_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toContain("NARA_API_KEY");
  expect(evidence).not.toContain("x-api-key");
  expect(evidence).not.toContain("candidate_identifier");
});

test("Batch 1021 coverage totals are public", async ({ request }) => {
  const response = await request.get("./data/stats.json");
  expect(response.ok()).toBeTruthy();
  const stats = await response.json();
  expect(stats).toMatchObject({
    source_rows: 23978,
    person_entities: 23935,
    research_attempted_people: 16887,
    verified_affiliation_people: 1192,
    verified_employer_people: 547,
    archival_review_assessed_people: 15368,
  });
});
