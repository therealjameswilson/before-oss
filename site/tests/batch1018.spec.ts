import fs from "node:fs";
import { expect, test } from "@playwright/test";
import type { APIRequestContext } from "@playwright/test";

const evidence = fs.readFileSync(
  new URL(
    "../../research/evidence-page508-gladys-a-wilson-to-frederick-c-wing-review_batch-1018_2026-11-04.json",
    import.meta.url,
  ),
  "utf8",
);

const profiles = {
  johnSkinnerWilson: ["642c8e61-e513-5ea2-b6dd-e3fc13c3c40e", "John S Wilson"],
  sivertWindh: ["13a0b5bc-18cf-5228-8f8d-4d5a0b3b0aac", "Sivert Windh"],
  geraldWinesIndexed: ["cf1e160d-64d7-5426-8311-1f272b49c392", "Gerald K Wines"],
  geraldWinesMajor: ["6f6de55e-192d-5c5d-a452-bf5d63148788", "Gerald K Wines"],
  johnHWilson: ["db161798-f1ee-5b94-80aa-73578257df6b", "John H Wilson"],
  leonardWilson: ["05aefa92-0a08-5672-af44-f8732050dbd2", "Leonard S Wilson"],
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

test("Batch 1018 publishes every page 508 row with a terminal outcome", async ({ request }) => {
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
        (row: { pdf_page: number }) => row.pdf_page === 508,
      );
      if (rows.length) {
        people += 1;
        sourceRows += rows.length;
        expect(person.research_status).not.toBe("not_started");
        expect(person.research_status).not.toBe("in_progress");
        expect(JSON.stringify(person)).not.toMatch(/\b[ORW]-?\d{5,9}\b/);
      }
    }
  }
  expect(people).toBe(46);
  expect(sourceRows).toBe(46);
});

test("John Skinner Wilson keeps Gilwell as a professional affiliation, not an employer", async ({ request }) => {
  const person = await publicPerson(request, profiles.johnSkinnerWilson);
  expect(person).toMatchObject({
    identity_status: "high_confidence",
    research_status: "requires_archival_review",
    personnel_category: "foreign_or_allied_military_personnel",
    commissioned_officer: true,
  });
  expect(person.immediate_pre_oss_affiliations).toHaveLength(0);
  expect(person.last_civilian_pre_service).toHaveLength(0);
  expect(person.other_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      canonical_organization: "The Scout Association at Gilwell Park",
      relationship_type: "professional_affiliation",
      temporal_basis: "documented_prewar",
      claim_confidence: "high",
    }),
  ]);
});

test("Sivert Windh publishes a qualified occupation without inventing an employer", async ({ request }) => {
  const person = await publicPerson(request, profiles.sivertWindh);
  expect(person).toMatchObject({
    identity_status: "confirmed",
    research_status: "occupation_only_found",
    personnel_category: "enlisted_army_personnel",
    commissioned_officer: false,
  });
  expect(person.name_variants).toContain("Kjell Rune Sivert Windh");
  expect(person.immediate_pre_oss_affiliations).toHaveLength(0);
  expect(person.last_civilian_pre_service).toHaveLength(0);
  expect(person.other_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      canonical_organization: null,
      occupation: "waiter or waitress outside private-family service",
      claim_confidence: "medium",
      publication_status: "publish_qualified",
    }),
  ]);
});

test("Gerald Wines keeps the unnamed newspaper as qualified documented-prewar work", async ({ request, page }) => {
  const person = await publicPerson(request, profiles.geraldWinesMajor);
  expect(person).toMatchObject({
    identity_status: "high_confidence",
    research_status: "documented_prewar_employer_found",
    personnel_category: "commissioned_army_officer",
    commissioned_officer: true,
  });
  expect(person.immediate_pre_oss_affiliations).toHaveLength(0);
  expect(person.last_civilian_pre_service).toHaveLength(0);
  expect(person.other_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      canonical_organization: "Unidentified major Dallas-area newspaper",
      role_title: "advertising representative",
      relationship_type: "employment",
      temporal_basis: "documented_prewar",
      claim_confidence: "medium",
    }),
  ]);

  await page.goto(`./people/${profiles.geraldWinesMajor[0]}/`);
  await expect(page.getByRole("heading", { name: "Gerald K Wines", level: 1 })).toBeVisible();
  await expect(page.locator("main")).toContainText("Unidentified major Dallas-area newspaper");
});

test("the adjacent Gerald Wines rows stay distinct and visibly grouped for review", async ({ request }) => {
  const indexed = await publicPerson(request, profiles.geraldWinesIndexed);
  const major = await publicPerson(request, profiles.geraldWinesMajor);
  expect(indexed.person_id).not.toBe(major.person_id);
  expect(indexed.possible_duplicate_group).toBeTruthy();
  expect(indexed.possible_duplicate_group).toBe(major.possible_duplicate_group);
  expect(indexed).toMatchObject({
    identity_status: "probable",
    research_status: "needs_identity_review",
  });
  expect(indexed.immediate_pre_oss_affiliations).toHaveLength(0);
  expect(indexed.last_civilian_pre_service).toHaveLength(0);
  expect(indexed.other_pre_oss_affiliations).toHaveLength(0);
});

test("John H Wilson's conflicting candidate transfers no affiliation", async ({ request }) => {
  const person = await publicPerson(request, profiles.johnHWilson);
  expect(person).toMatchObject({
    identity_status: "conflicting",
    research_status: "conflicting_sources",
  });
  expect(person.immediate_pre_oss_affiliations).toHaveLength(0);
  expect(person.last_civilian_pre_service).toHaveLength(0);
  expect(person.other_pre_oss_affiliations).toHaveLength(0);
  expect(person.claims).toEqual(
    expect.arrayContaining([
      expect.objectContaining({
        claim_confidence: "conflicting",
        publication_status: "conflicting",
      }),
    ]),
  );
});

test("Leonard Wilson is classified as a commissioned naval officer", async ({ request }) => {
  const person = await publicPerson(request, profiles.leonardWilson);
  expect(person).toMatchObject({
    personnel_category: "commissioned_naval_officer",
    commissioned_officer: true,
    research_status: "requires_archival_review",
  });
});

test("Batch 1018 evidence excludes secrets, identifiers, and raw bulk records", () => {
  expect(evidence).not.toMatch(/"serial_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toMatch(/"service_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toContain("NARA_API_KEY");
  expect(evidence).not.toContain("x-api-key");
  expect(evidence).not.toContain("candidate_identifier");
  expect(evidence).not.toContain("bulk_record_ordinal");
  expect(evidence).not.toMatch(/\b[ORW]-?\d{5,9}\b/);
});

test("Batch 1018 coverage totals are public", async ({ request }) => {
  const response = await request.get("./data/stats.json");
  expect(response.ok()).toBeTruthy();
  const stats = await response.json();
  expect(stats).toMatchObject({
    source_rows: 23978,
    person_entities: 23935,
    research_attempted_people: 16752,
    verified_affiliation_people: 1181,
    verified_employer_people: 542,
    archival_review_assessed_people: 15232,
  });
});
