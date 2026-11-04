import fs from "node:fs";
import { expect, test } from "@playwright/test";
import type { APIRequestContext } from "@playwright/test";

const evidence = fs.readFileSync(
  new URL(
    "../../research/evidence-page510-hedwig-wirowski-to-chester-wohlert-review_batch-1020_2026-11-04.json",
    import.meta.url,
  ),
  "utf8",
);

const profiles = {
  jamesWithrow: ["712fe131-fc7a-55be-8b3f-d4922c992f45", "James R Withrow Jr."],
  ottoWittman: ["d800fdf2-10cc-53a8-8ef6-246dfa5b0c2a", "Otto Wittman Jr."],
  peterWludyka: ["30f3b163-8dd2-5926-974e-396efe09a963", "Peter S Wludyka"],
  ernestWisynski: ["f6b3d97c-7a75-504d-8102-c8fe56f5a115", "Ernest J Wisynski"],
  ernestWixynski: ["a5557c77-d03c-5255-b8a3-fc8fd0f51eca", "Ernest J Wixynski"],
  carlWittke: ["9af5653f-b029-5395-a049-f75078a90fca", "Carl F Wittke"],
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

test("Batch 1020 publishes every page 510 row with a terminal outcome", async ({ request }) => {
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
        (row: { pdf_page: number }) => row.pdf_page === 510,
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

test("James Withrow keeps an explicitly recruited civilian employer without an invented end date", async ({ request, page }) => {
  const person = await publicPerson(request, profiles.jamesWithrow);
  expect(person).toMatchObject({
    identity_status: "high_confidence",
    research_status: "verified_employer_found",
    personnel_category: "commissioned_naval_officer",
    commissioned_officer: true,
  });
  expect(person.immediate_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      canonical_organization: "Donovan, Leisure, Newton & Lumbard",
      relationship_type: "employment",
      temporal_basis: "explicit_immediate",
      end_date: null,
    }),
  ]);
  expect(person.last_civilian_pre_service).toEqual(person.immediate_pre_oss_affiliations);

  await page.goto(`./people/${profiles.jamesWithrow[0]}/`);
  await expect(page.getByRole("heading", { name: "James R Withrow Jr.", level: 1 })).toBeVisible();
  await expect(page.locator("main")).toContainText("Donovan, Leisure, Newton & Lumbard");
});

test("Otto Wittman separates the military pathway, last civilian employer, and earlier museum work", async ({ request }) => {
  const person = await publicPerson(request, profiles.ottoWittman);
  expect(person).toMatchObject({
    identity_status: "confirmed",
    research_status: "verified_employer_found",
    personnel_category: "commissioned_army_officer",
  });
  expect(person.immediate_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      canonical_organization: "U.S. Army Air Forces Air Transport Command",
      relationship_type: "military_assignment",
    }),
  ]);
  expect(person.last_civilian_pre_service).toEqual([
    expect.objectContaining({
      canonical_organization: "Portland Art Museum",
      relationship_type: "employment",
    }),
  ]);
  expect(person.other_pre_oss_affiliations).toEqual(
    expect.arrayContaining([
      expect.objectContaining({ canonical_organization: "The Hyde Collection" }),
      expect.objectContaining({ canonical_organization: "Skidmore College" }),
      expect.objectContaining({
        canonical_organization: "William Rockhill Nelson Gallery of Art and Mary Atkins Museum of Fine Arts",
      }),
    ]),
  );
});

test("Peter Wludyka publishes an Army-to-OSS pathway, not a civilian employer", async ({ request }) => {
  const person = await publicPerson(request, profiles.peterWludyka);
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
      temporal_basis: "explicit_immediate",
      end_date: null,
    }),
  ]);
  expect(person.last_civilian_pre_service).toHaveLength(0);
});

test("variant Wisynski and Wixynski rows remain separate and visibly grouped", async ({ request }) => {
  const first = await publicPerson(request, profiles.ernestWisynski);
  const second = await publicPerson(request, profiles.ernestWixynski);
  expect(first.person_id).not.toBe(second.person_id);
  expect(first.possible_duplicate_group).toBeTruthy();
  expect(first.possible_duplicate_group).toBe(second.possible_duplicate_group);
  for (const person of [first, second]) {
    expect(person).toMatchObject({
      identity_status: "unresolved",
      research_status: "requires_archival_review",
    });
    expect(person.immediate_pre_oss_affiliations).toHaveLength(0);
    expect(person.last_civilian_pre_service).toHaveLength(0);
    expect(person.other_pre_oss_affiliations).toHaveLength(0);
  }
});

test("the famous Carl Wittke namesake does not transfer an academic career", async ({ request }) => {
  const person = await publicPerson(request, profiles.carlWittke);
  expect(person).toMatchObject({
    identity_status: "unresolved",
    research_status: "requires_archival_review",
  });
  expect(person.immediate_pre_oss_affiliations).toHaveLength(0);
  expect(person.last_civilian_pre_service).toHaveLength(0);
  expect(person.other_pre_oss_affiliations).toHaveLength(0);
  expect(person.claims).toHaveLength(0);
});

test("Batch 1020 evidence excludes secrets, identifiers, and raw bulk records", () => {
  expect(evidence).not.toMatch(/"serial_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toMatch(/"service_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toContain("NARA_API_KEY");
  expect(evidence).not.toContain("x-api-key");
  expect(evidence).not.toContain("candidate_identifier");
  expect(evidence).not.toContain("bulk_record_ordinal");
  expect(evidence).not.toMatch(/\b[ORW]-?\d{5,9}\b/);
});

test("Batch 1020 coverage totals are public", async ({ request }) => {
  const response = await request.get("./data/stats.json");
  expect(response.ok()).toBeTruthy();
  const stats = await response.json();
  expect(stats).toMatchObject({
    source_rows: 23978,
    person_entities: 23935,
    research_attempted_people: 16842,
    verified_affiliation_people: 1187,
    verified_employer_people: 546,
    archival_review_assessed_people: 15323,
  });
});
