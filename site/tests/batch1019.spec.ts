import fs from "node:fs";
import { expect, test } from "@playwright/test";
import type { APIRequestContext } from "@playwright/test";

const evidence = fs.readFileSync(
  new URL(
    "../../research/evidence-page509-george-p-wing-to-wimon-wiriyawit-review_batch-1019_2026-11-04.json",
    import.meta.url,
  ),
  "utf8",
);

const profiles = {
  kaiWinkelhorn: ["665fece9-5eb8-53a8-bc20-545723aa9f96", "Kai G Winkelhorn"],
  rudolphWinnacker: ["d63344e6-19c8-57a3-b62e-70c2744d4a7d", "Rudolph A Winnacker"],
  thomasWingWo: ["25ff31a3-cb41-5e92-9ec4-cc0084502e4f", "Thomas J Wing Wo"],
  georgeWinner: ["46bca5b6-f8df-50a2-88ba-c8fa2a1fc35f", "George Winner"],
  georgeLWinner: ["ef78a1a7-97e2-5959-80d7-13dfd64429ec", "George L Winner"],
  frankWinterrath: ["3ea8c344-a3cf-5dcf-89ec-40382243e0b5", "Frank J Winterrath"],
  wimonWiriyawit: ["1f71b51b-f7c7-5bd3-8ccf-c5a8e07fde6f", "Wimon Wiriyawit"],
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

test("Batch 1019 publishes every page 509 row with a terminal outcome", async ({ request }) => {
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
        (row: { pdf_page: number }) => row.pdf_page === 509,
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

test("Kai Winkelhorn keeps government assignment and last civilian employer separate", async ({ request, page }) => {
  const person = await publicPerson(request, profiles.kaiWinkelhorn);
  expect(person).toMatchObject({
    identity_status: "high_confidence",
    research_status: "verified_employer_found",
    personnel_category: "commissioned_army_officer",
    commissioned_officer: true,
  });
  expect(person.immediate_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      canonical_organization: "War Production Board",
      relationship_type: "government_assignment",
      claim_confidence: "high",
    }),
  ]);
  expect(person.last_civilian_pre_service).toEqual([
    expect.objectContaining({
      canonical_organization: "Goldman, Sachs & Co.",
      relationship_type: "employment",
      claim_confidence: "high",
    }),
  ]);

  await page.goto(`./people/${profiles.kaiWinkelhorn[0]}/`);
  await expect(page.getByRole("heading", { name: "Kai G Winkelhorn", level: 1 })).toBeVisible();
  await expect(page.locator("main")).toContainText("War Production Board");
  await expect(page.locator("main")).toContainText("Goldman, Sachs & Co.");
});

test("Rudolph Winnacker publishes the Nebraska-to-OSS chronology", async ({ request }) => {
  const person = await publicPerson(request, profiles.rudolphWinnacker);
  expect(person).toMatchObject({
    identity_status: "high_confidence",
    research_status: "verified_employer_found",
  });
  expect(person.immediate_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      canonical_organization: "University of Nebraska",
      relationship_type: "employment",
      temporal_basis: "explicit_immediate",
      claim_confidence: "high",
    }),
  ]);
  expect(person.last_civilian_pre_service).toEqual(person.immediate_pre_oss_affiliations);
  expect(person.other_pre_oss_affiliations).toEqual([
    expect.objectContaining({ canonical_organization: "University of Michigan" }),
  ]);
});

test("Wimon Wiriyawit is a student pathway, not an invented employer", async ({ request }) => {
  const person = await publicPerson(request, profiles.wimonWiriyawit);
  expect(person).toMatchObject({
    identity_status: "high_confidence",
    research_status: "completed",
    personnel_category: "foreign_or_allied_military_personnel",
    commissioned_officer: true,
  });
  expect(person.immediate_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      canonical_organization: "Massachusetts Institute of Technology",
      relationship_type: "student",
      temporal_basis: "explicit_immediate",
    }),
  ]);
  expect(person.last_civilian_pre_service).toHaveLength(0);
  expect(person.other_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      canonical_organization: "Chulalongkorn University",
      relationship_type: "student",
    }),
  ]);
});

test("Frank Winterrath uses the visually verified 891 category", async ({ request }) => {
  const person = await publicPerson(request, profiles.frankWinterrath);
  expect(person).toMatchObject({
    identity_status: "confirmed",
    research_status: "occupation_only_found",
  });
  expect(person.immediate_pre_oss_affiliations).toHaveLength(0);
  expect(person.last_civilian_pre_service).toHaveLength(0);
  expect(person.other_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      canonical_organization: null,
      occupation: "unskilled furnace, smelting, or pouring worker",
      claim_confidence: "medium",
      publication_status: "publish_qualified",
    }),
  ]);
  expect(JSON.stringify(person)).not.toContain("radio or phonograph");
});

test("the adjacent George Winner rows remain separate and visibly grouped", async ({ request }) => {
  const first = await publicPerson(request, profiles.georgeWinner);
  const second = await publicPerson(request, profiles.georgeLWinner);
  expect(first.person_id).not.toBe(second.person_id);
  expect(first.possible_duplicate_group).toBeTruthy();
  expect(first.possible_duplicate_group).toBe(second.possible_duplicate_group);
  expect(first).toMatchObject({
    identity_status: "high_confidence",
    research_status: "occupation_only_found",
  });
  expect(second).toMatchObject({
    identity_status: "probable",
    research_status: "needs_identity_review",
  });
  expect(second.immediate_pre_oss_affiliations).toHaveLength(0);
  expect(second.last_civilian_pre_service).toHaveLength(0);
  expect(second.other_pre_oss_affiliations).toHaveLength(0);
});

test("Thomas Wing Wo's conflicting candidate transfers no affiliation", async ({ request }) => {
  const person = await publicPerson(request, profiles.thomasWingWo);
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

test("Batch 1019 evidence excludes secrets, identifiers, and raw bulk records", () => {
  expect(evidence).not.toMatch(/"serial_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toMatch(/"service_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toContain("NARA_API_KEY");
  expect(evidence).not.toContain("x-api-key");
  expect(evidence).not.toContain("candidate_identifier");
  expect(evidence).not.toContain("bulk_record_ordinal");
  expect(evidence).not.toMatch(/\b[ORW]-?\d{5,9}\b/);
});

test("Batch 1019 coverage totals are public", async ({ request }) => {
  const response = await request.get("./data/stats.json");
  expect(response.ok()).toBeTruthy();
  const stats = await response.json();
  expect(stats).toMatchObject({
    source_rows: 23978,
    person_entities: 23935,
    research_attempted_people: 16797,
    verified_affiliation_people: 1184,
    verified_employer_people: 544,
    archival_review_assessed_people: 15278,
  });
});
